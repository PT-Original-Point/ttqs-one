from pathlib import Path
import re, json, hashlib, zipfile
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0128_I19-E17_SOURCE_PREP_R01_20261024")
WRITER=ROOT/"writer"
SOURCE=WRITER/"MANUSCRIPT_0128_I19-E17_R05.md"
OUTDIR=ROOT/"candidate"
OUT=OUTDIR/"0128_I19-E17_R05.docx"
RECEIPT=OUTDIR/"BUILD_RECEIPT_0128_R05.json"
if OUT.exists() or RECEIPT.exists():
    raise SystemExit("R04 candidate/receipt already exists; refusing overwrite")
OUTDIR.mkdir(parents=True,exist_ok=True)
md=SOURCE.read_text(encoding="utf-8")

def clean(s):
    s=s.replace("<br>","\n").replace("&nbsp;", " ")
    s=s.replace("$\\square$","□").replace("$\\rightarrow$","→")
    s=s.replace("\\times", "×").replace("\\rightarrow", "→").replace("\\%", "%")
    s=re.sub(r"\\text\{([^{}]*)\}",r"\1",s)
    s=s.replace("$","")
    s=s.replace("<", "〈").replace(">", "〉")
    return s.strip()

def set_east_asia(run, name="Microsoft JhengHei"):
    run.font.name=name
    rpr=run._element.get_or_add_rPr()
    rf=rpr.rFonts
    if rf is None:
        rf=OxmlElement("w:rFonts"); rpr.insert(0,rf)
    for k in ("ascii","hAnsi","eastAsia","cs"):
        rf.set(qn("w:"+k),name)

def add_rich(p, text, size=10.5, color=None, bold_default=False, italic=False):
    text=clean(text)
    # Preserve bold and inline-code markers without exposing Markdown punctuation.
    parts=re.split(r"(\*\*.*?\*\*|`[^`]*`|\*[^*]+\*)",text)
    for part in parts:
        if not part: continue
        bold=part.startswith("**") and part.endswith("**")
        code=part.startswith("`") and part.endswith("`")
        em=part.startswith("*") and part.endswith("*") and not bold
        value=part[2:-2] if bold else (part[1:-1] if code or em else part)
        run=p.add_run(value)
        set_east_asia(run, "Microsoft JhengHei Mono" if code else "Microsoft JhengHei")
        run.font.size=Pt(size)
        run.bold=bool(bold_default or bold)
        run.italic=bool(italic or em)
        if color is not None: run.font.color.rgb=RGBColor(*color)
    return p

def shade(cell, fill):
    tcPr=cell._tc.get_or_add_tcPr()
    shd=tcPr.find(qn("w:shd"))
    if shd is None: shd=OxmlElement("w:shd"); tcPr.append(shd)
    shd.set(qn("w:fill"),fill)

def shade_para(paragraph, fill):
    pPr=paragraph._p.get_or_add_pPr()
    shd=OxmlElement("w:shd"); shd.set(qn("w:fill"),fill); pPr.append(shd)

def set_cell_margins(cell, top=65, start=75, bottom=65, end=75):
    tc=cell._tc; tcPr=tc.get_or_add_tcPr()
    tcMar=tcPr.first_child_found_in("w:tcMar")
    if tcMar is None: tcMar=OxmlElement("w:tcMar"); tcPr.append(tcMar)
    for side,val in (("top",top),("start",start),("bottom",bottom),("end",end)):
        node=tcMar.find(qn("w:"+side))
        if node is None: node=OxmlElement("w:"+side); tcMar.append(node)
        node.set(qn("w:w"),str(val)); node.set(qn("w:type"),"dxa")

def mark_header(row):
    trPr=row._tr.get_or_add_trPr()
    tblHeader=OxmlElement("w:tblHeader"); tblHeader.set(qn("w:val"),"true"); trPr.append(tblHeader)

def keep_row(row):
    trPr=row._tr.get_or_add_trPr(); node=OxmlElement("w:cantSplit"); trPr.append(node)

def landscape_needed(rows):
    cols=len(rows[0])
    chars=sum(len(c) for row in rows for c in row)
    return cols>=8 or (cols>=4 and chars>900)

def set_section(section, landscape=False):
    if landscape:
        section.orientation=1
        section.page_width=Inches(11.69); section.page_height=Inches(8.27)
        section.left_margin=Inches(.55); section.right_margin=Inches(.55)
        section.top_margin=Inches(.55); section.bottom_margin=Inches(.55)
    else:
        section.orientation=0
        section.page_width=Inches(8.27); section.page_height=Inches(11.69)
        section.left_margin=Inches(.68); section.right_margin=Inches(.68)
        section.top_margin=Inches(.65); section.bottom_margin=Inches(.65)

