from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


BASE = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029")
SRC = BASE / "worker" / "R08E_REPORT_TABLE_START_20261031" / "R08E_INTEGRATED_SOURCE.md"
REGISTER = BASE / "worker" / "R08E_REPORT_TABLE_START_20261031" / "SYNTHETIC_REPLACEMENT_REGISTER_R08E.csv"
OFFICIAL_PDF = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf")
BLUEPRINT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl")
OUT = BASE / "candidate" / "0012_I02-E03_R08E.docx"
RECEIPT = BASE / "qa" / "R08E_REPORT_TABLE_START_20261031" / "BUILD_RECEIPT_R08E.json"

EXPECTED_SOURCE_SHA = "fb4c7a5ad1385b3fbf1a13e1323d77a2b4b365e7c19744c20fcf6e3f62a55a37"
EXPECTED_WORKER_SOURCE_SHA = "18127c1cb94425aa42ac7003640f6fb2ab95a3d872b0c84becfeedd030c6a3fe"
INTEGRATION_RECEIPT = BASE / "worker" / "R08E_REPORT_TABLE_START_20261031" / "R08B_SOURCE_INTEGRATION_RECEIPT.json"
EXPECTED_INTEGRATION_RECEIPT_SHA = "52ede5c8d3529218d64eec459cfa97b39c77cd86095f58b9a98a17b2c7f03b34"
EXPECTED_REGISTER_SHA = "ea6dd8d8df9694ec42289cee4f62497db30e1b8e99adf84096c213609c67315a"
EXPECTED_PDF_SHA = "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709"
EXPECTED_BLUEPRINT_FILE_SHA = "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e"
EXPECTED_BLUEPRINT_ROW_SHA = "0ebf302b8b3601be6c645573e9e12887242c8e64a2244d5cf738a35ee2f5fc04"

FONT = "Microsoft JhengHei"
NAVY = "17365D"
PALE = "EAF1F7"
ALT = "F5F8FB"
GRID = "B7C9D6"
GRAY = "5B6573"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def set_run_font(run, size: float, *, bold=None, italic=None, color=None, font=FONT):
    run.font.name = font
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.rFonts
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        rfonts.set(qn(f"w:{attr}"), font)


def add_inline(p, text: str, size: float):
    token_re = re.compile(r"(\*\*.+?\*\*|`.+?`|\*[^*]+\*)")
    pos = 0
    for match in token_re.finditer(text):
        if match.start() > pos:
            set_run_font(p.add_run(text[pos:match.start()]), size)
        token = match.group(0)
        if token.startswith("**"):
            set_run_font(p.add_run(token[2:-2]), size, bold=True)
        elif token.startswith("`"):
            set_run_font(p.add_run(token[1:-1]), size, font="Consolas", color=GRAY)
        else:
            set_run_font(p.add_run(token[1:-1]), size, italic=True)
        pos = match.end()
    if pos < len(text):
        set_run_font(p.add_run(text[pos:]), size)


def split_row(line: str):
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    cells, cur, escaped = [], [], False
    for ch in value:
        if ch == "|" and not escaped:
            cells.append("".join(cur).strip())
            cur = []
        elif ch == "|" and escaped and cur:
            cur[-1] = "|"
        else:
            cur.append(ch)
        escaped = ch == "\\" and not escaped
        if ch != "\\":
            escaped = False
    cells.append("".join(cur).strip())
    return cells


def table_start(lines, index):
    if index + 1 >= len(lines) or not lines[index].strip().startswith("|"):
        return False
    sep = lines[index + 1].strip()
    if not sep.startswith("|"):
        return False
    cells = split_row(sep)
    return len(cells) >= 2 and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)


def table_block(lines, index):
    heads = split_row(lines[index])
    rows = []
    j = index + 2
    while j < len(lines) and lines[j].strip().startswith("|"):
        vals = split_row(lines[j])
        if len(vals) < len(heads):
            vals += [""] * (len(heads) - len(vals))
        if len(vals) > len(heads):
            vals = vals[: len(heads) - 1] + [" | ".join(vals[len(heads) - 1 :])]
        rows.append(vals)
        j += 1
    return heads, rows, j


def set_cell_fill(cell, fill):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = tcpr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcpr.append(shd)
    shd.set(qn("w:fill"), fill)
    shd.set(qn("w:val"), "clear")


