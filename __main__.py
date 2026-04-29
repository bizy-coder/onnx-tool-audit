"""CLI entry point.

Usage:
    python -m onnx_tool_audit run                # full sweep, write findings/report.md
    python -m onnx_tool_audit run --op Where     # single op
    python -m onnx_tool_audit run --op Where Compress
    python -m onnx_tool_audit verify             # smoke-test the four known bugs
"""
from __future__ import annotations

import argparse
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from .harness import CONFIRMED_BUG_CLASSES, NOISE_BUG_CLASSES, run_dag_phase, run_op, run_op_with_timeout
from .profiles import DEFAULT_OPSET, MAX_CASES_PER_OP, load_profiles, list_specs
from .report import (
    build_catalog,
    render_catalog,
    render_case_findings_jsonl,
    render_case_ort_failure_jsonl,
    render_findings_jsonl,
    render_full_report,
    render_ort_failures_jsonl,
    render_profile_jsonl,
)
from .structured_report import render_structured_report


HERE = Path(__file__).resolve().parent
FINDINGS = HERE / "findings"


def _out_path(value: str | None, default: Path) -> Path:
    if not value:
        return default
    path = Path(value)
    if not path.is_absolute() and path.parts and path.parts[0].lower() == "findings":
        return FINDINGS.joinpath(*path.parts[1:])
    return path


def _report_counts(report) -> tuple[int, int, int]:
    confirmed = noise = other = 0
    for case in report.disagreements:
        if case.diff is None:
            continue
        classes = {d.bug_class for d in case.diff.tensor_diffs}
        if case.diff.claim_error:
            classes.add("onnx-tool-fails-valid-model")
        if classes & set(CONFIRMED_BUG_CLASSES):
            confirmed += 1
        elif classes <= set(NOISE_BUG_CLASSES):
            noise += 1
        else:
            other += 1
    return confirmed, noise, other


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s).strip("_")[:90] or "case"


def _error_family(error: str | None) -> str:
    if not error:
        return "unknown"
    head = error.splitlines()[0]
    for marker in (":", "["):
        if marker in head:
            head = head.split(marker, 1)[0]
    return head.strip()[:80] or "unknown"


