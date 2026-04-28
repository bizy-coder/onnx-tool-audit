# onnx_tool audit report
_generated 2026-04-28T18:42:27_

**156 ops, 14415 test cases, 2859 with disagreements, 7183 invalid ignored, 5 build errors.**

## Bug class totals

| class | count |
|---|---|
| `onnx-tool-fails-valid-model` | 2071 |
| `onnx-tool-error` | 2071 |
| `scalar-volume` | 490 |
| `wrong-shape` | 458 |
| `wrong-dtype` | 62 |

## Per-op summary

| op | cases | disagreements | invalid | build-errors | notes |
|---|---|---|---|---|---|
| [`IsInf@11`](#isinf@11) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Shrink@11`](#shrink@11) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Size@11`](#size@11) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Compress@11`](#compress@11) | 128 | 127 | 1 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`LpPool@11`](#lppool@11) | 128 | 101 | 27 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`BitShift@11`](#bitshift@11) | 128 | 93 | 35 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Selu@11`](#selu@11) | 128 | 92 | 36 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ThresholdedRelu@11`](#thresholdedrelu@11) | 128 | 89 | 39 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`RandomNormal@11`](#randomnormal@11) | 128 | 85 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`RandomUniform@11`](#randomuniform@11) | 128 | 85 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceL1@11`](#reducel1@11) | 128 | 85 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceLogSum@11`](#reducelogsum@11) | 128 | 85 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceLogSumExp@11`](#reducelogsumexp@11) | 128 | 85 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceSumSquare@11`](#reducesumsquare@11) | 128 | 85 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GlobalLpPool@11`](#globallppool@11) | 128 | 72 | 56 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MeanVarianceNormalization@11`](#meanvariancenormalization@11) | 128 | 72 | 56 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ArgMin@11`](#argmin@11) | 128 | 63 | 65 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`BatchNormalization@11`](#batchnormalization@11) | 128 | 62 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MaxPool@11`](#maxpool@11) | 128 | 62 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Unique@11`](#unique@11) | 128 | 45 | 83 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`IsNaN@11`](#isnan@11) | 36 | 36 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReverseSequence@11`](#reversesequence@11) | 128 | 36 | 92 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Round@11`](#round@11) | 36 | 36 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceMax@11`](#reducemax@11) | 128 | 32 | 30 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceMin@11`](#reducemin@11) | 128 | 32 | 30 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceL2@11`](#reducel2@11) | 128 | 31 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Abs@11`](#abs@11) | 128 | 29 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sign@11`](#sign@11) | 128 | 29 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Flatten@11`](#flatten@11) | 128 | 27 | 15 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Acos@11`](#acos@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Acosh@11`](#acosh@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Asin@11`](#asin@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Asinh@11`](#asinh@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Atanh@11`](#atanh@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Cosh@11`](#cosh@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Mean@11`](#mean@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sinh@11`](#sinh@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Softsign@11`](#softsign@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Tan@11`](#tan@11) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Squeeze@11`](#squeeze@11) | 128 | 23 | 49 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`TopK@11`](#topk@11) | 128 | 23 | 60 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Pow@11`](#pow@11) | 128 | 22 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Neg@11`](#neg@11) | 84 | 21 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Cast@11`](#cast@11) | 128 | 20 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Identity@11`](#identity@11) | 128 | 20 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceMean@11`](#reducemean@11) | 128 | 19 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceProd@11`](#reduceprod@11) | 128 | 19 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ReduceSum@11`](#reducesum@11) | 128 | 19 | 43 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GlobalMaxPool@11`](#globalmaxpool@11) | 36 | 18 | 18 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Split@11`](#split@11) | 128 | 18 | 65 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Elu@11`](#elu@11) | 128 | 17 | 39 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`LeakyRelu@11`](#leakyrelu@11) | 128 | 17 | 39 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Dropout@11`](#dropout@11) | 128 | 15 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`HardSigmoid@11`](#hardsigmoid@11) | 128 | 14 | 36 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`NonZero@11`](#nonzero@11) | 128 | 14 | 60 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SpaceToDepth@11`](#spacetodepth@11) | 128 | 14 | 114 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`DequantizeLinear@11`](#dequantizelinear@11) | 128 | 12 | 116 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: x_zero_point |
| [`Det@11`](#det@11) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`DynamicQuantizeLinear@11`](#dynamicquantizelinear@11) | 12 | 12 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Ceil@11`](#ceil@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Exp@11`](#exp@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Floor@11`](#floor@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Log@11`](#log@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Max@11`](#max@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Min@11`](#min@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Reciprocal@11`](#reciprocal@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Relu@11`](#relu@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sigmoid@11`](#sigmoid@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sin@11`](#sin@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sqrt@11`](#sqrt@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sum@11`](#sum@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Tanh@11`](#tanh@11) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Atan@11`](#atan@11) | 36 | 6 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Clip@11`](#clip@11) | 102 | 6 | 95 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: min, max |
| [`Cos@11`](#cos@11) | 36 | 6 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Erf@11`](#erf@11) | 128 | 6 | 104 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`PRelu@11`](#prelu@11) | 83 | 6 | 55 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`QuantizeLinear@11`](#quantizelinear@11) | 128 | 6 | 122 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: y_zero_point |
| [`Softplus@11`](#softplus@11) | 36 | 6 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Transpose@11`](#transpose@11) | 128 | 6 | 14 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Add@11`](#add@11) | 83 | 4 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Mul@11`](#mul@11) | 83 | 4 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Sub@11`](#sub@11) | 83 | 4 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Where@11`](#where@11) | 70 | 4 | 32 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`And@11`](#and@11) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`AveragePool@11`](#averagepool@11) | 128 | 3 | 30 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Not@11`](#not@11) | 12 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Or@11`](#or@11) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Xor@11`](#xor@11) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Conv@11`](#conv@11) | 128 | 2 | 117 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B |
| [`ConvInteger@11`](#convinteger@11) | 128 | 2 | 125 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: x_zero_point, w_zero_point |
| [`MatMulInteger@11`](#matmulinteger@11) | 128 | 2 | 123 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: a_zero_point, b_zero_point |
| [`RandomNormalLike@11`](#randomnormallike@11) | 128 | 2 | 118 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`RandomUniformLike@11`](#randomuniformlike@11) | 128 | 2 | 118 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Constant@11`](#constant@11) | 2 | 1 | 1 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Equal@11`](#equal@11) | 58 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Greater@11`](#greater@11) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Less@11`](#less@11) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ArgMax@11`](#argmax@11) | 128 | 0 | 65 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Concat@11`](#concat@11) | 128 | 0 | 20 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ConcatFromSequence@11`](#concatfromsequence@11) | 12 | 0 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ConstantOfShape@11`](#constantofshape@11) | 24 | 0 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ConvTranspose@11`](#convtranspose@11) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`CumSum@11`](#cumsum@11) | 128 | 0 | 112 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`DepthToSpace@11`](#depthtospace@11) | 128 | 0 | 118 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Div@11`](#div@11) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`Expand@11`](#expand@11) | 128 | 0 | 106 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`EyeLike@11`](#eyelike@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GRU@11`](#gru@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h |
| [`Gather@11`](#gather@11) | 128 | 0 | 73 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GatherElements@11`](#gatherelements@11) | 128 | 0 | 93 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`GatherND@11`](#gathernd@11) | 128 | 0 | 106 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Gemm@11`](#gemm@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: C |
| [`GlobalAveragePool@11`](#globalaveragepool@11) | 36 | 0 | 18 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Hardmax@11`](#hardmax@11) | 108 | 0 | 36 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`If@11`](#if@11) | 12 | 0 | 12 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`InstanceNormalization@11`](#instancenormalization@11) | 128 | 0 | 35 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`LRN@11`](#lrn@11) | 128 | 0 | 109 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`LSTM@11`](#lstm@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h, initial_c, P |
| [`LogSoftmax@11`](#logsoftmax@11) | 108 | 0 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Loop@11`](#loop@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: M, cond |
| [`LpNormalization@11`](#lpnormalization@11) | 128 | 0 | 42 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MatMul@11`](#matmul@11) | 83 | 0 | 53 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MaxRoiPool@11`](#maxroipool@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`MaxUnpool@11`](#maxunpool@11) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`Mod@11`](#mod@11) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`Multinomial@11`](#multinomial@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`NonMaxSuppression@11`](#nonmaxsuppression@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: max_output_boxes_per_class, iou_threshold, score_threshold |
| [`OneHot@11`](#onehot@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Pad@11`](#pad@11) | 116 | 0 | 116 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: constant_value |
| [`QLinearConv@11`](#qlinearconv@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B |
| [`QLinearMatMul@11`](#qlinearmatmul@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`RNN@11`](#rnn@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h |
| [`Range@11`](#range@11) | 32 | 0 | 31 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Reshape@11`](#reshape@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Resize@11`](#resize@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: sizes |
| [`RoiAlign@11`](#roialign@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Scan@11`](#scan@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Scatter@11`](#scatter@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ScatterElements@11`](#scatterelements@11) | 128 | 0 | 110 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`ScatterND@11`](#scatternd@11) | 62 | 0 | 62 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SequenceAt@11`](#sequenceat@11) | 24 | 0 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SequenceConstruct@11`](#sequenceconstruct@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SequenceEmpty@11`](#sequenceempty@11) | 4 | 0 | 4 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SequenceErase@11`](#sequenceerase@11) | 25 | 0 | 25 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: position |
| [`SequenceInsert@11`](#sequenceinsert@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: position |
| [`SequenceLength@11`](#sequencelength@11) | 1 | 0 | 1 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Shape@11`](#shape@11) | 128 | 0 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Slice@11`](#slice@11) | 97 | 0 | 97 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: axes, steps |
| [`Softmax@11`](#softmax@11) | 108 | 0 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`SplitToSequence@11`](#splittosequence@11) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`StringNormalizer@11`](#stringnormalizer@11) | 24 | 0 | 24 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`TfIdfVectorizer@11`](#tfidfvectorizer@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Tile@11`](#tile@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Unsqueeze@11`](#unsqueeze@11) | 128 | 0 | 14 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Upsample@11`](#upsample@11) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 11) |

## `IsInf@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 128 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=128, `onnx-tool-fails-valid-model`=128

### Disagreements
#### `onnx-tool-error` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random {'detect_negative': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'detect_negative': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'detect_negative': 1, 'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/random {'detect_negative': 1, 'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse {'detect_negative': 0, 'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating {'detect_negative': 0, 'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating {'detect_negative': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/random {'detect_negative': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/sparse {'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/alternating {'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'detect_negative': 1, 'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'detect_negative': 1, 'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/random {'detect_negative': 0, 'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/sparse {'detect_negative': 0, 'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/sparse {'detect_negative': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| ... | _+108 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random {'detect_negative': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'detect_negative': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'detect_negative': 1, 'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/random {'detect_negative': 1, 'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse {'detect_negative': 0, 'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating {'detect_negative': 0, 'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating {'detect_negative': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/random {'detect_negative': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/sparse {'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/alternating {'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'detect_negative': 1, 'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'detect_negative': 1, 'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/random {'detect_negative': 0, 'detect_positive': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/sparse {'detect_negative': 0, 'detect_positive': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/sparse {'detect_negative': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsInf-IsInf_0 has no value_infer |
| ... | _+108 more cases_ | | | |

## `Shrink@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 128 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=128, `onnx-tool-fails-valid-model`=128

### Disagreements
#### `onnx-tool-error` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random {'lambd': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/random {'lambd': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/int16/random {'lambd': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/random {'bias': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/int64/random {'bias': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/int8/random {'bias': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint16/random {'lambd': 0.0, 'bias': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint32/random {'lambd': 0.0, 'bias': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint64/random {'lambd': 0.0, 'bias': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint8/random {'lambd': 0.5, 'bias': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating {'lambd': 0.5, 'bias': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse {'lambd': 0.5, 'bias': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random {'lambd': 1.0, 'bias': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random {'lambd': 1.0, 'bias': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random {'lambd': 1.0, 'bias': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating {'lambd': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/sparse {'lambd': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/alternating {'lambd': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| ... | _+108 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random {'lambd': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/random {'lambd': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/int16/random {'lambd': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/random {'bias': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/int64/random {'bias': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/int8/random {'bias': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint16/random {'lambd': 0.0, 'bias': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint32/random {'lambd': 0.0, 'bias': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint64/random {'lambd': 0.0, 'bias': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint8/random {'lambd': 0.5, 'bias': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating {'lambd': 0.5, 'bias': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse {'lambd': 0.5, 'bias': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random {'lambd': 1.0, 'bias': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random {'lambd': 1.0, 'bias': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random {'lambd': 1.0, 'bias': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating {'lambd': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/sparse {'lambd': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/alternating {'lambd': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Shrink-Shrink_0 has no value_infer |
| ... | _+108 more cases_ | | | |

## `Size@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 128 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=128, `onnx-tool-fails-valid-model`=128

### Disagreements
#### `onnx-tool-error` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/bool/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/bool/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=scalar/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| ... | _+108 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/bool/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/bool/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=scalar/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Size-Size_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Size-Size_0 has no value_infer |
| ... | _+108 more cases_ | | | |

## `Compress@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 127 with disagreements, 1 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=127, `onnx-tool-fails-valid-model`=127

### Disagreements
#### `onnx-tool-error` (127 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_true  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/float16/random condition(input)=BCHW/bool/all_true {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/float32/random condition(input)=BCHW/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/float64/random condition(input)=BCHW/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/int16/random condition(input)=BCHW/bool/all_true  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/int32/random condition(input)=BCHW/bool/all_true {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/int64/random condition(input)=BCHW/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/int8/random condition(input)=BCHW/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/uint16/random condition(input)=BCHW/bool/all_true  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/uint32/random condition(input)=BCHW/bool/all_true {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/uint64/random condition(input)=BCHW/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/uint8/random condition(input)=BCHW/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_false  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=BCHW/bool/alternating {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=BCHW/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=B-1-H-1/bool/random condition(input)=B-1-H-1/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=B-C-1-1/bool/random condition(input)=B-C-1-1/bool/all_true  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=B-C-1-1/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=B-1-H-1/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=scalar/bool/all_false  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| ... | _+107 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (127 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_true  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/float16/random condition(input)=BCHW/bool/all_true {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/float32/random condition(input)=BCHW/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/float64/random condition(input)=BCHW/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/int16/random condition(input)=BCHW/bool/all_true  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/int32/random condition(input)=BCHW/bool/all_true {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/int64/random condition(input)=BCHW/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/int8/random condition(input)=BCHW/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/uint16/random condition(input)=BCHW/bool/all_true  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/uint32/random condition(input)=BCHW/bool/all_true {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/uint64/random condition(input)=BCHW/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/uint8/random condition(input)=BCHW/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=BCHW/bool/all_false  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/alternating condition(input)=BCHW/bool/alternating {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/sparse condition(input)=BCHW/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=B-1-H-1/bool/random condition(input)=B-1-H-1/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=B-C-1-1/bool/random condition(input)=B-C-1-1/bool/all_true  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=B-C-1-1/bool/all_true {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=B-1-H-1/bool/all_true {'axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| _case:_ `input(input)=BCHW/bool/random condition(input)=scalar/bool/all_false  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: condition must be a 1-d array |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: condition must be a 1-d array |
| ... | _+107 more cases_ | | | |

## `LpPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 101 with disagreements, 27 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=101, `onnx-tool-fails-valid-model`=101

### Disagreements
#### `onnx-tool-error` (101 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'kernel_shape': [2, 2]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'strides': [2, 2]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [1, 1], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0], 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER', 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'pads': [0, 0, 0, 0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'strides': [2, 2], 'pads': [0, 0, 0, 0], 'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'SAME_UPPER', 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| ... | _+81 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (101 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'kernel_shape': [2, 2]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `33640B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'strides': [2, 2]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4500B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [1, 1], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0], 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER', 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'kernel_shape': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'pads': [0, 0, 0, 0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4500B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'kernel_shape': [1, 1], 'strides': [2, 2], 'pads': [0, 0, 0, 0], 'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4500B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'SAME_UPPER', 'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node LpPool-LpPool_0 has no value_infer |
| ... | _+81 more cases_ | | | |

## `BitShift@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 93 with disagreements, 35 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=93, `onnx-tool-fails-valid-model`=93

### Disagreements
#### `onnx-tool-error` (93 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/uint32/random Y(input)=BCHW/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/random Y(input)=BCHW/uint64/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint8/random Y(input)=BCHW/uint8/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/random Y(input)=BCHW/uint32/sparse {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/random Y(input)=B-C-1-1/uint32/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/random Y(input)=B-1-H-1/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/random Y(input)=scalar/uint32/sparse {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/sparse Y(input)=BCHW/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/sparse Y(input)=B-C-1-1/uint32/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/sparse Y(input)=B-1-H-1/uint32/sparse {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/sparse Y(input)=scalar/uint32/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/alternating Y(input)=BCHW/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/alternating Y(input)=B-C-1-1/uint32/sparse {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/alternating Y(input)=B-1-H-1/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/alternating Y(input)=scalar/uint32/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/random Y(input)=B-C-1-1/uint64/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/random Y(input)=B-1-H-1/uint64/sparse {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/random Y(input)=scalar/uint64/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/sparse Y(input)=BCHW/uint64/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/sparse Y(input)=B-C-1-1/uint64/alternating {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| ... | _+73 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (93 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/uint32/random Y(input)=BCHW/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/random Y(input)=BCHW/uint64/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint8/random Y(input)=BCHW/uint8/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/random Y(input)=BCHW/uint32/sparse {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/random Y(input)=B-C-1-1/uint32/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/random Y(input)=B-1-H-1/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/random Y(input)=scalar/uint32/sparse {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/sparse Y(input)=BCHW/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/sparse Y(input)=B-C-1-1/uint32/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/sparse Y(input)=B-1-H-1/uint32/sparse {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/sparse Y(input)=scalar/uint32/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/alternating Y(input)=BCHW/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/alternating Y(input)=B-C-1-1/uint32/sparse {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/alternating Y(input)=B-1-H-1/uint32/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint32/alternating Y(input)=scalar/uint32/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/random Y(input)=B-C-1-1/uint64/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/random Y(input)=B-1-H-1/uint64/sparse {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/random Y(input)=scalar/uint64/random {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/sparse Y(input)=BCHW/uint64/random {'direction': b'LEFT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| _case:_ `X(input)=BCHW/uint64/sparse Y(input)=B-C-1-1/uint64/alternating {'direction': b'RIGHT'} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node BitShift-BitShift_0 has no value_infer |
| ... | _+73 more cases_ | | | |

## `Selu@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 92 with disagreements, 36 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=92, `onnx-tool-fails-valid-model`=92

### Disagreements
#### `onnx-tool-error` (92 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0, 'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'alpha': 0.0, 'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 0.0, 'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'alpha': 0.5, 'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'alpha': 1.0, 'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'alpha': 1.0, 'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'alpha': 1.0, 'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse {'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'alpha': 0.0, 'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'alpha': 0.0, 'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5, 'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| ... | _+72 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (92 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0, 'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'alpha': 0.0, 'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 0.0, 'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'alpha': 0.5, 'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'alpha': 1.0, 'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'alpha': 1.0, 'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'alpha': 1.0, 'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse {'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'alpha': 0.0, 'gamma': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'alpha': 0.0, 'gamma': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5, 'gamma': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Selu-Selu_0 has no value_infer |
| ... | _+72 more cases_ | | | |

## `ThresholdedRelu@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 89 with disagreements, 39 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=89, `onnx-tool-fails-valid-model`=89

### Disagreements
#### `onnx-tool-error` (89 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| ... | _+69 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (89 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer |
| ... | _+69 more cases_ | | | |

## `RandomNormal@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 85 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=85, `onnx-tool-fails-valid-model`=85

### Disagreements
#### `onnx-tool-error` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'seed': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'seed': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'seed': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'mean': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'mean': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'mean': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'dtype': 1, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'dtype': 11, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.0, 'dtype': 1, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.0, 'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.5, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 1.0, 'dtype': 1, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 1.0, 'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'mean': 0.0, 'scale': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| ... | _+65 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'seed': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'seed': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'seed': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'mean': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'mean': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'mean': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'dtype': 1, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'dtype': 11, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.0, 'dtype': 1, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.0, 'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 0.5, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 1.0, 'dtype': 1, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'scale': 1.0, 'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| _case:_ ` {'mean': 0.0, 'scale': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomNormal-RandomNormal_0 has no value_infer |
| ... | _+65 more cases_ | | | |

## `RandomUniform@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 85 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=85, `onnx-tool-fails-valid-model`=85

### Disagreements
#### `onnx-tool-error` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'low': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'low': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'low': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'high': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'high': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'high': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'dtype': 1, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'dtype': 11, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.0, 'dtype': 1, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.0, 'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.5, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 1.0, 'dtype': 1, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 1.0, 'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'high': 0.0, 'seed': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| ... | _+65 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'low': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'low': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'low': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'high': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'high': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'high': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.5, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 1.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'dtype': 1, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'dtype': 11, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.0, 'dtype': 1, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.0, 'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 0.5, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 1.0, 'dtype': 1, 'shape': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'seed': 1.0, 'dtype': 11, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| _case:_ ` {'high': 0.0, 'seed': 0.0, 'shape': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node RandomUniform-RandomUniform_0 has no value_infer |
| ... | _+65 more cases_ | | | |

## `ReduceL1@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 85 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=85, `onnx-tool-fails-valid-model`=85

### Disagreements
#### `onnx-tool-error` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| ... | _+65 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `80B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| ... | _+65 more cases_ | | | |

## `ReduceLogSum@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 85 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=85, `onnx-tool-fails-valid-model`=85

### Disagreements
#### `onnx-tool-error` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| ... | _+65 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `80B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| ... | _+65 more cases_ | | | |

## `ReduceLogSumExp@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 85 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=85, `onnx-tool-fails-valid-model`=85

### Disagreements
#### `onnx-tool-error` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| ... | _+65 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `80B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| ... | _+65 more cases_ | | | |

## `ReduceSumSquare@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 85 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=85, `onnx-tool-fails-valid-model`=85

### Disagreements
#### `onnx-tool-error` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| ... | _+65 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (85 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `80B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| ... | _+65 more cases_ | | | |

## `GlobalLpPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 72 with disagreements, 56 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=72, `onnx-tool-fails-valid-model`=72

### Disagreements
#### `onnx-tool-error` (72 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| ... | _+52 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (72 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'p': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 2} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'p': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer |
| ... | _+52 more cases_ | | | |

## `MeanVarianceNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 72 with disagreements, 56 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=72, `onnx-tool-fails-valid-model`=72

### Disagreements
#### `onnx-tool-error` (72 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| ... | _+52 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (72 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer |
| ... | _+52 more cases_ | | | |

## `ArgMin@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 63 with disagreements, 65 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=63, `onnx-tool-fails-valid-model`=63

### Disagreements
#### `onnx-tool-error` (63 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/random {'axis': 0, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random {'axis': -1, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axis': -1, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axis': 0, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axis': 0, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axis': -1, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axis': -1, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/sparse {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| ... | _+43 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (63 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/random {'axis': 0, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random {'axis': -1, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'axis': -1, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `240B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axis': 0, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axis': 0, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axis': -1, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axis': -1, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/sparse {'axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| ... | _+43 more cases_ | | | |

## `BatchNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 62 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=248

### Disagreements
#### `wrong-shape` (62 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/alternating scale(input)=1d-10/float16/alternating B(input)=1d-10/float16/alternating mean(input)=1d-10/float16/alternating var(input)=1d-10/float16/alternating {'epsilon': 1.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=B-1-H-1/float16/random scale(input)=1d-1/float16/random B(input)=1d-1/float16/random mean(input)=1d-1/float16/random var(input)=1d-1/float16/random {'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(1)` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1,) claim=(1, 1, 30, 1) |
| `saved_mean` | `wrong-shape` | `(1)` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1,) claim=(1, 1, 30, 1) |
| `saved_var` | `wrong-shape` | `(1)` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1,) claim=(1, 1, 30, 1) |
| `var_out` | `wrong-shape` | `(1)` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1,) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=BCHW/float32/sparse scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.0, 'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float64/random scale(input)=1d-10/float64/sparse B(input)=1d-10/float64/random mean(input)=1d-10/float64/random var(input)=1d-10/float64/random {'epsilon': 0.5, 'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=B-C-1-1/float16/sparse scale(input)=1d-10/float16/sparse B(input)=1d-10/float16/sparse mean(input)=1d-10/float16/sparse var(input)=1d-10/float16/sparse {'epsilon': 1.0, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,1,1)` / `float16` / `20B` | truth=(10,) claim=(1, 10, 1, 1) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,1,1)` / `float16` / `20B` | truth=(10,) claim=(1, 10, 1, 1) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,1,1)` / `float16` / `20B` | truth=(10,) claim=(1, 10, 1, 1) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,1,1)` / `float16` / `20B` | truth=(10,) claim=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float32/alternating scale(input)=1d-10/float32/sparse B(input)=1d-10/float32/sparse mean(input)=1d-10/float32/sparse var(input)=1d-10/float32/sparse {'epsilon': 1.0, 'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | truth=(10,) claim=(1, 10, 1, 1) |
| `saved_mean` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | truth=(10,) claim=(1, 10, 1, 1) |
| `saved_var` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | truth=(10,) claim=(1, 10, 1, 1) |
| `var_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | truth=(10,) claim=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float64/sparse scale(input)=1d-10/float64/alternating B(input)=1d-10/float64/sparse mean(input)=1d-10/float64/alternating var(input)=1d-10/float64/sparse {'epsilon': 0.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | truth=(10,) claim=(1, 10, 1, 1) |
| `saved_mean` | `wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | truth=(10,) claim=(1, 10, 1, 1) |
| `saved_var` | `wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | truth=(10,) claim=(1, 10, 1, 1) |
| `var_out` | `wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | truth=(10,) claim=(1, 10, 1, 1) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'epsilon': 0.0, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'epsilon': 1.0, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'epsilon': 1.0, 'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'epsilon': 1.0, 'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random  outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.0, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.0, 'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.0, 'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_mean` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `saved_var` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| `var_out` | `wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(10,) claim=(1, 10, 30, 30) |
| ... | _+42 more cases_ | | | |

## `MaxPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 62 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=64

### Disagreements
#### `wrong-shape` (62 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random {'kernel_shape': [2, 2]} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,29,29)` / `int64` / `67280B` | `()` / `int64` / `0B` | truth=(1, 10, 29, 29) claim=() |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1]} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0]} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=BCHW/float64/alternating {'kernel_shape': [1, 1], 'ceil_mode': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'kernel_shape': [1, 1], 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,1,1)` / `int64` / `80B` | `()` / `int64` / `0B` | truth=(1, 10, 1, 1) claim=() |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0], 'ceil_mode': 1, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,1,1)` / `int64` / `80B` | `()` / `int64` / `0B` | truth=(1, 10, 1, 1) claim=() |
| _case:_ `X(input)=B-1-H-1/float64/random {'kernel_shape': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET'} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=B-1-H-1/float64/alternating {'kernel_shape': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'ceil_mode': 1, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'dilations': [1, 1], 'ceil_mode': 1, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'ceil_mode': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'pads': [0, 0, 0, 0], 'ceil_mode': 0, 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,15,15)` / `int64` / `18000B` | `()` / `int64` / `0B` | truth=(1, 10, 15, 15) claim=() |
| _case:_ `X(input)=B-1-H-1/float16/sparse {'kernel_shape': [1, 1], 'strides': [2, 2], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'ceil_mode': 1} outputs=10` | | | | |
| `Y` | `wrong-shape` | `(1,1,15,1)` / `float16` / `30B` | `(1,1,16,1)` / `float16` / `32B` | truth=(1, 1, 15, 1) claim=(1, 1, 16, 1) |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'ceil_mode': 0, 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,15,1)` / `int64` / `120B` | `()` / `int64` / `0B` | truth=(1, 1, 15, 1) claim=() |
| _case:_ `X(input)=BCHW/float32/random {'kernel_shape': [2, 2], 'dilations': [1, 1], 'auto_pad': b'SAME_UPPER', 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [2, 2], 'strides': [1, 1], 'pads': [0, 0, 0, 0]} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,29,29)` / `int64` / `67280B` | `()` / `int64` / `0B` | truth=(1, 10, 29, 29) claim=() |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'kernel_shape': [2, 2], 'strides': [1, 1], 'dilations': [1, 1], 'pads': [1, 1, 1, 1], 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,2,2)` / `int64` / `320B` | `()` / `int64` / `0B` | truth=(1, 10, 2, 2) claim=() |
| _case:_ `X(input)=B-C-1-1/float64/alternating {'kernel_shape': [2, 2], 'strides': [2, 2], 'pads': [1, 1, 1, 1], 'ceil_mode': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,1,1)` / `int64` / `80B` | `()` / `int64` / `0B` | truth=(1, 10, 1, 1) claim=() |
| `Y` | `wrong-shape` | `(1,10,1,1)` / `float64` / `80B` | `(1,10,2,2)` / `float64` / `320B` | truth=(1, 10, 1, 1) claim=(1, 10, 2, 2) |
| _case:_ `X(input)=BCHW/float32/random {'kernel_shape': [3, 3], 'auto_pad': b'SAME_UPPER', 'pads': [1, 1, 1, 1], 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [3, 3], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'ceil_mode': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,28,28)` / `int64` / `62720B` | `()` / `int64` / `0B` | truth=(1, 10, 28, 28) claim=() |
| _case:_ `X(input)=BCHW/float64/alternating {'kernel_shape': [3, 3], 'dilations': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'ceil_mode': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| ... | _+42 more cases_ | | | |

## `Unique@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 45 with disagreements, 83 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=45, `onnx-tool-fails-valid-model`=45

### Disagreements
#### `onnx-tool-error` (45 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random {'sorted': 1} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'sorted': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random {'axis': 0} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int64/random {'sorted': 1, 'axis': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int8/random {'sorted': 1, 'axis': 1} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'axis': -1} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'sorted': 1, 'axis': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'sorted': 1, 'axis': 1} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'sorted': 1, 'axis': -1} outputs=1000` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse {'sorted': 0, 'axis': 0} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating {'sorted': 0, 'axis': 1} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int64/sparse {'axis': 0} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int64/alternating {'axis': 1} outputs=1000` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int8/sparse {'axis': -1} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int8/alternating {'sorted': 1, 'axis': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'axis': -1} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'sorted': 1, 'axis': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'sorted': 1, 'axis': 1} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'sorted': 1, 'axis': -1} outputs=1000` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'sorted': 0, 'axis': 0} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| ... | _+25 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (45 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random {'sorted': 1} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `163800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'sorted': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `108000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random {'axis': 0} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72016B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int64/random {'sorted': 1, 'axis': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int8/random {'sorted': 1, 'axis': 1} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9160B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse {'axis': -1} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18720B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating {'sorted': 1, 'axis': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'sorted': 1, 'axis': 1} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36160B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'sorted': 1, 'axis': -1} outputs=1000` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2400B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse {'sorted': 0, 'axis': 0} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72024B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating {'sorted': 0, 'axis': 1} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7208B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int64/sparse {'axis': 0} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72016B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int64/alternating {'axis': 1} outputs=1000` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int8/sparse {'axis': -1} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9720B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=BCHW/int8/alternating {'sorted': 1, 'axis': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random {'axis': -1} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `44B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse {'sorted': 1, 'axis': 0} outputs=1100` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `28B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating {'sorted': 1, 'axis': 1} outputs=1110` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `100B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random {'sorted': 1, 'axis': -1} outputs=1000` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'sorted': 0, 'axis': 0} outputs=1111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `64B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Unique-Unique_0 has no value_infer |
| ... | _+25 more cases_ | | | |

## `IsNaN@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 36 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=36, `onnx-tool-fails-valid-model`=36

### Disagreements
#### `onnx-tool-error` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| ... | _+16 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=BCHW/float64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer |
| ... | _+16 more cases_ | | | |

## `ReverseSequence@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 36 with disagreements, 92 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=36, `onnx-tool-fails-valid-model`=36

### Disagreements
#### `onnx-tool-error` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float64/random sequence_lens(init)=1d-1/int64/random {'time_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint8/random sequence_lens(init)=1d-1/int64/random {'time_axis': 1, 'batch_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-1/int64/sparse {'time_axis': -1, 'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-10/int64/sparse {'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-10/int64/alternating {'time_axis': 0, 'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/random sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse sequence_lens(init)=1d-1/int64/sparse {'time_axis': -1, 'batch_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse sequence_lens(init)=1d-10/int64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating sequence_lens(init)=1d-10/int64/alternating {'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random sequence_lens(init)=1d-10/int64/sparse {'time_axis': 0, 'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating sequence_lens(init)=1d-1/int64/random {'time_axis': 1, 'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': -1, 'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/random sequence_lens(init)=1d-10/int64/alternating {'time_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/sparse sequence_lens(init)=1d-1/int64/alternating {'time_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/sparse sequence_lens(init)=1d-10/int64/sparse {'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/int16/sparse sequence_lens(init)=1d-1/int64/sparse {'time_axis': 1, 'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/random sequence_lens(init)=1d-1/int64/sparse {'time_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/sparse sequence_lens(init)=1d-10/int64/alternating {'time_axis': 0, 'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| ... | _+16 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float64/random sequence_lens(init)=1d-1/int64/random {'time_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint8/random sequence_lens(init)=1d-1/int64/random {'time_axis': 1, 'batch_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-1/int64/sparse {'time_axis': -1, 'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-10/int64/sparse {'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse sequence_lens(init)=1d-10/int64/alternating {'time_axis': 0, 'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/random sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse sequence_lens(init)=1d-1/int64/sparse {'time_axis': -1, 'batch_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse sequence_lens(init)=1d-10/int64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating sequence_lens(init)=1d-10/int64/alternating {'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random sequence_lens(init)=1d-10/int64/sparse {'time_axis': 0, 'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating sequence_lens(init)=1d-1/int64/random {'time_axis': 1, 'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': -1, 'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/random sequence_lens(init)=1d-10/int64/alternating {'time_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/sparse sequence_lens(init)=1d-1/int64/alternating {'time_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/sparse sequence_lens(init)=1d-10/int64/sparse {'batch_axis': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/int16/sparse sequence_lens(init)=1d-1/int64/sparse {'time_axis': 1, 'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/random sequence_lens(init)=1d-1/int64/sparse {'time_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/sparse sequence_lens(init)=1d-10/int64/alternating {'time_axis': 0, 'batch_axis': -1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36080B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/alternating sequence_lens(init)=1d-1/int64/alternating {'time_axis': 1, 'batch_axis': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer |
| ... | _+16 more cases_ | | | |

## `Round@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 36 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `wrong-dtype`=36

### Disagreements
#### `wrong-dtype` (36 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float16` / `18000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float16 claim=bool |
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float32` / `36000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float32 claim=bool |
| _case:_ `X(input)=BCHW/float64/random  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float64` / `72000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float64 claim=bool |
| _case:_ `X(input)=BCHW/float16/alternating  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float16` / `18000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float16 claim=bool |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float16` / `18000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,1,30,1)` / `float16` / `60B` | `(1,1,30,1)` / `bool` / `30B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float16` / `20B` | `(1,10,1,1)` / `bool` / `10B` | truth=float16 claim=bool |
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `()` / `float16` / `2B` | `()` / `bool` / `0B` | truth=float16 claim=bool |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float32` / `36000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float32 claim=bool |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float32` / `36000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float32 claim=bool |
| _case:_ `X(input)=BCHW/float64/sparse  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float64` / `72000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float64 claim=bool |
| _case:_ `X(input)=BCHW/float64/alternating  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,30,30)` / `float64` / `72000B` | `(1,10,30,30)` / `bool` / `9000B` | truth=float64 claim=bool |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float16` / `20B` | `(1,10,1,1)` / `bool` / `10B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float16` / `20B` | `(1,10,1,1)` / `bool` / `10B` | truth=float16 claim=bool |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float32` / `40B` | `(1,10,1,1)` / `bool` / `10B` | truth=float32 claim=bool |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float32` / `40B` | `(1,10,1,1)` / `bool` / `10B` | truth=float32 claim=bool |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float32` / `40B` | `(1,10,1,1)` / `bool` / `10B` | truth=float32 claim=bool |
| _case:_ `X(input)=B-C-1-1/float64/random  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float64` / `80B` | `(1,10,1,1)` / `bool` / `10B` | truth=float64 claim=bool |
| _case:_ `X(input)=B-C-1-1/float64/sparse  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float64` / `80B` | `(1,10,1,1)` / `bool` / `10B` | truth=float64 claim=bool |
| _case:_ `X(input)=B-C-1-1/float64/alternating  outputs=1` | | | | |
| `Y` | `wrong-dtype` | `(1,10,1,1)` / `float64` / `80B` | `(1,10,1,1)` / `bool` / `10B` | truth=float64 claim=bool |
| ... | _+16 more cases_ | | | |

## `ReduceMax@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 32 with disagreements, 30 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=18, `wrong-shape`=14

### Disagreements
#### `scalar-volume` (18 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random {'axes': [2, 3], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float32/random {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/sparse {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/alternating {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float64/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float64/sparse {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float64/alternating {'axes': [2, 3], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int32/sparse {'axes': [0]} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int32/alternating {'axes': [1]} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int64/random {'axes': [2, 3]} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int64/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int64/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [1]} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,30,30)` / `int64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,1,1)` / `float32` / `40B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |

## `ReduceMin@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 32 with disagreements, 30 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=18, `wrong-shape`=14

### Disagreements
#### `scalar-volume` (18 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random {'axes': [2, 3], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float32/random {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/sparse {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/alternating {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float64/random {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float64/sparse {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float64/alternating {'axes': [2, 3], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int32/sparse {'axes': [0]} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int32/alternating {'axes': [1]} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int64/random {'axes': [2, 3]} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int64/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int64/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [1]} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,30,30)` / `int64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,1,1)` / `float32` / `40B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |

## `ReduceL2@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 31 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `wrong-dtype`=26, `scalar-volume`=5

### Disagreements
#### `scalar-volume` (5 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=B-C-1-1/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float16/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

#### `wrong-dtype` (26 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/int32/random {'axes': [2, 3]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10,1,1)` / `int32` / `40B` | `(1,10,1,1)` / `float64` / `80B` | truth=int32 claim=float64 |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int64` / `8B` | `(1,1,1,1)` / `float64` / `8B` | truth=int64 claim=float64 |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,1,1)` / `float64` / `8B` | truth=int32 claim=float64 |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `()` / `int32` / `4B` | `()` / `float64` / `0B` | truth=int32 claim=float64 |
| _case:_ `data(input)=BCHW/int64/sparse {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10,30,30)` / `int64` / `72000B` | `(1,10,30,30)` / `float64` / `72000B` | truth=int64 claim=float64 |
| _case:_ `data(input)=BCHW/int64/alternating {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(10,30,30)` / `int64` / `72000B` | `(10,30,30)` / `float64` / `72000B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int32/random {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,1,1)` / `float64` / `8B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int32/sparse {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1)` / `int32` / `4B` | `(1,1,1)` / `float64` / `8B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int32/alternating {'axes': [2, 3], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10,1,1)` / `int32` / `40B` | `(1,10,1,1)` / `float64` / `80B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int64/random {'axes': [2, 3], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10)` / `int64` / `80B` | `(1,10)` / `float64` / `80B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int64` / `8B` | `(1,1,1,1)` / `float64` / `8B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int64/alternating {'axes': [0]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10,1,1)` / `int64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,1,1)` / `float64` / `8B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `()` / `int32` / `4B` | `()` / `float64` / `0B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int32/alternating {'axes': [0], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,30,1)` / `int32` / `120B` | `(1,1,30,1)` / `float64` / `240B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int64/random {'axes': [0], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,30,1)` / `int64` / `240B` | `(1,30,1)` / `float64` / `240B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int64/sparse {'axes': [1], 'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,30,1)` / `int64` / `240B` | `(1,1,30,1)` / `float64` / `240B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int64/alternating {'axes': [1], 'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,30,1)` / `int64` / `240B` | `(1,30,1)` / `float64` / `240B` | truth=int64 claim=float64 |
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `()` / `int32` / `4B` | `()` / `float64` / `0B` | truth=int32 claim=float64 |
| _case:_ `data(input)=scalar/int64/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `()` / `int64` / `8B` | `()` / `float64` / `0B` | truth=int64 claim=float64 |
| ... | _+6 more cases_ | | | |

## `Abs@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 29 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=29

### Disagreements
#### `scalar-volume` (29 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/int16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/int16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/int16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/int32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/int64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/int64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/int8/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `X(input)=scalar/int8/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| ... | _+9 more cases_ | | | |

## `Sign@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 29 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=29

### Disagreements
#### `scalar-volume` (29 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float64/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/int16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/int16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/int16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/int32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/int32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/int32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/int64/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/int64/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/int64/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/int8/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/int8/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| ... | _+9 more cases_ | | | |

## `Flatten@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 27 with disagreements, 15 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=27

### Disagreements
#### `wrong-shape` (27 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float64/random {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(300,30)` / `float64` / `72000B` | `(1,9000)` / `float64` / `72000B` | truth=(300, 30) claim=(1, 9000) |
| _case:_ `input(input)=BCHW/int8/random {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(300,30)` / `int8` / `9000B` | `(1,9000)` / `int8` / `9000B` | truth=(300, 30) claim=(1, 9000) |
| _case:_ `input(input)=BCHW/uint8/random {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(300,30)` / `uint8` / `9000B` | `(1,9000)` / `uint8` / `9000B` | truth=(300, 30) claim=(1, 9000) |
| _case:_ `input(input)=B-C-1-1/bool/random {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `bool` / `10B` | `(1,10)` / `bool` / `10B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=BCHW/float32/sparse {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(300,30)` / `float32` / `36000B` | `(1,9000)` / `float32` / `36000B` | truth=(300, 30) claim=(1, 9000) |
| _case:_ `input(input)=BCHW/int16/sparse {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(300,30)` / `int16` / `18000B` | `(1,9000)` / `int16` / `18000B` | truth=(300, 30) claim=(1, 9000) |
| _case:_ `input(input)=BCHW/int64/sparse {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(300,30)` / `int64` / `72000B` | `(1,9000)` / `int64` / `72000B` | truth=(300, 30) claim=(1, 9000) |
| _case:_ `input(input)=BCHW/uint16/sparse {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(300,30)` / `uint16` / `18000B` | `(1,9000)` / `uint16` / `18000B` | truth=(300, 30) claim=(1, 9000) |
| _case:_ `input(input)=BCHW/uint64/sparse {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(300,30)` / `uint64` / `72000B` | `(1,9000)` / `uint64` / `72000B` | truth=(300, 30) claim=(1, 9000) |
| _case:_ `input(input)=B-C-1-1/bool/sparse {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `bool` / `10B` | `(1,10)` / `bool` / `10B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/float16/alternating {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `float16` / `20B` | `(1,10)` / `float16` / `20B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/float64/random {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `float64` / `80B` | `(1,10)` / `float64` / `80B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/int16/sparse {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `int16` / `20B` | `(1,10)` / `int16` / `20B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/int32/alternating {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `int32` / `40B` | `(1,10)` / `int32` / `40B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/int8/random {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `int8` / `10B` | `(1,10)` / `int8` / `10B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/uint16/sparse {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `uint16` / `20B` | `(1,10)` / `uint16` / `20B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/uint32/alternating {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `uint32` / `40B` | `(1,10)` / `uint32` / `40B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-C-1-1/uint8/random {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(10,1)` / `uint8` / `10B` | `(1,10)` / `uint8` / `10B` | truth=(10, 1) claim=(1, 10) |
| _case:_ `input(input)=B-1-H-1/bool/alternating {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,1)` / `bool` / `30B` | `(1,30)` / `bool` / `30B` | truth=(30, 1) claim=(1, 30) |
| _case:_ `input(input)=B-1-H-1/float32/random {'axis': -1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,1)` / `float32` / `120B` | `(1,30)` / `float32` / `120B` | truth=(30, 1) claim=(1, 30) |
| ... | _+7 more cases_ | | | |

## `Acos@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acos-Acos_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Acosh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Acosh-Acosh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Asin@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asin-Asin_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Asinh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Asinh-Asinh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Atanh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Atanh-Atanh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Cosh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Cosh-Cosh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Mean@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| _case:_ `data_0(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Mean-Mean_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Sinh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Sinh-Sinh_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Softsign@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Softsign-Softsign_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Tan@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 24 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=24, `onnx-tool-fails-valid-model`=24

### Disagreements
#### `onnx-tool-error` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| ... | _+4 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (24 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Tan-Tan_0 has no value_infer |
| ... | _+4 more cases_ | | | |

## `Squeeze@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 23 with disagreements, 49 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=18, `scalar-volume`=5

### Disagreements
#### `scalar-volume` (5 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/bool/random  outputs=1` | | | | |
| `squeezed` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=scalar/float16/sparse  outputs=1` | | | | |
| `squeezed` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float32/alternating  outputs=1` | | | | |
| `squeezed` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int16/random  outputs=1` | | | | |
| `squeezed` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/int32/sparse  outputs=1` | | | | |
| `squeezed` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |

#### `wrong-shape` (18 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=B-C-1-1/bool/alternating  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `bool` / `10B` | `(10,1,1)` / `bool` / `10B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `float32` / `40B` | `(10,1,1)` / `float32` / `40B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float64/sparse  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `float64` / `80B` | `(10,1,1)` / `float64` / `80B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int16/alternating  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `int16` / `20B` | `(10,1,1)` / `int16` / `20B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/random  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `int64` / `80B` | `(10,1,1)` / `int64` / `80B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int8/sparse  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `int8` / `10B` | `(10,1,1)` / `int8` / `10B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/uint16/alternating  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `uint16` / `20B` | `(10,1,1)` / `uint16` / `20B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/uint64/random  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `uint64` / `80B` | `(10,1,1)` / `uint64` / `80B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/uint8/sparse  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(10)` / `uint8` / `10B` | `(10,1,1)` / `uint8` / `10B` | truth=(10,) claim=(10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `float16` / `60B` | `(1,30,1)` / `float16` / `60B` | truth=(30,) claim=(1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `float32` / `120B` | `(1,30,1)` / `float32` / `120B` | truth=(30,) claim=(1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/alternating  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `float64` / `240B` | `(1,30,1)` / `float64` / `240B` | truth=(30,) claim=(1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/random  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `int32` / `120B` | `(1,30,1)` / `int32` / `120B` | truth=(30,) claim=(1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int64/sparse  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `int64` / `240B` | `(1,30,1)` / `int64` / `240B` | truth=(30,) claim=(1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int8/alternating  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `int8` / `30B` | `(1,30,1)` / `int8` / `30B` | truth=(30,) claim=(1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/uint32/random  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `uint32` / `120B` | `(1,30,1)` / `uint32` / `120B` | truth=(30,) claim=(1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/uint64/sparse  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `uint64` / `240B` | `(1,30,1)` / `uint64` / `240B` | truth=(30,) claim=(1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/uint8/alternating  outputs=1` | | | | |
| `squeezed` | `wrong-shape` | `(30)` / `uint8` / `30B` | `(1,30,1)` / `uint8` / `30B` | truth=(30,) claim=(1, 30, 1) |

## `TopK@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 23 with disagreements, 60 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=23, `onnx-tool-fails-valid-model`=23

### Disagreements
#### `onnx-tool-error` (23 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random K(init)=1d-1/int64/random  outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int32/random K(init)=1d-1/int64/random {'largest': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/random K(init)=1d-1/int64/random {'largest': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float16/alternating K(init)=1d-1/int64/alternating {'largest': 0, 'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float32/alternating K(init)=1d-10/int64/sparse  outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/random K(init)=1d-10/int64/sparse {'largest': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/random K(init)=1d-10/int64/alternating {'largest': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-1/int64/random {'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-1/int64/sparse {'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-1/int64/alternating {'largest': 1, 'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-10/int64/sparse {'largest': 1, 'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-10/int64/alternating {'largest': 0, 'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/alternating K(init)=1d-1/int64/sparse {'largest': 0, 'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int32/alternating K(init)=1d-10/int64/alternating  outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/random K(init)=1d-10/int64/alternating {'largest': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/sparse K(init)=1d-1/int64/random {'largest': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/sparse K(init)=1d-1/int64/sparse {'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/sparse K(init)=1d-10/int64/random {'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/sparse K(init)=1d-10/int64/sparse {'largest': 1, 'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/alternating K(init)=1d-1/int64/random {'largest': 1, 'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| ... | _+3 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (23 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random K(init)=1d-1/int64/random  outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `6008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int32/random K(init)=1d-1/int64/random {'largest': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7208B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/random K(init)=1d-1/int64/random {'largest': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float16/alternating K(init)=1d-1/int64/alternating {'largest': 0, 'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `6008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float32/alternating K(init)=1d-10/int64/sparse  outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7208B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/random K(init)=1d-10/int64/sparse {'largest': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/random K(init)=1d-10/int64/alternating {'largest': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-1/int64/random {'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-1/int64/sparse {'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-1/int64/alternating {'largest': 1, 'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-10/int64/sparse {'largest': 1, 'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/sparse K(init)=1d-10/int64/alternating {'largest': 0, 'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/float64/alternating K(init)=1d-1/int64/sparse {'largest': 0, 'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int32/alternating K(init)=1d-10/int64/alternating  outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7208B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/random K(init)=1d-10/int64/alternating {'largest': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/sparse K(init)=1d-1/int64/random {'largest': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/sparse K(init)=1d-1/int64/sparse {'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/sparse K(init)=1d-10/int64/random {'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/sparse K(init)=1d-10/int64/sparse {'largest': 1, 'sorted': 1} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `X(input)=BCHW/int64/alternating K(init)=1d-1/int64/random {'largest': 1, 'sorted': 0} outputs=11` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9608B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| ... | _+3 more cases_ | | | |

## `Pow@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 22 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=21, `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random Y(input)=scalar/float16/random  outputs=1` | | | | |
| `Z` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (21 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=B-C-1-1/float16/random Y(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/random Y(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/sparse Y(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/alternating Y(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float32/random Y(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float32/sparse Y(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float32/sparse Y(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float32/alternating Y(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float64/random Y(input)=B-1-H-1/float64/sparse  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float64/sparse Y(input)=B-1-H-1/float64/random  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float64/alternating Y(input)=B-1-H-1/float64/random  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float64/alternating Y(input)=B-1-H-1/float64/alternating  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float16/random Y(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float16/sparse Y(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float16/alternating Y(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float32/random Y(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float32/sparse Y(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float32/alternating Y(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float64/random Y(input)=B-C-1-1/float64/random  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float64/random Y(input)=B-C-1-1/float64/alternating  outputs=1` | | | | |
| `Z` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| ... | _+1 more cases_ | | | |

## `Neg@11`
_Auto-generated from ONNX schema (opset 11)_

- 84 cases, 21 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=21

### Disagreements
#### `scalar-volume` (21 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/int16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/int16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/int16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/int32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/int64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/int64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/int8/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `X(input)=scalar/int8/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| ... | _+1 more cases_ | | | |

## `Cast@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 20 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=20

### Disagreements
#### `scalar-volume` (20 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/bool/random {'to': 10} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/bool/sparse {'to': 9} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/bool/alternating {'to': 1} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float16/random {'to': 10} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse {'to': 11} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float16/alternating {'to': 7} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float32/random {'to': 9} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/float32/sparse {'to': 1} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating {'to': 10} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float64/random {'to': 11} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/sparse {'to': 7} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/alternating {'to': 9} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/int16/random {'to': 1} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/int16/sparse {'to': 10} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/int16/alternating {'to': 11} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/int32/random {'to': 7} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/int32/sparse {'to': 9} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/int32/alternating {'to': 1} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/int64/random {'to': 10} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/int64/sparse {'to': 11} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Identity@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 20 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=20

### Disagreements
#### `scalar-volume` (20 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/bool/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/bool/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/bool/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float64/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/int16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/int16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/int16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/int32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/int32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/int32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/int64/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/int64/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |

## `ReduceMean@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 19 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=14, `scalar-volume`=5

### Disagreements
#### `scalar-volume` (5 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int64/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int64/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |

#### `wrong-shape` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,30,30)` / `int64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,1,1)` / `float32` / `40B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |

## `ReduceProd@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 19 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=14, `scalar-volume`=5

### Disagreements
#### `scalar-volume` (5 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int64/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int64/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |

#### `wrong-shape` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,30,30)` / `int64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,1,1)` / `float32` / `40B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |

## `ReduceSum@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 19 with disagreements, 43 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=14, `scalar-volume`=5

### Disagreements
#### `scalar-volume` (5 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int64/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int64/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |

#### `wrong-shape` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,30,30)` / `int64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,10,30,30)` / `int32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,1,1)` / `float32` / `40B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,1,30,1)` / `int32` / `120B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |

## `GlobalMaxPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 18 with disagreements, 18 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=18, `onnx-tool-fails-valid-model`=18

### Disagreements
#### `onnx-tool-error` (18 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (18 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer |

## `Split@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 18 with disagreements, 65 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=18, `onnx-tool-fails-valid-model`=18

### Disagreements
#### `onnx-tool-error` (18 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=BCHW/int16/random {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/bool/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=BCHW/int16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=BCHW/int64/alternating {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/uint64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-C-1-1/bool/alternating {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-C-1-1/float64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-C-1-1/int16/alternating {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-C-1-1/int8/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-C-1-1/uint16/alternating {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-C-1-1/uint8/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-1-H-1/float16/random {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-1-H-1/float64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-1-H-1/int32/random {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-1-H-1/int8/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-1-H-1/uint32/random {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-1-H-1/uint8/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |

#### `onnx-tool-fails-valid-model` (18 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=BCHW/int16/random {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/bool/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=BCHW/int16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=BCHW/int64/alternating {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/uint64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-C-1-1/bool/alternating {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-C-1-1/float64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `80B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-C-1-1/int16/alternating {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-C-1-1/int8/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-C-1-1/uint16/alternating {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-C-1-1/uint8/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-1-H-1/float16/random {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-1-H-1/float64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `240B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-1-H-1/int32/random {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-1-H-1/int8/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=B-1-H-1/uint32/random {'split': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=B-1-H-1/uint8/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |

## `Elu@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 17 with disagreements, 39 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=17

### Disagreements
#### `scalar-volume` (17 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/random {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `LeakyRelu@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 17 with disagreements, 39 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=17

### Disagreements
#### `scalar-volume` (17 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/random {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `Dropout@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 15 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=23

### Disagreements
#### `scalar-volume` (15 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random {'ratio': 1.0} outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/sparse  outputs=10` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/alternating {'ratio': 0.0} outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float32/random {'ratio': 0.5} outputs=10` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/sparse {'ratio': 1.0} outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/alternating  outputs=10` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float64/random {'ratio': 0.0} outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float64/sparse {'ratio': 0.5} outputs=10` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float64/alternating {'ratio': 1.0} outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/float16/random  outputs=10` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random  outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'ratio': 0.0} outputs=10` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'ratio': 0.0} outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'ratio': 0.5} outputs=10` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'ratio': 0.5} outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `HardSigmoid@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 14 with disagreements, 36 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=14

### Disagreements
#### `scalar-volume` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0, 'beta': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse {'alpha': 0.5, 'beta': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating {'alpha': 1.0, 'beta': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random {'alpha': 1.0, 'beta': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse {'alpha': 1.0, 'beta': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'beta': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.0, 'beta': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5, 'beta': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 0.5, 'beta': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random {'alpha': 1.0, 'beta': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `NonZero@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 14 with disagreements, 60 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=14, `onnx-tool-fails-valid-model`=14

### Disagreements
#### `onnx-tool-error` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/bool/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/bool/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |

#### `onnx-tool-fails-valid-model` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/bool/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/bool/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. If the context of this error is of the form `arr[nonzero(cond)]`, just use `arr[cond]`. |
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| _case:_ `X(input)=scalar/int64/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `0B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead. |

## `SpaceToDepth@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 14 with disagreements, 114 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=14, `onnx-tool-fails-valid-model`=14

### Disagreements
#### `onnx-tool-error` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float64/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float64/alternating {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float64/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (14 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/float16/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float16/alternating {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float32/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float64/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `80B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/float64/alternating {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `80B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float16/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/random {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float32/alternating {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/float64/sparse {'blocksize': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `240B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node SpaceToDepth-SpaceToDepth_0 has no value_infer |

## `DequantizeLinear@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: x_zero_point_

- 128 cases, 12 with disagreements, 116 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=22

### Disagreements
#### `scalar-volume` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=scalar/int32/random x_scale(init)=scalar/float32/random x_zero_point(init)=scalar/int32/random  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| `y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/random x_scale(init)=scalar/float32/alternating x_zero_point(init)=scalar/int32/alternating  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/sparse  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/alternating  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/alternating x_scale(init)=scalar/float32/random x_zero_point(init)=scalar/int32/alternating  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int8/random x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int8/sparse  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/int8/alternating x_scale(init)=scalar/float32/alternating  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int8/alternating x_scale(init)=scalar/float32/alternating x_zero_point(init)=scalar/int8/random  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/uint8/random x_scale(init)=scalar/float32/random x_zero_point(init)=scalar/uint8/alternating  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=B-C-1-1/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/sparse  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=B-C-1-1/int32/alternating x_scale(init)=scalar/float32/random  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=B-C-1-1/int32/alternating x_scale(init)=scalar/float32/sparse  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `Det@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 12 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float16/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Det-Det_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Det-Det_0 has no value_infer |

## `DynamicQuantizeLinear@11`
_Auto-generated from ONNX schema (opset 11)_

- 12 cases, 12 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=12, `onnx-tool-fails-valid-model`=12

### Disagreements
#### `onnx-tool-error` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=BCHW/float32/random  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=BCHW/float32/alternating  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=BCHW/float32/sparse  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/random  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/random  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/random  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/sparse  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/alternating  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/sparse  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/alternating  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/sparse  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/alternating  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |

#### `onnx-tool-fails-valid-model` (12 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=BCHW/float32/random  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9005B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=BCHW/float32/alternating  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9005B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=BCHW/float32/sparse  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9005B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/random  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `35B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/random  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `15B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/random  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `6B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/sparse  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `15B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-C-1-1/float32/alternating  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `15B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/sparse  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `35B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=B-1-H-1/float32/alternating  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `35B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/sparse  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `6B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| _case:_ `x(input)=scalar/float32/alternating  outputs=111` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `6B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer |

## `Ceil@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Exp@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float64/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Floor@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Log@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float64/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Max@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=scalar/float16/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/alternating  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float32/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float32/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float32/alternating  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float64/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/float64/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/float64/alternating  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Min@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=scalar/float16/random  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/sparse  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/alternating  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float32/random  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float32/sparse  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float32/alternating  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float64/random  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/float64/sparse  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/float64/alternating  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Reciprocal@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Relu@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Sigmoid@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Sin@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float64/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Sqrt@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float64/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Sum@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data_0(input)=scalar/float16/random  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/sparse  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float16/alternating  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data_0(input)=scalar/float32/random  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float32/sparse  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float32/alternating  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/float64/random  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/float64/sparse  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/float64/alternating  outputs=1` | | | | |
| `sum` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Tanh@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 9 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=9

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float64/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `input(input)=scalar/float64/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Atan@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 6 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=6

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `Clip@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: min, max_

- 102 cases, 6 with disagreements, 95 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=12

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random min(init)=scalar/float16/random max(init)=scalar/float16/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=BCHW/float16/sparse min(init)=scalar/float16/alternating max(init)=scalar/float16/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=BCHW/float32/sparse min(init)=scalar/float32/random max(init)=scalar/float32/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `min` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=BCHW/float32/alternating min(init)=scalar/float32/sparse max(init)=scalar/float32/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `min` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=B-C-1-1/float16/sparse min(init)=scalar/float16/random max(init)=scalar/float16/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=B-C-1-1/float32/random min(init)=scalar/float32/alternating  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `Cos@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 6 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=6

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `Erf@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 6 with disagreements, 104 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=6

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float32/random  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/sparse  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `input(input)=scalar/float32/alternating  outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `PRelu@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 6 with disagreements, 55 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3, `wrong-shape`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random slope(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random slope(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse slope(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=B-C-1-1/float16/random slope(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/sparse slope(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/alternating slope(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |

## `QuantizeLinear@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: y_zero_point_

- 128 cases, 6 with disagreements, 122 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=13

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=scalar/float32/random y_scale(init)=scalar/float32/random y_zero_point(init)=scalar/int8/random  outputs=1` | | | | |
| `y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/random y_scale(init)=scalar/float32/alternating y_zero_point(init)=scalar/int8/sparse  outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/sparse y_scale(init)=scalar/float32/random y_zero_point(init)=scalar/uint8/alternating  outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/alternating y_scale(init)=scalar/float32/random y_zero_point(init)=scalar/int8/sparse  outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/alternating y_scale(init)=scalar/float32/sparse y_zero_point(init)=scalar/int8/sparse  outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/alternating y_scale(init)=scalar/float32/sparse y_zero_point(init)=scalar/uint8/sparse  outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |

## `Softplus@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 6 with disagreements, 12 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=6

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/float32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `Transpose@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 6 with disagreements, 14 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=6

### Disagreements
#### `scalar-volume` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random  outputs=1` | | | | |
| `transposed` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float32/random  outputs=1` | | | | |
| `transposed` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float64/random  outputs=1` | | | | |
| `transposed` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=scalar/int16/random  outputs=1` | | | | |
| `transposed` | `scalar-volume` | `()` / `int16` / `2B` | `()` / `int16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `transposed` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int64/random  outputs=1` | | | | |
| `transposed` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |

## `Add@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 4 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=4

### Disagreements
#### `scalar-volume` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/sparse  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/sparse B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float64/random B(input)=scalar/float64/alternating  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Mul@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 4 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=4

### Disagreements
#### `scalar-volume` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/sparse  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/sparse B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float64/random B(input)=scalar/float64/alternating  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Sub@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 4 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=4

### Disagreements
#### `scalar-volume` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/sparse  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float16/sparse B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `A(input)=scalar/float64/random B(input)=scalar/float64/alternating  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

## `Where@11`
_Auto-generated from ONNX schema (opset 11)_

- 70 cases, 4 with disagreements, 32 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=4

### Disagreements
#### `wrong-shape` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `condition(input)=B-C-1-1/bool/all_true X(input)=B-C-1-1/float32/sparse Y(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| `output` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `condition(input)=B-C-1-1/bool/all_true X(input)=B-1-H-1/uint8/random Y(input)=scalar/uint8/random  outputs=1` | | | | |
| `output` | `wrong-shape` | `(1,10,30,1)` / `uint8` / `300B` | `(1,1,30,1)` / `uint8` / `30B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `condition(input)=B-C-1-1/bool/all_false X(input)=scalar/float32/sparse Y(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| `output` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `condition(input)=B-C-1-1/bool/alternating X(input)=B-1-H-1/float32/sparse Y(input)=B-1-H-1/float32/random  outputs=1` | | | | |
| `output` | `wrong-shape` | `(1,10,30,1)` / `float32` / `1200B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |

## `And@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_true  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_false  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/alternating  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `AveragePool@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 30 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=3

### Disagreements
#### `wrong-shape` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=B-1-H-1/float32/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'ceil_mode': 1} outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,1,15,1)` / `float32` / `60B` | `(1,1,16,1)` / `float32` / `64B` | truth=(1, 1, 15, 1) claim=(1, 1, 16, 1) |
| _case:_ `X(input)=BCHW/float16/random {'kernel_shape': [1, 1], 'count_include_pad': 0, 'strides': [2, 2], 'ceil_mode': 1} outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,15,15)` / `float16` / `4500B` | `(1,10,16,16)` / `float16` / `5120B` | truth=(1, 10, 15, 15) claim=(1, 10, 16, 16) |
| _case:_ `X(input)=BCHW/float16/alternating {'kernel_shape': [1, 1], 'count_include_pad': 0, 'strides': [2, 2], 'ceil_mode': 1} outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,15,15)` / `float16` / `4500B` | `(1,10,16,16)` / `float16` / `5120B` | truth=(1, 10, 15, 15) claim=(1, 10, 16, 16) |

## `Not@11`
_Auto-generated from ONNX schema (opset 11)_

- 12 cases, 3 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/bool/all_true  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `X(input)=scalar/bool/all_false  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `X(input)=scalar/bool/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Or@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_true  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_false  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/alternating  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Xor@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 3 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (3 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_true  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/all_false  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=scalar/bool/all_true B(input)=scalar/bool/alternating  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Conv@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: B_

- 128 cases, 2 with disagreements, 117 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=2

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=B-C-1-1/float16/alternating W(input)=B-C-1-1/float16/random B(init)=scalar/float16/sparse {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0]} outputs=1` | | | | |
| `B` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=B-C-1-1/float32/sparse W(input)=B-C-1-1/float32/sparse B(init)=scalar/float32/sparse {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET', 'strides': [1, 1], 'pads': [1, 1, 1, 1]} outputs=1` | | | | |
| `B` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `ConvInteger@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: x_zero_point, w_zero_point_

- 128 cases, 2 with disagreements, 125 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=4

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `x(input)=BCHW/uint8/sparse w(input)=B-C-1-1/uint8/random x_zero_point(init)=scalar/uint8/sparse w_zero_point(init)=scalar/uint8/random {'group': 1, 'auto_pad': b'SAME_UPPER', 'kernel_shape': [1, 1]} outputs=1` | | | | |
| `w_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| `x_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=B-C-1-1/int8/random w(input)=B-C-1-1/int8/sparse x_zero_point(init)=scalar/int8/alternating w_zero_point(init)=scalar/int8/sparse {'group': 1, 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'kernel_shape': [1, 1], 'strides': [1, 1]} outputs=1` | | | | |
| `w_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| `x_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |

## `MatMulInteger@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: a_zero_point, b_zero_point_

- 128 cases, 2 with disagreements, 123 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=BCHW/uint8/random B(input)=B-1-H-1/uint8/random a_zero_point(init)=scalar/uint8/sparse  outputs=1` | | | | |
| `a_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `A(input)=B-C-1-1/int8/random B(input)=B-C-1-1/int8/sparse a_zero_point(init)=scalar/int8/alternating b_zero_point(init)=scalar/int8/sparse  outputs=1` | | | | |
| `a_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| `b_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |

## `RandomNormalLike@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 2 with disagreements, 118 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=2

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random {'seed': 0.5, 'mean': 0.0, 'dtype': 10} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse {'seed': 0.5, 'mean': 0.0, 'scale': 0.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `RandomUniformLike@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 2 with disagreements, 118 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=2

### Disagreements
#### `scalar-volume` (2 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random {'low': 0.5, 'high': 0.0, 'dtype': 10} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `input(input)=scalar/float16/sparse {'low': 0.5, 'high': 0.0, 'seed': 0.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Constant@11`
_Auto-generated from ONNX schema (opset 11)_

- 2 cases, 1 with disagreements, 1 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `Equal@11`
_Auto-generated from ONNX schema (opset 11)_

- 58 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/random B(input)=scalar/bool/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Greater@11`
_Auto-generated from ONNX schema (opset 11)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Less@11`
_Auto-generated from ONNX schema (opset 11)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `ArgMax@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 65 invalid ignored, 0 build errors

> No disagreements found.

## `Concat@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 20 invalid ignored, 0 build errors

> No disagreements found.

## `ConcatFromSequence@11`
_Auto-generated from ONNX schema (opset 11)_

- 12 cases, 0 with disagreements, 12 invalid ignored, 0 build errors

> No disagreements found.

## `ConstantOfShape@11`
_Auto-generated from ONNX schema (opset 11)_

- 24 cases, 0 with disagreements, 24 invalid ignored, 0 build errors

> No disagreements found.

## `ConvTranspose@11`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `CumSum@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 112 invalid ignored, 0 build errors

> No disagreements found.

## `DepthToSpace@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 118 invalid ignored, 0 build errors

> No disagreements found.

## `Div@11`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `Expand@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 106 invalid ignored, 0 build errors

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

- 128 cases, 0 with disagreements, 73 invalid ignored, 0 build errors

> No disagreements found.

## `GatherElements@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 93 invalid ignored, 0 build errors

> No disagreements found.

## `GatherND@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 106 invalid ignored, 0 build errors

> No disagreements found.

## `Gemm@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: C_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `GlobalAveragePool@11`
_Auto-generated from ONNX schema (opset 11)_

- 36 cases, 0 with disagreements, 18 invalid ignored, 0 build errors

> No disagreements found.

## `Hardmax@11`
_Auto-generated from ONNX schema (opset 11)_

- 108 cases, 0 with disagreements, 36 invalid ignored, 0 build errors

> No disagreements found.

## `If@11`
_Auto-generated from ONNX schema (opset 11)_

- 12 cases, 0 with disagreements, 12 invalid ignored, 0 build errors

> No disagreements found.

## `InstanceNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 35 invalid ignored, 0 build errors

> No disagreements found.

## `LRN@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 109 invalid ignored, 0 build errors

> No disagreements found.

## `LSTM@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: B, sequence_lens, initial_h, initial_c, P_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `LogSoftmax@11`
_Auto-generated from ONNX schema (opset 11)_

- 108 cases, 0 with disagreements, 0 invalid ignored, 0 build errors

> No disagreements found.

## `Loop@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: M, cond_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `LpNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 42 invalid ignored, 0 build errors

> No disagreements found.

## `MatMul@11`
_Auto-generated from ONNX schema (opset 11)_

- 83 cases, 0 with disagreements, 53 invalid ignored, 0 build errors

> No disagreements found.

## `MaxRoiPool@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `MaxUnpool@11`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `Mod@11`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

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

- 116 cases, 0 with disagreements, 116 invalid ignored, 0 build errors

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

- 128 cases, 0 with disagreements, 110 invalid ignored, 0 build errors

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

- 4 cases, 0 with disagreements, 4 invalid ignored, 0 build errors

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

- 108 cases, 0 with disagreements, 0 invalid ignored, 0 build errors

> No disagreements found.

## `SplitToSequence@11`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `StringNormalizer@11`
_Auto-generated from ONNX schema (opset 11)_

- 24 cases, 0 with disagreements, 24 invalid ignored, 0 build errors

> No disagreements found.

## `TfIdfVectorizer@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Tile@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Unsqueeze@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 14 invalid ignored, 0 build errors

> No disagreements found.

## `Upsample@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.
