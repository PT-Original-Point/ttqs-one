#!/usr/bin/env python3
import hashlib, json, re, sys
from pathlib import Path

base = Path(__file__).resolve().parents[1]
p = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "candidate" / "0083_R01_body.md"
text = p.read_text(encoding="utf-8-sig")
lines = text.splitlines()
headings = [ln.strip() for ln in lines if re.match(r"^#{1,3}\s", ln)]
checks = {}
checks["identity"] = all(x in text for x in ["DOCX 0083", "I17C-E02", "089"])
checks["correct_genre"] = "個別學員" in text and "行動計畫" in text and "追蹤" in text
checks["forms"] = all(x in text for x in ["Form-G1", "Form-T1", "Form-A1", "Form-E1"])
checks["sample_boundary"] = all(x in text for x in ["SAMPLE/SYNTHETIC", "REAL = UNKNOWN/HOLD", "FORMAL_ACCEPTANCE = NOT_GRANTED", "NOT EXECUTED"])
checks["cross_document_boundary"] = "0082" in text and "I17C-E01" in text and "088" in text
checks["replacement_register_reference"] = "SYNTHETIC_REPLACEMENT_REGISTER_0083_R03.csv" in text and "R-001" in text and "R-081" in text
checks["essential_dates"] = all(x in text for x in ["2026-02-06", "2026-03-05", "2026-03-06", "2026-03-09", "2026-04-03", "2026-05-01", "2026-05-29", "2026-06-26"])
checks["essential_rates"] = all(x in text for x in ["75.0%", "25.0%", "100.0%", "58.3%", "83.3%"])
checks["sample_aid_status"] = all(x in text for x in ["AID-01", "2026-04-13", "PROVIDED", "AID-02", "REQUESTED", "PENDING"])
checks["decision_actions"] = all(x in text for x in ["HOLD", "RETURN", "REJECT", "REVERIFY"])
checks["not_official_acceptance"] = "NOT_GRANTED" in text and "REAL = UNKNOWN/HOLD" in text
table_groups = []
group = []
for i, line in enumerate(lines + [""]):
    if line.strip().startswith("|") and line.strip().endswith("|"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            group.append((i + 1, len(cells), line))
    elif group:
        widths = sorted(set(row[1] for row in group))
        if len(widths) > 1:
            table_groups.append({"line_start": group[0][0], "line_end": group[-1][0], "widths": widths, "lines": [r[0] for r in group]})
        group = []
checks["markdown_table_groups_consistent"] = not table_groups
report = {
    "schema": "ttqs-0083-body-markdown-qa-v1",
    "document_id": "0083",
    "requirement_id": "I17C-E02",
    "official_checkbox": "089",
    "path": str(p),
    "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
    "bytes": p.stat().st_size,
    "heading_count": len(headings),
    "word_count_approx": len(text.split()),
    "checks": checks,
    "table_width_findings": table_groups,
    "failed_checks": [k for k, v in checks.items() if not v],
    "scope": "Deterministic text-structure checks only; not semantic acceptance or Word visual QA.",
    "result": "PASS_STRUCTURE" if all(checks.values()) else "FAIL",
}
out = base / "evidence" / "body_markdown_qa_R01.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=True))
if not all(checks.values()):
    sys.exit(1)
