"""Test execution: oracles (ORT, onnx_tool), diff logic, and result reporting."""
from __future__ import annotations

import os
import tempfile
import multiprocessing as mp
import queue as queue_mod
import time
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Callable, Iterable

import numpy as np
import onnx
import onnx_tool
import onnxruntime as ort

from .generators import TestCase, Scenario, generate_single_op
from .profiles import DEFAULT_OPSET, MAX_CASES_PER_OP, get_spec, list_specs

warnings.filterwarnings(
    "ignore",
    message=r"node .* is not registed for profiling.*",
    category=UserWarning,
    module=r"onnx_tool\.node",
)


# ─────────────────────────────────────────────────────────────────────────────
# Oracle results
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class TruthResult:
    tensors: dict[str, np.ndarray]
    initializers: dict[str, np.ndarray]
    error: str | None = None

    def all_tensors(self) -> dict[str, np.ndarray]:
        out = dict(self.initializers)
        out.update(self.tensors)
        return out

    def shape_of(self, name: str) -> tuple[int, ...] | None:
        if name in self.tensors:
            return tuple(self.tensors[name].shape)
        if name in self.initializers:
            return tuple(self.initializers[name].shape)
        return None

    def total_memory_bytes(self) -> int:
        total = 0
        for arr in self.tensors.values():
            total += int(arr.size) * arr.dtype.itemsize
        for arr in self.initializers.values():
            total += int(arr.size) * arr.dtype.itemsize
        return total

@dataclass
class OnnxToolResult:
    tensor_shapes: dict[str, tuple[int, ...]]
    tensor_dtypes: dict[str, str]
    tensor_bytes: dict[str, int]
    node_macs: dict[str, int]
    node_memory: dict[str, int]
    node_params: dict[str, int]
    total_memory: int = 0
    total_macs: int = 0
    total_params: int = 0
    error: str | None = None

@dataclass
class TensorDiff:
    name: str
    bug_class: str
    truth_shape: tuple[int, ...] | None
    truth_dtype: str | None
    truth_bytes: int | None
    claim_shape: tuple[int, ...] | None
    claim_dtype: str | None
    claim_bytes: int | None
    note: str = ""

@dataclass
class DiffResult:
    tensor_diffs: list[TensorDiff] = field(default_factory=list)
    truth_total_bytes: int = 0
    claim_total_bytes: int = 0
    truth_error: str | None = None
    claim_error: str | None = None
    spec_error: str | None = None

    @property
    def has_disagreement(self) -> bool:
        return bool(self.tensor_diffs) or self.truth_error is not None or self.claim_error is not None

# Bug classes
BUG_CLASSES = (
    "missing-tensor", "wrong-shape", "wrong-dtype", "wrong-bytes",
    "scalar-volume", "constant-uncounted",
    "onnx-tool-fails-valid-model", "onnx-tool-timeout-valid-model",
    "scorer-wrong-shape", "scorer-wrong-dtype",
    "scorer-missing-tensor", "scorer-extra-tensor",
    "scorer-memory-undercount", "scorer-memory-overcount",
    "scorer-shape-inference-incomplete", "scorer-rejects-valid-model",
    "ort-timeout", "ort-rejects-checker-valid-model", "invalid-test-case",
)
CONFIRMED_BUG_CLASSES = (
    "missing-tensor", "wrong-shape", "wrong-dtype", "wrong-bytes",
    "scalar-volume", "constant-uncounted", "onnx-tool-fails-valid-model",
    "onnx-tool-timeout-valid-model",
    "scorer-wrong-shape", "scorer-wrong-dtype",
    "scorer-missing-tensor", "scorer-extra-tensor",
    "scorer-memory-undercount", "scorer-memory-overcount",
    "scorer-shape-inference-incomplete", "scorer-rejects-valid-model",
)
NOISE_BUG_CLASSES = ("invalid-test-case",)
ONNXRUNTIME_BUG_CLASSES: tuple[str, ...] = ("ort-timeout", "ort-rejects-checker-valid-model")


