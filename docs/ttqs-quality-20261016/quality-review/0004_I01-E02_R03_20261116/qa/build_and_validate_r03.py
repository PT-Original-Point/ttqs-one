from pathlib import Path
from docx import Document
from docx.shared import Pt, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import csv,hashlib,json,re,datetime,sys
rt=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME");work=rt/"WORK"/"QUALITY_REBUILD_20261016"/"0004_I01-E02_SOURCE_PREP_R03_20261116"
worker=work/"worker";candidate=work/"candidate";qa_dir=work/"qa";candidate.mkdir(parents=True,exist_ok=True)
md=Path(sys.argv[1]) if len(sys.argv)>1 else worker/"worker_manuscript_repaired_raw.md"
reg=work/"SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R03.csv";manifest=work/"SOURCE_PREP_MANIFEST_0004_R03.json";sourceqa=work/"SOURCE_PREP_QA_R03.json"
docx=candidate/"0004_I01-E02_R03_CANDIDATE.docx"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def split_row(line):
 s=line.strip()
 if s.startswith("|"):s=s[1:]
 if s.endswith("|"):s=s[:-1]
 return [x.strip().replace(r"\|","|") for x in re.split(r"(?<!\\)\|",s)]
def sep(c):return bool(c) and all(re.fullmatch(r":?-{3,}:?",x.replace(" ","")) for x in c)
def sf(run,size=11,bold=None,name="Microsoft JhengHei",color=None):
 run.font.name=name;run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"),name);run.font.size=Pt(size)
 if bold is not None:run.bold=bold
 if color:run.font.color.rgb=color
def inline(p,text,size=11):
 tick=chr(96);pat=re.compile(r"(\*\*.+?\*\*|"+tick+r"[^"+tick+r"]+"+tick+r"|\*[^*]+\*)");pos=0
 for m in pat.finditer(text):
  if m.start()>pos:sf(p.add_run(text[pos:m.start()]),size)
  x=m.group(0)
  if x.startswith("**"):sf(p.add_run(x[2:-2]),size,True)
  elif x.startswith(tick):sf(p.add_run(x[1:-1]),size,name="Consolas",color=__import__("docx").shared.RGBColor.from_string("1F4E79"))
  else:
   r=p.add_run(x[1:-1]);sf(r,size);r.italic=True
  pos=m.end()
 if pos<len(text):sf(p.add_run(text[pos:]),size)
text=md.read_text(encoding="utf-8-sig").replace("\r\n","\n");lines=text.splitlines()
doc=Document();sec=doc.sections[0];sec.page_width=Mm(210);sec.page_height=Mm(297)
sec.top_margin=Mm(17.8);sec.bottom_margin=Mm(17.8);sec.left_margin=Mm(17.8);sec.right_margin=Mm(17.8)
sec.header_distance=Mm(8);sec.footer_distance=Mm(8)
normal=doc.styles["Normal"];normal.font.name="Microsoft JhengHei";normal._element.rPr.rFonts.set(qn("w:eastAsia"),"Microsoft JhengHei");normal.font.size=Pt(11)
styles={"Title":(19,"17365D"),"Heading 1":(15,"17365D"),"Heading 2":(13,"1F4E79"),"Heading 3":(11.5,"2F5597"),"Heading 4":(11,"2F5597")}
for n,(sz,col) in styles.items():
 s=doc.styles[n];s.font.name="Microsoft JhengHei";s._element.rPr.rFonts.set(qn("w:eastAsia"),"Microsoft JhengHei");s.font.size=Pt(sz);s.font.bold=True;s.font.color.rgb=__import__("docx").shared.RGBColor.from_string(col);s.paragraph_format.keep_with_next=True;s.paragraph_format.space_before=Pt(9);s.paragraph_format.space_after=Pt(4)
