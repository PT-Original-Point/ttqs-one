#!/usr/bin/env python3
"""Deterministically render the reviewed Markdown body as an editable Word record."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


BASE = Path(__file__).resolve().parents[1]
BODY = BASE / "candidate" / "0083_R02_body.md"
OUT = BASE / "candidate" / "0083_R02_pre_watermark.docx"
BLUEPRINT = BASE / "inputs" / "UNIQUE_BLUEPRINT_0083_R03.md"
FONT = "Microsoft JhengHei"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def shade(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def cell_margins(cell, top=85, start=95, bottom=85, end=95) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    margins = tc_pr.first_child_found_in("w:tcMar")
    if margins is None:
        margins = OxmlElement("w:tcMar")
        tc_pr.append(margins)
    for tag, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = margins.find(qn(f"w:{tag}"))
        if node is None:
            node = OxmlElement(f"w:{tag}")
            margins.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def keep_row_together(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    cant_split = OxmlElement("w:cantSplit")
    tr_pr.append(cant_split)


def set_run_font(run, size=10, bold=None, color=None, italic=None, mono=False) -> None:
    run.font.name = "Consolas" if mono else FONT
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Microsoft JhengHei")
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), "Consolas" if mono else FONT)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), "Consolas" if mono else FONT)
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color:
        run.font.color.rgb = RGBColor.from_string(color)


INLINE = re.compile(r"(\*\*.+?\*\*|`[^`]+`|\*[^*]+\*)")


def add_inline(paragraph, text: str, size=10, base_color=None) -> None:
    for token in INLINE.split(text):
        if not token:
            continue
        if token.startswith("**") and token.endswith("**"):
            run = paragraph.add_run(token[2:-2])
            set_run_font(run, size, bold=True, color=base_color)
        elif token.startswith("`") and token.endswith("`"):
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, size, color="36566F", mono=True)
        elif token.startswith("*") and token.endswith("*"):
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, size, italic=True, color=base_color)
        else:
            run = paragraph.add_run(token)
            set_run_font(run, size, color=base_color)


def is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2


def table_cells(line: str) -> list[str]:
    return [item.strip().replace("\\|", "|") for item in line.strip().strip("|").split("|")]


def is_separator(line: str) -> bool:
    cells = table_cells(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def add_markdown_table(doc: Document, lines: list[str]) -> None:
    rows = [table_cells(line) for line in lines if not is_separator(line)]
    if not rows:
        return
    cols = max(map(len, rows))
    table = doc.add_table(rows=len(rows), cols=cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    table.style = "Table Grid"
    for ri, values in enumerate(rows):
        row = table.rows[ri]
        keep_row_together(row)
        for ci in range(cols):
            cell = row.cells[ci]
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            cell_margins(cell)
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            value = values[ci] if ci < len(values) else ""
            add_inline(p, value, 10)
            if ri == 0:
                shade(cell, "244B68")
                for run in p.runs:
                    run.font.color.rgb = RGBColor(255, 255, 255)
                    run.bold = True
            elif ri % 2 == 0:
                shade(cell, "F2F6F8")
        if ri == 0:
            set_repeat_table_header(row)
    doc.add_paragraph().paragraph_format.space_after = Pt(1)


def add_page_field(paragraph) -> None:
    run = paragraph.add_run()
    set_run_font(run, 8, color="637585")
    begin = OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = " PAGE "
    separate = OxmlElement("w:fldChar"); separate.set(qn("w:fldCharType"), "separate")
    value = OxmlElement("w:t"); value.text = "1"
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instr, separate, value, end])


def set_orientation(section, landscape: bool) -> None:
    section.orientation = WD_ORIENT.LANDSCAPE if landscape else WD_ORIENT.PORTRAIT
    section.page_width = Inches(11 if landscape else 8.5)
    section.page_height = Inches(8.5 if landscape else 11)
    section.top_margin = Inches(0.55 if landscape else 0.68)
    section.bottom_margin = Inches(0.55 if landscape else 0.68)
    section.left_margin = Inches(0.55 if landscape else 0.72)
    section.right_margin = Inches(0.55 if landscape else 0.72)
    section.header_distance = Inches(0.28)
    section.footer_distance = Inches(0.28)
    hp = section.header.paragraphs[0]
    hp.clear()
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    add_inline(hp, "TTQS ONE　｜　DOCX 0083　｜　SAMPLE / SYNTHETIC", 8, "637585")
    fp = section.footer.paragraphs[0]
    fp.clear()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_inline(fp, "學員行動計畫追蹤紀錄　•　頁 ", 8, "637585")
    add_page_field(fp)


def add_sample_frame(paragraph) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:fill"), "F7ECEC"); p_pr.append(shd)
    borders = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        edge = OxmlElement(f"w:{side}")
        edge.set(qn("w:val"), "single")
        edge.set(qn("w:sz"), "6")
        edge.set(qn("w:space"), "4")
        edge.set(qn("w:color"), "B85C5C")
        borders.append(edge)
    p_pr.append(borders)


def format_document(doc: Document) -> None:
    sec = doc.sections[0]
    sec.top_margin = Inches(0.68)
    sec.bottom_margin = Inches(0.68)
    sec.left_margin = Inches(0.72)
    sec.right_margin = Inches(0.72)
    sec.header_distance = Inches(0.32)
    sec.footer_distance = Inches(0.32)
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = FONT
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    normal._element.rPr.rFonts.set(qn("w:ascii"), FONT)
    normal.font.size = Pt(12)
    normal.paragraph_format.space_after = Pt(5)
    normal.paragraph_format.line_spacing = 1.15
    for name, size, color in (("Title", 23, "1B3A4B"), ("Heading 1", 15, "1B3A4B"), ("Heading 2", 12, "28627B"), ("Heading 3", 10.5, "28627B")):
        style = styles[name]
        style.font.name = FONT
        style._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
        style._element.rPr.rFonts.set(qn("w:ascii"), FONT)
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor.from_string(color)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.space_before = Pt(12 if name == "Heading 1" else 8)
        style.paragraph_format.space_after = Pt(5)
    header = sec.header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    add_inline(header, "TTQS ONE　｜　DOCX 0083　｜　範例資料均為 SAMPLE / SYNTHETIC", 8, "637585")
    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_inline(footer, "學員行動計畫追蹤紀錄　•　頁 ", 8, "637585")
    add_page_field(footer)
    update_fields = OxmlElement("w:updateFields")
    update_fields.set(qn("w:val"), "true")
    doc.settings.element.append(update_fields)


def main() -> None:
    if len(sys.argv) > 1:
        global BODY, OUT
        BODY = Path(sys.argv[1]).resolve()
    if len(sys.argv) > 2:
        OUT = Path(sys.argv[2]).resolve()
    if not BODY.exists():
        raise SystemExit(f"Body not found: {BODY}")
    text = BODY.read_text(encoding="utf-8-sig")
    doc = Document()
    format_document(doc)
    lines = text.splitlines()
    # Render wide (over five-column) tables in landscape; keep source Markdown unchanged.
    insertions = []
    table_start = None
    for n in range(len(lines) + 1):
        line = lines[n].rstrip() if n < len(lines) else ""
        if is_table_line(line):
            if table_start is None:
                table_start = n
        elif table_start is not None:
            block = lines[table_start:n]
            widest = max((len(table_cells(x)) for x in block if is_table_line(x.rstrip()) and not is_separator(x.rstrip())), default=0)
            if widest > 5:
                insertions.extend([(table_start, "<!-- LANDSCAPE_START -->"), (n, "<!-- LANDSCAPE_END -->")])
            table_start = None
    for at, value in sorted(insertions, reverse=True):
        lines.insert(at, value)
    i = 0
    first_title = True
    landscape = False
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.strip() == "<!-- LANDSCAPE_START -->":
            section = doc.add_section(WD_SECTION.NEW_PAGE)
            set_orientation(section, True)
            landscape = True
            i += 1
            continue
        if line.strip() == "<!-- LANDSCAPE_END -->":
            section = doc.add_section(WD_SECTION.NEW_PAGE)
            set_orientation(section, False)
            landscape = False
            i += 1
            continue
        if is_table_line(line):
            block = []
            while i < len(lines) and is_table_line(lines[i].rstrip()):
                block.append(lines[i].rstrip()); i += 1
            add_markdown_table(doc, block)
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            level, title = len(heading.group(1)), heading.group(2).strip()
            para = doc.add_paragraph(style="Title" if level == 1 and first_title else f"Heading {min(level, 3)}")
            add_inline(para, title, 23 if level == 1 and first_title else (15 if level == 1 else (12 if level == 2 else 10.5)), "1B3A4B")
            if "SAMPLE/SYNTHETIC" in title or "完整合成案例" in title:
                add_sample_frame(para)
            if level == 1:
                first_title = False
            i += 1
            continue
        if line.strip() in ("---", "***", "___"):
            i += 1
            continue
        if line.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.18)
            p.paragraph_format.right_indent = Inches(0.08)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(7)
            p_pr = p._p.get_or_add_pPr()
            shd = OxmlElement("w:shd"); shd.set(qn("w:fill"), "EEF4F6"); p_pr.append(shd)
            add_inline(p, line[2:], 9.5, "36566F")
            i += 1
            continue
        bullet = re.match(r"^\s*[-*+]\s+(.+)$", line)
        numbered = re.match(r"^\s*(\d+)[.)]\s+(.+)$", line)
        if bullet or numbered:
            style = "List Bullet" if bullet else "List Number"
            p = doc.add_paragraph(style=style)
            add_inline(p, (bullet or numbered).group(1 if bullet else 2), 10.2)
            i += 1
            continue
        if not getattr(doc, "_toc_inserted", False) and len(doc.paragraphs) >= 2:
            # Insert a native Word TOC after the title and subtitle, before the body.
            doc.add_page_break()
            toc_title = doc.add_paragraph(style="Heading 1")
            add_inline(toc_title, "目錄", 15, "1B3A4B")
            toc = doc.add_paragraph()
            fld = OxmlElement("w:fldSimple")
            fld.set(qn("w:instr"), 'TOC \\o "1-3" \\h \\z \\u')
            r = OxmlElement("w:r")
            t = OxmlElement("w:t")
            t.text = "開啟 Word 後更新目錄欄位"
            r.append(t)
            fld.append(r)
            toc._p.append(fld)
            doc.add_page_break()
            doc._toc_inserted = True
        p = doc.add_paragraph()
        add_inline(p, line, 12)
        i += 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.core_properties.title = "學員行動計畫追蹤紀錄"
    doc.core_properties.subject = "DOCX 0083 / I17C-E02 / official checkbox 089"
    doc.core_properties.author = "原始點協會 TTQS ONE candidate; SAMPLE data only"
    doc.save(OUT)
    receipt = {
        "schema": "ttqs-0083-docx-build-v1",
        "document_id": "0083",
        "requirement_id": "I17C-E02",
        "official_checkbox": "089",
        "revision": "R02",
        "blueprint_sha256": sha(BLUEPRINT),
        "body_path": str(BODY),
        "body_sha256": sha(BODY),
        "docx_path": str(OUT),
        "docx_sha256": sha(OUT),
        "docx_bytes": OUT.stat().st_size,
        "acceptance_status": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
        "real_evidence_status": "UNKNOWN_HOLD",
    }
    (BASE / "evidence" / "build_receipt_R01.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=True))


if __name__ == "__main__":
    main()