def set_cell_margins(cell, top=95, start=100, bottom=95, end=100):
    tcpr = cell._tc.get_or_add_tcPr()
    margins = tcpr.first_child_found_in("w:tcMar")
    if margins is None:
        margins = OxmlElement("w:tcMar")
        tcpr.append(margins)
    for side, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = margins.find(qn(f"w:{side}"))
        if node is None:
            node = OxmlElement(f"w:{side}")
            margins.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_table_borders(table):
    tblpr = table._tbl.tblPr
    borders = tblpr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tblpr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        node = borders.find(qn(f"w:{edge}"))
        if node is None:
            node = OxmlElement(f"w:{edge}")
            borders.append(node)
        node.set(qn("w:val"), "single")
        node.set(qn("w:sz"), "5")
        node.set(qn("w:space"), "0")
        node.set(qn("w:color"), GRID)


def repeat_header(row):
    trpr = row._tr.get_or_add_trPr()
    mark = OxmlElement("w:tblHeader")
    mark.set(qn("w:val"), "true")
    trpr.append(mark)


def no_row_split(row):
    trpr = row._tr.get_or_add_trPr()
    mark = OxmlElement("w:cantSplit")
    trpr.append(mark)


def set_keep_with_next(p, enabled=True):
    p.paragraph_format.keep_with_next = enabled


def configure_section(section, landscape=False):
    if landscape:
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width, section.page_height = Inches(11.69), Inches(8.27)
        section.top_margin, section.bottom_margin = Inches(0.48), Inches(0.48)
        section.left_margin, section.right_margin = Inches(0.50), Inches(0.50)
    else:
        section.orientation = WD_ORIENT.PORTRAIT
        section.page_width, section.page_height = Inches(8.27), Inches(11.69)
        section.top_margin, section.bottom_margin = Inches(0.62), Inches(0.62)
        section.left_margin, section.right_margin = Inches(0.67), Inches(0.67)
    section.header_distance = Inches(0.28)
    section.footer_distance = Inches(0.28)


def add_page_number(p):
    run = p.add_run()
    set_run_font(run, 8.5, color=GRAY)
    for kind, text in (("begin", None), ("instrText", " PAGE "), ("separate", None), ("text", "1"), ("end", None)):
        if kind == "instrText":
            node = OxmlElement("w:instrText")
            node.set(qn("xml:space"), "preserve")
            node.text = text
        elif kind == "text":
            node = OxmlElement("w:t")
            node.text = text
        else:
            node = OxmlElement("w:fldChar")
            node.set(qn("w:fldCharType"), kind)
        run._r.append(node)


def setup_page_matter(doc):
    sections = list(doc.sections)
    for index, section in enumerate(sections):
        if index:
            section.header.is_linked_to_previous = True
            section.footer.is_linked_to_previous = True
    hp = sections[0].header.paragraphs[0]
    hp.clear()
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.paragraph_format.space_after = Pt(2)
    set_run_font(hp.add_run("TTQS ONE　｜　0012／I02-E03　｜　候選草案　SAMPLE／SYNTHETIC"), 8.5, color=GRAY)
    fp = sections[0].footer.paragraphs[0]
    fp.clear()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.paragraph_format.space_before = Pt(2)
    set_run_font(fp.add_run("未經核定：不得據此承諾優惠、核准、收費或付款　｜　頁 "), 8.5, color=GRAY)
    add_page_number(fp)


def make_table(doc, headers, rows, landscape=False):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    widths_in = None
    if len(headers) == 5 and landscape:
        widths_in = [0.55, 2.65, 1.20, 3.55, 2.74]
    elif len(headers) == 4:
        widths_in = [0.98, 1.78, 2.32, 1.85] if not landscape else [1.65, 3.15, 3.15, 2.0]
    elif len(headers) == 3:
        widths_in = [1.35, 2.80, 2.78] if not landscape else [2.0, 4.5, 3.45]
    elif len(headers) == 2:
        widths_in = [1.80, 5.13] if not landscape else [2.4, 8.2]
    else:
        usable = 10.69 if landscape else 6.93
        widths_in = [usable / len(headers)] * len(headers)
    for row_idx, values in enumerate([headers] + rows):
        cells = table.rows[0].cells if row_idx == 0 else table.add_row().cells
        if row_idx == 0:
            repeat_header(table.rows[0])
        no_row_split(table.rows[row_idx])
        for col_idx, value in enumerate(values):
            cell = cells[col_idx]
            cell.width = Inches(widths_in[col_idx])
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            if row_idx == 0:
                set_cell_fill(cell, NAVY)
            elif row_idx % 2 == 0:
                set_cell_fill(cell, ALT)
            else:
                set_cell_fill(cell, "FFFFFF")
            p = cell.paragraphs[0]
            if row_idx == 0:
                p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(1.5)
            p.paragraph_format.line_spacing = 1.05
            if col_idx == 0 and (len(headers) == 5 or len(headers) == 4):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_inline(p, value.replace("<br>", "\n"), 9.5)
            for run in p.runs:
                run.font.color.rgb = RGBColor.from_string("FFFFFF" if row_idx == 0 else "202830")
                if row_idx == 0:
                    run.bold = True
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    return table