h=sec.header.paragraphs[0];h.alignment=WD_ALIGN_PARAGRAPH.RIGHT;sf(h.add_run("TTQS ONE | CANDIDATE | SAMPLE/SYNTHETIC"),9.5,color=__import__("docx").shared.RGBColor.from_string("666666"))
f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.CENTER;sf(f.add_run("0004 • I01-E02 • 非正式接受 | 第 "),9.5,color=__import__("docx").shared.RGBColor.from_string("666666"))
field=OxmlElement("w:fldSimple");field.set(qn("w:instr"),"PAGE");f._p.append(field);sf(f.add_run(" 頁"),9.5,color=__import__("docx").shared.RGBColor.from_string("666666"))
def table(rows):
 cols=len(rows[0]);t=doc.add_table(rows=1,cols=cols);t.style="Table Grid";t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
 usable=Mm(210-17.8*2)
 weights={2:[.34,.66],3:[.24,.34,.42],4:[.18,.25,.23,.34],5:[.15,.19,.21,.20,.25]}.get(cols,[1/cols]*cols)
 for j,w in enumerate(weights):t.columns[j].width=int(usable*w)
 for ri,row in enumerate(rows):
  cells=t.rows[0].cells if ri==0 else t.add_row().cells
  tr=t.rows[ri]._tr.get_or_add_trPr();tr.append(OxmlElement("w:cantSplit"))
  if ri==0:tr.append(OxmlElement("w:tblHeader"))
  for j,val in enumerate(row):
   c=cells[j];c.width=int(usable*weights[j]);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP;c.text=""
   p=c.paragraphs[0];p.paragraph_format.space_after=Pt(1);p.paragraph_format.space_before=Pt(0);p.paragraph_format.keep_together=True;p.paragraph_format.keep_with_next=(ri==0)
   inline(p,re.sub(r"<br\s*/?>","\n",val.strip(),flags=re.I),9.5)
   if ri==0:
    sh=OxmlElement("w:shd");sh.set(qn("w:fill"),"1F4E79");c._tc.get_or_add_tcPr().append(sh)
    for r in p.runs:r.bold=True;r.font.color.rgb=__import__("docx").shared.RGBColor.from_string("FFFFFF")
   else:
    mar=OxmlElement("w:tcMar")
    for e0 in ("top","start","bottom","end"):
     e=OxmlElement("w:"+e0);e.set(qn("w:w"),"70");e.set(qn("w:type"),"dxa");mar.append(e)
    c._tc.get_or_add_tcPr().append(mar)
 doc.add_paragraph().paragraph_format.space_after=Pt(1)
fence=chr(96)*3;i=0;in_code=False;code=[]
while i<len(lines):
 line=lines[i]
 if line.strip().startswith(fence):
  if not in_code:in_code=True;code=[]
  else:
   p=doc.add_paragraph()
   for k,x in enumerate(code):sf(p.add_run(x+("\n" if k<len(code)-1 else "")),9.5,name="Consolas")
   in_code=False
  i+=1;continue
 if in_code:code.append(line);i+=1;continue
 if not line.strip() or re.fullmatch(r"\s*([-*_])\1{2,}\s*",line):i+=1;continue
 if line.lstrip().startswith("|"):
  rows=[]
  while i<len(lines) and lines[i].lstrip().startswith("|"):
   cells=split_row(lines[i])
   if not sep(cells):rows.append(cells)
   i+=1
  if rows:
   n=max(map(len,rows));table([r+[""]*(n-len(r)) for r in rows])
  continue
 hm=re.match(r"^(#{1,4})\s+(.*)$",line)
 if hm:
  n=len(hm.group(1));sty="Title" if n==1 else "Heading "+str(n-1);p=doc.add_paragraph(style=sty);inline(p,hm.group(2),styles[sty][0])
  if n==1:p.alignment=WD_ALIGN_PARAGRAPH.CENTER
  i+=1;continue
 bm=re.match(r"^\s*[-*+]\s+(.*)$",line);nm=re.match(r"^\s*\d+[.)]\s+(.*)$",line)
 if bm or nm:
  p=doc.add_paragraph(style="List Bullet" if bm else "List Number");p.paragraph_format.space_after=Pt(2);inline(p,(bm or nm).group(1),11);i+=1;continue
 p=doc.add_paragraph();p.paragraph_format.space_after=Pt(5);p.paragraph_format.line_spacing=1.08;inline(p,line.strip(),11);i+=1
