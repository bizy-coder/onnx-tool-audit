# Consolidated onnx_tool audit bug report

Generated from `all_ops_opset11` through `all_ops_opset18` sweep outputs.

## Run summary

- Opset profile rows: 1347
- Generated cases: 126,252
- ORT-valid comparison cases: 59,496
- Confirmed onnx_tool finding rows: 25,992
- Distinct normalized bug groups: 75
- ORT rejects, checker-valid: 61,750
- Harness-invalid/checker-failed rejects: 5,006

Interpretation: only ORT-valid cases are used as the oracle for onnx_tool comparisons. Checker-valid ORT rejects are tracked as ORT limitations. Checker-failed rejects are harness coverage gaps, not onnx_tool bugs.

## Confirmed onnx_tool bugs

| rank | surfaces | ops/opsets | class | issue | representative |
|---:|---:|---:|---|---|---|
| 1 | 4,165 | Abs@11-18, Add@11-18, And@11-18, Atan@11-18, Cast@11-18, Ceil@11-18, Clip@11-18, Constant@11-18, Conv@11-18, ConvInteger@11-18, Cos@11-18, DequantizeLinear@11-18, Dropout@11-18, Elu@11-18, Equal@11-18, Erf@11-18, Exp@11-18, Floor@11-18, Greater@11-18, GreaterOrEqual@12-18, HardSigmoid@11-18, HardSwish@14-18, Identity@11-18, LayerNormalization@17-18, LeakyRelu@11-18, Less@11-18, LessOrEqual@12-18, Log@11-18, MatMulInteger@11-18, Max@11-18, Min@11-18, Mul@11-18, Neg@11-18, Not@11-18, Or@11-18, PRelu@11-18, Pow@11-18, QuantizeLinear@11-18, RandomNormalLike@11-18, RandomUniformLike@11-18, Reciprocal@11-18, ReduceL2@11-18, ReduceMax@11-17, ReduceMean@11-17, ReduceMin@11-17, ReduceProd@11-17, ReduceSum@11-12, Relu@11-18, Sigmoid@11-18, Sign@11-18, Sin@11-18, Softplus@11-18, Sqrt@11-18, Squeeze@11-12, Sub@11-18, Sum@11-18, Tanh@11-18, Transpose@11-18, Xor@11-18 | `scalar-volume` | Scalar tensors counted as 0 bytes | `X(input)=scalar/int8/random  outputs=1`<br>scalar dropped from accounting (true=1B) |
| 2 | 1,024 | IsInf@11-18 | `onnx-tool-fails-valid-model` | IsInf: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float32/random  outputs=1`<br>NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| 3 | 1,024 | Shrink@11-18 | `onnx-tool-fails-valid-model` | Shrink: onnx_tool throws on ORT-valid model | `input(input)=BCHW/uint64/sparse  outputs=1`<br>NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| 4 | 1,024 | Size@11-18 | `onnx-tool-fails-valid-model` | Size: onnx_tool throws on ORT-valid model | `data(input)=BCHW/bool/random  outputs=1`<br>NotImplementedError: this Node Size-Size_0 has no value_infer |
| 5 | 1,016 | Compress@11-18 | `onnx-tool-fails-valid-model` | Compress: onnx_tool throws on ORT-valid model | `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_true  outputs=1`<br>ValueError: condition must be a 1-d array |
| 6 | 808 | LpPool@11-18 | `onnx-tool-fails-valid-model` | LpPool: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random {'kernel_shape': [1, 1]} outputs=1`<br>NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| 7 | 772 | Selu@11-18 | `onnx-tool-fails-valid-model` | Selu: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| 8 | 751 | ThresholdedRelu@11-18 | `onnx-tool-fails-valid-model` | ThresholdedRelu: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| 9 | 744 | BitShift@11-18 | `onnx-tool-fails-valid-model` | BitShift: onnx_tool throws on ORT-valid model | `X(input)=BCHW/uint8/random Y(input)=BCHW/uint8/random {'direction': b'RIGHT'} outputs=1`<br>NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| 10 | 680 | RandomNormal@11-18 | `onnx-tool-fails-valid-model` | RandomNormal: onnx_tool throws on ORT-valid model | ` {'shape': [1]} outputs=1`<br>NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| 11 | 680 | RandomUniform@11-18 | `onnx-tool-fails-valid-model` | RandomUniform: onnx_tool throws on ORT-valid model | ` {'shape': [1]} outputs=1`<br>NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| 12 | 677 | ReduceLogSumExp@11-18 | `onnx-tool-fails-valid-model` | ReduceLogSumExp: onnx_tool throws on ORT-valid model | `data(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| 13 | 655 | ReduceL1@11-18 | `onnx-tool-fails-valid-model` | ReduceL1: onnx_tool throws on ORT-valid model | `data(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| 14 | 655 | ReduceLogSum@11-18 | `onnx-tool-fails-valid-model` | ReduceLogSum: onnx_tool throws on ORT-valid model | `data(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| 15 | 655 | ReduceSumSquare@11-18 | `onnx-tool-fails-valid-model` | ReduceSumSquare: onnx_tool throws on ORT-valid model | `data(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| 16 | 602 | Constant@12-18 | `onnx-tool-fails-valid-model` | Constant: onnx_tool throws on ORT-valid model | ` {'value_int': 0} outputs=1`<br>AttributeError: 'ConstantNode' object has no attribute 'value' |
| 17 | 576 | GlobalLpPool@11-18 | `onnx-tool-fails-valid-model` | GlobalLpPool: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| 18 | 512 | CastLike@15-18 | `onnx-tool-fails-valid-model` | CastLike: onnx_tool throws on ORT-valid model | `input(input)=BCHW/bool/random target_type(input)=BCHW/bool/random  outputs=1`<br>NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| 19 | 504 | ArgMin@11-18 | `onnx-tool-fails-valid-model` | ArgMin: onnx_tool throws on ORT-valid model | `data(input)=BCHW/int64/sparse  outputs=1`<br>NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| 20 | 504 | MeanVarianceNormalization@11-18 | `onnx-tool-fails-valid-model` | MeanVarianceNormalization: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| 21 | 417 | MaxPool@11-18 | `wrong-shape` | MaxPool: wrong shape | `X(input)=BCHW/float32/random {'kernel_shape': [2, 2]} outputs=11`<br>truth=(1, 10, 29, 29) claim=() |
| 22 | 360 | Unique@11-18 | `onnx-tool-fails-valid-model` | Unique: onnx_tool throws on ORT-valid model | `X(input)=B-C-1-1/int8/sparse  outputs=1000`<br>NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| 23 | 336 | Celu@12-18 | `onnx-tool-fails-valid-model` | Celu: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float32/random  outputs=1`<br>NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| 24 | 332 | Shape@15-18 | `wrong-shape` | Shape: wrong shape | `data(input)=BCHW/bool/sparse {'end': 1} outputs=1`<br>truth=(1,) claim=(4,) |
| 25 | 288 | IsNaN@11-18 | `onnx-tool-fails-valid-model` | IsNaN: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| 26 | 288 | ReverseSequence@11-18 | `onnx-tool-fails-valid-model` | ReverseSequence: onnx_tool throws on ORT-valid model | `input(input)=BCHW/uint32/sparse sequence_lens(init)=1d-10/int64/sparse  outputs=1`<br>NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| 27 | 288 | Round@11-18 | `wrong-dtype` | Round: wrong dtype | `X(input)=BCHW/float16/random  outputs=1`<br>truth=float16 claim=bool |
| 28 | 216 | Flatten@11-18 | `wrong-shape` | Flatten: wrong shape | `input(input)=BCHW/int8/random {'axis': -1} outputs=1`<br>truth=(300, 30) claim=(1, 9000) |
| 29 | 204 | Softsign@11-18 | `onnx-tool-fails-valid-model` | Softsign: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| 30 | 192 | Acosh@11-18 | `onnx-tool-fails-valid-model` | Acosh: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| 31 | 192 | Acos@11-18 | `onnx-tool-fails-valid-model` | Acos: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| 32 | 192 | Asin@11-18 | `onnx-tool-fails-valid-model` | Asin: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| 33 | 192 | Asinh@11-18 | `onnx-tool-fails-valid-model` | Asinh: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| 34 | 192 | Atanh@11-18 | `onnx-tool-fails-valid-model` | Atanh: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| 35 | 192 | Cosh@11-18 | `onnx-tool-fails-valid-model` | Cosh: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| 36 | 192 | Mean@11-18 | `onnx-tool-fails-valid-model` | Mean: onnx_tool throws on ORT-valid model | `data_0(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| 37 | 192 | Sinh@11-18 | `onnx-tool-fails-valid-model` | Sinh: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| 38 | 192 | Tan@11-18 | `onnx-tool-fails-valid-model` | Tan: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| 39 | 186 | BatchNormalization@11-13 | `wrong-shape` | BatchNormalization: wrong shape | `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random  outputs=11111`<br>truth=(10,) claim=(1, 10, 30, 30) |
| 40 | 186 | BatchNormalization@11-13 | `wrong-shape` | BatchNormalization: wrong shape | `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random  outputs=11111`<br>truth=(10,) claim=(1, 10, 30, 30) |
| 41 | 186 | BatchNormalization@11-13 | `wrong-shape` | BatchNormalization: wrong shape | `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random  outputs=11111`<br>truth=(10,) claim=(1, 10, 30, 30) |
| 42 | 186 | BatchNormalization@11-13 | `wrong-shape` | BatchNormalization: wrong shape | `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random  outputs=11111`<br>truth=(10,) claim=(1, 10, 30, 30) |
| 43 | 184 | TopK@11-18 | `onnx-tool-fails-valid-model` | TopK: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random K(init)=1d-1/int64/random  outputs=11`<br>TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| 44 | 183 | ReduceL2@11-18 | `wrong-dtype` | ReduceL2: wrong dtype | `data(input)=scalar/int32/random  outputs=1`<br>truth=int32 claim=float64 |
| 45 | 144 | GlobalMaxPool@11-18 | `onnx-tool-fails-valid-model` | GlobalMaxPool: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| 46 | 141 | ReduceMean@11-18 | `wrong-shape` | ReduceMean: wrong shape | `data(input)=BCHW/float16/random  outputs=1`<br>truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| 47 | 141 | ReduceProd@11-18 | `wrong-shape` | ReduceProd: wrong shape | `data(input)=BCHW/float16/random  outputs=1`<br>truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| 48 | 140 | GatherND@12-18 | `wrong-shape` | GatherND: wrong shape | `data(input)=BCHW/bool/sparse indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1`<br>truth=(30, 30) claim=(10, 30, 30) |
| 49 | 127 | ReduceMax@11-18 | `wrong-shape` | ReduceMax: wrong shape | `data(input)=BCHW/int8/random  outputs=1`<br>truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| 50 | 127 | ReduceMin@11-18 | `wrong-shape` | ReduceMin: wrong shape | `data(input)=BCHW/int8/random  outputs=1`<br>truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| 51 | 119 | OptionalHasElement@18 | `onnx-tool-fails-valid-model` | OptionalHasElement: onnx_tool throws on ORT-valid model | `  outputs=1`<br>NotImplementedError: this Node OptionalHasElement-OptionalHasElement_0 has no value_infer |
| 52 | 112 | NonZero@11-18 | `onnx-tool-fails-valid-model` | NonZero: onnx_tool throws on ORT-valid model | `X(input)=scalar/bool/random  outputs=1`<br>ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `ar |
| 53 | 112 | SpaceToDepth@11-18 | `onnx-tool-fails-valid-model` | SpaceToDepth: onnx_tool throws on ORT-valid model | `input(input)=BCHW/float16/random {'blocksize': 1} outputs=1`<br>NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| 54 | 108 | LayerNormalization@17-18 | `wrong-shape` | LayerNormalization: wrong shape | `X(input)=BCHW/float64/random Scale(input)=BCHW/float64/random {'axis': -1, 'epsilon': 0.5} outputs=110`<br>truth=(1, 10, 30, 1) claim=() |
| 55 | 105 | Einsum@12-18 | `onnx-tool-fails-valid-model` | Einsum: onnx_tool throws on ORT-valid model | `Inputs(input)=scalar/int32/random {'equation': b''} outputs=1`<br>IndexError: list index out of range |
| 56 | 96 | Det@11-18 | `onnx-tool-fails-valid-model` | Det: onnx_tool throws on ORT-valid model | `X(input)=BCHW/float16/random  outputs=1`<br>NotImplementedError: this Node Det-Det_0 has no value_infer |
| 57 | 96 | DynamicQuantizeLinear@11-18 | `onnx-tool-fails-valid-model` | DynamicQuantizeLinear: onnx_tool throws on ORT-valid model | `x(input)=BCHW/float32/random  outputs=111`<br>NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| 58 | 96 | BitwiseNot@18 | `onnx-tool-fails-valid-model` | BitwiseNot: onnx_tool throws on ORT-valid model | `X(input)=BCHW/int8/random  outputs=1`<br>NotImplementedError: this Node BitwiseNot-BitwiseNot_0 has no value_infer |
| 59 | 79 | Split@11-18 | `onnx-tool-fails-valid-model` | Split: onnx_tool throws on ORT-valid model | `input(input)=BCHW/bool/random  outputs=1`<br>TypeError: list indices must be integers or slices, not NoneType |
| 60 | 76 | ReduceSum@11-18 | `wrong-shape` | ReduceSum: wrong shape | `data(input)=BCHW/float16/random  outputs=1`<br>truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |

_Additional confirmed groups omitted from table: 15. See per-opset `*_bugs.md` and `*_findings.jsonl` for the raw rows._

## Highest-confidence bug narratives

### Scalar tensors counted as 0 bytes

- Surfaces: 4,165
- Affected: Abs@11-18, Add@11-18, And@11-18, Atan@11-18, Cast@11-18, Ceil@11-18, Clip@11-18, Constant@11-18, Conv@11-18, ConvInteger@11-18, Cos@11-18, DequantizeLinear@11-18, Dropout@11-18, Elu@11-18, Equal@11-18, Erf@11-18, Exp@11-18, Floor@11-18, Greater@11-18, GreaterOrEqual@12-18, HardSigmoid@11-18, HardSwish@14-18, Identity@11-18, LayerNormalization@17-18, LeakyRelu@11-18, Less@11-18, LessOrEqual@12-18, Log@11-18, MatMulInteger@11-18, Max@11-18, Min@11-18, Mul@11-18, Neg@11-18, Not@11-18, Or@11-18, PRelu@11-18, Pow@11-18, QuantizeLinear@11-18, RandomNormalLike@11-18, RandomUniformLike@11-18, Reciprocal@11-18, ReduceL2@11-18, ReduceMax@11-17, ReduceMean@11-17, ReduceMin@11-17, ReduceProd@11-17, ReduceSum@11-12, Relu@11-18, Sigmoid@11-18, Sign@11-18, Sin@11-18, Softplus@11-18, Sqrt@11-18, Squeeze@11-12, Sub@11-18, Sum@11-18, Tanh@11-18, Transpose@11-18, Xor@11-18
- Representative case: `X(input)=scalar/int8/random  outputs=1`
- Evidence: `scalar-volume`; scalar dropped from accounting (true=1B)

### BatchNormalization: wrong shape

- Surfaces: 186
- Affected: BatchNormalization@11-13
- Representative case: `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random  outputs=11111`
- Evidence: `wrong-shape`; truth=(10,) claim=(1, 10, 30, 30)

### MaxPool: wrong shape

- Surfaces: 417
- Affected: MaxPool@11-18
- Representative case: `X(input)=BCHW/float32/random {'kernel_shape': [2, 2]} outputs=11`
- Evidence: `wrong-shape`; truth=(1, 10, 29, 29) claim=()

### Compress: onnx_tool throws on ORT-valid model

- Surfaces: 1,016
- Affected: Compress@11-18
- Representative case: `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_true  outputs=1`
- Evidence: `onnx-tool-fails-valid-model`; ValueError: condition must be a 1-d array

### Size: onnx_tool throws on ORT-valid model

- Surfaces: 1,024
- Affected: Size@11-18
- Representative case: `data(input)=BCHW/bool/random  outputs=1`
- Evidence: `onnx-tool-fails-valid-model`; NotImplementedError: this Node Size-Size_0 has no value_infer

### IsInf: onnx_tool throws on ORT-valid model

- Surfaces: 1,024
- Affected: IsInf@11-18
- Representative case: `X(input)=BCHW/float32/random  outputs=1`
- Evidence: `onnx-tool-fails-valid-model`; NotImplementedError: this Node IsInf-IsInf_0 has no value_infer

### CastLike: onnx_tool throws on ORT-valid model

- Surfaces: 512
- Affected: CastLike@15-18
- Representative case: `input(input)=BCHW/bool/random target_type(input)=BCHW/bool/random  outputs=1`
- Evidence: `onnx-tool-fails-valid-model`; NotImplementedError: this Node CastLike-CastLike_0 has no value_infer

### RandomNormal: onnx_tool throws on ORT-valid model

- Surfaces: 680
- Affected: RandomNormal@11-18
- Representative case: ` {'shape': [1]} outputs=1`
- Evidence: `onnx-tool-fails-valid-model`; NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer

## Harness coverage gaps

These are generated cases rejected by ONNX checker even after the relaxed graph-output-shape check. They should be fixed or intentionally skipped before claiming full coverage for these ops.

| count | op | opsets | dominant checker error | representative case |
|---:|---|---|---|---|
| 1,024 | `Upsample` | Upsample@11-18 | ValidationError: Op registered for Upsample is deprecated in domain_version of 11  ==> Context: Bad node spec for node. Name:  OpType: Upsample; after infer_shapes: ValidationError | `X(input)=BCHW/bool/random scales(init)=BCHW/float32/random  outputs=1` |
| 1,024 | `Scatter` | Scatter@11-18 | ValidationError: Op registered for Scatter is deprecated in domain_version of 11  ==> Context: Bad node spec for node. Name:  OpType: Scatter; after infer_shapes: ValidationError:  | `data(input)=BCHW/bool/random indices(input)=BCHW/int32/random updates(input)=BCHW/bool/random  outputs=1` |
| 1,024 | `Scan` | Scan@11-18 | ValidationError: Required attribute 'body' is missing.  ==> Context: Bad node spec for node. Name:  OpType: Scan; after infer_shapes: ValidationError: Required attribute 'body' is  | `initial_state_and_scan_inputs(input)=BCHW/bool/random {'num_scan_inputs': 0} outputs=1` |
| 1,024 | `Loop` | Loop@11-18 | ValidationError: Required attribute 'body' is missing.  ==> Context: Bad node spec for node. Name:  OpType: Loop; after infer_shapes: ValidationError: Required attribute 'body' is  | `v_initial(input)=BCHW/bool/random  outputs=1` |
| 256 | `SequenceMap` | SequenceMap@17-18 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: ValidationError: Field 'shape' of 'type' is required but missing.; after relaxing graph outpu | `additional_inputs(input)=BCHW/bool/random  outputs=1` |
| 192 | `StringNormalizer` | StringNormalizer@11-18 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: ValidationError: Field 'shape' of 'type' is required but missing.; after relaxing graph outpu | `  outputs=1` |
| 192 | `SequenceAt` | SequenceAt@11-18 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: ValidationError: Field 'shape' of 'type' is required but missing.; after relaxing graph outpu | `position(input)=BCHW/int32/random  outputs=1` |
| 96 | `If` | If@11-18 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: ValidationError: Field 'shape' of 'type' is required but missing.; after relaxing graph outpu | `cond(input)=BCHW/bool/all_true  outputs=1` |
| 96 | `ConcatFromSequence` | ConcatFromSequence@11-18 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: InferenceError: [ShapeInferenceError] (op_type:ConcatFromSequence): Input 0 is out of bounds. | ` {'axis': 0} outputs=1` |
| 56 | `SequenceInsert` | SequenceInsert@11-18 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: InferenceError: [ShapeInferenceError] (op_type:SequenceInsert): Input 1 is out of bounds.; af | `tensor(input)=BCHW/bool/random  outputs=1` |
| 8 | `SequenceLength` | SequenceLength@11-18 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: ValidationError: Node with schema(::SequenceLength:11) has input size 0 not in range [min=1,  | `  outputs=1` |
| 8 | `SequenceErase` | SequenceErase@11-18 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: InferenceError: [ShapeInferenceError] (op_type:SequenceErase): Input 0 is out of bounds.; aft | `  outputs=1` |
| 3 | `OptionalHasElement` | OptionalHasElement@15-17 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: ValidationError: Field 'shape' of 'type' is required but missing.; after relaxing graph outpu | `  outputs=1` |
| 3 | `OptionalGetElement` | OptionalGetElement@15-17 | ValidationError: Field 'shape' of 'type' is required but missing.; after infer_shapes: ValidationError: Field 'shape' of 'type' is required but missing.; after relaxing graph outpu | `  outputs=1` |

## ORT limitations observed

These are checker-valid ONNX models that ORT rejected, so they do not provide an onnx_tool comparison baseline. They are kept out of the confirmed bug catalog.

| count | op | opsets | ORT families | representative case |
|---:|---|---|---|---|
| 1,024 | `Tile` | Tile@11-18 | InvalidArgument:1024 | `input(input)=BCHW/bool/random repeats(input)=BCHW/int64/random  outputs=1` |
| 1,024 | `TfIdfVectorizer` | TfIdfVectorizer@11-18 | Fail:1024 | `X(input)=BCHW/int32/random {'mode': b'', 'max_gram_length': 0, 'min_gram_length': 0, 'ngram_indexes': [1], 'max_skip_count': 0, 'ngram_counts': [1]} outputs=1` |
| 1,024 | `SequenceConstruct` | SequenceConstruct@11-18 | Fail:1024 | `inputs(input)=BCHW/bool/random  outputs=1` |
| 1,024 | `RoiAlign` | RoiAlign@11-18 | Fail:1024 | `X(input)=BCHW/float16/random rois(input)=BCHW/float16/random batch_indices(input)=BCHW/int64/random  outputs=1` |
| 1,024 | `Resize` | Resize@11-18 | Fail:1023, NotImplemented:1 | `X(input)=BCHW/bool/random roi(input)=BCHW/float16/random scales(init)=BCHW/float32/random  outputs=1` |
| 1,024 | `Reshape` | Reshape@11-18 | RuntimeException:624, Fail:400 | `data(input)=BCHW/bool/random shape(init)=1d-1/int64/random  outputs=1` |
| 1,024 | `RNN` | RNN@11-18 | Fail:1024 | `X(input)=BCHW/float16/random W(input)=BCHW/float16/random R(input)=BCHW/float16/random  outputs=10` |
| 1,024 | `QLinearMatMul` | QLinearMatMul@11-18 | Fail:568, NotImplemented:272, RuntimeException:184 | `a(input)=BCHW/int8/random a_scale(init)=BCHW/float32/random a_zero_point(input)=BCHW/int8/random b(input)=BCHW/int8/random b_scale(init)=BCHW/float32/random b_zero_point(input)=BCH` |
| 1,024 | `QLinearConv` | QLinearConv@11-18 | Fail:568, NotImplemented:280, RuntimeException:176 | `x(input)=BCHW/int8/random x_scale(init)=BCHW/float32/random x_zero_point(input)=BCHW/int8/random w(input)=BCHW/int8/random w_scale(init)=BCHW/float32/random w_zero_point(input)=BCH` |
| 1,024 | `OneHot` | OneHot@11-18 | Fail:1024 | `indices(input)=BCHW/float16/random depth(input)=BCHW/float16/random values(input)=BCHW/bool/random  outputs=1` |
| 1,024 | `NonMaxSuppression` | NonMaxSuppression@11-18 | Fail:1024 | `boxes(init)=BCHW/float32/random scores(init)=BCHW/float32/random  outputs=1` |
| 1,024 | `Multinomial` | Multinomial@11-18 | Fail:1024 | `input(input)=BCHW/float16/random  outputs=1` |
| 1,024 | `MaxRoiPool` | MaxRoiPool@11-18 | Fail:1024 | `X(input)=BCHW/float16/random rois(input)=BCHW/float16/random {'pooled_shape': [1]} outputs=1` |
| 1,024 | `LSTM` | LSTM@11-18 | Fail:1024 | `X(input)=BCHW/float16/random W(input)=BCHW/float16/random R(input)=BCHW/float16/random  outputs=100` |
| 1,024 | `Gemm` | Gemm@11-18 | Fail:1024 | `A(input)=BCHW/float16/random B(input)=BCHW/float16/random  outputs=1` |
| 1,024 | `GRU` | GRU@11-18 | Fail:1024 | `X(input)=BCHW/float16/random W(input)=BCHW/float16/random R(input)=BCHW/float16/random  outputs=10` |
| 1,024 | `EyeLike` | EyeLike@11-18 | Fail:1024 | `input(input)=BCHW/bool/random  outputs=1` |
| 1,000 | `Pad` | Pad@11-18 | Fail:1000 | `data(input)=BCHW/float16/random pads(init)=1d-1/int64/random  outputs=1` |
| 1,000 | `ConvInteger` | ConvInteger@11-18 | Fail:624, RuntimeException:376 | `x(input)=BCHW/int8/random w(input)=BCHW/int8/random x_zero_point(init)=BCHW/int8/random w_zero_point(init)=BCHW/int8/random {'group': 1} outputs=1` |
| 984 | `MatMulInteger` | MatMulInteger@11-18 | Fail:600, RuntimeException:384 | `A(input)=BCHW/int8/random B(input)=BCHW/int8/random a_zero_point(init)=BCHW/int8/random b_zero_point(init)=BCHW/int8/random  outputs=1` |
| 976 | `QuantizeLinear` | QuantizeLinear@11-18 | RuntimeException:616, NotImplemented:272, Fail:88 | `x(input)=BCHW/float32/random y_scale(init)=BCHW/float32/random  outputs=1` |
| 968 | `SequenceInsert` | SequenceInsert@11-18 | InvalidGraph:968 | `tensor(input)=BCHW/bool/random position(init)=BCHW/int32/random  outputs=1` |
| 944 | `RandomUniformLike` | RandomUniformLike@11-18 | Fail:656, NotImplemented:288 | `input(input)=BCHW/bool/random  outputs=1` |
| 944 | `RandomNormalLike` | RandomNormalLike@11-18 | Fail:656, NotImplemented:288 | `input(input)=BCHW/bool/random  outputs=1` |
| 944 | `DepthToSpace` | DepthToSpace@11-18 | Fail:664, NotImplemented:280 | `input(input)=BCHW/bool/random {'blocksize': 0} outputs=1` |
| 936 | `Conv` | Conv@11-18 | Fail:656, NotImplemented:280 | `X(input)=BCHW/float16/random W(input)=BCHW/float16/random B(init)=BCHW/float16/random {'kernel_shape': [1, 1]} outputs=1` |
| 928 | `DequantizeLinear` | DequantizeLinear@11-18 | RuntimeException:928 | `x(input)=BCHW/int32/random x_scale(init)=BCHW/float32/random  outputs=1` |
| 912 | `SpaceToDepth` | SpaceToDepth@11-18 | Fail:592, NotImplemented:320 | `input(input)=BCHW/bool/random {'blocksize': 0} outputs=1` |
| 896 | `SoftmaxCrossEntropyLoss` | SoftmaxCrossEntropyLoss@12-18 | Fail:896 | `scores(input)=BCHW/float16/random labels(input)=BCHW/int32/random  outputs=10` |
| 896 | `NegativeLogLikelihoodLoss` | NegativeLogLikelihoodLoss@12-18 | Fail:896 | `input(input)=BCHW/float16/random target(input)=BCHW/int32/random  outputs=1` |
| 886 | `CumSum` | CumSum@11-18 | RuntimeException:662, NotImplemented:216, InvalidArgument:8 | `x(input)=BCHW/float32/random axis(input)=BCHW/int32/random  outputs=1` |
| 872 | `LRN` | LRN@11-18 | Fail:488, NotImplemented:336, RuntimeException:48 | `X(input)=BCHW/float16/random {'size': 0} outputs=1` |
| 871 | `ScatterElements` | ScatterElements@11-18 | InvalidArgument:848, RuntimeException:23 | `data(input)=BCHW/bool/random indices(input)=BCHW/int32/random updates(input)=BCHW/bool/random  outputs=1` |
| 848 | `Expand` | Expand@11-18 | Fail:848 | `input(input)=BCHW/bool/random shape(init)=1d-1/int64/random  outputs=1` |
| 826 | `Dropout` | Dropout@12-18 | Fail:812, RuntimeException:14 | `data(input)=BCHW/float16/random ratio(init)=BCHW/float16/random training_mode(init)=BCHW/bool/all_true {'seed': 0} outputs=11` |
| 791 | `Einsum` | Einsum@12-18 | NotImplemented:476, InvalidArgument:315 | `Inputs(input)=BCHW/float16/random {'equation': b''} outputs=1` |
| 776 | `Slice` | Slice@11-18 | Fail:768, InvalidArgument:8 | `data(input)=BCHW/bool/random starts(input)=BCHW/int32/random ends(input)=BCHW/int32/random  outputs=1` |
| 764 | `GatherND` | GatherND@11-18 | Fail:488, InvalidArgument:276 | `data(input)=BCHW/bool/random indices(init)=1d-1/int64/random  outputs=1` |
| 752 | `Split` | Split@11-18 | Fail:752 | `input(input)=BCHW/int32/random {'split': [1, 1]} outputs=1` |
| 744 | `GatherElements` | GatherElements@11-18 | RuntimeException:528, InvalidArgument:216 | `data(input)=BCHW/bool/random indices(input)=BCHW/int32/random  outputs=1` |
| 736 | `ReverseSequence` | ReverseSequence@11-18 | Fail:376, InvalidArgument:360 | `input(input)=BCHW/bool/random sequence_lens(init)=1d-1/int64/random  outputs=1` |
| 682 | `ScatterND` | ScatterND@11-18 | InvalidArgument:682 | `data(input)=BCHW/bool/random indices(init)=1d-1/int64/random updates(input)=BCHW/bool/random  outputs=1` |
| 674 | `Squeeze` | Squeeze@11-18 | Fail:644, RuntimeException:30 | `data(input)=BCHW/float32/random {'axes': [1]} outputs=1` |
| 664 | `Unique` | Unique@11-18 | NotImplemented:544, Fail:120 | `X(input)=BCHW/bool/random  outputs=1000` |
| 640 | `BatchNormalization` | BatchNormalization@14-18 | Fail:640 | `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random input_mean(input)=BCHW/float16/random input_var(input)=BCHW/float16/random  outputs=100` |
| 584 | `Gather` | Gather@11-18 | InvalidArgument:576, Fail:8 | `data(input)=BCHW/bool/random indices(input)=BCHW/int32/random  outputs=1` |
| 550 | `Unsqueeze` | Unsqueeze@11-18 | Fail:550 | `data(input)=scalar/bool/random {'axes': [1]} outputs=1` |
| 520 | `MeanVarianceNormalization` | MeanVarianceNormalization@11-18 | Fail:286, NotImplemented:234 | `X(input)=BCHW/float64/random {'axes': [1]} outputs=1` |
| 520 | `ArgMin` | ArgMin@11-18 | NotImplemented:288, Fail:232 | `data(input)=BCHW/int16/random {'axis': -1} outputs=1` |
| 520 | `ArgMax` | ArgMax@11-18 | NotImplemented:288, Fail:232 | `data(input)=BCHW/int16/random {'axis': -1} outputs=1` |

