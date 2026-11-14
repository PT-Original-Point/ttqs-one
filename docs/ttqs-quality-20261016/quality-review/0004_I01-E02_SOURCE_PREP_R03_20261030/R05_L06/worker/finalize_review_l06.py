from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0004_I01-E02_SOURCE_PREP_R03_20261030")
DOCX = ROOT / "docx" / "0004_I01-E02_R05_L06.docx"
PDF = ROOT / "render" / "0004_I01-E02_R05_L06_WordNative.pdf"
QA = ROOT / "qa"
REVIEW = ROOT / "worker" / "review"
EXPECTED_DOCX = "8fe5abdc8b90592b47af67c5ef5d0d37947eec0cdbd55f6034fce82d3723a561"
EXPECTED_PDF = "3ccaf47a6c03132d49196929d7fed86a9f6d0eeeda06905d96c238f545cb2d1d"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    docx_sha, pdf_sha = sha(DOCX), sha(PDF)
    assert docx_sha == EXPECTED_DOCX and pdf_sha == EXPECTED_PDF
    reviewers = []
    for name, agent_id, filename in [
        ("Zeno", "01a18a0f-38ea-7590-b3f3-f5ad5c0b67e2", "REVIEWER_ZENO_R05_L06_RAW.md"),
        ("Godel", "01a18a0f-3984-7ca3-9bfe-b0ba6ff1cdcb", "REVIEWER_GODEL_R05_L06_RAW.md"),
    ]:
        p = REVIEW / filename
        text = p.read_text(encoding="utf-8")
        assert docx_sha in text, f"Reviewer {name} response does not name the exact DOCX SHA"
        assert "PASS" in text and "正式接受" in text, f"Reviewer {name} response is missing verdict or acceptance limitation"
        if name == "Zeno":
            assert "977" in text and "1–4" in text
        else:
            assert "977" in text and "80.0%" in text
        reviewers.append({
            "reviewer": name,
            "agent_id": agent_id,
            "raw_response_file": filename,
            "raw_response_sha256": sha(p),
            "verdict": "PASS",
            "reviewed_docx_sha256": docx_sha,
            "reviewed_pdf_sha256": pdf_sha,
            "modified_artifact": False,
        })

    now = datetime.now(timezone.utc).isoformat()
    receipt = {
        "receipt_id": "SEMANTIC_REVIEW_R05_L06",
        "created_at_utc": now,
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "official_checkbox_project_serial": "002",
        "docx_sha256": docx_sha,
        "pdf_sha256": pdf_sha,
        "verdict": "PASS",
        "scope": [
            "exact candidate hash stable before and after review",
            "repair of prior L05 independent list-numbering defect",
            "official requirement, genre and negative-neighbor mapping",
            "SAMPLE/REAL boundary and cross-document fact consistency",
            "sample flow equations, rates and replacement register linkage",
            "Word/PDF readability and specified page locators",
        ],
        "reviewers": reviewers,
        "conclusion_limit": "Independent semantic candidate review only. Does not constitute formal association acceptance, REAL execution evidence, or approval.",
        "formal_acceptance": "UNKNOWN",
    }
    out = QA / "SEMANTIC_REVIEW_R05_L06.json"
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for filename, updates in [
        ("CANDIDATE_EVIDENCE_MANIFEST_R05_L06.json", {"semantic_qa": {"status": "PASS", "reviewed_sha256": docx_sha, "receipt": out.name, "reviewers": reviewers}, "formal_acceptance": "UNKNOWN"}),
        ("WORD_BUILD_RECEIPT_R05_L06.json", {"semantic_qa": "PASS exact DOCX SHA, two independent reviewers", "semantic_review_receipt": out.name, "formal_acceptance": "UNKNOWN"}),
        ("NUMBERING_REPAIR_RECEIPT_R05_L06.json", {"verification": {"independent_semantic_review_exact_sha": "PASS", "reviewed_docx_sha256": docx_sha, "formal_acceptance": "UNKNOWN"}}),
        ("TECHNICAL_QA_R05_L06.json", {"independent_semantic_review_exact_sha": "PASS", "semantic_review_receipt": out.name, "formal_acceptance": "UNKNOWN"}),
    ]:
        p = QA / filename
        data = json.loads(p.read_text(encoding="utf-8"))
        data.update(updates)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({"docx_sha256": docx_sha, "pdf_sha256": pdf_sha, "semantic_verdict": "PASS", "reviewers": reviewers, "formal_acceptance": "UNKNOWN"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