# ─────────────────────────────────────────────────────────────────────────────
# Oracles: ORT (ground truth) and onnx_tool (suspect)
# ─────────────────────────────────────────────────────────────────────────────

def _promote_all_outputs(model: onnx.ModelProto) -> onnx.ModelProto:
    produced = {out for node in model.graph.node for out in node.output if out}
    already_out = {o.name for o in model.graph.output}
    if produced <= already_out:
        return model
    inferred = onnx.shape_inference.infer_shapes(model)
    already_out = {o.name for o in inferred.graph.output}
    type_map = {vi.name: vi.type for vi in list(inferred.graph.value_info)
                + list(inferred.graph.output) + list(inferred.graph.input)}
    for name in sorted(produced - already_out):
        vi = onnx.ValueInfoProto()
        vi.name = name
        if name in type_map:
            vi.type.CopyFrom(type_map[name])
        else:
            tt = vi.type.tensor_type
            tt.elem_type = onnx.TensorProto.UNDEFINED
        inferred.graph.output.append(vi)
    return inferred

def run_truth(model: onnx.ModelProto, feeds: dict[str, np.ndarray]) -> TruthResult:
    """Run model with ORT (ground truth)."""
    initializers = {init.name: onnx.numpy_helper.to_array(init) for init in model.graph.initializer}
    feeds = dict(feeds)
    try:
        promoted = _promote_all_outputs(model)
        opts = ort.SessionOptions()
        opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
        opts.log_severity_level = 4
        opts.intra_op_num_threads = 1
        opts.inter_op_num_threads = 1
        sess = ort.InferenceSession(promoted.SerializeToString(), opts)
        outputs = sess.run(None, feeds)
        names = [o.name for o in sess.get_outputs()]
        tensors = {n: a for n, a in zip(names, outputs)}
        return TruthResult(tensors=tensors, initializers=initializers)
    except Exception as e:
        return TruthResult(tensors={}, initializers=initializers, error=f"{type(e).__name__}: {e}")

def run_onnx_tool(model: onnx.ModelProto, feeds: dict[str, np.ndarray]) -> OnnxToolResult:
    """Profile model with onnx_tool."""
    fd, path = tempfile.mkstemp(suffix=".onnx")
    os.close(fd)
    try:
        onnx.save(model, path)
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings(
                    "ignore",
                    message=r"node .* is not registed for profiling.*",
                    category=UserWarning,
                )
                mod = onnx_tool.Model(path)
                mod.graph.shape_infer(feeds)
                mod.graph.profile()
            tensor_shapes, tensor_dtypes, tensor_bytes = {}, {}, {}
            for name, t in mod.graph.tensormap.items():
                shape = getattr(t, "shape", None)
                tensor_shapes[name] = tuple(shape) if shape is not None else ()
                dtype = getattr(t, "dtype", None)
                tensor_dtypes[name] = np.dtype(dtype).name if dtype is not None else "?"
                try:
                    tensor_bytes[name] = int(t.get_memsize())
                except:
                    tensor_bytes[name] = -1

            def _scalar(v) -> int:
                if v is None:
                    return 0
                if isinstance(v, (list, tuple)):
                    return int(v[0]) if v else 0
                try:
                    return int(v)
                except:
                    return 0

            node_macs, node_memory, node_params = {}, {}, {}
            total_macs = total_memory = total_params = 0
            for nname, node in mod.graph.nodemap.items():
                m = _scalar(getattr(node, "macs", 0))
                mem = _scalar(getattr(node, "memory", 0))
                p = _scalar(getattr(node, "params", 0))
                node_macs[nname] = m
                node_memory[nname] = mem
                node_params[nname] = p
                total_macs += m
                total_memory += mem
                total_params += p

            return OnnxToolResult(
                tensor_shapes=tensor_shapes, tensor_dtypes=tensor_dtypes, tensor_bytes=tensor_bytes,
                node_macs=node_macs, node_memory=node_memory, node_params=node_params,
                total_macs=total_macs, total_memory=total_memory, total_params=total_params,
            )
        except Exception as e:
            return OnnxToolResult(
                tensor_shapes={}, tensor_dtypes={}, tensor_bytes={},
                node_macs={}, node_memory={}, node_params={},
                error=f"{type(e).__name__}: {e}",
            )
    finally:
        try:
            os.unlink(path)
        except:
            pass

