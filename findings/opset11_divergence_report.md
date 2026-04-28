# onnx_tool 1.0.1 vs onnxruntime — Opset 11 Divergence Report

Generated: 2026-04-28
Source data: `all_ops_opset11_bugs.md` (46 distinct bugs, 1,036 surface findings)

## Methodology

Each test case runs a model through two oracles:

- **onnxruntime (ORT)**: executes the model. If ORT rejects or fails the model, the case is discarded — an unrunnable model is irrelevant.
- **onnx_tool**: statically profiles the same model for MACs, memory, and parameter counts.

Only cases where ORT succeeds are recorded. Divergences fall into three classes:

| Class | Meaning | Competition impact |
|---|---|---|
| `onnx-tool-fails-valid-model` | onnx_tool throws an exception on a model ORT accepts | Model cannot be scored at all |
| `wrong-shape` | onnx_tool infers a different output shape than ORT produces | Wrong memory byte count in the score |
| `wrong-dtype` | onnx_tool infers a different output dtype than ORT produces | Wrong byte width used in memory calculation |

---

## Section 1 — Silent Miscounting: scalar-volume

**Affects 55 ops, 192 surface findings.**

`onnx_tool` reports 0 bytes for any tensor whose shape is `()` (a scalar). The correct value is `1 × sizeof(dtype)` — 1 byte for bool, 2 for float16, 4 for float32/int32, 8 for float64/int64.

**Root cause:** onnx_tool's internal volume function computes `product([]) = 0` instead of 1. All scalar-output tensors are therefore invisible to memory accounting.

**Repro:**
```
Op: Constant, value = float32 scalar
ORT:        shape=(), dtype=float32, bytes=4
onnx_tool:  shape=(), dtype=float32, bytes=0
```

**All affected ops:** `Abs`, `Add`, `And`, `Atan`, `Ceil`, `Clip`, `Constant`, `Conv`, `Cos`,
`DequantizeLinear`, `Div`, `Dropout`, `Elu`, `Equal`, `Erf`, `Exp`, `Floor`, `Greater`,
`HardSigmoid`, `Identity`, `LeakyRelu`, `Less`, `Log`, `MatMulInteger`, `Max`, `Min`,
`Mod`, `Mul`, `Neg`, `Not`, `Or`, `PRelu`, `Pow`, `QuantizeLinear`, `RandomNormalLike`,
`RandomUniformLike`, `Reciprocal`, `ReduceL2`, `ReduceMax`, `ReduceMean`, `ReduceMin`,
`ReduceProd`, `ReduceSum`, `Relu`, `Sigmoid`, `Sign`, `Sin`, `Softplus`, `Sqrt`, `Squeeze`,
`Sub`, `Sum`, `Tanh`, `Transpose`, `Xor`

**Fix:** In onnx_tool's volume utility, return 1 for an empty dimension list:
```python
def volume(dims):
    if len(dims) == 0:
        return 1
    result = 1
    for d in dims: result *= d
    return result
```

---

## Section 2 — Crashes: `onnx-tool-fails-valid-model`

ORT executes these models successfully. onnx_tool throws an exception, making scoring impossible.

### 2A — `NotImplementedError: has no value_infer` (dominant crash pattern)

onnx_tool's `Node.shape_infer()` unconditionally calls `value_infer()`. Any op not registered for value inference crashes with `NotImplementedError`. This is triggered regardless of input shape — even the simplest single-node model using these ops will fail scoring.

