from pathlib import Path
from io import BytesIO
from datetime import datetime, timezone
from fractions import Fraction
import hashlib,json,math,os,platform,re,subprocess,sys,zipfile
import xml.etree.ElementTree as ET
DEPS=Path(os.environ.get("TTQS_PYTHON_DOCX_DEPS",r"C:\Users\J\AppData\Local\Temp\ttqs_one_0035_r02_kepler_deps_20261118"))
if DEPS.is_dir(): sys.path.insert(0,str(DEPS))
import docx
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table

REPO=Path(r"E:\tqrepo")
ROOT=REPO/r"docs\ttqs-quality-20261016\quality-review\0035_I07-E03_SOURCE_PREP_R01_20261118"
BODY=ROOT/r"candidate\qa\scoped_repair_r02_worker\0035_I07-E03_R02_SCOPED_REPAIR.md"
PACKET=ROOT/"SOURCE_PACKET_0035_I07-E03_R01.md"
BLUEPRINT=ROOT/"UNIQUE_BLUEPRINT_0035_I07-E03_R01.md"
OUT=ROOT/r"candidate\0035_I07-E03_R02_SCOPED_REPAIR.docx"
RECEIPT=ROOT/r"candidate\qa\build_r02_kepler\BUILD_RECEIPT_0035_I07-E03_R02.json"
SCRIPT=Path(__file__).resolve()
EXPECTED={"body":"A11BE8683D2AF72D65BB3A02A4AC79F3035BCDFCAC6A064AEA66E03F9F50474C",
"packet":"36DCA53E98B77ECF6F9FAC96D2D74ECB817554E924B98F76A1B8C7182BD77891",
"blueprint":"ED05970D955945EAD41CD411D29DE0C55F92FF8737C93B463A4B0142ED3E8D9A"}
HEAD_EXPECTED="03348e7811dfe57a5b6e46efed1598b929db563d"
BRANCH_EXPECTED="work/ttqs-one-document-quality-contract-20261016"
TITLE_EXPECTED="對相關職能分析及運用的方法均能適時檢討隨時改_完整工作稿"
FONT="Microsoft JhengHei"; CODE=chr(96)
def sha(b): return hashlib.sha256(b).hexdigest().upper()
def fsha(p): return sha(Path(p).read_bytes())
def git(*a):
 p=subprocess.run(["git","-c","safe.directory=E:/tqrepo","-C",str(REPO),*a],capture_output=True,text=True,encoding="utf-8",errors="replace")
 return p.returncode,p.stdout.strip(),p.stderr.strip()
rc,head,err=git("rev-parse","HEAD"); rb,branch,berr=git("branch","--show-current"); rg,gitver,gerr=git("--version")
if (rc,rb,head,branch)!=(0,0,HEAD_EXPECTED,BRANCH_EXPECTED): raise RuntimeError(f"checkout mismatch: {head} {branch} {err} {berr}")
for p in (BODY,PACKET,BLUEPRINT):
 if not p.is_file(): raise FileNotFoundError(str(p))
if RECEIPT.exists(): raise FileExistsError(f"refusing to overwrite existing receipt: {RECEIPT}")
if OUT.exists() and fsha(OUT)!="080D1C6FFCC032F7EC3ACE277A2E84E69A3554B9B8E4BB2E73F7E0E048AB2BE4": raise FileExistsError(f"output exists and is not the recorded intermediate: {OUT}")
body_bytes,packet_bytes,blueprint_bytes=[p.read_bytes() for p in (BODY,PACKET,BLUEPRINT)]
body_sha,packet_sha,blueprint_sha=[sha(x) for x in (body_bytes,packet_bytes,blueprint_bytes)]
for n,h in zip(("body","packet","blueprint"),(body_sha,packet_sha,blueprint_sha)):
 if h!=EXPECTED[n]: raise RuntimeError(f"{n} SHA mismatch: {h}")
body,packet_text,blueprint_text=[x.decode("utf-8-sig") for x in (body_bytes,packet_bytes,blueprint_bytes)]
def meta(t,label):
 prefix=f"**{label}:**"
 for line in t.splitlines():
  if line.strip().startswith(prefix): return line.strip()[len(prefix):].strip()
 return None
