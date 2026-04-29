# Structured onnx_tool issue report

Confirmed divergences vs. ORT, grouped by `(op, family, opsets)`. **31 issues**: 0 type, 0 shape, 4 shape-inference (memory), 27 error.

**Columns:**
- **Inputs**: each port shown as `name: shape/dtype/fill`. `(init)` marks initializer (constant input).
- **Attrs**: op attributes used in the failing case.
- **`*` suffix** on any field means it *varies* across triggers — the shown value is just one example and other values also reproduce the bug. Unmarked values are required (consistent across all triggers).
- **Repro**: `required` if a single Inputs+Attrs configuration triggers the bug; `example (1/N)` if N distinct configurations trigger it (we show the simplest).
- **Cases**: `hits/valid_cases` — how many ORT-valid configurations onnx_tool got wrong. Trailing `(N surf)` means N raw findings collapsed into the same group.

**Sections:** *Incorrect Type* and *Incorrect Shape* are bugs in `onnx_tool`'s static profiler (impact MAC counting). *Shape Inference (memory)* is bugs that come **directly from `onnx.shape_inference`** — these affect the new scorer's `calculate_memory()` total even after the metric migration. *Incorrect Errors* covers cases where the scorer rejects an ORT-runnable model.

## Incorrect Type

_No confirmed findings._

## Incorrect Shape

_No confirmed findings._

## Shape Inference (memory)

| Op | Opsets | Family | Inputs | Attrs | Repro | ORT bytes | scorer bytes | Cases |
|---|---|---|---|---|---|---|---|---|
| `BatchNormalization` | 11–13 | shape overcount | `X`: B-1-H-1\*/f16\*/random\*<br>`scale`: 1d-1\*/f16\*/random\*<br>`B`: 1d-1\*/f16\*/random\*<br>`mean`: 1d-1\*/f16\*/random\*<br>`var`: 1d-1\*/f16\*/random\* | — | example (1/50) | `2` | `60` | 3/384 (600 surf) |
| `BatchNormalization` | 11–13 | shape undercount | `X`: B-C-1-1/f64\*/sparse\*<br>`scale`: 1d-10/f64\*/alternating\*<br>`B`: 1d-10/f64\*/sparse\*<br>`mean`: 1d-10/f64\*/alternating\*<br>`var`: 1d-10/f64\*/sparse\* | `epsilon=1.0\*` | example (1/15) | `80` | `80` | 3/384 (180 surf) |
| `Clip` | 11–18 | tensor missing from shape_inference | `input`: B-C-1-1\*/f32\*/random\*<br>`min` (init): scalar/f32\*/alternating\* | — | example (1/6) | `4` | — | 8/21 (25 surf) |
| `DequantizeLinear` | 11–18 | tensor missing from shape_inference | `x`: scalar/i32/random<br>`x_scale` (init): scalar/f32/random<br>`x_zero_point` (init): scalar/i32/random | — | example (1/2) | `4` | — | 8/96 (16 surf) |

## Incorrect Errors

