# onnx_tool audit report
_generated 2026-04-28T02:17:28_

**1 ops, 24 test cases, 2 with disagreements, 0 build errors.**

## Bug class totals

| class | count |
|---|---|
| `wrong-shape` | 1 |
| `constant-uncounted` | 1 |

## Per-op summary

| op | cases | disagreements | build-errors | notes |
|---|---|---|---|---|
| [`DAG`](#dag) | 24 | 2 | 0 | Phase 2 multi-op DAGs (24 cases: scenarios+20 random target_nodes=4) |

## `DAG`
_Phase 2 multi-op DAGs (24 cases: scenarios+20 random target_nodes=4)_

- 24 cases, 2 with disagreements, 0 build errors
- bug classes hit: `wrong-shape`=1, `constant-uncounted`=1

### Disagreements
#### `constant-uncounted` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `Constant -> Add` | | | | |
| `c` | `constant-uncounted` | `(1,10,30,30)` / `float32` / `36000B` | `(1,10,30,30)` / `float32` / `36000B` | node  memory=0 ignores produced tensor (true=36000B) |

#### `wrong-shape` (1 cases)

| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |
|---|---|---|---|---|
| _case:_ `Cast(bool) -> Compress[axis=1]` | | | | |
| `out` | `wrong-shape` | `(1,5,30,30)` / `float32` / `18000B` | `(1,0,30,30)` / `float32` / `0B` | truth=(1, 5, 30, 30) claim=(1, 0, 30, 30) |