def _shapes_equal(a: tuple[int, ...] | None, b: tuple[int, ...] | None) -> bool:
    if a is None or b is None:
        return a is b
    return tuple(a) == tuple(b)

def _is_constant_output(model: onnx.ModelProto, tensor_name: str) -> bool:
    for node in model.graph.node:
        if node.op_type == "Constant" and tensor_name in node.output:
            return True
    return False

def _with_relaxed_graph_output_shapes(model: onnx.ModelProto) -> onnx.ModelProto:
    relaxed = onnx.ModelProto()
    relaxed.CopyFrom(model)
    for out in relaxed.graph.output:
        tt = out.type.tensor_type
        if tt.elem_type and not tt.HasField("shape"):
            tt.shape.CopyFrom(onnx.TensorShapeProto())
    return relaxed

def _check_model_error(model: onnx.ModelProto) -> str | None:
    try:
        onnx.checker.check_model(model)
        return None
    except Exception as e:
        first = f"{type(e).__name__}: {e}"
    try:
        onnx.checker.check_model(onnx.shape_inference.infer_shapes(model))
        return None
    except Exception as e:
        second = f"{type(e).__name__}: {e}"
    try:
        onnx.checker.check_model(_with_relaxed_graph_output_shapes(model))
        return None
    except Exception:
        pass
    try:
        inferred = onnx.shape_inference.infer_shapes(model)
        onnx.checker.check_model(_with_relaxed_graph_output_shapes(inferred))
        return None
    except Exception as e:
        return f"{first}; after infer_shapes: {second}; after relaxing graph output shapes: {type(e).__name__}: {e}"