nonempty=[x.strip() for x in body.splitlines() if x.strip()]
hm=re.fullmatch(r"#{1,6}\s+(.+)",nonempty[0]) if nonempty else None
if not hm: raise RuntimeError("body title heading missing")
body_title=hm.group(1).strip(); front=nonempty[1] if len(nonempty)>1 else ""
if "doc_id: 0035" not in front or "requirement_id: I07-E03" not in front: raise RuntimeError(f"body metadata mismatch: {front}")
md={"packet_doc_id":meta(packet_text,"doc_id"),"packet_requirement_id":meta(packet_text,"requirement_id"),
"packet_crosswalk_title":meta(packet_text,"Crosswalk title (exact row value)"),
"blueprint_doc_id":meta(blueprint_text,"doc_id"),"blueprint_requirement_id":meta(blueprint_text,"requirement_id"),
"blueprint_crosswalk_title":meta(blueprint_text,"Crosswalk title (exact row value)"),
"blueprint_genre":meta(blueprint_text,"Blueprint genre")}
if md["packet_doc_id"]!="0035" or md["blueprint_doc_id"]!="0035" or md["packet_requirement_id"]!="I07-E03" or md["blueprint_requirement_id"]!="I07-E03" or md["packet_crosswalk_title"]!=TITLE_EXPECTED or md["blueprint_crosswalk_title"]!=TITLE_EXPECTED:
 raise RuntimeError(f"packet/Blueprint metadata mismatch: {md}")
INLINE=re.compile(r"(\*\*.*?\*\*|"+CODE+r"[^"+CODE+r"]+"+CODE+r"|\*[^*]+\*)")
def plain(s):
 out=[]
 for t in INLINE.split(s):
  if not t: continue
  if t.startswith("**") and t.endswith("**"): out.append(t[2:-2])
  elif t.startswith(CODE) and t.endswith(CODE): out.append(t[1:-1])
  elif t.startswith("*") and t.endswith("*"): out.append(t[1:-1])
  else: out.append(t)
 return "".join(out).replace("<br>","\n")
def cells(line):
 s=line.strip()
 if s.startswith("|"): s=s[1:]
 if s.endswith("|"): s=s[:-1]
 return [x.strip().replace(r"\|","|") for x in re.split(r"(?<!\\)\|",s)]
def sep(line): return bool(cells(line)) and all(re.fullmatch(r":?-{3,}:?",x.replace(" ","")) for x in cells(line))
def hr(s): return s in ("---","***","___")
def structural(line):
 s=line.strip()
 return (not s or hr(s) or s.startswith("|") or re.match(r"^#{1,6}\s+",s) is not None
 or re.match(r"^>\s+",s) is not None or re.match(r"^[-*+]\s+",s) is not None or re.match(r"^\d+[.)]\s+",s) is not None)
def join_lines(parts):
 if not parts: return ""
 out=parts[0].strip(); prev=parts[0].endswith("  ") or parts[0].rstrip().endswith("\\")
 if parts[0].rstrip().endswith("\\") and out.endswith("\\"): out=out[:-1].rstrip()
 for raw in parts[1:]:
  val=raw.strip(); hard=raw.endswith("  ") or raw.rstrip().endswith("\\")
  if raw.rstrip().endswith("\\") and val.endswith("\\"): val=val[:-1].rstrip()
  out+=("\n" if prev else " ")+val; prev=hard
 return out
