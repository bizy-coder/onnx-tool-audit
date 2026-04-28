# onnx_tool 1.0.1 — bug catalog

Each test case runs through two oracles:

- **`onnxruntime`** executes the model. Validity is decided by execution: if ORT runs the model cleanly, it's a model that could ship. If ORT rejects it, we ignore the case — an unrunnable model can't be submitted to Kaggle and can't influence scoring.
- **`onnx_tool`** statically profiles the model.

Classification:

| ORT | onnx_tool | classification |
|-----|-----------|----------------|
| reject | (any) | **invalid-test-case** (noise — model unrunnable) |
| accept | reject | **onnx-tool-fails-valid-model** |
| accept | accept-but-disagrees | **onnx_tool wrong shape/dtype/bytes** |

**Summary**: 2 distinct onnx_tool bugs (2 surface findings collapsed) | 0 noise patterns (0 surface findings ignored).

## Bugs in onnx_tool

### Bug 1: `constant-uncounted`

_Constant node outputs are tracked at the per-tensor level but not added to per-node memory; the model total under-reports by the constant's size._

- **Affected ops** (1): `DAG`
- **Surface findings collapsed**: 1
- **Minimal repro**:

  Op: `DAG-scenario`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10, 30, 30)` | `float32` | `36000` |
  | onnx_tool| `(1, 10, 30, 30)` | `float32` | `36000` |

  _node  memory=0 ignores produced tensor (true=36000B)_

### Bug 2: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `DAG`
- **Surface findings collapsed**: 1
- **Minimal repro**:

  Op: `DAG-scenario`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 5, 30, 30)` | `float32` | `18000` |
  | onnx_tool| `(1, 0, 30, 30)` | `float32` | `0` |

  _truth=(1, 5, 30, 30) claim=(1, 0, 30, 30)_