def _diff_scorer(model: onnx.ModelProto, truth: TruthResult,
                 feeds: dict[str, np.ndarray] | None = None) -> list[TensorDiff]:
    """Compare the neurogolf scorer's reported memory to ORT's actual, per tensor.

    The 2026 NeuroGolf scorer measures memory via onnx.shape_inference instead of
    onnx_tool. Diff that path against ORT to find scorer-vs-reality divergences.
    """
    from .scorer import score_via_neurogolf, ort_intermediate_memory

    out: list[TensorDiff] = []
    score = score_via_neurogolf(model)

    # If the scorer rejects but ORT ran cleanly, that's a blocker bug.
    if score.error is not None:
        err = score.error
        bug = "scorer-shape-inference-incomplete" if "shape inference" in err.lower() else "scorer-rejects-valid-model"
        out.append(TensorDiff(
            name="<scorer>", bug_class=bug,
            truth_shape=None, truth_dtype=None, truth_bytes=truth.total_memory_bytes(),
            claim_shape=None, claim_dtype=None, claim_bytes=None,
            note=f"ORT executed cleanly; scorer: {err[:200]}",
        ))
        return out

    # Build ORT per-tensor info: name -> numpy array
    _, ort_per = ort_intermediate_memory(truth.all_tensors(), feeds)
    ort_tensors: dict[str, np.ndarray] = {}
    for src in (feeds or {}, truth.all_tensors()):
        for name, arr in src.items():
            if name not in ort_tensors:
                ort_tensors[name] = arr

    # scorer per-tensor info: name -> {shape, dtype, bytes}
    si_per = score.tensor_bytes or {}

    all_names = set(ort_per) | set(si_per)
    has_diff = False
    for name in sorted(all_names):
        ort_arr = ort_tensors.get(name)
        ort_shape = tuple(ort_arr.shape) if ort_arr is not None else None
        ort_dtype = ort_arr.dtype.name if ort_arr is not None else None
        ort_bytes = (ort_arr.size * ort_arr.dtype.itemsize) if ort_arr is not None else None

        si = si_per.get(name)
        si_shape = tuple(si["shape"]) if si else None
        si_dtype = si["dtype"] if si else None
        si_bytes = si["bytes"] if si else None

        if name in ort_per and name not in si_per:
            bug = "scorer-missing-tensor"
            note = f"shape_inference omits tensor (ORT: shape={ort_shape} dtype={ort_dtype} bytes={ort_bytes})"
        elif name not in ort_per and name in si_per:
            bug = "scorer-extra-tensor"
            note = f"shape_inference counts phantom tensor (SI: shape={si_shape} dtype={si_dtype} bytes={si_bytes})"
        elif ort_shape != si_shape:
            bug = "scorer-wrong-shape"
            note = f"ORT={ort_shape} SI={si_shape}"
        elif ort_dtype != si_dtype:
            bug = "scorer-wrong-dtype"
            note = f"ORT={ort_dtype} SI={si_dtype}"
        else:
            continue  # matches

        has_diff = True
        out.append(TensorDiff(
            name=name, bug_class=bug,
            truth_shape=ort_shape, truth_dtype=ort_dtype, truth_bytes=ort_bytes,
            claim_shape=si_shape, claim_dtype=si_dtype, claim_bytes=si_bytes,
            note=note,
        ))

    # If no per-tensor breakdown but totals differ, fall back to aggregate diff.
    if not has_diff:
        ort_total = sum(ort_per.values())
        if score.memory != ort_total:
            bug = "scorer-memory-undercount" if score.memory < ort_total else "scorer-memory-overcount"
            out.append(TensorDiff(
                name="<scorer-memory>", bug_class=bug,
                truth_shape=None, truth_dtype=None, truth_bytes=ort_total,
                claim_shape=None, claim_dtype=None, claim_bytes=score.memory,
                note=f"scorer={score.memory}B ORT={ort_total}B",
            ))
    return out