| Op | Surface findings | Error |
|---|---|---|
| `IsInf@11` | 128 | `NotImplementedError: this Node IsInf-IsInf_0 has no value_infer` |
| `Size@11` | 128 | `NotImplementedError: this Node Size-Size_0 has no value_infer` |
| `ArgMin@11` | 63 | `NotImplementedError: this Node ArgMin-ArgMin_0 has no value_infer` |
| `ThresholdedRelu@11` | 42 | `NotImplementedError: this Node ThresholdedRelu-ThresholdedRelu_0 has no value_infer` |
| `Selu@11` | 40 | `NotImplementedError: this Node Selu-Selu_0 has no value_infer` |
| `GlobalLpPool@11` | 36 | `NotImplementedError: this Node GlobalLpPool-GlobalLpPool_0 has no value_infer` |
| `IsNaN@11` | 36 | `NotImplementedError: this Node IsNaN-IsNaN_0 has no value_infer` |
| `MeanVarianceNormalization@11` | 36 | `NotImplementedError: this Node MeanVarianceNormalization-MeanVarianceNormalization_0 has no value_infer` |
| `LpPool@11` | 23 | `NotImplementedError: this Node LpPool-LpPool_0 has no value_infer` |
| `ReduceL1@11` | 19 | `NotImplementedError: this Node ReduceL1-ReduceL1_0 has no value_infer` |
| `ReduceLogSum@11` | 19 | `NotImplementedError: this Node ReduceLogSum-ReduceLogSum_0 has no value_infer` |
| `ReduceLogSumExp@11` | 19 | `NotImplementedError: this Node ReduceLogSumExp-ReduceLogSumExp_0 has no value_infer` |
| `ReduceSumSquare@11` | 19 | `NotImplementedError: this Node ReduceSumSquare-ReduceSumSquare_0 has no value_infer` |
| `Acos@11` | 12 | `NotImplementedError: this Node Acos-Acos_0 has no value_infer` |
| `Acosh@11` | 12 | `NotImplementedError: this Node Acosh-Acosh_0 has no value_infer` |
| `Asin@11` | 12 | `NotImplementedError: this Node Asin-Asin_0 has no value_infer` |
| `Asinh@11` | 12 | `NotImplementedError: this Node Asinh-Asinh_0 has no value_infer` |
| `Atanh@11` | 12 | `NotImplementedError: this Node Atanh-Atanh_0 has no value_infer` |
| `Cosh@11` | 12 | `NotImplementedError: this Node Cosh-Cosh_0 has no value_infer` |
| `DynamicQuantizeLinear@11` | 12 | `NotImplementedError: this Node DynamicQuantizeLinear-DynamicQuantizeLinear_0 has no value_infer` |
| `Mean@11` | 12 | `NotImplementedError: this Node Mean-Mean_0 has no value_infer` |
| `Sinh@11` | 12 | `NotImplementedError: this Node Sinh-Sinh_0 has no value_infer` |
| `Softsign@11` | 12 | `NotImplementedError: this Node Softsign-Softsign_0 has no value_infer` |
| `Tan@11` | 12 | `NotImplementedError: this Node Tan-Tan_0 has no value_infer` |
| `GlobalMaxPool@11` | 9 | `NotImplementedError: this Node GlobalMaxPool-GlobalMaxPool_0 has no value_infer` |
| `Det@11` | 6 | `NotImplementedError: this Node Det-Det_0 has no value_infer` |
| `Shrink@11` | 6 | `NotImplementedError: this Node Shrink-Shrink_0 has no value_infer` |
| `ReverseSequence@11` | 4 | `NotImplementedError: this Node ReverseSequence-ReverseSequence_0 has no value_infer` |

**Fix pattern for all of the above:** Register a `value_infer` method for each op. For elementwise/passthrough ops the stub can be a no-op (shape is already set by `shape_infer`). For ops with non-trivial output shapes, the correct shape must be computed.

| Op type | Required `value_infer` behavior |
|---|---|
| Elementwise unary (Acos, Acosh, Asin, Asinh, Atanh, Cosh, IsNaN, Selu, Shrink, Sinh, Softsign, Tan, ThresholdedRelu) | Passthrough: output shape and dtype = input |
| Elementwise n-ary (Mean, MeanVarianceNormalization) | Passthrough: same shape/dtype as inputs |
| Reduction (GlobalLpPool, GlobalMaxPool) | Output shape = `[N, C, 1, 1]` |
| Reduction (LpPool) | Output shape follows kernel/stride/padding, same as AveragePool |
| Reduction (ReduceL1, ReduceLogSum, ReduceLogSumExp, ReduceSumSquare) | Apply axes + keepdims to input shape, same dtype |
| ArgMin | Same shape logic as ArgMax; output dtype = int64 |
| IsInf | Same shape as input; output dtype = bool |
| Size | Output shape = `()`; output dtype = int64 |
| Det | Output shape = input shape with last two dims removed |
| ReverseSequence | Passthrough: same shape/dtype as input |
| DynamicQuantizeLinear | Three outputs: quantized uint8 (same shape), scale scalar float32, zero_point scalar uint8 |