def cmd_run(args: argparse.Namespace) -> int:
    op_filter = args.op or None
    specs_for_opset = load_profiles(opset=args.opset)
    if op_filter:
        unknown = [o for o in op_filter if o not in specs_for_opset and o != "DAG"]
        if unknown:
            print(f"unknown ops: {unknown}", file=sys.stderr)
            print(f"available for opset {args.opset}: {sorted(specs_for_opset.keys())} + DAG", file=sys.stderr)
            return 2

    reports = []
    out_path = _out_path(args.out, FINDINGS / "report.md")
    findings_path = (
        _out_path(args.findings_out, FINDINGS / "findings.jsonl") if args.findings_out
        else out_path.with_name(out_path.stem + "_findings.jsonl") if args.out
        else FINDINGS / "findings.jsonl"
    )
    catalog_path = (
        _out_path(args.catalog_out, FINDINGS / "bugs.md") if args.catalog_out
        else out_path.with_name(out_path.stem + "_bugs.md") if args.out
        else FINDINGS / "bugs.md"
    )
    ort_failures_path = (
        _out_path(args.ort_failures_out, FINDINGS / "ort_failures.jsonl") if args.ort_failures_out
        else out_path.with_name(out_path.stem + "_ort_failures.jsonl") if args.out
        else FINDINGS / "ort_failures.jsonl"
    )
    profile_path = (
        _out_path(args.profile_out, FINDINGS / "profile.jsonl") if args.profile_out
        else out_path.with_name(out_path.stem + "_profile.jsonl") if args.out
        else FINDINGS / "profile.jsonl"
    )
    findings_path.parent.mkdir(parents=True, exist_ok=True)
    findings_path.write_text("", encoding="utf-8")
    ort_failures_path.parent.mkdir(parents=True, exist_ok=True)
    ort_failures_path.write_text("", encoding="utf-8")

    write_lock = threading.Lock()
    saved_ort_failures: set[tuple[str, str]] = set()
    ort_save_dir = _out_path(args.save_ort_failures, FINDINGS / "ort_repros") if args.save_ort_failures else None
    if ort_save_dir:
        ort_save_dir.mkdir(parents=True, exist_ok=True)

    def on_case_result(report, case_result) -> None:
        chunk = render_case_findings_jsonl(report.op, case_result)
        if chunk:
            with write_lock:
                with findings_path.open("a", encoding="utf-8") as f:
                    f.write(chunk)
        ort_chunk = render_case_ort_failure_jsonl(report.op, case_result)
        if ort_chunk:
            with write_lock:
                with ort_failures_path.open("a", encoding="utf-8") as f:
                    f.write(ort_chunk)
                if ort_save_dir and case_result.case.model is not None and case_result.diff is not None:
                    family = _error_family(case_result.diff.truth_error)
                    key = (report.op, family)
                    if key not in saved_ort_failures:
                        saved_ort_failures.add(key)
                        name = f"{_slug(report.op)}__{_slug(family)}.onnx"
                        (ort_save_dir / name).write_bytes(case_result.case.model.SerializeToString())

    def _print_op_result(r, label: str, total: int) -> None:
        n_dis = len(r.disagreements)
        n_invalid = len(r.invalid_cases)
        n_conf, n_noise, n_other = _report_counts(r)
        n_be = len(r.build_errors)
        flag = ("!" if n_dis > 0 else " ") + ("?" if n_be > 0 else " ")
        print(f"  {label} {flag} {r.op.split('@')[0]:30s} "
              f"cases={len(r.cases):3d} dis={n_dis:3d} "
              f"confirmed={n_conf:3d} noise={n_noise:3d} other={n_other:3d} "
              f"invalid={n_invalid:3d} be={n_be:3d}",
              file=sys.stderr, flush=True)
        if args.profile:
            t = r.timings
            valid = max(1, len(r.cases) - len(r.invalid_cases))
            print(f"        time gen={t.get('generate', 0.0):6.2f}s "
                  f"run={t.get('run', 0.0):6.2f}s "
                  f"ort={t.get('ort', 0.0):6.2f}s "
                  f"onnx_tool={t.get('onnx_tool', 0.0):6.2f}s "
                  f"valid/s={valid / max(t.get('run', 0.000001), 0.000001):6.1f}",
                  file=sys.stderr, flush=True)

    # Phase 1: single-op sweep
    if not args.dag_only:
        specs = list_specs(only=op_filter, opset=args.opset) if op_filter else list_specs(opset=args.opset)
        specs = [s for s in specs if s.name != "DAG"]
        workers = args.workers
        case_workers = args.case_workers
        print(f"Phase 1: running {len(specs)} ops at opset {args.opset} "
              f"(workers={workers}, case-workers={case_workers})...", file=sys.stderr)

        if workers > 1:
            done_count = [0]
            done_lock = threading.Lock()

            def _run_one(spec):
                if args.op_timeout > 0:
                    return run_op_with_timeout(
                        spec.name, opset=args.opset,
                        op_timeout=args.op_timeout,
                        case_timeout=args.case_timeout,
                        case_limit=args.case_limit,
                        case_workers=case_workers,
                        compare=args.compare,
                    )
                return run_op(spec.name, opset=args.opset,
                              case_timeout=args.case_timeout,
                              case_limit=args.case_limit,
                              case_workers=case_workers,
                              compare=args.compare,
                              on_result=on_case_result)

            with ThreadPoolExecutor(max_workers=workers) as pool:
                future_to_spec = {pool.submit(_run_one, spec): spec for spec in specs}
                for future in as_completed(future_to_spec):
                    spec = future_to_spec[future]
                    with done_lock:
                        done_count[0] += 1
                        label = f"[{done_count[0]:3d}/{len(specs)}]"
                    try:
                        r = future.result()
                    except Exception as e:
                        print(f"  {label} {spec.name}: HARNESS-ERROR: {type(e).__name__}: {e}",
                              file=sys.stderr, flush=True)
                        continue
                    _print_op_result(r, label, len(specs))
                    reports.append(r)
        else:
            for i, spec in enumerate(specs):
                label = f"[{i+1:3d}/{len(specs)}]"
                print(f"  {label} .. {spec.name:30s} starting", file=sys.stderr, flush=True)
                try:
                    if args.op_timeout > 0:
                        r = run_op_with_timeout(
                            spec.name, opset=args.opset,
                            op_timeout=args.op_timeout,
                            case_timeout=args.case_timeout,
                            case_limit=args.case_limit,
                            case_workers=case_workers,
                            compare=args.compare,
                        )
                    else:
                        r = run_op(spec.name, opset=args.opset,
                                   case_timeout=args.case_timeout,
                                   case_limit=args.case_limit,
                                   case_workers=case_workers,
                                   compare=args.compare,
                                   on_result=on_case_result)
                except Exception as e:
                    print(f"  {label} {spec.name}: HARNESS-ERROR: {type(e).__name__}: {e}",
                          file=sys.stderr)
                    continue
                _print_op_result(r, label, len(specs))
                reports.append(r)

    # Phase 2: DAG sweep
    run_dag = (op_filter is None) or ("DAG" in op_filter) or args.dag_only
    if run_dag and not args.no_dag:
        print(f"Phase 2: running DAG generator ({args.dag_count} random + scenarios)...",
              file=sys.stderr)
        try:
            r = run_dag_phase(n_random=args.dag_count,
                              target_nodes=args.dag_nodes,
                              opset=args.opset,
                              case_timeout=args.case_timeout,
                              on_result=on_case_result)
            n_dis = len(r.disagreements)
            n_invalid = len(r.invalid_cases)
            n_conf, n_noise, n_other = _report_counts(r)
            n_be = len(r.build_errors)
            flag = ("!" if n_dis > 0 else " ") + ("?" if n_be > 0 else " ")
            print(f"  [DAG] {flag} {r.op:30s} cases={len(r.cases):3d} "
                  f"dis={n_dis:3d} confirmed={n_conf:3d} noise={n_noise:3d} "
                  f"other={n_other:3d} invalid={n_invalid:3d} be={n_be:3d}",
                  file=sys.stderr, flush=True)
            reports.append(r)
        except Exception as e:
            print(f"  [DAG] HARNESS-ERROR: {type(e).__name__}: {e}", file=sys.stderr)

    # Raw report — full detail, one row per disagreement.
    md = render_full_report(reports)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    print(f"wrote {out_path}", file=sys.stderr)

    findings_path.write_text(render_findings_jsonl(reports), encoding="utf-8")
    print(f"wrote {findings_path}", file=sys.stderr)

    ort_failures_path.write_text(render_ort_failures_jsonl(reports), encoding="utf-8")
    print(f"wrote {ort_failures_path}", file=sys.stderr)

    profile_path.parent.mkdir(parents=True, exist_ok=True)
    profile_path.write_text(render_profile_jsonl(reports), encoding="utf-8")
    print(f"wrote {profile_path}", file=sys.stderr)

    # Bug catalog — surface findings clustered into distinct bugs with
    # minimal repros. This is the actionable artifact.
    catalog = build_catalog(reports)
    catalog_md = render_catalog(catalog)
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(catalog_md, encoding="utf-8")
    print(f"wrote {catalog_path}", file=sys.stderr)

    # Brief stdout summary
    n_dis = sum(len(r.disagreements) for r in reports)
    n_be = sum(len(r.build_errors) for r in reports)
    n_confirmed = sum(1 for e in catalog if e.bug_class in CONFIRMED_BUG_CLASSES)
    n_invalid_cases = sum(len(r.invalid_cases) for r in reports)
    confirmed_surface = sum(e.surface_count for e in catalog if e.bug_class in CONFIRMED_BUG_CLASSES)
    print(f"  {len(reports)} ops | {sum(len(r.cases) for r in reports)} cases | "
          f"{n_dis} finding cases | {n_be} build errors", file=sys.stderr)
    print(f"  bug catalog: {n_confirmed} distinct confirmed bugs | "
          f"{confirmed_surface} confirmed surfaces | "
          f"{n_invalid_cases} invalid cases ignored", file=sys.stderr)
    return 0 if n_confirmed == 0 else 1


