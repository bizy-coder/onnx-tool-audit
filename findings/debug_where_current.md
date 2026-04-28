# onnx_tool audit report
_generated 2026-04-28T18:58:34_

**1 ops, 70 test cases, 4 with disagreements, 32 invalid ignored, 0 build errors.**

## Bug class totals

| class | count |
|---|---|
| `wrong-shape` | 4 |

## Per-op summary

| op | cases | disagreements | invalid | build-errors | notes |
|---|---|---|---|---|---|
| [`Where@11`](#where@11) | 70 | 4 | 32 | 0 | Auto-generated from ONNX schema (opset 11) |

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