---

### 2B — `Compress@11` — ValueError on multi-dimensional condition

**Surface findings:** 16

**Error:** `ValueError: condition must be a 1-d array`

**Root cause:** The ONNX spec for Compress permits any shape for the `condition` input — it is applied after implicit flattening. onnx_tool passes the condition tensor directly to `np.nonzero()`, which requires exactly 1-D input. ORT handles multi-dimensional conditions correctly.

**Repro:**
```
Op: Compress, input=[1,10,1,1]/bool, condition=[1,10,1,1]/bool
ORT:       runs successfully, bytes=10
onnx_tool: ValueError: condition must be a 1-d array
```

**Fix:**
```python
condition_flat = condition.flatten()
indices = np.nonzero(condition_flat)[0]
```

---

### 2C — `NonZero@11` — ValueError on scalar input

**Surface findings:** 14

**Error:** `ValueError: Calling nonzero on 0d arrays is not allowed. Use np.atleast_1d(scalar).nonzero() instead.`

**Root cause:** ORT accepts scalar inputs to NonZero per spec. onnx_tool passes the input directly to `np.nonzero()`, which rejects 0-D arrays in NumPy.

**Repro:**
```
Op: NonZero, X=scalar/bool
ORT:       runs successfully, bytes=8
onnx_tool: ValueError: Calling nonzero on 0d arrays is not allowed
```

**Fix:**
```python
x = np.atleast_1d(x)
result = np.nonzero(x)
```

---

### 2D — `Constant@11` — AttributeError on raw int/float value attribute

**Surface findings:** 3

**Error:** `AttributeError: 'int' object has no attribute 'shape'`

**Root cause:** The ONNX spec allows Constant's `value` attribute to be encoded as a raw scalar (int or float) in addition to a TensorProto. onnx_tool's Constant handler calls `.shape` on the attribute value, assuming it is always a TensorProto or numpy array. Raw int/float attributes crash.

**Repro:**
```
Op: Constant, attrs={'value': 0}  (raw int, not TensorProto)
ORT:       shape=None, bytes=8
onnx_tool: AttributeError: 'int' object has no attribute 'shape'
```

**Fix:**
```python
val = node.attrs.get('value')
if isinstance(val, (int, float)):
    val = np.array(val, dtype=np.float32)
# then use val.shape, val.dtype normally
```

---

### 2E — `TopK@11` — TypeError when K is a runtime input

**Surface findings:** 2

**Error:** `TypeError: '<' not supported between instances of 'NoneType' and 'int'`

**Root cause:** At opset 11+, K is passed as a tensor input rather than an attribute. When K is a runtime (non-static) input, onnx_tool cannot resolve its value statically and returns `None`. The shape inference code then attempts `None < input_shape[axis]`, which fails in Python 3.

**Repro:**
```
Op: TopK, X=[1,10,30,30]/float16, K=runtime input
ORT:       runs successfully
onnx_tool: TypeError: '<' not supported between instances of 'NoneType' and 'int'
```

**Fix:** Guard the comparison:
```python
k_val = try_get_const_value(k_tensor)  # returns None if not a static initializer
if k_val is not None:
    out_dim = min(int(k_val), input_shape[axis])
else:
    out_dim = None  # unknown statically
```

---

### 2F — `Split@11` — TypeError when `split` attribute is absent

**Surface findings:** 1

**Error:** `TypeError: list indices must be integers or slices, not NoneType`

**Root cause:** When the `split` attribute is omitted, Split divides the input equally among `num_outputs` outputs (inferred from the number of output names). onnx_tool attempts to index a list using the missing `split` value directly, which is `None`.

**Repro:**
```
Op: Split, input=[1,10,30,30]/bool, no split attr, 1 output
ORT:       runs successfully, bytes=9000
onnx_tool: TypeError: list indices must be integers or slices, not NoneType
```

