from pathlib import Path
import sys,re,json,hashlib,platform
sys.path.insert(0,r'C:\Users\J\AppData\Local\Temp\ttqs_one_0035_r02_kepler_deps_20261118')
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
BASE=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0048_SOURCE_PACKET_20261118')
BODY=BASE/'scoped_repair_w1_longcat_r02/WORKER_BODY_R02_TYPOFIX.md'
RAW_R02=BASE/'scoped_repair_w1_longcat_r02/WORKER_BODY_R02.md'
CAND=BASE/'candidate/0048_I10-E03_R02_SCOPED_REPAIR_TEXTFIX.docx'
QA=BASE/'candidate/qa/build_r02_codex'; QA.mkdir(parents=True,exist_ok=True)
SOURCE=BASE/'OFFICIAL_REQUIREMENT_EXTRACT.md'; BLUEPRINT=BASE/'UNIQUE_BLUEPRINT_ROW.json'; SOURCE_RECEIPT=BASE/'SOURCE_PACKET_RECEIPT.json'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def runfont(r,size=11,bold=None,italic=None,color=None,font='Aptos'):
 r.font.name=font;r._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei');r.font.size=Pt(size)
 if bold is not None:r.bold=bold
 if italic is not None:r.italic=italic
 if color:r.font.color.rgb=RGBColor(*color)
def inline(p,s,size=11,bold=False,italic=False,color=None):
 pat=re.compile(r'(\*\*.+?\*\*|\*[^*]+?\*|`[^`]+`)');pos=0
 for m in pat.finditer(s):
  if m.start()>pos:runfont(p.add_run(s[pos:m.start()]),size,bold,italic,color)
  t=m.group(); isbold=t.startswith('**'); isitalic=t.startswith('*') and not isbold
  value=t[2:-2] if isbold else t[1:-1]
  runfont(p.add_run(value),size,bold or isbold,italic or isitalic,color,'Consolas' if t.startswith('`') else 'Aptos');pos=m.end()
 if pos<len(s):runfont(p.add_run(s[pos:]),size,bold,italic,color)
def split(line):return [x.strip() for x in line.strip().strip('|').split('|')]
def sep(row):return bool(row) and all(re.fullmatch(r':?-{3,}:?',x.replace(' ','')) for x in row)
def cell_margin(cell):
 tc=cell._tc.get_or_add_tcPr();m=OxmlElement('w:tcMar')
 for edge,val in [('top',55),('start',65),('bottom',55),('end',65)]:
  e=OxmlElement('w:'+edge);e.set(qn('w:w'),str(val));e.set(qn('w:type'),'dxa');m.append(e)
 tc.append(m)
def table_borders(t):
 pr=t._tbl.tblPr;bs=OxmlElement('w:tblBorders')
 for edge in ('top','left','bottom','right','insideH','insideV'):
  e=OxmlElement('w:'+edge);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:space'),'0');e.set(qn('w:color'),'B9C6D4');bs.append(e)
 pr.append(bs)
def weights(n):return {2:[1.3,4],3:[1.15,3,1.4],4:[.65,1.35,1.2,2.2],5:[.6,1.25,1.6,1.6,1.8],6:[.55,1.1,1.8,.72,1.8,1.35]}.get(n,[1]*n)
def add_table(lines):
 rows=[split(x) for x in lines if not sep(split(x))]
 n=max(len(x) for x in rows)
 if any(len(x)!=n for x in rows):raise ValueError('inconsistent markdown table columns')
 t=doc.add_table(rows=len(rows),cols=n);t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
 ws=weights(n);total=10.57;den=sum(ws)
 for c,w in zip(t.columns,ws):c.width=Inches(total*w/den)
 for ri,row in enumerate(rows):
  tr=t.rows[ri]._tr.get_or_add_trPr();tr.append(OxmlElement('w:cantSplit'))
  if ri==0:
   h=OxmlElement('w:tblHeader');h.set(qn('w:val'),'true');tr.append(h)
  for ci,val in enumerate(row):
   cell=t.cell(ri,ci);cell.width=Inches(total*ws[ci]/den);cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP;cell_margin(cell)
   p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.04;inline(p,val,9.5,ri==0,color=(255,255,255) if ri==0 else None)
   if ri==0:sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'254A70');cell._tc.get_or_add_tcPr().append(sh)
   elif ri%2==0:sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'F2F6FA');cell._tc.get_or_add_tcPr().append(sh)
 table_borders(t);p=doc.add_paragraph();p.paragraph_format.space_after=Pt(3);p.paragraph_format.line_spacing=1
def page_field(p):
 r=p.add_run();runfont(r,9,color=(100,100,100))
 for typ,txt in [('begin',None),('instrText',' PAGE '),('end',None)]:
  e=OxmlElement('w:instrText') if typ=='instrText' else OxmlElement('w:fldChar')
  if typ=='instrText':e.set(qn('xml:space'),'preserve');e.text=txt
  else:e.set(qn('w:fldCharType'),typ)
  r._r.append(e)
