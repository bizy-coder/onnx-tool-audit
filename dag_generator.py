"""Phase 2: multi-op DAG generator.

Phase 1 (single-op) tests miss bugs that only manifest under data flow between
ops. The canonical example is Compress's `get_numpy()` zero fabrication: when
condition is an initializer, onnx_tool reads the true value; when condition is
the output of another node, onnx_tool fabricates zeros. Single-op tests can
only test the initializer path.

This module generates small DAGs (typically 2-5 nodes) by:
  1. Maintaining a pool of "live" tensor edges (name, shape, dtype, value).
  2. Each step: pick an op whose input requirements can be met by the pool
     plus generated initializers; add the node; advance the pool.
  3. Use ``onnx.shape_inference.infer_shapes`` to recover output shapes for
     edges. (We don't trust onnx_tool's inference — that's what we're testing.
     ONNX's reference inference is sometimes incomplete, in which case we
     fall back to running ORT speculatively.)
  4. Declare the final live edge as the graph output.

The output is a ``TestCase`` (same type as Phase 1) so the existing oracle +
diff machinery just works.

We intentionally keep the generator small and grammar-based rather than
constraint-solver-based (cf. NNSmith's Z3 approach). Our op set is narrow
enough that hand-coded compatibility rules cover it.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

import numpy as np
import onnx
import onnxruntime as ort

from .generators import DTYPE_TABLE, SHAPE_BUCKETS, fill, np_dtype, onnx_dtype, TestCase, Scenario
from .profiles import OpSpec, SPECS


# ---------------------------------------------------------------------------
# Edge: a live tensor in the partial graph
# ---------------------------------------------------------------------------


@dataclass
class Edge:
    name: str
    shape: tuple[int, ...]
    dtype_label: str
    is_input: bool = False     # True if this is a graph input (in feeds)
    is_init: bool = False      # True if this is an initializer

    @property
    def rank(self) -> int:
        return len(self.shape)


# ---------------------------------------------------------------------------
# Compatibility: can op consume edge for a particular port?
# ---------------------------------------------------------------------------


def _port_accepts(port_dtype_labels: tuple[str, ...], edge: Edge) -> bool:
    return edge.dtype_label in port_dtype_labels


def _spec_consumable_inputs(spec: OpSpec):
    """Yield the input ports that must be wired (not initializers)."""
    for p in spec.inputs:
        if not p.is_init:
            yield p


def _spec_init_inputs(spec: OpSpec):
    for p in spec.inputs:
        if p.is_init:
            yield p


# ---------------------------------------------------------------------------
# DAG builder
# ---------------------------------------------------------------------------


# Curated list of ops the multi-op generator may use. Filtered to keep DAGs
# valid by construction: we exclude ops whose specs are too constraint-heavy
# for the simple compatibility logic below (Conv shape rules, Pool, GridSample,
# Quantization, Resize, Reshape with computed shape, etc.). The test harness
# can still test those via Phase 1.
DAG_OP_ALLOWLIST = (
    # unary float
    "Identity", "Relu", "Sigmoid", "Tanh", "Neg", "Abs", "Sqrt",
    "Sign", "Exp", "Log", "Erf", "Reciprocal", "Elu", "LeakyRelu",
    "Softplus", "Floor", "Ceil",
    # unary bool
    "Not",
    # binary broadcast (we'll use only same-shape pairings for simplicity)
    "Add", "Mul", "Sub", "Div", "Pow",
    "Equal", "Greater", "Less", "GreaterOrEqual", "LessOrEqual", "NotEqual",
    "Max", "Min",
    "And", "Or", "Xor",
    # reductions
    "ReduceMax", "ReduceMin", "ReduceMean", "ReduceSum",
    # cast (key for triggering the Compress get_numpy bug)
    "Cast",
    # shape ops with init-only side inputs
    "Transpose",
    # data-dependent inputs from runtime tensor (key bug case)
    "Compress",
    "Where",
)


@dataclass
class DAGCase:
    """Generated DAG plus metadata for shrinking and reporting."""
    decisions: list[tuple[str, dict]] = field(default_factory=list)
    seed: int = 0


def _produce_initializer(name: str, shape, dtype_label: str, fill_label: str = "random",
                         value=None) -> tuple[onnx.TensorProto, np.ndarray]:
    if value is not None:
        arr = np.asarray(value, dtype=np_dtype(dtype_label)).reshape(shape) if shape else np.asarray(value, dtype=np_dtype(dtype_label))
    else:
        arr = fill(fill_label, tuple(shape), np_dtype(dtype_label))
    return onnx.numpy_helper.from_array(arr, name=name), arr


def _node_for(op_name: str, inputs: list[str], outputs: list[str], **attrs):
    return onnx.helper.make_node(op_name, inputs, outputs, **attrs)


def _try_infer(model: onnx.ModelProto) -> dict[str, tuple[tuple[int, ...], int]]:
    """Return name -> (shape, elem_type) from ONNX shape inference, where known."""
    try:
        m = onnx.shape_inference.infer_shapes(model)
    except Exception:
        return {}
    out = {}
    for vi in list(m.graph.value_info) + list(m.graph.output):
        if vi.type.HasField("tensor_type"):
            tt = vi.type.tensor_type
            if not tt.HasField("shape"):
                continue
            shape = tuple(d.dim_value if d.HasField("dim_value") else -1 for d in tt.shape.dim)
            out[vi.name] = (shape, tt.elem_type)
    return out


def _ort_probe_shape(model: onnx.ModelProto, feeds: dict, target_name: str) -> tuple[tuple[int, ...], np.dtype] | None:
    """Run the model with target_name promoted to output; return real shape/dtype."""
    m = onnx.ModelProto()
    m.CopyFrom(model)
    # Promote target to output
    if not any(o.name == target_name for o in m.graph.output):
        vi = onnx.ValueInfoProto()
        vi.name = target_name
        vi.type.tensor_type.elem_type = onnx.TensorProto.FLOAT
        _ = vi.type.tensor_type.shape
        m.graph.output.append(vi)
    try:
        opts = ort.SessionOptions()
        opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
        opts.log_severity_level = 3
        sess = ort.InferenceSession(m.SerializeToString(), opts)
        outs = sess.run([target_name], feeds)
        arr = outs[0]
        return tuple(arr.shape), arr.dtype
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Per-op step builders
# ---------------------------------------------------------------------------
# Each builder takes (rng, frontier, fresh_name) and returns:
#     (op_name, attrs, consumed_edges, produced_edge_template, extra_inits)
# `produced_edge_template` is a dict with at least dtype_label; shape is
# inferred after assembly. `consumed_edges` is the list of frontier edges to
# remove (replaced by produced).


@dataclass
class StepPlan:
    op_name: str
    attrs: dict
    consumed: list[Edge]
    extra_inits: list[onnx.TensorProto]
    extra_init_arrays: dict[str, np.ndarray]
    output_dtype_label: str
    output_name: str


def _plan_unary(rng, frontier: list[Edge], name: str, op_name: str,
                in_dtypes: tuple[str, ...]) -> StepPlan | None:
    candidates = [e for e in frontier if e.dtype_label in in_dtypes]
    if not candidates:
        return None
    e = candidates[rng.integers(len(candidates))]
    out_dtype = e.dtype_label
    return StepPlan(op_name=op_name, attrs={}, consumed=[e], extra_inits=[],
                    extra_init_arrays={}, output_dtype_label=out_dtype, output_name=name)


def _plan_unary_float(rng, frontier, name, op_name):
    return _plan_unary(rng, frontier, name, op_name, ("float32", "float16"))


def _plan_unary_bool(rng, frontier, name, op_name):
    return _plan_unary(rng, frontier, name, op_name, ("bool",))


def _plan_binary_same_shape(rng, frontier, name, op_name,
                            in_dtypes: tuple[str, ...], out_dtype_label: str | None = None):
    # Pick two edges with same shape and same dtype.
    by_key: dict[tuple, list[Edge]] = {}
    for e in frontier:
        if e.dtype_label not in in_dtypes:
            continue
        by_key.setdefault((e.shape, e.dtype_label), []).append(e)
    keys = [k for k, v in by_key.items() if len(v) >= 1]
    if not keys:
        return None
    k = keys[rng.integers(len(keys))]
    pool = by_key[k]
    if len(pool) >= 2:
        a, b = pool[0], pool[1]
    else:
        # Reuse the same edge as both inputs (still a valid DAG; some ops dedupe).
        a = b = pool[0]
    out_dtype = out_dtype_label or a.dtype_label
    return StepPlan(op_name=op_name, attrs={}, consumed=[a, b],
                    extra_inits=[], extra_init_arrays={},
                    output_dtype_label=out_dtype, output_name=name)


def _plan_reduce(rng, frontier, name, op_name):
    candidates = [e for e in frontier if e.dtype_label in ("float32", "float16") and e.rank >= 2]
    if not candidates:
        return None
    e = candidates[rng.integers(len(candidates))]
    axes = (1,) if e.rank > 1 else (0,)
    return StepPlan(op_name=op_name, attrs={"axes": list(axes), "keepdims": 1},
                    consumed=[e], extra_inits=[], extra_init_arrays={},
                    output_dtype_label=e.dtype_label, output_name=name)


def _plan_cast(rng, frontier, name):
    # Cast is the key bug-revealing op: turning float into bool feeds Compress's
    # condition with a runtime tensor.
    candidates = [e for e in frontier if e.dtype_label in ("float32", "float16", "int32", "int64", "bool")]
    if not candidates:
        return None
    e = candidates[rng.integers(len(candidates))]
    # Pick a random target dtype; favor BOOL for downstream Compress/Where.
    targets = ["bool", "float32", "int32", "int64"]
    target = targets[rng.integers(len(targets))]
    onnx_to = onnx_dtype(target)
    return StepPlan(op_name="Cast", attrs={"to": onnx_to},
                    consumed=[e], extra_inits=[], extra_init_arrays={},
                    output_dtype_label=target, output_name=name)


def _plan_compress(rng, frontier, name):
    # X must be rank>=1 numeric; condition must be a 1-D bool tensor with the
    # right length. We pick condition from the frontier (runtime-computed)
    # since that's what the bug needs — the static-init path is covered by
    # Phase 1.
    x_candidates = [e for e in frontier
                    if e.rank >= 1 and e.dtype_label in ("float32", "float16", "int32", "int64")]
    if not x_candidates:
        return None
    x = x_candidates[rng.integers(len(x_candidates))]
    axis = int(rng.integers(x.rank))
    target_len = x.shape[axis]
    if target_len < 1:
        return None
    # Look for a bool 1-D edge with shape (target_len,).
    cond_candidates = [e for e in frontier
                       if e.dtype_label == "bool" and e.shape == (target_len,)]
    if not cond_candidates:
        return None
    cond = cond_candidates[rng.integers(len(cond_candidates))]
    return StepPlan(op_name="Compress", attrs={"axis": axis},
                    consumed=[x, cond], extra_inits=[], extra_init_arrays={},
                    output_dtype_label=x.dtype_label, output_name=name)


def _plan_where(rng, frontier, name):
    cond_candidates = [e for e in frontier if e.dtype_label == "bool"]
    if not cond_candidates:
        return None
    cond = cond_candidates[rng.integers(len(cond_candidates))]
    # Pick X and Y with matching numeric dtype, same shape if possible.
    pairs = []
    for e1 in frontier:
        if e1.dtype_label not in ("float32", "float16", "int32", "int64"):
            continue
        for e2 in frontier:
            if e2.dtype_label != e1.dtype_label or e2.shape != e1.shape:
                continue
            pairs.append((e1, e2))
    if not pairs:
        return None
    x, y = pairs[rng.integers(len(pairs))]
    # Skip combos with broadcast-incompatible cond.
    try:
        np.broadcast_shapes(cond.shape, x.shape, y.shape)
    except ValueError:
        return None
    return StepPlan(op_name="Where", attrs={},
                    consumed=[cond, x, y], extra_inits=[], extra_init_arrays={},
                    output_dtype_label=x.dtype_label, output_name=name)


def _plan_transpose(rng, frontier, name):
    candidates = [e for e in frontier if e.rank == 4]
    if not candidates:
        return None
    e = candidates[rng.integers(len(candidates))]
    perms = [[0, 1, 3, 2], [0, 2, 1, 3]]
    perm = perms[rng.integers(len(perms))]
    return StepPlan(op_name="Transpose", attrs={"perm": perm},
                    consumed=[e], extra_inits=[], extra_init_arrays={},
                    output_dtype_label=e.dtype_label, output_name=name)


# Dispatch table mapping op_name -> planner
PLANNERS = {
    "Identity": lambda r, f, n: _plan_unary(r, f, n, "Identity",
                                            ("float32", "float16", "int32", "int64", "bool")),
    "Relu":       lambda r, f, n: _plan_unary_float(r, f, n, "Relu"),
    "Sigmoid":    lambda r, f, n: _plan_unary_float(r, f, n, "Sigmoid"),
    "Tanh":       lambda r, f, n: _plan_unary_float(r, f, n, "Tanh"),
    "Neg":        lambda r, f, n: _plan_unary(r, f, n, "Neg", ("float32", "int32")),
    "Abs":        lambda r, f, n: _plan_unary(r, f, n, "Abs", ("float32", "int32")),
    "Sqrt":       lambda r, f, n: _plan_unary_float(r, f, n, "Sqrt"),
    "Sign":       lambda r, f, n: _plan_unary(r, f, n, "Sign", ("float32", "int32")),
    "Exp":        lambda r, f, n: _plan_unary_float(r, f, n, "Exp"),
    "Log":        lambda r, f, n: _plan_unary_float(r, f, n, "Log"),
    "Erf":        lambda r, f, n: _plan_unary_float(r, f, n, "Erf"),
    "Reciprocal": lambda r, f, n: _plan_unary_float(r, f, n, "Reciprocal"),
    "Elu":        lambda r, f, n: _plan_unary_float(r, f, n, "Elu"),
    "LeakyRelu":  lambda r, f, n: _plan_unary_float(r, f, n, "LeakyRelu"),
    "Softplus":   lambda r, f, n: _plan_unary_float(r, f, n, "Softplus"),
    "Floor":      lambda r, f, n: _plan_unary_float(r, f, n, "Floor"),
    "Ceil":       lambda r, f, n: _plan_unary_float(r, f, n, "Ceil"),
    "Not":        lambda r, f, n: _plan_unary_bool(r, f, n, "Not"),

    "Add": lambda r, f, n: _plan_binary_same_shape(r, f, n, "Add", ("float32", "int32")),
    "Mul": lambda r, f, n: _plan_binary_same_shape(r, f, n, "Mul", ("float32", "int32")),
    "Sub": lambda r, f, n: _plan_binary_same_shape(r, f, n, "Sub", ("float32", "int32")),
    "Div": lambda r, f, n: _plan_binary_same_shape(r, f, n, "Div", ("float32",)),
    "Pow": lambda r, f, n: _plan_binary_same_shape(r, f, n, "Pow", ("float32",)),
    "Equal":          lambda r, f, n: _plan_binary_same_shape(r, f, n, "Equal", ("float32", "int32"), "bool"),
    "Greater":        lambda r, f, n: _plan_binary_same_shape(r, f, n, "Greater", ("float32", "int32"), "bool"),
    "Less":           lambda r, f, n: _plan_binary_same_shape(r, f, n, "Less", ("float32", "int32"), "bool"),
    "GreaterOrEqual": lambda r, f, n: _plan_binary_same_shape(r, f, n, "GreaterOrEqual", ("float32",), "bool"),
    "LessOrEqual":    lambda r, f, n: _plan_binary_same_shape(r, f, n, "LessOrEqual", ("float32",), "bool"),
    "NotEqual":       lambda r, f, n: _plan_binary_same_shape(r, f, n, "NotEqual", ("float32", "int32"), "bool"),
    "Max": lambda r, f, n: _plan_binary_same_shape(r, f, n, "Max", ("float32",)),
    "Min": lambda r, f, n: _plan_binary_same_shape(r, f, n, "Min", ("float32",)),
    "And": lambda r, f, n: _plan_binary_same_shape(r, f, n, "And", ("bool",)),
    "Or":  lambda r, f, n: _plan_binary_same_shape(r, f, n, "Or",  ("bool",)),
    "Xor": lambda r, f, n: _plan_binary_same_shape(r, f, n, "Xor", ("bool",)),

    "ReduceMax":  lambda r, f, n: _plan_reduce(r, f, n, "ReduceMax"),
    "ReduceMin":  lambda r, f, n: _plan_reduce(r, f, n, "ReduceMin"),
    "ReduceSum":  lambda r, f, n: _plan_reduce(r, f, n, "ReduceSum"),
    "ReduceMean": lambda r, f, n: _plan_reduce(r, f, n, "ReduceMean"),

    "Cast":      _plan_cast,
    "Compress":  _plan_compress,
    "Where":     _plan_where,
    "Transpose": _plan_transpose,
}


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------


def _seed_inputs(rng) -> tuple[list[Edge], dict[str, np.ndarray]]:
    """Initialize the frontier with a couple of graph inputs.

    We add:
      - `x_main` : (1,10,30,30) float32 — the canonical NeuroGolf shape
      - `x_idx`  : (10,) bool — a 1D bool that pairs with axis-1 Compress
      - `x_row`  : (30,) bool — a 1D bool that pairs with axis-2 / axis-3 Compress
    """
    edges, feeds = [], {}
    main = fill("random", (1, 10, 30, 30), np.float32)
    feeds["x_main"] = main
    edges.append(Edge("x_main", (1, 10, 30, 30), "float32", is_input=True))

    bool10 = fill("alternating", (10,), np.bool_)
    feeds["x_idx"] = bool10
    edges.append(Edge("x_idx", (10,), "bool", is_input=True))

    bool30 = fill("alternating", (30,), np.bool_)
    feeds["x_row"] = bool30
    edges.append(Edge("x_row", (30,), "bool", is_input=True))

    return edges, feeds


def generate_dag(seed: int, *, target_nodes: int = 4, opset: int = 11,
                 op_filter: Iterable[str] | None = None) -> TestCase | None:
    """Generate one random DAG with up to ``target_nodes`` nodes.

    Returns None if no valid DAG could be assembled (e.g. all planners failed
    on the initial frontier).
    """
    rng = np.random.default_rng(seed)
    frontier, feeds = _seed_inputs(rng)
    initializers: list[onnx.TensorProto] = []

    # Build the graph proto incrementally so we can run shape_inference at
    # any point to backfill output shapes.
    nodes: list[onnx.NodeProto] = []
    decisions: list[tuple[str, dict]] = []

    allowed = list(op_filter) if op_filter else list(DAG_OP_ALLOWLIST)

    def fresh_name() -> str:
        return f"v{len(nodes)}"

    for step in range(target_nodes):
        rng.shuffle(allowed)
        plan: StepPlan | None = None
        for op_name in allowed:
            planner = PLANNERS.get(op_name)
            if planner is None:
                continue
            p = planner(rng, frontier, fresh_name())
            if p is not None:
                plan = p
                break
        if plan is None:
            break

        # Append the node
        node = _node_for(plan.op_name,
                         inputs=[c.name for c in plan.consumed],
                         outputs=[plan.output_name],
                         **plan.attrs)
        nodes.append(node)
        initializers.extend(plan.extra_inits)
        feeds.update(plan.extra_init_arrays)
        decisions.append((plan.op_name, plan.attrs))

        # Build a *speculative* model and infer the new edge's shape via ORT
        # (truth-grade). We feed real inputs so all dynamic shape paths resolve.
        graph_inputs = [
            onnx.helper.make_tensor_value_info(e.name, onnx_dtype(e.dtype_label), list(e.shape))
            for e in frontier if e.is_input
        ]
        # Anything in feeds but not in `frontier` is a graph_input that has
        # already been consumed earlier in the chain — keep it as input so
        # the model is closed.
        feed_names = {gi.name for gi in graph_inputs}
        for fname in feeds.keys():
            if fname not in feed_names and not any(init.name == fname for init in initializers):
                graph_inputs.append(onnx.helper.make_tensor_value_info(
                    fname, onnx_dtype("float32"), list(feeds[fname].shape)))
                feed_names.add(fname)
        # Output (placeholder)
        out_vi = onnx.helper.make_tensor_value_info(
            plan.output_name, onnx_dtype(plan.output_dtype_label), None)
        g = onnx.helper.make_graph(nodes, f"dag_{seed}", graph_inputs,
                                   [out_vi], initializer=initializers)
        m = onnx.helper.make_model(g, opset_imports=[onnx.helper.make_opsetid("", opset)])
        m.ir_version = 10

        probe = _ort_probe_shape(m, feeds, plan.output_name)
        if probe is None:
            # The speculative graph couldn't be executed; back up one step.
            nodes.pop()
            decisions.pop()
            continue
        out_shape, out_np_dtype = probe
        out_dtype_label = next((k for k, (n, _) in DTYPE_TABLE.items() if n == out_np_dtype), plan.output_dtype_label)

        # Update frontier: remove consumed (only if no other unconsumed node
        # still references them); add the produced edge.
        # For simplicity we treat consumed edges as "still alive" (DAG can fan
        # out). This matches reality — multiple ops can reuse the same edge.
        produced = Edge(name=plan.output_name, shape=out_shape,
                        dtype_label=out_dtype_label)
        frontier.append(produced)

    if not nodes:
        return None

    # Final assembly: the last produced edge becomes the graph output.
    final = frontier[-1]
    graph_inputs = []
    seen = set()
    for fname, arr in feeds.items():
        if fname in seen:
            continue
        seen.add(fname)
        np_dt = arr.dtype
        dtype_label = next((k for k, (n, _) in DTYPE_TABLE.items() if n == np_dt), "float32")
        graph_inputs.append(onnx.helper.make_tensor_value_info(
            fname, onnx_dtype(dtype_label), list(arr.shape)))
    out_vi = onnx.helper.make_tensor_value_info(
        final.name, onnx_dtype(final.dtype_label), list(final.shape))
    g = onnx.helper.make_graph(nodes, f"dag_{seed}", graph_inputs,
                               [out_vi], initializer=initializers)
    m = onnx.helper.make_model(g, opset_imports=[onnx.helper.make_opsetid("", opset)])
    m.ir_version = 10

    label = " -> ".join(d[0] for d in decisions)
    return TestCase(
        op=f"DAG[{len(nodes)}]",
        label=f"opset={opset} | seed={seed} | {label}",
        model=m, feeds=feeds, input_cases=(), attrs={},
    )


def generate_batch(n: int, *, seed_start: int = 0,
                   target_nodes: int = 4, opset: int = 11) -> list[TestCase]:
    out = []
    for s in range(seed_start, seed_start + n):
        tc = generate_dag(s, target_nodes=target_nodes, opset=opset)
        if tc is not None:
            out.append(tc)
    return out


# ---------------------------------------------------------------------------
# Scenario generator: explicit bug-targeted op sequences
# ---------------------------------------------------------------------------
# Random DAG generation finds *some* bugs but is poor at exercising specific
# patterns (e.g. Cast(bool) -> Compress fires the get_numpy zero-fabrication
# bug). Scenarios are hand-written sequences that we know hit specific bugs.
# Each scenario asserts a specific invariant: which op consumes which.


def _build_scenario_compress_runtime_cond(opset: int = 11) -> TestCase:
    """Cast a float input to bool, then feed it to Compress as condition.

    This is the canonical pattern that reveals onnx_tool's get_numpy()
    zero-fabrication bug: when condition is a runtime tensor (not an init),
    onnx_tool can't read its value, so it fabricates zeros and infers an
    empty (zero-length) output — which propagates downstream.
    """
    # We'll cast a (10,) float input to (10,) bool, then Compress axis=1 on x_main.
    x_main = fill("random", (1, 10, 30, 30), np.float32)
    x_idx_float = fill("alternating", (10,), np.float32)
    feeds = {"x_main": x_main, "x_idx_float": x_idx_float}

    nodes = []
    # Cast x_idx_float -> bool
    nodes.append(_node_for("Cast", ["x_idx_float"], ["cond"], to=onnx.TensorProto.BOOL))
    # Compress x_main with that bool condition along axis 1
    nodes.append(_node_for("Compress", ["x_main", "cond"], ["out"], axis=1))

    g = onnx.helper.make_graph(
        nodes, "compress_runtime_cond",
        inputs=[
            onnx.helper.make_tensor_value_info("x_main", onnx.TensorProto.FLOAT, [1, 10, 30, 30]),
            onnx.helper.make_tensor_value_info("x_idx_float", onnx.TensorProto.FLOAT, [10]),
        ],
        outputs=[
            onnx.helper.make_tensor_value_info("out", onnx.TensorProto.FLOAT, None),
        ],
    )
    m = onnx.helper.make_model(g, opset_imports=[onnx.helper.make_opsetid("", opset)])
    m.ir_version = 10
    return TestCase(op="DAG-scenario", label=f"opset={opset} | Cast(bool) -> Compress[axis=1]",
                    model=m, feeds=feeds, input_cases=(), attrs={})


def _build_scenario_where_runtime_cond(opset: int = 11) -> TestCase:
    """Cast a float input to bool, then feed it to Where.

    Where's _max_shape bug fires regardless of init-vs-runtime, but using a
    runtime cond stresses the propagation path through one extra hop.
    """
    x_main = fill("random", (1, 10, 9, 9), np.float32)
    x_thresh = fill("random", (1, 1, 9, 9), np.float32)
    x_y = fill("zeros", (1, 10, 9, 9), np.float32)
    feeds = {"x_main": x_main, "x_thresh": x_thresh, "x_y": x_y}

    nodes = []
    nodes.append(_node_for("Greater", ["x_main", "x_thresh"], ["cond"]))
    nodes.append(_node_for("Where", ["cond", "x_main", "x_y"], ["out"]))

    g = onnx.helper.make_graph(
        nodes, "where_runtime_cond",
        inputs=[
            onnx.helper.make_tensor_value_info("x_main", onnx.TensorProto.FLOAT, [1, 10, 9, 9]),
            onnx.helper.make_tensor_value_info("x_thresh", onnx.TensorProto.FLOAT, [1, 1, 9, 9]),
            onnx.helper.make_tensor_value_info("x_y", onnx.TensorProto.FLOAT, [1, 10, 9, 9]),
        ],
        outputs=[
            onnx.helper.make_tensor_value_info("out", onnx.TensorProto.FLOAT, None),
        ],
    )
    m = onnx.helper.make_model(g, opset_imports=[onnx.helper.make_opsetid("", opset)])
    m.ir_version = 10
    return TestCase(op="DAG-scenario", label=f"opset={opset} | Greater -> Where (runtime cond)",
                    model=m, feeds=feeds, input_cases=(), attrs={})


def _build_scenario_constant_then_consume(opset: int = 11) -> TestCase:
    """Constant -> Add: a Constant feeding a downstream op.

    Tests whether onnx_tool counts the Constant's output when it's actually
    consumed (vs. being a dead leaf). The constant-uncounted bug should fire
    here too if the per-tensor accounting is consistent.
    """
    x_main = fill("random", (1, 10, 30, 30), np.float32)
    feeds = {"x_main": x_main}

    nodes = []
    const_val = onnx.numpy_helper.from_array(
        np.ones((1, 10, 30, 30), dtype=np.float32), name="const_tensor")
    nodes.append(onnx.helper.make_node("Constant", [], ["c"], value=const_val))
    nodes.append(_node_for("Add", ["x_main", "c"], ["out"]))

    g = onnx.helper.make_graph(
        nodes, "constant_then_add",
        inputs=[onnx.helper.make_tensor_value_info("x_main", onnx.TensorProto.FLOAT, [1, 10, 30, 30])],
        outputs=[onnx.helper.make_tensor_value_info("out", onnx.TensorProto.FLOAT, None)],
    )
    m = onnx.helper.make_model(g, opset_imports=[onnx.helper.make_opsetid("", opset)])
    m.ir_version = 10
    return TestCase(op="DAG-scenario", label=f"opset={opset} | Constant -> Add",
                    model=m, feeds=feeds, input_cases=(), attrs={})


def _build_scenario_reduce_then_broadcast(opset: int = 11) -> TestCase:
    """ReduceMax -> Add: reduction output broadcasts back. Stresses the
    interaction between reduction shape inference and downstream broadcast.
    """
    x_main = fill("random", (1, 10, 30, 30), np.float32)
    x_other = fill("random", (1, 10, 1, 1), np.float32)
    feeds = {"x_main": x_main, "x_other": x_other}

    nodes = []
    nodes.append(_node_for("ReduceMax", ["x_main"], ["reduced"], axes=[2, 3], keepdims=1))
    nodes.append(_node_for("Add", ["reduced", "x_other"], ["out"]))

    g = onnx.helper.make_graph(
        nodes, "reduce_then_broadcast",
        inputs=[
            onnx.helper.make_tensor_value_info("x_main", onnx.TensorProto.FLOAT, [1, 10, 30, 30]),
            onnx.helper.make_tensor_value_info("x_other", onnx.TensorProto.FLOAT, [1, 10, 1, 1]),
        ],
        outputs=[onnx.helper.make_tensor_value_info("out", onnx.TensorProto.FLOAT, None)],
    )
    m = onnx.helper.make_model(g, opset_imports=[onnx.helper.make_opsetid("", opset)])
    m.ir_version = 10
    return TestCase(op="DAG-scenario", label=f"opset={opset} | ReduceMax -> Add",
                    model=m, feeds=feeds, input_cases=(), attrs={})


SCENARIOS = [
    _build_scenario_compress_runtime_cond,
    _build_scenario_where_runtime_cond,
    _build_scenario_constant_then_consume,
    _build_scenario_reduce_then_broadcast,
]


def generate_scenarios(*, opset: int = 11) -> list[TestCase]:
    return [fn(opset) for fn in SCENARIOS]


# Aliases for the new generator interface
def generate_random_dags(n: int, *, target_nodes: int = 4, opset: int = 11) -> list[TestCase]:
    """Generate n random multi-op DAGs."""
    return generate_batch(n, target_nodes=target_nodes, opset=opset)

def generate_specific_scenarios(*, opset: int = 11) -> list[TestCase]:
    """Generate hand-crafted test scenarios."""
    return generate_scenarios(opset=opset)

__all__ = ["generate_dag", "generate_batch", "generate_scenarios",
           "generate_random_dags", "generate_specific_scenarios",
           "DAG_OP_ALLOWLIST", "SCENARIOS"]
