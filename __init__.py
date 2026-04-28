"""Automated ONNX operator testing: generate test cases from schema, run against two oracles.

Public entry points:

    from onnx_tool_audit.harness import run_op, run_all
    from onnx_tool_audit.profiles import SPECS

The harness is intentionally separate from the rest of NeuroGolf — it has no
imports of `src/` or `web/`, only `onnx`, `onnxruntime`, `onnx_tool`, and `numpy`.
"""

__version__ = "0.1.0"