def cmd_verify(args: argparse.Namespace) -> int:
    """Smoke test: verify the harness runs and generates test cases."""
    print(f"Running smoke tests on a few operators at opset {args.opset}...", file=sys.stderr)

    test_ops = ["Add", "Where", "Identity", "Relu"]
    all_ok = True

    for op_name in test_ops:
        try:
            report = run_op(op_name, opset=args.opset)
            n_cases = len(report.cases)
            n_dis = len(report.disagreements)
            status = "OK" if n_cases > 0 else "SKIP"
            print(f"  {op_name:15s} {status:4s}  cases={n_cases:3d} disagreements={n_dis:3d}", file=sys.stderr)
            if n_cases == 0:
                all_ok = False
        except Exception as e:
            print(f"  {op_name:15s} FAIL  {type(e).__name__}: {e}", file=sys.stderr)
            all_ok = False

    if all_ok:
        print("VERIFY PASSED: harness generates test cases.", file=sys.stderr)
        return 0
    else:
        print("VERIFY FAILED: some operators generated no test cases.", file=sys.stderr)
        return 1


def _expand_paths(values: list[str] | None, default_glob: str) -> list[Path]:
    if not values:
        return sorted(FINDINGS.glob(default_glob))
    out = []
    for value in values:
        path = _out_path(value, FINDINGS / value)
        matches = sorted(path.parent.glob(path.name)) if any(ch in path.name for ch in "*?[") else [path]
        out.extend(matches)
    return out