def parse(text):
 lines=text.splitlines(); out=[]; i=0
 while i<len(lines):
  raw=lines[i]; s=raw.strip()
  if not s or hr(s): i+=1; continue
  if s.startswith("|"):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith("|"):
    if not sep(lines[i]): rows.append(cells(lines[i]))
    i+=1
   if rows:
    width=max(map(len,rows)); out.append({"kind":"table","rows":[r+[""]*(width-len(r)) for r in rows]})
   continue
  h=re.match(r"^(#{1,6})\s+(.*)$",s)
  if h: out.append({"kind":"heading","level":len(h.group(1)),"text":h.group(2)}); i+=1; continue
  if s.startswith("> "):
   q=[]
   while i<len(lines) and lines[i].strip().startswith("> "): q.append(lines[i].strip()[2:]); i+=1
   out.append({"kind":"quote","text":join_lines(q)}); continue
  b=re.match(r"^([-*+])\s+(.*)$",s); n=re.match(r"^(\d+[.)])\s+(.*)$",s)
  if b or n:
   m=b or n; kind="bullet" if b else "numbered"; parts=[m.group(2)]; marker=m.group(1); i+=1
   while i<len(lines) and lines[i].strip() and not structural(lines[i]):
    if len(lines[i])-len(lines[i].lstrip())<2: break
    parts.append(lines[i].strip()); i+=1
   out.append({"kind":kind,"marker":marker,"text":join_lines(parts)}); continue
  parts=[raw]; i+=1
  while i<len(lines) and lines[i].strip() and not structural(lines[i]): parts.append(lines[i]); i+=1
  out.append({"kind":"paragraph","text":join_lines(parts)})
 return out
blocks=parse(body); paragraph_blocks=[b for b in blocks if b["kind"]!="table"]; tables=[b for b in blocks if b["kind"]=="table"]
if not paragraph_blocks or not tables: raise RuntimeError("empty Markdown parse")
row_counts=[len(t["rows"]) for t in tables]
def registered(section,column):
 idx=next((i for i,b in enumerate(blocks) if b["kind"]=="heading" and b["text"].startswith(section)),None)
 if idx is None: raise RuntimeError(f"missing register section {section}")
 for b in blocks[idx+1:]:
  if b["kind"]=="heading": break
  if b["kind"]!="table": continue
  header=[plain(x).strip().casefold() for x in b["rows"][0]]
  if column.casefold() in header:
   c=header.index(column.casefold())
   return [plain(r[c]).strip() for r in b["rows"][1:] if c<len(r) and plain(r[c]).strip()]
 raise RuntimeError(f"missing register table {section}:{column}")
facts=registered("12.7 FACT","fact_id"); findings=registered("12.8 FINDING ID","finding_id")
fact_occ=re.findall(r"\bSYN-0035-\d{4}\b",body); finding_occ=re.findall(r"\bSYN-0035-F\d{2}\b",body)
fact_ids=sorted(set(fact_occ)); finding_ids=sorted(set(finding_occ))
expected_facts=[f"SYN-0035-{i:04d}" for i in range(1,78)]
expected_findings=[f"SYN-0035-F{i:02d}" for i in range(1,6)]
if fact_ids!=expected_facts or facts!=expected_facts or len(facts)!=77: raise RuntimeError(f"FACT registration mismatch: unique={len(fact_ids)} rows={len(facts)}")
if finding_ids!=expected_findings or findings!=expected_findings or len(findings)!=5: raise RuntimeError(f"FINDING registration mismatch: unique={len(finding_ids)} rows={len(findings)}")
if set(fact_ids)&set(finding_ids) or len(set(facts+findings))!=82: raise RuntimeError("FACT/FINDING IDs not distinct")
def matrix(prefix):
 rows=next((t["rows"] for t in tables if t["rows"] and plain(t["rows"][0][0]).strip().startswith(prefix)),None)
 if rows is None: raise RuntimeError(f"missing matrix {prefix}")
 data={}
 for r in rows[1:]:
  label=plain(r[0]).strip()
  if label in ("達成","未達成","合計"): data[label]=[int(plain(x).strip()) for x in r[1:4]]
 if set(data)!={"達成","未達成","合計"}: raise RuntimeError(f"matrix rows malformed {prefix}: {data}")
 m=[data["達成"][:2],data["未達成"][:2]]; rt=[sum(x) for x in m]; ct=[m[0][i]+m[1][i] for i in range(2)]; n=sum(rt)
 if rt!=[data["達成"][2],data["未達成"][2]] or ct!=data["合計"][:2] or n!=data["合計"][2]: raise RuntimeError(f"matrix totals wrong: {prefix}")
 po=Fraction(m[0][0]+m[1][1],n); pe=sum((Fraction(rt[i]*ct[i],n*n) for i in range(2)),Fraction(0,1)); k=(po-pe)/(1-pe)
 return {"matrix":m,"row_totals":rt,"column_totals":ct,"n":n,"p_o":float(po),"p_e":float(pe),"kappa":float(k),"fraction":f"{k.numerator}/{k.denominator}"}
