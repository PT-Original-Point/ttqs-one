from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


PACKAGE = Path(__file__).resolve().parents[1]
R02_PACKAGE = PACKAGE.parent / "0047_R02"
SOURCE = R02_PACKAGE / "candidate" / "0047_R02.docx"
DEST = PACKAGE / "candidate" / "0047_R03.docx"


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


def repeat_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    node = tr_pr.find(qn("w:tblHeader"))
    if node is None:
        node = OxmlElement("w:tblHeader")
        tr_pr.append(node)
    node.set(qn("w:val"), "1")


def prevent_row_split(row):
    tr_pr = row._tr.get_or_add_trPr()
    if tr_pr.find(qn("w:cantSplit")) is None:
        tr_pr.append(OxmlElement("w:cantSplit"))


if not SOURCE.is_file():
    raise FileNotFoundError(SOURCE)
if DEST.exists():
    raise FileExistsError(f"Refusing to overwrite an existing candidate: {DEST}")

parent_sha = sha256(SOURCE)
shutil.copy2(SOURCE, DEST)
doc = Document(DEST)
before = all_text(doc)

for paragraph in doc.paragraphs:
    text = paragraph.text.strip()
    if text in ("資料欄位、定義、分母、來源及限制字典", "年度案例明細與逐步計算"):
        paragraph.paragraph_format.page_break_before = False
        paragraph.paragraph_format.keep_with_next = True

for table in doc.tables:
    if table.rows:
        repeat_header(table.rows[0])
    for row in table.rows:
        prevent_row_split(row)

doc.core_properties.comments = "R03: layout-only correction of R02 page-flow defects. Removed forced page breaks that created a sparse page and enabled repeating headers across all document tables; no body text or table values changed."
doc.save(DEST)

check = Document(DEST)
after = all_text(check)
if before != after:
    raise AssertionError("Text/table content changed in this presentation-only repair.")
for table in check.tables:
    if table.rows and table.rows[0]._tr.trPr.find(qn("w:tblHeader")) is None:
        raise AssertionError("A document table is missing a repeating header.")
if sha256(SOURCE) != parent_sha:
    raise AssertionError("R02 parent bytes changed during R03 creation.")

receipt = {
    "doc_id": "0047",
    "revision": "R03",
    "change_scope": "PRESENTATION_ONLY",
    "parent_candidate": str(SOURCE),
    "parent_sha256": parent_sha,
    "candidate": str(DEST),
    "candidate_sha256": sha256(DEST),
    "layout_fixes": [
        "Removed forced page starts before the data dictionary and annual-case sections, eliminating the sparse fourth page while keeping section headings with following content.",
        "Marked the header row of every document table to repeat across page breaks, including the six-column cross-year comparison table.",
        "Prevented individual table rows from splitting across pages.",
    ],
    "body_text_and_table_values_changed": False,
    "post_save_checks": "PASS: python-docx reopened R03; all paragraph and table cell text exactly matches R02; every table has a repeating header; R02 SHA unchanged.",
    "independent_semantic_review": "PENDING: neither R01 nor R02 review transfers to the R03 exact SHA.",
}
(PACKAGE / "evidence" / "R03_LAYOUT_REPAIR_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
