# onnx_tool audit report
_generated 2026-04-28T18:45:25_

**170 ops, 15870 test cases, 3168 with disagreements, 8459 invalid ignored, 5 build errors.**

## Bug class totals

| class | count |
|---|---|
| `onnx-tool-fails-valid-model` | 2334 |
| `onnx-tool-error` | 2334 |
| `scalar-volume` | 526 |
| `wrong-shape` | 281 |
| `wrong-dtype` | 62 |

## Per-op summary

| op | cases | disagreements | invalid | build-errors | notes |
|---|---|---|---|---|---|
| [`CastLike@16`](#castlike@16) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`IsInf@16`](#isinf@16) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Shrink@16`](#shrink@16) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Size@16`](#size@16) | 128 | 128 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Compress@16`](#compress@16) | 128 | 127 | 1 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Constant@16`](#constant@16) | 128 | 127 | 1 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`LpPool@16`](#lppool@16) | 128 | 101 | 27 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`BitShift@16`](#bitshift@16) | 128 | 93 | 35 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Selu@16`](#selu@16) | 128 | 92 | 36 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ThresholdedRelu@16`](#thresholdedrelu@16) | 128 | 89 | 39 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`RandomNormal@16`](#randomnormal@16) | 128 | 85 | 43 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`RandomUniform@16`](#randomuniform@16) | 128 | 85 | 43 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceL1@16`](#reducel1@16) | 128 | 84 | 44 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceLogSum@16`](#reducelogsum@16) | 128 | 84 | 44 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceLogSumExp@16`](#reducelogsumexp@16) | 128 | 84 | 44 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceSumSquare@16`](#reducesumsquare@16) | 128 | 84 | 44 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Shape@16`](#shape@16) | 128 | 83 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`GlobalLpPool@16`](#globallppool@16) | 128 | 72 | 56 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`MeanVarianceNormalization@16`](#meanvariancenormalization@16) | 128 | 72 | 56 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ArgMin@16`](#argmin@16) | 128 | 63 | 65 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`MaxPool@16`](#maxpool@16) | 128 | 52 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Celu@16`](#celu@16) | 48 | 48 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Unique@16`](#unique@16) | 128 | 45 | 83 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`IsNaN@16`](#isnan@16) | 36 | 36 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceL2@16`](#reducel2@16) | 128 | 36 | 44 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReverseSequence@16`](#reversesequence@16) | 128 | 36 | 92 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Round@16`](#round@16) | 36 | 36 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Abs@16`](#abs@16) | 128 | 29 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Sign@16`](#sign@16) | 128 | 29 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Flatten@16`](#flatten@16) | 128 | 27 | 15 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceMean@16`](#reducemean@16) | 128 | 25 | 44 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceProd@16`](#reduceprod@16) | 128 | 25 | 44 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Acos@16`](#acos@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Acosh@16`](#acosh@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Asin@16`](#asin@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Asinh@16`](#asinh@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Atanh@16`](#atanh@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Cosh@16`](#cosh@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Mean@16`](#mean@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Sinh@16`](#sinh@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Softsign@16`](#softsign@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Tan@16`](#tan@16) | 36 | 24 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Max@16`](#max@16) | 128 | 23 | 24 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Min@16`](#min@16) | 128 | 23 | 24 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceMax@16`](#reducemax@16) | 128 | 23 | 41 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceMin@16`](#reducemin@16) | 128 | 23 | 41 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`TopK@16`](#topk@16) | 128 | 23 | 60 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Neg@16`](#neg@16) | 84 | 21 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Cast@16`](#cast@16) | 128 | 20 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`GatherND@16`](#gathernd@16) | 128 | 20 | 94 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Identity@16`](#identity@16) | 128 | 20 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`LeakyRelu@16`](#leakyrelu@16) | 128 | 20 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`GlobalMaxPool@16`](#globalmaxpool@16) | 36 | 18 | 18 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Elu@16`](#elu@16) | 128 | 17 | 39 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Einsum@16`](#einsum@16) | 128 | 15 | 113 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Relu@16`](#relu@16) | 84 | 15 | 24 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`HardSigmoid@16`](#hardsigmoid@16) | 128 | 14 | 36 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`NonZero@16`](#nonzero@16) | 128 | 14 | 60 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`SpaceToDepth@16`](#spacetodepth@16) | 128 | 14 | 114 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`DequantizeLinear@16`](#dequantizelinear@16) | 128 | 12 | 116 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: x_zero_point |
| [`Det@16`](#det@16) | 36 | 12 | 24 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`DynamicQuantizeLinear@16`](#dynamicquantizelinear@16) | 12 | 12 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`PRelu@16`](#prelu@16) | 83 | 12 | 30 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Ceil@16`](#ceil@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Dropout@16`](#dropout@16) | 128 | 9 | 118 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: ratio, training_mode |
| [`Exp@16`](#exp@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Floor@16`](#floor@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Log@16`](#log@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Reciprocal@16`](#reciprocal@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Sigmoid@16`](#sigmoid@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Sin@16`](#sin@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Sqrt@16`](#sqrt@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Sum@16`](#sum@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Tanh@16`](#tanh@16) | 36 | 9 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ReduceSum@16`](#reducesum@16) | 128 | 8 | 63 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: axes |
| [`Split@16`](#split@16) | 128 | 8 | 101 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: split |
| [`Atan@16`](#atan@16) | 36 | 6 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Cos@16`](#cos@16) | 36 | 6 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Erf@16`](#erf@16) | 36 | 6 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`HardSwish@16`](#hardswish@16) | 36 | 6 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`QuantizeLinear@16`](#quantizelinear@16) | 128 | 6 | 122 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: y_zero_point |
| [`Softplus@16`](#softplus@16) | 36 | 6 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Transpose@16`](#transpose@16) | 128 | 6 | 14 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Where@16`](#where@16) | 70 | 4 | 32 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`And@16`](#and@16) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`AveragePool@16`](#averagepool@16) | 128 | 3 | 30 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Not@16`](#not@16) | 12 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Or@16`](#or@16) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Xor@16`](#xor@16) | 128 | 3 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Conv@16`](#conv@16) | 128 | 2 | 117 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: B |
| [`ConvInteger@16`](#convinteger@16) | 128 | 2 | 125 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: x_zero_point, w_zero_point |
| [`MatMulInteger@16`](#matmulinteger@16) | 128 | 2 | 123 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: a_zero_point, b_zero_point |
| [`RandomNormalLike@16`](#randomnormallike@16) | 128 | 2 | 118 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`RandomUniformLike@16`](#randomuniformlike@16) | 128 | 2 | 118 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Add@16`](#add@16) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Clip@16`](#clip@16) | 21 | 1 | 19 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: min, max |
| [`Equal@16`](#equal@16) | 58 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Greater@16`](#greater@16) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`GreaterOrEqual@16`](#greaterorequal@16) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Less@16`](#less@16) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`LessOrEqual@16`](#lessorequal@16) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Mul@16`](#mul@16) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Pow@16`](#pow@16) | 128 | 1 | 69 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Sub@16`](#sub@16) | 67 | 1 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ArgMax@16`](#argmax@16) | 128 | 0 | 65 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`BatchNormalization@16`](#batchnormalization@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Bernoulli@16`](#bernoulli@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Concat@16`](#concat@16) | 128 | 0 | 20 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ConcatFromSequence@16`](#concatfromsequence@16) | 12 | 0 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ConstantOfShape@16`](#constantofshape@16) | 24 | 0 | 24 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ConvTranspose@16`](#convtranspose@16) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`CumSum@16`](#cumsum@16) | 128 | 0 | 110 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`DepthToSpace@16`](#depthtospace@16) | 128 | 0 | 118 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Div@16`](#div@16) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`Expand@16`](#expand@16) | 128 | 0 | 106 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`EyeLike@16`](#eyelike@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`GRU@16`](#gru@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: B, sequence_lens, initial_h |
| [`Gather@16`](#gather@16) | 128 | 0 | 73 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`GatherElements@16`](#gatherelements@16) | 128 | 0 | 93 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Gemm@16`](#gemm@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: C |
| [`GlobalAveragePool@16`](#globalaveragepool@16) | 36 | 0 | 18 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`GridSample@16`](#gridsample@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Hardmax@16`](#hardmax@16) | 108 | 0 | 36 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`If@16`](#if@16) | 12 | 0 | 12 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`InstanceNormalization@16`](#instancenormalization@16) | 128 | 0 | 35 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`LRN@16`](#lrn@16) | 128 | 0 | 109 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`LSTM@16`](#lstm@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: B, sequence_lens, initial_h, initial_c, P |
| [`LogSoftmax@16`](#logsoftmax@16) | 108 | 0 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Loop@16`](#loop@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: M, cond |
| [`LpNormalization@16`](#lpnormalization@16) | 128 | 0 | 42 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`MatMul@16`](#matmul@16) | 83 | 0 | 53 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`MaxRoiPool@16`](#maxroipool@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`MaxUnpool@16`](#maxunpool@16) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`Mod@16`](#mod@16) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`Multinomial@16`](#multinomial@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`NegativeLogLikelihoodLoss@16`](#negativeloglikelihoodloss@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: weight |
| [`NonMaxSuppression@16`](#nonmaxsuppression@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: max_output_boxes_per_class, iou_threshold, score_threshold |
| [`OneHot@16`](#onehot@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Optional@16`](#optional@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: input |
| [`OptionalGetElement@16`](#optionalgetelement@16) | 1 | 0 | 1 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`OptionalHasElement@16`](#optionalhaselement@16) | 1 | 0 | 1 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Pad@16`](#pad@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: constant_value |
| [`QLinearConv@16`](#qlinearconv@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: B |
| [`QLinearMatMul@16`](#qlinearmatmul@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`RNN@16`](#rnn@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: B, sequence_lens, initial_h |
| [`Range@16`](#range@16) | 32 | 0 | 31 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Reshape@16`](#reshape@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Resize@16`](#resize@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: roi, scales, sizes |
| [`RoiAlign@16`](#roialign@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Scan@16`](#scan@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Scatter@16`](#scatter@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ScatterElements@16`](#scatterelements@16) | 128 | 0 | 107 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`ScatterND@16`](#scatternd@16) | 124 | 0 | 124 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`SequenceAt@16`](#sequenceat@16) | 24 | 0 | 24 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`SequenceConstruct@16`](#sequenceconstruct@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`SequenceEmpty@16`](#sequenceempty@16) | 4 | 0 | 4 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`SequenceErase@16`](#sequenceerase@16) | 25 | 0 | 25 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: position |
| [`SequenceInsert@16`](#sequenceinsert@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: position |
| [`SequenceLength@16`](#sequencelength@16) | 1 | 0 | 1 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Slice@16`](#slice@16) | 97 | 0 | 97 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: axes, steps |
| [`Softmax@16`](#softmax@16) | 108 | 0 | 0 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`SoftmaxCrossEntropyLoss@16`](#softmaxcrossentropyloss@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: weights |
| [`SplitToSequence@16`](#splittosequence@16) | 1 | 0 | 0 | 1 | op worker exited without result |
| [`Squeeze@16`](#squeeze@16) | 128 | 0 | 96 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: axes |
| [`StringNormalizer@16`](#stringnormalizer@16) | 24 | 0 | 24 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`TfIdfVectorizer@16`](#tfidfvectorizer@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Tile@16`](#tile@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Trilu@16`](#trilu@16) | 128 | 0 | 92 | 0 | Auto-generated from ONNX schema (opset 16). Optional inputs: k |
| [`Unsqueeze@16`](#unsqueeze@16) | 128 | 0 | 87 | 0 | Auto-generated from ONNX schema (opset 16) |
| [`Upsample@16`](#upsample@16) | 128 | 0 | 128 | 0 | Auto-generated from ONNX schema (opset 16) |

## `CastLike@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 128 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=128, `onnx-tool-fails-valid-model`=128

### Disagreements
#### `onnx-tool-error` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random target_type(input)=BCHW/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/random target_type(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random target_type(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/random target_type(input)=BCHW/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/int16/random target_type(input)=BCHW/int16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/random target_type(input)=BCHW/int32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/int64/random target_type(input)=BCHW/int64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/int8/random target_type(input)=BCHW/int8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint16/random target_type(input)=BCHW/uint16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint32/random target_type(input)=BCHW/uint32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint64/random target_type(input)=BCHW/uint64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint8/random target_type(input)=BCHW/uint8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/alternating target_type(input)=BCHW/bool/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse target_type(input)=BCHW/bool/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/bool/random target_type(input)=B-1-H-1/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/bool/random target_type(input)=B-C-1-1/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=scalar/bool/random target_type(input)=scalar/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/random target_type(input)=BCHW/uint8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/random target_type(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/random target_type(input)=B-1-H-1/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| ... | _+108 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (128 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random target_type(input)=BCHW/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/float16/random target_type(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/float32/random target_type(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/float64/random target_type(input)=BCHW/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/int16/random target_type(input)=BCHW/int16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/int32/random target_type(input)=BCHW/int32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/int64/random target_type(input)=BCHW/int64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/int8/random target_type(input)=BCHW/int8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint16/random target_type(input)=BCHW/uint16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint32/random target_type(input)=BCHW/uint32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint64/random target_type(input)=BCHW/uint64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/uint8/random target_type(input)=BCHW/uint8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/alternating target_type(input)=BCHW/bool/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/sparse target_type(input)=BCHW/bool/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=B-1-H-1/bool/random target_type(input)=B-1-H-1/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `30B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=B-C-1-1/bool/random target_type(input)=B-C-1-1/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `10B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=scalar/bool/random target_type(input)=scalar/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/random target_type(input)=BCHW/uint8/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/random target_type(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| _case:_ `input(input)=BCHW/bool/random target_type(input)=B-1-H-1/float64/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node CastLike-CastLike_0 has no value_infer |
| ... | _+108 more cases_ | | | |

## `IsInf@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Shrink@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Size@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Compress@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Constant@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 127 with disagreements, 1 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=86, `onnx-tool-fails-valid-model`=86, `scalar-volume`=41

### Disagreements
#### `onnx-tool-error` (86 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'value_string': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_floats': [0.0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_floats': [0.0, 1.0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_ints': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_ints': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_strings': [b'']} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_float': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_float': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_float': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_strings': [b''], 'value_float': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_ints': [1], 'value_strings': [b''], 'value_float': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_ints': [1, 1], 'value_strings': [b'']} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0, 'value_float': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0, 'value_ints': [1], 'value_float': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0, 'value_ints': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0, 'value_ints': [1, 1], 'value_strings': [b''], 'value_float': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 1, 'value_strings': [b''], 'value_float': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 1, 'value_ints': [1], 'value_strings': [b'']} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| ... | _+66 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (86 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'value_string': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_floats': [0.0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_floats': [0.0, 1.0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_ints': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_ints': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `16B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_strings': [b'']} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_float': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_float': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_float': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_strings': [b''], 'value_float': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_ints': [1], 'value_strings': [b''], 'value_float': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_ints': [1, 1], 'value_strings': [b'']} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `16B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0, 'value_float': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0, 'value_ints': [1], 'value_float': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0, 'value_ints': [1, 1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 0, 'value_ints': [1, 1], 'value_strings': [b''], 'value_float': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 1, 'value_strings': [b''], 'value_float': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| _case:_ ` {'value_int': 1, 'value_ints': [1], 'value_strings': [b'']} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | AttributeError: 'ConstantNode' object has no attribute 'value' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: AttributeError: 'ConstantNode' object has no attribute 'value' |
| ... | _+66 more cases_ | | | |

#### `scalar-volume` (41 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_float': 0.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_strings': [b''], 'value_float': 0.5} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_ints': [1]} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_ints': [1], 'value_strings': [b''], 'value_float': 1.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_ints': [1, 1], 'value_strings': [b''], 'value_float': 0.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 0, 'value_strings': [b'']} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 0, 'value_ints': [1], 'value_float': 0.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 0, 'value_ints': [1], 'value_float': 1.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 0, 'value_ints': [1, 1], 'value_float': 0.5} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 1, 'value_float': 0.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 1, 'value_strings': [b''], 'value_float': 1.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 1, 'value_ints': [1], 'value_strings': [b'']} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 1, 'value_ints': [1], 'value_strings': [b''], 'value_float': 0.5} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_int': 1, 'value_ints': [1, 1], 'value_strings': [b''], 'value_float': 0.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_floats': [0.0], 'value_strings': [b'']} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_floats': [0.0], 'value_ints': [1], 'value_float': 0.5} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_floats': [0.0], 'value_ints': [1], 'value_strings': [b''], 'value_float': 1.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_floats': [0.0], 'value_ints': [1, 1], 'value_float': 0.0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ ` {'value': data_type: 1
name: "attr_value"
raw_data: "\000\000\200?"
, 'value_floats': [0.0], 'value_int': 0} outputs=1` | | | | |
| `output` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| ... | _+21 more cases_ | | | |

## `LpPool@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `BitShift@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Selu@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `ThresholdedRelu@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `RandomNormal@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `RandomUniform@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `ReduceL1@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 84 with disagreements, 44 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=84, `onnx-tool-fails-valid-model`=84

### Disagreements
#### `onnx-tool-error` (84 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| ... | _+64 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (84 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `3600B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer |
| ... | _+64 more cases_ | | | |

## `ReduceLogSum@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 84 with disagreements, 44 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=84, `onnx-tool-fails-valid-model`=84

### Disagreements
#### `onnx-tool-error` (84 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| ... | _+64 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (84 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `3600B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer |
| ... | _+64 more cases_ | | | |

## `ReduceLogSumExp@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 84 with disagreements, 44 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=84, `onnx-tool-fails-valid-model`=84

### Disagreements
#### `onnx-tool-error` (84 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| ... | _+64 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (84 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `3600B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer |
| ... | _+64 more cases_ | | | |

## `ReduceSumSquare@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 84 with disagreements, 44 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=84, `onnx-tool-fails-valid-model`=84

### Disagreements
#### `onnx-tool-error` (84 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| ... | _+64 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (84 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `1800B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `20B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `60B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `3600B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer |
| ... | _+64 more cases_ | | | |

## `Shape@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 83 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=83

### Disagreements
#### `wrong-shape` (83 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float32/random {'start': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(3)` / `int64` / `24B` | `(4)` / `int64` / `32B` | truth=(3,) claim=(4,) |
| _case:_ `data(input)=BCHW/float64/random {'end': 0} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/int16/random {'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(1)` / `int64` / `8B` | `(4)` / `int64` / `32B` | truth=(1,) claim=(4,) |
| _case:_ `data(input)=BCHW/int32/random {'start': 0, 'end': 0} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/int64/random {'start': 0, 'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(1)` / `int64` / `8B` | `(4)` / `int64` / `32B` | truth=(1,) claim=(4,) |
| _case:_ `data(input)=BCHW/int8/random {'start': 1, 'end': 0} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/uint16/random {'start': 1, 'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/uint8/random {'start': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(3)` / `int64` / `24B` | `(4)` / `int64` / `32B` | truth=(3,) claim=(4,) |
| _case:_ `data(input)=BCHW/bool/alternating {'end': 0} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/bool/sparse {'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(1)` / `int64` / `8B` | `(4)` / `int64` / `32B` | truth=(1,) claim=(4,) |
| _case:_ `data(input)=B-1-H-1/bool/random {'start': 0, 'end': 0} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=B-C-1-1/bool/random {'start': 0, 'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(1)` / `int64` / `8B` | `(4)` / `int64` / `32B` | truth=(1,) claim=(4,) |
| _case:_ `data(input)=BCHW/float16/sparse {'start': 1, 'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/float32/alternating {'start': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(3)` / `int64` / `24B` | `(4)` / `int64` / `32B` | truth=(3,) claim=(4,) |
| _case:_ `data(input)=BCHW/float64/sparse {'end': 0} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/float64/alternating {'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(1)` / `int64` / `8B` | `(4)` / `int64` / `32B` | truth=(1,) claim=(4,) |
| _case:_ `data(input)=BCHW/int16/sparse {'start': 0, 'end': 0} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/int16/alternating {'start': 0, 'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(1)` / `int64` / `8B` | `(4)` / `int64` / `32B` | truth=(1,) claim=(4,) |
| _case:_ `data(input)=BCHW/int32/sparse {'start': 1, 'end': 0} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| _case:_ `data(input)=BCHW/int32/alternating {'start': 1, 'end': 1} outputs=1` | | | | |
| `shape` | `wrong-shape` | `(0)` / `int64` / `0B` | `(4)` / `int64` / `32B` | truth=(0,) claim=(4,) |
| ... | _+63 more cases_ | | | |

## `GlobalLpPool@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `MeanVarianceNormalization@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `ArgMin@16`
_Auto-generated from ONNX schema (opset 16)_

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
| _case:_ `data(input)=BCHW/int8/random {'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random {'keepdims': 0, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 0, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axis': 0, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axis': 0, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axis': 0, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse {'axis': 0, 'keepdims': 1, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axis': 0, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axis': 0, 'keepdims': 0, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axis': 0, 'keepdims': 0, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axis': 1, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axis': 1, 'keepdims': 1, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axis': 1, 'keepdims': 1, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axis': 1, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/sparse {'axis': 1, 'keepdims': 0, 'select_last_index': 0} outputs=1` | | | | |
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
| _case:_ `data(input)=BCHW/int8/random {'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/uint8/random {'keepdims': 0, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 0, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float16/sparse {'axis': 0, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-1-H-1/float16/random {'axis': 0, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `240B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=B-C-1-1/float16/random {'axis': 0, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `80B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/sparse {'axis': 0, 'keepdims': 1, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float32/alternating {'axis': 0, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/sparse {'axis': 0, 'keepdims': 0, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/float64/alternating {'axis': 0, 'keepdims': 0, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/sparse {'axis': 1, 'keepdims': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int32/alternating {'axis': 1, 'keepdims': 1, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/sparse {'axis': 1, 'keepdims': 1, 'select_last_index': 1} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int64/alternating {'axis': 1, 'keepdims': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| _case:_ `data(input)=BCHW/int8/sparse {'axis': 1, 'keepdims': 0, 'select_last_index': 0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `7200B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer |
| ... | _+43 more cases_ | | | |

## `MaxPool@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 52 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=54

### Disagreements
#### `wrong-shape` (52 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random {'kernel_shape': [2, 2]} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,29,29)` / `int64` / `67280B` | `()` / `int64` / `0B` | truth=(1, 10, 29, 29) claim=() |
| _case:_ `X(input)=BCHW/int8/random {'kernel_shape': [1, 1], 'strides': [1, 1]} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=B-1-H-1/float16/random {'kernel_shape': [1, 1], 'auto_pad': b'NOTSET'} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [1, 1], 'ceil_mode': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=BCHW/float64/alternating {'kernel_shape': [1, 1], 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=BCHW/int8/alternating {'kernel_shape': [1, 1], 'pads': [0, 0, 0, 0], 'ceil_mode': 1, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=B-C-1-1/float64/alternating {'kernel_shape': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET'} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,1,1)` / `int64` / `80B` | `()` / `int64` / `0B` | truth=(1, 10, 1, 1) claim=() |
| _case:_ `X(input)=B-C-1-1/int8/sparse {'kernel_shape': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'ceil_mode': 1, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,1,1)` / `int64` / `80B` | `()` / `int64` / `0B` | truth=(1, 10, 1, 1) claim=() |
| _case:_ `X(input)=B-C-1-1/uint8/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'ceil_mode': 0, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,1,1)` / `int64` / `80B` | `()` / `int64` / `0B` | truth=(1, 10, 1, 1) claim=() |
| _case:_ `X(input)=B-1-H-1/float16/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'auto_pad': b'SAME_UPPER', 'pads': [0, 0, 0, 0], 'ceil_mode': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=B-1-H-1/float64/alternating {'kernel_shape': [1, 1], 'strides': [1, 1], 'dilations': [1, 1], 'ceil_mode': 1, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=B-1-H-1/int8/sparse {'kernel_shape': [1, 1], 'strides': [1, 1], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'ceil_mode': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=B-1-H-1/uint8/random {'kernel_shape': [1, 1], 'strides': [1, 1], 'dilations': [1, 1], 'auto_pad': b'SAME_UPPER', 'ceil_mode': 0, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,30,1)` / `int64` / `240B` | `()` / `int64` / `0B` | truth=(1, 1, 30, 1) claim=() |
| _case:_ `X(input)=B-1-H-1/uint8/alternating {'kernel_shape': [1, 1], 'strides': [2, 2], 'pads': [0, 0, 0, 0], 'ceil_mode': 0, 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,1,15,1)` / `int64` / `120B` | `()` / `int64` / `0B` | truth=(1, 1, 15, 1) claim=() |
| _case:_ `X(input)=BCHW/float32/random {'kernel_shape': [2, 2], 'auto_pad': b'NOTSET', 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,29,29)` / `int64` / `67280B` | `()` / `int64` / `0B` | truth=(1, 10, 29, 29) claim=() |
| _case:_ `X(input)=BCHW/int8/random {'kernel_shape': [2, 2], 'auto_pad': b'SAME_UPPER', 'ceil_mode': 1, 'storage_order': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=BCHW/float32/alternating {'kernel_shape': [2, 2], 'dilations': [1, 1], 'auto_pad': b'NOTSET', 'ceil_mode': 1} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,29,29)` / `int64` / `67280B` | `()` / `int64` / `0B` | truth=(1, 10, 29, 29) claim=() |
| _case:_ `X(input)=BCHW/float64/alternating {'kernel_shape': [2, 2], 'dilations': [1, 1], 'auto_pad': b'SAME_UPPER', 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,30,30)` / `int64` / `72000B` | `()` / `int64` / `0B` | truth=(1, 10, 30, 30) claim=() |
| _case:_ `X(input)=BCHW/int8/alternating {'kernel_shape': [2, 2], 'strides': [1, 1], 'pads': [0, 0, 0, 0]} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,29,29)` / `int64` / `67280B` | `()` / `int64` / `0B` | truth=(1, 10, 29, 29) claim=() |
| _case:_ `X(input)=BCHW/uint8/alternating {'kernel_shape': [2, 2], 'strides': [1, 1], 'auto_pad': b'NOTSET', 'pads': [0, 0, 0, 0], 'ceil_mode': 1, 'storage_order': 0} outputs=11` | | | | |
| `Indices` | `wrong-shape` | `(1,10,29,29)` / `int64` / `67280B` | `()` / `int64` / `0B` | truth=(1, 10, 29, 29) claim=() |
| ... | _+32 more cases_ | | | |

## `Celu@16`
_Auto-generated from ONNX schema (opset 16)_

- 48 cases, 48 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=48, `onnx-tool-fails-valid-model`=48

### Disagreements
#### `onnx-tool-error` (48 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/sparse {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| ... | _+28 more cases_ | | | |

#### `onnx-tool-fails-valid-model` (48 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/random {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/sparse {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-C-1-1/float32/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `40B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=B-1-H-1/float32/alternating {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `120B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/sparse {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=scalar/float32/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/random {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 0.5} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/alternating {'alpha': 1.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| _case:_ `X(input)=BCHW/float32/sparse {'alpha': 0.0} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: NotImplementedError: this Node Celu-Celu_0 has no value_infer |
| ... | _+28 more cases_ | | | |

## `Unique@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `IsNaN@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `ReduceL2@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 36 with disagreements, 44 invalid ignored, 0 build errors
- bug classes hit: `wrong-dtype`=26, `scalar-volume`=10

### Disagreements
#### `scalar-volume` (10 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=B-1-H-1/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

#### `wrong-dtype` (26 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/int32/random {'axes': [0]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10,30,30)` / `int32` / `36000B` | `(1,10,30,30)` / `float64` / `72000B` | truth=int32 claim=float64 |
| _case:_ `data(input)=BCHW/int64/random {'axes': [1]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,30,30)` / `int64` / `7200B` | `(1,1,30,30)` / `float64` / `7200B` | truth=int64 claim=float64 |
| _case:_ `data(input)=BCHW/int32/sparse {'axes': [1]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,30,30)` / `int32` / `3600B` | `(1,1,30,30)` / `float64` / `7200B` | truth=int32 claim=float64 |
| _case:_ `data(input)=BCHW/int32/alternating {'axes': [2, 3]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10,1,1)` / `int32` / `40B` | `(1,10,1,1)` / `float64` / `80B` | truth=int32 claim=float64 |
| _case:_ `data(input)=BCHW/int64/sparse {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10,30,30)` / `int64` / `72000B` | `(1,10,30,30)` / `float64` / `72000B` | truth=int64 claim=float64 |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,30,30)` / `int64` / `7200B` | `(1,1,30,30)` / `float64` / `7200B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int32/random {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10,1,1)` / `int32` / `40B` | `(1,10,1,1)` / `float64` / `80B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int32/sparse {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(10,1,1)` / `int32` / `40B` | `(10,1,1)` / `float64` / `80B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int32/alternating {'keepdims': 0, 'axes': [1]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1)` / `int32` / `4B` | `(1,1,1)` / `float64` / `8B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int64/random {'keepdims': 0, 'axes': [2, 3]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,10)` / `int64` / `80B` | `(1,10)` / `float64` / `80B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int64` / `8B` | `(1,1,1,1)` / `float64` / `8B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-C-1-1/int64/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int64` / `8B` | `(1,1,1,1)` / `float64` / `8B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int32/random {'axes': [1]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,30,1)` / `int32` / `120B` | `(1,1,30,1)` / `float64` / `240B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int32/sparse {'axes': [2, 3]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int32` / `4B` | `(1,1,1,1)` / `float64` / `8B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int32/alternating {'keepdims': 1, 'axes': [0]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,30,1)` / `int32` / `120B` | `(1,1,30,1)` / `float64` / `240B` | truth=int32 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int64/random {'keepdims': 1, 'axes': [1]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,30,1)` / `int64` / `240B` | `(1,1,30,1)` / `float64` / `240B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int64/sparse {'keepdims': 1, 'axes': [2, 3]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,1,1,1)` / `int64` / `8B` | `(1,1,1,1)` / `float64` / `8B` | truth=int64 claim=float64 |
| _case:_ `data(input)=B-1-H-1/int64/alternating {'keepdims': 0, 'axes': [0]} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `(1,30,1)` / `int64` / `240B` | `(1,30,1)` / `float64` / `240B` | truth=int64 claim=float64 |
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `()` / `int32` / `4B` | `()` / `float64` / `0B` | truth=int32 claim=float64 |
| _case:_ `data(input)=scalar/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-dtype` | `()` / `int32` / `4B` | `()` / `float64` / `0B` | truth=int32 claim=float64 |
| ... | _+6 more cases_ | | | |

## `ReverseSequence@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Round@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Abs@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Sign@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Flatten@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `ReduceMean@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 25 with disagreements, 44 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=21, `scalar-volume`=4

### Disagreements
#### `scalar-volume` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (21 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,1,1)` / `float32` / `40B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,1,30,1)` / `float64` / `240B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| ... | _+1 more cases_ | | | |

## `ReduceProd@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 25 with disagreements, 44 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=21, `scalar-volume`=4

### Disagreements
#### `scalar-volume` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/int32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

#### `wrong-shape` (21 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float16/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float32/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,1,1)` / `float32` / `40B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int64/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,1,1)` / `int64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,1,30,1)` / `float64` / `240B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float16/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-1-H-1/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-C-1-1/float16/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| ... | _+1 more cases_ | | | |

## `Acos@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Acosh@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Asin@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Asinh@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Atanh@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Cosh@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Mean@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Sinh@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Softsign@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Tan@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Max@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 23 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=23

### Disagreements
#### `scalar-volume` (23 cases)

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
| _case:_ `data_0(input)=scalar/int32/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/int32/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/int32/alternating  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/int64/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/int64/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/int64/alternating  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/int8/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data_0(input)=scalar/int8/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data_0(input)=scalar/int8/alternating  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data_0(input)=scalar/uint32/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `uint32` / `4B` | `()` / `uint32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/uint32/sparse  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `uint32` / `4B` | `()` / `uint32` / `0B` | scalar dropped from accounting (true=4B) |
| ... | _+3 more cases_ | | | |

## `Min@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 23 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=23

### Disagreements
#### `scalar-volume` (23 cases)

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
| _case:_ `data_0(input)=scalar/int32/random  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/int32/sparse  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/int32/alternating  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/int64/random  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/int64/sparse  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/int64/alternating  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int64` / `8B` | `()` / `int64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `data_0(input)=scalar/int8/random  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data_0(input)=scalar/int8/sparse  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data_0(input)=scalar/int8/alternating  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data_0(input)=scalar/uint32/random  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `uint32` / `4B` | `()` / `uint32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data_0(input)=scalar/uint32/sparse  outputs=1` | | | | |
| `min` | `scalar-volume` | `()` / `uint32` / `4B` | `()` / `uint32` / `0B` | scalar dropped from accounting (true=4B) |
| ... | _+3 more cases_ | | | |

## `ReduceMax@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 23 with disagreements, 41 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=16, `scalar-volume`=7

### Disagreements
#### `scalar-volume` (7 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int8/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=scalar/int8/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=scalar/int8/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |

#### `wrong-shape` (16 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float64/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int32/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,10,1,1)` / `int32` / `40B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,1,30,1)` / `float64` / `240B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int8/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int8` / `1B` | `(1,1,30,1)` / `int8` / `30B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int64` / `8B` | `(1,10,30,30)` / `int64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int8/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int8` / `1B` | `(1,10,30,30)` / `int8` / `9000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/uint8/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `uint8` / `1B` | `(1,10,30,30)` / `uint8` / `9000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |

## `ReduceMin@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 23 with disagreements, 41 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=16, `scalar-volume`=7

### Disagreements
#### `scalar-volume` (7 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `data(input)=scalar/float32/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/float32/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `data(input)=scalar/int8/random  outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=scalar/int8/sparse {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=scalar/int8/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |

#### `wrong-shape` (16 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,1,1)` / `float16` / `20B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=BCHW/float32/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=B-C-1-1/float64/sparse  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/float64/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,1,1)` / `float64` / `80B` | truth=(1, 1, 1, 1) claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-C-1-1/int32/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int32` / `4B` | `(1,10,1,1)` / `int32` / `40B` | truth=() claim=(1, 10, 1, 1) |
| _case:_ `data(input)=B-1-H-1/float32/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,1,30,1)` / `float32` / `120B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/float64/sparse {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,1,30,1)` / `float64` / `240B` | truth=() claim=(1, 1, 30, 1) |
| _case:_ `data(input)=B-1-H-1/int8/alternating  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int8` / `1B` | `(1,1,30,1)` / `int8` / `30B` | truth=(1, 1, 1, 1) claim=(1, 1, 30, 1) |
| _case:_ `data(input)=BCHW/float64/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/random {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `int64` / `8B` | `(1,10,30,30)` / `int64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int8/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int8` / `1B` | `(1,10,30,30)` / `int8` / `9000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/uint8/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `uint8` / `1B` | `(1,10,30,30)` / `uint8` / `9000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |

## `TopK@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Neg@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Cast@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `GatherND@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 20 with disagreements, 94 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=20

### Disagreements
#### `wrong-shape` (20 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float32/random indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `float32` / `3600B` | `(10,30,30)` / `float32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/random indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `int32` / `3600B` | `(10,30,30)` / `int32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/uint16/random indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `uint16` / `1800B` | `(10,30,30)` / `uint16` / `18000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/uint8/random indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `uint8` / `900B` | `(10,30,30)` / `uint8` / `9000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/bool/sparse indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `bool` / `900B` | `(10,30,30)` / `bool` / `9000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/random indices(init)=1d-1/int64/alternating {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `float32` / `3600B` | `(10,30,30)` / `float32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/sparse indices(init)=1d-1/int64/sparse {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `float32` / `3600B` | `(10,30,30)` / `float32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/alternating indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `float32` / `3600B` | `(10,30,30)` / `float32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/random indices(init)=1d-1/int64/sparse {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `float64` / `7200B` | `(10,30,30)` / `float64` / `72000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `float64` / `7200B` | `(10,30,30)` / `float64` / `72000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/random indices(init)=1d-1/int64/alternating {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `int32` / `3600B` | `(10,30,30)` / `int32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/sparse indices(init)=1d-1/int64/sparse {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `int32` / `3600B` | `(10,30,30)` / `int32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/int32/alternating indices(init)=1d-1/int64/sparse {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `int32` / `3600B` | `(10,30,30)` / `int32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/random indices(init)=1d-1/int64/sparse {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `int64` / `7200B` | `(10,30,30)` / `int64` / `72000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/sparse indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `int64` / `7200B` | `(10,30,30)` / `int64` / `72000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/uint16/random indices(init)=1d-1/int64/alternating {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `uint16` / `1800B` | `(10,30,30)` / `uint16` / `18000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/uint16/sparse indices(init)=1d-1/int64/sparse {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `uint16` / `1800B` | `(10,30,30)` / `uint16` / `18000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/uint16/alternating indices(init)=1d-1/int64/sparse {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `uint16` / `1800B` | `(10,30,30)` / `uint16` / `18000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/uint32/random indices(init)=1d-1/int64/sparse {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `uint32` / `3600B` | `(10,30,30)` / `uint32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |
| _case:_ `data(input)=BCHW/uint32/sparse indices(init)=1d-1/int64/random {'batch_dims': 1} outputs=1` | | | | |
| `output` | `wrong-shape` | `(30,30)` / `uint32` / `3600B` | `(10,30,30)` / `uint32` / `36000B` | truth=(30, 30) claim=(10, 30, 30) |

## `Identity@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `LeakyRelu@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 20 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=20

### Disagreements
#### `scalar-volume` (20 cases)

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
| _case:_ `X(input)=scalar/float64/random {'alpha': 0.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/sparse {'alpha': 0.5} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| _case:_ `X(input)=scalar/float64/alternating {'alpha': 1.0} outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
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

## `GlobalMaxPool@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Elu@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Einsum@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 15 with disagreements, 113 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=15, `onnx-tool-fails-valid-model`=15

### Disagreements
#### `onnx-tool-error` (15 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `Inputs(input)=scalar/float16/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float16/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float16/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float32/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float32/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float32/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float64/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float64/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float64/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int32/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int32/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int32/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int64/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int64/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int64/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |

#### `onnx-tool-fails-valid-model` (15 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `Inputs(input)=scalar/float16/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float16/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float16/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `2B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float32/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float32/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float32/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float64/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float64/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/float64/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int32/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int32/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int32/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `4B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int64/random {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int64/sparse {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |
| _case:_ `Inputs(input)=scalar/int64/alternating {'equation': b''} outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | IndexError: list index out of range |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `8B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: IndexError: list index out of range |

## `Relu@16`
_Auto-generated from ONNX schema (opset 16)_

- 84 cases, 15 with disagreements, 24 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=15

### Disagreements
#### `scalar-volume` (15 cases)

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
| _case:_ `X(input)=scalar/int32/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int32/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int32/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `X(input)=scalar/int8/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `X(input)=scalar/int8/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `X(input)=scalar/int8/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |

## `HardSigmoid@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `NonZero@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `SpaceToDepth@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `DequantizeLinear@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: x_zero_point_

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
| _case:_ `x(input)=BCHW/int32/random x_scale(init)=scalar/float32/alternating x_zero_point(init)=scalar/int32/alternating {'axis': 1} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/sparse {'axis': 0} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/alternating {'axis': -1} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int32/alternating x_scale(init)=scalar/float32/random x_zero_point(init)=scalar/int32/alternating  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int8/random x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int8/sparse {'axis': 0} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/int8/alternating x_scale(init)=scalar/float32/alternating {'axis': 1} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=BCHW/int8/alternating x_scale(init)=scalar/float32/alternating x_zero_point(init)=scalar/int8/random {'axis': 0} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/uint8/random x_scale(init)=scalar/float32/random x_zero_point(init)=scalar/uint8/alternating {'axis': -1} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=B-C-1-1/int32/sparse x_scale(init)=scalar/float32/sparse x_zero_point(init)=scalar/int32/sparse {'axis': 1} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `x_zero_point` | `scalar-volume` | `()` / `int32` / `4B` | `()` / `int32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=B-C-1-1/int32/alternating x_scale(init)=scalar/float32/random {'axis': -1} outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| _case:_ `x(input)=B-C-1-1/int32/alternating x_scale(init)=scalar/float32/sparse  outputs=1` | | | | |
| `x_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |

## `Det@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `DynamicQuantizeLinear@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `PRelu@16`
_Auto-generated from ONNX schema (opset 16)_

- 83 cases, 12 with disagreements, 30 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=8, `scalar-volume`=4

### Disagreements
#### `scalar-volume` (4 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random slope(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/random slope(input)=scalar/float16/sparse  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float16/sparse slope(input)=scalar/float16/random  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| _case:_ `X(input)=scalar/float64/random slope(input)=scalar/float64/alternating  outputs=1` | | | | |
| `Y` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |

#### `wrong-shape` (8 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=B-C-1-1/float16/random slope(input)=B-1-H-1/float16/alternating  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/sparse slope(input)=B-1-H-1/float16/sparse  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float16/alternating slope(input)=B-1-H-1/float16/random  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float16` / `600B` | `(1,1,30,1)` / `float16` / `60B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float64/sparse slope(input)=B-1-H-1/float64/alternating  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/float64/alternating slope(input)=B-1-H-1/float64/sparse  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-C-1-1/int64/alternating slope(input)=B-1-H-1/int64/sparse  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `int64` / `2400B` | `(1,1,30,1)` / `int64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/float64/random slope(input)=B-C-1-1/float64/random  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `float64` / `2400B` | `(1,1,30,1)` / `float64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |
| _case:_ `X(input)=B-1-H-1/int64/random slope(input)=B-C-1-1/int64/random  outputs=1` | | | | |
| `Y` | `wrong-shape` | `(1,10,30,1)` / `int64` / `2400B` | `(1,1,30,1)` / `int64` / `240B` | truth=(1, 10, 30, 1) claim=(1, 1, 30, 1) |

## `Ceil@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Dropout@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: ratio, training_mode_

- 128 cases, 9 with disagreements, 118 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=20

### Disagreements
#### `scalar-volume` (9 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=scalar/float16/random ratio(init)=scalar/float16/random training_mode(init)=scalar/bool/all_true {'seed': 1} outputs=11` | | | | |
| `mask` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `ratio` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=BCHW/float16/random ratio(init)=scalar/float64/sparse training_mode(init)=scalar/bool/all_true  outputs=10` | | | | |
| `ratio` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=BCHW/float16/sparse ratio(init)=scalar/float16/sparse training_mode(init)=scalar/bool/alternating {'seed': 1} outputs=11` | | | | |
| `ratio` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=BCHW/float16/sparse ratio(init)=scalar/float64/sparse training_mode(init)=scalar/bool/alternating  outputs=11` | | | | |
| `ratio` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=BCHW/float16/alternating ratio(init)=scalar/float16/random training_mode(init)=scalar/bool/alternating {'seed': 1} outputs=10` | | | | |
| `ratio` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=BCHW/float16/alternating ratio(init)=scalar/float32/sparse training_mode(init)=scalar/bool/all_false {'seed': 1} outputs=11` | | | | |
| `ratio` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=BCHW/float16/alternating ratio(init)=scalar/float64/sparse training_mode(init)=scalar/bool/all_false {'seed': 1} outputs=10` | | | | |
| `ratio` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=BCHW/float32/random ratio(init)=scalar/float64/random training_mode(init)=scalar/bool/all_false {'seed': 1} outputs=11` | | | | |
| `ratio` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `data(input)=BCHW/float32/random ratio(init)=scalar/float64/random training_mode(init)=scalar/bool/alternating  outputs=10` | | | | |
| `ratio` | `scalar-volume` | `()` / `float64` / `8B` | `()` / `float64` / `0B` | scalar dropped from accounting (true=8B) |
| `training_mode` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Exp@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Floor@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Log@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Reciprocal@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Sigmoid@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Sin@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Sqrt@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Sum@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Tanh@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `ReduceSum@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: axes_

- 128 cases, 8 with disagreements, 63 invalid ignored, 0 build errors
- bug classes hit: `wrong-shape`=8

### Disagreements
#### `wrong-shape` (8 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `data(input)=BCHW/float16/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float16/alternating {'keepdims': 1, 'noop_with_empty_axes': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float16` / `2B` | `(1,10,30,30)` / `float16` / `18000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/random {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float32/alternating {'noop_with_empty_axes': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float32` / `4B` | `(1,10,30,30)` / `float32` / `36000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/random  outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/sparse {'keepdims': 1, 'noop_with_empty_axes': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/float64/alternating {'keepdims': 0} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `()` / `float64` / `8B` | `(1,10,30,30)` / `float64` / `72000B` | truth=() claim=(1, 10, 30, 30) |
| _case:_ `data(input)=BCHW/int64/alternating {'keepdims': 1} outputs=1` | | | | |
| `reduced` | `wrong-shape` | `(1,1,1,1)` / `int64` / `8B` | `(1,10,30,30)` / `int64` / `72000B` | truth=(1, 1, 1, 1) claim=(1, 10, 30, 30) |

## `Split@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: split_

- 128 cases, 8 with disagreements, 101 invalid ignored, 0 build errors
- bug classes hit: `onnx-tool-error`=8, `onnx-tool-fails-valid-model`=8

### Disagreements
#### `onnx-tool-error` (8 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=BCHW/float32/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/float64/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/int32/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/int64/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/uint16/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/uint32/sparse split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/uint32/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |

#### `onnx-tool-fails-valid-model` (8 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=BCHW/bool/random  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: list indices must be integers or slices, not NoneType |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `9000B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: list indices must be integers or slices, not NoneType |
| _case:_ `input(input)=BCHW/float32/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/float64/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/int32/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/int64/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `72008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/uint16/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `18008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/uint32/sparse split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| _case:_ `input(input)=BCHW/uint32/alternating split(init)=1d-1/int64/alternating  outputs=1` | | | | |
| _onnx-tool-error_ | `onnx-tool-error` | | | TypeError: '<' not supported between instances of 'NoneType' and 'int' |
| `<model>` | `onnx-tool-fails-valid-model` | `?` / `None` / `36008B` | `?` / `None` / `?B` | ORT executed cleanly; onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int' |

## `Atan@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Cos@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Erf@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `HardSwish@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `QuantizeLinear@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: y_zero_point_

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
| _case:_ `x(input)=BCHW/float32/sparse y_scale(init)=scalar/float32/random y_zero_point(init)=scalar/uint8/alternating {'axis': -1} outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/alternating y_scale(init)=scalar/float32/random y_zero_point(init)=scalar/int8/sparse {'axis': 0} outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/alternating y_scale(init)=scalar/float32/sparse y_zero_point(init)=scalar/int8/sparse  outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `int8` / `1B` | `()` / `int8` / `0B` | scalar dropped from accounting (true=1B) |
| _case:_ `x(input)=BCHW/float32/alternating y_scale(init)=scalar/float32/sparse y_zero_point(init)=scalar/uint8/sparse {'axis': 1} outputs=1` | | | | |
| `y_scale` | `scalar-volume` | `()` / `float32` / `4B` | `()` / `float32` / `0B` | scalar dropped from accounting (true=4B) |
| `y_zero_point` | `scalar-volume` | `()` / `uint8` / `1B` | `()` / `uint8` / `0B` | scalar dropped from accounting (true=1B) |

## `Softplus@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Transpose@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Where@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `And@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `AveragePool@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Not@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Or@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Xor@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Conv@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: B_

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

## `ConvInteger@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: x_zero_point, w_zero_point_

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

## `MatMulInteger@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: a_zero_point, b_zero_point_

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

## `RandomNormalLike@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `RandomUniformLike@16`
_Auto-generated from ONNX schema (opset 16)_

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

## `Add@16`
_Auto-generated from ONNX schema (opset 16)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Clip@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: min, max_

- 21 cases, 1 with disagreements, 19 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=3

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random min(init)=scalar/float16/random max(init)=scalar/float16/random  outputs=1` | | | | |
| `max` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `min` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |
| `output` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Equal@16`
_Auto-generated from ONNX schema (opset 16)_

- 58 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/bool/random B(input)=scalar/bool/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Greater@16`
_Auto-generated from ONNX schema (opset 16)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `GreaterOrEqual@16`
_Auto-generated from ONNX schema (opset 16)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Less@16`
_Auto-generated from ONNX schema (opset 16)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `LessOrEqual@16`
_Auto-generated from ONNX schema (opset 16)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `bool` / `1B` | `()` / `bool` / `0B` | scalar dropped from accounting (true=1B) |

## `Mul@16`
_Auto-generated from ONNX schema (opset 16)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Pow@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 1 with disagreements, 69 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=scalar/float16/random Y(input)=scalar/float16/random  outputs=1` | | | | |
| `Z` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `Sub@16`
_Auto-generated from ONNX schema (opset 16)_

- 67 cases, 1 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scalar-volume`=1

### Disagreements
#### `scalar-volume` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `A(input)=scalar/float16/random B(input)=scalar/float16/random  outputs=1` | | | | |
| `C` | `scalar-volume` | `()` / `float16` / `2B` | `()` / `float16` / `0B` | scalar dropped from accounting (true=2B) |

## `ArgMax@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 65 invalid ignored, 0 build errors

> No disagreements found.

## `BatchNormalization@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Bernoulli@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Concat@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 20 invalid ignored, 0 build errors

> No disagreements found.

## `ConcatFromSequence@16`
_Auto-generated from ONNX schema (opset 16)_

- 12 cases, 0 with disagreements, 12 invalid ignored, 0 build errors

> No disagreements found.

## `ConstantOfShape@16`
_Auto-generated from ONNX schema (opset 16)_

- 24 cases, 0 with disagreements, 24 invalid ignored, 0 build errors

> No disagreements found.

## `ConvTranspose@16`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `CumSum@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 110 invalid ignored, 0 build errors

> No disagreements found.

## `DepthToSpace@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 118 invalid ignored, 0 build errors

> No disagreements found.

## `Div@16`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `Expand@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 106 invalid ignored, 0 build errors

> No disagreements found.

## `EyeLike@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `GRU@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: B, sequence_lens, initial_h_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Gather@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 73 invalid ignored, 0 build errors

> No disagreements found.

## `GatherElements@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 93 invalid ignored, 0 build errors

> No disagreements found.

## `Gemm@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: C_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `GlobalAveragePool@16`
_Auto-generated from ONNX schema (opset 16)_

- 36 cases, 0 with disagreements, 18 invalid ignored, 0 build errors

> No disagreements found.

## `GridSample@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Hardmax@16`
_Auto-generated from ONNX schema (opset 16)_

- 108 cases, 0 with disagreements, 36 invalid ignored, 0 build errors

> No disagreements found.

## `If@16`
_Auto-generated from ONNX schema (opset 16)_

- 12 cases, 0 with disagreements, 12 invalid ignored, 0 build errors

> No disagreements found.

## `InstanceNormalization@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 35 invalid ignored, 0 build errors

> No disagreements found.

## `LRN@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 109 invalid ignored, 0 build errors

> No disagreements found.

## `LSTM@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: B, sequence_lens, initial_h, initial_c, P_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `LogSoftmax@16`
_Auto-generated from ONNX schema (opset 16)_

- 108 cases, 0 with disagreements, 0 invalid ignored, 0 build errors

> No disagreements found.

## `Loop@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: M, cond_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `LpNormalization@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 42 invalid ignored, 0 build errors

> No disagreements found.

## `MatMul@16`
_Auto-generated from ONNX schema (opset 16)_

- 83 cases, 0 with disagreements, 53 invalid ignored, 0 build errors

> No disagreements found.

## `MaxRoiPool@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `MaxUnpool@16`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `Mod@16`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `Multinomial@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `NegativeLogLikelihoodLoss@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: weight_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `NonMaxSuppression@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: max_output_boxes_per_class, iou_threshold, score_threshold_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `OneHot@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Optional@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: input_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `OptionalGetElement@16`
_Auto-generated from ONNX schema (opset 16)_

- 1 cases, 0 with disagreements, 1 invalid ignored, 0 build errors

> No disagreements found.

## `OptionalHasElement@16`
_Auto-generated from ONNX schema (opset 16)_

- 1 cases, 0 with disagreements, 1 invalid ignored, 0 build errors

> No disagreements found.

## `Pad@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: constant_value_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `QLinearConv@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: B_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `QLinearMatMul@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `RNN@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: B, sequence_lens, initial_h_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Range@16`
_Auto-generated from ONNX schema (opset 16)_

- 32 cases, 0 with disagreements, 31 invalid ignored, 0 build errors

> No disagreements found.

## `Reshape@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Resize@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: roi, scales, sizes_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `RoiAlign@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Scan@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Scatter@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `ScatterElements@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 107 invalid ignored, 0 build errors

> No disagreements found.

## `ScatterND@16`
_Auto-generated from ONNX schema (opset 16)_

- 124 cases, 0 with disagreements, 124 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceAt@16`
_Auto-generated from ONNX schema (opset 16)_

- 24 cases, 0 with disagreements, 24 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceConstruct@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceEmpty@16`
_Auto-generated from ONNX schema (opset 16)_

- 4 cases, 0 with disagreements, 4 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceErase@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: position_

- 25 cases, 0 with disagreements, 25 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceInsert@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: position_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `SequenceLength@16`
_Auto-generated from ONNX schema (opset 16)_

- 1 cases, 0 with disagreements, 1 invalid ignored, 0 build errors

> No disagreements found.

## `Slice@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: axes, steps_

- 97 cases, 0 with disagreements, 97 invalid ignored, 0 build errors

> No disagreements found.

## `Softmax@16`
_Auto-generated from ONNX schema (opset 16)_

- 108 cases, 0 with disagreements, 0 invalid ignored, 0 build errors

> No disagreements found.

## `SoftmaxCrossEntropyLoss@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: weights_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `SplitToSequence@16`
_op worker exited without result_

- 1 cases, 0 with disagreements, 0 invalid ignored, 1 build errors

### Build errors
- OP-HARNESS-ERROR: worker exited without result

## `Squeeze@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: axes_

- 128 cases, 0 with disagreements, 96 invalid ignored, 0 build errors

> No disagreements found.

## `StringNormalizer@16`
_Auto-generated from ONNX schema (opset 16)_

- 24 cases, 0 with disagreements, 24 invalid ignored, 0 build errors

> No disagreements found.

## `TfIdfVectorizer@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Tile@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.

## `Trilu@16`
_Auto-generated from ONNX schema (opset 16). Optional inputs: k_

- 128 cases, 0 with disagreements, 92 invalid ignored, 0 build errors

> No disagreements found.

## `Unsqueeze@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 87 invalid ignored, 0 build errors

> No disagreements found.

## `Upsample@16`
_Auto-generated from ONNX schema (opset 16)_

- 128 cases, 0 with disagreements, 128 invalid ignored, 0 build errors

> No disagreements found.
