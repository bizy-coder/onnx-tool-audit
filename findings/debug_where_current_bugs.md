# onnx_tool 1.0.1 — bug catalog

Each test case runs through two oracles:

- **`onnxruntime`** executes the model and provides the runtime baseline. If ORT rejects a model, there is no shape/type/byte baseline for comparing onnx_tool.
- **`onnx_tool`** statically profiles the model.

Classification:

| ORT | onnx_tool | classification |
|-----|-----------|----------------|
| reject + checker rejects | (any) | **invalid-test-case** / harness coverage gap |
| reject + checker accepts | (any) | **ort-rejects-checker-valid-model** / no onnx_tool baseline |
| accept | reject | **onnx-tool-fails-valid-model** |
| accept | accept-but-disagrees | **onnx_tool wrong shape/dtype/bytes** |

**Summary**: 1 distinct onnx_tool bugs (4 surface findings collapsed).

## Bugs in onnx_tool

### Bug 1: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `Where@11`
- **Surface findings collapsed**: 4
- **Minimal repro**:

  Op: `Where`  
  Inputs: `condition(input)=B-C-1-1/bool/all_true X(input)=B-1-H-1/uint8/random Y(input)=scalar/uint8/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10, 30, 1)` | `uint8` | `300` |
  | onnx_tool| `(1, 1, 30, 1)` | `uint8` | `30` |

  _truth=(1, 10, 30, 1) claim=(1, 1, 30, 1)_
