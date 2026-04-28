# Structured onnx_tool issue report

Confirmed divergences vs. ORT, grouped by `(op, family, opsets)`. **134 issues**: 5 type, 79 shape, 50 error.

**Columns:**
- **Inputs**: each port shown as `name: shape/dtype/fill`. `(init)` marks initializer (constant input).
- **Attrs**: op attributes used in the failing case.
- **Cases**: `hits/valid_cases` — how many ORT-valid configurations onnx_tool got wrong.
  Trailing `(N surf)` means N raw findings collapsed into the same group.

## Incorrect Type

| Op | Opsets | Inputs | Attrs | ORT | onnx_tool | Cases |
|---|---|---|---|---|---|---|
| `Round` | 11–18 | `X`: BCHW/f16/random | — | `float16` | `bool` | 96/288 |
| `Round` | 11–18 | `X`: BCHW/f32/random | — | `float32` | `bool` | 96/288 |
| `Round` | 11–18 | `X`: BCHW/f64/random | — | `float64` | `bool` | 96/288 |
| `ReduceL2` | 11–17 | `data`: BCHW/i32/random | `axes=[2, 3]` | `int32` | `float64` | 94/590 |
| `ReduceL2` | 11–18 | `data`: BCHW/i64/random | `keepdims=1` | `int64` | `float64` | 89/655 |

## Incorrect Shape