def diff_oracles(model: onnx.ModelProto, truth: TruthResult, claim: OnnxToolResult,
                 feeds: dict[str, np.ndarray] | None = None,
                 compare: str = "both") -> DiffResult:
    """Compare oracle outputs and classify disagreements.

    compare: "onnx_tool" — only onnx_tool vs ORT diffs
             "scorer"    — only scorer (onnx.shape_inference) vs ORT diffs
             "both"      — both (default)
    """
    res = DiffResult(
        truth_total_bytes=truth.total_memory_bytes(),
        claim_total_bytes=claim.total_memory,
        truth_error=truth.error,
        claim_error=claim.error,
    )
    if truth.error:
        res.spec_error = _check_model_error(model)
        bug_class = "invalid-test-case" if res.spec_error else "ort-rejects-checker-valid-model"
        res.tensor_diffs.append(TensorDiff(
            name="<model>", bug_class=bug_class,
            truth_shape=None, truth_dtype=None, truth_bytes=None,
            claim_shape=None, claim_dtype=None,
            claim_bytes=claim.total_memory if not claim.error else None,
            note=f"ORT rejected: {truth.error[:200]}",
        ))
        return res
    if claim.error and compare != "scorer":
        res.tensor_diffs.append(TensorDiff(
            name="<model>", bug_class="onnx-tool-fails-valid-model",
            truth_shape=None, truth_dtype=None, truth_bytes=truth.total_memory_bytes(),
            claim_shape=None, claim_dtype=None, claim_bytes=None,
            note=f"ORT executed cleanly; onnx_tool: {claim.error[:200]}",
        ))
        if compare in ("scorer", "both"):
            res.tensor_diffs.extend(_diff_scorer(model, truth, feeds))
        return res

    truth_tensors = truth.all_tensors()

    if compare in ("onnx_tool", "both"):
        all_names = set(truth_tensors.keys()) | set(claim.tensor_shapes.keys())
    else:
        all_names = set()

    for name in sorted(all_names):
        true_arr = truth_tensors.get(name)
        true_shape = tuple(true_arr.shape) if true_arr is not None else None
        true_dtype = true_arr.dtype.name if true_arr is not None else None
        true_bytes = int(true_arr.size) * true_arr.dtype.itemsize if true_arr is not None else None

        claim_shape = claim.tensor_shapes.get(name)
        claim_dtype = claim.tensor_dtypes.get(name)
        claim_bytes = claim.tensor_bytes.get(name)

        if claim_shape is None and true_arr is not None:
            res.tensor_diffs.append(TensorDiff(
                name=name, bug_class="missing-tensor",
                truth_shape=true_shape, truth_dtype=true_dtype, truth_bytes=true_bytes,
                claim_shape=None, claim_dtype=None, claim_bytes=None,
                note="tensor not in onnx_tool.graph.tensormap",
            ))
            continue

        if true_arr is None:
            continue

        bug = None
        note = ""

        if not _shapes_equal(true_shape, claim_shape):
            bug = "wrong-shape"
            note = f"truth={true_shape} claim={claim_shape}"
        elif true_dtype != claim_dtype and not (true_dtype is None or claim_dtype is None):
            bug = "wrong-dtype"
            note = f"truth={true_dtype} claim={claim_dtype}"
        elif true_bytes != claim_bytes:
            if true_arr.shape == () and claim_bytes == 0 and true_bytes and true_bytes > 0:
                bug = "scalar-volume"
                note = f"scalar dropped from accounting (true={true_bytes}B)"
            elif _is_constant_output(model, name) and (claim_bytes is None or claim_bytes == 0):
                bug = "constant-uncounted"
                note = f"Constant output not in memory accounting (true={true_bytes}B)"
            else:
                bug = "wrong-bytes"
                note = f"truth={true_bytes}B claim={claim_bytes}B"

        if bug is not None:
            res.tensor_diffs.append(TensorDiff(
                name=name, bug_class=bug,
                truth_shape=true_shape, truth_dtype=true_dtype, truth_bytes=true_bytes,
                claim_shape=claim_shape, claim_dtype=claim_dtype, claim_bytes=claim_bytes,
                note=note,
            ))

    if compare in ("onnx_tool", "both"):
        for node in model.graph.node:
            if node.op_type != "Constant":
                continue
            node_mem = claim.node_memory.get(node.name, 0)
            for out in node.output:
                if out not in truth_tensors:
                    continue
                true_arr = truth_tensors[out]
                true_b = int(true_arr.size) * true_arr.dtype.itemsize
                tensor_b = claim.tensor_bytes.get(out, 0) or 0
                already_flagged = any(d.name == out for d in res.tensor_diffs)
                if node_mem == 0 and true_b > 0 and not already_flagged:
                    res.tensor_diffs.append(TensorDiff(
                        name=out, bug_class="constant-uncounted",
                        truth_shape=tuple(true_arr.shape), truth_dtype=true_arr.dtype.name, truth_bytes=true_b,
                        claim_shape=claim.tensor_shapes.get(out),
                        claim_dtype=claim.tensor_dtypes.get(out),
                        claim_bytes=tensor_b,
                        note=f"node {node.name} memory=0 ignores produced tensor (true={true_b}B)",
                    ))

    # Compare the new neurogolf scorer's memory path (onnx.shape_inference) against ORT.
    if compare in ("scorer", "both"):
        res.tensor_diffs.extend(_diff_scorer(model, truth, feeds))

    return res


# ─────────────────────────────────────────────────────────────────────────────
# Test case execution
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class CaseResult:
    case: TestCase
    truth: TruthResult | None
    claim: OnnxToolResult | None
    diff: DiffResult | None
    build_error: str | None = None
    timings: dict[str, float] = field(default_factory=dict)

    @property
    def is_invalid_case(self) -> bool:
        return self.diff is not None and self.diff.truth_error is not None

    @property
    def has_disagreement(self) -> bool:
        return self.diff.has_disagreement and not self.is_invalid_case if self.diff is not None else False

