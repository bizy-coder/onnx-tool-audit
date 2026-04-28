"""Test case generation: shapes, dtypes, fills, and case expansion."""
from __future__ import annotations

import itertools
import math
from dataclasses import dataclass

import numpy as np
import onnx

from .profiles import MAX_CASES_PER_OP, AttrSpec, OpSpec, SPECS


# ─────────────────────────────────────────────────────────────────────────────
# Shape and dtype tables
# ─────────────────────────────────────────────────────────────────────────────

SHAPE_BUCKETS = {
    "BCHW": (1, 10, 30, 30),
    "B-C-1-1": (1, 10, 1, 1),
    "B-1-H-W": (1, 1, 30, 30),
    "B-1-H-1": (1, 1, 30, 1),
    "B-1-1-W": (1, 1, 1, 30),
    "B-1-1-1": (1, 1, 1, 1),
    "BCHW-9": (1, 10, 9, 9),
    "B-1-9-9": (1, 1, 9, 9),
    "BCHW-5": (1, 10, 5, 5),
    "BCHW-asym": (1, 10, 9, 30),
    "scalar": (),
    "1d-1": (1,),
    "1d-9": (9,),
    "1d-10": (10,),
    "1d-30": (30,),
    "2d": (1, 10),
    "3d": (1, 10, 30),
    "BCHW-tiny": (1, 1, 1, 30),
    "BCHW-batchN": (2, 10, 30, 30),
}

DTYPE_TABLE = {
    "float32": (np.dtype(np.float32), onnx.TensorProto.FLOAT),
    "float16": (np.dtype(np.float16), onnx.TensorProto.FLOAT16),
    "float64": (np.dtype(np.float64), onnx.TensorProto.DOUBLE),
    "int8": (np.dtype(np.int8), onnx.TensorProto.INT8),
    "int16": (np.dtype(np.int16), onnx.TensorProto.INT16),
    "int32": (np.dtype(np.int32), onnx.TensorProto.INT32),
    "int64": (np.dtype(np.int64), onnx.TensorProto.INT64),
    "uint8": (np.dtype(np.uint8), onnx.TensorProto.UINT8),
    "uint16": (np.dtype(np.uint16), onnx.TensorProto.UINT16),
    "uint32": (np.dtype(np.uint32), onnx.TensorProto.UINT32),
    "uint64": (np.dtype(np.uint64), onnx.TensorProto.UINT64),
    "bool": (np.dtype(np.bool_), onnx.TensorProto.BOOL),
    "bfloat16": (np.dtype(np.float32), onnx.TensorProto.BFLOAT16),  # bfloat16 not in numpy, use float32 as proxy
}

def np_dtype(name: str) -> np.dtype:
    return DTYPE_TABLE[name][0]

def onnx_dtype(name: str) -> int:
    return DTYPE_TABLE[name][1]


# ─────────────────────────────────────────────────────────────────────────────
# Fill functions
# ─────────────────────────────────────────────────────────────────────────────

def _is_float(dt: np.dtype) -> bool:
    return np.issubdtype(dt, np.floating)

def _is_int(dt: np.dtype) -> bool:
    return np.issubdtype(dt, np.integer)

def _is_bool(dt: np.dtype) -> bool:
    return dt == np.bool_

def _safe_size(shape: tuple[int, ...]) -> int:
    return max(1, int(np.prod(shape))) if shape else 1

def fill_zeros(shape, dtype):
    return np.zeros(shape, dtype=dtype)

def fill_ones(shape, dtype):
    return np.ones(shape, dtype=dtype)

def fill_sequential(shape, dtype):
    n = _safe_size(shape)
    if _is_bool(dtype):
        flat = (np.arange(n) % 2 == 0)
    elif _is_int(dtype):
        info = np.iinfo(dtype)
        flat = (np.arange(n) % min(info.max, 100)).astype(dtype)
    else:
        flat = (np.arange(n) / max(n, 1)).astype(dtype)
    return flat.reshape(shape).astype(dtype, copy=False)

