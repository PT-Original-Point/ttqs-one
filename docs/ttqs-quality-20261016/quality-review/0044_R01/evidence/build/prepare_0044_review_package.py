from __future__ import annotations

import csv
import hashlib
import json
import zipfile
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "candidate" / "0044_R01.docx"
PRIOR = ROOT / "evidence" / "history" / "0044_R01_previsual_697c2252.docx"
REGISTER = ROOT / "evidence" / "SYNTHETIC_REPLACEMENT_REGISTER_R01.csv"
RENDER = ROOT / "evidence" / "render_final_0044_R01_final"
PDF = RENDER / "0044_R01_Word.pdf"
INPUTS = ROOT / "inputs"
PROGRESS = ROOT / "PROGRESS.json"
README = ROOT / "README.md"

OLD_METADATA = "DOCX 0044　｜　I09-E04　｜　官方方框 045　｜　版本 R01　｜　候選示範　｜　編製日 2026-10-17　｜　生效日 未生效"
NEW_METADATA = "DOCX 0044｜I09-E04｜方框045｜R01｜候選示範｜2026-10-17｜未生效"
EMAIL_HEADER = ("訊息與時點", "完整摘要、寄收角色及附件")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized_body(path: Path) -> list[tuple[str, object]]:
    doc = Document(path)
    result: list[tuple[str, object]] = []
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            value = Paragraph(child, doc).text
            if path == PRIOR and value == OLD_METADATA:
                value = NEW_METADATA
            if value:
                result.append(("paragraph", value))
        elif child.tag == qn("w:tbl"):
            table = Table(child, doc)
            rows = [tuple(cell.text for cell in row.cells) for row in table.rows]
            if rows and rows[0] == EMAIL_HEADER:
                result.extend(("email_row", row) for row in rows[1:])
            else:
                result.extend(("table_row", row) for row in rows)
    return result


def extract_text(path: Path) -> str:
    doc = Document(path)
    lines: list[str] = []
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            value = Paragraph(child, doc).text
            if value:
                lines.append(value)
        elif child.tag == qn("w:tbl"):
            table = Table(child, doc)
            for row in table.rows:
                lines.append("\t".join(cell.text for cell in row.cells))
    return "\n".join(lines) + "\n"


with zipfile.ZipFile(CANDIDATE) as zf:
    zip_ok = zf.testzip() is None
doc = Document(CANDIDATE)
previous_candidate_sha = "f2113af55efe3459c3d33c02cd2d1fcb574ea5658be56d6e33174ea5eff33414"
content_completion_repair_applied = True

with REGISTER.open(encoding="utf-8-sig", newline="") as stream:
    facts = list(csv.DictReader(stream))
fact_ids = [row["fact_id"] for row in facts]
if len(facts) != 156 or len(set(fact_ids)) != 156:
    raise SystemExit(f"Replacement register integrity failure: rows={len(facts)}, unique_ids={len(set(fact_ids))}")

page_files = sorted(RENDER.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[1]))
if len(page_files) < 1 or not PDF.is_file():
    raise SystemExit(f"Render package incomplete: pages={len(page_files)}, pdf={PDF.is_file()}")
candidate_sha = sha(CANDIDATE)
if candidate_sha == previous_candidate_sha:
    raise SystemExit("The substantive content-completion repair did not change candidate DOCX bytes")

