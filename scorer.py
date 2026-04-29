"""Mirror of neurogolf_utils.score_network for differential testing.

The 2026 NeuroGolf scorer computes:
    score = max(1, 25 - ln(MACs + memory + params))

Where:
    - memory = sum of intermediate tensor bytes via `onnx.shape_inference.infer_shapes`
               (excludes graph inputs/outputs by name)
    - MACs   = sum of node.macs from onnx_tool.profile()
    - params = sum of node.params from onnx_tool.profile()

This module reproduces those three numbers for a given model, exactly like
the scorer would, so we can diff:
    - calculate_memory()  vs  ORT-actual intermediate bytes
    - g.valid_profile     vs  ORT-runs-cleanly
"""
from __future__ import annotations

import os
import tempfile
import warnings
from dataclasses import dataclass

import numpy as np
import onnx
import onnx_tool


_EXCLUDED_OP_TYPES = ["LOOP", "SCAN", "NONZERO", "UNIQUE", "SCRIPT", "FUNCTION"]
_EXCLUDED_TENSOR_NAMES = {"input", "output"}


@dataclass
class ScoreResult:
    """What the neurogolf scorer would report for a model."""
    macs: int | None
    memory: int | None
    params: int | None
    error: str | None = None
    # Per-tensor memory contributions for diffing
    tensor_bytes: dict[str, int] | None = None


def calculate_memory(model: onnx.ModelProto) -> tuple[int | None, dict[str, int]]:
    """Reimplements neurogolf_utils.calculate_memory.

    Returns:
        (total_bytes, per_tensor_bytes). Returns (None, {}) if shape inference
        leaves any dim symbolic (matching the scorer's None return).
    """
    try:
        graph = onnx.shape_inference.infer_shapes(model, strict_mode=True).graph
    except Exception:
        return None, {}

    per_tensor: dict[str, int] = {}
    total = 0
    for item in list(graph.input) + list(graph.value_info) + list(graph.output):
        if not item.type.HasField("tensor_type"):
            continue
        tt = item.type.tensor_type
        if not tt.HasField("shape"):
            return None, {}
        n = 1
        for dim in tt.shape.dim:
            if dim.HasField("dim_param") or not dim.HasField("dim_value"):
                return None, {}
            n *= dim.dim_value
        if item.name in _EXCLUDED_TENSOR_NAMES:
            continue
        try:
            np_dt = onnx.helper.tensor_dtype_to_np_dtype(tt.elem_type)
        except Exception:
            continue
        bytes_ = n * np.dtype(np_dt).itemsize
        per_tensor[item.name] = bytes_
        total += bytes_
    return total, per_tensor


def score_via_neurogolf(model: onnx.ModelProto) -> ScoreResult:
    """Reproduce score_network() from neurogolf_utils, end-to-end."""
    fd, path = tempfile.mkstemp(suffix=".onnx")
    os.close(fd)
    try:
        onnx.save(model, path)

        # Validity check from onnx.checker (the new scorer calls it inside calculate_memory)
        try:
            onnx.checker.check_model(model, full_check=True)
        except Exception as e:
            return ScoreResult(None, None, None, error=f"checker: {type(e).__name__}: {e}")

        # onnx_tool path for MACs/params
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                m = onnx_tool.loadmodel(path, {"verbose": False, "constant_folding": True})
                g = m.graph
                g.graph_reorder_nodes()
                g.shape_infer(None)
                g.profile()
        except Exception as e:
            return ScoreResult(None, None, None, error=f"onnx_tool: {type(e).__name__}: {e}")

        if not g.valid_profile:
            return ScoreResult(None, None, None, error="onnx_tool: invalid profile")

        for key, node in g.nodemap.items():
            if node.op_type.upper() in _EXCLUDED_OP_TYPES:
                return ScoreResult(None, None, None, error=f"excluded op: {node.op_type}")
            if int(getattr(node, "memory", 0) or 0) < 0 or int(getattr(node, "params", 0) or 0) < 0:
                return ScoreResult(None, None, None, error="negative memory or params")
            macs = getattr(node, "macs", 0)
            macs_min = min(macs) if isinstance(macs, (list, tuple)) and macs else int(macs or 0)
            if macs_min < 0:
                return ScoreResult(None, None, None, error="negative macs")

        memory, per_tensor = calculate_memory(model)
        if memory is None:
            return ScoreResult(None, None, None, error="shape inference incomplete")

        macs_total = int(sum(g.macs)) if hasattr(g, "macs") else 0
        params_total = int(g.params) if hasattr(g, "params") else 0

        return ScoreResult(
            macs=macs_total,
            memory=memory,
            params=params_total,
            tensor_bytes=per_tensor,
        )
    finally:
        try:
            os.unlink(path)
        except Exception:
            pass


def ort_intermediate_memory(tensors: dict[str, np.ndarray],
                             feeds: dict[str, np.ndarray] | None = None) -> tuple[int, dict[str, int]]:
    """Sum bytes of every tensor that calculate_memory would count.

    Matches the scorer's exclusion rule (skip 'input'/'output' names) and includes:
      - graph feeds  (the model's inputs, often named X/A/etc. in our test harness)
      - initializers (constants stored in the graph)
      - intermediate node outputs and final outputs

    `tensors` should be the output of TruthResult.all_tensors(); `feeds` is the
    original feed dict passed to run_truth.
    """
    per_tensor: dict[str, int] = {}
    total = 0
    seen: set[str] = set()
    for source in (feeds or {}, tensors):
        for name, arr in source.items():
            if name in _EXCLUDED_TENSOR_NAMES or name in seen:
                continue
            seen.add(name)
            b = int(arr.size) * arr.dtype.itemsize
            per_tensor[name] = b
            total += b
    return total, per_tensor
