# onnx_tool audit report
_generated 2026-04-28T11:51:46_

**156 ops, 14877 test cases, 1011 with disagreements, 12248 invalid ignored, 13 build errors.**

## Bug class totals

| class | count |
|---|---|
| `onnx-tool-fails-valid-model` | 801 |
| `onnx-tool-error` | 801 |
| `scalar-volume` | 192 |
| `wrong-shape` | 30 |
| `wrong-dtype` | 13 |
| `ort-timeout` | 1 |

## Per-op summary

| op | cases | disagreements | invalid | build-errors | notes |
|---|---|---|---|---|---|
| [`IsInf@11`](#isinf@11) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Size@11`](#size@11) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ArgMin@11`](#argmin@11) | 128 | 63 | 65 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ThresholdedRelu@11`](#thresholdedrelu@11) | 128 | 42 | 86 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Selu@11`](#selu@11) | 128 | 40 | 88 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GlobalLpPool@11`](#globallppool@11) | 128 | 36 | 92 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`IsNaN@11`](#isnan@11) | 36 | 36 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MeanVarianceNormalization@11`](#meanvariancenormalization@11) | 128 | 36 | 92 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`LpPool@11`](#lppool@11) | 84 | 23 | 61 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceL1@11`](#reducel1@11) | 128 | 19 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceLogSum@11`](#reducelogsum@11) | 128 | 19 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceLogSumExp@11`](#reducelogsumexp@11) | 128 | 19 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceSumSquare@11`](#reducesumsquare@11) | 128 | 19 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Compress@11`](#compress@11) | 128 | 16 | 112 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`NonZero@11`](#nonzero@11) | 128 | 14 | 60 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Acos@11`](#acos@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Acosh@11`](#acosh@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Asin@11`](#asin@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Asinh@11`](#asinh@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Atanh@11`](#atanh@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Cosh@11`](#cosh@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`DequantizeLinear@11`](#dequantizelinear@11) | 128 | 12 | 116 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: x_zero_point |
| [`DynamicQuantizeLinear@11`](#dynamicquantizelinear@11) | 12 | 12 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Mean@11`](#mean@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Round@11`](#round@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sinh@11`](#sinh@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Softsign@11`](#softsign@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Tan@11`](#tan@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GlobalMaxPool@11`](#globalmaxpool@11) | 36 | 9 | 27 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`HardSigmoid@11`](#hardsigmoid@11) | 128 | 9 | 88 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Pow@11`](#pow@11) | 128 | 8 | 81 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceMax@11`](#reducemax@11) | 128 | 7 | 105 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceMin@11`](#reducemin@11) | 128 | 7 | 105 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Det@11`](#det@11) | 36 | 6 | 30 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Dropout@11`](#dropout@11) | 128 | 6 | 86 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Elu@11`](#elu@11) | 128 | 6 | 86 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`LeakyRelu@11`](#leakyrelu@11) | 128 | 6 | 86 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`PRelu@11`](#prelu@11) | 83 | 6 | 67 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Shrink@11`](#shrink@11) | 128 | 6 | 122 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Constant@11`](#constant@11) | 6 | 5 | 1 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MaxPool@11`](#maxpool@11) | 42 | 4 | 38 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`QuantizeLinear@11`](#quantizelinear@11) | 128 | 4 | 124 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: y_zero_point |
| [`ReverseSequence@11`](#reversesequence@11) | 128 | 4 | 124 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Squeeze@11`](#squeeze@11) | 128 | 4 | 121 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Abs@11`](#abs@11) | 128 | 3 | 116 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Add@11`](#add@11) | 83 | 3 | 67 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`And@11`](#and@11) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Atan@11`](#atan@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Ceil@11`](#ceil@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Clip@11`](#clip@11) | 102 | 3 | 98 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: min, max |
| [`Cos@11`](#cos@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Div@11`](#div@11) | 83 | 3 | 67 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Erf@11`](#erf@11) | 128 | 3 | 116 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Exp@11`](#exp@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Flatten@11`](#flatten@11) | 128 | 3 | 118 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Floor@11`](#floor@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Identity@11`](#identity@11) | 128 | 3 | 116 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Log@11`](#log@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Max@11`](#max@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Min@11`](#min@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Mul@11`](#mul@11) | 83 | 3 | 67 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Neg@11`](#neg@11) | 84 | 3 | 72 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Not@11`](#not@11) | 12 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Or@11`](#or@11) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Reciprocal@11`](#reciprocal@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceMean@11`](#reducemean@11) | 128 | 3 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceProd@11`](#reduceprod@11) | 128 | 3 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceSum@11`](#reducesum@11) | 128 | 3 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Relu@11`](#relu@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sigmoid@11`](#sigmoid@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sign@11`](#sign@11) | 128 | 3 | 116 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sin@11`](#sin@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Softplus@11`](#softplus@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sqrt@11`](#sqrt@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sub@11`](#sub@11) | 83 | 3 | 67 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sum@11`](#sum@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Tanh@11`](#tanh@11) | 36 | 3 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Xor@11`](#xor@11) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Conv@11`](#conv@11) | 128 | 2 | 123 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B |
| [`MatMulInteger@11`](#matmulinteger@11) | 128 | 2 | 123 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: a_zero_point, b_zero_point |
| [`RandomNormalLike@11`](#randomnormallike@11) | 128 | 2 | 125 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`RandomUniformLike@11`](#randomuniformlike@11) | 128 | 2 | 125 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`TopK@11`](#topk@11) | 128 | 2 | 122 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Equal@11`](#equal@11) | 58 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Greater@11`](#greater@11) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Less@11`](#less@11) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Mod@11`](#mod@11) | 128 | 1 | 119 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceL2@11`](#reducel2@11) | 128 | 1 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Split@11`](#split@11) | 128 | 1 | 124 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SplitToSequence@11`](#splittosequence@11) | 128 | 1 | 117 | 10 | Auto-generated from ONNX schema (opset 11). Optional inputs: split |
| [`Transpose@11`](#transpose@11) | 128 | 1 | 119 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ArgMax@11`](#argmax@11) | 128 | 0 | 65 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`AveragePool@11`](#averagepool@11) | 46 | 0 | 34 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`BatchNormalization@11`](#batchnormalization@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`BitShift@11`](#bitshift@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Cast@11`](#cast@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Concat@11`](#concat@11) | 128 | 0 | 119 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ConcatFromSequence@11`](#concatfromsequence@11) | 12 | 0 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ConstantOfShape@11`](#constantofshape@11) | 36 | 0 | 36 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ConvInteger@11`](#convinteger@11) | 128 | 0 | 127 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: x_zero_point, w_zero_point |
| [`ConvTranspose@11`](#convtranspose@11) | 128 | 0 | 127 | 1 | Auto-generated from ONNX schema (opset 11). Optional inputs: B |
| [`CumSum@11`](#cumsum@11) | 128 | 0 | 122 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`DepthToSpace@11`](#depthtospace@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Expand@11`](#expand@11) | 128 | 0 | 123 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`EyeLike@11`](#eyelike@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GRU@11`](#gru@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h |
| [`Gather@11`](#gather@11) | 128 | 0 | 123 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GatherElements@11`](#gatherelements@11) | 128 | 0 | 126 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GatherND@11`](#gathernd@11) | 128 | 0 | 125 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Gemm@11`](#gemm@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: C |
| [`GlobalAveragePool@11`](#globalaveragepool@11) | 36 | 0 | 27 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Hardmax@11`](#hardmax@11) | 108 | 0 | 72 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`If@11`](#if@11) | 12 | 0 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`InstanceNormalization@11`](#instancenormalization@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`LRN@11`](#lrn@11) | 128 | 0 | 123 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`LSTM@11`](#lstm@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h, initial_c, P |
| [`LogSoftmax@11`](#logsoftmax@11) | 108 | 0 | 72 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Loop@11`](#loop@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: M, cond |
| [`LpNormalization@11`](#lpnormalization@11) | 128 | 0 | 93 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MatMul@11`](#matmul@11) | 83 | 0 | 79 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MaxRoiPool@11`](#maxroipool@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MaxUnpool@11`](#maxunpool@11) | 128 | 0 | 126 | 2 | Auto-generated from ONNX schema (opset 11). Optional inputs: output_shape |
| [`Multinomial@11`](#multinomial@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`NonMaxSuppression@11`](#nonmaxsuppression@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: max_output_boxes_per_class, iou_threshold, score_threshold |
| [`OneHot@11`](#onehot@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Pad@11`](#pad@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: constant_value |
| [`QLinearConv@11`](#qlinearconv@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B |
| [`QLinearMatMul@11`](#qlinearmatmul@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`RNN@11`](#rnn@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h |
| [`RandomNormal@11`](#randomnormal@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`RandomUniform@11`](#randomuniform@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Range@11`](#range@11) | 32 | 0 | 31 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Reshape@11`](#reshape@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Resize@11`](#resize@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: sizes |
| [`RoiAlign@11`](#roialign@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Scan@11`](#scan@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Scatter@11`](#scatter@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ScatterElements@11`](#scatterelements@11) | 128 | 0 | 122 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ScatterND@11`](#scatternd@11) | 62 | 0 | 62 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SequenceAt@11`](#sequenceat@11) | 24 | 0 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SequenceConstruct@11`](#sequenceconstruct@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SequenceEmpty@11`](#sequenceempty@11) | 3 | 0 | 3 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SequenceErase@11`](#sequenceerase@11) | 25 | 0 | 25 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: position |
| [`SequenceInsert@11`](#sequenceinsert@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: position |
| [`SequenceLength@11`](#sequencelength@11) | 1 | 0 | 1 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Shape@11`](#shape@11) | 128 | 0 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Slice@11`](#slice@11) | 97 | 0 | 97 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: axes, steps |
| [`Softmax@11`](#softmax@11) | 108 | 0 | 72 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SpaceToDepth@11`](#spacetodepth@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`StringNormalizer@11`](#stringnormalizer@11) | 81 | 0 | 81 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`TfIdfVectorizer@11`](#tfidfvectorizer@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Tile@11`](#tile@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Unique@11`](#unique@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Unsqueeze@11`](#unsqueeze@11) | 128 | 0 | 121 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Upsample@11`](#upsample@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Where@11`](#where@11) | 70 | 0 | 70 | 0 | Auto-generated from ONNX schema (opset 11) |

## `IsInf@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 128 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=128, `onnx-tool-fails-valid-model`=128

### Disagreements
#### `onnx-tool-error` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random {'detect_negative': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'detect_negative': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'detect_negative': 1, 'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/random {'detect_negative': 1, 'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse {'detect_negative': 0, 'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating {'detect_negative': 0, 'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating {'detect_negative': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/random {'detect_negative': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/sparse {'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/alternating {'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'detect_negative': 1, 'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'detect_negative': 1, 'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/random {'detect_negative': 0, 'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/sparse {'detect_negative': 0, 'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/sparse {'detect_negative': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| ... | _+108 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random {'detect_negative': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'detect_negative': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'detect_negative': 1, 'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/random {'detect_negative': 1, 'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse {'detect_negative': 0, 'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating {'detect_negative': 0, 'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating {'detect_negative': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/random {'detect_negative': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/sparse {'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/alternating {'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'detect_negative': 1, 'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'detect_negative': 1, 'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/random {'detect_negative': 0, 'detect_positive': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/sparse {'detect_negative': 0, 'detect_positive': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/sparse {'detect_negative': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| ... | _+108 more cases_ | | | |

## `Size@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 128 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=128, `onnx-tool-fails-valid-model`=128

### Disagreements
#### `onnx-tool-error` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/bool/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/bool/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=scalar/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| ... | _+108 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/bool/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/bool/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=scalar/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| ... | _+108 more cases_ | | | |

## `ArgMin@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 63 with disagreements, 65 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=63, `onnx-tool-fails-valid-model`=63

### Disagreements
#### `onnx-tool-error` (63 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/random {'axis': 0, 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random {'axis': -1, 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axis': -1, 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axis': 0, 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axis': 0, 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axis': -1, 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axis': -1, 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/sparse {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| ... | _+43 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (63 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/random {'axis': 0, 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random {'axis': -1, 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axis': -1, 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `240B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axis': 0, 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axis': 0, 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axis': -1, 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axis': -1, 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/sparse {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| ... | _+43 more cases_ | | | |

## `ThresholdedRelu@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 42 with disagreements, 86 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=42, `onnx-tool-fails-valid-model`=42

### Disagreements
#### `onnx-tool-error` (42 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| ... | _+22 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (42 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| ... | _+22 more cases_ | | | |

## `Selu@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 40 with disagreements, 88 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=40, `onnx-tool-fails-valid-model`=40

### Disagreements
#### `onnx-tool-error` (40 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'gamma': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random {'gamma': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse {'alpha': 0.5, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'gamma': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.0, 'gamma': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.0, 'gamma': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 1.0, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'gamma': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.0, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.5, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 1.0, 'gamma': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 0.0, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| ... | _+20 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (40 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'gamma': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random {'gamma': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse {'alpha': 0.5, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'gamma': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.0, 'gamma': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 0.0, 'gamma': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'alpha': 1.0, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'gamma': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.0, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 0.5, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 1.0, 'gamma': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'alpha': 0.0, 'gamma': 1.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| ... | _+20 more cases_ | | | |

## `GlobalLpPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 36 with disagreements, 92 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=36, `onnx-tool-fails-valid-model`=36

### Disagreements
#### `onnx-tool-error` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| ... | _+16 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| ... | _+16 more cases_ | | | |

## `IsNaN@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 36 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=36, `onnx-tool-fails-valid-model`=36

### Disagreements
#### `onnx-tool-error` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| ... | _+16 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| ... | _+16 more cases_ | | | |

## `MeanVarianceNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 36 with disagreements, 92 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=36, `onnx-tool-fails-valid-model`=36

### Disagreements
#### `onnx-tool-error` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| ... | _+16 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'axes': [0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| ... | _+16 more cases_ | | | |

## `LpPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 84 cases, 23 with disagreements, 61 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=23, `onnx-tool-fails-valid-model`=23

### Disagreements
#### `onnx-tool-error` (23 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [3, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET'}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'strides': [2, 2], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1], 'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'SAME_UPPER', 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0], 'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| ... | _+3 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (23 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [3, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `15680B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET'}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'strides': [2, 2], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1], 'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'SAME_UPPER', 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4500B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0], 'p': 2}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'p': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| ... | _+3 more cases_ | | | |

## `ReduceL1@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 19 with disagreements, 109 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=19, `onnx-tool-fails-valid-model`=19

### Disagreements
#### `onnx-tool-error` (19 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/sparse {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (19 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/sparse {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |

## `ReduceLogSum@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 19 with disagreements, 109 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=19, `onnx-tool-fails-valid-model`=19

### Disagreements
#### `onnx-tool-error` (19 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/sparse {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (19 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/sparse {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |

## `ReduceLogSumExp@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 19 with disagreements, 109 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=19, `onnx-tool-fails-valid-model`=19

### Disagreements
#### `onnx-tool-error` (19 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/sparse {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (19 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/sparse {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |

## `ReduceSumSquare@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 19 with disagreements, 109 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=19, `onnx-tool-fails-valid-model`=19

### Disagreements
#### `onnx-tool-error` (19 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/sparse {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (19 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/sparse {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [0], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random {'axes': [2, 3], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [2, 3], 'keepdims': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1]}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |

## `Compress@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 16 with disagreements, 112 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=16, `onnx-tool-fails-valid-model`=16

### Disagreements
#### `onnx-tool-error` (16 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_true ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_false ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=BCHW/bool/alternating {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=BCHW/bool/all_true {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=B-1-H-1/bool/random condition(input)=B-1-H-1/bool/all_true {'axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=B-C-1-1/bool/random condition(input)=B-C-1-1/bool/all_true ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=B-C-1-1/bool/all_true {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=B-1-H-1/bool/all_true {'axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=scalar/bool/all_false ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=BCHW/bool/all_false {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=B-C-1-1/bool/all_false {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=B-1-H-1/bool/alternating {'axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=scalar/bool/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=B-C-1-1/bool/all_true {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=B-1-H-1/bool/all_true {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=scalar/bool/all_true {'axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |

#### `onnx-tool-fails-valid-model` (16 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_true ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_false ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=BCHW/bool/alternating {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=BCHW/bool/all_true {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=B-1-H-1/bool/random condition(input)=B-1-H-1/bool/all_true {'axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=B-C-1-1/bool/random condition(input)=B-C-1-1/bool/all_true ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=B-C-1-1/bool/all_true {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=B-1-H-1/bool/all_true {'axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=scalar/bool/all_false ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=BCHW/bool/all_false {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=B-C-1-1/bool/all_false {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=B-1-H-1/bool/alternating {'axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4500B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=scalar/bool/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=B-C-1-1/bool/all_true {'axis': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=B-1-H-1/bool/all_true {'axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=scalar/bool/all_true {'axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `300B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |

## `NonZero@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 14 with disagreements, 60 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=14, `onnx-tool-fails-valid-model`=14

### Disagreements
#### `onnx-tool-error` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/bool/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/bool/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int64/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |

#### `onnx-tool-fails-valid-model` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/bool/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/bool/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int64/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |

## `Acos@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |

## `Acosh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |

## `Asin@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |

## `Asinh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |

## `Atanh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |

## `Cosh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |

## `DequantizeLinear@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: x_zero_point_

- 128 cases, 12 with disagreements, 116 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=22

### Disagreements
#### `scalar-volume` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=scalar/int32/random x_scale(init)=scalar/float32/random x_zero_point(init)=scalar/int32/random ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| `y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/random x_scale(init)=scalar/float32/alternating x_zero_point(init)=scalar/int32/alternating ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/sparse ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/alternating ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/alternating x_scale(init)=scalar/float32/random x_zero_point(init)=scalar/int32/alternating ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int8/random x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int8/sparse ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/int8/alternating x_scale(init)=scalar/float32/alternating ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int8/alternating x_scale(init)=scalar/float32/alternating x_zero_point(init)=scalar/int8/random ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/uint8/random x_scale(init)=scalar/float32/random x_zero_point(init)=scalar/uint8/alternating ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=B-C-1-1/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/sparse ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=B-C-1-1/int32/alternating x_scale(init)=scalar/float32/random ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=B-C-1-1/int32/alternating x_scale(init)=scalar/float32/sparse ` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `DynamicQuantizeLinear@11`
_Auto-generated from ONNX schema (opset 11)_

- 12 cases, 12 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=BCHW/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=BCHW/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=BCHW/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=BCHW/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9005B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=BCHW/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9005B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=BCHW/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9005B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `35B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `15B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `6B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `15B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `15B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `35B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `35B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `6B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `6B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |

## `Mean@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |

## `Round@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `wrong-dtype`=12

### Disagreements
#### `wrong-dtype` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float16` / `18000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float16 claim=bool |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float16` / `18000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float16 claim=bool |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float16` / `18000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| `Y` | `wrong-dtype` | `(1,1,30,1)` / `float16` / `60B` | `(1,1,30,1)` / `bool` / `30B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float16` / `20B` | `(1,10,1,1)` / `bool` / `10B` | truth=float16 claim=bool |
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `wrong-dtype` | `()` / `float16` / `2B` | `()` / `bool` / `0B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float16` / `20B` | `(1,10,1,1)` / `bool` / `10B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-C-1-1/float16/alternating ` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float16` / `20B` | `(1,10,1,1)` / `bool` / `10B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| `Y` | `wrong-dtype` | `(1,1,30,1)` / `float16` / `60B` | `(1,1,30,1)` / `bool` / `30B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-1-H-1/float16/alternating ` | | | | |
| `Y` | `wrong-dtype` | `(1,1,30,1)` / `float16` / `60B` | `(1,1,30,1)` / `bool` / `30B` | truth=float16 claim=bool |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `wrong-dtype` | `()` / `float16` / `2B` | `()` / `bool` / `0B` | truth=float16 claim=bool |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `wrong-dtype` | `()` / `float16` / `2B` | `()` / `bool` / `0B` | truth=float16 claim=bool |

## `Sinh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |

## `Softsign@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |

## `Tan@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |

## `GlobalMaxPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 27 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=9, `onnx-tool-fails-valid-model`=9

### Disagreements
#### `onnx-tool-error` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |

## `HardSigmoid@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 9 with disagreements, 88 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random {'beta': 0.5}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'beta': 1.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0, 'beta': 0.5}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5, 'beta': 0.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5, 'beta': 1.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0, 'beta': 0.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Pow@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 8 with disagreements, 81 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=7, `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random Y(input)=scalar/float16/random ` | | | | |
| `Z` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (7 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=B-C-1-1/float16/random Y(input)=B-1-H-1/float16/random ` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/random Y(input)=B-1-H-1/float16/alternating ` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/sparse Y(input)=B-1-H-1/float16/alternating ` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/alternating Y(input)=B-1-H-1/float16/sparse ` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float16/random Y(input)=B-C-1-1/float16/sparse ` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float16/sparse Y(input)=B-C-1-1/float16/sparse ` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float16/alternating Y(input)=B-C-1-1/float16/random ` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |

## `ReduceMax@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 7 with disagreements, 105 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=5, `wrong-shape`=2

### Disagreements
#### `scalar-volume` (5 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random {'axes': [1], 'keepdims': 1}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/sparse {'axes': [2, 3]}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [0]}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |

## `ReduceMin@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 7 with disagreements, 105 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=5, `wrong-shape`=2

### Disagreements
#### `scalar-volume` (5 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random {'axes': [1], 'keepdims': 1}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/sparse {'axes': [2, 3]}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [0]}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [1], 'keepdims': 0}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |

## `Det@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 6 with disagreements, 30 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=6, `onnx-tool-fails-valid-model`=6

### Disagreements
#### `onnx-tool-error` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |

## `Dropout@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 6 with disagreements, 86 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=12

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random {'ratio': 0.0}` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/sparse {'ratio': 0.5}` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'ratio': 1.0}` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random ` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'ratio': 0.5}` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'ratio': 1.0}` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Elu@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 6 with disagreements, 86 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=6

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `LeakyRelu@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 6 with disagreements, 86 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=6

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0}` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `PRelu@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 6 with disagreements, 67 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3, `wrong-shape`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random slope(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random slope(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse slope(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=B-C-1-1/float16/random slope(input)=B-1-H-1/float16/alternating ` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/sparse slope(input)=B-1-H-1/float16/sparse ` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/alternating slope(input)=B-1-H-1/float16/random ` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |

## `Shrink@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 6 with disagreements, 122 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=6, `onnx-tool-fails-valid-model`=6

### Disagreements
#### `onnx-tool-error` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random {'lambd': 0.0, 'bias': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random {'lambd': 0.0, 'bias': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse {'lambd': 0.5, 'bias': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating {'lambd': 0.5, 'bias': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random {'lambd': 0.0, 'bias': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random {'lambd': 0.0, 'bias': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse {'lambd': 0.5, 'bias': 0.0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating {'lambd': 0.5, 'bias': 0.5}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |

## `Constant@11`
_Auto-generated from ONNX schema (opset 11)_

- 6 cases, 5 with disagreements, 1 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=3, `onnx-tool-fails-valid-model`=3, `scalar-volume`=1, `wrong-dtype`=1

### Disagreements
#### `onnx-tool-error` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'value': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'int' object has no attribute 'shape' |
| _case:_ ` {'sparse_value': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value': 0, 'sparse_value': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'int' object has no attribute 'shape' |

#### `onnx-tool-fails-valid-model` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'value': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'int' object has no attribute 'shape' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'int' object has no attribute 'shape' |
| _case:_ ` {'sparse_value': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value': 0, 'sparse_value': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'int' object has no attribute 'shape' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'int' object has no attribute 'shape' |

#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
}` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

#### `wrong-dtype` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'sparse_value': 0}` | | | | |
| `output` | `wrong-dtype` | `()` / `int64` / `8B` | `()` / `float32` / `0B` | truth=int64 claim=float32 |

## `MaxPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 42 cases, 4 with disagreements, 38 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=4

### Disagreements
#### `wrong-shape` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [3, 3]}` | | | | |
| `Indices` | `wrong-shape` | `(1,10,28,28)` / `int64` / `62720B` | `()` / `int64` / `0B` | truth=(1, 10, 28, 28) claim=() |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'kernel_shape': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'ceil_mode': 0}` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0]}` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0]}` | | | | |
| `Indices` | `wrong-shape` | `(1,10,1,1)` / `int64` / `80B` | `()` / `int64` / `0B` | truth=(1, 10, 1, 1) claim=() |

## `QuantizeLinear@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: y_zero_point_

- 128 cases, 4 with disagreements, 124 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=scalar/float32/random y_scale(init)=scalar/float32/random y_zero_point(init)=scalar/int8/random ` | | | | |
| `y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/random y_scale(init)=scalar/float32/alternating y_zero_point(init)=scalar/int8/sparse ` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/alternating y_scale(init)=scalar/float32/random y_zero_point(init)=scalar/int8/sparse ` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/alternating y_scale(init)=scalar/float32/sparse y_zero_point(init)=scalar/int8/sparse ` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |

## `ReverseSequence@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 4 with disagreements, 124 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=4, `onnx-tool-fails-valid-model`=4

### Disagreements
#### `onnx-tool-error` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-1/int64/sparse {'time_axis': -1, 'batch_axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-10/int64/sparse {'batch_axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-10/int64/alternating {'time_axis': 0, 'batch_axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-1/int64/sparse {'time_axis': -1, 'batch_axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-10/int64/sparse {'batch_axis': -1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-10/int64/alternating {'time_axis': 0, 'batch_axis': 1}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |

## `Squeeze@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 4 with disagreements, 121 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=3, `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/bool/alternating ` | | | | |
| `squeezed` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

#### `wrong-shape` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=B-C-1-1/bool/random ` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `bool` / `10B` | `(10,1,1)` / `bool` / `10B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/bool/alternating ` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `bool` / `10B` | `(10,1,1)` / `bool` / `10B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/bool/alternating ` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `bool` / `30B` | `(1,30,1)` / `bool` / `30B` | truth=(30,) claim=(1, 30, 1) |

## `Abs@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 116 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Add@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 3 with disagreements, 67 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/sparse ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/sparse B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `And@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_true ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_false ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/alternating ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Atan@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Ceil@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Clip@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: min, max_

- 102 cases, 3 with disagreements, 98 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=7

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random min(init)=scalar/float16/random max(init)=scalar/float16/random ` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=BCHW/float16/sparse min(init)=scalar/float16/alternating max(init)=scalar/float16/random ` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=B-C-1-1/float16/sparse min(init)=scalar/float16/random max(init)=scalar/float16/sparse ` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Cos@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Div@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 3 with disagreements, 67 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/sparse ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/sparse B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Erf@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 116 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Exp@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Flatten@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 118 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=3

### Disagreements
#### `wrong-shape` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=B-C-1-1/bool/random {'axis': -1}` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `bool` / `10B` | `(1,10)` / `bool` / `10B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/bool/sparse {'axis': -1}` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `bool` / `10B` | `(1,10)` / `bool` / `10B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-1-H-1/bool/alternating {'axis': -1}` | | | | |
| `output` | `wrong-shape` | `(30,1)` / `bool` / `30B` | `(1,30)` / `bool` / `30B` | truth=(30, 1) claim=(1, 30) |

## `Floor@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Identity@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 116 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/bool/random ` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/bool/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/bool/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Log@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Max@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=scalar/float16/random ` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/sparse ` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/alternating ` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Min@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=scalar/float16/random ` | | | | |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/sparse ` | | | | |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/alternating ` | | | | |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Mul@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 3 with disagreements, 67 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/sparse ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/sparse B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Neg@11`
_Auto-generated from ONNX schema (opset 11)_

- 84 cases, 3 with disagreements, 72 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Not@11`
_Auto-generated from ONNX schema (opset 11)_

- 12 cases, 3 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/bool/all_true ` | | | | |
| `Y` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `X(input)=scalar/bool/all_false ` | | | | |
| `Y` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `X(input)=scalar/bool/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Or@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_true ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_false ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/alternating ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Reciprocal@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `ReduceMean@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 109 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=2, `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |

## `ReduceProd@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 109 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=2, `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |

## `ReduceSum@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 109 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=2, `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |
| _case:_ `data(input)=B-1-H-1/float16/alternating ` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `()` / `float16` / `0B` | truth=(1, 1, 1, 1) claim=() |

## `Relu@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Sigmoid@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Sign@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 116 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Sin@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Softplus@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Sqrt@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating ` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Sub@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 3 with disagreements, 67 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/sparse ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/sparse B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Sum@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=scalar/float16/random ` | | | | |
| `sum` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/sparse ` | | | | |
| `sum` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/alternating ` | | | | |
| `sum` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Tanh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 3 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating ` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Xor@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_true ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_false ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/alternating ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Conv@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: B_

- 128 cases, 2 with disagreements, 123 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=2

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=B-C-1-1/float16/random W(input)=B-C-1-1/float16/sparse B(init)=scalar/float16/random {'group': 1, 'auto_pad': b'NOTSET', 'strides': [1, 1]}` | | | | |
| `B` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=B-C-1-1/float16/alternating W(input)=B-C-1-1/float16/random B(init)=scalar/float16/sparse {'group': 1, 'auto_pad': b'NOTSET', 'dilations': [1, 1], 'pads': [1, 1, 1, 1]}` | | | | |
| `B` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `MatMulInteger@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: a_zero_point, b_zero_point_

- 128 cases, 2 with disagreements, 123 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=BCHW/uint8/random B(input)=B-1-H-1/uint8/random a_zero_point(init)=scalar/uint8/sparse ` | | | | |
| `a_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=B-C-1-1/int8/random B(input)=B-C-1-1/int8/sparse a_zero_point(init)=scalar/int8/alternating b_zero_point(init)=scalar/int8/sparse ` | | | | |
| `a_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| `b_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |

## `RandomNormalLike@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 2 with disagreements, 125 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=2

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random {'seed': 0.5, 'mean': 0.0, 'scale': 1.0}` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse {'seed': 0.5, 'mean': 0.5}` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `RandomUniformLike@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 2 with disagreements, 125 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=2

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random {'low': 0.5, 'high': 0.0, 'seed': 1.0}` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse {'low': 0.5, 'high': 0.5}` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `TopK@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 2 with disagreements, 122 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=2, `onnx-tool-fails-valid-model`=2

### Disagreements
#### `onnx-tool-error` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random K(init)=1d-1/int64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float16/alternating K(init)=1d-1/int64/alternating {'largest': 0, 'sorted': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |

#### `onnx-tool-fails-valid-model` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random K(init)=1d-1/int64/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `21008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float16/alternating K(init)=1d-1/int64/alternating {'largest': 0, 'sorted': 0}` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `3008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |

## `Equal@11`
_Auto-generated from ONNX schema (opset 11)_

- 58 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/random B(input)=scalar/bool/random ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Greater@11`
_Auto-generated from ONNX schema (opset 11)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Less@11`
_Auto-generated from ONNX schema (opset 11)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random ` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Mod@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 1 with disagreements, 119 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random {'fmod': 1}` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `ReduceL2@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 1 with disagreements, 109 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 1}` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Split@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 1 with disagreements, 124 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=1, `onnx-tool-fails-valid-model`=1

### Disagreements
#### `onnx-tool-error` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |

#### `onnx-tool-fails-valid-model` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random ` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |

## `SplitToSequence@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: split_

- 128 cases, 1 with disagreements, 117 invalid ignored, 10 build errors
- bug classes hit: `ort-timeout`=1

### Build errors
- input(input)=BCHW/bool/alternating split(init)=scalar/int32/sparse {'keepdims': 0}
- input(input)=BCHW/float16/random split(init)=scalar/int64/sparse {'axis': 1, 'keepdims': 0}
- input(input)=BCHW/float32/sparse split(init)=scalar/int32/sparse 
- input(input)=BCHW/float64/alternating split(init)=scalar/int32/sparse {'keepdims': 0}
- input(input)=BCHW/int16/random split(init)=scalar/int64/sparse {'axis': 1, 'keepdims': 0}
- input(input)=BCHW/int16/sparse split(init)=scalar/int32/sparse {'axis': 0}
- input(input)=BCHW/int16/alternating split(init)=scalar/int64/sparse {'keepdims': 0}
- input(input)=BCHW/int8/sparse split(init)=scalar/int32/sparse {'axis': 1}
- input(input)=BCHW/int8/alternating split(init)=scalar/int64/sparse {'axis': 0, 'keepdims': 1}
- input(input)=BCHW/uint16/sparse split(init)=scalar/int32/sparse {'axis': 1}

### Disagreements
#### `ort-timeout` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/int32/sparse split(init)=scalar/int32/sparse {'axis': 0}` | | | | |
| `<model>` | `ort-timeout` | `?` / `None` / `?B` | `?` / `None` / `?B` | ORT/truth oracle did not finish within 10s (phase=start) |

## `Transpose@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 1 with disagreements, 119 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/bool/random ` | | | | |
| `transposed` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `ArgMax@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 65 invalid ignored, 0 build errors

> No disagreements found.

## `AveragePool@11`
_Auto-generated from ONNX schema (opset 11)_

- 46 cases, 0 with disagreements, 34 invalid ignored, 0 build errors

> No disagreements found.

## `BatchNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `BitShift@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Cast@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Concat@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 119 invalid ignored, 0 build errors

> No disagreements found.

## `ConcatFromSequence@11`
_Auto-generated from ONNX schema (opset 11)_

- 12 cases, 0 with disagreements, 12 invalid ignored, 0 build errors

> No disagreements found.

## `ConstantOfShape@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 0 with disagreements, 36 invalid ignored, 0 build errors

> No disagreements found.

## `ConvInteger@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: x_zero_point, w_zero_point_

- 128 cases, 0 with disagreements, 127 invalid ignored, 0 build errors

> No disagreements found.

## `ConvTranspose@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: B_

- 128 cases, 0 with disagreements, 127 invalid ignored, 1 build errors

### Build errors
- X(input)=BCHW/float64/random W(input)=scalar/float64/sparse B(init)=B-C-1-1/float64/sparse {'pads': [1, 1, 1, 1]}

## `CumSum@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 122 invalid ignored, 0 build errors

> No disagreements found.

## `DepthToSpace@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Expand@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 123 invalid ignored, 0 build errors

> No disagreements found.

## `EyeLike@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `GRU@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Gather@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 123 invalid ignored, 0 build errors

> No disagreements found.

## `GatherElements@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 126 invalid ignored, 0 build errors

> No disagreements found.

## `GatherND@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 125 invalid ignored, 0 build errors

> No disagreements found.

## `Gemm@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: C_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `GlobalAveragePool@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 0 with disagreements, 27 invalid ignored, 0 build errors

> No disagreements found.

## `Hardmax@11`
_Auto-generated from ONNX schema (opset 11)_

- 108 cases, 0 with disagreements, 72 invalid ignored, 0 build errors

> No disagreements found.

## `If@11`
_Auto-generated from ONNX schema (opset 11)_

- 12 cases, 0 with disagreements, 12 invalid ignored, 0 build errors

> No disagreements found.

## `InstanceNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `LRN@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 123 invalid ignored, 0 build errors

> No disagreements found.

## `LSTM@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h, initial_c, P_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `LogSoftmax@11`
_Auto-generated from ONNX schema (opset 11)_

- 108 cases, 0 with disagreements, 72 invalid ignored, 0 build errors

> No disagreements found.

## `Loop@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: M, cond_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `LpNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 93 invalid ignored, 0 build errors

> No disagreements found.

## `MatMul@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 0 with disagreements, 79 invalid ignored, 0 build errors

> No disagreements found.

## `MaxRoiPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `MaxUnpool@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: output_shape_

- 128 cases, 0 with disagreements, 126 invalid ignored, 2 build errors

### Build errors
- X(input)=BCHW/float32/alternating I(input)=scalar/int64/random {'kernel_shape': [3, 3], 'strides': [1, 1]}
- X(input)=BCHW/float32/alternating I(input)=scalar/int64/alternating {'kernel_shape': [3, 3], 'strides': [1, 1], 'pads': [1, 1, 1, 1]}

## `Multinomial@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `NonMaxSuppression@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: max_output_boxes_per_class, iou_threshold, score_threshold_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `OneHot@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Pad@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: constant_value_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `QLinearConv@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: B_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `QLinearMatMul@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `RNN@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `RandomNormal@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `RandomUniform@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Range@11`
_Auto-generated from ONNX schema (opset 11)_

- 32 cases, 0 with disagreements, 31 invalid ignored, 0 build errors

> No disagreements found.

## `Reshape@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Resize@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: sizes_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `RoiAlign@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Scan@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Scatter@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `ScatterElements@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 122 invalid ignored, 0 build errors

> No disagreements found.

## `ScatterND@11`
_Auto-generated from ONNX schema (opset 11)_

- 62 cases, 0 with disagreements, 62 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceAt@11`
_Auto-generated from ONNX schema (opset 11)_

- 24 cases, 0 with disagreements, 24 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceConstruct@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceEmpty@11`
_Auto-generated from ONNX schema (opset 11)_

- 3 cases, 0 with disagreements, 3 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceErase@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: position_

- 25 cases, 0 with disagreements, 25 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceInsert@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: position_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceLength@11`
_Auto-generated from ONNX schema (opset 11)_

- 1 cases, 0 with disagreements, 1 invalid ignored, 0 build errors

> No disagreements found.

## `Shape@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 0 invalid ignored, 0 build errors

> No disagreements found.

## `Slice@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: axes, steps_

- 97 cases, 0 with disagreements, 97 invalid ignored, 0 build errors

> No disagreements found.

## `Softmax@11`
_Auto-generated from ONNX schema (opset 11)_

- 108 cases, 0 with disagreements, 72 invalid ignored, 0 build errors

> No disagreements found.

## `SpaceToDepth@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `StringNormalizer@11`
_Auto-generated from ONNX schema (opset 11)_

- 81 cases, 0 with disagreements, 81 invalid ignored, 0 build errors

> No disagreements found.

## `TfIdfVectorizer@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Tile@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Unique@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Unsqueeze@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 121 invalid ignored, 0 build errors

> No disagreements found.

## `Upsample@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Where@11`
_Auto-generated from ONNX schema (opset 11)_

- 70 cases, 0 with disagreements, 70 invalid ignored, 0 build errors

> No disagreements found.
