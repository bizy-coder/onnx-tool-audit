# onnx_tool audit report
_generated 2026-04-28T21:50:47_

**2 ops, 230 test cases, 71 with disagreements, 95 invalid ignored, 0 build errors.**

## Bug class totals

| class | count |
|---|---|
| `scorer-wrong-shape` | 260 |
| `scorer-missing-tensor` | 11 |

## Per-op summary

| op | cases | disagreements | invalid | build-errors | notes |
|---|---|---|---|---|---|
| [`BatchNormalization@11`](#batchnormalization@11) | 128 | 65 | 0 | 0 | Auto-generated from ONNX schema (opset 11) |
| [`Clip@11`](#clip@11) | 102 | 6 | 95 | 0 | Auto-generated from ONNX schema (opset 11). Optional inputs: min, max |

## `BatchNormalization@11`
_Auto-generated from ONNX schema (opset 11)_

- 128 cases, 65 with disagreements, 0 invalid ignored, 0 build errors
- bug classes hit: `scorer-wrong-shape`=260

### Disagreements
#### `scorer-wrong-shape` (65 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `X(input)=BCHW/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 1.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/alternating scale(input)=1d-10/float16/alternating B(input)=1d-10/float16/alternating mean(input)=1d-10/float16/alternating var(input)=1d-10/float16/alternating {'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=B-1-H-1/float16/random scale(input)=1d-1/float16/random B(input)=1d-1/float16/random mean(input)=1d-1/float16/random var(input)=1d-1/float16/random {'epsilon': 0.0, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(1)` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | ORT=(1,) SI=(1, 1, 30, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(1)` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | ORT=(1,) SI=(1, 1, 30, 1) |
| `saved_var` | `scorer-wrong-shape` | `(1)` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | ORT=(1,) SI=(1, 1, 30, 1) |
| `var_out` | `scorer-wrong-shape` | `(1)` / `float16` / `2B` | `(1,1,30,1)` / `float16` / `60B` | ORT=(1,) SI=(1, 1, 30, 1) |
| _case:_ `X(input)=BCHW/float32/sparse scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.5, 'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,30,30)` / `float32` / `36000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float64/random scale(input)=1d-10/float64/sparse B(input)=1d-10/float64/random mean(input)=1d-10/float64/random var(input)=1d-10/float64/random {'epsilon': 1.0, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,30,30)` / `float64` / `72000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,30,30)` / `float64` / `72000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,30,30)` / `float64` / `72000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,30,30)` / `float64` / `72000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=B-C-1-1/float16/sparse scale(input)=1d-10/float16/sparse B(input)=1d-10/float16/sparse mean(input)=1d-10/float16/sparse var(input)=1d-10/float16/sparse {'epsilon': 1.0, 'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,1,1)` / `float16` / `20B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,1,1)` / `float16` / `20B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,1,1)` / `float16` / `20B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,1,1)` / `float16` / `20B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float32/alternating scale(input)=1d-10/float32/sparse B(input)=1d-10/float32/sparse mean(input)=1d-10/float32/sparse var(input)=1d-10/float32/sparse {'epsilon': 0.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float64/sparse scale(input)=1d-10/float64/alternating B(input)=1d-10/float64/sparse mean(input)=1d-10/float64/alternating var(input)=1d-10/float64/sparse {'epsilon': 1.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float64` / `80B` | `(1,10,1,1)` / `float64` / `80B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.5} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 1.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.0, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.0, 'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 0.5, 'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=B-C-1-1/float32/random scale(input)=1d-10/float32/random B(input)=1d-10/float32/random mean(input)=1d-10/float32/random var(input)=1d-10/float32/random {'epsilon': 1.0, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float32` / `40B` | `(1,10,1,1)` / `float32` / `40B` | ORT=(10,) SI=(1, 10, 1, 1) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random  outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'epsilon': 0.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'momentum': 1.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'epsilon': 0.5, 'momentum': 0.0} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| _case:_ `X(input)=BCHW/float16/random scale(input)=1d-10/float16/random B(input)=1d-10/float16/random mean(input)=1d-10/float16/random var(input)=1d-10/float16/random {'epsilon': 0.5, 'momentum': 0.5} outputs=11111` | | | | |
| `mean_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_mean` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `saved_var` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| `var_out` | `scorer-wrong-shape` | `(10)` / `float16` / `20B` | `(1,10,30,30)` / `float16` / `18000B` | ORT=(10,) SI=(1, 10, 30, 30) |
| ... | _+45 more cases_ | | | |

## `Clip@11`
_Auto-generated from ONNX schema (opset 11). Optional inputs: min, max_

- 102 cases, 6 with disagreements, 95 invalid ignored, 0 build errors
- bug classes hit: `scorer-missing-tensor`=11

### Disagreements
#### `scorer-missing-tensor` (6 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `input(input)=scalar/float16/random min(init)=scalar/float16/random max(init)=scalar/float16/random  outputs=1` | | | | |
| `max` | `scorer-missing-tensor` | `()` / `float16` / `2B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float16 bytes=2) |
| `min` | `scorer-missing-tensor` | `()` / `float16` / `2B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float16 bytes=2) |
| _case:_ `input(input)=BCHW/float16/sparse min(init)=scalar/float16/alternating max(init)=scalar/float16/random  outputs=1` | | | | |
| `max` | `scorer-missing-tensor` | `()` / `float16` / `2B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float16 bytes=2) |
| `min` | `scorer-missing-tensor` | `()` / `float16` / `2B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float16 bytes=2) |
| _case:_ `input(input)=BCHW/float32/sparse min(init)=scalar/float32/random max(init)=scalar/float32/random  outputs=1` | | | | |
| `max` | `scorer-missing-tensor` | `()` / `float32` / `4B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float32 bytes=4) |
| `min` | `scorer-missing-tensor` | `()` / `float32` / `4B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float32 bytes=4) |
| _case:_ `input(input)=BCHW/float32/alternating min(init)=scalar/float32/sparse max(init)=scalar/float32/sparse  outputs=1` | | | | |
| `max` | `scorer-missing-tensor` | `()` / `float32` / `4B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float32 bytes=4) |
| `min` | `scorer-missing-tensor` | `()` / `float32` / `4B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float32 bytes=4) |
| _case:_ `input(input)=B-C-1-1/float16/sparse min(init)=scalar/float16/random max(init)=scalar/float16/sparse  outputs=1` | | | | |
| `max` | `scorer-missing-tensor` | `()` / `float16` / `2B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float16 bytes=2) |
| `min` | `scorer-missing-tensor` | `()` / `float16` / `2B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float16 bytes=2) |
| _case:_ `input(input)=B-C-1-1/float32/random min(init)=scalar/float32/alternating  outputs=1` | | | | |
| `min` | `scorer-missing-tensor` | `()` / `float32` / `4B` | `?` / `None` / `?B` | shape_inference omits tensor (ORT: shape=() dtype=float32 bytes=4) |
