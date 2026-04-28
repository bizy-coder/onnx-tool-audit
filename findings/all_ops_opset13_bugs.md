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

**Summary**: 58 distinct onnx_tool bugs (3192 surface findings collapsed).

## Bugs in onnx_tool

### Bug 1: `scalar-volume`

_onnx_tool reports 0 bytes for tensors with shape `()` because `volume([])` returns 0 instead of 1._

- **Affected ops** (55): `Abs@13`, `Add@13`, `And@13`, `Atan@13`, `Cast@13`, `Ceil@13`, `Clip@13`, `Constant@13`, `Conv@13`, `ConvInteger@13`, `Cos@13`, `DequantizeLinear@13`, `Dropout@13`, `Elu@13`, `Equal@13`, `Erf@13`, `Exp@13`, `Floor@13`, `Greater@13`, `GreaterOrEqual@13`, `HardSigmoid@13`, `Identity@13`, `LeakyRelu@13`, `Less@13`, `LessOrEqual@13`, `Log@13`, `MatMulInteger@13`, `Max@13`, `Min@13`, `Mul@13`, `Neg@13`, `Not@13`, `Or@13`, `PRelu@13`, `Pow@13`, `QuantizeLinear@13`, `RandomNormalLike@13`, `RandomUniformLike@13`, `Reciprocal@13`, `ReduceL2@13`, `ReduceMax@13`, `ReduceMean@13`, `ReduceMin@13`, `ReduceProd@13`, `Relu@13`, `Sigmoid@13`, `Sign@13`, `Sin@13`, `Softplus@13`, `Sqrt@13`, `Sub@13`, `Sum@13`, `Tanh@13`, `Transpose@13`, `Xor@13`
- **Surface findings collapsed**: 519
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

### Bug 2: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `BatchNormalization@13`
- **Surface findings collapsed**: 248
- **Minimal repro**:

  Op: `BatchNormalization`  
  Inputs: `X(input)=B-1-H-1/float16/random scale(input)=1d-1/float16/random B(input)=1d-1/float16/random mean(input)=1d-1/float16/random var(input)=1d-1/float16/random {'momentum': 0.5} outputs=11111`  
  Attrs: `{'momentum': 0.5}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1,)` | `float16` | `2` |
  | onnx_tool| `(1, 1, 30, 1)` | `float16` | `60` |

  _truth=(1,) claim=(1, 1, 30, 1)_

### Bug 3: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `IsInf@13`
- **Surface findings collapsed**: 128
- **Minimal repro**:

  Op: `IsInf`  
  Inputs: `X(input)=scalar/float32/random {'detect_negative': 1, 'detect_positive': 0} outputs=1`  
  Attrs: `{'detect_negative': 1, 'detect_positive': 0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `1` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node IsInf-IsInf_0 has no value_infer_

### Bug 4: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Shrink@13`
- **Surface findings collapsed**: 128
- **Minimal repro**:

  Op: `Shrink`  
  Inputs: `input(input)=scalar/float16/random {'lambd': 1.0, 'bias': 1.0} outputs=1`  
  Attrs: `{'lambd': 1.0, 'bias': 1.0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Shrink-Shrink_0 has no value_infer_

### Bug 5: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Size@13`
- **Surface findings collapsed**: 128
- **Minimal repro**:

  Op: `Size`  
  Inputs: `data(input)=scalar/bool/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `8` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Size-Size_0 has no value_infer_

### Bug 6: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Compress@13`
- **Surface findings collapsed**: 127
- **Minimal repro**:

  Op: `Compress`  
  Inputs: `input(input)=B-C-1-1/bool/random condition(input)=B-C-1-1/bool/all_true  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `10` |
  | onnx_tool| `None` | `None` | `None` |

  _ValueError: condition must be a 1-d array_

### Bug 7: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `LpPool@13`
- **Surface findings collapsed**: 101
- **Minimal repro**:

  Op: `LpPool`  
  Inputs: `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER'} outputs=1`  
  Attrs: `{'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER'}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node LpPool-LpPool_0 has no value_infer_

### Bug 8: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `BitShift@13`
- **Surface findings collapsed**: 93
- **Minimal repro**:

  Op: `BitShift`  
  Inputs: `X(input)=B-C-1-1/uint32/random Y(input)=scalar/uint32/alternating {'direction': b'LEFT'} outputs=1`  
  Attrs: `{'direction': b'LEFT'}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `40` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node BitShift-BitShift_0 has no value_infer_

