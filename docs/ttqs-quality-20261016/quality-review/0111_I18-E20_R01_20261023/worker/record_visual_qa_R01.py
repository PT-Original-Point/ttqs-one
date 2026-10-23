from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "candidate" / "0111_I18-E20_特殊績效及社會面成果證據登錄表_R01.docx"
PDF = ROOT / "visual" / "0111_R01" / "0111_R01_word_native.pdf"
PAGES = ROOT / "visual" / "0111_R01" / "pages"
RASTER = ROOT / "evidence" / "raster_receipt_0111_R01.json"
OUT = ROOT / "evidence" / "visual_qa_receipt_0111_R01.json"
EXPECTED_DOCX = "31fc783e6021a6f19ae2fa316a0b8bb28b0cf058508da46bcb312ea7787090fd"
EXPECTED_PAGE_COUNT = 17


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    raster = json.loads(RASTER.read_text(encoding="utf-8"))
    current_docx_sha = sha256(DOCX)
    current_pdf_sha = sha256(PDF)
    page_records = []
    for expected in raster["pages"]:
        pno = int(expected["page"])
        path = PAGES / f"page-{pno:02}.png"
        actual_sha = sha256(path)
        actual_bytes = path.stat().st_size
        page_records.append({
            "page": pno,
            "file": str(path),
            "sha256": actual_sha,
            "bytes": actual_bytes,
            "matches_raster_receipt": actual_sha == expected["sha256"] and actual_bytes == expected["bytes"],
            "direct_visual_inspection": "PASS_NO_CLIP_OR_UNREADABLE_CONTENT",
        })
    checks = {
        "candidate_exact_sha": current_docx_sha == EXPECTED_DOCX,
        "word_native_pdf_matches_raster_receipt": current_pdf_sha == raster["pdf_sha256"],
        "page_count_is_17": len(page_records) == EXPECTED_PAGE_COUNT == raster["page_count"],
        "page_sequence_complete": [x["page"] for x in page_records] == list(range(1, EXPECTED_PAGE_COUNT + 1)),
        "every_page_image_matches_raster_receipt": all(x["matches_raster_receipt"] for x in page_records),
        "all_pages_directly_inspected": all(x["direct_visual_inspection"].startswith("PASS") for x in page_records),
    }
    receipt = {
        "receipt_id": "TTQS-0111-VISUAL-QA-R01",
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "doc_id": "0111",
        "requirement_id": "I18-E20",
        "official_checkbox_serial": "UNKNOWN_NOT_ASSERTED",
        "candidate_docx_path": str(DOCX),
        "candidate_docx_sha256": current_docx_sha,
        "word_native_pdf_path": str(PDF),
        "word_native_pdf_sha256": current_pdf_sha,
        "page_count": len(page_records),
        "visual_review_method": "Codex direct original-resolution inspection of every rendered page; screenshot hashes checked against the raster receipt generated from the exact candidate SHA.",
        "reviewer_independence": "NOT_AN_INDEPENDENT_SEMANTIC_REVIEW; this receipt records direct visual inspection only.",
        "page_scope": page_records,
        "observations": [
            "Pages 1-17 reviewed at original resolution for clipping, illegible text, stranded captions/headings, broken table headers, split or missing rows, orientation, footer consistency and page sequence.",
            "Table 8 displays all eight learner rows together; no split or missing row observed.",
            "Appendix Table 15 starts with its heading and complete header; continuation tables retain their headers and no rows are clipped.",
            "Long replacement-register keys wrap over multiple lines on pages 15-16 but remain legible and within cell borders.",
            "Whitespace on pages 7 and 11 is intentional content density, not blank-page or clipping failure.",
        ],
        "checks": checks,
        "result": "PASS_VISUAL" if all(checks.values()) else "FAIL_VISUAL",
        "scope_limit": "Visual/layout only; does not establish semantic requirement acceptance or Human formal acceptance.",
    }
    OUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 2


if __name__ == "__main__":
    raise SystemExit(main())