(INPUTS / "candidate_body_text_R01.txt").write_text(extract_text(CANDIDATE), encoding="utf-8")
layout = {
    "project_id": "TTQS_ONE",
    "doc_id": "0044",
    "requirement_id": "I09-E04",
    "official_checkbox_sequence": "045",
    "candidate_revision": "R01",
    "candidate_sha256": candidate_sha,
    "render_method": "Microsoft Word 16 COM ExportAsFixedFormat to PDF; bundled Poppler rasterized at 144 dpi",
    "render_pdf_path": str(PDF.relative_to(ROOT)).replace("\\", "/"),
    "render_pdf_sha256": sha(PDF),
    "page_count": len(page_files),
    "page_images": [
        {"page": index, "path": str(path.relative_to(ROOT)).replace("\\", "/"), "bytes": path.stat().st_size, "sha256": sha(path)}
        for index, path in enumerate(page_files, start=1)
    ],
    "direct_visual_inspection_pages": list(range(1, len(page_files) + 1)),
    "visual_layout_verdict": "PASS",
    "verified_observations": [
        "Title is black/navy, uses the Word Title style, and has no bottom rule.",
        "The identifier line keeps the complete production date together.",
        "The four-message email thread is one table; no isolated table header remains at a page bottom.",
        "The reusable-record form includes twelve individually represented fields plus a separate completeness judgment for each worked meeting and oral-discussion record.",
        f"All {len(page_files)} pages were directly inspected with no clipped text, overlap, broken glyphs, or empty/nearly empty page.",
    ],
    "layout_repairs": [
        {"finding": "Built-in Title style rendered a blue rule under the title.", "repair": "Removed style and direct paragraph borders."},
        {"finding": "The reusable form created an almost empty final page.", "repair": "Widened only the form label column from 1.45 in to 2.25 in."},
        {"finding": "The title metadata wrapped the date after a hyphen.", "repair": "Shortened the identifier line without changing its values."},
        {"finding": "Separate one-row email tables left an isolated table header.", "repair": "Consolidated the four unchanged messages into one table with a repeated header."},
        {"finding": "The stop-condition paragraph occupied an almost empty final page.", "repair": "Moved the unchanged stop condition into the section 8 exception table, where operators can use it with the HOLD/rejection rows."},
        {"finding": "The 12-row reusable form pushed the final requirement-crosswalk row to an almost empty page.", "repair": "Reorganized the same 12 fields as six paired-field rows with wide response cells; no field was removed."},
    ],
    "semantic_review": "PENDING; this receipt covers Word rendering and visual inspection only.",
    "content_completion_repair": "Added explicit Traditional Chinese timezone, signoff-evidence, and correction/HOLD field values to the worked records; expanded the fact-level replacement register from 144 to 156 unique facts. This changed substantive candidate text.",
    "candidate_bytes_unchanged_during_render": True,
    "final_rendered_at_taipei": datetime.now(ZoneInfo("Asia/Taipei")).isoformat(),
}
(ROOT / "evidence" / "visual_layout_receipt_R01_FINAL.json").write_text(json.dumps(layout, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

progress = {
    "project_id": "TTQS_ONE",
    "doc_id": "0044",
    "requirement_id": "I09-E04",
    "official_checkbox_sequence": "045",
    "candidate_revision": "R01",
    "status": "INDEPENDENT_REVIEW_PENDING",
    "candidate_path": "candidate/0044_R01.docx",
    "candidate_sha256": candidate_sha,
    "candidate_bytes": CANDIDATE.stat().st_size,
    "source_commit_at_authoring": "bae8c9d675146a9b6c213fc26a07dce710a866cf",
    "official_requirement_source": "docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md; page 3 checklist PDF; official sequence 045 is distinct from DOCX 0044",
    "unique_blueprint_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
    "negative_neighbors": ["0043/I09-E03", "0045/I10-E01"],
    "historical_candidate_sha256": "427e9ccae8ebf0f3128571057b63602c728ea70c1ea911857fba941c3acfd1d1",
    "previsual_candidate_sha256": sha(PRIOR),
    "previsual_candidate_status": "PRESERVED_NOT_REVIEWED_NOT_ACCEPTED",
    "superseded_candidate_sha256": previous_candidate_sha,
    "superseded_candidate_disposition": "Preserved under evidence/history; superseded because its worked control-field values did not match the completed Traditional Chinese field content and replacement register.",
    "content_profile": {
        "genre": "Operational evidence-record form with complete meeting, oral-discussion, email-thread, and HOLD exception examples",
        "synthetic_register_rows": len(facts),
        "synthetic_register_unique_fact_ids": len(set(fact_ids)),
        "all_examples": "SAMPLE/SYNTHETIC; no association event, approval, signature, or archive is asserted",
        "text_and_data_unchanged_from_previsual_candidate": False,
        "content_completion_repair_applied": content_completion_repair_applied,
        "content_delta": "Completed the twelve-field examples and three additional control facts per record; expanded the unique fact-level replacement register from 144 to 156 rows. All new values remain SAMPLE/SYNTHETIC.",
        "structural_layout_change": "Four email messages remain consolidated under one table header; earlier localized layout repairs are retained.",
    },
    "technical_integrity": "PASS",
    "visual_layout": f"PASS; Word-native render; all {len(page_files)} pages directly inspected",
    "semantic_review": "PENDING; no builder claim will substitute for independent exact-SHA review",
    "formal_acceptance": "NOT_REQUESTED_OR_GRANTED",
    "real_evidence": "NOT_EVIDENCED; synthetic demonstration only",
    "authoring_owner": "current TTQS ONE GOAL thread; no competing active Builder reported",
    "next_action": "Read-only independent semantic and visual review of this exact SHA; repair only cited material defects, then sync review evidence to existing PR #92.",
    "updated_at_taipei": datetime.now(ZoneInfo("Asia/Taipei")).isoformat(),
}
PROGRESS.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

readme = f"""# 0044 R01 candidate package and independent review

## Identity and status

- Project: TTQS ONE
- DOCX deliverable: 0044
- Unique official requirement: I09-E04 — 所有的討論、 會議或E-mail均留有完整紀錄並經簽核後存檔。
- Official checklist sequence: 045. This is distinct from DOCX ID 0044.
- Candidate revision: R01, `CANDIDATE / NOT_PROMOTED`.
- Candidate DOCX SHA-256: `{candidate_sha}`.
- Current status: exact-SHA independent semantic review pending. Technical and visual receipts do not establish semantic acceptance.
- Real association discussions, meetings, emails, signatures, approvals, and archive locations: NOT EVIDENCED.

## Source and requirement mapping

The official checklist page 3, sequence 045, and the current Unique Blueprint bind DOCX 0044 to I09-E04. The package includes the exact official source, source page image, sequence excerpt, current 0043/0044/0045 Blueprint rows, and the 129-to-142 mapping crosswalk. DOCX 0043/I09-E03 is the neighboring needs-interview/analysis report; DOCX 0045/I10-E01 is the procurement and selection procedure. Neither is interchangeable with this evidence record.

## Candidate content

This is an operational evidence-record form and worked example, not a policy claiming association approval. It explains when and how to retain an original discussion, meeting, or complete email thread; separates opinions from decisions and unresolved items; indexes attachments and versions; records review/signoff and archive retrieval requirements; gives a worked synthetic meeting, face-to-face discussion, four-message email thread, and a missing-source HOLD example; and includes completeness rules, rejection conditions, an operator replacement register, and a reusable single-record form.

The 156-row fact-level register binds each synthetic date, role, event, message, attachment, decision state, review trace, archive locator, each of the twelve reusable form fields, and each field-model judgment to a body location, the real source needed, and a verification rule. The modeled completeness is 3/4 = 75% only for the four displayed synthetic records; it is not an association result or compliance rate. Missing originals, authority, signoff, or archive evidence remain HOLD.

## Technical and visual checks

- DOCX ZIP integrity: {"PASS" if zip_ok else "FAIL"}; {len(doc.paragraphs)} top-level paragraphs; {len(doc.tables)} tables; {len(facts)} unique synthetic replacement facts.
- Word-native render: {len(page_files)} pages; every page was opened and directly inspected. PDF SHA-256: `{sha(PDF)}`.
- Final visual receipt: `evidence/visual_layout_receipt_R01_FINAL.json`; page images are included in `{str(RENDER.relative_to(ROOT)).replace(chr(92), '/')}/`.
- Earlier localized layout defects were corrected: the built-in title border, excessive wrapping in the reusable form label column, the date split in the identifier line, and an isolated email table header. The stop condition is now in the section 8 exception table. The 12-field reusable form uses six paired-field rows with wide response cells so the final official crosswalk stays together. The candidate also completes missing Chinese control-field examples and adds the corresponding 12-field evidence facts; these are substantive content repairs, not metadata-only changes.

## Candidate lineage

- Runtime historical DOCX SHA-256: `427e9ccae8ebf0f3128571057b63602c728ea70c1ea911857fba941c3acfd1d1`; retained as discovery-only. It lacks fully worked meeting/oral-discussion examples and a fact-level replacement register and was not used as a writing template.
- Previsual R01 bytes SHA-256: `{sha(PRIOR)}`; preserved in `evidence/history/` and explicitly not independently reviewed or accepted.
- The builder was authored from current official source and Unique Blueprint materials. Candidate `{previous_candidate_sha}` is preserved in history as the pre-layout-repair version. Earlier 95532fa8 and b047fe36 candidates are also retained; 95532fa8 was superseded after its incomplete content fields were detected, and b047fe36/f2113af5 were superseded after their isolated-page layout defects were located.

## Artifact map

- `candidate/`: exact current DOCX candidate.
- `inputs/`: official source, requirement identity, unique and negative-neighbor Blueprints, crosswalk, historical disposition, source map, and candidate body text.
- `evidence/`: technical receipt, final Word PDF and page images, final visual receipt, 156-row synthetic replacement register, deterministic builder, and preserved prior visual candidates.
- `review/`: frozen exact-SHA independent review packet, raw CLI response, and execution receipt after review completes.
- `PROGRESS.json`: machine-readable candidate, source, verification, and next-action state.
- `artifact_manifest.json`: hashes and byte sizes for package files other than the manifest itself.

## Acceptance boundary

Only an independent reviewer result bound to the exact candidate SHA can establish candidate semantic review. A review PASS still does not prove actual association records, real execution, formal approval, or final Human acceptance. Do not promote this package or present synthetic examples as real evidence.
"""
README.write_text(readme, encoding="utf-8")

print(json.dumps({
    "candidate_sha256": candidate_sha,
    "technical_zip_integrity": zip_ok,
    "paragraph_count": len(doc.paragraphs),
    "table_count": len(doc.tables),
    "register_rows": len(facts),
    "unique_fact_ids": len(set(fact_ids)),
    "content_completion_repair_applied": content_completion_repair_applied,
    "pages": len(page_files),
    "pdf_sha256": sha(PDF),
    "page_image_hashes": {path.name: sha(path) for path in page_files},
}, ensure_ascii=False))
