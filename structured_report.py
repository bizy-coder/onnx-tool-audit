"""Structured issue report from findings/profile JSONL artifacts.

Renders confirmed onnx_tool divergences as compact markdown tables grouped
by category (Type / Shape / Errors). Each row is one (op, opsets, family)
issue; columns describe how the test was set up and what diverged.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


TYPE_CLASSES = {"wrong-dtype"}
SHAPE_CLASSES = {"wrong-shape", "wrong-bytes", "scalar-volume", "missing-tensor", "constant-uncounted"}
ERROR_CLASSES = {"onnx-tool-fails-valid-model", "onnx-tool-timeout-valid-model"}


def _read_jsonl(paths: Iterable[Path]) -> Iterable[dict]:
    for path in paths:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield json.loads(line)


def _opset(row: dict) -> int | str:
    opsets = row.get("case", {}).get("opsets", {})
    if "" in opsets:
        return opsets[""]
    m = re.search(r"@(\d+)$", row.get("report_op", ""))
    return int(m.group(1)) if m else "?"


def _op(row: dict) -> str:
    return row.get("case", {}).get("op") or row.get("report_op", "").split("@")[0]


def _product(shape) -> int | None:
    if shape is None:
        return None
    n = 1
    for d in shape:
        n *= int(d)
    return n


def _error_family(error: str | None) -> str:
    if not error:
        return "unknown error"
    head = error.splitlines()[0]
    for marker in (":", "["):
        if marker in head:
            head = head.split(marker, 1)[0]
    return head.strip()[:120] or "unknown error"


def _shape_family(row: dict) -> str:
    klass = row["bug_class"]
    if klass == "scalar-volume":
        return "scalar counted as 0 bytes"
    if klass == "missing-tensor":
        return "tensor missing from tensormap"
    if klass == "constant-uncounted":
        return "constant output not counted"
    if klass == "wrong-bytes":
        return "byte count mismatch"

    truth, claim = row.get("truth", {}), row.get("claim", {})
    ts, cs = truth.get("shape"), claim.get("shape")
    tv, cv = _product(ts), _product(cs)
    if tv is not None and cv is not None and cv < tv:
        return "shape undercount"
    if tv is not None and cv is not None and cv > tv:
        return "shape overcount"
    if ts is not None and cs is not None and len(ts) != len(cs):
        return "rank mismatch"
    return "wrong shape"


def _family(row: dict) -> str:
    klass = row["bug_class"]
    if klass in TYPE_CLASSES:
        return f"{row.get('truth', {}).get('dtype')} → {row.get('claim', {}).get('dtype')}"
    if klass in SHAPE_CLASSES:
        return _shape_family(row)
    if klass in ERROR_CLASSES:
        return _error_family(row.get("claim_error") or row.get("note"))
    return klass


def _category(klass: str) -> str | None:
    if klass in TYPE_CLASSES:
        return "Incorrect Type"
    if klass in SHAPE_CLASSES:
        return "Incorrect Shape"
    if klass in ERROR_CLASSES:
        return "Incorrect Errors"
    return None


def _fmt_opsets(vals: set[int | str]) -> str:
    ints = sorted(v for v in vals if isinstance(v, int))
    other = sorted(str(v) for v in vals if not isinstance(v, int))
    ranges = []
    i = 0
    while i < len(ints):
        start = end = ints[i]
        while i + 1 < len(ints) and ints[i + 1] == end + 1:
            i += 1
            end = ints[i]
        ranges.append(str(start) if start == end else f"{start}–{end}")
        i += 1
    return ", ".join(ranges + other)


# ─────────────────────────────────────────────────────────────────────────────
# Trigger parsing — turn raw labels into human-readable pieces
# ─────────────────────────────────────────────────────────────────────────────
#
# Raw label format from the harness:
#     "X(input)=BCHW/float32/random data2(init)=1d-10/int64/zeros {'axis': 0} outputs=1"
#
# We split it into:
#   inputs: list of (name, kind, shape, dtype, fill)
#   attrs:  dict of attribute name -> value (parsed where possible)

_PORT_RE = re.compile(r"(\w+)\((input|init)\)=([^\s]+)")
_ATTRS_RE = re.compile(r"\{[^}]*\}")


def _parse_trigger(label: str) -> tuple[list[tuple[str, str, str, str, str]], str]:
    """Return (ports, attrs_str) parsed from a TestCase.label."""
    ports = []
    for m in _PORT_RE.finditer(label or ""):
        name, kind, spec = m.group(1), m.group(2), m.group(3)
        parts = spec.split("/")
        shape = parts[0] if len(parts) > 0 else ""
        dtype = parts[1] if len(parts) > 1 else ""
        fill = parts[2] if len(parts) > 2 else ""
        ports.append((name, kind, shape, dtype, fill))

    attrs_match = _ATTRS_RE.search(label or "")
    attrs_raw = attrs_match.group(0) if attrs_match else ""
    return ports, attrs_raw


def _parse_attrs_dict(attrs_raw: str) -> dict:
    """Best-effort parse of attrs raw string into a dict. Returns {} on failure."""
    import ast
    if not attrs_raw or attrs_raw.strip() in ("", "{}"):
        return {}
    try:
        v = ast.literal_eval(attrs_raw)
        return v if isinstance(v, dict) else {}
    except Exception:
        return {}


def _analyze_variation(rows: list[dict]) -> tuple[set[tuple[int, str]], set[str]]:
    """For all rows in a group, find which input port fields and attr keys vary.

    Returns:
        varying_fields: set of (port_index, field_name) where field_name in {"shape", "dtype", "fill"}
        varying_attrs: set of attr keys that take more than one value across rows
    """
    if not rows or len(rows) < 2:
        return set(), set()

    parsed = [_parse_trigger((r.get("case", {}) or {}).get("label", "")) for r in rows]
    n_ports = max(len(p) for p, _ in parsed) if parsed else 0

    varying_fields = set()
    for i in range(n_ports):
        shapes, dtypes, fills = set(), set(), set()
        for ports, _ in parsed:
            if i < len(ports):
                shapes.add(ports[i][2])
                dtypes.add(ports[i][3])
                fills.add(ports[i][4])
        if len(shapes) > 1:
            varying_fields.add((i, "shape"))
        if len(dtypes) > 1:
            varying_fields.add((i, "dtype"))
        if len(fills) > 1:
            varying_fields.add((i, "fill"))

    varying_attrs = set()
    attrs_dicts = [_parse_attrs_dict(s) for _, s in parsed]
    all_keys = set().union(*(d.keys() for d in attrs_dicts)) if attrs_dicts else set()
    for k in all_keys:
        vals = {repr(d.get(k)) for d in attrs_dicts}
        if len(vals) > 1:
            varying_attrs.add(k)
    return varying_fields, varying_attrs


def _format_inputs(ports: list[tuple[str, str, str, str, str]],
                   varying_fields: set[tuple[int, str]] = frozenset()) -> str:
    """Render input ports. Mark varying fields with `*` (means "any value works")."""
    if not ports:
        return "—"
    chunks = []
    for i, (name, kind, shape, dtype, fill) in enumerate(ports):
        kind_tag = "" if kind == "input" else " (init)"
        d_short = dtype.replace("float", "f").replace("int", "i").replace("uint", "u")
        s = f"{shape}\\*" if (i, "shape") in varying_fields else shape
        d = f"{d_short}\\*" if (i, "dtype") in varying_fields else d_short
        f = f"{fill}\\*" if (i, "fill") in varying_fields else fill
        chunks.append(f"`{name}`{kind_tag}: {s}/{d}/{f}")
    return "<br>".join(chunks)


def _format_attrs(attrs_raw: str, varying_attrs: set[str] = frozenset()) -> str:
    """Strip dict noise; mark varying keys with `*`."""
    if not attrs_raw or attrs_raw == "{}":
        return "—"
    d = _parse_attrs_dict(attrs_raw)
    if not d:
        # Fall back to old string cleanup
        s = attrs_raw.strip("{}").strip()
        s = re.sub(r"'(\w+)':\s*", r"\1=", s)
        s = re.sub(r"b'([^']*)'", r"\1", s)
        return f"`{s}`"
    parts = []
    for k, v in d.items():
        if isinstance(v, bytes):
            v_str = v.decode("utf-8", errors="replace")
        else:
            v_str = repr(v) if isinstance(v, str) else str(v)
        marker = "\\*" if k in varying_attrs else ""
        parts.append(f"{k}={v_str}{marker}")
    return f"`{', '.join(parts)}`"


def _md_shape(s) -> str:
    if s is None:
        return "—"
    return f"`{tuple(s)}`"


def _md_cell(s) -> str:
    if s is None or s == "":
        return "—"
    return f"`{s}`"


def _coverage_cell(hit_cases: int, surfaces: int, valid: int | None) -> str:
    if valid is None or valid <= 0:
        base = f"{hit_cases}"
    elif hit_cases >= valid:
        base = f"{hit_cases}/{valid}"
    else:
        base = f"{hit_cases}/{valid}"
    if surfaces != hit_cases:
        base += f" ({surfaces} surf)"
    return base


def _md_escape(s: str) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


# ─────────────────────────────────────────────────────────────────────────────
# "Simplest example" scoring — pick the cleanest repro for display
# ─────────────────────────────────────────────────────────────────────────────

_FILL_SCORE = {
    "zeros": 0, "ones": 1, "all_true": 1, "all_false": 1,
    "alternating": 2, "sequential": 2, "sparse": 3,
    "random": 4, "onehot": 4, "edges": 5,
}
_SHAPE_SCORE = {
    "scalar": 0,
    "1d-1": 1, "1d-9": 1, "1d-10": 1, "1d-30": 1,
    "2d": 2, "3d": 3,
    "B-1-1-1": 4, "B-1-1-W": 4, "B-1-H-1": 4, "B-1-H-W": 4, "B-1-9-9": 4,
    "B-C-1-1": 5,
    "BCHW-tiny": 5, "BCHW-5": 6, "BCHW-9": 6,
    "BCHW-asym": 7, "BCHW": 8, "BCHW-batchN": 9,
}


def _simplicity_score(row: dict) -> tuple:
    """Lower is simpler. Prefer fewer/smaller inputs, simpler fills, fewer attrs."""
    case = row.get("case", {}) or {}
    ports, attrs_raw = _parse_trigger(case.get("label", ""))
    shape_total = sum(_SHAPE_SCORE.get(p[2], 10) for p in ports)
    fill_total = sum(_FILL_SCORE.get(p[4], 10) for p in ports)
    attr_complexity = max(0, len(attrs_raw or "") - 2)
    return (len(ports), shape_total, fill_total, attr_complexity)


def _trigger_signature(row: dict) -> str:
    return (row.get("case", {}) or {}).get("label", "")


@dataclass
class IssueGroup:
    category: str
    op: str
    family: str
    opsets: set[int | str] = field(default_factory=set)
    surfaces: int = 0
    case_keys: set[tuple[str, int | str]] = field(default_factory=set)
    trigger_sigs: set[str] = field(default_factory=set)
    all_rows: list[dict] = field(default_factory=list)
    representative: dict | None = None
    valid_cases: int = 0

    def add(self, row: dict) -> None:
        self.opsets.add(_opset(row))
        self.surfaces += 1
        self.case_keys.add((row.get("report_op", self.op), row.get("case_index", "?")))
        self.trigger_sigs.add(_trigger_signature(row))
        self.all_rows.append(row)
        # Keep the simplest row as representative.
        if self.representative is None or _simplicity_score(row) < _simplicity_score(self.representative):
            self.representative = row

    @property
    def unique_triggers(self) -> int:
        return len(self.trigger_sigs)


def _load_profile_counts(paths: Iterable[Path]) -> dict[tuple[str, int | str], int]:
    out = {}
    for row in _read_jsonl(paths):
        op = row.get("op", "")
        if "@" in op:
            name, opset = op.rsplit("@", 1)
            out[(name, int(opset) if opset.isdigit() else opset)] = int(row.get("valid", 0))
    return out


def build_structured_groups(findings_paths: Iterable[Path], profile_paths: Iterable[Path] = ()) -> list[IssueGroup]:
    profiles = _load_profile_counts(profile_paths)
    groups: dict[tuple[str, str, str], IssueGroup] = {}
    for row in _read_jsonl(findings_paths):
        cat = _category(row.get("bug_class", ""))
        if not cat or row.get("classification") != "confirmed":
            continue
        op = _op(row)
        fam = _family(row)
        key = (cat, op, fam)
        groups.setdefault(key, IssueGroup(category=cat, op=op, family=fam)).add(row)

    for g in groups.values():
        g.valid_cases = sum(profiles.get((g.op, opset), 0) for opset in g.opsets)

    order = {"Incorrect Type": 0, "Incorrect Shape": 1, "Incorrect Errors": 2}
    return sorted(groups.values(), key=lambda g: (order[g.category], g.family, g.op, _fmt_opsets(g.opsets), -g.surfaces))


# ─────────────────────────────────────────────────────────────────────────────
# Table rendering
# ─────────────────────────────────────────────────────────────────────────────


def _kind_cell(g: IssueGroup) -> str:
    """One of: `required` (single trigger), or `example (1 of N)`."""
    if g.unique_triggers <= 1:
        return "**required**"
    return f"example (1/{g.unique_triggers})"


def _row_type(g: IssueGroup) -> list[str]:
    row = g.representative or {}
    case = row.get("case", {})
    ports, attrs_raw = _parse_trigger(case.get("label", ""))
    varying_fields, varying_attrs = _analyze_variation(g.all_rows)
    truth_dtype = (row.get("truth") or {}).get("dtype")
    claim_dtype = (row.get("claim") or {}).get("dtype")
    return [
        f"`{g.op}`",
        _fmt_opsets(g.opsets),
        _md_escape(_format_inputs(ports, varying_fields)),
        _md_escape(_format_attrs(attrs_raw, varying_attrs)),
        _kind_cell(g),
        _md_cell(truth_dtype),
        _md_cell(claim_dtype),
        _coverage_cell(len(g.case_keys), g.surfaces, g.valid_cases),
    ]


def _row_shape(g: IssueGroup) -> list[str]:
    row = g.representative or {}
    case = row.get("case", {})
    ports, attrs_raw = _parse_trigger(case.get("label", ""))
    varying_fields, varying_attrs = _analyze_variation(g.all_rows)
    truth = row.get("truth") or {}
    claim = row.get("claim") or {}
    return [
        f"`{g.op}`",
        _fmt_opsets(g.opsets),
        g.family,
        _md_escape(_format_inputs(ports, varying_fields)),
        _md_escape(_format_attrs(attrs_raw, varying_attrs)),
        _kind_cell(g),
        _md_shape(truth.get("shape")),
        _md_shape(claim.get("shape")),
        _coverage_cell(len(g.case_keys), g.surfaces, g.valid_cases),
    ]


def _row_error(g: IssueGroup) -> list[str]:
    row = g.representative or {}
    case = row.get("case", {})
    ports, attrs_raw = _parse_trigger(case.get("label", ""))
    varying_fields, varying_attrs = _analyze_variation(g.all_rows)
    err = row.get("claim_error") or row.get("note") or ""
    err_short = _md_escape(err.splitlines()[0][:140]) if err else "—"
    return [
        f"`{g.op}`",
        _fmt_opsets(g.opsets),
        g.family,
        _md_escape(_format_inputs(ports, varying_fields)),
        _md_escape(_format_attrs(attrs_raw, varying_attrs)),
        _kind_cell(g),
        f"`{err_short}`" if err_short != "—" else "—",
        _coverage_cell(len(g.case_keys), g.surfaces, g.valid_cases),
    ]


def _table(headers: list[str], rows: list[list[str]]) -> list[str]:
    if not rows:
        return ["_No confirmed findings._", ""]
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    out.append("")
    return out


def render_structured_report(findings_paths: Iterable[Path], profile_paths: Iterable[Path] = ()) -> str:
    groups = build_structured_groups(findings_paths, profile_paths)
    by_cat = defaultdict(list)
    for g in groups:
        by_cat[g.category].append(g)

    n_total = len(groups)
    n_type = len(by_cat["Incorrect Type"])
    n_shape = len(by_cat["Incorrect Shape"])
    n_err = len(by_cat["Incorrect Errors"])

    lines = [
        "# Structured onnx_tool issue report",
        "",
        f"Confirmed divergences vs. ORT, grouped by `(op, family, opsets)`. "
        f"**{n_total} issues**: {n_type} type, {n_shape} shape, {n_err} error.",
        "",
        "**Columns:**",
        "- **Inputs**: each port shown as `name: shape/dtype/fill`. `(init)` marks initializer (constant input).",
        "- **Attrs**: op attributes used in the failing case.",
        "- **`*` suffix** on any field means it *varies* across triggers — the shown value is just one example "
        "and other values also reproduce the bug. Unmarked values are required (consistent across all triggers).",
        "- **Repro**: `required` if a single Inputs+Attrs configuration triggers the bug; "
        "`example (1/N)` if N distinct configurations trigger it (we show the simplest).",
        "- **Cases**: `hits/valid_cases` — how many ORT-valid configurations onnx_tool got wrong. "
        "Trailing `(N surf)` means N raw findings collapsed into the same group.",
        "",
    ]

    # Incorrect Type
    lines += ["## Incorrect Type", ""]
    lines += _table(
        ["Op", "Opsets", "Inputs", "Attrs", "Repro", "ORT", "onnx_tool", "Cases"],
        [_row_type(g) for g in by_cat["Incorrect Type"]],
    )

    # Incorrect Shape
    lines += ["## Incorrect Shape", ""]
    lines += _table(
        ["Op", "Opsets", "Family", "Inputs", "Attrs", "Repro", "ORT shape", "onnx_tool shape", "Cases"],
        [_row_shape(g) for g in by_cat["Incorrect Shape"]],
    )

    # Incorrect Errors
    lines += ["## Incorrect Errors", ""]
    lines += _table(
        ["Op", "Opsets", "Family", "Inputs", "Attrs", "Repro", "onnx_tool error", "Cases"],
        [_row_error(g) for g in by_cat["Incorrect Errors"]],
    )

    return "\n".join(lines)
