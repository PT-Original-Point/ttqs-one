from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from hashlib import sha256

here = Path(__file__).resolve().parent
src = here / "inputs" / "candidate" / "0058_R08.docx"
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
with ZipFile(src) as z:
    doc = etree.fromstring(z.read("word/document.xml"))
body = doc.find("w:body", ns)
out = [f"# 0058 R08 extracted document text\n\nDOCX SHA-256: `{sha256(src.read_bytes()).hexdigest().upper()}`\n"]
paragraph_no = 0
table_no = 0
for child in body:
    if child.tag.endswith("}p"):
        text = "".join(child.xpath(".//w:t/text()", namespaces=ns)).strip()
        if text:
            paragraph_no += 1
            out.append(f"\nP{paragraph_no:04d}: {text}\n")
    elif child.tag.endswith("}tbl"):
        table_no += 1
        out.append(f"\n## TABLE {table_no}\n")
        for row_no, row in enumerate(child.findall("w:tr", ns), 1):
            cells = []
            for cell in row.findall("w:tc", ns):
                parts = ["".join(p.xpath(".//w:t/text()", namespaces=ns)).strip() for p in cell.findall("w:p", ns)]
                cells.append(" / ".join(p for p in parts if p))
            out.append(f"R{row_no:02d}: " + " | ".join(cells) + "\n")
dest = here / "inputs" / "candidate" / "0058_R08_document_text.md"
dest.write_text("".join(out), encoding="utf-8")
print(f"paragraphs={paragraph_no}; tables={table_no}; bytes={dest.stat().st_size}; docx_sha={sha256(src.read_bytes()).hexdigest().upper()}; output={dest}")