@dataclass
class OpReport:
    op: str
    cases: list[CaseResult] = field(default_factory=list)
    notes: str = ""
    timings: dict[str, float] = field(default_factory=dict)

    @property
    def disagreements(self) -> list[CaseResult]:
        return [c for c in self.cases if c.has_disagreement]

    @property
    def invalid_cases(self) -> list[CaseResult]:
        return [c for c in self.cases if c.is_invalid_case]

    @property
    def build_errors(self) -> list[CaseResult]:
        return [c for c in self.cases if c.build_error is not None]

def _run_case_impl(tc: TestCase | Scenario, progress=None, compare: str = "both") -> CaseResult:
    t_case = time.perf_counter()
    timings: dict[str, float] = {}
    if tc.model is None:
        timings["total"] = time.perf_counter() - t_case
        return CaseResult(case=tc, truth=None, claim=None, diff=None,
                          build_error=tc.label, timings=timings)
    if progress:
        progress("ort")
    t = time.perf_counter()
    truth = run_truth(tc.model, tc.feeds)
    timings["ort"] = time.perf_counter() - t
    if truth.error:
        claim = OnnxToolResult(
            tensor_shapes={}, tensor_dtypes={}, tensor_bytes={},
            node_macs={}, node_memory={}, node_params={},
        )
        timings["total"] = time.perf_counter() - t_case
        return CaseResult(case=tc, truth=truth, claim=claim,
                          diff=diff_oracles(tc.model, truth, claim, compare=compare),
                          timings=timings)
    if progress:
        progress("onnx_tool")
    # Skip onnx_tool entirely when only testing the scorer.
    if compare == "scorer":
        claim = OnnxToolResult(
            tensor_shapes={}, tensor_dtypes={}, tensor_bytes={},
            node_macs={}, node_memory={}, node_params={},
        )
    else:
        t = time.perf_counter()
        claim = run_onnx_tool(tc.model, tc.feeds)
        timings["onnx_tool"] = time.perf_counter() - t
    diff = diff_oracles(tc.model, truth, claim, tc.feeds, compare=compare)
    timings["total"] = time.perf_counter() - t_case
    return CaseResult(case=tc, truth=truth, claim=claim, diff=diff, timings=timings)


def _run_case_worker(tc: TestCase | Scenario, q, compare: str = "both") -> None:
    try:
        q.put(("phase", "start"))
        q.put(("result", _run_case_impl(tc, progress=lambda phase: q.put(("phase", phase)), compare=compare)))
    except Exception as e:
        q.put(("result", CaseResult(
            case=tc, truth=None, claim=None, diff=None,
            build_error=f"HARNESS-ERROR: {type(e).__name__}: {e}",
            timings={},
        )))


def _timeout_result(tc: TestCase | Scenario, phase: str, timeout: float) -> CaseResult:
    if phase == "onnx_tool":
        klass = "onnx-tool-timeout-valid-model"
        note = f"onnx_tool did not finish within {timeout:g}s after ORT accepted the model"
    else:
        klass = "ort-timeout"
        note = f"ORT/truth oracle did not finish within {timeout:g}s (phase={phase})"
    diff = DiffResult(tensor_diffs=[TensorDiff(
        name="<model>", bug_class=klass,
        truth_shape=None, truth_dtype=None, truth_bytes=None,
        claim_shape=None, claim_dtype=None, claim_bytes=None,
        note=note,
    )])
    return CaseResult(case=tc, truth=None, claim=None, diff=diff,
                      timings={"total": timeout})