**Fix:**
```python
split_sizes = node.attrs.get('split')
if split_sizes is None:
    total = input_shape[axis]
    n = len(node.outputs)
    split_sizes = [total // n] * n
```

---

## Section 3 — Wrong Shape (silent miscounting)

onnx_tool infers a different output shape than ORT produces. This results in a wrong byte count in memory accounting. The magnitude of the error depends on how far the shapes diverge.

### 3A — `Pow@11` — broadcast shape wrong

**Surface findings:** 7

**Direction: Undercount**

**Repro:**
```
Op: Pow, X=[1,10,1,1]/float16, Y=[1,1,30,1]/float16
ORT:       shape=(1,10,30,1), bytes=600
onnx_tool: shape=(1,1,30,1),  bytes=60   ← 10× undercount
```

**Root cause:** onnx_tool's Pow shape inference takes one input's shape rather than computing the true numpy-style broadcast result. With `B-C-1-1` × `B-1-H-1` inputs, the correct broadcast is `B-C-H-1`; onnx_tool returns one of the input shapes.

**Fix:** Apply full broadcast shape derivation:
```python
def broadcast_shape(a, b):
    ndim = max(len(a), len(b))
    a = [1]*(ndim-len(a)) + list(a)
    b = [1]*(ndim-len(b)) + list(b)
    return [max(x, y) for x, y in zip(a, b)]
```

---

### 3B — `MaxPool@11` — indices (second) output shape wrong

**Surface findings:** 4

**Direction: Undercount**

**Repro:**
```
Op: MaxPool, kernel=[1,1], X=[1,10,1,1]/float16, pads=[0,0,0,0]
Second output (Indices):
ORT:       shape=(1,10,1,1), dtype=int64, bytes=80
onnx_tool: shape=(),         dtype=int64, bytes=0   ← completely absent from accounting
```

**Root cause:** onnx_tool collapses the indices output to scalar `()`. The scalar-volume bug then reports 0 bytes. The indices output shape must equal the primary output shape.

**Fix:** Propagate the primary output shape to the second output in MaxPool's shape inference handler.

---

### 3C — `Flatten@11` with `axis=-1` — output dimensions transposed

**Surface findings:** 3

**Direction: Byte-count equal, shape wrong**

**Repro:**
```
Op: Flatten, axis=-1, X=[1,10,1,1]/bool
ORT:       shape=(10,1), bytes=10
onnx_tool: shape=(1,10), bytes=10   ← same bytes, wrong shape
```

**Root cause:** Negative axis is not normalized before computing the flatten split point. `axis=-1` on a rank-4 tensor should resolve to `axis=3`, yielding outer product `1×10×1=10` and inner product `1=1`. onnx_tool appears to use axis=1 or similar.

**Fix:**
```python
rank = len(input_shape)
axis = axis if axis >= 0 else rank + axis
outer = int(np.prod(input_shape[:axis])) if axis > 0 else 1
inner = int(np.prod(input_shape[axis:]))
out_shape = [outer, inner]
```

---

### 3D — `PRelu@11` — broadcast shape wrong

**Surface findings:** 3

**Direction: Undercount**

**Repro:**
```
Op: PRelu, X=[1,10,1,1]/float16, slope=[1,1,30,1]/float16
ORT:       shape=(1,10,30,1), bytes=600
onnx_tool: shape=(1,1,30,1),  bytes=60   ← 10× undercount
```

Same root cause as Bug 30 (Pow). The broadcast shape fix above applies identically.

---

### 3E — `Squeeze@11` with no `axes` attribute — singleton dims not removed

**Surface findings:** 3

**Direction: Byte-count equal, shape wrong**

**Repro:**
```
Op: Squeeze, X=[1,10,1,1]/bool, no axes attr
ORT:       shape=(10,), bytes=10
onnx_tool: shape=(10,1,1), bytes=10   ← same bytes, wrong shape
```

**Root cause:** When `axes` is absent, Squeeze must remove all dimensions of size 1. onnx_tool only partially removes them (removes the batch dim but leaves trailing `1,1`).

