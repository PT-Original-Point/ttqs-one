from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import subprocess, hashlib, json, datetime, sys

repo=Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016")
base=repo/"docs/ttqs-quality-20261016/quality-review/0059_R01"
content=base/"worker/opencode/0059_DOCUMENT_BODY_R03_FINAL.md"
build=base/"build"
template=build/"0059_reference_template_R03.docx"
output=base/"0059_R03.docx"
pandoc=Path(r"C:\Users\J\AppData\Local\Pandoc\pandoc.exe")
font_name="Microsoft JhengHei"
blue="1F4E79"
gray="5B6573"

def set_font(style, size, bold=False, color=None):
    style.font.name=font_name
    style.font.size=Pt(size)
    style.font.bold=bold
    if color: style.font.color.rgb=RGBColor.from_string(color)
    rpr=style.element.get_or_add_rPr()
    rfonts=rpr.rFonts
    if rfonts is None:
        rfonts=OxmlElement("w:rFonts"); rpr.insert(0,rfonts)
    for key in ("ascii","hAnsi","eastAsia","cs"):
        rfonts.set(qn("w:"+key),font_name)

# Create a Pandoc reference document with page furniture and named styles.
ref=Document()
sec=ref.sections[0]
sec.page_width=Inches(8.27); sec.page_height=Inches(11.69)
sec.top_margin=Inches(0.72); sec.bottom_margin=Inches(0.70)
sec.left_margin=Inches(0.72); sec.right_margin=Inches(0.72)
sec.header_distance=Inches(0.28); sec.footer_distance=Inches(0.28)
normal=ref.styles["Normal"]; set_font(normal,11,color="202833")
normal.paragraph_format.space_after=Pt(5)
normal.paragraph_format.line_spacing=1.15
for name,size in [("Title",25),("Subtitle",13),("Heading 1",17),("Heading 2",15),("Heading 3",12)]:
    st=ref.styles[name]; set_font(st,size,bold=name!="Subtitle",color=blue if "Heading" in name or name=="Title" else gray)
    st.paragraph_format.space_before=Pt(10 if name!="Title" else 4)
    st.paragraph_format.space_after=Pt(5)
    st.paragraph_format.keep_with_next=True
    st.paragraph_format.keep_together=True
for name in ("List Bullet","List Number"):
    set_font(ref.styles[name],10.5,color="202833")
    ref.styles[name].paragraph_format.space_after=Pt(3)
# Header
h=sec.header.paragraphs[0]
h.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=h.add_run("TTQS ONE  ｜  I13-E03  ｜  候選合成案例")
r.font.name=font_name; r.font.size=Pt(8.5); r.font.color.rgb=RGBColor.from_string(gray)
r._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"),font_name)
# Footer with a genuine Word PAGE field.
f=sec.footer.paragraphs[0]
f.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=f.add_run("CANDIDATE · SAMPLE/SYNTHETIC  ｜  第 ")
r.font.name=font_name; r.font.size=Pt(8); r.font.color.rgb=RGBColor.from_string(gray)
r._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"),font_name)
field=OxmlElement("w:fldSimple"); field.set(qn("w:instr"),"PAGE"); f._p.append(field)
r=f.add_run(" 頁")
r.font.name=font_name; r.font.size=Pt(8); r.font.color.rgb=RGBColor.from_string(gray)
r._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"),font_name)
ref.save(template)

cmd=[str(pandoc),"-f","gfm","-t","docx","--reference-doc",str(template),"-o",str(output),str(content)]
p=subprocess.run(cmd,cwd=repo,capture_output=True,text=True)
if p.returncode:
    print(p.stderr,file=sys.stderr); raise SystemExit(p.returncode)
doc=Document(output)
available=sec.page_width-sec.left_margin-sec.right_margin
# Reapply East Asian fonts, consistent paragraph spacing, and compact table typography.
for para in doc.paragraphs:
    if para.style and para.style.name.startswith("Heading"):
        para.paragraph_format.keep_with_next=True
        para.paragraph_format.keep_together=True
    # Keep this bold survey subsection label with the Q9-Q10 question table.
    if para.text.strip() == "構面三：可近性與公平性（Q9–Q10）":
        para.paragraph_format.keep_with_next=True
        para.paragraph_format.keep_together=True
    for run in para.runs:
        run.font.name=font_name
        rpr=run._element.get_or_add_rPr()
        rf=rpr.rFonts
        if rf is None:
            rf=OxmlElement("w:rFonts"); rpr.insert(0,rf)
        rf.set(qn("w:eastAsia"),font_name)