ka=matrix("版本 A：審查者"); kb=matrix("版本 B：審查者"); delta=kb["kappa"]-ka["kappa"]
if ka["matrix"]!=[[2,3],[3,2]] or ka["n"]!=10 or not math.isclose(ka["kappa"],-.2,abs_tol=1e-12): raise RuntimeError(f"A matrix/kappa mismatch: {ka}")
if kb["matrix"]!=[[4,1],[1,4]] or kb["n"]!=10 or not math.isclose(kb["kappa"],.6,abs_tol=1e-12): raise RuntimeError(f"B matrix/kappa mismatch: {kb}")
if not math.isclose(delta,.8,abs_tol=1e-12) or not all(x in body for x in ("−0.20","0.60","0.80")): raise RuntimeError(f"kappa delta/report mismatch: {delta}")
boundary={x:body.count(x) for x in ("SAMPLE/SYNTHETIC","REAL","UNKNOWN")}
if any(n==0 for n in boundary.values()): raise RuntimeError(f"truth boundary missing: {boundary}")

def setfont(run,size,bold=None,color=None,italic=None):
 run.font.name=FONT; run.font.size=Pt(size); rp=run._element.get_or_add_rPr(); rf=rp.rFonts
 if rf is None: rf=OxmlElement("w:rFonts"); rp.insert(0,rf)
 for x in ("eastAsia","ascii","hAnsi"): rf.set(qn("w:"+x),FONT)
 if bold is not None: run.bold=bold
 if color is not None: run.font.color.rgb=RGBColor(*color)
 if italic is not None: run.italic=italic
def addinline(p,text,size=11,bold=False,color=None):
 for tok in INLINE.split(text):
  if not tok: continue
  ib=tok.startswith("**") and tok.endswith("**"); ic=tok.startswith(CODE) and tok.endswith(CODE); ii=tok.startswith("*") and tok.endswith("*") and not ib
  val=tok[2:-2] if ib else (tok[1:-1] if ic or ii else tok)
  for j,part in enumerate(val.split("<br>")):
   if j: p.add_run().add_break()
   r=p.add_run(part); setfont(r,size,bold=(bold or ib),color=color,italic=ii)
   if ic: r.font.name="Consolas"; r._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"),FONT)
def shade(cell,color):
 tc=cell._tc.get_or_add_tcPr(); shd=tc.find(qn("w:shd"))
 if shd is None: shd=OxmlElement("w:shd"); tc.append(shd)
 shd.set(qn("w:fill"),color)
def cellmargins(cell):
 tc=cell._tc.get_or_add_tcPr(); mar=tc.first_child_found_in("w:tcMar")
 if mar is None: mar=OxmlElement("w:tcMar"); tc.append(mar)
 for k,v in (("top",70),("start",80),("bottom",70),("end",80)):
  node=mar.find(qn("w:"+k))
  if node is None: node=OxmlElement("w:"+k); mar.append(node)
  node.set(qn("w:w"),str(v)); node.set(qn("w:type"),"dxa")
def pagefield(p):
 r=p.add_run(); setfont(r,9)
 for tag,val in (("w:fldChar","begin"),("w:instrText"," PAGE "),("w:fldChar","separate")):
  n=OxmlElement(tag)
  if tag=="w:fldChar": n.set(qn("w:fldCharType"),val)
  else: n.set(qn("xml:space"),"preserve"); n.text=val
  r._r.append(n)
 t=OxmlElement("w:t"); t.text="1"; r._r.append(t)
 e=OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"),"end"); r._r.append(e)