def set_styles(doc):
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor(32, 40, 48)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.14
    for style_name, size, before, after in (("Title", 22, 0, 12), ("Heading 1", 16, 14, 6), ("Heading 2", 12.5, 10, 4), ("Heading 3", 11.5, 8, 3)):
        st = doc.styles[style_name]
        st.font.name = FONT
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = RGBColor(0, 0, 0)
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True
        ppr = st._element.pPr
        if ppr is not None:
            borders = ppr.find(qn("w:pBdr"))
            if borders is not None:
                ppr.remove(borders)
    for name in ("List Bullet", "List Number"):
        st = doc.styles[name]
        st.font.name = FONT
        st.font.size = Pt(10.5)


def write_docx():
    if file_sha(SRC) != EXPECTED_SOURCE_SHA:
        raise SystemExit("source SHA mismatch")
    if file_sha(OFFICIAL_PDF) != EXPECTED_PDF_SHA:
        raise SystemExit("official requirement PDF SHA mismatch")
    if file_sha(BLUEPRINT) != EXPECTED_BLUEPRINT_FILE_SHA:
        raise SystemExit("current Blueprint file SHA mismatch")
    rows = BLUEPRINT.read_text(encoding="utf-8-sig").splitlines()
    if len(rows) < 12 or sha_bytes(rows[11].encode("utf-8")) != EXPECTED_BLUEPRINT_ROW_SHA:
        raise SystemExit("Blueprint row 0012 SHA mismatch")
    blueprint_record = json.loads(rows[11])
    if blueprint_record.get("deliverable_id") != "0012" or blueprint_record.get("requirement_id") != "I02-E03":
        raise SystemExit("Blueprint row identity mismatch")
    if file_sha(INTEGRATION_RECEIPT) != EXPECTED_INTEGRATION_RECEIPT_SHA:
        raise SystemExit("source integration receipt SHA mismatch")
    if file_sha(REGISTER) != EXPECTED_REGISTER_SHA:
        raise SystemExit("synthetic replacement register SHA mismatch")
    with REGISTER.open("r", encoding="utf-8-sig", newline="") as f:
        register_rows = list(csv.DictReader(f))
    expected_columns = ["ID", "合成事實／參數及值", "文內定位", "REAL替換所需原件／查核路徑", "責任角色與替換控制"]
    if not register_rows or list(register_rows[0].keys()) != expected_columns:
        raise SystemExit("synthetic replacement register schema mismatch")
    register_ids = [row["ID"] for row in register_rows]
    if len(register_ids) != 65 or len(set(register_ids)) != len(register_ids):
        raise SystemExit("synthetic replacement register count or uniqueness mismatch")
    if any(not value.strip() for row in register_rows for value in row.values()):
        raise SystemExit("synthetic replacement register contains blank fields")
    markdown = SRC.read_text(encoding="utf-8-sig")
    lines = markdown.splitlines()
    section12_index = next((i for i, line in enumerate(lines) if line.strip().startswith("## 12.")), None)
    if section12_index is None:
        raise SystemExit("section 12 synthetic register not found")
    table_index = next((i for i in range(section12_index + 1, len(lines)) if lines[i].strip().startswith("|")), None)
    if table_index is None or not table_start(lines, table_index):
        raise SystemExit("section 12 markdown register table not found")
    table_headers, markdown_register_rows, _ = table_block(lines, table_index)
    if not table_headers or table_headers[0] != "ID":
        raise SystemExit("section 12 markdown register header mismatch")
    markdown_register_ids = [row[0] for row in markdown_register_rows]
    if markdown_register_ids != register_ids:
        raise SystemExit("markdown and CSV register IDs/order mismatch")
    doc = Document()
    set_styles(doc)
    for section in doc.sections:
        configure_section(section, landscape=False)
    doc.core_properties.title = "0012 I02-E03 補助參與機構公開招生課程或進階課程優惠辦法"
    doc.core_properties.subject = "SAMPLE／SYNTHETIC 制度草案；未核定、非正式辦法"
    doc.core_properties.keywords = "TTQS ONE, 0012, I02-E03, SAMPLE, SYNTHETIC"
    landscape = False
    heading_count = 0
    table_count = 0
    blockquote_lines = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        text = raw.strip()
        if not text:
            i += 1
            continue
        if text.startswith("## 12.") and not landscape:
            sec = doc.add_section(WD_SECTION.NEW_PAGE)
            configure_section(sec, landscape=True)
            landscape = True
        if text.startswith("## 13.") and landscape:
            sec = doc.add_section(WD_SECTION.NEW_PAGE)
            configure_section(sec, landscape=False)
            landscape = False
        if text.startswith(">"):
            blockquote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                blockquote_lines.append(re.sub(r"^\s*>\s?", "", lines[i].strip()))
                i += 1
            quote_text = " ".join(x.strip() for x in blockquote_lines if x.strip())
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.2)
            p.paragraph_format.right_indent = Inches(0.12)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(7)
            p.paragraph_format.line_spacing = 1.1
            add_inline(p, quote_text, 10.5)
            for run in p.runs:
                run.italic = True
            continue
        if text.startswith("|") and table_start(lines, i):
            heads, data_rows, next_i = table_block(lines, i)
            make_table(doc, heads, data_rows, landscape)
            table_count += 1
            i = next_i
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", text)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if level == 1:
                p = doc.add_paragraph(style="Title")
                ppr = p._p.get_or_add_pPr()
                borders = ppr.find(qn("w:pBdr"))
                if borders is not None:
                    ppr.remove(borders)
                add_inline(p, title, 22)
            else:
                p = doc.add_paragraph(style=f"Heading {level - 1}")
                add_inline(p, title, 16 if level == 2 else 12.5)
                if title.startswith("11. 來源追溯及負向鄰項檢核"):
                    p.paragraph_format.page_break_before = True
                elif title.startswith("R08 SAMPLE 月報完整算例"):
                    p.paragraph_format.page_break_before = True
            heading_count += 1
            i += 1
            continue
        if text.startswith("---"):
            i += 1
            continue
        bullet = re.match(r"^\s*[-*+]\s+(.*)$", raw)
        numbered = re.match(r"^\s*(\d+)\.\s+(.*)$", raw)
        if bullet or numbered:
            content = bullet.group(1) if bullet else numbered.group(2)
            p = doc.add_paragraph(style="List Bullet" if bullet else None)
            p.paragraph_format.left_indent = Inches(0.22 if bullet else 0.04)
            p.paragraph_format.first_line_indent = Inches(-0.13 if bullet else 0)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.1
            if numbered:
                set_run_font(p.add_run(numbered.group(1) + ". "), 10.5, bold=True, color=NAVY)
            add_inline(p, content, 10.5)
            i += 1
            continue
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.14
        p.paragraph_format.widow_control = True
        add_inline(p, text, 11)
        i += 1
    setup_page_matter(doc)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        raise SystemExit("refusing to overwrite existing candidate")
    doc.save(OUT)
    reopened = Document(OUT)
    table_rows = sum(len(t.rows) for t in reopened.tables)
    receipt = {
        "receipt_id": "0012_I02-E03_R08E_BUILD_RECEIPT",
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "document_id": "0012",
        "requirement_id": "I02-E03",
        "artifact_state": "CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED",
        "artifact_path": str(OUT),
        "artifact_sha256": file_sha(OUT),
        "artifact_bytes": OUT.stat().st_size,
        "source_path": str(SRC),
        "source_sha256": file_sha(SRC),
        "official_requirement_pdf_sha256": file_sha(OFFICIAL_PDF),
        "blueprint_file_sha256": file_sha(BLUEPRINT),
        "blueprint_row_sha256": sha_bytes(rows[11].encode("utf-8")),
        "title": "補助參與機構公開招生課程或進階課程優惠辦法之制度文件",
        "paper": "A4; sections 1-11 and 13 portrait; section 12 (65-row synthetic replacement register) landscape",
        "body_font_min_pt": 11,
        "table_font_pt": 9.5,
        "markdown_heading_count": heading_count,
        "markdown_table_count": table_count,
        "docx_table_count": len(reopened.tables),
        "docx_table_rows_including_headers": table_rows,
        "worker_source_sha256": EXPECTED_WORKER_SOURCE_SHA,
        "integrated_source_sha256": file_sha(SRC),
        "integration_receipt_path": str(INTEGRATION_RECEIPT),
        "integration_receipt_sha256": file_sha(INTEGRATION_RECEIPT),
        "synthetic_register_path": str(REGISTER),
        "synthetic_register_sha256": file_sha(REGISTER),
        "synthetic_register_records": len(register_rows),
        "semantic_review": "PENDING",
        "visual_review": "PENDING",
        "formal_acceptance": "UNKNOWN"
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    write_docx()
