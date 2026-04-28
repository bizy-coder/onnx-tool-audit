# onnx_tool audit harness

Differential test harness for `onnx_tool 1.0.1`. For every op (and every
multi-op DAG) we exercise, two oracles run on the same model and the harness
diffs their outputs:

| Oracle             | What it provides                              | Trust level   |
|--------------------|-----------------------------------------------|---------------|
| onnxruntime (ORT)  | Real shapes/dtypes/sizes via execution        | Ground truth  |
| `onnx_tool`        | Static-inferred shapes + memory + MAC counts  | Suspect       |

The truth oracle promotes every node output to a graph output, disables
optimizations, and reads the actual numpy arrays each kernel produces. The
suspect oracle profiles the same model with `onnx_tool.Model.profile()`. The
diff is per-tensor and per-node.

## What it found (last run)

90 ops × 2715 test cases → **379 disagreements** classified across 6 bug
classes:

| class                 | count |  meaning |
|-----------------------|-------|----------|
| `scalar-volume`       | 187   | shape `()` scalars reported as 0 bytes (`volume([]) == 0` bug) |
| `ort-error`           | 164   | mostly invalid generator combos for one op (Pad needs more gating) |
| `onnx-tool-error`     |  67   | onnx_tool throws on certain shape/dtype combos |
| `wrong-shape`         |  37   | broadcast `_max_shape` heuristic gets the output shape wrong |
| `constant-uncounted`  |   4   | Constant outputs are not added to the memory total |
| `wrong-dtype`         |   2   | declared output dtype disagrees with kernel output dtype (QLinearConv) |

Bugs the harness is built to detect (and the test that proves it):

| bug                                              | regression test                                |
|--------------------------------------------------|------------------------------------------------|
| `volume([]) == 0` for scalars                    | `test_scalar_volume_via_identity`              |
| `_max_shape` broadcast heuristic                 | `test_max_shape_via_where`                     |
| Constant outputs not counted                     | `test_constant_uncounted`                      |
| `Tensor.get_numpy()` zero-fabrication            | `test_compress_get_numpy_zero_fabrication`     |

Run all four:

```bash
python -m onnx_tool_audit.tests.test_known_bugs
```

## Architecture

```
README.md             — this file
__init__.py           — package marker
__main__.py           — CLI: `python -m onnx_tool_audit run [...]`
generators.py         — primitive sweeps (shapes, dtypes, fill patterns)
op_specs.py           — declarative spec table (89 catalog ops + Constant)
oracles.py            — ORT all-outputs runner + onnx_tool profiler + per-tensor diff
harness.py            — Phase 1 single-op orchestration
dag_generator.py      — Phase 2 multi-op DAGs (random + bug-targeted scenarios)
shrinker.py           — delta-debugging for failing DAGs
report.py             — markdown report rendering
findings/report.md    — output (overwritten on each run)
findings/run.log      — full progress log
tests/test_known_bugs.py — regression suite for the four known bugs
```

## Usage

```bash
# Full sweep: 89 ops × ~30 cases each, plus 200 random DAGs + 4 scenarios
python -m onnx_tool_audit run

# Phase 1 only (single-op)
python -m onnx_tool_audit run --no-dag

# Phase 2 only (DAGs)
python -m onnx_tool_audit run --dag-only

# Single op
python -m onnx_tool_audit run --op Where

# More aggressive DAG sweep
python -m onnx_tool_audit run --dag-count 1000 --dag-nodes 6
```

## Two phases

**Phase 1 — single-op sweep.** Each spec in `op_specs.py` declares input shape
candidates, dtype candidates, fill patterns, and attribute grids. The harness
expands the cartesian product, capped at 64 cases per op, builds a one-node
ONNX model per case, runs both oracles, and per-tensor diffs the results.
Catches bugs whose root cause is local to the op: shape inference, scalar
volume accounting, dtype tracking, MAC formulas.

**Phase 2 — multi-op DAGs.** Random small graphs (3–6 nodes) are generated
using a frontier-based picker (`dag_generator.PLANNERS`), with shape
propagation grounded by an ORT speculative run after each step. We also
include a small set of **bug-targeted scenarios** — hand-written sequences
known to trigger specific bugs (e.g. `Cast(bool) -> Compress` for
`get_numpy()` zero fabrication). Catches bugs that only manifest under data
flow between ops.

## Adding ops

Drop a new entry into `op_specs.SPECS`:

```python
"NewOp": OpSpec(
    name="NewOp",
    inputs=(InputPort("X", shape_labels=("BCHW",), dtype_labels=("float32",)),),
    attrs={"axis": (1, 2, 3)},
    notes="why we test this",
),
```

For ops fitting common patterns, use the helpers `unary_op`, `binary_broadcast_op`,
`bool_binary_op`, `reduce_op`, `pool_op`.

For ops needing input-shape constraints (like Compress's condition length),
add a case to `_apply_input_constraints` in `harness.py`.

For ops that need a specific opset, pass `opset=N` to `OpSpec` (most ops are
fine on opset 11; comparison ops added in opset 12+ need explicit bumps —
e.g. `GreaterOrEqual`, `LessOrEqual`, `NotEqual`).

## Known limitations

1. **MAC counting** is not directly diff-tested. ORT exposes no FLOP counts.
   We can sanity-check onnx_tool's MAC formulas by hand against a small per-op
   table; that's a separate workstream.

2. **Coverage of input space**. A bug that only fires for, say, NaN inputs
   to Pow won't show up unless `fill_edges` ends up in the sweep for that op.
   The `generators.FILL_FNS` dict is the place to broaden coverage.

3. **Optimization-dependent bugs**. We disable ORT optimizations
   (`ORT_DISABLE_ALL`) so intermediates remain visible. The Kaggle scorer
   appears to also run unoptimized; if that ever changes we'd diverge.

4. **Mod hangs in onnxruntime 1.24.4** for reasons not yet diagnosed; spec
   commented out in `op_specs.py`. Re-enable once root-caused.