def fill_random_uniform(shape, dtype, *, seed: int = 0):
    rng = np.random.default_rng(seed)
    n = _safe_size(shape)
    if _is_bool(dtype):
        flat = rng.integers(0, 2, size=n).astype(np.bool_)
    elif _is_int(dtype):
        info = np.iinfo(dtype)
        lo, hi = max(info.min, -10), min(info.max, 10)
        flat = rng.integers(lo, hi + 1, size=n).astype(dtype)
    else:
        flat = rng.uniform(-1, 1, size=n).astype(dtype)
    return flat.reshape(shape).astype(dtype, copy=False)

def fill_sparse(shape, dtype, *, density: float = 0.1, seed: int = 1):
    rng = np.random.default_rng(seed)
    n = _safe_size(shape)
    mask = rng.random(n) < density
    flat = mask.astype(dtype)
    return flat.reshape(shape).astype(dtype, copy=False)

def fill_one_hot_per_channel(shape, dtype):
    arr = np.zeros(shape, dtype=dtype)
    if len(shape) >= 2 and shape[1] >= 1:
        for c in range(shape[1]):
            idx = (0,) * 1 + (c,) + (0,) * (len(shape) - 2)
            arr[idx] = 1
    return arr

def fill_edges(shape, dtype):
    n = _safe_size(shape)
    if _is_float(dtype):
        candidates = np.array(
            [0.0, 1.0, -1.0, np.finfo(dtype).max, np.finfo(dtype).min, np.nan, np.inf, -np.inf],
            dtype=dtype,
        )
    elif _is_int(dtype):
        info = np.iinfo(dtype)
        candidates = np.array([0, 1, -1 if info.min < 0 else 0, info.max, info.min], dtype=dtype)
    elif _is_bool(dtype):
        candidates = np.array([True, False], dtype=np.bool_)
    else:
        candidates = np.zeros(1, dtype=dtype)
    flat = np.tile(candidates, (n // len(candidates) + 1))[:n].astype(dtype)
    return flat.reshape(shape).astype(dtype, copy=False)

def fill_all_true(shape, dtype):
    return np.ones(shape, dtype=dtype)

def fill_all_false(shape, dtype):
    return np.zeros(shape, dtype=dtype)

def fill_alternating(shape, dtype):
    n = _safe_size(shape)
    flat = (np.arange(n) % 2 == 0).astype(dtype)
    return flat.reshape(shape).astype(dtype, copy=False)

FILL_FNS = {
    "zeros": fill_zeros,
    "ones": fill_ones,
    "sequential": fill_sequential,
    "random": fill_random_uniform,
    "sparse": fill_sparse,
    "onehot": fill_one_hot_per_channel,
    "edges": fill_edges,
    "all_true": fill_all_true,
    "all_false": fill_all_false,
    "alternating": fill_alternating,
}

def fill(name: str, shape: tuple[int, ...], dtype: np.dtype) -> np.ndarray:
    return FILL_FNS[name](shape, dtype)


# ─────────────────────────────────────────────────────────────────────────────
# Input cases
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class InputCase:
    name: str
    shape_label: str
    shape: tuple[int, ...]
    dtype_label: str
    fill_label: str
    is_init: bool

    @property
    def np_dtype(self) -> np.dtype:
        return DTYPE_TABLE[self.dtype_label][0]

    @property
    def onnx_dtype(self) -> int:
        return DTYPE_TABLE[self.dtype_label][1]

    def materialize(self) -> np.ndarray:
        return FILL_FNS[self.fill_label](self.shape, self.np_dtype)

    def label(self) -> str:
        kind = "init" if self.is_init else "input"
        return f"{self.name}({kind})={self.shape_label}/{self.dtype_label}/{self.fill_label}"


def _tensor_value(dtype_label: str = "float32", shape: tuple[int, ...] = ()) -> onnx.TensorProto:
    arr = np.asarray(1, dtype=np_dtype(dtype_label)).reshape(shape)
    return onnx.numpy_helper.from_array(arr, name="attr_value")


# ─────────────────────────────────────────────────────────────────────────────
# Test case building
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class TestCase:
    op: str
    label: str
    model: onnx.ModelProto
    feeds: dict[str, np.ndarray]
    input_cases: tuple[InputCase, ...]
    attrs: dict[str, object]

@dataclass
class Scenario(TestCase):
    """Multi-op scenario (DAG test case)."""
    pass


def _apply_input_constraints(spec: OpSpec, input_cases: tuple[InputCase, ...], attrs: dict) -> tuple[InputCase, ...]:
    """Apply op-specific constraints to input cases."""
    # Compress: condition size must match axis
    if spec.name == "Compress":
        x_case = next((c for c in input_cases if c.name == "X"), None)
        cond_case = next((c for c in input_cases if c.name == "condition"), None)
        axis = int(attrs.get("axis", 0))
        if x_case is not None and cond_case is not None and x_case.shape and 0 <= axis < len(x_case.shape):
            target = int(x_case.shape[axis])
            label = f"1d-{target}"
            new_cond = InputCase(
                name=cond_case.name, shape_label=label, shape=(target,),
                dtype_label=cond_case.dtype_label, fill_label=cond_case.fill_label, is_init=cond_case.is_init,
            )
            input_cases = tuple(new_cond if c.name == "condition" else c for c in input_cases)
    if spec.name in {"BatchNormalization", "InstanceNormalization"}:
        x_case = next((c for c in input_cases if c.name in {"X", "input"}), None)
        if x_case is not None and len(x_case.shape) >= 2:
            cdim = int(x_case.shape[1])
            label = f"1d-{cdim}" if f"1d-{cdim}" in SHAPE_BUCKETS else "1d-1"
            shape = SHAPE_BUCKETS[label]
            channel_inputs = {"scale", "B", "bias", "mean", "var"}
            input_cases = tuple(
                InputCase(c.name, label, shape, c.dtype_label, c.fill_label, c.is_init)
                if c.name in channel_inputs else c
                for c in input_cases
            )
    return input_cases


def _materialize_case_array(spec: OpSpec, case: InputCase, input_cases: tuple[InputCase, ...], attrs: dict) -> np.ndarray:
    if spec.name == "TopK" and case.name == "K":
        x_case = next((c for c in input_cases if c.name == "X"), None)
        axis = int(attrs.get("axis", -1))
        axis_size = 1
        if x_case is not None and x_case.shape:
            axis %= len(x_case.shape)
            axis_size = int(x_case.shape[axis])
        return np.array([max(1, min(axis_size, 2))], dtype=case.np_dtype)
    return case.materialize()


def build_case(spec: OpSpec, input_cases: tuple[InputCase, ...], attrs: dict, *,
               idx: int = 0, output_mask: tuple[bool, ...] | None = None) -> TestCase:
    """Build a concrete test case from a spec and input configuration."""
    nodes = []
    initializers: list[onnx.TensorProto] = []
    graph_inputs: list[onnx.ValueInfoProto] = []
    feeds: dict[str, np.ndarray] = {}

    input_cases = _apply_input_constraints(spec, input_cases, attrs)

    by_name = {c.name: c for c in input_cases}
    port_input_names: list[str] = []
    for port in spec.inputs:
        case = by_name.get(port.name)
        if case is None:
            port_input_names.append("")
            continue
        if case.is_init:
            arr = _materialize_case_array(spec, case, input_cases, attrs)
            initializers.append(onnx.numpy_helper.from_array(arr, name=case.name))
        else:
            arr = _materialize_case_array(spec, case, input_cases, attrs)
            vi = onnx.helper.make_tensor_value_info(case.name, case.onnx_dtype, list(case.shape))
            graph_inputs.append(vi)
            feeds[case.name] = arr
        port_input_names.append(case.name)
    while port_input_names and port_input_names[-1] == "":
        port_input_names.pop()

    static = list(spec.static_inits)
    for sname, sdtype, sshape_label, svalue in static:
        if sshape_label == "scalar":
            sshape = ()
        else:
            sshape = SHAPE_BUCKETS.get(sshape_label, ())
        arr = np.array(svalue, dtype=np_dtype(sdtype)).reshape(sshape)
        initializers.append(onnx.numpy_helper.from_array(arr, name=sname))
        port_input_names.append(sname)

    clean_attrs = {k: v for k, v in attrs.items() if not k.startswith("_") and v is not None}
    used_names = {c.name for c in input_cases} | {i.name for i in initializers}
    spec_outputs = spec.outputs or tuple()
    if output_mask is None:
        output_mask = tuple(not out.is_optional for out in spec_outputs)
    if spec_outputs and not any(output_mask):
        output_mask = (True,) + tuple(False for _ in spec_outputs[1:])

    node_output_names: list[str] = []
    graph_output_pairs = []
    for i, out in enumerate(spec_outputs):
        if i < len(output_mask) and not output_mask[i]:
            node_output_names.append("")
            continue
        base = out.name or f"output_{i}"
        name = f"{base}_out" if base in used_names else base
        while name in used_names or name in node_output_names:
            name = f"{base}_{len(graph_output_pairs)}"
        node_output_names.append(name)
        graph_output_pairs.append((name, out))
    while node_output_names and node_output_names[-1] == "":
        node_output_names.pop()
    if not node_output_names:
        node_output_names = [f"output_{i}" for i in range(spec.output_count or 1)]
    node = onnx.helper.make_node(spec.name, inputs=port_input_names, outputs=node_output_names, **clean_attrs)
    nodes.append(node)

    def output_elem_type(out) -> int:
        if spec.name == "Cast" and "to" in attrs:
            return int(attrs["to"])
        if spec.name in {"RandomNormal", "RandomUniform"} and "dtype" in attrs:
            return int(attrs["dtype"])
        if spec.name in {"RandomNormal", "RandomUniform"}:
            return onnx.TensorProto.FLOAT
        for port, case in zip(spec.inputs, (by_name.get(p.name) for p in spec.inputs)):
            if case is not None and out.type_param and out.type_param == port.type_param:
                return case.onnx_dtype
        if out.name.lower() in {"indices", "argmax", "argmin"}:
            return onnx.TensorProto.INT64
        if out.name.lower() in {"mask"}:
            return onnx.TensorProto.BOOL
        if out.dtype_labels:
            return onnx_dtype(out.dtype_labels[0])
        return onnx.TensorProto.FLOAT

    def output_shape(out) -> list[int] | None:
        if spec.name in {"RandomNormal", "RandomUniform"} and isinstance(attrs.get("shape"), (list, tuple)):
            return [int(x) for x in attrs["shape"]]
        for port, case in zip(spec.inputs, (by_name.get(p.name) for p in spec.inputs)):
            if case is not None and out.type_param and out.type_param == port.type_param:
                return list(case.shape)
        return None

    graph_outputs = [
        onnx.helper.make_tensor_value_info(name, output_elem_type(out), output_shape(out))
        for name, out in graph_output_pairs
    ]
    if not graph_outputs:
        graph_outputs = [onnx.helper.make_tensor_value_info(name, onnx.TensorProto.FLOAT, None)
                         for name in node_output_names if name]

    graph = onnx.helper.make_graph(nodes, f"{spec.name}_{idx}", graph_inputs, graph_outputs,
                                    initializer=initializers if initializers else None)
    model = onnx.helper.make_model(graph, producer_name="onnx_tool_audit", opset_imports=[onnx.helper.make_opsetid("", spec.opset)])

    out_label = "" if output_mask is None else f" outputs={''.join('1' if b else '0' for b in output_mask)}"
    label = " ".join([c.label() for c in input_cases]) + " " + str(attrs if attrs else "") + out_label
    return TestCase(op=spec.name, label=label, model=model, feeds=feeds, input_cases=input_cases, attrs=attrs)


# ─────────────────────────────────────────────────────────────────────────────
# Test case expansion (single-op)
# ─────────────────────────────────────────────────────────────────────────────

def _input_choice_sets(spec: OpSpec) -> list[list[InputCase | None]]:
    """Build choices per input port without crossing the products."""
    if not spec.inputs:
        return []
    per_port: list[list[InputCase]] = []
    for port in spec.inputs:
        cases: list[InputCase | None] = [None] if port.is_optional else []
        for shape_label in port.shape_labels:
            if shape_label not in SHAPE_BUCKETS:
                continue
            for dtype_label in port.dtype_labels:
                if dtype_label not in DTYPE_TABLE:
                    continue
                fills = port.fill_labels if not spec.pinned_fills.get(port.name) else (spec.pinned_fills[port.name],)
                for fill_label in fills:
                    cases.append(InputCase(
                        name=port.name, shape_label=shape_label, shape=SHAPE_BUCKETS[shape_label],
                        dtype_label=dtype_label, fill_label=fill_label, is_init=port.is_init,
                    ))
        per_port.append(cases)
    return per_port


def _strip_omitted(combo: tuple[InputCase | None, ...]) -> tuple[InputCase, ...]:
    return tuple(c for c in combo if c is not None)


def _combo_key(combo: tuple[InputCase | None, ...]) -> tuple[str, ...]:
    return tuple("<omit>" if c is None else c.label() for c in combo)


def _combo_ok(spec: OpSpec, combo: tuple[InputCase | None, ...]) -> bool:
    name_to_idx = {port.name: i for i, port in enumerate(spec.inputs)}
    for i, port in enumerate(spec.inputs):
        if combo[i] is None or not port.tied_dtype_to:
            continue
        j = name_to_idx[port.tied_dtype_to]
        if combo[j] is not None and combo[i].dtype_label != combo[j].dtype_label:
            return False
    return True


def _first_matching(choices: list[InputCase | None], **want) -> InputCase | None:
    for c in choices:
        if c is None:
            continue
        if all(getattr(c, k) == v for k, v in want.items() if v is not None):
            return c
    return next((c for c in choices if c is not None), None)


def _preferred_dtype(choices: list[InputCase | None]) -> str | None:
    labels = {c.dtype_label for c in choices if c is not None}
    for label in ("float32", "int64", "uint8", "bool"):
        if label in labels:
            return label
    return next(iter(sorted(labels)), None)


def _stress_input_combos(spec: OpSpec, choice_sets: list[list[InputCase | None]]) -> list[tuple[InputCase | None, ...]]:
    """Generic multi-input shape stress cases, especially for broadcast-like ops."""
    required = [i for i, p in enumerate(spec.inputs) if not p.is_optional]
    if len(required) < 2:
        return []

    patterns = [
        ("B-1-9-9", "B-C-1-1", "B-C-1-1"),
        ("B-C-1-1", "B-1-H-1", "scalar"),
        ("scalar", "B-C-1-1", "B-1-H-1"),
    ]
    out = []
    for pattern in patterns:
        combo = [None if p.is_optional else _first_matching(cs) for p, cs in zip(spec.inputs, choice_sets)]
        dtype_by_root = {}
        ok = True
        for pos, idx in enumerate(required):
            port = spec.inputs[idx]
            root = port.tied_dtype_to or port.name
            dtype_by_root.setdefault(root, _preferred_dtype(choice_sets[idx]))
            shape_label = pattern[min(pos, len(pattern) - 1)]
            picked = _first_matching(choice_sets[idx],
                                     shape_label=shape_label,
                                     dtype_label=dtype_by_root[root])
            if picked is None:
                ok = False
                break
            combo[idx] = picked
        if ok:
            out.append(tuple(combo))
    return out


def _combo_from_index(choice_sets: list[list], index: int) -> tuple:
    picked = []
    for choices in reversed(choice_sets):
        index, j = divmod(index, len(choices))
        picked.append(choices[j])
    return tuple(reversed(picked))


def _spread_indices(total: int, limit: int) -> list[int]:
    if total <= 0:
        return []
    if total <= limit:
        return list(range(total))
    even = {i * (total - 1) // max(1, limit - 1) for i in range(limit)}
    mixed = {((i + 1) * 1103515245 + 12345) % total for i in range(limit)}
    return sorted((even | mixed))[:limit]


def _sample_input_combos(spec: OpSpec, limit: int = MAX_CASES_PER_OP) -> list[tuple[InputCase, ...]]:
    """Coverage-ish input sampling without materializing the full product."""
    choice_sets = _input_choice_sets(spec)
    if not choice_sets:
        return [()]

    out: list[tuple[InputCase, ...]] = []
    seen = set()

    def add(combo: tuple[InputCase | None, ...]) -> None:
        key = _combo_key(combo)
        if key not in seen and _combo_ok(spec, combo):
            seen.add(key)
            out.append(_strip_omitted(combo))

    for combo in _stress_input_combos(spec, choice_sets):
        add(combo)

    first_present = tuple(_first_matching(cs) for cs in choice_sets)
    first_optional_omitted = tuple(None if port.is_optional else _first_matching(cs)
                                  for port, cs in zip(spec.inputs, choice_sets))
    add(first_optional_omitted)
    add(first_present)

    optional_idxs = [i for i, p in enumerate(spec.inputs) if p.is_optional]
    for mask in range(min(1 << len(optional_idxs), 32)):
        combo = list(first_optional_omitted)
        for bit, idx in enumerate(optional_idxs):
            combo[idx] = _first_matching(choice_sets[idx]) if mask & (1 << bit) else None
        add(tuple(combo))

    dtype_labels = sorted({c.dtype_label for cs in choice_sets for c in cs if c is not None})
    for dtype_label in dtype_labels:
        add(tuple(_first_matching(cs, dtype_label=dtype_label) for cs in choice_sets))

    fill_labels = sorted({c.fill_label for cs in choice_sets for c in cs if c is not None})
    for fill_label in fill_labels:
        add(tuple(_first_matching(cs, fill_label=fill_label) for cs in choice_sets))

    shape_labels = sorted({c.shape_label for cs in choice_sets for c in cs if c is not None})
    for shape_label in shape_labels:
        add(tuple(_first_matching(cs, shape_label=shape_label) for cs in choice_sets))

    total = math.prod(len(cs) for cs in choice_sets)
    for idx in _spread_indices(total, limit * 4):
        add(_combo_from_index(choice_sets, idx))
        if len(out) >= limit:
            break

    return out[:limit]


def _attr_choices(name: str, spec: AttrSpec) -> tuple:
    t = spec.attr_type
    vals = []
    if not spec.required:
        vals.append(None)
    if t == "INT":
        if name == "to":
            vals += [onnx.TensorProto.FLOAT, onnx.TensorProto.FLOAT16, onnx.TensorProto.DOUBLE,
                     onnx.TensorProto.INT64, onnx.TensorProto.BOOL]
        elif name == "dtype":
            vals += [onnx.TensorProto.FLOAT, onnx.TensorProto.FLOAT16, onnx.TensorProto.DOUBLE]
        else:
            vals += [0, 1, -1] if "axis" in name else [0, 1]
    elif t == "INTS":
        if name == "kernel_shape":
            vals += [[1, 1], [2, 2], [3, 3]]
        elif name == "pads":
            vals += [[0, 0, 0, 0], [1, 1, 1, 1]]
        elif name == "strides":
            vals += [[1, 1], [2, 2]]
        elif "axes" in name:
            vals += [[0], [1], [2, 3]]
        elif name == "perm":
            vals += [[0, 1, 3, 2], [0, 2, 1, 3]]
        else:
            vals += [[1], [1, 1]]
    elif t == "FLOAT":
        vals += [0.0, 0.5, 1.0]
    elif t == "FLOATS":
        vals += [[0.0], [0.0, 1.0]]
    elif t == "STRING":
        if name == "auto_pad":
            vals += [b"NOTSET", b"SAME_UPPER"]
        elif name == "direction":
            vals += [b"LEFT", b"RIGHT"]
        else:
            vals += [b""]
    elif t == "STRINGS":
        vals += [[b""]]
    elif t == "TENSOR":
        vals += [_tensor_value()]
    elif t == "TENSORS":
        vals += [[_tensor_value()]]

    default = None if name in {"to", "dtype"} and spec.default == 0 else spec.default
    if _attr_default_fits(t, default):
        vals.insert(1 if not spec.required else 0, default)
    # preserve order, drop dupes by repr because lists/tensors are unhashable
    return tuple({repr(v): v for v in vals}.values()) or (None,)


def _attr_default_fits(attr_type: str, value) -> bool:
    if value in (None, ""):
        return False
    if attr_type == "INT":
        return isinstance(value, int) and not isinstance(value, bool)
    if attr_type == "INTS":
        return isinstance(value, (list, tuple)) and all(isinstance(v, int) and not isinstance(v, bool) for v in value)
    if attr_type == "FLOAT":
        return isinstance(value, float)
    if attr_type == "FLOATS":
        return isinstance(value, (list, tuple)) and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in value)
    if attr_type == "STRING":
        return isinstance(value, (bytes, str))
    if attr_type == "STRINGS":
        return isinstance(value, (list, tuple)) and all(isinstance(v, (bytes, str)) for v in value)
    if attr_type == "TENSOR":
        return isinstance(value, onnx.TensorProto)
    if attr_type == "TENSORS":
        return isinstance(value, (list, tuple)) and all(isinstance(v, onnx.TensorProto) for v in value)
    return False


def _attr_choice_sets(spec: OpSpec) -> tuple[list[str], list[tuple]]:
    if not spec.attrs and not spec.attr_specs:
        return [], []
    keys = list((spec.attr_specs or spec.attrs).keys())
    choices = []
    for k in keys:
        values = spec.attrs.get(k, ())
        if values:
            choices.append(values)
        elif k in spec.attr_specs:
            choices.append(_attr_choices(k, spec.attr_specs[k]))
        else:
            choices.append((None,))
    return keys, choices


def _attrs_from_combo(keys: list[str], combo: tuple) -> dict[str, object]:
    return {k: v for k, v in zip(keys, combo) if v is not None}


def _expand_attrs(spec: OpSpec, limit: int = MAX_CASES_PER_OP) -> list[dict[str, object]]:
    """Sample attributes without exploding the full product."""
    keys, choices = _attr_choice_sets(spec)
    if not keys:
        return [{}]
    out = []
    seen = set()

    def add(combo: tuple) -> None:
        attrs = _attrs_from_combo(keys, combo)
        key = repr(attrs)
        if key not in seen:
            seen.add(key)
            out.append(attrs)

    first = tuple(cs[0] for cs in choices)
    add(first)
    for i, cs in enumerate(choices):
        for value in cs:
            combo = list(first)
            combo[i] = value
            add(tuple(combo))

    total = math.prod(len(cs) for cs in choices)
    for idx in _spread_indices(total, limit):
        add(_combo_from_index(choices, idx))
        if len(out) >= limit:
            break
    return out[:limit]


def _output_masks(spec: OpSpec) -> list[tuple[bool, ...]]:
    if not spec.outputs:
        return [()]
    optional_idxs = [i for i, out in enumerate(spec.outputs) if out.is_optional]
    base = tuple(not out.is_optional for out in spec.outputs)
    masks = [base]
    if optional_idxs:
        all_present = tuple(True for _ in spec.outputs)
        masks.append(all_present)
        if spec.name != "BatchNormalization":
            for count in range(1, len(optional_idxs) + 1):
                mask = list(base)
                for idx in optional_idxs[:count]:
                    mask[idx] = True
                masks.append(tuple(mask))
    return list({repr(m): m for m in masks}.values())[:32]


def _cap(cases: list, limit: int) -> list:
    """Cap case list at limit, preserving diversity."""
    if len(cases) <= limit:
        return cases
    indices = np.linspace(0, len(cases) - 1, limit, dtype=int)
    return [cases[i] for i in indices]


_BROADCAST_OPS = {
    "Add": ("A", "B"), "Mul": ("A", "B"), "Sub": ("A", "B"), "Div": ("A", "B"),
    "Equal": ("A", "B"), "Greater": ("A", "B"), "Less": ("A", "B"),
    "GreaterOrEqual": ("A", "B"), "LessOrEqual": ("A", "B"), "NotEqual": ("A", "B"),
    "And": ("A", "B"), "Or": ("A", "B"), "Xor": ("A", "B"),
    "Pow": ("A", "B"), "Mod": ("A", "B"),
    "Sum": ("A", "B"), "Max": ("A", "B"), "Min": ("A", "B"),
    "MatMul": ("A", "B"), "Einsum": ("A", "B"),
}

def _broadcastable(input_cases: tuple[InputCase, ...], names: tuple[str, ...]) -> bool:
    """Check if inputs can broadcast."""
    by_name = {c.name: c for c in input_cases}
    shapes = [by_name[n].shape for n in names if n in by_name]
    if not shapes:
        return True
    try:
        np.broadcast_shapes(*shapes)
        return True
    except ValueError:
        return False


_POOL_OPS = {"AveragePool", "MaxPool", "LpPool"}

def _pool_attrs_valid(input_cases: tuple[InputCase, ...], attrs: dict) -> bool:
    data = next((c for c in input_cases if not c.is_init), None) or (input_cases[0] if input_cases else None)
    if data is None or len(data.shape) < 3:
        return False
    spatial = len(data.shape) - 2
    spatial_dims = data.shape[2:]
    kernel = attrs.get("kernel_shape")
    if not isinstance(kernel, (list, tuple)) or len(kernel) != spatial:
        return False
    if any(int(k) <= 0 for k in kernel):
        return False
    strides = attrs.get("strides")
    if strides is not None and (not isinstance(strides, (list, tuple)) or len(strides) != spatial):
        return False
    dilations = attrs.get("dilations")
    if dilations is not None and (not isinstance(dilations, (list, tuple)) or len(dilations) != spatial):
        return False
    pads = attrs.get("pads", [0] * (2 * spatial))
    if not isinstance(pads, (list, tuple)) or len(pads) != 2 * spatial:
        return False
    return all(int(pads[i]) < int(kernel[i]) and
               int(pads[i + spatial]) < int(kernel[i]) and
               int(kernel[i]) <= int(spatial_dims[i]) + int(pads[i]) + int(pads[i + spatial])
               for i in range(spatial))


def generate_single_op(spec: OpSpec, *, limit: int = MAX_CASES_PER_OP) -> list[TestCase]:
    """Generate all test cases for one operator."""
    inp_combos = _sample_input_combos(spec, limit=limit)
    attr_combos = _expand_attrs(spec, limit=limit)
    output_masks = _output_masks(spec)

    if spec.name in _BROADCAST_OPS:
        names = _BROADCAST_OPS[spec.name]
        inp_combos = [c for c in inp_combos if _broadcastable(c, names)]

    if spec.name == "Pad":
        inp_combos = [c for c in inp_combos if all(len(ic.shape) == 4 for ic in c if ic.name == "data")]
    if not inp_combos:
        return []

    def good_pair(inp_combo, attrs) -> bool:
        if spec.name in ("Softmax", "LogSoftmax", "Hardmax"):
            axis = int(attrs.get("axis", -1))
            rank = max(len(c.shape) for c in inp_combo) if inp_combo else 0
            return rank > 0 and -rank <= axis < rank
        if spec.name == "TopK":
            x_case = next((c for c in inp_combo if c.name == "X"), None)
            axis = int(attrs.get("axis", -1))
            return x_case is not None and len(x_case.shape) > 0 and -len(x_case.shape) <= axis < len(x_case.shape)
        if spec.name in _POOL_OPS:
            return _pool_attrs_valid(inp_combo, attrs)
        if spec.name in {"BatchNormalization", "InstanceNormalization"}:
            x_case = next((c for c in inp_combo if c.name in {"X", "input"}), None)
            return x_case is not None and len(x_case.shape) >= 2
        return True

    pairs = []
    seen = set()

    def add_pair(inp_combo, attrs, output_mask) -> None:
        if not good_pair(inp_combo, attrs):
            return
        key = (tuple(c.label() for c in inp_combo), repr(attrs), output_mask)
        if key not in seen:
            seen.add(key)
            pairs.append((inp_combo, attrs, output_mask))

    for i, inp_combo in enumerate(inp_combos):
        add_pair(inp_combo, attr_combos[i % len(attr_combos)], output_masks[i % len(output_masks)])
    for i, attrs in enumerate(attr_combos):
        add_pair(inp_combos[i % len(inp_combos)], attrs, output_masks[i % len(output_masks)])
    for i, output_mask in enumerate(output_masks):
        add_pair(inp_combos[i % len(inp_combos)], attr_combos[i % len(attr_combos)], output_mask)

    total = len(inp_combos) * len(attr_combos) * len(output_masks)
    for idx in _spread_indices(total, limit * 2):
        inp_combo, attrs, output_mask = _combo_from_index([inp_combos, attr_combos, output_masks], idx)
        add_pair(inp_combo, attrs, output_mask)
        if len(pairs) >= limit:
            break

    cases = []
    for idx, (inp_combo, attr_combo, output_mask) in enumerate(pairs[:limit]):
        case = build_case(spec, inp_combo, attr_combo, idx=idx, output_mask=output_mask)
        cases.append(case)

    return cases
