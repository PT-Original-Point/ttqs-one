from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "0038_WRITER_MANUSCRIPT_W3_R02_20261101.md"
OUT = ROOT / "candidate" / "0038_I08-E02_R05_20261101.docx"
OUT.parent.mkdir(parents=True, exist_ok=True)
text = SOURCE.read_text(encoding="utf-8")
lines = text.splitlines()

NAVY = "17365D"
BLUE = "1F4E78"
PALE = "D9EAF7"
LIGHT = "F2F6FA"
WHITE = "FFFFFF"
GRAY = "526171"

doc = Document()
sec = doc.sections[0]
sec.page_width = Inches(8.27)
sec.page_height = Inches(11.69)
sec.top_margin = Inches(0.68)
sec.bottom_margin = Inches(0.68)
sec.left_margin = Inches(0.64)
sec.right_margin = Inches(0.64)
sec.header_distance = Inches(0.32)
sec.footer_distance = Inches(0.32)

def set_run_font(run, size=10.5, bold=None, color=None, italic=None):
    run.font.name = "Microsoft JhengHei"
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Microsoft JhengHei")
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), "Aptos")
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), "Aptos")
    run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if italic is not None: run.italic = italic
    if color: run.font.color.rgb = RGBColor.from_string(color)

styles = doc.styles
normal = styles["Normal"]
normal.font.name = "Microsoft JhengHei"
normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft JhengHei")
normal._element.rPr.rFonts.set(qn("w:ascii"), "Aptos")
normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos")
normal.font.size = Pt(10.5)
normal.font.color.rgb = RGBColor.from_string("202A35")
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.12

for name, size, color in [("Title", 22, NAVY), ("Heading 1", 15, NAVY), ("Heading 2", 12, BLUE), ("Heading 3", 10.5, BLUE)]:
    st = styles[name]
    st.font.name = "Microsoft JhengHei"
    st._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft JhengHei")
    st._element.rPr.rFonts.set(qn("w:ascii"), "Aptos")
    st._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos")
    st.font.size = Pt(size)
    st.font.bold = name != "Title" or True
    st.font.color.rgb = RGBColor.from_string(color)
    st.paragraph_format.keep_with_next = True
    st.paragraph_format.space_before = Pt(11 if name != "Title" else 0)
    st.paragraph_format.space_after = Pt(5)
    ppr = st._element.pPr
    if ppr is not None:
        border = ppr.find(qn("w:pBdr"))
        if border is not None:
            ppr.remove(border)

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcPr.append(shd)
    shd.set(qn("w:fill"), fill)

def set_cell_margins(cell, top=75, start=85, bottom=75, end=85):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in("w:tcMar")
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tcMar.find(qn("w:" + m))
        if node is None:
            node = OxmlElement("w:" + m)
            tcMar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")

def set_repeat_table_header(row):
    trPr = row._tr.get_or_add_trPr()
    tblHeader = OxmlElement("w:tblHeader")
    tblHeader.set(qn("w:val"), "true")
    trPr.append(tblHeader)

def prevent_row_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))

def add_rich(paragraph, value, size=10.5, base_color=None):
    # Inline **bold** and `code`; all other text remains literal.
    pattern = re.compile(r"(\*\*.*?\*\*|`.*?`)")
    pos = 0
    for m in pattern.finditer(value):
        if m.start() > pos:
            r = paragraph.add_run(value[pos:m.start()]); set_run_font(r, size, color=base_color)
        tok = m.group(0)
        if tok.startswith("**"):
            r = paragraph.add_run(tok[2:-2]); set_run_font(r, size, bold=True, color=base_color)
        else:
            r = paragraph.add_run(tok[1:-1]); set_run_font(r, size, color=BLUE)
            r.font.name = "Consolas"
        pos = m.end()
    if pos < len(value):
        r = paragraph.add_run(value[pos:]); set_run_font(r, size, color=base_color)