def run_case(tc: TestCase | Scenario, *, timeout: float | None = None,
             compare: str = "both") -> CaseResult:
    """Run a single test case and compare oracles, optionally with a hard timeout.

    compare: "onnx_tool" — only onnx_tool vs ORT
             "scorer"    — only scorer (onnx.shape_inference) vs ORT
             "both"      — both (default)
    """
    if timeout is None or timeout <= 0:
        return _run_case_impl(tc, compare=compare)

    q = mp.Queue(maxsize=1)
    p = mp.Process(target=_run_case_worker, args=(tc, q, compare))
    p.start()
    deadline = time.monotonic() + timeout
    phase = "start"
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        try:
            kind, payload = q.get(timeout=min(0.2, remaining))
        except queue_mod.Empty:
            if not p.is_alive():
                break
            continue
        if kind == "phase":
            phase = payload
            continue
        if kind == "result":
            p.join(2)
            return payload

    if p.is_alive():
        p.terminate()
        p.join(2)
        if p.is_alive():
            p.kill()
            p.join(2)
        return _timeout_result(tc, phase, timeout)

    try:
        kind, payload = q.get_nowait()
        if kind == "result":
            return payload
    except queue_mod.Empty:
        pass
    return CaseResult(
        case=tc, truth=None, claim=None, diff=None,
        build_error=f"HARNESS-ERROR: worker exited without result (exitcode={p.exitcode}, phase={phase})",
        timings={},
    )


CaseCallback = Callable[[OpReport, CaseResult], None]


def run_op(name: str, *, opset: int = DEFAULT_OPSET,
           case_timeout: float | None = None,
           case_limit: int | None = None,
           case_workers: int = 1,
           compare: str = "both",
           on_result: CaseCallback | None = None) -> OpReport:
    """Generate and run all test cases for one operator."""
    spec = get_spec(name, opset=opset)
    t = time.perf_counter()
    cases = generate_single_op(spec, limit=case_limit or MAX_CASES_PER_OP)
    gen_seconds = time.perf_counter() - t
    report = OpReport(op=f"{name}@{spec.opset}", notes=spec.notes)
    report.timings["generate"] = gen_seconds

    t = time.perf_counter()
    if case_workers > 1 and len(cases) > 1:
        with ThreadPoolExecutor(max_workers=case_workers) as pool:
            future_to_tc = {pool.submit(run_case, tc, timeout=case_timeout, compare=compare): tc for tc in cases}
            for future in as_completed(future_to_tc):
                try:
                    res = future.result()
                except Exception as e:
                    tc = future_to_tc[future]
                    res = CaseResult(case=tc, truth=None, claim=None, diff=None,
                                     build_error=f"HARNESS-ERROR: {type(e).__name__}: {e}")
                report.cases.append(res)
                if on_result:
                    on_result(report, res)
    else:
        for tc in cases:
            res = run_case(tc, timeout=case_timeout, compare=compare)
            report.cases.append(res)
            if on_result:
                on_result(report, res)
    report.timings["run"] = time.perf_counter() - t
    report.timings["ort"] = sum(c.timings.get("ort", 0.0) for c in report.cases)
    report.timings["onnx_tool"] = sum(c.timings.get("onnx_tool", 0.0) for c in report.cases)
    report.timings["case_total"] = sum(c.timings.get("total", 0.0) for c in report.cases)
    return report


def _run_op_worker(name: str, opset: int, case_timeout: float | None,
                   case_limit: int | None, case_workers: int, q,
                   compare: str = "both") -> None:
    try:
        q.put(("result", run_op(
            name, opset=opset, case_timeout=case_timeout,
            case_limit=case_limit, case_workers=case_workers,
            compare=compare, on_result=None,
        )))
    except Exception as e:
        report = OpReport(op=f"{name}@{opset}")
        report.cases.append(CaseResult(
            case=TestCase(op=name, label=f"HARNESS-ERROR: {type(e).__name__}: {e}",
                          model=None, feeds={}, input_cases=(), attrs={}),
            truth=None, claim=None, diff=None,
            build_error=f"HARNESS-ERROR: {type(e).__name__}: {e}",
        ))
        q.put(("result", report))