doc=Document(); sec=doc.sections[0]; sec.orientation=WD_ORIENT.LANDSCAPE
sec.page_width=Inches(11.69); sec.page_height=Inches(8.27); sec.top_margin=Inches(.58); sec.bottom_margin=Inches(.58); sec.left_margin=Inches(.52); sec.right_margin=Inches(.52); sec.header_distance=Inches(.26); sec.footer_distance=Inches(.26)
normal=doc.styles["Normal"]; normal.font.name=FONT; normal.font.size=Pt(11); normal._element.rPr.rFonts.set(qn("w:eastAsia"),FONT); normal.paragraph_format.space_after=Pt(5); normal.paragraph_format.line_spacing=1.08
for name,size in (("Title",18),("Heading 1",15),("Heading 2",13),("Heading 3",12)):
 st=doc.styles[name]; st.font.name=FONT; st.font.size=Pt(size); st.font.bold=True; st._element.rPr.rFonts.set(qn("w:eastAsia"),FONT); st.font.color.rgb=RGBColor(31,66,110); st.paragraph_format.keep_with_next=True; st.paragraph_format.space_before=Pt(8); st.paragraph_format.space_after=Pt(4)
h=sec.header.paragraphs[0]; h.alignment=WD_ALIGN_PARAGRAPH.RIGHT; addinline(h,"TTQS ONE  |  0035 / I07-E03  |  CANDIDATE · SAMPLE/SYNTHETIC",9,color=(85,100,120))
f=sec.footer.paragraphs[0]; f.alignment=WD_ALIGN_PARAGRAPH.CENTER; addinline(f,"TTQS ONE candidate  •  ",9,color=(100,100,100)); pagefield(f)
for b in blocks:
 if b["kind"]=="table":
  cols=max(map(len,b["rows"])); t=doc.add_table(rows=0,cols=cols); t.style="Table Grid"; t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=True
  for ri,row in enumerate(b["rows"]):
   dest=t.add_row().cells
   for ci in range(cols):
    c=dest[ci]; c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER; cellmargins(c); p=c.paragraphs[0]; p.paragraph_format.space_after=Pt(0); p.paragraph_format.line_spacing=1.0
    addinline(p,row[ci] if ci<len(row) else "",9.5,bold=(ri==0),color=(255,255,255) if ri==0 else None)
    if ri==0: shade(c,"24476B")
    elif ri%2==0: shade(c,"F2F6FA")
   tr=t.rows[ri]._tr.get_or_add_trPr()
   if ri==0: rep=OxmlElement("w:tblHeader"); rep.set(qn("w:val"),"true"); tr.append(rep)
   tr.append(OxmlElement("w:cantSplit"))
 elif b["kind"]=="heading":
  lev=b["level"]; style="Title" if lev==1 else f"Heading {min(lev-1,3)}"; size=18 if lev==1 else (15 if lev==2 else (13 if lev==3 else 12))
  p=doc.add_paragraph(style=style); addinline(p,b["text"],size,bold=True,color=(31,66,110))
 elif b["kind"]=="bullet":
  p=doc.add_paragraph(style="List Bullet"); p.paragraph_format.space_after=Pt(3); addinline(p,b["text"])
 elif b["kind"]=="numbered":
  p=doc.add_paragraph(style="Normal"); p.paragraph_format.left_indent=Inches(.28); p.paragraph_format.first_line_indent=Inches(-.28); addinline(p,b["marker"]+" "+b["text"])
 elif b["kind"]=="quote":
  p=doc.add_paragraph(style="Normal"); p.paragraph_format.left_indent=Inches(.25); p.paragraph_format.right_indent=Inches(.2); addinline(p,b["text"],color=(70,80,95))
 else:
  p=doc.add_paragraph(style="Normal"); addinline(p,b["text"])
  if len(b["text"])>180: p.paragraph_format.widow_control=True

def expected_seq(bs):
 out=[]
 for b in bs:
  if b["kind"]=="table": out.append({"type":"table","rows":[[plain(x) for x in r] for r in b["rows"]]})
  else:
   v=plain(b["text"])
   if b["kind"]=="numbered": v=b["marker"]+" "+v
   out.append({"type":"paragraph","text":v})
 return out
def actual_seq(d):
 out=[]
 for child in d.element.body.iterchildren():
  if child.tag==qn("w:p"):
   p=Paragraph(child,d)
   if p.text: out.append({"type":"paragraph","text":p.text})
  elif child.tag==qn("w:tbl"):
   t=Table(child,d); out.append({"type":"table","rows":[[c.text for c in r.cells] for r in t.rows]})
 return out