| Op | Opsets | Family | Inputs | Attrs | Repro | scorer error | Cases |
|---|---|---|---|---|---|---|---|
| `Acos` | 11–18 | ORT executed cleanly; scorer | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer` | 8/192 (192 surf) |
| `Acosh` | 11–18 | ORT executed cleanly; scorer | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer` | 8/192 (192 surf) |
| `Add` | 11–18 | ORT executed cleanly; scorer | `A`: scalar\*/f32\*/random\*<br>`B`: B-1-H-1\*/f32\*/alternating\* | — | example (1/42) | `ORT executed cleanly; scorer: checker: InferenceError: [ShapeInferenceError] Inference error(s): (op_type:Add): [ShapeInferenceError] Inferr` | 8/584 (161 surf) |
| `And` | 11–18 | ORT executed cleanly; scorer | `A`: scalar\*/bool/all_true\*<br>`B`: scalar\*/bool/all_true\* | — | example (1/128) | `ORT executed cleanly; scorer: checker: ValidationError: Field 'shape' of 'type' is required but missing.` | 8/1024 (1024 surf) |
| `ArgMax` | 11–18 | ORT executed cleanly; scorer | `data`: B-1-H-1\*/f32\*/alternating\* | — | example (1/111) | `ORT executed cleanly; scorer: checker: ValidationError: Field 'shape' of 'type' is required but missing.` | 8/504 (504 surf) |
| `ArgMin` | 11–18 | ORT executed cleanly; scorer | `data`: B-1-H-1\*/f32\*/alternating\* | — | example (1/111) | `ORT executed cleanly; scorer: checker: ValidationError: Field 'shape' of 'type' is required but missing.` | 8/504 (504 surf) |
| `Asin` | 11–18 | ORT executed cleanly; scorer | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer` | 8/192 (192 surf) |
| `Asinh` | 11–18 | ORT executed cleanly; scorer | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer` | 8/192 (192 surf) |
| `Atanh` | 11–18 | ORT executed cleanly; scorer | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer` | 8/192 (192 surf) |
| `AveragePool` | 11–18 | ORT executed cleanly; scorer | `X`: B-1-H-1\*/f32\*/alternating\* | `kernel_shape=[2, 2]\*, auto_pad=SAME_UPPER\*, pads=[1, 1, 1, 1]\*, ceil_mode=1\*` | example (1/49) | `ORT executed cleanly; scorer: checker: InferenceError: [ShapeInferenceError] Inference error(s): (op_type:AveragePool): [ShapeInferenceError` | 8/784 (392 surf) |
| `BitShift` | 11–18 | ORT executed cleanly; scorer | `X`: B-1-H-1\*/ui32\*/alternating\*<br>`Y`: scalar\*/ui32\*/alternating\* | `direction=RIGHT\*` | example (1/93) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer` | 8/744 (744 surf) |
| `BitwiseAnd` | 18 | ORT executed cleanly; scorer | `A`: scalar\*/i16\*/random\*<br>`B`: scalar\*/i16\*/random\* | — | example (1/76) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node BitwiseAnd-BitwiseAnd_0 has no value_infer` | 1/74 (76 surf) |
| `BitwiseNot` | 18 | ORT executed cleanly; scorer | `X`: scalar\*/i16\*/alternating\* | — | example (1/96) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node BitwiseNot-BitwiseNot_0 has no value_infer` | 1/96 (96 surf) |
| `BitwiseOr` | 18 | ORT executed cleanly; scorer | `A`: scalar\*/i16\*/random\*<br>`B`: scalar\*/i16\*/random\* | — | example (1/76) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node BitwiseOr-BitwiseOr_0 has no value_infer` | 1/74 (76 surf) |
| `BitwiseXor` | 18 | ORT executed cleanly; scorer | `A`: scalar\*/i16\*/random\*<br>`B`: scalar\*/i16\*/random\* | — | example (1/76) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node BitwiseXor-BitwiseXor_0 has no value_infer` | 1/74 (76 surf) |
| `Cast` | 11–18 | ORT executed cleanly; scorer | `input`: scalar\*/bool\*/alternating\* | `to=1\*` | example (1/128) | `ORT executed cleanly; scorer: checker: ValidationError: Field 'shape' of 'type' is required but missing.` | 8/1024 (1024 surf) |
| `CastLike` | 15–18 | ORT executed cleanly; scorer | `input`: scalar\*/bool\*/random\*<br>`target_type`: scalar\*/bool\*/random\* | — | example (1/128) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer` | 4/512 (512 surf) |
| `Celu` | 12–18 | ORT executed cleanly; scorer | `X`: scalar\*/f32/alternating\* | — | example (1/48) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer` | 7/336 (336 surf) |
| `CenterCropPad` | 18 | ORT executed cleanly; scorer | `input_data`: BCHW/bool\*/sparse\*<br>`shape`: scalar/i64/alternating\* | `axes=[1]\*` | example (1/10) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node CenterCropPad-CenterCropPad_0 has no value_infer` | 1/10 (10 surf) |
| `Compress` | 11–18 | ORT executed cleanly; scorer | `input`: BCHW\*/f16\*/alternating\*<br>`condition`: scalar\*/bool/all_false\* | — | example (1/126) | `ORT executed cleanly; scorer: checker: InferenceError: [ShapeInferenceError] Inference error(s): (op_type:Compress): [ShapeInferenceError] I` | 8/1016 (1008 surf) |
| `Constant` | 11–18 | ORT executed cleanly; scorer | — | `value_int=0\*` | example (1/127) | `ORT executed cleanly; scorer: checker: ValidationError: Field 'shape' of 'type' is required but missing.` | 8/890 (890 surf) |
| `Conv` | 11–18 | ORT executed cleanly; scorer | `X`: B-C-1-1\*/f32\*/sparse\*<br>`W`: B-C-1-1\*/f32\*/sparse\*<br>`B` (init): scalar\*/f32\*/sparse\* | `kernel_shape=[1, 1]\*, auto_pad=NOTSET\*, dilations=[1, 1]\*, pads=[1, 1, 1, 1]\*` | example (1/10) | `ORT executed cleanly; scorer: checker: InferenceError: [ShapeInferenceError] Inference error(s): (op_type:Conv): [ShapeInferenceError] Infer` | 8/88 (80 surf) |
| `ConvInteger` | 11–18 | ORT executed cleanly; scorer | `x`: BCHW/i8/random<br>`w`: B-C-1-1/ui8/random | — | **required** | `ORT executed cleanly; scorer: checker: ValidationError: Field 'shape' of 'type' is required but missing.` | 8/24 |
| `Cosh` | 11–18 | ORT executed cleanly; scorer | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `ORT executed cleanly; scorer: onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer` | 8/192 (192 surf) |
| `DequantizeLinear` | 11–18 | ORT executed cleanly; scorer | `x`: B-C-1-1\*/i32\*/alternating\*<br>`x_scale` (init): scalar/f32/sparse\* | — | example (1/19) | `ORT executed cleanly; scorer: checker: InferenceError: [ShapeInferenceError] Inference error(s): (op_type:DequantizeLinear): [ShapeInference` | 8/96 (88 surf) |
| `Det` | 11–18 | ORT executed cleanly; scorer | `X`: B-C-1-1\*/f16\*/alternating\* | — | example (1/12) | `ORT executed cleanly; scorer: checker: InferenceError: [ShapeInferenceError] Inference error(s): (op_type:Det): [ShapeInferenceError] Inferr` | 8/96 (96 surf) |
| `Div` | 11–18 | ORT executed cleanly; scorer | `A`: scalar\*/f32/random<br>`B`: B-C-1-1\*/f32/random | — | example (1/2) | `ORT executed cleanly; scorer: checker: InferenceError: [ShapeInferenceError] Inference error(s): (op_type:Div): [ShapeInferenceError] Inferr` | 8/8 (16 surf) |