# Start the reading guide on page 2, leaving the document identity as cover.
for para in doc.paragraphs:
    if "閱讀導覽" in para.text:
        para.paragraph_format.page_break_before=True
        break
def set_cell_shading(cell,fill):
    tcpr=cell._tc.get_or_add_tcPr()
    shd=tcpr.find(qn("w:shd"))
    if shd is None: shd=OxmlElement("w:shd"); tcpr.append(shd)
    shd.set(qn("w:fill"),fill)
def set_cell_margins(cell,top=70,start=75,bottom=70,end=75):
    tc=cell._tc; tcPr=tc.get_or_add_tcPr()
    tcMar=tcPr.first_child_found_in("w:tcMar")
    if tcMar is None: tcMar=OxmlElement("w:tcMar"); tcPr.append(tcMar)
    for m,v in (("top",top),("start",start),("bottom",bottom),("end",end)):
        node=tcMar.find(qn("w:"+m))
        if node is None: node=OxmlElement("w:"+m); tcMar.append(node)
        node.set(qn("w:w"),str(v)); node.set(qn("w:type"),"dxa")
def set_repeat_table_header(row):
    trpr=row._tr.get_or_add_trPr()
    tblHeader=OxmlElement("w:tblHeader"); tblHeader.set(qn("w:val"),"true"); trpr.append(tblHeader)
def prevent_row_split(row):
    trpr=row._tr.get_or_add_trPr()
    el=OxmlElement("w:cantSplit"); trpr.append(el)
# Preserve the table's source-heading context so the repair targets only the
# isolated 4.3 execution-step header found on rendered page 8.
table_contexts=[]
last_paragraph=""
for child in doc.element.body.iterchildren():
    if child.tag == qn("w:p"):
        para=Paragraph(child,doc)
        if para.text.strip(): last_paragraph=para.text.strip()
    elif child.tag == qn("w:tbl"):
        table_contexts.append(last_paragraph)
        last_paragraph=""
for table_index,table in enumerate(doc.tables):
    table.alignment=WD_TABLE_ALIGNMENT.CENTER
    table.autofit=False
    n=len(table.columns)
    width=available/n
    header_text=tuple(" ".join(cell.text.split()) for cell in table.rows[0].cells) if table.rows else ()
    keep_header_with_first_record = (
        table_contexts[table_index] == "4.3 執行步驟"
        or table_contexts[table_index] == "4.7 狀態字典"
        or
        header_text[:2] == ("情境項目", "合成設定與操作")
        or header_text[:5] == ("學員", "首測分數／結果", "補強日期", "重測日期", "重測結果／最終狀態")
    )
    for row_idx,row in enumerate(table.rows):
        prevent_row_split(row)
        if row_idx==0: set_repeat_table_header(row)
        for cell in row.cells:
            cell.width=width
            cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            if row_idx==0: set_cell_shading(cell,blue)
            for para in cell.paragraphs:
                para.paragraph_format.space_before=Pt(0)
                para.paragraph_format.space_after=Pt(0)
                para.paragraph_format.line_spacing=1.0
                if row_idx==0 and keep_header_with_first_record:
                    para.paragraph_format.keep_with_next=True
                for run in para.runs:
                    run.font.name=font_name
                    run.font.size=Pt(9.5)
                    run.font.bold=(row_idx==0)
                    if row_idx==0: run.font.color.rgb=RGBColor(255,255,255)
                    rpr=run._element.get_or_add_rPr()
                    rf=rpr.rFonts
                    if rf is None: rf=OxmlElement("w:rFonts"); rpr.insert(0,rf)
                    rf.set(qn("w:eastAsia"),font_name)
# Reassert document properties and save the final candidate bytes.
doc.core_properties.title="訓練成果移轉機制運作與證據整合報告"
doc.core_properties.subject="0059 R03 / I13-E03 / checkbox 063 / SAMPLE-SYN-113"
doc.core_properties.author="TTQS ONE candidate production"
doc.save(output)
print(json.dumps({
 "output":str(output),"sha256":hashlib.sha256(output.read_bytes()).hexdigest().upper(),
 "bytes":output.stat().st_size,"content_sha256":hashlib.sha256(content.read_bytes()).hexdigest().upper(),
 "tables":len(Document(output).tables),"template":str(template),"pandoc_exit":p.returncode,
 "pandoc_stderr":p.stderr[:500]
},ensure_ascii=False))
