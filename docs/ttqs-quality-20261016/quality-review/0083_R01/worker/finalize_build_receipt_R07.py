from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


BASE = Path(__file__).resolve().parents[1]
CANDIDATE = BASE / "candidate"
PRE = CANDIDATE / "0083_R07_pre_watermark.docx"
TEMPLATE = CANDIDATE / "0083_R03.docx"
FINAL = CANDIDATE / "0083_R07.docx"
RECEIPT = BASE / "evidence" / "build_receipt_R07.json"
EXTRACTED = BASE / "evidence" / "docx_extracted_R07.md"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


with zipfile.ZipFile(TEMPLATE, "r") as template_zip, zipfile.ZipFile(PRE, "r") as pre_zip:
    names = set(pre_zip.namelist())
    if "word/header1.xml" not in names or "word/header1.xml" not in template_zip.namelist():
        raise RuntimeError("Expected the same primary Word header part in R03 and R04")
    replacements = {"word/header1.xml": template_zip.read("word/header1.xml")}
    rel_name = "word/_rels/header1.xml.rels"
    if rel_name in template_zip.namelist():
        if rel_name not in names:
            raise RuntimeError("R04 header relationship part missing; refuse to create dangling watermark references")
        replacements[rel_name] = template_zip.read(rel_name)
    temp = FINAL.with_suffix(".tmp.docx")
    with zipfile.ZipFile(temp, "w", compression=zipfile.ZIP_DEFLATED) as out_zip:
        for info in pre_zip.infolist():
            out_zip.writestr(info, replacements.get(info.filename, pre_zip.read(info.filename)))
temp.replace(FINAL)

with zipfile.ZipFile(FINAL, "r") as package:
    bad = package.testzip()
    if bad:
        raise RuntimeError(f"DOCX package CRC failure in {bad}")
    header = package.read("word/header1.xml").decode("utf-8", "replace")
    if "SAMPLE / SYNTHETIC" not in header or "pict" not in header:
        raise RuntimeError("The copied SAMPLE/SYNTHETIC watermark was not found in header1.xml")

doc = Document(FINAL)
lines: list[str] = []
body = doc._element.body
for child in body.iterchildren():
    if isinstance(child, CT_P):
        value = Paragraph(child, doc).text.strip()
        if value:
            lines.append(value)
    elif isinstance(child, CT_Tbl):
        table = Table(child, doc)
        for row in table.rows:
            lines.append(" | ".join(cell.text.replace("\n", " / ").strip() for cell in row.cells))
        lines.append("")
EXTRACTED.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")

receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
receipt.update({
    "revision": "R07",
    "pre_watermark_docx_path": str(PRE.relative_to(BASE)).replace("/", "\\"),
    "pre_watermark_docx_sha256": sha(PRE),
    "docx_path": str(FINAL.relative_to(BASE)).replace("/", "\\"),
    "docx_sha256": sha(FINAL),
    "docx_bytes": FINAL.stat().st_size,
    "watermark": "SAMPLE / SYNTHETIC copied from the unchanged R03 header part; body is not modified by watermark transfer",
    "extracted_text_path": str(EXTRACTED.relative_to(BASE)).replace("/", "\\"),
    "extracted_text_sha256": sha(EXTRACTED),
    "layout_change_scope": "Targeted R07 corrections: source/hash table first column widened to keep SRC identifiers on one line;  removed the default Title bottom rule; kept the Form-A1 blank form group together; moved Appendix A source hashes and Appendix E heading/description into landscape regions; refreshed candidate/version and dynamic remote-readback status rows. The 81-row sample register and all case values are preserved.",
    "acceptance_status": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
    "real_evidence_status": "UNKNOWN_HOLD",
})
RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({
    "docx_sha256": receipt["docx_sha256"],
    "docx_bytes": receipt["docx_bytes"],
    "zip_crc": "PASS",
    "watermark": "PASS",
    "extracted_text_sha256": receipt["extracted_text_sha256"],
    "receipt_sha256": sha(RECEIPT),
}, ensure_ascii=False, indent=2))