def run_op_with_timeout(name: str, *, opset: int = DEFAULT_OPSET,
                        op_timeout: float | None = None,
                        case_timeout: float | None = None,
                        case_limit: int | None = None,
                        case_workers: int = 1,
                        compare: str = "both") -> OpReport:
    """Run one op in a killable process so a sweep can skip wedged ops."""
    if op_timeout is None or op_timeout <= 0:
        return run_op(name, opset=opset, case_timeout=case_timeout,
                      case_limit=case_limit, case_workers=case_workers, compare=compare)

    q = mp.Queue(maxsize=1)
    p = mp.Process(target=_run_op_worker,
                   args=(name, opset, case_timeout, case_limit, case_workers, q, compare))
    p.start()
    deadline = time.monotonic() + op_timeout
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        try:
            kind, payload = q.get(timeout=min(0.2, remaining))
        except queue_mod.Empty:
            if not p.is_alive():
                break
            continue
        if kind == "result":
            p.join(2)
            return payload

    if p.is_alive():
        p.terminate()
        p.join(2)
        if p.is_alive():
            p.kill()
            p.join(2)
        report = OpReport(op=f"{name}@{opset}", notes=f"op timed out after {op_timeout:g}s")
        report.cases.append(CaseResult(
            case=TestCase(op=name, label=f"OP-TIMEOUT after {op_timeout:g}s",
                          model=None, feeds={}, input_cases=(), attrs={}),
            truth=None, claim=None, diff=None,
            build_error=f"OP-TIMEOUT after {op_timeout:g}s",
            timings={"total": op_timeout},
        ))
        report.timings["run"] = op_timeout
        return report

    try:
        kind, payload = q.get_nowait()
        if kind == "result":
            return payload
    except queue_mod.Empty:
        pass

    report = OpReport(op=f"{name}@{opset}", notes="op worker exited without result")
    report.cases.append(CaseResult(
        case=TestCase(op=name, label="OP-HARNESS-ERROR: worker exited without result",
                      model=None, feeds={}, input_cases=(), attrs={}),
        truth=None, claim=None, diff=None,
        build_error=f"OP-HARNESS-ERROR: worker exited without result (exitcode={p.exitcode})",
    ))
    return report

def run_all(only: Iterable[str] | None = None, *, opset: int = DEFAULT_OPSET,
            case_timeout: float | None = None,
            case_limit: int | None = None,
            compare: str = "both",
            on_result: CaseCallback | None = None) -> list[OpReport]:
    """Generate and run all test cases for multiple operators."""
    reports = []
    for spec in list_specs(only=only, opset=opset):
        reports.append(run_op(spec.name, opset=opset,
                              case_timeout=case_timeout,
                              case_limit=case_limit,
                              compare=compare,
                              on_result=on_result))
    return reports

def run_dag_phase(*, n_random: int = 100, target_nodes: int = 4, opset: int = 11,
                  include_scenarios: bool = True,
                  case_timeout: float | None = None,
                  on_result: CaseCallback | None = None) -> OpReport:
    """Run multi-op DAG scenarios."""
    from .dag_generator import generate_random_dags, generate_specific_scenarios
    cases: list[TestCase | Scenario] = []
    if include_scenarios:
        cases.extend(generate_specific_scenarios(opset=opset))
    cases.extend(generate_random_dags(n_random, target_nodes=target_nodes, opset=opset))

    report = OpReport(op=f"DAG@{opset}",
                      notes=f"Phase 2 multi-op DAGs ({len(cases)} cases: "
                            f"{'scenarios+' if include_scenarios else ''}{n_random} random "
                            f"target_nodes={target_nodes}, opset={opset})")
    for tc in cases:
        res = run_case(tc, timeout=case_timeout)
        report.cases.append(res)
        if on_result:
            on_result(report, res)
    return report

__all__ = [
    "TestCase", "CaseResult", "OpReport", "TensorDiff", "DiffResult",
    "run_case", "run_op", "run_op_with_timeout", "run_all", "run_dag_phase",
    "run_truth", "run_onnx_tool", "diff_oracles",
    "BUG_CLASSES", "CONFIRMED_BUG_CLASSES", "NOISE_BUG_CLASSES",
]
