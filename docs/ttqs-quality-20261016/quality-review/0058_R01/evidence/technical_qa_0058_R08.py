from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from hashlib import sha256
from pypdf import PdfReader
import json
import re

root = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0058_R01")
r06 = root / "candidate" / "0058_R06.docx"
r08 = root / "candidate" / "0058_R08.docx"
pdf = root / "evidence" / "render_R08" / "0058_R08.pdf"
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

def digest(path):
    return sha256(path.read_bytes()).hexdigest().upper()

with ZipFile(r06) as z6, ZipFile(r08) as z8:
    names6, names8 = set(z6.namelist()), set(z8.namelist())
    assert names6 == names8, "OOXML entry list changed"
    assert z8.testzip() is None, "R08 package CRC failure"
    changed = sorted(n for n in names6 if z6.read(n) != z8.read(n))
    assert changed == ["word/document.xml"], changed
    x6 = etree.fromstring(z6.read("word/document.xml"))
    x8 = etree.fromstring(z8.read("word/document.xml"))
    assert x6.xpath("//w:t/text()", namespaces=ns) == x8.xpath("//w:t/text()", namespaces=ns), "Text changed"
    body = x8.find("w:body", ns)
    children = list(body)
    caption = "表 10-3：文件修訂與版本管制紀錄表"
    matches = [e for e in children if e.tag.endswith("}p") and "".join(e.xpath(".//w:t/text()", namespaces=ns)) == caption]
    assert len(matches) == 1, f"caption count {len(matches)}"
    paragraph = matches[0]
    breaks = paragraph.xpath(".//w:pPr/w:pageBreakBefore", namespaces=ns)
    assert len(breaks) == 1, f"pageBreakBefore count {len(breaks)}"
    paragraph.find("w:pPr", ns).remove(breaks[0])
    table = children[children.index(paragraph) + 1]
    assert table.tag.endswith("}tbl"), "caption is not followed by table"
    rows = table.findall("w:tr", ns)
    assert len(rows) == 8, f"row count {len(rows)}"
    spacing_count = 0
    for row in rows[1:]:
        for cell in row.findall("w:tc", ns):
            for spacing in cell.xpath('.//w:pPr/w:spacing[@w:line="240"]', namespaces=ns):
                spacing.set("{%s}line" % ns["w"], "276")
                spacing_count += 1
    assert spacing_count == 35, f"spacing edits {spacing_count}"
    assert etree.tostring(x6, method="c14n") == etree.tostring(x8, method="c14n"), "Reversing layout delta does not reproduce R06"

sidecars = [
    root / "worker/antigravity/0058_CONTENT_R06.json",
    root / "worker/antigravity/0058_CONTENT_R08.json",
    root / "worker/antigravity/0058_SYNTHETIC_REPLACEMENT_REGISTER_R06.csv",
    root / "worker/antigravity/0058_SYNTHETIC_REPLACEMENT_REGISTER_R08.csv",
]
sidecar_hashes = {p.name: digest(p) for p in sidecars}
assert sidecar_hashes[sidecars[0].name] == sidecar_hashes[sidecars[1].name]
assert sidecar_hashes[sidecars[2].name] == sidecar_hashes[sidecars[3].name]

reader = PdfReader(str(pdf))
assert len(reader.pages) == 32, f"PDF pages {len(reader.pages)}"
page_text = [re.sub(r"\s+", " ", p.extract_text() or "") for p in reader.pages]
assert "10-3" not in page_text[29], "Table 10-3 caption remains on page 30"
assert "10-3" in page_text[30] and "R00" in page_text[30] and "R03" in page_text[30]
assert all(f"R0{i}" in page_text[31] for i in (4, 5, 6))

report = {
    "doc_id": "0058", "requirement_id": "I13-E02", "official_checkbox_serial": "062",
    "candidate_revision": "R08", "source_revision": "R06",
    "source_docx_sha256": digest(r06), "candidate_docx_sha256": digest(r08), "candidate_bytes": r08.stat().st_size,
    "changed_ooxml_parts": changed, "package_entries_identical": True, "zip_integrity": "PASS",
    "text_nodes_unchanged": True, "reversed_layout_delta_canonical_equal_to_R06": True,
    "page_break_before_table_10_3": True, "table_10_3_rows_including_header": len(rows),
    "data_cell_paragraph_spacing_adjustments": spacing_count, "font_size_changed": False, "content_or_data_changed": False,
    "sidecars_byte_identical_to_R06": True, "sidecar_sha256": sidecar_hashes,
    "renderer": "Microsoft Word COM; newly owned process; read-only",
    "render_pdf_sha256": digest(pdf), "render_pages": len(reader.pages),
    "table_10_3_page_flow": "Caption/header and R00-R03 on page 31; repeated header and R04-R06 on page 32; no row stranded on page 33.",
    "technical_qa": "PASS", "visual_review": "PASS; all 8 contact sheets and full-resolution pages 29-32 inspected",
    "semantic_review": "PENDING exact R08 SHA", "formal_acceptance": "NOT_CLAIMED",
}
qa_path = root / "evidence" / "technical_qa_0058_R08.json"
qa_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
visual = f"""# 0058 R08 visual review

- Binding: `doc_id=0058`, `requirement_id=I13-E02`, official checkbox `062`; candidate SHA-256 `{digest(r08)}`.
- Renderer: Microsoft Word COM opened the candidate read-only and exported a 32-page PDF (SHA-256 `{digest(pdf)}`). The receipt identifies a newly owned Word process and confirms it did not attach to a pre-existing instance.
- Scope: all eight 4-page contact sheets (pages 1–32) inspected; full-resolution pages 29–32 inspected.
- R06 defect: Table 10-3 caption/header stranded at the foot of page 30. R07 moved the table start but stranded row R06 on page 33. R08 starts the table on page 31: page 31 contains the caption/header and R00–R03; page 32 repeats the table header and contains R04–R06.
- Page 29 ends with Table 10-1; page 30 contains the complete Table 10-2 and no Table 10-3 caption.
- The full-size pages show readable table text, visible cell boundaries, no clipping or overlap, and clear footer clearance. The repeated page-32 header preserves row context.
- R08 is a layout-only candidate. It adds no semantic or association decision. Visual inspection does not establish formal acceptance.

**Visual result: PASS for rendered layout.** Exact-SHA independent semantic delta review remains pending.
"""
visual_path = root / "evidence" / "visual_review_0058_R08.md"
visual_path.write_text(visual, encoding="utf-8")
print(json.dumps({"technical_qa": "PASS", "candidate_sha256": report["candidate_docx_sha256"], "pdf_sha256": report["render_pdf_sha256"], "pages": len(reader.pages), "changed_parts": changed, "spacing_adjustments": spacing_count, "sidecars_identical": True, "qa_receipt": str(qa_path), "visual_note": str(visual_path)}, ensure_ascii=False))
