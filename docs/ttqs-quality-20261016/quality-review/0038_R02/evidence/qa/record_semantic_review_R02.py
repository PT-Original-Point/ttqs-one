from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QA = ROOT / "evidence" / "qa"
DOCX = ROOT / "candidate" / "0038_R02.docx"
PDF = ROOT / "evidence" / "render" / "0038_R02.pdf"
RAW = QA / "independent_semantic_review_R02.md"
PROGRESS = ROOT / "PROGRESS.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


expected_docx = "bdb6ef07c1aacd31f638cdad511012777d2f1b9d2c9f5f307252dd62de0170a4"
expected_pdf = "f549d34db5d841dc04b61df3ce217a7ad1e2e5ee97d5f53106896ad3f5776012"
docx_sha = sha256(DOCX)
pdf_sha = sha256(PDF)
if docx_sha != expected_docx or pdf_sha != expected_pdf:
    raise SystemExit(f"exact-SHA mismatch: DOCX={docx_sha}; PDF={pdf_sha}")
raw_sha = sha256(RAW)
raw_text = RAW.read_text(encoding="utf-8")
if expected_docx not in raw_text or expected_pdf not in raw_text or "整體語意判定：PASS" not in raw_text:
    raise SystemExit("raw reviewer record does not bind both artifact SHAs and PASS")

receipt = {
    "project_id": "TTQS_ONE",
    "doc_id": "0038",
    "requirement_id": "I08-E02",
    "official_checkbox_sequence": "039",
    "candidate": "0038_R02",
    "candidate_sha256": docx_sha,
    "render_pdf_sha256": pdf_sha,
    "page_count": 14,
    "reviewer_route": "Fresh independent Codex subagent review; reviewer is separate from DOCX builder",
    "reviewer_agent_id": "01a14596-0f8b-7bd0-b192-f9e07ef7957c",
    "verdict": "PASS",
    "criteria_passed": 9,
    "criteria_total": 9,
    "findings": [],
    "review_scope": [
        "official requirement and Unique Blueprint mapping",
        "title-blind genre and 0037/0039 negative-neighbor distinction",
        "small volunteer-association operational usability",
        "SAMPLE/REAL and authority boundary",
        "row-level execution trace and 24-case replacement-register consistency",
        "official-requirement-to-fields/source/decision/review crosswalk",
        "recomputation of case totals, denominators, rates, weighted alternatives and B08 exception",
        "direct visual inspection of all 14 rendered pages",
    ],
    "r01_findings_resolved": [
        "row-level channel, consent, inclusion reason, missing/duplicate/correction trace",
        "explicit requirement-to-record/source/decision/review crosswalk",
    ],
    "review_raw_file": "evidence/qa/independent_semantic_review_R02.md",
    "review_raw_sha256": raw_sha,
    "formal_acceptance": "NOT_GRANTED",
    "promotion": "NOT_PROMOTED",
}
(QA / "semantic_review_receipt_R02.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

progress = json.loads(PROGRESS.read_text(encoding="utf-8"))
if progress.get("candidate_sha256") != docx_sha:
    raise SystemExit("PROGRESS candidate SHA changed unexpectedly")
progress["status"] = "CANDIDATE_BUILT; technical=PASS; visual=PASS; independent_semantic_review=PASS; formal_acceptance=NOT_GRANTED"
progress["review"].update({
    "semantic": "PASS",
    "semantic_review_sha256": raw_sha,
    "semantic_review_receipt": "evidence/qa/semantic_review_receipt_R02.json",
    "reviewer_agent_id": receipt["reviewer_agent_id"],
    "exact_sha_bound_review": True,
    "formal_acceptance": "NOT_GRANTED",
})
PROGRESS.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

for name in ("technical_qa.json", "visual_qa.json"):
    p = QA / name
    data = json.loads(p.read_text(encoding="utf-8"))
    data["independent_semantic_review"] = "PASS"
    data["semantic_review_candidate_sha256"] = docx_sha
    data["semantic_review_raw_sha256"] = raw_sha
    data["formal_acceptance"] = "NOT_GRANTED"
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
text = text.replace("獨立語意審查待 exact-SHA 回覆", "獨立語意審查 PASS（exact SHA 綁定）")
text = text.replace("相應 exact-SHA 收據為準。", "相應 exact-SHA 收據為準；本件正式接受仍未授與。")
readme.write_text(text, encoding="utf-8")

print(json.dumps({"candidate_sha256": docx_sha, "pdf_sha256": pdf_sha, "raw_review_sha256": raw_sha, "semantic": receipt["verdict"], "formal_acceptance": "NOT_GRANTED"}, ensure_ascii=False))