body=BODY.read_text(encoding='utf-8')
doc=Document();sec=doc.sections[0];sec.orientation=WD_ORIENT.LANDSCAPE;sec.page_width=Inches(11.69);sec.page_height=Inches(8.27);sec.top_margin=Inches(.58);sec.bottom_margin=Inches(.58);sec.left_margin=Inches(.56);sec.right_margin=Inches(.56);sec.header_distance=Inches(.25);sec.footer_distance=Inches(.25)
normal=doc.styles['Normal'];normal.font.name='Aptos';normal.font.size=Pt(11);normal._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei');normal.paragraph_format.space_after=Pt(5);normal.paragraph_format.line_spacing=1.08
for name,size in [('Title',18),('Heading 1',15),('Heading 2',13)]:
 st=doc.styles[name];st.font.name='Aptos';st.font.size=Pt(size);st.font.bold=True;st.font.color.rgb=RGBColor(31,66,110);st._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei');st.paragraph_format.keep_with_next=True;st.paragraph_format.space_before=Pt(8);st.paragraph_format.space_after=Pt(4)
h=sec.header.paragraphs[0];h.alignment=WD_ALIGN_PARAGRAPH.RIGHT;inline(h,'TTQS ONE  |  0048 / I10-E03  |  CANDIDATE · SAMPLE/SYNTHETIC',9,color=(85,100,120))
f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.CENTER;inline(f,'TTQS ONE candidate  •  ',9,color=(100,100,100));page_field(f)
doc.core_properties.title='大型採購會議及師資遴聘後審查佐證紀錄｜SAMPLE/SYNTHETIC';doc.core_properties.subject='TTQS ONE 0048 / I10-E03 candidate';doc.core_properties.author='TTQS ONE candidate builder'
lines=body.splitlines();i=0
while i<len(lines):
 s=lines[i].strip()
 if not s:i+=1;continue
 if s.startswith('|'):
  table=[]
  while i<len(lines) and lines[i].strip().startswith('|'):table.append(lines[i].strip());i+=1
  add_table(table);continue
 if s in ('---','***','___'):i+=1;continue
 hm=re.match(r'^(#{1,3})\s+(.*)$',s)
 if hm:
  level=len(hm.group(1));sty={1:'Title',2:'Heading 1',3:'Heading 2'}[level];p=doc.add_paragraph(style=sty);inline(p,hm.group(2),18 if level==1 else 15 if level==2 else 13,True,color=(31,66,110));i+=1;continue
 if s.startswith('>'):
  p=doc.add_paragraph();p.paragraph_format.left_indent=Inches(.18);p.paragraph_format.space_after=Pt(3);inline(p,s[1:].lstrip(),10,italic=True,color=(70,80,95));i+=1;continue
 bm=re.match(r'^[-*]\s+(.*)$',s);nm=re.match(r'^\d+[.)]\s+(.*)$',s)
 if bm or nm:
  p=doc.add_paragraph(style='List Bullet' if bm else 'List Number');p.paragraph_format.space_after=Pt(2);inline(p,(bm or nm).group(1),11);i+=1;continue
 p=doc.add_paragraph();p.paragraph_format.widow_control=True;inline(p,s,11);i+=1
doc.save(CAND)
script=Path(__file__).resolve();outputs={'docx':{'path':str(CAND.resolve()),'sha256':sha(CAND),'bytes':CAND.stat().st_size},'builder_script':{'path':str(script),'sha256':sha(script),'bytes':script.stat().st_size}}
receipt={'receipt_type':'TTQS_ONE_DOCX_BUILD_RECEIPT','work_id':'0048-I10-E03-BUILD-R02-TEXTFIX','doc_id':'0048','requirement_id':'I10-E03','revision':'R02_TEXTFIX','status':'CANDIDATE_BUILD_COMPLETE_DETERMINISTIC_CHECKS_ONLY','built_at_tpe':__import__('datetime').datetime.now().astimezone().isoformat(),'inputs':{'adopted_worker_body':{'path':str(BODY.resolve()),'sha256':sha(BODY),'bytes':BODY.stat().st_size},'raw_worker_r02':{'path':str(RAW_R02.resolve()),'sha256':sha(RAW_R02),'bytes':RAW_R02.stat().st_size},'official_requirement_extract':{'path':str(SOURCE.resolve()),'sha256':sha(SOURCE),'bytes':SOURCE.stat().st_size},'unique_blueprint_row':{'path':str(BLUEPRINT.resolve()),'sha256':sha(BLUEPRINT),'bytes':BLUEPRINT.stat().st_size},'source_packet_receipt':{'path':str(SOURCE_RECEIPT.resolve()),'sha256':sha(SOURCE_RECEIPT),'bytes':SOURCE_RECEIPT.stat().st_size}},'outputs':outputs,'builder':{'python':platform.python_version(),'python_docx':'1.2.0','orientation':'A4 landscape','body_font_pt':11,'table_font_pt':9.5,'table_headers_repeat':True,'table_rows_cant_split':True,'markdown_blocks_preserved':True},'synthetic_boundary':'SAMPLE/SYNTHETIC; no real association facts asserted','formal_acceptance':'NOT_CLAIMED'}
(QA/'BUILD_RECEIPT_0048_I10-E03_R02_TEXTFIX.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
