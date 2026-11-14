from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0004_I01-E02_SOURCE_PREP_R03_20261030")
DOCX = ROOT / "docx" / "0004_I01-E02_R05_L06.docx"
PDF = ROOT / "render" / "0004_I01-E02_R05_L06_WordNative.pdf"
SHEET = ROOT / "render" / "CONTACT_SHEET_R05_L06.jpg"
PAGE_DIR = ROOT / "render" / "pages_R05_L06"
MANUSCRIPT = ROOT / "worker" / "0004_WRITER_MANUSCRIPT_CANDIDATE_R05.md"
REGISTER = ROOT / "SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R05.csv"
SOURCE_PACKET = ROOT / "SOURCE_PACKET_0004_I01-E02_R03.md"
BLUEPRINT = ROOT / "UNIQUE_BLUEPRINT_0004_I01-E02_R03.md"
CURRENT_ROW = ROOT / "source" / "BLUEPRINT_CURRENT_ROW_0004.jsonl"
PATCH = ROOT / "worker" / "repair_list_numbering_l06.py"
VERIFY = ROOT / "worker" / "verify_candidate_l06.py"
QA = ROOT / "qa"


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def save_once(name: str, data: dict) -> None:
    p = QA / name
    if p.exists():
        raise FileExistsError(p)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    docx_sha = sha(DOCX)
    pdf_sha = sha(PDF)
    sheet_sha = sha(SHEET)
    assert docx_sha == "8fe5abdc8b90592b47af67c5ef5d0d37947eec0cdbd55f6034fce82d3723a561"
    assert pdf_sha == "3ccaf47a6c03132d49196929d7fed86a9f6d0eeeda06905d96c238f545cb2d1d"
    assert len(list(PAGE_DIR.glob("page-*.png"))) == 21
    assert len(list((ROOT / "render" / "pages_R05_L05").glob("page-*.png"))) == 21

    now = datetime.now(timezone.utc).isoformat()
    repair_path = QA / "NUMBERING_REPAIR_RECEIPT_R05_L06.json"
    repair = json.loads(repair_path.read_text(encoding="utf-8"))
    repair["verification"].update({
        "native_word_open_export_and_visual_check": "PASS",
        "word_native_pdf_sha256": pdf_sha,
        "page_count": 21,
        "independent_semantic_review_exact_sha": "PENDING_TWO_REVIEWERS",
        "formal_acceptance": "UNKNOWN",
    })
    repair["updated_at_utc"] = now
    repair_path.write_text(json.dumps(repair, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    save_once("WORD_NATIVE_RENDER_R05_L06.json", {
        "receipt_id": "WORD_NATIVE_RENDER_R05_L06",
        "created_at_utc": now,
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "docx_sha256": docx_sha,
        "output_pdf": PDF.name,
        "output_pdf_sha256": pdf_sha,
        "pdf_bytes": PDF.stat().st_size,
        "page_count": 21,
        "native_application": "Microsoft Word COM, read-only open, ExportAsFixedFormat PDF",
        "export_status": "PASS",
        "word_process_id": "UNKNOWN; PowerShell PID variable collision prevented PID capture during successful export",
        "post_close_process_readback": "No newly remaining WINWORD process was observed; pre-existing user Word processes were preserved",
        "formal_acceptance": "UNKNOWN",
    })

    save_once("VISUAL_QA_R05_L06.json", {
        "receipt_id": "VISUAL_QA_R05_L06",
        "created_at_utc": now,
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "docx_sha256": docx_sha,
        "pdf_sha256": pdf_sha,
        "page_count": 21,
        "page_png_count": 21,
        "contact_sheet": SHEET.name,
        "contact_sheet_sha256": sheet_sha,
        "visual_method": "21-page contact-sheet inspection; high-resolution inspection of pages 13-16; exact pixel comparison against L05 render",
        "pixel_comparison": {
            "pages_unchanged": [i for i in range(1, 22) if i not in [13, 14, 15, 16]],
            "only_expected_changed_pages": [13, 14, 15, 16],
            "page_13_14_16_17_index_note": "PDF pages 13-16 contain the repaired independent numbering groups; all other page rasters are pixel-identical to L05 at the same render settings",
        },
        "fixed_visual_findings": {
            "pdf_page_13_14_section_6_2": "PASS; four balance checks display 1-4",
            "pdf_page_15_section_8_1": "PASS; two independent items display 1-2",
            "pdf_page_16_section_8_2": "PASS; two independent items display 1-2",
            "pdf_page_16_section_8_3": "PASS; two independent items display 1-2",
        },
        "layout_observation": "PDF page 10 contains the final U005 row of Table 4-1 group 3 without a repeated group header on that continuation page; the row is intact and no clipping or overlap was observed. Nonblocking observation retained for reviewer disposition.",
        "status": "PASS_WITH_NONBLOCKING_CONTINUATION_OBSERVATION",
        "formal_acceptance": "UNKNOWN",
    })

    save_once("LAYOUT_REPAIR_RECEIPT_R05_L06.json", {
        "receipt_id": "LAYOUT_REPAIR_RECEIPT_R05_L06",
        "created_at_utc": now,
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "source_l05_docx_sha256": "be55d8f06dd0179cf043cfd4c48ba76bbdb8c110de109a111d8c58dc91b48f85",
        "candidate_l06_docx_sha256": docx_sha,
        "source_manuscript_sha256": sha(MANUSCRIPT),
        "repair": "Set direct, independent restart-at-1 numbering instances for the existing ListNumber paragraphs under sections 6.2, 8.1, 8.2 and 8.3. No body text, table data, calculations, register entries or text run formatting changed.",
        "repair_script_sha256": sha(PATCH),
        "verification_script_sha256": sha(VERIFY),
        "word_native_pdf_sha256": pdf_sha,
        "changed_pages": [13, 14, 15, 16],
        "unchanged_pages_pixel_identical": 17,
        "remaining_observation": "Page 10 Table 4-1 group 3 continuation has a final U005 row without a repeated group header; row is intact and readable.",
        "status": "REPAIRED_CANDIDATE_PENDING_EXACT_SHA_REVIEW",
        "formal_acceptance": "UNKNOWN",
    })

    save_once("WORD_BUILD_RECEIPT_R05_L06.json", {
        "receipt_id": "WORD_BUILD_RECEIPT_R05_L06",
        "created_at_utc": now,
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "candidate": DOCX.name,
        "candidate_sha256": docx_sha,
        "bytes": DOCX.stat().st_size,
        "change_type": "Bounded OOXML list-numbering repair from L05; no substantive document rebuild",
        "source_docx_sha256": "be55d8f06dd0179cf043cfd4c48ba76bbdb8c110de109a111d8c58dc91b48f85",
        "source_manuscript_sha256": sha(MANUSCRIPT),
        "replacement_register_sha256": sha(REGISTER),
        "word_native_pdf_sha256": pdf_sha,
        "technical_qa": "PASS_TECHNICAL_CANDIDATE_ONLY",
        "visual_qa": "PASS_WITH_NONBLOCKING_CONTINUATION_OBSERVATION",
        "semantic_qa": "PENDING_TWO_REVIEWERS_EXACT_SHA",
        "formal_acceptance": "UNKNOWN",
    })

    save_once("CANDIDATE_EVIDENCE_MANIFEST_R05_L06.json", {
        "project_id": "TTQS_ONE",
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "official_checkbox_project_serial": "002",
        "state": "CANDIDATE",
        "revision": "R05_L06",
        "created_at_utc": now,
        "repository": "PT-Original-Point/ttqs-one",
        "branch": "work/ttqs-one-document-quality-contract-20261016",
        "source_packet_sha256": sha(SOURCE_PACKET),
        "unique_blueprint_sha256": sha(BLUEPRINT),
        "official_requirement_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
        "blueprint_current_row_sha256": sha(CURRENT_ROW),
        "manuscript_sha256": sha(MANUSCRIPT),
        "synthetic_register_sha256": sha(REGISTER),
        "docx_sha256": docx_sha,
        "word_native_pdf_sha256": pdf_sha,
        "technical_qa_receipt": {"file": "TECHNICAL_QA_R05_L06.json", "status": "PASS_TECHNICAL_CANDIDATE_ONLY"},
        "visual_qa_receipt": {"file": "VISUAL_QA_R05_L06.json", "status": "PASS_WITH_NONBLOCKING_CONTINUATION_OBSERVATION"},
        "semantic_qa": {"status": "PENDING", "reviewed_sha256": docx_sha},
        "formal_acceptance": "UNKNOWN",
        "real_execution": "UNKNOWN",
        "sample_boundary": "All sample data remain synthetic; no real survey, consent, delivery, approval or association execution is asserted.",
    })

    print(json.dumps({"docx_sha256": docx_sha, "pdf_sha256": pdf_sha, "contact_sheet_sha256": sheet_sha, "receipts_written": 5}, ensure_ascii=False))


if __name__ == "__main__":
    main()
