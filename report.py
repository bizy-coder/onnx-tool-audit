"""Consolidated report rendering: raw findings + bug catalog."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Iterable

import numpy as np

from .harness import (
    CaseResult, OpReport, TensorDiff,
    CONFIRMED_BUG_CLASSES, NOISE_BUG_CLASSES, ONNXRUNTIME_BUG_CLASSES,
)


# ─────────────────────────────────────────────────────────────────────────────
# Bug catalog (collapse findings into distinct bugs)
# ─────────────────────────────────────────────────────────────────────────────

def _shape_signature(shape: tuple[int, ...] | None) -> str:
    if shape is None:
        return "?"
    if shape == ():
        return "scalar"
    rank = len(shape)
    has_broadcast = any(d == 1 for d in shape) and any(d > 1 for d in shape)
    if rank == 4:
        return "rank4-broadcast" if has_broadcast else "rank4-full"
    if rank == 1:
        return "rank1"
    if rank == 0:
        return "scalar"
    return f"rank{rank}"

def fingerprint(op: str, diff: TensorDiff) -> tuple:
    klass = diff.bug_class
    if klass == "scalar-volume":
        return (klass,)
    if klass == "constant-uncounted":
        return (klass,)
    if klass == "wrong-shape":
        return (klass, op)
    if klass == "wrong-dtype":
        return (klass, op, diff.truth_dtype, diff.claim_dtype)
    if klass == "wrong-bytes":
        return (klass, op, _shape_signature(diff.truth_shape))
    if klass == "missing-tensor":
        return (klass, op)
    if klass == "onnx-tool-fails-valid-model":
        return (klass, op)
    if klass == "ort-rejects-checker-valid-model":
        return (klass, op)
    if klass == "invalid-test-case":
        return (klass, op)
    return (klass, op)

def _error_family(error: str | None) -> str:
    if not error:
        return ""
    head = error.splitlines()[0]
    for marker in (":", "["):
        if marker in head:
            head = head.split(marker, 1)[0]
    return head.strip()[:120]

@dataclass
class BugEntry:
    fingerprint: tuple
    bug_class: str
    ops: set[str] = field(default_factory=set)
    surface_count: int = 0
    representative: CaseResult | None = None
    rep_diff: TensorDiff | None = None
    minimal_label: str = ""
    error: str = ""

    def add(self, op: str, case: CaseResult, diff: TensorDiff) -> None:
        self.ops.add(op)
        self.surface_count += 1
        if diff.note and not self.error:
            self.error = diff.note
        if self.representative is None:
            self.representative = case
            self.rep_diff = diff
            self.minimal_label = case.case.label
            return
        cur_vol = sum(int(np.prod(c.shape) or 1) for c in self.representative.case.input_cases)
        new_vol = sum(int(np.prod(c.shape) or 1) for c in case.case.input_cases)
        if new_vol < cur_vol:
            self.representative = case
            self.rep_diff = diff
            self.minimal_label = case.case.label

def build_catalog(reports: Iterable[OpReport]) -> list[BugEntry]:
    catalog: dict[tuple, BugEntry] = {}
    for report in reports:
        for case in report.cases:
            if case.diff is None:
                continue
            if case.diff.truth_error:
                continue
            if case.diff.claim_error:
                d = TensorDiff(
                    name="<model>", bug_class="onnx-tool-fails-valid-model",
                    truth_shape=None, truth_dtype=None,
                    truth_bytes=case.diff.truth_total_bytes,
                    claim_shape=None, claim_dtype=None, claim_bytes=None,
                    note=case.diff.claim_error[:500],
                )
                fp = ("onnx-tool-fails-valid-model", report.op, _error_family(case.diff.claim_error))
                entry = catalog.get(fp)
                if entry is None:
                    entry = BugEntry(fingerprint=fp, bug_class=d.bug_class)
                    catalog[fp] = entry
                entry.add(report.op, case, d)
                continue
            for d in case.diff.tensor_diffs:
                fp = fingerprint(report.op, d)
                entry = catalog.get(fp)
                if entry is None:
                    entry = BugEntry(fingerprint=fp, bug_class=d.bug_class)
                    catalog[fp] = entry
                entry.add(report.op, case, d)

    def sort_key(e: BugEntry):
        is_noise = e.bug_class in NOISE_BUG_CLASSES
        return (is_noise, -e.surface_count, e.bug_class, sorted(e.ops)[0])

    return sorted(catalog.values(), key=sort_key)

def _bug_class_explanation(klass: str) -> str:
    expl = {
        "scalar-volume":
            "onnx_tool reports 0 bytes for tensors with shape `()` because "
            "`volume([])` returns 0 instead of 1.",
        "wrong-shape":
            "onnx_tool's static shape inference disagrees with the runtime "
            "shape produced by ORT execution.",
        "wrong-dtype":
            "onnx_tool's claimed output dtype disagrees with what ORT "
            "produces at runtime.",
        "wrong-bytes":
            "shape and dtype agree but byte counts differ — likely a "
            "miscomputed elementsize or an off-by-one in volume.",
        "constant-uncounted":
            "Constant node outputs are tracked at the per-tensor level but "
            "not added to per-node memory; the model total under-reports by "
            "the constant's size.",
        "missing-tensor":
            "onnx_tool's tensormap lacks an entry for a tensor that exists "
            "at runtime — the tensor is invisible to memory accounting.",
        "onnx-tool-fails-valid-model":
            "onnx_tool throws when profiling a model the ONNX spec checker "
            "AND ORT both accept. Either onnx_tool's op coverage is "
            "incomplete or it has a bug in shape/value inference.",
        "onnx-tool-timeout-valid-model":
            "onnx_tool did not finish within the per-case timeout after ORT "
            "accepted the model. This is recorded as a confirmed onnx_tool "
            "failure mode distinct from a thrown exception.",
        "ort-timeout":
            "The ORT/truth oracle did not finish within the per-case timeout. "
            "Recorded separately because this blocks validation, but it is "
            "not evidence of an onnx_tool bug.",
        "onnxruntime-rejects-valid-model":
            "onnxruntime fails to load or execute a model that the ONNX "
            "spec checker considers valid. This is an ORT bug, not an "
            "onnx_tool bug — onnx_tool may or may not have its own issue, "
            "but the primary signal here is ORT misbehaving.",
        "invalid-test-case":
            "The ONNX spec checker rejects the model. Our generator made "
            "an invalid combination — not a bug in any tool.",
    }
    return expl.get(klass, "(no explanation)")

def _render_catalog_entry(num: int, e: BugEntry) -> str:
    lines = []
    lines.append(f"### Bug {num}: `{e.bug_class}`")
    lines.append("")
    lines.append(f"_{_bug_class_explanation(e.bug_class)}_")
    lines.append("")
    ops_list = ", ".join(f"`{o}`" for o in sorted(e.ops))
    lines.append(f"- **Affected ops** ({len(e.ops)}): {ops_list}")
    lines.append(f"- **Surface findings collapsed**: {e.surface_count}")

    if e.rep_diff and e.representative:
        d = e.rep_diff
        case = e.representative.case
        lines.append("- **Minimal repro**:")
        lines.append("")
        lines.append(f"  Op: `{case.op}`  ")
        if case.input_cases:
            lines.append(f"  Inputs: `{e.minimal_label}`  ")
        if case.attrs:
            lines.append(f"  Attrs: `{case.attrs}`  ")
        lines.append("")
        if d.truth_shape is not None or d.truth_bytes is not None:
            lines.append("  | what     | shape | dtype | bytes |")
            lines.append("  |----------|-------|-------|-------|")
            lines.append(f"  | truth    | `{d.truth_shape}` | `{d.truth_dtype}` | `{d.truth_bytes}` |")
            lines.append(f"  | onnx_tool| `{d.claim_shape}` | `{d.claim_dtype}` | `{d.claim_bytes}` |")
        if d.note:
            lines.append("")
            lines.append(f"  _{d.note}_")
    elif e.error:
        lines.append("")
        lines.append(f"- **Representative error**: `{e.error[:300]}`")
    return "\n".join(lines)


def _jsonable(v):
    if isinstance(v, np.generic):
        return v.item()
    if isinstance(v, np.ndarray):
        return v.tolist()
    if isinstance(v, tuple):
        return list(v)
    if isinstance(v, list):
        return [_jsonable(x) for x in v]
    if isinstance(v, dict):
        return {str(k): _jsonable(val) for k, val in v.items()}
    if isinstance(v, bytes):
        return v.decode("utf-8", errors="replace")
    if hasattr(v, "SerializeToString"):
        return repr(v)
    return v


def _case_meta(case: CaseResult) -> dict:
    tc = case.case
    opsets = {imp.domain or "": imp.version for imp in tc.model.opset_import} if tc.model is not None else {}
    return {
        "op": tc.op,
        "opsets": opsets,
        "label": tc.label,
        "attrs": _jsonable(tc.attrs),
        "inputs": [
            {
                "name": c.name,
                "kind": "init" if c.is_init else "input",
                "shape_label": c.shape_label,
                "shape": list(c.shape),
                "dtype": c.dtype_label,
                "fill": c.fill_label,
            }
            for c in tc.input_cases
        ],
        "node_ops": [n.op_type for n in tc.model.graph.node] if tc.model is not None else [],
    }


def iter_raw_findings(reports: Iterable[OpReport]):
    """Yield one machine-readable record per raw finding surface."""
    for report in reports:
        for case_idx, case in enumerate(report.cases):
            if case.diff is None:
                continue
            base = {
                "report_op": report.op,
                "case_index": case_idx,
                "case": _case_meta(case),
                "timings": _jsonable(case.timings),
                "truth_total_bytes": case.diff.truth_total_bytes,
                "claim_total_bytes": case.diff.claim_total_bytes,
            }
            if case.diff.truth_error:
                continue
            if case.diff.claim_error:
                yield {
                    **base,
                    "bug_class": "onnx-tool-fails-valid-model",
                    "classification": "confirmed",
                    "tensor": "<model>",
                    "truth_error": None,
                    "claim_error": case.diff.claim_error,
                    "fingerprint": list(("onnx-tool-fails-valid-model", report.op, _error_family(case.diff.claim_error))),
                }
                continue
            for d in case.diff.tensor_diffs:
                yield {
                    **base,
                    "bug_class": d.bug_class,
                    "classification": (
                        "noise" if d.bug_class in NOISE_BUG_CLASSES
                        else "onnxruntime" if d.bug_class in ONNXRUNTIME_BUG_CLASSES
                        else "confirmed"
                    ),
                    "tensor": d.name,
                    "truth": {"shape": list(d.truth_shape) if d.truth_shape is not None else None,
                              "dtype": d.truth_dtype, "bytes": d.truth_bytes},
                    "claim": {"shape": list(d.claim_shape) if d.claim_shape is not None else None,
                              "dtype": d.claim_dtype, "bytes": d.claim_bytes},
                    "note": d.note,
                    "fingerprint": list(fingerprint(report.op, d)),
                }


def render_findings_jsonl(reports: Iterable[OpReport]) -> str:
    return "\n".join(json.dumps(_jsonable(row), sort_keys=True, default=repr)
                     for row in iter_raw_findings(reports)) + "\n"


def render_case_findings_jsonl(report_op: str, case: CaseResult) -> str:
    report = OpReport(op=report_op, cases=[case])
    rows = list(iter_raw_findings([report]))
    if not rows:
        return ""
    return "\n".join(json.dumps(_jsonable(row), sort_keys=True, default=repr)
                     for row in rows) + "\n"


def iter_ort_failures(reports: Iterable[OpReport]):
    """Yield one machine-readable record per ORT-rejected generated case."""
    for report in reports:
        for case_idx, case in enumerate(report.cases):
            if case.diff is None or not case.diff.truth_error:
                continue
            bug_class = case.diff.tensor_diffs[0].bug_class if case.diff.tensor_diffs else "invalid-test-case"
            yield {
                "report_op": report.op,
                "case_index": case_idx,
                "case": _case_meta(case),
                "classification": bug_class,
                "truth_error": case.diff.truth_error,
                "checker_error": case.diff.spec_error,
                "checker_passed": case.diff.spec_error is None,
                "error_family": _error_family(case.diff.truth_error),
                "timings": _jsonable(case.timings),
            }


def render_ort_failures_jsonl(reports: Iterable[OpReport]) -> str:
    return "\n".join(json.dumps(_jsonable(row), sort_keys=True, default=repr)
                     for row in iter_ort_failures(reports)) + "\n"


def render_case_ort_failure_jsonl(report_op: str, case: CaseResult) -> str:
    report = OpReport(op=report_op, cases=[case])
    rows = list(iter_ort_failures([report]))
    if not rows:
        return ""
    return "\n".join(json.dumps(_jsonable(row), sort_keys=True, default=repr)
                     for row in rows) + "\n"


def iter_profile_rows(reports: Iterable[OpReport]):
    for report in reports:
        invalid = len(report.invalid_cases)
        checker_passed_invalid = sum(
            1 for c in report.invalid_cases
            if c.diff is not None and c.diff.spec_error is None
        )
        cases = len(report.cases)
        yield {
            "op": report.op,
            "cases": cases,
            "disagreements": len(report.disagreements),
            "invalid": invalid,
            "invalid_checker_passed": checker_passed_invalid,
            "invalid_checker_failed": invalid - checker_passed_invalid,
            "build_errors": len(report.build_errors),
            "valid": cases - invalid,
            "timings": _jsonable(report.timings),
        }


def render_profile_jsonl(reports: Iterable[OpReport]) -> str:
    return "\n".join(json.dumps(_jsonable(row), sort_keys=True, default=repr)
                     for row in iter_profile_rows(reports)) + "\n"

def render_catalog(entries: list[BugEntry]) -> str:
    onnx_tool_bugs = [e for e in entries if e.bug_class in CONFIRMED_BUG_CLASSES]
    onnxruntime_bugs = [e for e in entries if e.bug_class in ONNXRUNTIME_BUG_CLASSES]
    noise = [e for e in entries if e.bug_class in NOISE_BUG_CLASSES]

    out: list[str] = []
    out.append("# onnx_tool 1.0.1 — bug catalog")
    out.append("")
    out.append("Each test case runs through two oracles:")
    out.append("")
    out.append("- **`onnxruntime`** executes the model and provides the runtime "
               "baseline. If ORT rejects a model, there is no shape/type/byte "
               "baseline for comparing onnx_tool.")
    out.append("- **`onnx_tool`** statically profiles the model.")
    out.append("")
    out.append("Classification:")
    out.append("")
    out.append("| ORT | onnx_tool | classification |")
    out.append("|-----|-----------|----------------|")
    out.append("| reject + checker rejects | (any) | **invalid-test-case** / harness coverage gap |")
    out.append("| reject + checker accepts | (any) | **ort-rejects-checker-valid-model** / no onnx_tool baseline |")
    out.append("| accept | reject | **onnx-tool-fails-valid-model** |")
    out.append("| accept | accept-but-disagrees | **onnx_tool wrong shape/dtype/bytes** |")
    out.append("")
    out.append(f"**Summary**: {len(onnx_tool_bugs)} distinct onnx_tool bugs "
               f"({sum(e.surface_count for e in onnx_tool_bugs)} surface findings collapsed).")
    out.append("")

    if onnx_tool_bugs:
        out.append("## Bugs in onnx_tool")
        out.append("")
        for i, e in enumerate(onnx_tool_bugs, 1):
            out.append(_render_catalog_entry(i, e))
            out.append("")

    if onnxruntime_bugs:
        out.append("---")
        out.append("")
        out.append("## Bugs in onnxruntime")
        out.append("")
        out.append("These models pass the ONNX spec checker but onnxruntime "
                   "fails to load or execute them. Reported separately because "
                   "fixing them is in onnxruntime, not onnx_tool.")
        out.append("")
        for i, e in enumerate(onnxruntime_bugs, 1):
            out.append(_render_catalog_entry(i, e))
            out.append("")

    if noise:
        out.append("---")
        out.append("")
        out.append("## Test-generation noise (not bugs)")
        out.append("")
        out.append("`onnx.checker` rejects these models — they're invalid per "
                   "the ONNX spec, so any tool's behavior on them is undefined. "
                   "Listed here for completeness so we can audit which generator "
                   "patterns produce invalid combinations.")
        out.append("")
        out.append("| ops | count | spec rejection | example |")
        out.append("|---|---|---|---|")
        for e in noise:
            label = e.minimal_label.replace("|", "\\|")[:60] if e.minimal_label else ""
            note = (e.rep_diff.note if e.rep_diff else "").replace("|", "\\|")[:80]
            out.append(f"| {', '.join(sorted(e.ops))} | {e.surface_count} | `{note}` | `{label}` |")
        out.append("")

    return "\n".join(out)


# ─────────────────────────────────────────────────────────────────────────────
# Raw report (per-op disagreement breakdown)
# ─────────────────────────────────────────────────────────────────────────────

def _shape_str(s) -> str:
    return "?" if s is None else f"({','.join(str(x) for x in s)})"

def _bytes_str(b) -> str:
    return "?" if b is None else f"{b}"

def _row_for_diff(d: TensorDiff) -> str:
    return (
        f"| `{d.name}` | `{d.bug_class}` | "
        f"`{_shape_str(d.truth_shape)}` / `{d.truth_dtype}` / `{_bytes_str(d.truth_bytes)}B` | "
        f"`{_shape_str(d.claim_shape)}` / `{d.claim_dtype}` / `{_bytes_str(d.claim_bytes)}B` | "
        f"{d.note} |"
    )

def render_op(report: OpReport) -> str:
    lines: list[str] = []
    lines.append(f"## `{report.op}`")
    if report.notes:
        lines.append(f"_{report.notes}_")
    lines.append("")
    n_total = len(report.cases)
    n_dis = len(report.disagreements)
    n_invalid = len(report.invalid_cases)
    n_be = len(report.build_errors)
    lines.append(f"- {n_total} cases, {n_dis} with disagreements, "
                 f"{n_invalid} invalid ignored, {n_be} build errors")

    klass_count: Counter[str] = Counter()
    for c in report.disagreements:
        if c.diff is None:
            continue
        if c.diff.truth_error:
            klass_count["ort-error"] += 1
        if c.diff.claim_error:
            klass_count["onnx-tool-error"] += 1
        for d in c.diff.tensor_diffs:
            klass_count[d.bug_class] += 1
    if klass_count:
        breakdown = ", ".join(f"`{k}`={v}" for k, v in klass_count.most_common())
        lines.append(f"- bug classes hit: {breakdown}")
    lines.append("")

    if not report.disagreements and not report.build_errors:
        lines.append("> No disagreements found.")
        lines.append("")
        return "\n".join(lines)

    if report.build_errors:
        lines.append("### Build errors")
        for c in report.build_errors[:20]:
            lines.append(f"- {c.case.label}")
        if len(report.build_errors) > 20:
            lines.append(f"- ... +{len(report.build_errors) - 20} more")
        lines.append("")

    if report.disagreements:
        lines.append("### Disagreements")
        by_class: dict[str, list[CaseResult]] = defaultdict(list)
        for c in report.disagreements:
            if c.diff is None:
                continue
            seen_classes = set()
            for d in c.diff.tensor_diffs:
                seen_classes.add(d.bug_class)
            if c.diff.truth_error:
                seen_classes.add("ort-error")
            if c.diff.claim_error:
                seen_classes.add("onnx-tool-error")
            if not seen_classes and c.diff.truth_total_bytes != c.diff.claim_total_bytes:
                seen_classes.add("totals-mismatch")
            for k in seen_classes:
                by_class[k].append(c)

        for klass in sorted(by_class.keys()):
            cases = by_class[klass]
            lines.append(f"#### `{klass}` ({len(cases)} cases)")
            lines.append("")
            lines.append("| tensor | bug | truth (shape/dtype/bytes) | claim (shape/dtype/bytes) | note |")
            lines.append("|---|---|---|---|---|")
            for c in cases[:20]:
                if c.diff is None:
                    continue
                lines.append(f"| _case:_ `{c.case.label}` | | | | |")
                if c.diff.truth_error:
                    lines.append(f"| _ort-error_ | `ort-error` | | | {c.diff.truth_error} |")
                if c.diff.claim_error:
                    lines.append(f"| _onnx-tool-error_ | `onnx-tool-error` | | | {c.diff.claim_error} |")
                for d in c.diff.tensor_diffs:
                    if d.bug_class == klass:
                        lines.append(_row_for_diff(d))
                if c.diff.truth_total_bytes != c.diff.claim_total_bytes and klass == "totals-mismatch":
                    lines.append(
                        f"| _totals_ | `totals-mismatch` | "
                        f"`{c.diff.truth_total_bytes}B` | `{c.diff.claim_total_bytes}B` | "
                        f"diff={c.diff.claim_total_bytes - c.diff.truth_total_bytes:+d}B |"
                    )
            if len(cases) > 20:
                lines.append(f"| ... | _+{len(cases) - 20} more cases_ | | | |")
            lines.append("")
    return "\n".join(lines)

def render_summary(reports: list[OpReport]) -> str:
    lines = ["# onnx_tool audit report",
             f"_generated {datetime.now().isoformat(timespec='seconds')}_",
             ""]
    n_ops = len(reports)
    n_cases = sum(len(r.cases) for r in reports)
    n_dis_cases = sum(len(r.disagreements) for r in reports)
    n_invalid_cases = sum(len(r.invalid_cases) for r in reports)
    n_be = sum(len(r.build_errors) for r in reports)
    lines.append(f"**{n_ops} ops, {n_cases} test cases, "
                 f"{n_dis_cases} with disagreements, {n_invalid_cases} invalid ignored, "
                 f"{n_be} build errors.**")
    lines.append("")

    klass_total: Counter[str] = Counter()
    for r in reports:
        for c in r.disagreements:
            if c.diff is None:
                continue
            for d in c.diff.tensor_diffs:
                klass_total[d.bug_class] += 1
            if c.diff.truth_error:
                klass_total["ort-error"] += 1
            if c.diff.claim_error:
                klass_total["onnx-tool-error"] += 1

    if klass_total:
        lines.append("## Bug class totals")
        lines.append("")
        lines.append("| class | count |")
        lines.append("|---|---|")
        for k, v in klass_total.most_common():
            lines.append(f"| `{k}` | {v} |")
        lines.append("")

    lines.append("## Per-op summary")
    lines.append("")
    lines.append("| op | cases | disagreements | invalid | build-errors | notes |")
    lines.append("|---|---|---|---|---|---|")
    for r in sorted(reports, key=lambda x: (-len(x.disagreements), x.op)):
        lines.append(f"| [`{r.op}`](#{r.op.lower()}) | "
                     f"{len(r.cases)} | {len(r.disagreements)} | {len(r.invalid_cases)} | "
                     f"{len(r.build_errors)} | "
                     f"{r.notes or ''} |")
    lines.append("")
    return "\n".join(lines)

def render_full_report(reports: list[OpReport]) -> str:
    sections = [render_summary(reports)]
    for r in sorted(reports, key=lambda x: (-len(x.disagreements), x.op)):
        sections.append(render_op(r))
    return "\n".join(sections)

__all__ = [
    "BugEntry", "build_catalog", "render_catalog",
    "iter_raw_findings", "render_findings_jsonl", "render_case_findings_jsonl",
    "iter_ort_failures", "render_ort_failures_jsonl", "render_case_ort_failure_jsonl",
    "iter_profile_rows", "render_profile_jsonl",
    "render_summary", "render_op", "render_full_report",
]
