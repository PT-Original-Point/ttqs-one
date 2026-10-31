from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt


PACKAGE = Path(__file__).resolve().parents[1]
PARENT_PACKAGE = PACKAGE.parent / "0047_R03"
SOURCE = PARENT_PACKAGE / "candidate" / "0047_R03.docx"
DEST = PACKAGE / "candidate" / "0047_R04.docx"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def all_text(doc):
    parts = [p.text for p in doc.paragraphs]
    for table in doc.tables:
        for row in table.rows:
            parts.extend(cell.text for cell in row.cells)
    return parts


def tighten_cell(cell):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        from docx.oxml import OxmlElement
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for side, value in (("top", 40), ("bottom", 40), ("start", 80), ("end", 80)):
        node = tc_mar.find(qn(f"w:{side}"))
        if node is None:
            from docx.oxml import OxmlElement
            node = OxmlElement(f"w:{side}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


if not SOURCE.is_file():
    raise FileNotFoundError(SOURCE)
if DEST.exists():
    raise FileExistsError(f"Refusing to overwrite existing candidate: {DEST}")

parent_sha = sha256(SOURCE)
shutil.copy2(SOURCE, DEST)
doc = Document(DEST)
before = all_text(doc)

target_tables = {}
for table in doc.tables:
    if table.rows:
        header = table.rows[0].cells[0].text.strip()
        if header in {"評量項目", "分數", "判讀條件"}:
            target_tables[header] = table
if set(target_tables) != {"評量項目", "分數", "判讀條件"}:
    raise AssertionError(f"Could not locate the complete final assessment section: {sorted(target_tables)}")

for table in target_tables.values():
    for ri, row in enumerate(table.rows):
        for cell in row.cells:
            tighten_cell(cell)
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_before = Pt(0)
                paragraph.paragraph_format.space_after = Pt(0)
                paragraph.paragraph_format.line_spacing = 1.0
                for run in paragraph.runs:
                    run.font.size = Pt(10 if ri == 0 else 9.5)

for paragraph in doc.paragraphs:
    text = paragraph.text.strip()
    if text in {"評量方式與判定", "判斷依據", "評分量尺", "示範判讀門檻"}:
        paragraph.paragraph_format.keep_with_next = True
        paragraph.paragraph_format.space_before = Pt(3)
        paragraph.paragraph_format.space_after = Pt(2)

doc.core_properties.comments = "R04: presentation-only fit adjustment to keep the final sample-threshold row with its assessment section; no text or table values changed. Table body text remains at 9.5 pt or larger."
doc.save(DEST)

check = Document(DEST)
if before != all_text(check):
    raise AssertionError("Content changed during R04 layout-only repair.")
if sha256(SOURCE) != parent_sha:
    raise AssertionError("R03 parent bytes changed during R04 creation.")
for table in target_tables.values():
    if any(run.font.size is not None and run.font.size.pt < 9.5 for row in table.rows for cell in row.cells for paragraph in cell.paragraphs for run in paragraph.runs):
        raise AssertionError("A final assessment table run fell below the 9.5 pt minimum.")

receipt = {
    "doc_id": "0047",
    "revision": "R04",
    "change_scope": "PRESENTATION_ONLY",
    "parent_candidate": str(SOURCE),
    "parent_sha256": parent_sha,
    "candidate": str(DEST),
    "candidate_sha256": sha256(DEST),
    "layout_fixes": [
        "Tightened only the last three assessment tables to 9.5 pt body text, 10 pt headers, 1.0 line spacing, and compact cell margins.",
        "Kept assessment headings attached to their following content so the final threshold row does not orphan on a separate page.",
    ],
    "body_text_and_table_values_changed": False,
    "minimum_table_body_font_pt": 9.5,
    "post_save_checks": "PASS: reopened R04; all paragraph/table cell text unchanged from R03; R03 parent SHA unchanged; assessment-table font minimum verified.",
    "independent_semantic_review": "PENDING: prior review receipts do not transfer to R04 exact SHA.",
}
(PACKAGE / "evidence" / "R04_LAYOUT_REPAIR_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