def parse_table_block(start):
    block=[]
    i=start
    while i < len(lines) and lines[i].strip().startswith("|"):
        block.append(lines[i].strip()); i+=1
    rows=[]
    for row in block:
        cells=[c.strip() for c in row.strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            continue
        rows.append(cells)
    return rows, i

def add_table(rows):
    if not rows: return
    cols=max(len(r) for r in rows)
    table=doc.add_table(rows=0, cols=cols)
    table.alignment=WD_TABLE_ALIGNMENT.CENTER
    table.autofit=True
    table.style="Table Grid"
    for ridx, values in enumerate(rows):
        row=table.add_row()
        prevent_row_split(row)
        for cidx in range(cols):
            cell=row.cells[cidx]
            cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            cell.text=""
            p=cell.paragraphs[0]
            p.paragraph_format.space_after=Pt(0)
            p.paragraph_format.line_spacing=1.0
            value=values[cidx] if cidx<len(values) else ""
            add_rich(p,value,size=9.5)
            if ridx==0:
                shade(cell,NAVY)
                for run in p.runs:
                    run.font.color.rgb=RGBColor.from_string(WHITE)
                    run.bold=True
            elif ridx%2==0:
                shade(cell,LIGHT)
        if ridx==0:
            set_repeat_table_header(row)
    spacer=doc.add_paragraph()
    spacer.paragraph_format.space_after=Pt(2)
    spacer.paragraph_format.space_before=Pt(0)

def add_page_field(paragraph):
    r=paragraph.add_run()
    begin=OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"),"begin")
    instr=OxmlElement("w:instrText"); instr.set(qn("xml:space"),"preserve"); instr.text=" PAGE "
    sep=OxmlElement("w:fldChar"); sep.set(qn("w:fldCharType"),"separate")
    txt=OxmlElement("w:t"); txt.text="1"
    end=OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"),"end")
    r._r.append(begin); r._r.append(instr); r._r.append(sep); r._r.append(txt); r._r.append(end)
    set_run_font(r,8,color=GRAY)

# Header and footer
hp=sec.header.paragraphs[0]
hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
rr=hp.add_run("TTQS ONE　｜　0038　I08-E02　｜　候選文件")
set_run_font(rr,8,color=GRAY)
fp=sec.footer.paragraphs[0]
fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
rr=fp.add_run("SAMPLE／SYNTHETIC 範例　　•　　頁次 "); set_run_font(rr,8,color=GRAY)
add_page_field(fp)

idx=0
first=True
while idx < len(lines):
    raw=lines[idx]
    s=raw.strip()
    if not s:
        idx+=1; continue
    if s.startswith("|"):
        rows,idx=parse_table_block(idx)
        add_table(rows)
        continue
    hm=re.match(r"^(#{1,3})\s+(.*)$",s)
    if hm:
        level=len(hm.group(1)); title=hm.group(2).strip()
        if first and level==1:
            p=doc.add_paragraph(style="Title")
            p.paragraph_format.space_after=Pt(12)
            ppr=p._p.get_or_add_pPr()
            border=ppr.find(qn("w:pBdr"))
            if border is not None:
                ppr.remove(border)
            add_rich(p,title,size=22,base_color=NAVY)
            first=False
        else:
            p=doc.add_paragraph(style=f"Heading {level}")
            if title == "表單B 修改設計驗證與下一步決定":
                p.paragraph_format.page_break_before=True
            if title == "9. 拒收／暫停檢核":
                p.paragraph_format.page_break_before=True
            add_rich(p,title,size={1:15,2:12,3:10.5}[level],base_color=NAVY if level==1 else BLUE)
        idx+=1; continue
    if re.match(r"^[-*]\s+",s):
        p=doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after=Pt(2)
        add_rich(p,re.sub(r"^[-*]\s+","",s),size=10.5)
        idx+=1; continue
    if re.match(r"^\d+[.)]\s+",s):
        p=doc.add_paragraph()
        p.paragraph_format.left_indent=Inches(0.25)
        p.paragraph_format.first_line_indent=Inches(-0.25)
        p.paragraph_format.space_after=Pt(2)
        add_rich(p,s,size=10.5)
        idx+=1; continue
    p=doc.add_paragraph()
    p.paragraph_format.widow_control=True
    add_rich(p,s,size=10.5)
    idx+=1

# Make headings/paragraphs readable and keep labels from breaking awkwardly.
for p in doc.paragraphs:
    if p.style.name.startswith("Heading"):
        p.paragraph_format.keep_with_next=True
    if p.style.name == "Title":
        p.paragraph_format.keep_with_next=True

doc.core_properties.title="訓練方案系統設計改善實施紀錄"
doc.core_properties.subject="0038／I08-E02／檢核碼039；SAMPLE／SYNTHETIC 候選"
doc.core_properties.author="TTQS ONE 候選文件"
doc.core_properties.keywords="0038; I08-E02; SAMPLE; SYNTHETIC"
doc.save(OUT)
print(f"OUTPUT={OUT}")
print(f"BYTES={OUT.stat().st_size}")