**Fix:**
```python
if axes is None or len(axes) == 0:
    out_shape = [d for d in input_shape if d != 1]
```

---

### 3F — `ReduceMax@11` — wrong output shape with default attrs on singleton-dimension input

**Surface findings:** 2

**Direction: Undercount (compounded with scalar-volume)**

**Repro:**
```
Op: ReduceMax, X=[1,1,30,1]/float16, no attrs (default: keepdims=1, all axes)
ORT:       shape=(1,1,1,1), bytes=2
onnx_tool: shape=(),        bytes=0   ← scalar-volume compounds: 0 instead of 2
```

**Root cause:** When no `axes` are specified and `keepdims=1` (the default), reducing all axes should produce an all-ones tensor of the same rank. onnx_tool collapses to `()`.

**Fix:**
```python
if axes is None:
    reduced_axes = set(range(len(input_shape)))
else:
    reduced_axes = set(axes)

if keepdims:
    out_shape = [1 if i in reduced_axes else d for i, d in enumerate(input_shape)]
else:
    out_shape = [d for i, d in enumerate(input_shape) if i not in reduced_axes]
```

---

### 3G — `ReduceMean@11` — same as 3F

**Surface findings:** 2
Identical repro and root cause to ReduceMax. Same fix applies.

---

### 3H — `ReduceMin@11` — same as 3F

**Surface findings:** 2
Identical repro and root cause to ReduceMax. Same fix applies.

---

### 3I — `ReduceProd@11` — same as 3F

**Surface findings:** 2
Identical repro and root cause to ReduceMax. Same fix applies.

---

### 3J — `ReduceSum@11` — same as 3F

**Surface findings:** 2
Identical repro and root cause to ReduceMax. Same fix applies.

---

## Section 4 — Wrong Dtype (silent miscounting)

onnx_tool infers a different output dtype than ORT produces. Wrong dtype means wrong byte width, which produces wrong memory byte counts.

### 4A — `Round@11` — output dtype reported as `bool` instead of `float16`

**Surface findings:** 12 (all scalar inputs; also triggers scalar-volume)

**Repro:**
```
Op: Round, X=scalar/float16
ORT:       shape=(), dtype=float16, bytes=2
onnx_tool: shape=(), dtype=bool,    bytes=0   ← wrong dtype AND scalar-volume
```

**Root cause:** Two bugs compound. First, onnx_tool's Round dtype inference incorrectly assigns `bool` as the output dtype instead of passing through the input dtype. Second, scalar-volume then reports 0 bytes for the (wrongly-typed) scalar. The dtype error is independent of the scalar-volume bug.

**Fix:** Round's output dtype must equal its input dtype:
```python
outtensors[0].dtype = intensors[0].dtype
```

---

### 4B — `Constant@11` with both `value` and `sparse_value` — dtype priority wrong

**Surface findings:** 1

**Repro:**
```
Op: Constant, attrs={'value': TensorProto(float32), 'sparse_value': 0}
ORT:       shape=(), dtype=int64, bytes=8
onnx_tool: shape=(), dtype=float32, bytes=0   ← wrong dtype AND scalar-volume
```

**Root cause:** When both `value` and `sparse_value` are present, onnx_tool reads `value`'s dtype (float32) and ignores `sparse_value`. ORT gives `sparse_value` precedence and outputs int64.

**Fix:** In onnx_tool's Constant handler, check `sparse_value` before `value`:
```python
if 'sparse_value' in node.attrs:
    # use sparse_value's dtype and shape
elif 'value' in node.attrs:
    # use value's dtype and shape
```

---

## Summary Table

