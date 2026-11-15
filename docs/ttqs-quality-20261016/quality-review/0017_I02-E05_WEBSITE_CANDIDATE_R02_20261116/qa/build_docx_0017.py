from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path
import re, hashlib, json

root = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0017_I02-E05_WEBSITE_R01_20261116")
source = root / "worker" / "ADOPTED_BODY_R03.md"
out = root / "candidate" / "0017_WEBSITE_DISCLOSURE_R02.docx"
lines = source.read_text(encoding="utf-8").splitlines()

def font(run, size=10.5, bold=None, color=None, name="Microsoft JhengHei"):
    run.font.name=name; run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"),name); run.font.size=Pt(size)
    if bold is not None: run.bold=bold
    if color is not None: run.font.color.rgb=RGBColor(*color)

def inline(p,s,size=10.5,color=None):
    s=s.replace(chr(96),"")
    parts=re.split(r"(\*\*.+?\*\*)",s)
    for part in parts:
        if not part: continue
        b=part.startswith("**") and part.endswith("**")
        r=p.add_run(part[2:-2] if b else part); font(r,size=size,bold=True if b else None,color=color)

def cells(line): return [x.strip() for x in line.strip().strip("|").split("|")]
def sep(line): return bool(re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$",line))
def shade(c):
    x=OxmlElement("w:shd"); x.set(qn("w:fill"),"D9EAF7"); c._tc.get_or_add_tcPr().append(x)
def dont_split(row): row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))

doc=Document(); sec=doc.sections[0]
sec.top_margin=Inches(.68); sec.bottom_margin=Inches(.68); sec.left_margin=Inches(.78); sec.right_margin=Inches(.78)
normal=doc.styles["Normal"]; normal.font.name="Microsoft JhengHei"; normal._element.rPr.rFonts.set(qn("w:eastAsia"),"Microsoft JhengHei"); normal.font.size=Pt(10.5); normal.paragraph_format.space_after=Pt(4); normal.paragraph_format.line_spacing=1.08
for name,size,color in [("Title",20,(31,55,83)),("Heading 1",15,(31,78,121)),("Heading 2",12.5,(46,92,138)),("Heading 3",11,(70,95,120))]:
    st=doc.styles[name]; st.font.name="Microsoft JhengHei"; st._element.rPr.rFonts.set(qn("w:eastAsia"),"Microsoft JhengHei"); st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=RGBColor(*color); st.paragraph_format.space_before=Pt(8); st.paragraph_format.space_after=Pt(4)
