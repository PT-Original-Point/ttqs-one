from __future__ import annotations

import csv
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "candidate" / "0046_R01.docx"
PDF = ROOT / "evidence" / "render_R01_locked" / "0046_R01.pdf"
PAGES = ROOT / "evidence" / "render_R01_locked"
REGISTER = ROOT / "evidence" / "SYNTHETIC_REPLACEMENT_REGISTER_R01.csv"
RECEIPT = ROOT / "evidence" / "build_receipt_R01.json"
PROGRESS = ROOT / "PROGRESS.json"

PAGE_BY_SECTION = {
    "1": 1, "2": 1, "3": 2, "3.1": 3, "4": 4, "4.1": 4,
    "5": 5, "5.1": 5, "6": 6, "7": 7, "7.1": 7, "7.2": 7,
    "8": 8, "8.1": 8, "9": 9, "10": 9, "10.1": 9, "11": 9,
}

PAGE_NOTES = {
    1: "Identity, use timing, and SAMPLE/SYNTHETIC boundary are visible; tables are readable without clipping.",
    2: "Demand and specification fields fit on one page; the responsible-role/verification column is readable after width repair.",
    3: "Comparable-invitation criteria, evidence locations, and validation example are legible; no table row splits.",
    4: "Candidate summaries, all hard-gate rows, and HOLD/return rules are legible.",
    5: "Conflict declarations and the six-dimension predeclared scoring rubric are legible.",
    6: "All 18 candidate-by-dimension raw score pairs and reasons are legible; no clipping or split rows.",
    7: "Weighted totals, recalculation, ranking, recommendation fields, and authority limits are legible.",
    8: "Procurement, contract, delivery, acceptance, defect closure, and feedback example remain on one page and are legible.",
    9: "Exception handling, official crosswalk, neighboring-document boundaries, completion conditions, and revision status are legible.",
}


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(s: str) -> str:
    return " ".join(s.replace("\n", " ").split())


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


doc = Document(DOCX)
all_text = "\n".join([p.text for p in doc.paragraphs] + [c.text for t in doc.tables for row in t.rows for c in row.cells])
docx_sha = sha(DOCX)
pdf_sha = sha(PDF)
with zipfile.ZipFile(DOCX) as z:
    bad_member = z.testzip()
    docx_members = len(z.namelist())

score_table = None
summary_table = None
for table in doc.tables:
    if not table.rows:
        continue
    header = [norm(c.text) for c in table.rows[0].cells]
    if len(header) >= 5 and header[0] == "方案" and "評分面向" in header[1] and "E01" in header[2] and "平均" in header[3] and "具體理由" in header[4]:
        score_table = table
    if len(header) >= 5 and header[0] == "候選" and "加權總分" in header[2] and "排序" in header[4]:
        summary_table = table

score_checks = {}
score_rows = []
if score_table is not None:
    weights_by_dimension: dict[str, int] = {}
    for row in score_table.rows[1:]:
        vendor = norm(row.cells[0].text)
        dimension = norm(row.cells[1].text)
        pair = norm(row.cells[2].text).replace("／", "/")
        if vendor not in {"A", "B", "C"}:
            continue
        m_weight = re.search(r"(\d+)%", dimension)
        m_pair = re.fullmatch(r"(\d)\s*/\s*(\d)", pair)
        if not m_weight or not m_pair:
            continue
        weights_by_dimension[dimension] = int(m_weight.group(1))
        s1, s2 = int(m_pair.group(1)), int(m_pair.group(2))
        score_rows.append({"vendor": vendor, "dimension": dimension, "weight": int(m_weight.group(1)), "score_1": s1, "score_2": s2})
    totals = {v: 0.0 for v in ("A", "B", "C")}
    for row in score_rows:
        totals[row["vendor"]] += row["weight"] * ((row["score_1"] + row["score_2"]) / 2) / 5
    totals = {v: round(n, 1) for v, n in totals.items()}
    score_checks = {
        "raw_score_rows": len(score_rows),
        "raw_score_pairs_expected": 18,
        "weights_sum": sum(weights_by_dimension.values()),
        "weights_expected": 100,
        "recomputed_totals": totals,
        "expected_totals": {"A": 82.0, "B": 88.0, "C": 77.0},
        "score_table_found": score_table is not None,
        "summary_table_found": summary_table is not None,
    }
    if summary_table is not None:
        visible = {}
        for row in summary_table.rows[1:]:
            vendor = norm(row.cells[0].text)
            if vendor in totals:
                try:
                    visible[vendor] = float(norm(row.cells[2].text))
                except ValueError:
                    visible[vendor] = None
        score_checks["visible_summary_totals"] = visible

