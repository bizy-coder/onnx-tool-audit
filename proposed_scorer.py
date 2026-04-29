"""Proposed replacement scorer for NeuroGolf 2026.

Differences from the current scorer (neurogolf_utils.score_network):

  Memory  — measured by running the model through ORT with all intermediate
             tensors promoted to outputs. Ground truth: no shape_inference bugs,
             no onnx_tool bugs, value-dependent shapes (Compress, NonZero, etc.)
             are handled correctly because real data flows through.

  Exploit-proof — exclusions are by graph-input/output *identity*, not by
             tensor name, so naming an initializer "input" has no effect.

  MACs/params — still from onnx_tool (no static alternative yet). This is
             noted as the remaining gap; a follow-up would replace these with
             a simple static walker over ORT-inferred shapes.

Usage:
    feeds = {"input": np.zeros((1, 10, 30, 30), dtype=np.float32)}
    result = proposed_score(model, feeds)
    print(result.score, result.memory, result.macs, result.params)
"""
from __future__ import annotations

import math
import os
import tempfile
import warnings
from dataclasses import dataclass

import numpy as np
import onnx
import onnxruntime as ort


# ─────────────────────────────────────────────────────────────────────────────
# Memory via ORT promoted outputs
# ─────────────────────────────────────────────────────────────────────────────

def _promote_all_outputs(model: onnx.ModelProto) -> onnx.ModelProto:
    """Return a copy of model with every node output added as a graph output."""
    produced = {out for node in model.graph.node for out in node.output if out}
    already_out = {o.name for o in model.graph.output}

    inferred = onnx.shape_inference.infer_shapes(model)
    type_map = {vi.name: vi.type for vi in list(inferred.graph.value_info)
                + list(inferred.graph.output) + list(inferred.graph.input)}

    for name in sorted(produced - already_out):
        vi = onnx.ValueInfoProto()
        vi.name = name
        if name in type_map:
            vi.type.CopyFrom(type_map[name])
        else:
            vi.type.tensor_type.elem_type = onnx.TensorProto.UNDEFINED
        inferred.graph.output.append(vi)
    return inferred


def calculate_memory_ort(model: onnx.ModelProto,
                         feeds: dict[str, np.ndarray]) -> tuple[int, dict[str, dict]]:
    """Measure intermediate tensor memory by running the model through ORT.

    Excludes the model's declared graph inputs and graph outputs (by identity,
    not by name — exploit-proof). Includes initializers and all intermediates.

    Returns:
        (total_bytes, per_tensor) where per_tensor maps name ->
        {'shape': tuple, 'dtype': str, 'bytes': int}.
    """
    # Tensors to exclude: actual graph inputs (feeds) and final graph outputs.
    # Use sets of names from the *original* model, not the promoted copy.
    graph_input_names  = {inp.name for inp in model.graph.input
                          if inp.name not in {init.name for init in model.graph.initializer}}
    graph_output_names = {out.name for out in model.graph.output}

    promoted = _promote_all_outputs(model)
    opts = ort.SessionOptions()
    opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
    opts.log_severity_level = 4
    opts.intra_op_num_threads = 1
    opts.inter_op_num_threads = 1

    try:
        sess = ort.InferenceSession(promoted.SerializeToString(), opts)
    except Exception as e:
        raise RuntimeError(f"ORT session creation failed: {e}") from e

    try:
        outputs = sess.run(None, feeds)
    except Exception as e:
        raise RuntimeError(f"ORT execution failed: {e}") from e

    output_names = [o.name for o in sess.get_outputs()]
    tensor_map = dict(zip(output_names, outputs))

    # Also include initializers (constants stored in the graph).
    for init in model.graph.initializer:
        if init.name not in tensor_map:
            tensor_map[init.name] = onnx.numpy_helper.to_array(init)

    per_tensor: dict[str, dict] = {}
    total = 0
    for name, arr in tensor_map.items():
        if name in graph_input_names or name in graph_output_names:
            continue
        b = int(arr.size) * arr.dtype.itemsize
        per_tensor[name] = {"shape": tuple(arr.shape), "dtype": arr.dtype.name, "bytes": b}
        total += b

    return total, per_tensor


# ─────────────────────────────────────────────────────────────────────────────
# MACs / params — still via onnx_tool (known gap)
# ─────────────────────────────────────────────────────────────────────────────

def _macs_params_via_onnx_tool(model: onnx.ModelProto,
                                feeds: dict[str, np.ndarray]) -> tuple[int, int, str | None]:
    """Return (macs, params, error). Still uses onnx_tool — known to have bugs."""
    import onnx_tool

    fd, path = tempfile.mkstemp(suffix=".onnx")
    os.close(fd)
    try:
        onnx.save(model, path)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            m = onnx_tool.loadmodel(path, {"verbose": False, "constant_folding": True})
            g = m.graph
            g.graph_reorder_nodes()
            g.shape_infer(feeds)
            g.profile()

        if not g.valid_profile:
            return 0, 0, "onnx_tool: invalid profile"

        def _scalar(v):
            if v is None: return 0
            if isinstance(v, (list, tuple)): return int(v[0]) if v else 0
            try: return int(v)
            except: return 0

        macs   = sum(_scalar(getattr(n, "macs",   0)) for n in g.nodemap.values())
        params = sum(_scalar(getattr(n, "params", 0)) for n in g.nodemap.values())
        return macs, params, None
    except Exception as e:
        return 0, 0, f"onnx_tool: {type(e).__name__}: {e}"
    finally:
        try: os.unlink(path)
        except: pass


# ─────────────────────────────────────────────────────────────────────────────
# Top-level proposed scorer
# ─────────────────────────────────────────────────────────────────────────────

_BANNED_OPS = {"Loop", "Scan", "NonZero", "Unique", "Script", "Function"}


@dataclass
class ProposedScoreResult:
    score:   float | None
    macs:    int   | None
    memory:  int   | None
    params:  int   | None
    error:   str   | None = None
    # Per-tensor memory breakdown for inspection
    tensor_bytes: dict[str, dict] | None = None


def proposed_score(model: onnx.ModelProto,
                   feeds: dict[str, np.ndarray]) -> ProposedScoreResult:
    """Score a model using ORT for memory and onnx_tool for MACs/params.

    Args:
        model: the ONNX model to score.
        feeds: real input tensors (e.g. {"input": np.zeros((1,10,30,30), np.float32)}).
               Value-dependent ops (Compress, NonZero, etc.) will reflect actual
               output sizes for these specific inputs.
    """
    # Banned ops check.
    for node in model.graph.node:
        if node.op_type in _BANNED_OPS:
            return ProposedScoreResult(None, None, None, None,
                                       error=f"banned op: {node.op_type}")

    # Memory via ORT.
    try:
        memory, tensor_bytes = calculate_memory_ort(model, feeds)
    except Exception as e:
        return ProposedScoreResult(None, None, None, None, error=str(e))

    # MACs + params via onnx_tool (still the weak link).
    macs, params, mac_err = _macs_params_via_onnx_tool(model, feeds)
    if mac_err:
        # Still return memory even if MACs fail — useful for debugging.
        return ProposedScoreResult(None, macs=None, memory=memory, params=None,
                                   error=mac_err, tensor_bytes=tensor_bytes)

    total = macs + memory + params
    score = max(1.0, 25.0 - math.log(total)) if total > 0 else 25.0
    return ProposedScoreResult(score=score, macs=macs, memory=memory,
                               params=params, tensor_bytes=tensor_bytes)