doc.core_properties.title="0004 目標市場調查執行與樣本紀錄（R03 CANDIDATE）";doc.core_properties.subject="TTQS ONE I01-E02; SAMPLE/SYNTHETIC candidate; not formal acceptance";doc.core_properties.author="TTQS ONE";doc.save(docx)
d=Document(docx);alltext="\n".join([p.text for p in d.paragraphs]+[c.text for t in d.tables for row in t.rows for c in row.cells])
with reg.open("r",encoding="utf-8-sig",newline="") as f0:facts=list(csv.DictReader(f0));ids=[x["fact_id"] for x in facts]
counts=["SYN-0004-COUNT-SCREENED","SYN-0004-COUNT-INELIGIBLE","SYN-0004-COUNT-ELIGIBLE_INVITES","SYN-0004-COUNT-UNIQUE_RETURNS","SYN-0004-COUNT-VALID_UNIQUE","SYN-0004-COUNT-INVALID_UNIQUE","SYN-0004-COUNT-REFUSALS","SYN-0004-COUNT-NO_RESPONSE","SYN-0004-COUNT-DUPLICATE_EXTRAS","SYN-0004-COUNT-RAW_RECEIPT_EVENTS"]
flows=["SYN-0004-FLOW-SCREEN","SYN-0004-FLOW-INVITE","SYN-0004-FLOW-VALID","SYN-0004-FLOW-RECEIPT"]
rates=["SYN-0004-RATE-RESPONSE","SYN-0004-RATE-EFFECTIVE","SYN-0004-RATE-YIELD","SYN-0004-RATE-ELIGIBLE"]
checks={}
def ck(n,v):checks[n]=bool(v)
sq=json.loads(sourceqa.read_text(encoding="utf-8"))
ck("source_prep_qa_16_of_16",sq["check_count"]==16 and not sq["failures"])
ck("84_unique_register_ids_present",len(facts)==84 and len(set(ids))==84 and all(x in alltext for x in ids))
ck("all_18_count_flow_rate_ids_present",all(x in alltext for x in counts+flows+rates))
ck("no_wildcard_ids",not any(x in alltext for x in ["SYN-0004-COUNT-*","SYN-0004-FLOW-*","SYN-0004-RATE-*"]))
ck("u004_invite_chronology", "2026-10-29" in alltext and "SYN-0004-U004-INVITE-DATE" in alltext and "2026-10-28（SYN-0004-U004-INVITE-DATE）" not in alltext)
norm=re.sub(r"\s+","",alltext)
rate_expected={"SYN-0004-RATE-RESPONSE":("2/4","50.0%"),"SYN-0004-RATE-EFFECTIVE":("1/2","50.0%"),"SYN-0004-RATE-YIELD":("1/4","25.0%"),"SYN-0004-RATE-ELIGIBLE":("4/5","80.0%")}
rate_rows={k:False for k in rate_expected}
for t in d.tables:
 for row in t.rows:
  row_text="".join(c.text for c in row.cells);row_norm=re.sub(r"\s+","",row_text)
  for k,(fraction,pct) in rate_expected.items():
   if k in row_text and fraction in row_norm and pct in row_norm:rate_rows[k]=True
ck("four_required_rates",all(rate_rows.values()))
ck("candidate_synthetic_unknown_boundary",all(x in alltext for x in ["CANDIDATE","SAMPLE/SYNTHETIC","UNKNOWN"]) and ("NOT GRANTED" in alltext or "非正式接受" in alltext))
ck("no_stale_r02_register_hash","0e0748a80d512c9e49abea3c567838239db21510408570d84f0ecfdb7e10d0c9" not in alltext)
ck("no_source_prep_pass_claim","PASS_SOURCE_PREP" not in alltext and "44/44" not in alltext)
ck("no_self_cert_section","合成事實 ID 覆蓋說明" not in alltext and "未新增 register 之外" not in alltext)
ck("no_placeholders",not any(x in alltext.lower() for x in ["todo","tbd","待填","保持空白","會後填寫","空白考卷","空白表"]))
ck("max_five_table_columns",all(len(t.columns)<=5 for t in d.tables))
ck("docx_reopens",len(d.paragraphs)>10 and len(d.tables)>8)
bs=[r.font.size.pt for p in d.paragraphs for r in p.runs if r.text.strip() and r.font.size]
ts=[r.font.size.pt for t in d.tables for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs if r.text.strip() and r.font.size]
ck("body_min_10_5pt",bool(bs) and min(bs)>=10.5);ck("table_min_9_5pt",bool(ts) and min(ts)>=9.5)
ck("A4_page",296<=d.sections[0].page_height.mm<=298 and 209<=d.sections[0].page_width.mm<=211)
qa={"schema":"ttqs-one-docx-deterministic-qa-v1","work_id":"TTQS-0004-I01-E02-DOCX-BUILD-QA-R03-20261116","project_id":"TTQS_ONE","doc_id":"0004","requirement_id":"I01-E02","candidate_status":"CANDIDATE","acceptance":"NOT_GRANTED","semantic_review":"PENDING","visual_review":"PENDING","candidate_docx_path":str(docx),"candidate_docx_sha256":sha(docx),"candidate_docx_bytes":docx.stat().st_size,"source_packet_sha256":sha(work/"SOURCE_PACKET_0004_I01-E02_R02.md"),"unique_blueprint_sha256":sha(work/"UNIQUE_BLUEPRINT_0004_I01-E02_R02.md"),"register_sha256":sha(reg),"source_prep_manifest_sha256":sha(manifest),"source_prep_qa_sha256":sha(sourceqa),"worker_response_sha256":sha(md),"checks":checks,"check_count":len(checks),"failures":[k for k,v in checks.items() if not v],"status":"PASS_SCOPED_DETERMINISTIC" if all(checks.values()) else "FAIL","observed_at_local":datetime.datetime.now().astimezone().isoformat()}
(qa_dir/"DETERMINISTIC_DOCX_QA_R03.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"candidate":str(docx),"sha256":qa["candidate_docx_sha256"],"bytes":qa["candidate_docx_bytes"],"tables":len(d.tables),"checks":qa["check_count"],"failures":qa["failures"],"status":qa["status"]},ensure_ascii=False,indent=2))
if qa["failures"]:sys.exit(3)