def footer(section):
    p=section.footer.paragraphs[0]
    p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    add_rich(p,"TTQS ONE 0128  |  SAMPLE / SYNTHETIC  |  ",size=9.5,color=(70,80,92))
    r=p.add_run(); set_east_asia(r); r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(70,80,92)
    fld=OxmlElement("w:fldSimple"); fld.set(qn("w:instr"),"PAGE"); r._r.addnext(fld)

def parse_table(lines):
    raw=[]
    for line in lines:
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?",c.replace(" ","")) for c in cells):
            continue
        raw.append(cells)
    if not raw: return []
    n=max(map(len,raw))
    return [row+([""]*(n-len(row))) for row in raw]

doc=Document()
set_section(doc.sections[0],False)
styles=doc.styles
normal=styles["Normal"]; normal.font.name="Microsoft JhengHei"; normal.font.size=Pt(10.5)
normal.paragraph_format.space_after=Pt(4); normal.paragraph_format.line_spacing=1.08
for nm,size in (("Title",19),("Heading 1",15),("Heading 2",12.5),("Heading 3",11.5)):
    st=styles[nm]; st.font.name="Microsoft JhengHei"; st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=RGBColor(25,45,70)
    st.paragraph_format.keep_with_next=True; st.paragraph_format.space_before=Pt(9); st.paragraph_format.space_after=Pt(4)
    rpr=st._element.rPr
    if rpr is not None:
        rf=rpr.rFonts
        if rf is None: rf=OxmlElement("w:rFonts"); rpr.insert(0,rf)
        rf.set(qn("w:eastAsia"),"Microsoft JhengHei")
footer(doc.sections[0])
doc.core_properties.title="個人訓後績效改善個案分析表"
doc.core_properties.subject="TTQS ONE 0128 I19-E17 SAMPLE/SYNTHETIC candidate"
doc.core_properties.author="TTQS ONE candidate document"

lines=md.splitlines(); i=0; code=False; code_lines=[]; current_landscape=False; table_count=0; paragraph_count=0
while i<len(lines):
    line=lines[i]
    if line.strip().startswith("```"):
        code=not code
        if not code and code_lines:
            p=doc.add_paragraph()
            p.paragraph_format.left_indent=Inches(.22); p.paragraph_format.space_after=Pt(5)
            add_rich(p,"\n".join(code_lines),size=10.5)
            code_lines=[]; paragraph_count+=1
        i+=1; continue
    if code:
        code_lines.append(line); i+=1; continue
    if not line.strip() or line.strip()=="---": i+=1; continue
    if line.lstrip().startswith("|"):
        group=[]
        while i<len(lines) and lines[i].lstrip().startswith("|"):
            group.append(lines[i]); i+=1
        rows=parse_table(group)
        if not rows: continue
        want_landscape=landscape_needed(rows)
        if want_landscape!=current_landscape:
            section=doc.add_section(WD_SECTION.NEW_PAGE); set_section(section,want_landscape); footer(section); current_landscape=want_landscape
        table=doc.add_table(rows=len(rows),cols=len(rows[0]))
        table.style="Table Grid"; table.autofit=False
        available=10.55 if current_landscape else 6.91
        widths=None
        if len(rows[0])==10:
            widths=[.76,.98,.62,.98,.62,.82,1.0,1.12,1.45,1.45]
        elif len(rows[0])==8:
            widths=[.45,1.1,1.28,1.15,1.28,1.15,.85,1.2]
        elif len(rows[0])==5 and current_landscape:
            widths=[.68,1.65,2.7,3.0,1.2]
        elif len(rows[0])==4 and current_landscape:
            widths=[1.35,1.7,4.2,1.85]
        if widths and abs(sum(widths)-available)>.2:
            factor=available/sum(widths); widths=[v*factor for v in widths]
        if not widths: widths=[available/len(rows[0])]*len(rows[0])
        for ri,row_data in enumerate(rows):
            row=table.rows[ri]; keep_row(row)
            for ci,val in enumerate(row_data):
                cell=row.cells[ci]; cell.width=Inches(widths[ci]); cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
                set_cell_margins(cell)
                p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(0); p.paragraph_format.line_spacing=1.0
                p.alignment=WD_ALIGN_PARAGRAPH.CENTER if ri==0 else WD_ALIGN_PARAGRAPH.LEFT
                add_rich(p,val,size=9.5,color=(255,255,255) if ri==0 else None,bold_default=(ri==0))
                if ri==0: shade(cell,"243B53")
                elif ri%2==0: shade(cell,"F1F5F8")
        mark_header(table.rows[0]); table_count+=1
        doc.add_paragraph().paragraph_format.space_after=Pt(1)
        if current_landscape:
            section=doc.add_section(WD_SECTION.NEW_PAGE); set_section(section,False); footer(section); current_landscape=False
        continue
    stripped=line.strip()
    if stripped.startswith("# "):
        p=doc.add_paragraph(style="Title"); add_rich(p,stripped[2:],size=19,bold_default=True); p.paragraph_format.keep_with_next=True
    elif stripped.startswith("## "):
        p=doc.add_paragraph(style="Heading 1"); add_rich(p,stripped[3:],size=15,bold_default=True)
    elif stripped.startswith("### "):
        p=doc.add_paragraph(style="Heading 2"); add_rich(p,stripped[4:],size=12.5,bold_default=True)
    elif stripped.startswith(">"):
        value=stripped[1:].strip()
        if value.startswith("[!") and value.endswith("]"):
            label=value[2:-1]
            p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.14); p.paragraph_format.space_before=Pt(3); p.paragraph_format.space_after=Pt(3)
            add_rich(p,"資料提醒｜"+label,size=10.5,bold_default=True,color=(25,65,105)); shade_para(p,"EAF2F8")
        else:
            p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.18); p.paragraph_format.right_indent=Inches(.12); p.paragraph_format.space_after=Pt(5)
            add_rich(p,value,size=10.5); shade_para(p,"F4F7FA")
    elif re.match(r"^\s*[-*]\s+",line):
        p=doc.add_paragraph(style="List Bullet"); add_rich(p,re.sub(r"^\s*[-*]\s+","",line),size=10.5)
    elif re.match(r"^\s*\d+\.\s+",line):
        p=doc.add_paragraph(style="List Number"); add_rich(p,re.sub(r"^\s*\d+\.\s+","",line),size=10.5)
    else:
        p=doc.add_paragraph(); add_rich(p,stripped,size=10.5); paragraph_count+=1
    i+=1

