# Structured onnx_tool issue report

Confirmed divergences vs. ORT, grouped by `(op, family, opsets)`. **134 issues**: 5 type, 79 shape, 50 error.

**Columns:**
- **Inputs**: each port shown as `name: shape/dtype/fill`. `(init)` marks initializer (constant input).
- **Attrs**: op attributes used in the failing case.
- **`*` suffix** on any field means it *varies* across triggers — the shown value is just one example and other values also reproduce the bug. Unmarked values are required (consistent across all triggers).
- **Repro**: `required` if a single Inputs+Attrs configuration triggers the bug; `example (1/N)` if N distinct configurations trigger it (we show the simplest).
- **Cases**: `hits/valid_cases` — how many ORT-valid configurations onnx_tool got wrong. Trailing `(N surf)` means N raw findings collapsed into the same group.

## Incorrect Type

| Op | Opsets | Inputs | Attrs | Repro | ORT | onnx_tool | Cases |
|---|---|---|---|---|---|---|---|
| `Round` | 11–18 | `X`: scalar\*/f16/alternating\* | — | example (1/12) | `float16` | `bool` | 96/288 |
| `Round` | 11–18 | `X`: scalar\*/f32/alternating\* | — | example (1/12) | `float32` | `bool` | 96/288 |
| `Round` | 11–18 | `X`: scalar\*/f64/alternating\* | — | example (1/12) | `float64` | `bool` | 96/288 |
| `ReduceL2` | 11–17 | `data`: scalar\*/i32/alternating\* | `keepdims=0\*` | example (1/25) | `int32` | `float64` | 94/590 |
| `ReduceL2` | 11–18 | `data`: scalar\*/i64/alternating\* | `keepdims=0\*` | example (1/26) | `int64` | `float64` | 89/655 |

## Incorrect Shape

