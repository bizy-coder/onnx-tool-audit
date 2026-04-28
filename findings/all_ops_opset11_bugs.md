# onnx_tool 1.0.1 — bug catalog

Each test case runs through two oracles:

- **`onnxruntime`** executes the model. Validity is decided by execution: if ORT runs the model cleanly, it's a model that could ship. If ORT rejects it, we ignore the case — an unrunnable model can't be submitted to Kaggle and can't influence scoring.
- **`onnx_tool`** statically profiles the model.

Classification:

| ORT | onnx_tool | classification |
|-----|-----------|----------------|
| reject | (any) | ignored (generator noise; not recorded here) |
| accept | reject | **onnx-tool-fails-valid-model** |
| accept | accept-but-disagrees | **onnx_tool wrong shape/dtype/bytes** |

**Summary**: 46 distinct onnx_tool bugs (1036 surface findings collapsed).

## Bugs in onnx_tool

### Bug 1: `scalar-volume`

_onnx_tool reports 0 bytes for tensors with shape `()` because `volume([])` returns 0 instead of 1._

- **Affected ops** (55): `Abs@11`, `Add@11`, `And@11`, `Atan@11`, `Ceil@11`, `Clip@11`, `Constant@11`, `Conv@11`, `Cos@11`, `DequantizeLinear@11`, `Div@11`, `Dropout@11`, `Elu@11`, `Equal@11`, `Erf@11`, `Exp@11`, `Floor@11`, `Greater@11`, `HardSigmoid@11`, `Identity@11`, `LeakyRelu@11`, `Less@11`, `Log@11`, `MatMulInteger@11`, `Max@11`, `Min@11`, `Mod@11`, `Mul@11`, `Neg@11`, `Not@11`, `Or@11`, `PRelu@11`, `Pow@11`, `QuantizeLinear@11`, `RandomNormalLike@11`, `RandomUniformLike@11`, `Reciprocal@11`, `ReduceL2@11`, `ReduceMax@11`, `ReduceMean@11`, `ReduceMin@11`, `ReduceProd@11`, `ReduceSum@11`, `Relu@11`, `Sigmoid@11`, `Sign@11`, `Sin@11`, `Softplus@11`, `Sqrt@11`, `Squeeze@11`, `Sub@11`, `Sum@11`, `Tanh@11`, `Transpose@11`, `Xor@11`
- **Surface findings collapsed**: 192
- **Minimal repro**:

  Op: `Constant`  
  Attrs: `{'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `()` | `float32` | `4` |
  | onnx_tool| `()` | `float32` | `0` |

  _scalar dropped from accounting (true=4B)_

### Bug 2: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `IsInf@11`
- **Surface findings collapsed**: 128
- **Minimal repro**:

  Op: `IsInf`  
  Inputs: `X(input)=scalar/float32/random {'detect_negative': 1, 'detect_positive': 0}`  
  Attrs: `{'detect_negative': 1, 'detect_positive': 0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `1` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node IsInf-IsInf_0 has no value_infer_

### Bug 3: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Size@11`
- **Surface findings collapsed**: 128
- **Minimal repro**:

  Op: `Size`  
  Inputs: `data(input)=scalar/bool/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `8` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Size-Size_0 has no value_infer_

### Bug 4: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ArgMin@11`
- **Surface findings collapsed**: 63
- **Minimal repro**:

  Op: `ArgMin`  
  Inputs: `data(input)=B-C-1-1/float16/random {'axis': 1}`  
  Attrs: `{'axis': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `8` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer_

### Bug 5: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ThresholdedRelu@11`
- **Surface findings collapsed**: 42
- **Minimal repro**:

  Op: `ThresholdedRelu`  
  Inputs: `X(input)=scalar/float16/random {'alpha': 0.0}`  
  Attrs: `{'alpha': 0.0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer_

### Bug 6: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Selu@11`
- **Surface findings collapsed**: 40
- **Minimal repro**:

  Op: `Selu`  
  Inputs: `X(input)=scalar/float16/random {'gamma': 0.5}`  
  Attrs: `{'gamma': 0.5}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Selu-Selu_0 has no value_infer_

### Bug 7: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `GlobalLpPool@11`
- **Surface findings collapsed**: 36
- **Minimal repro**:

  Op: `GlobalLpPool`  
  Inputs: `X(input)=B-C-1-1/float16/random {'p': 0}`  
  Attrs: `{'p': 0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer_

### Bug 8: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `IsNaN@11`
- **Surface findings collapsed**: 36
- **Minimal repro**:

  Op: `IsNaN`  
  Inputs: `X(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `1` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer_

### Bug 9: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `MeanVarianceNormalization@11`
- **Surface findings collapsed**: 36
- **Minimal repro**:

  Op: `MeanVarianceNormalization`  
  Inputs: `X(input)=B-C-1-1/float16/sparse {'axes': [0]}`  
  Attrs: `{'axes': [0]}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer_

### Bug 10: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `LpPool@11`
- **Surface findings collapsed**: 23
- **Minimal repro**:

  Op: `LpPool`  
  Inputs: `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}`  
  Attrs: `{'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node LpPool-LpPool_0 has no value_infer_

### Bug 11: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReduceL1@11`
- **Surface findings collapsed**: 19
- **Minimal repro**:

  Op: `ReduceL1`  
  Inputs: `data(input)=scalar/float16/alternating {'keepdims': 1}`  
  Attrs: `{'keepdims': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer_

### Bug 12: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReduceLogSum@11`
- **Surface findings collapsed**: 19
- **Minimal repro**:

  Op: `ReduceLogSum`  
  Inputs: `data(input)=scalar/float16/alternating {'keepdims': 1}`  
  Attrs: `{'keepdims': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer_

### Bug 13: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReduceLogSumExp@11`
- **Surface findings collapsed**: 19
- **Minimal repro**:

  Op: `ReduceLogSumExp`  
  Inputs: `data(input)=scalar/float16/alternating {'keepdims': 1}`  
  Attrs: `{'keepdims': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer_

### Bug 14: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReduceSumSquare@11`
- **Surface findings collapsed**: 19
- **Minimal repro**:

  Op: `ReduceSumSquare`  
  Inputs: `data(input)=scalar/float16/alternating {'keepdims': 1}`  
  Attrs: `{'keepdims': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer_

### Bug 15: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Compress@11`
- **Surface findings collapsed**: 16
- **Minimal repro**:

  Op: `Compress`  
  Inputs: `input(input)=B-C-1-1/bool/random condition(input)=B-C-1-1/bool/all_true `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `10` |
  | onnx_tool| `None` | `None` | `None` |

  _ValueError: condition must be a 1-d array_

### Bug 16: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `NonZero@11`
- **Surface findings collapsed**: 14
- **Minimal repro**:

  Op: `NonZero`  
  Inputs: `X(input)=scalar/bool/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `8` |
  | onnx_tool| `None` | `None` | `None` |

  _ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`._

### Bug 17: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Acos@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Acos`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Acos-Acos_0 has no value_infer_

### Bug 18: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Acosh@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Acosh`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Acosh-Acosh_0 has no value_infer_

### Bug 19: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Asin@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Asin`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Asin-Asin_0 has no value_infer_

### Bug 20: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Asinh@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Asinh`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Asinh-Asinh_0 has no value_infer_

### Bug 21: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Atanh@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Atanh`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Atanh-Atanh_0 has no value_infer_

### Bug 22: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Cosh@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Cosh`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Cosh-Cosh_0 has no value_infer_

### Bug 23: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `DynamicQuantizeLinear@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `DynamicQuantizeLinear`  
  Inputs: `x(input)=scalar/float32/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `6` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer_

### Bug 24: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Mean@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Mean`  
  Inputs: `data_0(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Mean-Mean_0 has no value_infer_

### Bug 25: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Sinh@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Sinh`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Sinh-Sinh_0 has no value_infer_

### Bug 26: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Softsign@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Softsign`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Softsign-Softsign_0 has no value_infer_

### Bug 27: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Tan@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Tan`  
  Inputs: `input(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Tan-Tan_0 has no value_infer_

### Bug 28: `wrong-dtype`

_onnx_tool's claimed output dtype disagrees with what ORT produces at runtime._

- **Affected ops** (1): `Round@11`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Round`  
  Inputs: `X(input)=scalar/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `()` | `float16` | `2` |
  | onnx_tool| `()` | `bool` | `0` |

  _truth=float16 claim=bool_

### Bug 29: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `GlobalMaxPool@11`
- **Surface findings collapsed**: 9
- **Minimal repro**:

  Op: `GlobalMaxPool`  
  Inputs: `X(input)=B-C-1-1/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer_

### Bug 30: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `Pow@11`
- **Surface findings collapsed**: 7
- **Minimal repro**:

  Op: `Pow`  
  Inputs: `X(input)=B-C-1-1/float16/random Y(input)=B-1-H-1/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10, 30, 1)` | `float16` | `600` |
  | onnx_tool| `(1, 1, 30, 1)` | `float16` | `60` |

  _truth=(1, 10, 30, 1) claim=(1, 1, 30, 1)_

### Bug 31: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Det@11`
- **Surface findings collapsed**: 6
- **Minimal repro**:

  Op: `Det`  
  Inputs: `X(input)=B-C-1-1/float16/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Det-Det_0 has no value_infer_

### Bug 32: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Shrink@11`
- **Surface findings collapsed**: 6
- **Minimal repro**:

  Op: `Shrink`  
  Inputs: `input(input)=scalar/float16/random {'lambd': 0.0, 'bias': 0.5}`  
  Attrs: `{'lambd': 0.0, 'bias': 0.5}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Shrink-Shrink_0 has no value_infer_

### Bug 33: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReverseSequence@11`
- **Surface findings collapsed**: 4
- **Minimal repro**:

  Op: `ReverseSequence`  
  Inputs: `input(input)=BCHW/bool/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': -1}`  
  Attrs: `{'time_axis': 1, 'batch_axis': -1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `9008` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer_

### Bug 34: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `MaxPool@11`
- **Surface findings collapsed**: 4
- **Minimal repro**:

  Op: `MaxPool`  
  Inputs: `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0]}`  
  Attrs: `{'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0]}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10, 1, 1)` | `int64` | `80` |
  | onnx_tool| `()` | `int64` | `0` |

  _truth=(1, 10, 1, 1) claim=()_

### Bug 35: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Constant@11`
- **Surface findings collapsed**: 3
- **Minimal repro**:

  Op: `Constant`  
  Attrs: `{'value': 0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `8` |
  | onnx_tool| `None` | `None` | `None` |

  _AttributeError: 'int' object has no attribute 'shape'_

### Bug 36: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `Flatten@11`
- **Surface findings collapsed**: 3
- **Minimal repro**:

  Op: `Flatten`  
  Inputs: `input(input)=B-C-1-1/bool/random {'axis': -1}`  
  Attrs: `{'axis': -1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(10, 1)` | `bool` | `10` |
  | onnx_tool| `(1, 10)` | `bool` | `10` |

  _truth=(10, 1) claim=(1, 10)_

### Bug 37: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `PRelu@11`
- **Surface findings collapsed**: 3
- **Minimal repro**:

  Op: `PRelu`  
  Inputs: `X(input)=B-C-1-1/float16/random slope(input)=B-1-H-1/float16/alternating `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10, 30, 1)` | `float16` | `600` |
  | onnx_tool| `(1, 1, 30, 1)` | `float16` | `60` |

  _truth=(1, 10, 30, 1) claim=(1, 1, 30, 1)_

### Bug 38: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `Squeeze@11`
- **Surface findings collapsed**: 3
- **Minimal repro**:

  Op: `Squeeze`  
  Inputs: `data(input)=B-C-1-1/bool/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(10,)` | `bool` | `10` |
  | onnx_tool| `(10, 1, 1)` | `bool` | `10` |

  _truth=(10,) claim=(10, 1, 1)_

### Bug 39: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `TopK@11`
- **Surface findings collapsed**: 2
- **Minimal repro**:

  Op: `TopK`  
  Inputs: `X(input)=BCHW/float16/random K(init)=1d-1/int64/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `21008` |
  | onnx_tool| `None` | `None` | `None` |

  _TypeError: '<' not supported between instances of 'NoneType' and 'int'_

### Bug 40: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceMax@11`
- **Surface findings collapsed**: 2
- **Minimal repro**:

  Op: `ReduceMax`  
  Inputs: `data(input)=B-1-H-1/float16/alternating `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `()` | `float16` | `0` |

  _truth=(1, 1, 1, 1) claim=()_

### Bug 41: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceMean@11`
- **Surface findings collapsed**: 2
- **Minimal repro**:

  Op: `ReduceMean`  
  Inputs: `data(input)=B-1-H-1/float16/alternating `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `()` | `float16` | `0` |

  _truth=(1, 1, 1, 1) claim=()_

### Bug 42: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceMin@11`
- **Surface findings collapsed**: 2
- **Minimal repro**:

  Op: `ReduceMin`  
  Inputs: `data(input)=B-1-H-1/float16/alternating `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `()` | `float16` | `0` |

  _truth=(1, 1, 1, 1) claim=()_

### Bug 43: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceProd@11`
- **Surface findings collapsed**: 2
- **Minimal repro**:

  Op: `ReduceProd`  
  Inputs: `data(input)=B-1-H-1/float16/alternating `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `()` | `float16` | `0` |

  _truth=(1, 1, 1, 1) claim=()_

### Bug 44: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceSum@11`
- **Surface findings collapsed**: 2
- **Minimal repro**:

  Op: `ReduceSum`  
  Inputs: `data(input)=B-1-H-1/float16/alternating `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `()` | `float16` | `0` |

  _truth=(1, 1, 1, 1) claim=()_

### Bug 45: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Split@11`
- **Surface findings collapsed**: 1
- **Minimal repro**:

  Op: `Split`  
  Inputs: `input(input)=BCHW/bool/random `  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `9000` |
  | onnx_tool| `None` | `None` | `None` |

  _TypeError: list indices must be integers or slices, not NoneType_

### Bug 46: `wrong-dtype`

_onnx_tool's claimed output dtype disagrees with what ORT produces at runtime._

- **Affected ops** (1): `Constant@11`
- **Surface findings collapsed**: 1
- **Minimal repro**:

  Op: `Constant`  
  Attrs: `{'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'sparse_value': 0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `()` | `int64` | `8` |
  | onnx_tool| `()` | `float32` | `0` |

  _truth=int64 claim=float32_

---

## Bugs in onnxruntime

These models pass the ONNX spec checker but onnxruntime fails to load or execute them. Reported separately because fixing them is in onnxruntime, not onnx_tool.

### Bug 1: `ort-timeout`

_The ORT/truth oracle did not finish within the per-case timeout. Recorded separately because this blocks validation, but it is not evidence of an onnx_tool bug._

- **Affected ops** (1): `SplitToSequence@11`
- **Surface findings collapsed**: 1
- **Minimal repro**:

  Op: `SplitToSequence`  
  Inputs: `input(input)=BCHW/int32/sparse split(init)=scalar/int32/sparse {'axis': 0}`  
  Attrs: `{'axis': 0}`  


  _ORT/truth oracle did not finish within 10s (phase=start)_