def audit_fonts(blob):
 with zipfile.ZipFile(BytesIO(blob)) as z: root=ET.fromstring(z.read("word/document.xml"))
 bodyel=root.find(qn("w:body")); tablenodes=[x for x in bodyel if x.tag==qn("w:tbl")]; bs=[]; ts=[]; bm=tm=0; rows=[]
 def collect(el):
  sizes=[]; missing=0
  for run in el.iter(qn("w:r")):
   if not "".join(n.text or "" for n in run.iter(qn("w:t"))): continue
   rp=run.find(qn("w:rPr")); sn=rp.find(qn("w:sz")) if rp is not None else None
   if sn is None or not sn.get(qn("w:val")): missing+=1
   else: sizes.append(int(sn.get(qn("w:val")))/2)
  return sizes,missing
 for child in bodyel:
  if child.tag==qn("w:p"):
   a,m=collect(child); bs.extend(a); bm+=m
  elif child.tag==qn("w:tbl"):
   rows.append(len(child.findall(qn("w:tr")))); a,m=collect(child); ts.extend(a); tm+=m
 return {"table_count":len(tablenodes),"table_row_counts":rows,"body_min_pt":min(bs) if bs else None,"table_min_pt":min(ts) if ts else None,
 "body_text_run_count":len(bs),"table_text_run_count":len(ts),"body_text_runs_missing_explicit_size":bm,"table_text_runs_missing_explicit_size":tm}
expected=expected_seq(blocks); buf=BytesIO(); doc.save(buf); data=buf.getvalue()
memdoc=Document(BytesIO(data)); actual=actual_seq(memdoc)
if expected!=actual:
 i=next((i for i,(a,b) in enumerate(zip(expected,actual)) if a!=b),min(len(expected),len(actual)))
 raise RuntimeError(f"source content/order mismatch block {i}; expected={len(expected)} actual={len(actual)}")
fa=audit_fonts(data)
if fa["table_count"]!=len(tables) or fa["table_row_counts"]!=row_counts: raise RuntimeError(f"table/row mismatch {fa}")
if fa["body_text_runs_missing_explicit_size"] or fa["table_text_runs_missing_explicit_size"] or fa["body_min_pt"]<10.5 or fa["table_min_pt"]<9.5: raise RuntimeError(f"font check failed {fa}")
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_bytes(data)
if fsha(OUT)!=sha(data): raise RuntimeError("output SHA changed after write")
saved=Document(str(OUT))
if expected!=actual_seq(saved): raise RuntimeError("saved output reread content mismatch")
def pkgver(n):
 try:
  from importlib.metadata import version
  return version(n)
 except Exception: return "UNKNOWN"
def cmdver(args):
 p=subprocess.run(args,capture_output=True,text=True,encoding="utf-8",errors="replace")
 return {"exit_code":p.returncode,"output":(p.stdout+p.stderr).strip()}