| Op | Opsets | Family | Inputs | Attrs | Repro | ORT shape | onnx_tool shape | Cases |
|---|---|---|---|---|---|---|---|---|
| `BatchNormalization` | 11–13 | rank mismatch | `X`: B-C-1-1/f64\*/sparse\*<br>`scale`: 1d-10/f64\*/alternating\*<br>`B`: 1d-10/f64\*/sparse\*<br>`mean`: 1d-10/f64\*/alternating\*<br>`var`: 1d-10/f64\*/sparse\* | `epsilon=0.0\*` | example (1/11) | `(10,)` | `(1, 10, 1, 1)` | 33/384 (132 surf) |
| `LayerNormalization` | 17–18 | rank mismatch | `X`: BCHW\*/f64\*/alternating\*<br>`Scale`: B-C-1-1\*/f64\*/random\* | `axis=1\*, stash_type=1\*` | example (1/25) | `(1, 1, 1, 1)` | `()` | 50/214 (74 surf) |
| `Squeeze` | 11–12 | rank mismatch | `data`: B-1-H-1\*/f64\*/alternating\* | — | example (1/18) | `(30,)` | `(1, 30, 1)` | 36/158 |
| `Abs` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/29) | `()` | `()` | 232/1024 |
| `Add` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f64\*/random\*<br>`B`: scalar/f64\*/alternating\* | — | example (1/4) | `()` | `()` | 17/584 |
| `And` | 11–18 | scalar counted as 0 bytes | `A`: scalar/bool/all_true<br>`B`: scalar/bool/all_true\* | — | example (1/3) | `()` | `()` | 24/1024 |
| `Atan` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16\*/alternating\* | — | example (1/6) | `()` | `()` | 48/192 |
| `Cast` | 11–18 | scalar counted as 0 bytes | `input`: scalar/bool\*/alternating\* | `to=1\*` | example (1/20) | `()` | `()` | 160/1024 |
| `Ceil` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `Clip` | 11–18 | scalar counted as 0 bytes | `input`: B-C-1-1\*/f32\*/random\*<br>`min` (init): scalar/f32\*/alternating\* | — | example (1/6) | `()` | `()` | 13/21 (33 surf) |
| `Constant` | 11–18 | scalar counted as 0 bytes | — | `value=data_type: 1 name: "attr_value" raw_data: "\000\000\200?"` | example (1/41) | `()` | `()` | 288/890 |
| `Conv` | 11–18 | scalar counted as 0 bytes | `X`: B-C-1-1/f16\*/alternating\*<br>`W`: B-C-1-1/f16\*/random\*<br>`B` (init): scalar/f16\*/sparse | `kernel_shape=[1, 1], pads=[0, 0, 0, 0]\*` | example (1/2) | `()` | `()` | 16/88 |
| `ConvInteger` | 11–18 | scalar counted as 0 bytes | `x`: B-C-1-1\*/i8\*/random\*<br>`w`: B-C-1-1/i8\*/sparse\*<br>`x_zero_point` (init): scalar/i8\*/alternating\*<br>`w_zero_point` (init): scalar/i8\*/sparse\* | `group=1, dilations=[1, 1]\*, auto_pad=NOTSET\*, kernel_shape=[1, 1], strides=[1, 1]\*` | example (1/2) | `()` | `()` | 16/24 (32 surf) |
| `Cos` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16\*/alternating\* | — | example (1/6) | `()` | `()` | 48/192 |
| `DequantizeLinear` | 11–18 | scalar counted as 0 bytes | `x`: B-C-1-1\*/i32\*/alternating\*<br>`x_scale` (init): scalar/f32/sparse\* | — | example (1/21) | `()` | `()` | 96/96 (176 surf) |
| `Dropout` | 11–18 | scalar counted as 0 bytes | `data`: scalar\*/f32\*/alternating\* | — | example (1/24) | `()` | `()` | 78/198 (163 surf) |
| `Elu` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f32\*/alternating\* | — | example (1/20) | `()` | `()` | 139/751 |
| `Equal` | 11–18 | scalar counted as 0 bytes | `A`: scalar/bool/random<br>`B`: scalar/bool/random | — | **required** | `()` | `()` | 8/464 |
| `Erf` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16\*/alternating\* | — | example (1/6) | `()` | `()` | 48/192 |
| `Exp` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `Floor` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `Greater` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | **required** | `()` | `()` | 8/536 |
| `GreaterOrEqual` | 12–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | **required** | `()` | `()` | 7/469 |
| `HardSigmoid` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f32\*/alternating\* | — | example (1/17) | `()` | `()` | 115/772 |
| `HardSwish` | 14–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 33/132 |
| `Identity` | 11–18 | scalar counted as 0 bytes | `input`: scalar/bool\*/alternating\* | — | example (1/20) | `()` | `()` | 160/1024 |
| `LayerNormalization` | 17–18 | scalar counted as 0 bytes | `X`: B-C-1-1\*/f64\*/alternating\*<br>`Scale`: B-C-1-1\*/f64\*/sparse\*<br>`B` (init): scalar/f64\*/sparse\* | `axis=-1\*, epsilon=0.5\*, stash_type=1\*` | example (1/15) | `()` | `()` | 30/214 |
| `LeakyRelu` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f32\*/alternating\* | — | example (1/20) | `()` | `()` | 145/829 |
| `Less` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | **required** | `()` | `()` | 8/536 |
| `LessOrEqual` | 12–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | **required** | `()` | `()` | 7/469 |
| `Log` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `MatMulInteger` | 11–18 | scalar counted as 0 bytes | `A`: BCHW\*/ui8\*/random<br>`B`: B-1-H-1\*/ui8\*/random\*<br>`a_zero_point` (init): scalar/ui8\*/sparse\* | — | example (1/2) | `()` | `()` | 16/40 (24 surf) |
| `Max` | 11–18 | scalar counted as 0 bytes | `data_0`: scalar/f16\*/alternating\* | — | example (1/23) | `()` | `()` | 170/764 |
| `Min` | 11–18 | scalar counted as 0 bytes | `data_0`: scalar/f16\*/alternating\* | — | example (1/23) | `()` | `()` | 170/764 |
| `Mul` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f64\*/random\*<br>`B`: scalar/f64\*/alternating\* | — | example (1/4) | `()` | `()` | 17/584 |
| `Neg` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/21) | `()` | `()` | 168/672 |
| `Not` | 11–18 | scalar counted as 0 bytes | `X`: scalar/bool/all_true\* | — | example (1/3) | `()` | `()` | 24/96 |
| `Or` | 11–18 | scalar counted as 0 bytes | `A`: scalar/bool/all_true<br>`B`: scalar/bool/all_true\* | — | example (1/3) | `()` | `()` | 24/1024 |
| `PRelu` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f64\*/random\*<br>`slope`: scalar/f64\*/alternating\* | — | example (1/4) | `()` | `()` | 27/299 |
| `Pow` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random<br>`Y`: scalar/f16/random | — | **required** | `()` | `()` | 8/541 |
| `QuantizeLinear` | 11–18 | scalar counted as 0 bytes | `x`: scalar\*/f32/random\*<br>`y_scale` (init): scalar/f32/random\*<br>`y_zero_point` (init): scalar/i8\*/random\* | — | example (1/9) | `()` | `()` | 48/48 (104 surf) |
| `RandomNormalLike` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/sparse\* | `seed=0.5, mean=0.0, scale=0.0\*` | example (1/2) | `()` | `()` | 16/80 |
| `RandomUniformLike` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/sparse\* | `low=0.5, high=0.0, seed=0.0\*` | example (1/2) | `()` | `()` | 16/80 |
| `Reciprocal` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `ReduceL2` | 11–18 | scalar counted as 0 bytes | `data`: scalar\*/f16\*/alternating\* | `keepdims=0\*` | example (1/15) | `()` | `()` | 61/655 |
| `ReduceMax` | 11–17 | scalar counted as 0 bytes | `data`: scalar/i32\*/alternating\* | `axes=[1]\*` | example (1/27) | `()` | `()` | 57/617 |
| `ReduceMean` | 11–17 | scalar counted as 0 bytes | `data`: scalar/f16\*/alternating\* | `keepdims=0\*` | example (1/8) | `()` | `()` | 30/590 |
| `ReduceMin` | 11–17 | scalar counted as 0 bytes | `data`: scalar/i32\*/alternating\* | `axes=[1]\*` | example (1/27) | `()` | `()` | 57/617 |
| `ReduceProd` | 11–17 | scalar counted as 0 bytes | `data`: scalar/f16\*/alternating\* | `keepdims=0\*` | example (1/8) | `()` | `()` | 30/590 |
| `ReduceSum` | 11–12 | scalar counted as 0 bytes | `data`: scalar/f16\*/alternating\* | `keepdims=0\*` | example (1/5) | `()` | `()` | 10/170 |
| `Relu` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/18) | `()` | `()` | 105/420 |
| `Sigmoid` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `Sign` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16\*/alternating\* | — | example (1/29) | `()` | `()` | 232/1024 |
| `Sin` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `Softplus` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 51/204 |
| `Sqrt` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `Squeeze` | 11–12 | scalar counted as 0 bytes | `data`: scalar/f32\*/alternating\* | — | example (1/5) | `()` | `()` | 10/158 |
| `Sub` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f64\*/random\*<br>`B`: scalar/f64\*/alternating\* | — | example (1/4) | `()` | `()` | 17/584 |
| `Sum` | 11–18 | scalar counted as 0 bytes | `data_0`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `Tanh` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16\*/alternating\* | — | example (1/9) | `()` | `()` | 72/288 |
| `Transpose` | 11–18 | scalar counted as 0 bytes | `data`: scalar/f16\*/random | — | example (1/6) | `()` | `()` | 48/912 |
| `Xor` | 11–18 | scalar counted as 0 bytes | `A`: scalar/bool/all_true<br>`B`: scalar/bool/all_true\* | — | example (1/3) | `()` | `()` | 24/1024 |
| `AveragePool` | 11–18 | shape overcount | `X`: B-1-H-1\*/f32\*/alternating\* | `kernel_shape=[1, 1], strides=[2, 2], auto_pad=NOTSET\*, pads=[0, 0, 0, 0]\*, ceil_mode=1` | example (1/3) | `(1, 1, 15, 1)` | `(1, 1, 16, 1)` | 24/784 |
| `BatchNormalization` | 11–13 | shape overcount | `X`: B-1-H-1\*/f16\*/random\*<br>`scale`: 1d-1\*/f16\*/random\*<br>`B`: 1d-1\*/f16\*/random\*<br>`mean`: 1d-1\*/f16\*/random\*<br>`var`: 1d-1\*/f16\*/random\* | `momentum=0.5\*` | example (1/51) | `(1,)` | `(1, 1, 30, 1)` | 153/384 (612 surf) |
| `GatherND` | 12–18 | shape overcount | `data`: BCHW/i32\*/alternating\*<br>`indices` (init): 1d-1/i64/sparse\* | `batch_dims=1` | example (1/20) | `(30, 30)` | `(10, 30, 30)` | 140/238 |
| `MaxPool` | 11–18 | shape overcount | `X`: B-1-H-1\*/f16\*/sparse\* | `kernel_shape=[1, 1]\*, strides=[2, 2], dilations=[1, 1]\*, auto_pad=NOTSET\*, ceil_mode=1` | example (1/7) | `(1, 1, 15, 1)` | `(1, 1, 16, 1)` | 25/1024 |
| `ReduceMax` | 11–18 | shape overcount | `data`: B-1-H-1\*/f32\*/alternating\* | — | example (1/50) | `(1, 1, 1, 1)` | `(1, 1, 30, 1)` | 127/686 |
| `ReduceMean` | 11–18 | shape overcount | `data`: B-1-H-1\*/f32\*/alternating\* | — | example (1/35) | `(1, 1, 1, 1)` | `(1, 1, 30, 1)` | 141/655 |
| `ReduceMin` | 11–18 | shape overcount | `data`: B-1-H-1\*/f32\*/alternating\* | — | example (1/50) | `(1, 1, 1, 1)` | `(1, 1, 30, 1)` | 127/686 |
| `ReduceProd` | 11–18 | shape overcount | `data`: B-1-H-1\*/f32\*/alternating\* | — | example (1/35) | `(1, 1, 1, 1)` | `(1, 1, 30, 1)` | 141/655 |
| `ReduceSum` | 11–18 | shape overcount | `data`: B-1-H-1\*/f32\*/alternating\* | — | example (1/21) | `(1, 1, 1, 1)` | `(1, 1, 30, 1)` | 76/560 |
| `Shape` | 15–18 | shape overcount | `data`: B-1-H-1\*/bool\*/alternating\* | `end=0\*` | example (1/83) | `(0,)` | `(4,)` | 332/512 |
| `LayerNormalization` | 17–18 | shape undercount | `X`: B-C-1-1\*/f64\*/alternating\*<br>`Scale`: B-C-1-1\*/f64\*/random\* | `axis=-1\*, epsilon=0.5\*` | example (1/29) | `(1, 10, 1, 1)` | `()` | 58/214 (88 surf) |
| `MaxPool` | 11–18 | shape undercount | `X`: B-1-H-1\*/f64\*/alternating\* | `kernel_shape=[1, 1]\*, strides=[1, 1]\*, dilations=[1, 1]\*, ceil_mode=1\*, storage_order=1\*` | example (1/109) | `(1, 1, 30, 1)` | `()` | 417/1024 |
| `PRelu` | 11–18 | shape undercount | `X`: B-C-1-1\*/f64\*/sparse\*<br>`slope`: B-1-H-1\*/f64\*/alternating\* | — | example (1/8) | `(1, 10, 30, 1)` | `(1, 1, 30, 1)` | 39/299 |
| `Pow` | 11 | shape undercount | `X`: B-C-1-1\*/f32\*/alternating\*<br>`Y`: B-1-H-1\*/f32\*/alternating\* | — | example (1/21) | `(1, 10, 30, 1)` | `(1, 1, 30, 1)` | 21/128 |
| `ReduceL2` | 18 | shape undercount | `data`: BCHW/i32\*/sparse\* | `noop_with_empty_axes=1\*` | example (1/57) | `(1, 10, 30, 30)` | `(1, 1, 1, 1)` | 57/65 |
| `Where` | 11–18 | shape undercount | `condition`: B-C-1-1/bool/all_false\*<br>`X`: scalar\*/f32\*/sparse\*<br>`Y`: B-1-H-1\*/f32\*/random | — | example (1/4) | `(1, 10, 30, 1)` | `(1, 1, 30, 1)` | 32/304 |
| `Flatten` | 11–18 | wrong shape | `input`: B-1-H-1\*/bool\*/alternating\* | `axis=-1` | example (1/27) | `(30, 1)` | `(1, 30)` | 216/904 |