| Op | Opsets | Family | Inputs | Attrs | ORT shape | onnx_tool shape | Cases |
|---|---|---|---|---|---|---|---|
| `BatchNormalization` | 11–13 | rank mismatch | `X`: B-C-1-1/f16/sparse<br>`scale`: 1d-10/f16/sparse<br>`B`: 1d-10/f16/sparse<br>`mean`: 1d-10/f16/sparse<br>`var`: 1d-10/f16/sparse | `epsilon=1.0, momentum=0.0` | `(10,)` | `(1, 10, 1, 1)` | 33/384 (132 surf) |
| `LayerNormalization` | 17–18 | rank mismatch | `X`: BCHW/f32/random<br>`Scale`: BCHW/f32/random<br>`B` (init): BCHW/f32/random | `axis=0` | `(1, 1, 1, 1)` | `()` | 50/214 (74 surf) |
| `Squeeze` | 11–12 | rank mismatch | `data`: B-C-1-1/bool/alternating | — | `(10,)` | `(10, 1, 1)` | 36/158 |
| `Abs` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 232/1024 |
| `Add` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | `()` | `()` | 17/584 |
| `And` | 11–18 | scalar counted as 0 bytes | `A`: scalar/bool/all_true<br>`B`: scalar/bool/all_true | — | `()` | `()` | 24/1024 |
| `Atan` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | — | `()` | `()` | 48/192 |
| `Cast` | 11–18 | scalar counted as 0 bytes | `input`: scalar/bool/random | `to=10` | `()` | `()` | 160/1024 |
| `Ceil` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `Clip` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random<br>`min` (init): scalar/f16/random<br>`max` (init): scalar/f16/random | — | `()` | `()` | 13/21 (33 surf) |
| `Constant` | 11–18 | scalar counted as 0 bytes | — | `value=data_type: 1 name: "attr_value" raw_data: "\000\000\200?"` | `()` | `()` | 288/890 |
| `Conv` | 11–18 | scalar counted as 0 bytes | `X`: B-C-1-1/f16/alternating<br>`W`: B-C-1-1/f16/random<br>`B` (init): scalar/f16/sparse | `kernel_shape=[1, 1], pads=[0, 0, 0, 0]` | `()` | `()` | 16/88 |
| `ConvInteger` | 11–18 | scalar counted as 0 bytes | `x`: BCHW/ui8/sparse<br>`w`: B-C-1-1/ui8/random<br>`x_zero_point` (init): scalar/ui8/sparse<br>`w_zero_point` (init): scalar/ui8/random | `group=1, auto_pad=SAME_UPPER, kernel_shape=[1, 1]` | `()` | `()` | 16/24 (32 surf) |
| `Cos` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | — | `()` | `()` | 48/192 |
| `DequantizeLinear` | 11–18 | scalar counted as 0 bytes | `x`: scalar/i32/random<br>`x_scale` (init): scalar/f32/random<br>`x_zero_point` (init): scalar/i32/random | — | `()` | `()` | 96/96 (176 surf) |
| `Dropout` | 11–18 | scalar counted as 0 bytes | `data`: scalar/f16/random | `ratio=1.0` | `()` | `()` | 78/198 (163 surf) |
| `Elu` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | `alpha=1.0` | `()` | `()` | 139/751 |
| `Equal` | 11–18 | scalar counted as 0 bytes | `A`: scalar/bool/random<br>`B`: scalar/bool/random | — | `()` | `()` | 8/464 |
| `Erf` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | — | `()` | `()` | 48/192 |
| `Exp` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `Floor` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `Greater` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | `()` | `()` | 8/536 |
| `GreaterOrEqual` | 12–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | `()` | `()` | 7/469 |
| `HardSigmoid` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | `alpha=0.0, beta=0.0` | `()` | `()` | 115/772 |
| `HardSwish` | 14–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 33/132 |
| `Identity` | 11–18 | scalar counted as 0 bytes | `input`: scalar/bool/random | — | `()` | `()` | 160/1024 |
| `LayerNormalization` | 17–18 | scalar counted as 0 bytes | `X`: BCHW/f16/sparse<br>`Scale`: B-1-H-1/f16/sparse<br>`B` (init): scalar/f16/sparse | `epsilon=0.5, stash_type=0` | `()` | `()` | 30/214 |
| `LeakyRelu` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | `alpha=1.0` | `()` | `()` | 145/829 |
| `Less` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | `()` | `()` | 8/536 |
| `LessOrEqual` | 12–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | `()` | `()` | 7/469 |
| `Log` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `MatMulInteger` | 11–18 | scalar counted as 0 bytes | `A`: BCHW/ui8/random<br>`B`: B-1-H-1/ui8/random<br>`a_zero_point` (init): scalar/ui8/sparse | — | `()` | `()` | 16/40 (24 surf) |
| `Max` | 11–18 | scalar counted as 0 bytes | `data_0`: scalar/f16/random | — | `()` | `()` | 170/764 |
| `Min` | 11–18 | scalar counted as 0 bytes | `data_0`: scalar/f16/random | — | `()` | `()` | 170/764 |
| `Mul` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | `()` | `()` | 17/584 |
| `Neg` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 168/672 |
| `Not` | 11–18 | scalar counted as 0 bytes | `X`: scalar/bool/all_true | — | `()` | `()` | 24/96 |
| `Or` | 11–18 | scalar counted as 0 bytes | `A`: scalar/bool/all_true<br>`B`: scalar/bool/all_true | — | `()` | `()` | 24/1024 |
| `PRelu` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random<br>`slope`: scalar/f16/random | — | `()` | `()` | 27/299 |
| `Pow` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random<br>`Y`: scalar/f16/random | — | `()` | `()` | 8/541 |
| `QuantizeLinear` | 11–18 | scalar counted as 0 bytes | `x`: scalar/f32/random<br>`y_scale` (init): scalar/f32/random<br>`y_zero_point` (init): scalar/i8/random | — | `()` | `()` | 48/48 (104 surf) |
| `RandomNormalLike` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | `seed=0.5, mean=0.0, dtype=10` | `()` | `()` | 16/80 |
| `RandomUniformLike` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | `low=0.5, high=0.0, dtype=10` | `()` | `()` | 16/80 |
| `Reciprocal` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `ReduceL2` | 11–18 | scalar counted as 0 bytes | `data`: B-C-1-1/f64/random | `keepdims=0` | `()` | `()` | 61/655 |
| `ReduceMax` | 11–17 | scalar counted as 0 bytes | `data`: scalar/f16/random | `axes=[2, 3], keepdims=0` | `()` | `()` | 57/617 |
| `ReduceMean` | 11–17 | scalar counted as 0 bytes | `data`: scalar/f16/sparse | `keepdims=1` | `()` | `()` | 30/590 |
| `ReduceMin` | 11–17 | scalar counted as 0 bytes | `data`: scalar/f16/random | `axes=[2, 3], keepdims=0` | `()` | `()` | 57/617 |
| `ReduceProd` | 11–17 | scalar counted as 0 bytes | `data`: scalar/f16/sparse | `keepdims=1` | `()` | `()` | 30/590 |
| `ReduceSum` | 11–12 | scalar counted as 0 bytes | `data`: scalar/f16/sparse | `keepdims=1` | `()` | `()` | 10/170 |
| `Relu` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 105/420 |
| `Sigmoid` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `Sign` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | — | `()` | `()` | 232/1024 |
| `Sin` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `Softplus` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 51/204 |
| `Sqrt` | 11–18 | scalar counted as 0 bytes | `X`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `Squeeze` | 11–12 | scalar counted as 0 bytes | `data`: scalar/bool/random | — | `()` | `()` | 10/158 |
| `Sub` | 11–18 | scalar counted as 0 bytes | `A`: scalar/f16/random<br>`B`: scalar/f16/random | — | `()` | `()` | 17/584 |
| `Sum` | 11–18 | scalar counted as 0 bytes | `data_0`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `Tanh` | 11–18 | scalar counted as 0 bytes | `input`: scalar/f16/random | — | `()` | `()` | 72/288 |
| `Transpose` | 11–18 | scalar counted as 0 bytes | `data`: scalar/f16/random | — | `()` | `()` | 48/912 |
| `Xor` | 11–18 | scalar counted as 0 bytes | `A`: scalar/bool/all_true<br>`B`: scalar/bool/all_true | — | `()` | `()` | 24/1024 |
| `AveragePool` | 11–18 | shape overcount | `X`: B-1-H-1/f32/alternating | `kernel_shape=[1, 1], strides=[2, 2], auto_pad=NOTSET, pads=[0, 0, 0, 0], ceil_mode=1` | `(1, 1, 15, 1)` | `(1, 1, 16, 1)` | 24/784 |
| `BatchNormalization` | 11–13 | shape overcount | `X`: BCHW/f32/random<br>`scale`: 1d-10/f32/random<br>`B`: 1d-10/f32/random<br>`mean`: 1d-10/f32/random<br>`var`: 1d-10/f32/random | `epsilon=0.0` | `(10,)` | `(1, 10, 30, 30)` | 153/384 (612 surf) |
| `GatherND` | 12–18 | shape overcount | `data`: BCHW/f32/random<br>`indices` (init): 1d-1/i64/random | `batch_dims=1` | `(30, 30)` | `(10, 30, 30)` | 140/238 |
| `MaxPool` | 11–18 | shape overcount | `X`: B-1-H-1/f16/sparse | `kernel_shape=[1, 1], strides=[2, 2], dilations=[1, 1], auto_pad=NOTSET, ceil_mode=1` | `(1, 1, 15, 1)` | `(1, 1, 16, 1)` | 25/1024 |
| `ReduceMax` | 11–18 | shape overcount | `data`: BCHW/f16/random | — | `(1, 1, 1, 1)` | `(1, 10, 30, 30)` | 127/686 |
| `ReduceMean` | 11–18 | shape overcount | `data`: BCHW/f16/random | — | `(1, 1, 1, 1)` | `(1, 10, 30, 30)` | 141/655 |
| `ReduceMin` | 11–18 | shape overcount | `data`: BCHW/f16/random | — | `(1, 1, 1, 1)` | `(1, 10, 30, 30)` | 127/686 |
| `ReduceProd` | 11–18 | shape overcount | `data`: BCHW/f16/random | — | `(1, 1, 1, 1)` | `(1, 10, 30, 30)` | 141/655 |
| `ReduceSum` | 11–18 | shape overcount | `data`: BCHW/f16/random | — | `(1, 1, 1, 1)` | `(1, 10, 30, 30)` | 76/560 |
| `Shape` | 15–18 | shape overcount | `data`: BCHW/f32/random | `start=1` | `(3,)` | `(4,)` | 332/512 |
| `LayerNormalization` | 17–18 | shape undercount | `X`: BCHW/f16/random<br>`Scale`: BCHW/f16/random<br>`B` (init): BCHW/f16/random | `axis=-1` | `(1, 10, 30, 1)` | `()` | 58/214 (88 surf) |
| `MaxPool` | 11–18 | shape undercount | `X`: BCHW/f32/random | `kernel_shape=[2, 2]` | `(1, 10, 29, 29)` | `()` | 417/1024 |
| `PRelu` | 11–18 | shape undercount | `X`: B-C-1-1/f16/random<br>`slope`: B-1-H-1/f16/alternating | — | `(1, 10, 30, 1)` | `(1, 1, 30, 1)` | 39/299 |
| `Pow` | 11 | shape undercount | `X`: B-C-1-1/f16/random<br>`Y`: B-1-H-1/f16/random | — | `(1, 10, 30, 1)` | `(1, 1, 30, 1)` | 21/128 |
| `ReduceL2` | 18 | shape undercount | `data`: BCHW/f16/alternating<br>`axes` (init): 1d-1/i64/alternating | `keepdims=0, noop_with_empty_axes=1` | `(1, 30, 30)` | `()` | 57/65 |
| `Where` | 11–18 | shape undercount | `condition`: B-C-1-1/bool/all_true<br>`X`: B-C-1-1/f32/sparse<br>`Y`: B-1-H-1/f32/random | — | `(1, 10, 30, 1)` | `(1, 1, 30, 1)` | 32/304 |
| `Flatten` | 11–18 | wrong shape | `input`: BCHW/f64/random | `axis=-1` | `(300, 30)` | `(1, 9000)` | 216/904 |