| # | Op | Class | Findings | Direction | Root cause |
|---|---|---|---|---|---|
| 1 | 55 ops | scalar-volume | 192 | Undercount (0 bytes for scalars) | `volume([]) = 0` instead of 1 |
| 2 | IsInf | crash | 128 | N/A | No `value_infer` registered |
| 3 | Size | crash | 128 | N/A | No `value_infer` registered |
| 4 | ArgMin | crash | 63 | N/A | No `value_infer` registered |
| 5 | ThresholdedRelu | crash | 42 | N/A | No `value_infer` registered |
| 6 | Selu | crash | 40 | N/A | No `value_infer` registered |
| 7 | GlobalLpPool | crash | 36 | N/A | No `value_infer` registered |
| 8 | IsNaN | crash | 36 | N/A | No `value_infer` registered |
| 9 | MeanVarianceNormalization | crash | 36 | N/A | No `value_infer` registered |
| 10 | LpPool | crash | 23 | N/A | No `value_infer` registered |
| 11 | ReduceL1 | crash | 19 | N/A | No `value_infer` registered |
| 12 | ReduceLogSum | crash | 19 | N/A | No `value_infer` registered |
| 13 | ReduceLogSumExp | crash | 19 | N/A | No `value_infer` registered |
| 14 | ReduceSumSquare | crash | 19 | N/A | No `value_infer` registered |
| 15 | Compress | crash | 16 | N/A | `np.nonzero` rejects multi-dim condition |
| 16 | NonZero | crash | 14 | N/A | `np.nonzero` rejects 0-D input |
| 17 | Acos | crash | 12 | N/A | No `value_infer` registered |
| 18 | Acosh | crash | 12 | N/A | No `value_infer` registered |
| 19 | Asin | crash | 12 | N/A | No `value_infer` registered |
| 20 | Asinh | crash | 12 | N/A | No `value_infer` registered |
| 21 | Atanh | crash | 12 | N/A | No `value_infer` registered |
| 22 | Cosh | crash | 12 | N/A | No `value_infer` registered |
| 23 | DynamicQuantizeLinear | crash | 12 | N/A | No `value_infer` registered |
| 24 | Mean | crash | 12 | N/A | No `value_infer` registered |
| 25 | Sinh | crash | 12 | N/A | No `value_infer` registered |
| 26 | Softsign | crash | 12 | N/A | No `value_infer` registered |
| 27 | Tan | crash | 12 | N/A | No `value_infer` registered |
| 28 | Round | wrong-dtype | 12 | Undercount (wrong width + scalar-volume) | Output dtype set to bool instead of passthrough |
| 29 | GlobalMaxPool | crash | 9 | N/A | No `value_infer` registered |
| 30 | Pow | wrong-shape | 7 | Undercount | Broadcast shape uses one input instead of numpy rules |
| 31 | Det | crash | 6 | N/A | No `value_infer` registered |
| 32 | Shrink | crash | 6 | N/A | No `value_infer` registered |
| 33 | ReverseSequence | crash | 4 | N/A | No `value_infer` registered |
| 34 | MaxPool | wrong-shape | 4 | Undercount | Indices output shape collapsed to scalar |
| 35 | Constant | crash | 3 | N/A | `.shape` called on raw int attribute |
| 36 | Flatten | wrong-shape | 3 | Shape wrong, bytes equal | Negative axis not normalized |
| 37 | PRelu | wrong-shape | 3 | Undercount | Same broadcast bug as Pow |
| 38 | Squeeze | wrong-shape | 3 | Shape wrong, bytes equal | Incomplete removal of size-1 dims when axes absent |
| 39 | TopK | crash | 2 | N/A | `None < int` comparison when K not static |
| 40 | ReduceMax | wrong-shape | 2 | Undercount (+ scalar-volume) | keepdims=1 all-axes collapse to `()` |
| 41 | ReduceMean | wrong-shape | 2 | Undercount (+ scalar-volume) | Same as ReduceMax |
| 42 | ReduceMin | wrong-shape | 2 | Undercount (+ scalar-volume) | Same as ReduceMax |
| 43 | ReduceProd | wrong-shape | 2 | Undercount (+ scalar-volume) | Same as ReduceMax |
| 44 | ReduceSum | wrong-shape | 2 | Undercount (+ scalar-volume) | Same as ReduceMax |
| 45 | Split | crash | 1 | N/A | `None` used as list index when split attr absent |
| 46 | Constant | wrong-dtype | 1 | Wrong byte width (+ scalar-volume) | sparse_value dtype priority wrong |

---

## ORT-side bug (not onnx_tool)

`SplitToSequence@11` — ORT does not finish executing within the 10-second per-case timeout. Not an onnx_tool issue.