### Bug 9: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Selu@13`
- **Surface findings collapsed**: 92
- **Minimal repro**:

  Op: `Selu`  
  Inputs: `X(input)=scalar/float16/random {'alpha': 0.0, 'gamma': 0.0} outputs=1`  
  Attrs: `{'alpha': 0.0, 'gamma': 0.0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Selu-Selu_0 has no value_infer_

### Bug 10: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ThresholdedRelu@13`
- **Surface findings collapsed**: 89
- **Minimal repro**:

  Op: `ThresholdedRelu`  
  Inputs: `X(input)=scalar/float16/random {'alpha': 1.0} outputs=1`  
  Attrs: `{'alpha': 1.0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer_

### Bug 11: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Constant@13`
- **Surface findings collapsed**: 86
- **Minimal repro**:

  Op: `Constant`  
  Attrs: `{'value_string': b''}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `8` |
  | onnx_tool| `None` | `None` | `None` |

  _AttributeError: 'ConstantNode' object has no attribute 'value'_

### Bug 12: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `RandomNormal@13`
- **Surface findings collapsed**: 85
- **Minimal repro**:

  Op: `RandomNormal`  
  Attrs: `{'shape': [1]}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `4` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer_

### Bug 13: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `RandomUniform@13`
- **Surface findings collapsed**: 85
- **Minimal repro**:

  Op: `RandomUniform`  
  Attrs: `{'shape': [1]}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `4` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer_

### Bug 14: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReduceL1@13`
- **Surface findings collapsed**: 84
- **Minimal repro**:

  Op: `ReduceL1`  
  Inputs: `data(input)=scalar/int32/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `4` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer_

### Bug 15: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReduceLogSum@13`
- **Surface findings collapsed**: 84
- **Minimal repro**:

  Op: `ReduceLogSum`  
  Inputs: `data(input)=scalar/int32/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `4` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer_

### Bug 16: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReduceLogSumExp@13`
- **Surface findings collapsed**: 84
- **Minimal repro**:

  Op: `ReduceLogSumExp`  
  Inputs: `data(input)=scalar/int32/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `4` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer_

### Bug 17: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReduceSumSquare@13`
- **Surface findings collapsed**: 84
- **Minimal repro**:

  Op: `ReduceSumSquare`  
  Inputs: `data(input)=scalar/int32/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `4` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer_

### Bug 18: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `GlobalLpPool@13`
- **Surface findings collapsed**: 72
- **Minimal repro**:

  Op: `GlobalLpPool`  
  Inputs: `X(input)=B-C-1-1/float16/random {'p': 0} outputs=1`  
  Attrs: `{'p': 0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer_

### Bug 19: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ArgMin@13`
- **Surface findings collapsed**: 63
- **Minimal repro**:

  Op: `ArgMin`  
  Inputs: `data(input)=B-C-1-1/float16/random {'axis': 0, 'keepdims': 1} outputs=1`  
  Attrs: `{'axis': 0, 'keepdims': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `80` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer_

### Bug 20: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `MaxPool@13`
- **Surface findings collapsed**: 54
- **Minimal repro**:

  Op: `MaxPool`  
  Inputs: `X(input)=B-C-1-1/float64/alternating {'kernel_shape': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET'} outputs=11`  
  Attrs: `{'kernel_shape': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET'}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10, 1, 1)` | `int64` | `80` |
  | onnx_tool| `()` | `int64` | `0` |

  _truth=(1, 10, 1, 1) claim=()_

### Bug 21: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Celu@13`
- **Surface findings collapsed**: 48
- **Minimal repro**:

  Op: `Celu`  
  Inputs: `X(input)=scalar/float32/random {'alpha': 0.0} outputs=1`  
  Attrs: `{'alpha': 0.0}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `4` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Celu-Celu_0 has no value_infer_

### Bug 22: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Unique@13`
- **Surface findings collapsed**: 45
- **Minimal repro**:

  Op: `Unique`  
  Inputs: `X(input)=B-C-1-1/float16/random {'axis': -1} outputs=1111`  
  Attrs: `{'axis': -1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `44` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Unique-Unique_0 has no value_infer_

### Bug 23: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `IsNaN@13`
- **Surface findings collapsed**: 36
- **Minimal repro**:

  Op: `IsNaN`  
  Inputs: `X(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `1` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer_

### Bug 24: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `MeanVarianceNormalization@13`
- **Surface findings collapsed**: 36
- **Minimal repro**:

  Op: `MeanVarianceNormalization`  
  Inputs: `X(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1`  
  Attrs: `{'axes': [1]}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `40` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer_

### Bug 25: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `ReverseSequence@13`
- **Surface findings collapsed**: 36
- **Minimal repro**:

  Op: `ReverseSequence`  
  Inputs: `input(input)=BCHW/float64/random sequence_lens(init)=1d-1/int64/random {'time_axis': -1} outputs=1`  
  Attrs: `{'time_axis': -1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `72008` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer_

### Bug 26: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `Flatten@13`
- **Surface findings collapsed**: 27
- **Minimal repro**:

  Op: `Flatten`  
  Inputs: `input(input)=B-C-1-1/bool/random {'axis': -1} outputs=1`  
  Attrs: `{'axis': -1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(10, 1)` | `bool` | `10` |
  | onnx_tool| `(1, 10)` | `bool` | `10` |

  _truth=(10, 1) claim=(1, 10)_

### Bug 27: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Acos@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Acos`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Acos-Acos_0 has no value_infer_

### Bug 28: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Acosh@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Acosh`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Acosh-Acosh_0 has no value_infer_

### Bug 29: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Asin@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Asin`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Asin-Asin_0 has no value_infer_

### Bug 30: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Asinh@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Asinh`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Asinh-Asinh_0 has no value_infer_

### Bug 31: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Atanh@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Atanh`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Atanh-Atanh_0 has no value_infer_

### Bug 32: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Cosh@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Cosh`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Cosh-Cosh_0 has no value_infer_

### Bug 33: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Mean@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Mean`  
  Inputs: `data_0(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Mean-Mean_0 has no value_infer_

### Bug 34: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Sinh@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Sinh`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Sinh-Sinh_0 has no value_infer_

### Bug 35: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Softsign@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Softsign`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Softsign-Softsign_0 has no value_infer_

### Bug 36: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Tan@13`
- **Surface findings collapsed**: 24
- **Minimal repro**:

  Op: `Tan`  
  Inputs: `input(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Tan-Tan_0 has no value_infer_

### Bug 37: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `TopK@13`
- **Surface findings collapsed**: 23
- **Minimal repro**:

  Op: `TopK`  
  Inputs: `X(input)=BCHW/float16/random K(init)=1d-1/int64/random  outputs=11`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `6008` |
  | onnx_tool| `None` | `None` | `None` |

  _TypeError: '<' not supported between instances of 'NoneType' and 'int'_

### Bug 38: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceMean@13`
- **Surface findings collapsed**: 21
- **Minimal repro**:

  Op: `ReduceMean`  
  Inputs: `data(input)=B-C-1-1/float16/sparse  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `(1, 10, 1, 1)` | `float16` | `20` |

  _truth=(1, 1, 1, 1) claim=(1, 10, 1, 1)_

### Bug 39: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceProd@13`
- **Surface findings collapsed**: 21
- **Minimal repro**:

  Op: `ReduceProd`  
  Inputs: `data(input)=B-C-1-1/float16/sparse  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `(1, 10, 1, 1)` | `float16` | `20` |

  _truth=(1, 1, 1, 1) claim=(1, 10, 1, 1)_

### Bug 40: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `GatherND@13`
- **Surface findings collapsed**: 20
- **Minimal repro**:

  Op: `GatherND`  
  Inputs: `data(input)=BCHW/float32/random indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1`  
  Attrs: `{'batch_dims': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(30, 30)` | `float32` | `3600` |
  | onnx_tool| `(10, 30, 30)` | `float32` | `36000` |

  _truth=(30, 30) claim=(10, 30, 30)_

### Bug 41: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `GlobalMaxPool@13`
- **Surface findings collapsed**: 18
- **Minimal repro**:

  Op: `GlobalMaxPool`  
  Inputs: `X(input)=B-C-1-1/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer_

### Bug 42: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceMax@13`
- **Surface findings collapsed**: 16
- **Minimal repro**:

  Op: `ReduceMax`  
  Inputs: `data(input)=B-C-1-1/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `(1, 10, 1, 1)` | `float16` | `20` |

  _truth=(1, 1, 1, 1) claim=(1, 10, 1, 1)_

### Bug 43: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceMin@13`
- **Surface findings collapsed**: 16
- **Minimal repro**:

  Op: `ReduceMin`  
  Inputs: `data(input)=B-C-1-1/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `(1, 10, 1, 1)` | `float16` | `20` |

  _truth=(1, 1, 1, 1) claim=(1, 10, 1, 1)_

### Bug 44: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Einsum@13`
- **Surface findings collapsed**: 15
- **Minimal repro**:

  Op: `Einsum`  
  Inputs: `Inputs(input)=scalar/float16/random {'equation': b''} outputs=1`  
  Attrs: `{'equation': b''}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `2` |
  | onnx_tool| `None` | `None` | `None` |

  _IndexError: list index out of range_

### Bug 45: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `NonZero@13`
- **Surface findings collapsed**: 14
- **Minimal repro**:

  Op: `NonZero`  
  Inputs: `X(input)=scalar/bool/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `8` |
  | onnx_tool| `None` | `None` | `None` |

  _ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`._

### Bug 46: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `SpaceToDepth@13`
- **Surface findings collapsed**: 14
- **Minimal repro**:

  Op: `SpaceToDepth`  
  Inputs: `input(input)=B-C-1-1/float16/random {'blocksize': 1} outputs=1`  
  Attrs: `{'blocksize': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer_

### Bug 47: `wrong-dtype`

_onnx_tool's claimed output dtype disagrees with what ORT produces at runtime._

- **Affected ops** (1): `ReduceL2@13`
- **Surface findings collapsed**: 14
- **Minimal repro**:

  Op: `ReduceL2`  
  Inputs: `data(input)=scalar/int32/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `()` | `int32` | `4` |
  | onnx_tool| `()` | `float64` | `0` |

  _truth=int32 claim=float64_

### Bug 48: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Det@13`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Det`  
  Inputs: `X(input)=B-C-1-1/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `20` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node Det-Det_0 has no value_infer_

### Bug 49: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `DynamicQuantizeLinear@13`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `DynamicQuantizeLinear`  
  Inputs: `x(input)=scalar/float32/random  outputs=111`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `6` |
  | onnx_tool| `None` | `None` | `None` |

  _NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer_

### Bug 50: `wrong-dtype`

_onnx_tool's claimed output dtype disagrees with what ORT produces at runtime._

- **Affected ops** (1): `ReduceL2@13`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `ReduceL2`  
  Inputs: `data(input)=B-C-1-1/int64/random {'keepdims': 0, 'axes': [2, 3]} outputs=1`  
  Attrs: `{'keepdims': 0, 'axes': [2, 3]}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10)` | `int64` | `80` |
  | onnx_tool| `(1, 10)` | `float64` | `80` |

  _truth=int64 claim=float64_

### Bug 51: `wrong-dtype`

_onnx_tool's claimed output dtype disagrees with what ORT produces at runtime._

- **Affected ops** (1): `Round@13`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Round`  
  Inputs: `X(input)=scalar/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `()` | `float16` | `2` |
  | onnx_tool| `()` | `bool` | `0` |

  _truth=float16 claim=bool_

### Bug 52: `wrong-dtype`

_onnx_tool's claimed output dtype disagrees with what ORT produces at runtime._

- **Affected ops** (1): `Round@13`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Round`  
  Inputs: `X(input)=scalar/float32/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `()` | `float32` | `4` |
  | onnx_tool| `()` | `bool` | `0` |

  _truth=float32 claim=bool_

### Bug 53: `wrong-dtype`

_onnx_tool's claimed output dtype disagrees with what ORT produces at runtime._

- **Affected ops** (1): `Round@13`
- **Surface findings collapsed**: 12
- **Minimal repro**:

  Op: `Round`  
  Inputs: `X(input)=scalar/float64/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `()` | `float64` | `8` |
  | onnx_tool| `()` | `bool` | `0` |

  _truth=float64 claim=bool_

### Bug 54: `onnx-tool-fails-valid-model`

_onnx_tool throws when profiling a model the ONNX spec checker AND ORT both accept. Either onnx_tool's op coverage is incomplete or it has a bug in shape/value inference._

- **Affected ops** (1): `Split@13`
- **Surface findings collapsed**: 8
- **Minimal repro**:

  Op: `Split`  
  Inputs: `input(input)=BCHW/bool/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `None` | `None` | `9000` |
  | onnx_tool| `None` | `None` | `None` |

  _TypeError: list indices must be integers or slices, not NoneType_

### Bug 55: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `ReduceSum@13`
- **Surface findings collapsed**: 8
- **Minimal repro**:

  Op: `ReduceSum`  
  Inputs: `data(input)=BCHW/float16/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 1, 1)` | `float16` | `2` |
  | onnx_tool| `(1, 10, 30, 30)` | `float16` | `18000` |

  _truth=(1, 1, 1, 1) claim=(1, 10, 30, 30)_

### Bug 56: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `Where@13`
- **Surface findings collapsed**: 4
- **Minimal repro**:

  Op: `Where`  
  Inputs: `condition(input)=B-C-1-1/bool/all_true X(input)=B-1-H-1/uint8/random Y(input)=scalar/uint8/random  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10, 30, 1)` | `uint8` | `300` |
  | onnx_tool| `(1, 1, 30, 1)` | `uint8` | `30` |

  _truth=(1, 10, 30, 1) claim=(1, 1, 30, 1)_

### Bug 57: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `AveragePool@13`
- **Surface findings collapsed**: 3
- **Minimal repro**:

  Op: `AveragePool`  
  Inputs: `X(input)=B-1-H-1/float32/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'ceil_mode': 1} outputs=1`  
  Attrs: `{'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'ceil_mode': 1}`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 1, 15, 1)` | `float32` | `60` |
  | onnx_tool| `(1, 1, 16, 1)` | `float32` | `64` |

  _truth=(1, 1, 15, 1) claim=(1, 1, 16, 1)_

### Bug 58: `wrong-shape`

_onnx_tool's static shape inference disagrees with the runtime shape produced by ORT execution._

- **Affected ops** (1): `PRelu@13`
- **Surface findings collapsed**: 3
- **Minimal repro**:

  Op: `PRelu`  
  Inputs: `X(input)=B-C-1-1/float16/random slope(input)=B-1-H-1/float16/alternating  outputs=1`  

  | what     | shape | dtype | bytes |
  |----------|-------|-------|-------|
  | truth    | `(1, 10, 30, 1)` | `float16` | `600` |
  | onnx_tool| `(1, 1, 30, 1)` | `float16` | `60` |

  _truth=(1, 10, 30, 1) claim=(1, 1, 30, 1)_