def cmd_structured_report(args: argparse.Namespace) -> int:
    findings = _expand_paths(args.findings, "all_ops_opset*_findings.jsonl")
    profiles = _expand_paths(args.profiles, "all_ops_opset*_profile.jsonl")
    if not findings:
        print("no findings JSONL files found", file=sys.stderr)
        return 2
    out_path = _out_path(args.out, FINDINGS / "structured_issue_report.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render_structured_report(findings, profiles), encoding="utf-8")
    print(f"wrote {out_path}", file=sys.stderr)
    print(f"  findings files: {len(findings)} | profile files: {len(profiles)}", file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="python -m onnx_tool_audit")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="run the differential sweep")
    p_run.add_argument("--op", nargs="*", help="restrict to specific op names (or 'DAG' for Phase 2 only)")
    p_run.add_argument("--out", help="output markdown path (default: onnx_tool_audit/findings/report.md)")
    p_run.add_argument("--catalog-out", help="bug catalog markdown path (default: onnx_tool_audit/findings/bugs.md, or alongside --out)")
    p_run.add_argument("--findings-out", help="raw findings JSONL path (default: onnx_tool_audit/findings/findings.jsonl, or alongside --out)")
    p_run.add_argument("--ort-failures-out", help="ORT rejection JSONL path (default: onnx_tool_audit/findings/ort_failures.jsonl, or alongside --out)")
    p_run.add_argument("--profile-out", help="per-op timing JSONL path (default: onnx_tool_audit/findings/profile.jsonl, or alongside --out)")
    p_run.add_argument("--save-ort-failures",
                       help="optional directory to save first rejected ONNX model per op/error-family")
    p_run.add_argument("--opset", type=int, default=DEFAULT_OPSET,
                       help=f"ONNX opset to test for single-op generation (default {DEFAULT_OPSET})")
    p_run.add_argument("--case-timeout", type=float, default=0.0,
                       help="seconds before one test case is killed and marked as a timeout (default disabled; >0 enables)")
    p_run.add_argument("--op-timeout", type=float, default=0.0,
                       help="seconds before one whole op is killed and marked as OP-TIMEOUT (default disabled; cheaper than --case-timeout)")
    p_run.add_argument("--case-limit", type=int, default=MAX_CASES_PER_OP,
                       help=f"max generated single-op cases per op (default {MAX_CASES_PER_OP})")
    p_run.add_argument("--dag-count", type=int, default=200,
                       help="number of random DAGs in Phase 2 (default 200)")
    p_run.add_argument("--dag-nodes", type=int, default=4,
                       help="target nodes per DAG (default 4)")
    p_run.add_argument("--no-dag", action="store_true", help="skip Phase 2 (DAG)")
    p_run.add_argument("--dag-only", action="store_true",
                       help="run only Phase 2 (DAG); skip Phase 1 single-op sweep")
    p_run.add_argument("--workers", type=int, default=1,
                       help="number of ops to run in parallel (default 1)")
    p_run.add_argument("--case-workers", type=int, default=1,
                       help="number of cases to run in parallel within each op (default 1)")
    p_run.add_argument("--profile", action="store_true",
                       help="print per-op generation/ORT/onnx_tool timing while running")
    p_run.add_argument("--compare", default="both",
                       choices=["onnx_tool", "scorer", "both"],
                       help="which oracle to diff against ORT: onnx_tool, scorer (onnx.shape_inference memory path), or both (default)")
    p_run.set_defaults(func=cmd_run)

    p_verify = sub.add_parser("verify", help="smoke-test against known bugs")
    p_verify.add_argument("--opset", type=int, default=DEFAULT_OPSET,
                          help=f"ONNX opset to test (default {DEFAULT_OPSET})")
    p_verify.set_defaults(func=cmd_verify)

    p_structured = sub.add_parser("structured-report", help="build grouped issue report from findings JSONL")
    p_structured.add_argument("--findings", nargs="*",
                              help="findings JSONL path/glob (default: findings/all_ops_opset*_findings.jsonl)")
    p_structured.add_argument("--profiles", nargs="*",
                              help="profile JSONL path/glob for coverage notes (default: findings/all_ops_opset*_profile.jsonl)")
    p_structured.add_argument("--out", default="findings/structured_issue_report.md",
                              help="output markdown path (default: findings/structured_issue_report.md)")
    p_structured.set_defaults(func=cmd_structured_report)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
