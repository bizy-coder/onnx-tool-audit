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

**Summary**: 2 distinct onnx_tool bugs (271 surface findings collapsed).

## Bugs in onnx_tool

### Bug 1: `scorer-wrong-shape`

_(no explanation)_

- **Affected ops** (1): `BatchNormalization@11`
- **Surface findings collapsed**: 260
- **Minimal repro**:

  Op: `BatchNormalization`  
  Inputs: `X(input)=B-1-H-1/float16/random scale(input)=1d-1/float16/random B(input)=1d-1/float16/random mean(input)=1d-1/float16/random var(input)=1d-1/float16/random {'epsilon': 0.0, 'momentum': 0.0} outputs=11111`  
  Attrs: `{'epsilon': 0.0, 'momentum': 0.0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1,)` | `float16` | `2` |
  | onnx_tool| `(1, 1, 30, 1)` | `float16` | `60` |

  _ORT=(1,) SI=(1, 1, 30, 1)_

### Bug 2: `scorer-missing-tensor`

_(no explanation)_

- **Affected ops** (1): `Clip@11`
- **Surface findings collapsed**: 11
- **Minimal repro**:

  Op: `Clip`  
  Inputs: `input(input)=scalar/float16/random min(init)=scalar/float16/random max(init)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `()` | `float16` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _shape_inference omits tensor (ORT: shape=() dtype=float16 bytes=2)_