source_paragraphs=len(paragraph_blocks); total_rows=sum(row_counts)
receipt={
 "receipt_type":"TTQS_ONE_DOCX_BUILD_RECEIPT","work_id":"TTQS_ONE_0035_I07-E03_BUILD_R02_20261118","doc_id":"0035","requirement_id":"I07-E03","revision":"R02",
 "status":"CANDIDATE_BUILD_COMPLETE_DETERMINISTIC_CHECKS_ONLY","built_at_utc":datetime.now(timezone.utc).isoformat(),
 "inputs":{"sole_body_source":{"path":str(BODY),"sha256":body_sha,"bytes":len(body_bytes)},"source_packet_metadata_only":{"path":str(PACKET),"sha256":packet_sha,"bytes":len(packet_bytes)},"blueprint_metadata_only":{"path":str(BLUEPRINT),"sha256":blueprint_sha,"bytes":len(blueprint_bytes)}},
 "front_matter_checks":{"body_title":body_title,"body_front_matter":front,**md,"status":"PASS"},
 "checkout":{"repo":str(REPO),"branch":branch,"head":head,"git_version":gitver},
 "builder":{"path":str(SCRIPT),"sha256":fsha(SCRIPT),"executable":"py -3","python_executable":sys.executable,"python_version":sys.version,"python_docx_version":docx.__version__,
 "python_docx_module":str(Path(docx.__file__).resolve()),"lxml_version":pkgver("lxml"),"typing_extensions_version":pkgver("typing_extensions"),
 "pip_version":cmdver([sys.executable,"-m","pip","--version"]),"powershell_version":os.environ.get("TTQS_POWERSHELL_VERSION","NOT_CAPTURED"),
 "platform":platform.platform(),"dependency_scope":"isolated 0035-specific TEMP target; no global/repository package install","dependency_target":str(DEPS)},
 "content":{"content_blocks_preserved_in_source_order":True,"normalized_content_sequence_sha256":sha(json.dumps(expected,ensure_ascii=False,separators=(",",":")).encode("utf-8")),
 "paragraph_count":source_paragraphs,"output_paragraph_count":sum(x["type"]=="paragraph" for x in actual),"table_count":len(tables),"table_row_counts_including_header":row_counts,"total_table_rows_including_header":total_rows,
 "FACT_FINDING_ID_checks":{"FACT_occurrences":len(fact_occ),"FACT_unique":len(fact_ids),"FACT_registered_rows":len(facts),"FINDING_occurrences":len(finding_occ),"FINDING_unique":len(finding_ids),"FINDING_registered_rows":len(findings),"total_distinct_registered":82,"status":"PASS","fact_ids":fact_ids,"finding_ids":finding_ids},
 "boundary_label_occurrences":boundary},
 "calculations":{"corrected_synthetic_kappa_matrices":{"version_A":ka,"version_B":kb,"kappa_delta_B_minus_A":delta,"status":"PASS"}},
 "OOXML_font_checks":{**fa,"body_min_required_pt":10.5,"table_min_required_pt":9.5,"body_status":"PASS","table_status":"PASS","method":"direct w:sz in word/document.xml"},
 "check_outcomes":{"input_hashes":"PASS","title_and_requirement_metadata":"PASS","content_and_table_order":"PASS","77_distinct_FACT_IDs":"PASS","5_distinct_FINDING_IDs":"PASS","kappa_matrices_and_calculations":"PASS","SAMPLE_SYNTHETIC_REAL_UNKNOWN_boundaries":"PASS","OOXML_fonts":"PASS"},
 "outputs":{"docx":{"path":str(OUT),"sha256":fsha(OUT),"bytes":OUT.stat().st_size},"builder_script":{"path":str(SCRIPT),"sha256":fsha(SCRIPT),"bytes":SCRIPT.stat().st_size}},
 "execution":{"process_exit_code":"CAPTURED_BY_POWERSHELL_WRAPPER","stdout":"CAPTURED_BY_POWERSHELL_WRAPPER","stderr":"CAPTURED_BY_POWERSHELL_WRAPPER"},
 "not_performed":{"word_com":"NOT_PERFORMED","render":"NOT_PERFORMED","visual_review":"NOT_PERFORMED","semantic_review":"NOT_PERFORMED","github":"NOT_PERFORMED","promotion":"NOT_PERFORMED","shared_CURRENT_queue":"NOT_MODIFIED","commit":"NOT_PERFORMED","push":"NOT_PERFORMED"},
 "formal_acceptance":"NOT_CLAIMED"}
RECEIPT.parent.mkdir(parents=True,exist_ok=True); RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":receipt["status"],"output":str(OUT),"output_sha256":receipt["outputs"]["docx"]["sha256"],"builder_sha256":receipt["outputs"]["builder_script"]["sha256"],
"body_sha256":body_sha,"paragraphs":source_paragraphs,"tables":len(tables),"rows":total_rows,"facts":len(fact_ids),"findings":len(finding_ids),"kappa_A":ka["kappa"],"kappa_B":kb["kappa"],"delta":delta,
"body_min_pt":fa["body_min_pt"],"table_min_pt":fa["table_min_pt"]},ensure_ascii=False))