## Incorrect Errors

| Op | Opsets | Family | Inputs | Attrs | onnx_tool error | Cases |
|---|---|---|---|---|---|---|
| `Constant` | 12–18 | AttributeError | — | `value_string=` | `AttributeError: 'ConstantNode' object has no attribute 'value'` | 602/889 |
| `Einsum` | 12–18 | IndexError | `Inputs`: scalar/f16/random | `equation=` | `IndexError: list index out of range` | 105/105 |
| `Acos` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Acos-Acos_0 has no value_infer` | 192/192 |
| `Acosh` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Acosh-Acosh_0 has no value_infer` | 192/192 |
| `ArgMin` | 11–18 | NotImplementedError | `data`: BCHW/f16/random | — | `NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer` | 504/504 |
| `Asin` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Asin-Asin_0 has no value_infer` | 192/192 |
| `Asinh` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Asinh-Asinh_0 has no value_infer` | 192/192 |
| `Atanh` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Atanh-Atanh_0 has no value_infer` | 192/192 |
| `BitShift` | 11–18 | NotImplementedError | `X`: BCHW/ui32/random<br>`Y`: BCHW/ui32/random | `direction=RIGHT` | `NotImplementedError: this Node BitShift-BitShift_0 has no value_infer` | 744/744 |
| `BitwiseAnd` | 18 | NotImplementedError | `A`: BCHW/i16/random<br>`B`: BCHW/i16/random | — | `NotImplementedError: this Node BitwiseAnd-BitwiseAnd_0 has no value_infer` | 74/74 |
| `BitwiseNot` | 18 | NotImplementedError | `X`: BCHW/i16/random | — | `NotImplementedError: this Node BitwiseNot-BitwiseNot_0 has no value_infer` | 96/96 |
| `BitwiseOr` | 18 | NotImplementedError | `A`: BCHW/i16/random<br>`B`: BCHW/i16/random | — | `NotImplementedError: this Node BitwiseOr-BitwiseOr_0 has no value_infer` | 74/74 |
| `BitwiseXor` | 18 | NotImplementedError | `A`: BCHW/i16/random<br>`B`: BCHW/i16/random | — | `NotImplementedError: this Node BitwiseXor-BitwiseXor_0 has no value_infer` | 74/74 |
| `CastLike` | 15–18 | NotImplementedError | `input`: BCHW/bool/random<br>`target_type`: BCHW/bool/random | — | `NotImplementedError: this Node CastLike-CastLike_0 has no value_infer` | 512/512 |
| `Celu` | 12–18 | NotImplementedError | `X`: BCHW/f32/random | — | `NotImplementedError: this Node Celu-Celu_0 has no value_infer` | 336/336 |
| `CenterCropPad` | 18 | NotImplementedError | `input_data`: BCHW/bool/sparse<br>`shape`: scalar/i64/alternating | `axes=[2, 3]` | `NotImplementedError: this Node CenterCropPad-CenterCropPad_0 has no value_infer` | 10/10 |
| `Cosh` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Cosh-Cosh_0 has no value_infer` | 192/192 |
| `Det` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | — | `NotImplementedError: this Node Det-Det_0 has no value_infer` | 96/96 |
| `DynamicQuantizeLinear` | 11–18 | NotImplementedError | `x`: BCHW/f32/random | — | `NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer` | 96/96 |
| `GlobalLpPool` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | — | `NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer` | 576/576 |
| `GlobalMaxPool` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | — | `NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer` | 144/144 |
| `IsInf` | 11–18 | NotImplementedError | `X`: BCHW/f32/random | — | `NotImplementedError: this Node IsInf-IsInf_0 has no value_infer` | 1024/1024 |
| `IsNaN` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | — | `NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer` | 288/288 |
| `LpPool` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | `kernel_shape=[1, 1]` | `NotImplementedError: this Node LpPool-LpPool_0 has no value_infer` | 808/808 |
| `Mean` | 11–18 | NotImplementedError | `data_0`: BCHW/f16/random | — | `NotImplementedError: this Node Mean-Mean_0 has no value_infer` | 192/192 |
| `MeanVarianceNormalization` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | — | `NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer` | 504/504 |
| `Mish` | 18 | NotImplementedError | `X`: BCHW/f16/random | — | `NotImplementedError: this Node Mish-Mish_0 has no value_infer` | 36/36 |
| `OptionalGetElement` | 18 | NotImplementedError | `input`: BCHW/bool/random | — | `NotImplementedError: this Node OptionalGetElement-OptionalGetElement_0 has no value_infer` | 12/12 |
| `OptionalHasElement` | 18 | NotImplementedError | — | — | `NotImplementedError: this Node OptionalHasElement-OptionalHasElement_0 has no value_infer` | 119/128 |
| `RandomNormal` | 11–18 | NotImplementedError | — | `shape=[1]` | `NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer` | 680/680 |
| `RandomUniform` | 11–18 | NotImplementedError | — | `shape=[1]` | `NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer` | 680/680 |
| `ReduceL1` | 11–18 | NotImplementedError | `data`: BCHW/f16/random | — | `NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer` | 655/655 |
| `ReduceLogSum` | 11–18 | NotImplementedError | `data`: BCHW/f16/random | — | `NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer` | 655/655 |
| `ReduceLogSumExp` | 11–18 | NotImplementedError | `data`: BCHW/f16/random | — | `NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer` | 677/677 |
| `ReduceSumSquare` | 11–18 | NotImplementedError | `data`: BCHW/f16/random | — | `NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer` | 655/655 |
| `ReverseSequence` | 11–18 | NotImplementedError | `input`: BCHW/f64/random<br>`sequence_lens` (init): 1d-1/i64/random | `time_axis=-1` | `NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer` | 288/288 |
| `Selu` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | — | `NotImplementedError: this Node Selu-Selu_0 has no value_infer` | 772/772 |
| `Shrink` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Shrink-Shrink_0 has no value_infer` | 1024/1024 |
| `Sinh` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Sinh-Sinh_0 has no value_infer` | 192/192 |
| `Size` | 11–18 | NotImplementedError | `data`: BCHW/bool/random | — | `NotImplementedError: this Node Size-Size_0 has no value_infer` | 1024/1024 |
| `Softsign` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Softsign-Softsign_0 has no value_infer` | 204/204 |
| `SpaceToDepth` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | `blocksize=1` | `NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer` | 112/112 |
| `Tan` | 11–18 | NotImplementedError | `input`: BCHW/f16/random | — | `NotImplementedError: this Node Tan-Tan_0 has no value_infer` | 192/192 |
| `ThresholdedRelu` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | — | `NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer` | 751/751 |
| `Unique` | 11–18 | NotImplementedError | `X`: BCHW/f16/random | `sorted=1` | `NotImplementedError: this Node Unique-Unique_0 has no value_infer` | 360/360 |
| `Split` | 11–18 | TypeError | `input`: BCHW/bool/random | — | `TypeError: list indices must be integers or slices, not NoneType` | 79/272 |
| `TopK` | 11–18 | TypeError | `X`: BCHW/f16/random<br>`K` (init): 1d-1/i64/random | — | `TypeError: '<' not supported between instances of 'NoneType' and 'int'` | 184/544 |
| `Compress` | 11–18 | ValueError | `input`: BCHW/bool/random<br>`condition`: BCHW/bool/all_true | — | `ValueError: condition must be a 1-d array` | 1016/1016 |
| `NonZero` | 11–18 | ValueError | `X`: scalar/bool/random | — | `ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the` | 112/544 |
| `OptionalHasElement` | 18 | ValueError | `input` (init): BCHW/ui32/random | — | `ValueError: cannot reshape array of size 4500 into shape (1,10,30,30)` | 9/128 |
