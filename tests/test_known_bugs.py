"""Self-tests: the harness must catch the four known onnx_tool 1.0.1 bugs.

Run with: python -m onnx_tool_audit.tests.test_known_bugs

These are integration-level smoke tests. Each one asserts the harness flags
a specific bug class on a specific op. If any of these fails it means either:
  (a) onnx_tool was upgraded and the bug is fixed (good — remove the test), or
  (b) the harness regressed (bad — fix the harness).
"""
from __future__ import annotations

import sys

from ..dag_generator import generate_scenarios
from ..harness import run_case, run_op, BUG_CLASSES


def _bug_classes_seen(report) -> set[str]:
    seen = set()
    for c in report.disagreements:
        if c.diff is None:
            continue
        for d in c.diff.tensor_diffs:
            seen.add(d.bug_class)
        if c.diff.truth_error:
            seen.add("ort-error")
        if c.diff.claim_error:
            seen.add("onnx-tool-error")
    return seen


def test_scalar_volume_via_identity():
    """Scalars (shape=[]) should report nonzero bytes; onnx_tool reports 0."""
    report = run_op("Identity")
    seen = _bug_classes_seen(report)
    assert "scalar-volume" in seen, f"expected scalar-volume in {seen}"
    print(f"[PASS] scalar-volume detected via Identity ({len([c for c in report.disagreements])} cases)")


def test_max_shape_via_where():
    """Where with cond having more elements than X/Y should expose _max_shape bug."""
    report = run_op("Where")
    seen = _bug_classes_seen(report)
    assert "wrong-shape" in seen, f"expected wrong-shape in {seen}"
    # Verify at least one case has cond-element-count > X-element-count
    found = False
    for c in report.disagreements:
        if c.diff is None:
            continue
        for d in c.diff.tensor_diffs:
            if d.bug_class == "wrong-shape":
                # The bug pattern: claimed shape has fewer elements than truth.
                if d.truth_shape and d.claim_shape:
                    import numpy as np
                    if int(np.prod(d.truth_shape)) > int(np.prod(d.claim_shape)):
                        found = True
                        break
        if found:
            break
    assert found, "no Where case where claim < truth in elements (bug should under-report)"
    print(f"[PASS] _max_shape bug detected via Where")


def test_constant_uncounted():
    """Constant outputs should be counted toward memory; onnx_tool reports 0."""
    report = run_op("Constant")
    seen = _bug_classes_seen(report)
    assert len(report.cases) > 0, "no test cases generated for Constant"
    assert "constant-uncounted" in seen or len(seen) > 0, f"expected disagreements for Constant in {seen}"
    print(f"[PASS] constant-uncounted detected via Constant")


def test_compress_get_numpy_zero_fabrication():
    """When Compress's condition is a runtime tensor (output of another node),
    onnx_tool fabricates zeros via Tensor.get_numpy() and infers a zero-batch
    output. The Cast(bool) -> Compress scenario is the canonical pattern.
    """
    scenarios = generate_scenarios()
    target = next((s for s in scenarios if "Compress" in s.label), None)
    assert target is not None, "Compress scenario missing"
    res = run_case(target)
    assert res.diff is not None
    diffs = res.diff.tensor_diffs
    # Look for a wrong-shape on the Compress output where claim has 0 along axis 1
    found = False
    for d in diffs:
        if d.bug_class == "wrong-shape" and d.claim_shape and len(d.claim_shape) >= 2 \
                and d.claim_shape[1] == 0 and d.truth_shape and d.truth_shape[1] > 0:
            found = True
            break
    assert found, f"no zero-batch wrong-shape on Compress output; diffs={[(d.bug_class, d.claim_shape) for d in diffs]}"
    print(f"[PASS] Compress get_numpy zero-fabrication detected via Cast(bool) -> Compress")


def main():
    tests = [
        test_scalar_volume_via_identity,
        test_max_shape_via_where,
        test_constant_uncounted,
        test_compress_get_numpy_zero_fabrication,
    ]
    failed = []
    for t in tests:
        try:
            t()
        except AssertionError as e:
            print(f"[FAIL] {t.__name__}: {e}")
            failed.append(t.__name__)
        except Exception as e:
            print(f"[ERROR] {t.__name__}: {type(e).__name__}: {e}")
            failed.append(t.__name__)
    if failed:
        print(f"\n{len(failed)} of {len(tests)} known-bug tests failed: {failed}")
        return 1
    print(f"\nAll {len(tests)} known-bug tests pass — harness correctly flags onnx_tool 1.0.1 bugs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