h=sec.header.paragraphs[0]; h.alignment=WD_ALIGN_PARAGRAPH.RIGHT; font(h.add_run("TTQS ONE｜0017｜CANDIDATE / SAMPLE"),8,color=(95,105,115))
f=sec.footer.paragraphs[0]; f.alignment=WD_ALIGN_PARAGRAPH.CENTER; font(f.add_run("未核准・未公開・報名關閉｜不得作為正式招生或收款頁"),8,color=(105,105,105))
i=0
while i<len(lines):
    s=lines[i].strip()
    if not s or s=="---": i+=1; continue
    if s.startswith("|") and i+1<len(lines) and sep(lines[i+1]):
        hs=cells(s); i+=2; rows=[]
        while i<len(lines) and lines[i].strip().startswith("|"): rows.append(cells(lines[i])); i+=1
        t=doc.add_table(rows=1,cols=len(hs)); t.style="Table Grid"; t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=True
        trPr=t.rows[0]._tr.get_or_add_trPr(); hd=OxmlElement("w:tblHeader"); hd.set(qn("w:val"),"true"); trPr.append(hd)
        for j,val in enumerate(hs):
            c=t.rows[0].cells[j]; c.text=""; shade(c); p=c.paragraphs[0]; p.paragraph_format.space_after=Pt(0); inline(p,val,9.5)
            for r in p.runs:r.bold=True
        for vals in rows:
            cs=t.add_row().cells; dont_split(t.rows[-1])
            for j,c in enumerate(cs):
                c.text=""; p=c.paragraphs[0]; p.paragraph_format.space_after=Pt(0); p.paragraph_format.line_spacing=1
                inline(p,vals[j] if j<len(vals) else "",9.5)
        doc.add_paragraph().paragraph_format.space_after=Pt(1); continue
    s=s.replace(chr(96),"")
    hm=re.match(r"^(#{1,4})\s+(.*)$",s)
    if hm:
        lev=len(hm.group(1)); title=hm.group(2)
        if lev==1: p=doc.add_paragraph(style="Title"); inline(p,title,20,(31,55,83))
        else: p=doc.add_paragraph(style="Heading "+str(min(lev-1,3))); inline(p,title,{2:15,3:12.5,4:11}[lev])
        i+=1; continue
    if s.startswith(">"):
        p=doc.add_paragraph(style="Quote"); p.paragraph_format.left_indent=Inches(.18); inline(p,s[1:].strip(),10.5,(60,70,80)); i+=1; continue
    if re.match(r"^[-*]\s+",s):
        p=doc.add_paragraph(style="List Bullet"); inline(p,re.sub(r"^[-*]\s+","",s),10.5); i+=1; continue
    n=re.match(r"^\d+\.\s+(.*)$",s)
    if n:
        p=doc.add_paragraph(style="List Number"); inline(p,n.group(1),10.5); i+=1; continue
    p=doc.add_paragraph(); inline(p,s,10.5)
    if re.match(r"^\*\*Q\d+：",s): p.paragraph_format.keep_with_next=True
    i+=1
doc.core_properties.title="網站課程揭露頁完整內容｜0017"; doc.core_properties.subject="I02-E05 SAMPLE/SYNTHETIC CANDIDATE"; doc.core_properties.author="TTQS ONE Candidate Workflow"; doc.save(out)
v=Document(out); plain="\n".join(p.text for p in v.paragraphs); tabs="\n".join(" | ".join(c.text for c in row.cells) for t in v.tables for row in t.rows); alltext=plain+"\n"+tabs
checks={
"docx_reopens":len(v.paragraphs)>0 and len(v.tables)>=2,
"boundary":all(x in alltext for x in ["SAMPLE","SYNTHETIC","CANDIDATE","未核准","未公開","報名關閉"]),
"title":"非營利專案紀錄入門：從需求到證據的練習" in alltext,
"agenda":all(x in alltext for x in ["09:30–09:50","09:50–10:15","10:15–10:40","10:40–10:50","10:50–11:20","11:20–11:55","11:55–12:30"]),
"hours":"170" in alltext and "180" in alltext,
"inactive_urls":"https://example.invalid/courses/sample-0017" in alltext and "https://example.invalid/register/sample-0017" in alltext,
"no_transaction":"不收款" in alltext and "不接收報名" in alltext,
"no_placeholders":not any(x in alltext for x in ["待填","待核","保持空白","會後填寫"]),
"tables":len(v.tables)>=2,
"body_min_font":all(r.font.size is None or r.font.size.pt>=10.5 for p in v.paragraphs for r in p.runs if r.text.strip()),
"table_min_font":all(r.font.size is None or r.font.size.pt>=9.5 for t in v.tables for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs if r.text.strip())
}
sha=hashlib.sha256(out.read_bytes()).hexdigest()
receipt={"work_id":"TTQS-0017-I02-E05-WEBSITE-DOCX-R01-20261116","candidate_path":str(out),"candidate_sha256":sha,"paragraphs":len(v.paragraphs),"tables":len(v.tables),"checks":checks,"pass":all(checks.values()),"worker_body_sha256":hashlib.sha256(source.read_bytes()).hexdigest()}
(root/"qa"/"DETERMINISTIC_QA_R01.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False))