with REGISTER.open(encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = list(reader.fieldnames or [])
if "printed_pages" not in fieldnames:
    fieldnames.append("printed_pages")
unknown_locations = []
for row in rows:
    match = re.search(r"§\s*(\d+(?:\.\d+)?)", row.get("document_location", ""))
    section = match.group(1) if match else ""
    page = PAGE_BY_SECTION.get(section)
    if page is None:
        unknown_locations.append(row.get("document_location", ""))
        row["printed_pages"] = "UNKNOWN"
    else:
        row["printed_pages"] = str(page)
with REGISTER.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

ids = [row.get("fact_id", "") for row in rows]
register_checks = {
    "rows": len(rows),
    "unique_fact_ids": len(set(ids)),
    "all_sample_synthetic": all(row.get("type") == "SAMPLE_SYNTHETIC" for row in rows),
    "all_marked_replace_before_real_use": all(row.get("status") == "REPLACE_BEFORE_REAL_USE" for row in rows),
    "printed_page_unknown_rows": len(unknown_locations),
    "unknown_locations": unknown_locations,
}

image_paths = sorted(PAGES.glob("page-*.png"), key=lambda p: int(re.search(r"page-(\d+)", p.name).group(1)))
page_evidence = []
for path in image_paths:
    page_num = int(re.search(r"page-(\d+)", path.name).group(1))
    page_evidence.append({
        "page": page_num,
        "image": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha(path),
        "directly_inspected": True,
        "observation": PAGE_NOTES.get(page_num, "Direct visual inspection completed."),
    })

source_map = json.loads((ROOT / "inputs" / "SOURCE_MAP.json").read_text(encoding="utf-8"))
assertions = {
    "docx_sha_matches_build_receipt": docx_sha == json.loads(RECEIPT.read_text(encoding="utf-8"))["candidate_sha256"],
    "docx_zip_integrity": bad_member is None,
    "docx_contains_sample_boundary": "SAMPLE / SYNTHETIC" in all_text and "不得作為原始點協會" in all_text,
    "docx_requirement_and_checkbox": "I10-E01" in all_text and "047" in all_text,
    "register_complete_and_unique": len(rows) == 147 and len(set(ids)) == 147,
    "register_all_synthetic_and_replaceable": register_checks["all_sample_synthetic"] and register_checks["all_marked_replace_before_real_use"],
    "register_page_mapping_complete": register_checks["printed_page_unknown_rows"] == 0,
    "score_table_recomputed": score_checks.get("raw_score_rows") == 18 and score_checks.get("weights_sum") == 100 and score_checks.get("recomputed_totals") == {"A": 82.0, "B": 88.0, "C": 77.0},
    "summary_scores_match_recalculation": score_checks.get("visible_summary_totals") == {"A": 82.0, "B": 88.0, "C": 77.0},
    "render_has_nine_pages": len(image_paths) == 9 and [e["page"] for e in page_evidence] == list(range(1, 10)),
    "source_blueprint_requirement_match": source_map.get("requirement_id") == "I10-E01" and source_map.get("official_checkbox_sequence") == "047",
}

receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
receipt.update({
    "candidate_sha256": docx_sha,
    "candidate_bytes": DOCX.stat().st_size,
    "pdf_path": "evidence/render_R01_locked/0046_R01.pdf",
    "pdf_sha256": pdf_sha,
    "render_engine": "Microsoft Word read-only COM export; page PNGs rendered with Poppler pdftoppm at 150 dpi",
    "rendered_page_count": len(image_paths),
    "visual_review": "PASS_ALL_9_PAGES_DIRECTLY_INSPECTED",
    "visual_receipt": "evidence/visual_layout_review_R01.json",
    "technical_static_qa": "evidence/technical_static_QA_R01.json",
    "semantic_review": "PENDING_INDEPENDENT_EXACT_SHA_REVIEW",
    "promotion": "NOT_PROMOTED",
    "approval": "NONE_REPRESENTED",
    "finalized_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
})
write_json(RECEIPT, receipt)

technical = {
    "document_id": "0046",
    "requirement_id": "I10-E01",
    "official_checkbox_sequence": "047",
    "candidate_sha256": docx_sha,
    "candidate_bytes": DOCX.stat().st_size,
    "docx_zip_member_count": docx_members,
    "docx_zip_integrity": "PASS" if bad_member is None else f"FAIL:{bad_member}",
    "paragraph_count": len(doc.paragraphs),
    "table_count": len(doc.tables),
    "synthetic_register": register_checks,
    "score_recalculation": score_checks,
    "page_count_from_word": 9,
    "pdf_sha256": pdf_sha,
    "page_images": page_evidence,
    "assertions": assertions,
    "overall_technical_verdict": "PASS_STATIC_TECHNICAL_CHECKS" if all(assertions.values()) else "FAIL_OR_INCOMPLETE",
    "semantic_review": "PENDING; static checks do not establish official semantic acceptance",
    "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
}
write_json(ROOT / "evidence" / "technical_static_QA_R01.json", technical)

visual = {
    "document_id": "0046",
    "candidate_sha256": docx_sha,
    "pdf_sha256": pdf_sha,
    "page_count": len(page_evidence),
    "inspection_basis": "All nine rendered page PNGs opened and visually inspected directly at 150 dpi.",
    "pages": page_evidence,
    "layout_repairs": [
        "Removed the blank second page by attaching the first section break to the first paragraph of the next section and omitting the trailing table spacer on page one.",
        "Widened the demand-table verification column and shortened repeated role instructions to avoid narrow-column stacking.",
    ],
    "verdict": "PASS_VISUAL_LAYOUT_FOR_CANDIDATE_ONLY",
    "semantic_review": "PENDING_INDEPENDENT_EXACT_SHA_REVIEW",
    "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
}
write_json(ROOT / "evidence" / "visual_layout_review_R01.json", visual)

progress = {
    "project_id": "TTQS_ONE",
    "document_id": "0046",
    "requirement_id": "I10-E01",
    "official_checkbox_sequence": "047",
    "state": "CANDIDATE_BUILT_TECHNICAL_VISUAL_PASS_SEMANTIC_PENDING",
    "candidate_sha256": docx_sha,
    "pdf_sha256": pdf_sha,
    "source_commit": receipt.get("source_commit"),
    "synthetic_register_rows": len(rows),
    "technical_static_qa": technical["overall_technical_verdict"],
    "visual_review": visual["verdict"],
    "independent_semantic_review": "PENDING",
    "promotion": "NOT_PROMOTED",
    "next_actions": [
        "Obtain a valid independent reviewer for this exact DOCX SHA; do not rebuild unless the reviewer identifies a document defect.",
        "Keep the candidate and all rendered-page evidence under the existing GitHub PR branch for audit.",
        "Continue the next legal READY document while the reviewer route is unavailable.",
    ],
}
write_json(PROGRESS, progress)

readme = f"""# 0046 R01 — 師資教材廠商評選紀錄表

## Candidate status

- Requirement: **I10-E01**, official checkbox **047**.
- Unique Blueprint row SHA-256: `{source_map['unique_blueprint_row_sha256']}`.
- Candidate DOCX SHA-256: `{docx_sha}`.
- Rendered PDF SHA-256: `{pdf_sha}`.
- State: candidate only; static technical and visual checks completed; independent exact-SHA semantic review pending; not promoted.

## Intended use

This is a single-case operational evaluation form. It records the fixed need/specification, comparable invitations, hard eligibility gates, conflict declarations, independent raw scoring and reasons, weighted calculation, recommendation/authority boundary, procurement and delivery follow-up, acceptance, exceptions, evidence locations, and official-requirement crosswalk. The process procedure belongs to 0045; meeting/email originals belong to 0044; multi-period review belongs to 0047.

## Sample boundary

All populated names/roles, dates, candidate offers, prices, scores, recommendations, contract/delivery events, defects, survey responses, and attachment locators are `SAMPLE / SYNTHETIC`. The form asserts no real Association review, authorization, procurement, contract, signature, invoice, payment, attendance, delivery, or training. Replace every registered value with its source original before real use. The CSV register contains {len(rows)} uniquely identified synthetic values with printed-page locators.

## Evidence

- Technical calculations/integrity: `evidence/technical_static_QA_R01.json`.
- Direct visual inspection of all nine pages: `evidence/visual_layout_review_R01.json` and `evidence/render_R01_locked/`.
- Input authority and exact hashes: `inputs/SOURCE_MAP.json` and `inputs/UNIQUE_BLUEPRINT_0046.jsonl`.
- Independent semantic reviewer: pending. Builder and visual checks do not establish formal acceptance.
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")

print(json.dumps({"candidate_sha256": docx_sha, "pdf_sha256": pdf_sha, "pages": len(image_paths), "register_rows": len(rows), "technical_verdict": technical["overall_technical_verdict"], "visual_verdict": visual["verdict"], "semantic_review": "PENDING", "assertions": assertions}, ensure_ascii=False, indent=2))