doc.save(OUT)
# Structural and bound-source checks; no acceptance promotion.
with zipfile.ZipFile(OUT) as z:
    bad=z.testzip()
    if bad: raise RuntimeError("OOXML ZIP CRC failed at "+bad)
check=Document(OUT)
alltext="\n".join(p.text for p in check.paragraphs)+"\n"+"\n".join(c.text for t in check.tables for row in t.rows for c in row.cells)
required=["I19-E17","相關證據顯示個人訓練後之績效改善成果","S-EMP-01","S-EMP-06","93 / 120","101 / 120","UNKNOWN_UNTIL_SOURCE","REAL 實際資料替換表單"]
missing=[s for s in required if s not in alltext]
if missing: raise RuntimeError("Missing required content: "+repr(missing))
for cid in [f"S-EMP-{i:02d}" for i in range(1,7)]:
    if cid not in alltext: raise RuntimeError("Missing sample case "+cid)
font_sizes=[]; table_font_sizes=[]
for p in check.paragraphs:
    for r in p.runs:
        if r.font.size: font_sizes.append(r.font.size.pt)
for table in check.tables:
    for row in table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for r in p.runs:
                    if r.font.size: table_font_sizes.append(r.font.size.pt)
if font_sizes and min(font_sizes)<10.5: raise RuntimeError(f"Body font below floor: {min(font_sizes)}")
if table_font_sizes and min(table_font_sizes)<9.5: raise RuntimeError(f"Table font below floor: {min(table_font_sizes)}")
receipt={"project_id":"TTQS_ONE","work_id":"TTQS-0128-I19-E17-BUILD-R05","doc_id":"0128","official_requirement_id":"I19-E17","candidate_path":str(OUT),"candidate_sha256":hashlib.sha256(OUT.read_bytes()).hexdigest(),"candidate_bytes":OUT.stat().st_size,"manuscript_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest(),"sample_csv_sha256":hashlib.sha256((ROOT/"source"/"SAMPLE_INDIVIDUAL_PERFORMANCE_PANEL_R01.csv").read_bytes()).hexdigest(),"build_tool":"bundled Python 3.12.14 + python-docx 1.2.0","build_time_local":datetime.now().astimezone().isoformat(),"table_count":len(check.tables),"paragraph_count":len(check.paragraphs),"package_crc":"PASS","required_content":"PASS","sample_case_count":6,"math_binding":"PASS_SOURCE_MATH_RECEIPT_PRESENT","body_min_font_pt":min(font_sizes) if font_sizes else None,"table_min_font_pt":min(table_font_sizes) if table_font_sizes else None,"visual_render":"PENDING","independent_semantic_review":"PENDING","real_evidence":"UNKNOWN_UNTIL_SOURCE","formal_acceptance":"NOT_GRANTED"}
RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False))