## Incorrect Errors

| Op | Opsets | Family | Inputs | Attrs | Repro | onnx_tool error | Cases |
|---|---|---|---|---|---|---|---|
| `Constant` | 12–18 | AttributeError | — | `value_int=0\*` | example (1/86) | `AttributeError: 'ConstantNode' object has no attribute 'value'` | 602/889 |
| `Einsum` | 12–18 | IndexError | `Inputs`: scalar/f16\*/alternating\* | `equation=` | example (1/15) | `IndexError: list index out of range` | 105/105 |
| `Acos` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Acos-Acos_0 has no value_infer` | 192/192 |
| `Acosh` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Acosh-Acosh_0 has no value_infer` | 192/192 |
| `ArgMin` | 11–18 | NotImplementedError | `data`: B-1-H-1\*/f32\*/alternating\* | — | example (1/111) | `NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer` | 504/504 |
| `Asin` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Asin-Asin_0 has no value_infer` | 192/192 |
| `Asinh` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Asinh-Asinh_0 has no value_infer` | 192/192 |
| `Atanh` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Atanh-Atanh_0 has no value_infer` | 192/192 |
| `BitShift` | 11–18 | NotImplementedError | `X`: B-1-H-1\*/ui32\*/alternating\*<br>`Y`: scalar\*/ui32\*/alternating\* | `direction=LEFT\*` | example (1/93) | `NotImplementedError: this Node BitShift-BitShift_0 has no value_infer` | 744/744 |
| `BitwiseAnd` | 18 | NotImplementedError | `A`: scalar\*/i16\*/random\*<br>`B`: scalar\*/i16\*/random\* | — | example (1/74) | `NotImplementedError: this Node BitwiseAnd-BitwiseAnd_0 has no value_infer` | 74/74 |
| `BitwiseNot` | 18 | NotImplementedError | `X`: scalar\*/i16\*/alternating\* | — | example (1/96) | `NotImplementedError: this Node BitwiseNot-BitwiseNot_0 has no value_infer` | 96/96 |
| `BitwiseOr` | 18 | NotImplementedError | `A`: scalar\*/i16\*/random\*<br>`B`: scalar\*/i16\*/random\* | — | example (1/74) | `NotImplementedError: this Node BitwiseOr-BitwiseOr_0 has no value_infer` | 74/74 |
| `BitwiseXor` | 18 | NotImplementedError | `A`: scalar\*/i16\*/random\*<br>`B`: scalar\*/i16\*/random\* | — | example (1/74) | `NotImplementedError: this Node BitwiseXor-BitwiseXor_0 has no value_infer` | 74/74 |
| `CastLike` | 15–18 | NotImplementedError | `input`: scalar\*/bool\*/random\*<br>`target_type`: scalar\*/bool\*/random\* | — | example (1/128) | `NotImplementedError: this Node CastLike-CastLike_0 has no value_infer` | 512/512 |
| `Celu` | 12–18 | NotImplementedError | `X`: scalar\*/f32/alternating\* | — | example (1/48) | `NotImplementedError: this Node Celu-Celu_0 has no value_infer` | 336/336 |
| `CenterCropPad` | 18 | NotImplementedError | `input_data`: BCHW/i8\*/alternating\*<br>`shape`: scalar/i64/sparse\* | — | example (1/10) | `NotImplementedError: this Node CenterCropPad-CenterCropPad_0 has no value_infer` | 10/10 |
| `Cosh` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Cosh-Cosh_0 has no value_infer` | 192/192 |
| `Det` | 11–18 | NotImplementedError | `X`: B-C-1-1\*/f16\*/alternating\* | — | example (1/12) | `NotImplementedError: this Node Det-Det_0 has no value_infer` | 96/96 |
| `DynamicQuantizeLinear` | 11–18 | NotImplementedError | `x`: scalar\*/f32/alternating\* | — | example (1/12) | `NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer` | 96/96 |
| `GlobalLpPool` | 11–18 | NotImplementedError | `X`: B-1-H-1\*/f32\*/alternating\* | — | example (1/72) | `NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer` | 576/576 |
| `GlobalMaxPool` | 11–18 | NotImplementedError | `X`: B-1-H-1\*/f16\*/alternating\* | — | example (1/18) | `NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer` | 144/144 |
| `IsInf` | 11–18 | NotImplementedError | `X`: scalar\*/f32\*/alternating\* | `detect_negative=0\*` | example (1/128) | `NotImplementedError: this Node IsInf-IsInf_0 has no value_infer` | 1024/1024 |
| `IsNaN` | 11–18 | NotImplementedError | `X`: scalar\*/f16\*/alternating\* | — | example (1/36) | `NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer` | 288/288 |
| `LpPool` | 11–18 | NotImplementedError | `X`: B-1-H-1\*/f32\*/alternating\* | `kernel_shape=[1, 1]\*, strides=[1, 1]\*, p=0\*` | example (1/193) | `NotImplementedError: this Node LpPool-LpPool_0 has no value_infer` | 808/808 |
| `Mean` | 11–18 | NotImplementedError | `data_0`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Mean-Mean_0 has no value_infer` | 192/192 |
| `MeanVarianceNormalization` | 11–18 | NotImplementedError | `X`: B-1-H-1\*/f32\*/alternating\* | — | example (1/72) | `NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer` | 504/504 |
| `Mish` | 18 | NotImplementedError | `X`: scalar\*/f16\*/alternating\* | — | example (1/36) | `NotImplementedError: this Node Mish-Mish_0 has no value_infer` | 36/36 |
| `OptionalGetElement` | 18 | NotImplementedError | `input`: scalar\*/bool/alternating\* | — | example (1/12) | `NotImplementedError: this Node OptionalGetElement-OptionalGetElement_0 has no value_infer` | 12/12 |
| `OptionalHasElement` | 18 | NotImplementedError | — | — | example (1/119) | `NotImplementedError: this Node OptionalHasElement-OptionalHasElement_0 has no value_infer` | 119/128 |
| `RandomNormal` | 11–18 | NotImplementedError | — | `shape=[1]\*` | example (1/85) | `NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer` | 680/680 |
| `RandomUniform` | 11–18 | NotImplementedError | — | `shape=[1]\*` | example (1/85) | `NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer` | 680/680 |
| `ReduceL1` | 11–18 | NotImplementedError | `data`: scalar\*/f16\*/alternating\* | `keepdims=0\*` | example (1/223) | `NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer` | 655/655 |
| `ReduceLogSum` | 11–18 | NotImplementedError | `data`: scalar\*/f16\*/alternating\* | `keepdims=0\*` | example (1/223) | `NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer` | 655/655 |
| `ReduceLogSumExp` | 11–18 | NotImplementedError | `data`: scalar\*/f16\*/alternating\* | `keepdims=0\*` | example (1/245) | `NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer` | 677/677 |
| `ReduceSumSquare` | 11–18 | NotImplementedError | `data`: scalar\*/f16\*/alternating\* | `keepdims=0\*` | example (1/223) | `NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer` | 655/655 |
| `ReverseSequence` | 11–18 | NotImplementedError | `input`: BCHW/i8\*/alternating\*<br>`sequence_lens` (init): 1d-10\*/i64/alternating\* | — | example (1/36) | `NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer` | 288/288 |
| `Selu` | 11–18 | NotImplementedError | `X`: scalar\*/f32\*/alternating\* | — | example (1/128) | `NotImplementedError: this Node Selu-Selu_0 has no value_infer` | 772/772 |
| `Shrink` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | `bias=0.5\*` | example (1/128) | `NotImplementedError: this Node Shrink-Shrink_0 has no value_infer` | 1024/1024 |
| `Sinh` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Sinh-Sinh_0 has no value_infer` | 192/192 |
| `Size` | 11–18 | NotImplementedError | `data`: scalar\*/bool\*/alternating\* | — | example (1/128) | `NotImplementedError: this Node Size-Size_0 has no value_infer` | 1024/1024 |
| `Softsign` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/36) | `NotImplementedError: this Node Softsign-Softsign_0 has no value_infer` | 204/204 |
| `SpaceToDepth` | 11–18 | NotImplementedError | `input`: B-1-H-1\*/f32\*/alternating\* | `blocksize=1` | example (1/14) | `NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer` | 112/112 |
| `Tan` | 11–18 | NotImplementedError | `input`: scalar\*/f16\*/alternating\* | — | example (1/24) | `NotImplementedError: this Node Tan-Tan_0 has no value_infer` | 192/192 |
| `ThresholdedRelu` | 11–18 | NotImplementedError | `X`: scalar\*/f32\*/alternating\* | — | example (1/128) | `NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer` | 751/751 |
| `Unique` | 11–18 | NotImplementedError | `X`: B-1-H-1\*/f64\*/alternating\* | — | example (1/45) | `NotImplementedError: this Node Unique-Unique_0 has no value_infer` | 360/360 |
| `Split` | 11–18 | TypeError | `input`: B-1-H-1\*/f64\*/alternating\* | — | example (1/26) | `TypeError: list indices must be integers or slices, not NoneType` | 79/272 |
| `TopK` | 11–18 | TypeError | `X`: BCHW/i32\*/alternating\*<br>`K` (init): 1d-10\*/i64/alternating\* | — | example (1/23) | `TypeError: '<' not supported between instances of 'NoneType' and 'int'` | 184/544 |
| `Compress` | 11–18 | ValueError | `input`: BCHW\*/i64\*/alternating\*<br>`condition`: scalar\*/bool/all_false\* | — | example (1/127) | `ValueError: condition must be a 1-d array` | 1016/1016 |
| `NonZero` | 11–18 | ValueError | `X`: scalar/bool\*/alternating\* | — | example (1/14) | `ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the` | 112/544 |
| `OptionalHasElement` | 18 | ValueError | `input` (init): B-1-H-1\*/ui32/alternating\* | — | example (1/9) | `ValueError: cannot reshape array of size 15 into shape (1,1,30,1)` | 9/128 |
