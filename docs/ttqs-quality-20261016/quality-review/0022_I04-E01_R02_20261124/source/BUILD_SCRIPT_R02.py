from pathlib import Path
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import csv, hashlib, json, re, zipfile

SRC=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\PARALLEL_NEXT_READY_SOURCE_PREP_20261116\0022_I04-E01')
OUT=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0022_I04-E01_R02_LAYOUT_REBUILD_20261124')
CAND=OUT/'candidate'/'0022_I04-E01_R02.docx'
if not OUT.is_dir() or CAND.exists(): raise SystemExit('CANDIDATE_ALREADY_EXISTS')
for sub in ['candidate','source','supporting','qa']:(OUT/sub).mkdir(parents=True,exist_ok=True)
body_src=SRC/'writer_R01'/'REPORT_BODY_0022_I04-E01_R01.md'
register_src=SRC/'writer_R01'/'SYNTHETIC_REPLACEMENT_REGISTER_0022_I04-E01_R01.csv'
calc_src=SRC/'writer_R01'/'CROSS_CALCULATION_0022_I04-E01_R01.csv'
body_original=body_src.read_text(encoding='utf-8-sig'); body=body_original
replacements=[('待核定（非 REAL 狀態）','尚未核准（CANDIDATE，非 REAL 狀態）'),('未核定前不得對外公告','核准前不得對外公告')]
for old,new in replacements:
 count=body.count(old)
 if count!=1: raise SystemExit(f'SCOPED_REPAIR_COUNT_{count}: {old}')
 body=body.replace(old,new,1)
body_out=OUT/'source'/'REPORT_BODY_0022_I04-E01_R02_SCOPED_TERMS.md'; body_out.write_text(body,encoding='utf-8',newline='\n')
shutil=None
import shutil
shutil.copy2(register_src,OUT/'supporting'/register_src.name); shutil.copy2(calc_src,OUT/'supporting'/calc_src.name)
for name in ['SOURCE_PACKET_0022_I04-E01_R01.md','UNIQUE_BLUEPRINT_0022_I04-E01_R01.md','SOURCE_PREP_RECEIPT_R01.json']: shutil.copy2(SRC/name,OUT/'source'/name)
shutil.copy2(SRC/'writer_R01'/'WRITER_RECEIPT_R01.json',OUT/'source'/'WRITER_RECEIPT_R01.json')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def md_cells(line):
 x=line.strip()
 if x.startswith('|'): x=x[1:]
 if x.endswith('|'): x=x[:-1]
 parts=[]; buf=''; escaped=False; code=False
 for ch in x:
  if ch=='`': code=not code
  if ch=='|' and not escaped and not code: parts.append(buf.strip()); buf=''; continue
  if ch=='\\' and not escaped: escaped=True; buf+=ch; continue
  escaped=False; buf+=ch
 parts.append(buf.strip()); return [p.replace('\\|','|') for p in parts]
def is_sep(line): return bool(re.fullmatch(r'\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*',line))
def table_cols(line): return len(md_cells(line))
def set_cell_shading(cell,fill):
 tcPr=cell._tc.get_or_add_tcPr(); shd=tcPr.find(qn('w:shd'))
 if shd is None: shd=OxmlElement('w:shd'); tcPr.append(shd)
 shd.set(qn('w:fill'),fill)
def set_cell_margins(cell,top=70,start=85,bottom=70,end=85):
 tcPr=cell._tc.get_or_add_tcPr(); mar=tcPr.first_child_found_in('w:tcMar')
 if mar is None: mar=OxmlElement('w:tcMar'); tcPr.append(mar)
 for side,val in [('top',top),('start',start),('bottom',bottom),('end',end)]:
  node=mar.find(qn('w:'+side))
  if node is None: node=OxmlElement('w:'+side); mar.append(node)
  node.set(qn('w:w'),str(val)); node.set(qn('w:type'),'dxa')
def apply_inline(p,text,table=False):
 pattern=re.compile(r'(\*\*.+?\*\*|`[^`]+`|(?<!\*)\*[^*]+\*(?!\*))'); pos=0
 for m in pattern.finditer(text):
  if m.start()>pos: p.add_run(text[pos:m.start()])
  token=m.group(0); val=token[2:-2] if token.startswith('**') else token[1:-1]
  r=p.add_run(val)
  if token.startswith('**'): r.bold=True
  elif token.startswith('`'): r.font.name='Consolas'; r.font.size=Pt(9.5 if table else 10.5)
  elif token.startswith('*'): r.italic=True
  pos=m.end()
 if pos<len(text): p.add_run(text[pos:])
 for r in p.runs:
  if r.font.name is None:r.font.name='Microsoft JhengHei'
  r._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')
  if table and r.font.size is None:r.font.size=Pt(9.5)
def set_section(sec,landscape):
 sec.orientation=WD_ORIENT.LANDSCAPE if landscape else WD_ORIENT.PORTRAIT
 sec.page_width=Cm(29.7 if landscape else 21.0); sec.page_height=Cm(21.0 if landscape else 29.7)
 sec.top_margin=Cm(1.65); sec.bottom_margin=Cm(1.65); sec.left_margin=Cm(1.7); sec.right_margin=Cm(1.7)
 sec.header_distance=Cm(0.75); sec.footer_distance=Cm(0.75)
def next_section(doc,landscape):
 sec=doc.add_section(WD_SECTION.NEW_PAGE); set_section(sec,landscape); return sec
def add_table(doc,rows,landscape):
 if not rows:return
 n=max(len(r) for r in rows); rows=[r+['']*(n-len(r)) for r in rows]
 table=doc.add_table(rows=1,cols=n); table.alignment=WD_TABLE_ALIGNMENT.CENTER; table.style='Table Grid'; table.autofit=False
 hdr=table.rows[0]; trPr=hdr._tr.get_or_add_trPr(); repeat=OxmlElement('w:tblHeader'); repeat.set(qn('w:val'),'true'); trPr.append(repeat)
 for idx,row in enumerate(rows):
  cells=hdr.cells if idx==0 else table.add_row().cells
  for j,val in enumerate(row):
   cell=cells[j]; cell.text=''; cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER; set_cell_margins(cell)
   p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(0); p.paragraph_format.space_before=Pt(0); p.paragraph_format.line_spacing=1.0
   apply_inline(p,str(val),table=True)
   for r in p.runs:
    r.font.size=Pt(9.5)
    if idx==0:r.bold=True; r.font.color.rgb=RGBColor(255,255,255)
   if idx==0:set_cell_shading(cell,'1F4E78')
   elif idx%2==0:set_cell_shading(cell,'F2F6FA')
 # Data rows deliberately remain splittable; no w:cantSplit property is emitted.
 width=Cm(26.3 if landscape else 17.4)
 weights=[]
 for j in range(n): weights.append(min(54,max(5,max((len(str(r[j])) for r in rows),default=5)))**0.72+1.5)
 total=sum(weights)
 for row in table.rows:
  for j,cell in enumerate(row.cells): cell.width=width*(weights[j]/total)
 return table
def page_field(p):
 p.alignment=WD_ALIGN_PARAGRAPH.CENTER
 r=p.add_run('CANDIDATE｜SAMPLE/SYNTHETIC｜0022 / I04-E01　•　第 '); r.font.name='Microsoft JhengHei'; r.font.size=Pt(8); r.font.color.rgb=RGBColor(95,105,115); r._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')
 f=OxmlElement('w:fldSimple'); f.set(qn('w:instr'),'PAGE'); p._p.append(f)
 r=p.add_run(' 頁'); r.font.name='Microsoft JhengHei'; r.font.size=Pt(8); r.font.color.rgb=RGBColor(95,105,115)
def decorate(doc):
 for sec in doc.sections:
  sec.header.is_linked_to_previous=False; sec.footer.is_linked_to_previous=False
  h=sec.header.paragraphs[0]; h.clear(); h.alignment=WD_ALIGN_PARAGRAPH.RIGHT
  r=h.add_run('TTQS ONE　｜　候選文件　｜　I04-E01 / 0022'); r.font.name='Microsoft JhengHei'; r.font.size=Pt(8); r.font.color.rgb=RGBColor(70,90,110); r._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')
  f=sec.footer.paragraphs[0]; f.clear(); page_field(f)

doc=Document(); set_section(doc.sections[0],False)
normal=doc.styles['Normal']; normal.font.name='Microsoft JhengHei'; normal._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei'); normal.font.size=Pt(11); normal.paragraph_format.space_after=Pt(5); normal.paragraph_format.line_spacing=1.12
for name,size,color in [('Title',20,'17365D'),('Heading 1',16,'1F4E78'),('Heading 2',13,'2F5597'),('Heading 3',11.5,'4472C4')]:
 st=doc.styles[name]; st.font.name='Microsoft JhengHei'; st._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei'); st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=RGBColor.from_string(color); st.paragraph_format.keep_with_next=True; st.paragraph_format.space_before=Pt(10); st.paragraph_format.space_after=Pt(4)
current_landscape=False; lines=body.splitlines(); i=0
while i<len(lines):
 line=lines[i]; stripped=line.strip()
 if not stripped:i+=1;continue
 if stripped.startswith('|'):
  raw=[]
  while i<len(lines) and lines[i].strip().startswith('|'):raw.append(lines[i]);i+=1
  rows=[md_cells(x) for x in raw if not is_sep(x)]
  if not rows:continue
  wide=len(rows[0])>=6
  if wide!=current_landscape:next_section(doc,wide);current_landscape=wide
  add_table(doc,rows,wide)
  continue
 if stripped.startswith('#'):
  level=len(stripped)-len(stripped.lstrip('#')); text=stripped[level:].strip(); j=i+1
  while j<len(lines) and not lines[j].strip():j+=1
  if j<len(lines) and lines[j].strip().startswith('|'):
   desired=table_cols(lines[j])>=6
   if desired!=current_landscape:next_section(doc,desired);current_landscape=desired
  p=doc.add_paragraph(style='Title' if level==1 else f'Heading {min(level-1,3)}');apply_inline(p,text);i+=1;continue
 if re.fullmatch(r'[-*_]{3,}',stripped):i+=1;continue
 bm=re.match(r'^(\s*)([-+*])\s+(.*)$',line); nm=re.match(r'^(\s*)(\d+)[.)]\s+(.*)$',line)
 if bm or nm:
  m=bm or nm;p=doc.add_paragraph(style='List Bullet' if bm else 'List Number');p.paragraph_format.left_indent=Cm(0.6+0.35*(len(m.group(1))//2));p.paragraph_format.first_line_indent=Cm(-0.25);apply_inline(p,m.group(3));i+=1;continue
 p=doc.add_paragraph();apply_inline(p,stripped);i+=1

if not current_landscape:next_section(doc,True);current_landscape=True
p=doc.add_paragraph(style='Heading 1');p.add_run('附錄 A｜SAMPLE/SYNTHETIC 事實替換清冊（完整 112 筆）')
p=doc.add_paragraph('本附錄逐筆列示合成事實、正文位置、計算依據、REAL 替換原件、責任角色與狀態。此表不代表真實機構紀錄。')
with (OUT/'supporting'/register_src.name).open(encoding='utf-8-sig',newline='') as f:reg=list(csv.DictReader(f))
reg_rows=[['事實 ID','事實欄位與合成值','正文位置／公式或依據','REAL 替換證據／責任／狀態']]
for x in reg:reg_rows.append([x['fact_id'],f"{x['field']}\n{x['value']} {x['unit']}",f"{x['report_location']}\n依據：{x['formula_or_basis']}",f"替換原件：{x['real_replacement_evidence']}\n責任：{x['owner_role']}\n狀態：{x['status']}"])
add_table(doc,reg_rows,True)
p=doc.add_paragraph(style='Heading 1');p.add_run('附錄 B｜公式、輸入事實與重算結果（完整 39 筆）')
p=doc.add_paragraph('以下保留計算 ID、公式、輸入事實 ID、計算步驟、結果及確定性檢核；均為 SAMPLE/SYNTHETIC 演練，不表示真實績效。')
with (OUT/'supporting'/calc_src.name).open(encoding='utf-8-sig',newline='') as f:calcs=list(csv.DictReader(f))
calc_rows=[['計算 ID','指標／單位','公式／輸入事實','逐步計算／結果','重算驗證']]
for x in calcs:calc_rows.append([x['calc_id'],f"{x['metric']}\n單位：{x['unit']}",f"公式：{x['formula']}\n輸入：{x['input_fact_ids']}",f"步驟：{x['worked_steps']}\n結果：{x['result']}（{x['rounding']}）",x['validation']])
add_table(doc,calc_rows,True)
for sec in doc.sections:set_section(sec,sec.orientation==WD_ORIENT.LANDSCAPE)
decorate(doc)
doc.core_properties.title='訓練需求的定期調查與分析｜分析報告（SAMPLE/SYNTHETIC）';doc.core_properties.subject='TTQS I04-E01 / 0022 候選分析報告';doc.core_properties.author='TTQS ONE Candidate Production';doc.core_properties.keywords='TTQS; I04-E01; 0022; CANDIDATE; SAMPLE; SYNTHETIC';doc.core_properties.comments='候選文件；未經正式接受；所有合成資料須以真實原件替換。'
doc.save(CAND)
with zipfile.ZipFile(CAND) as z:
 bad=z.testzip(); import xml.etree.ElementTree as ET
 for n in z.namelist():
  if n.endswith('.xml') or n.endswith('.rels'):ET.fromstring(z.read(n))
reopened=Document(CAND); extracted='\n'.join([p.text for p in reopened.paragraphs]+[c.text for t in reopened.tables for row in t.rows for c in row.cells])
reg_ids={x['fact_id'] for x in reg};refs=set(re.findall(r'SF-\d{3}',body));missing=sorted(refs-reg_ids)
forbidden={term:extracted.count(term) for term in ['待填','待核','保持空白','會後填寫','\\begin{','\\[']}
body_sizes=[r.font.size.pt if r.font.size else 11 for p in reopened.paragraphs for r in p.runs if r.text.strip()]
table_sizes=[r.font.size.pt if r.font.size else 9.5 for t in reopened.tables for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs if r.text.strip()]
checks={'docx_opens':True,'zip_crc_pass':bad is None,'all_xml_parts_parse':True,'source_body_scoped_repair_only':body!=body_original,'all_body_fact_refs_resolve':not missing,'register_rows_112':len(reg)==112,'calculation_rows_39':len(calcs)==39,'candidate_marked_sample_synthetic':('SAMPLE/SYNTHETIC' in extracted and 'CANDIDATE' in extracted),'no_latex_math_markup':not bool(re.search(r'\\begin\{|\\\[|\\\(',extracted)),'no_blank_placeholders':all(v==0 for v in forbidden.values()),'body_font_floor_10_5':min(body_sizes or [11])>=10.5,'table_font_floor_9_5':min(table_sizes or [9.5])>=9.5,'table_data_rows_splittable':True,'supporting_register_copied':(OUT/'supporting'/register_src.name).is_file(),'cross_calculation_support_copied':(OUT/'supporting'/calc_src.name).is_file()}
receipt={'schema':'TTQS_ONE_DOCX_BUILD_RECEIPT_R02_V1','project_id':'TTQS_ONE','doc_id':'0022','requirement_id':'I04-E01','revision':'R02','work_id':'TTQS_ONE_0022_I04-E01_DOCX_BUILD_R02_20261124','candidate_status':'CANDIDATE_NOT_CURRENT_NOT_FORMALLY_ACCEPTED','built_at_local':'2026-11-24','candidate_path':'candidate/0022_I04-E01_R02.docx','candidate_sha256':sha(CAND),'candidate_bytes':CAND.stat().st_size,'builder':'python-docx 1.2.0; converted completed W1 body; full synthetic register and 39 calculations appended','builder_script_sha256':sha(Path(__file__)),'inputs':{'writer_body_original_sha256':sha(body_src),'writer_body_scoped_repair_sha256':sha(body_out),'source_packet_sha256':sha(OUT/'source'/'SOURCE_PACKET_0022_I04-E01_R01.md'),'unique_blueprint_sha256':sha(OUT/'source'/'UNIQUE_BLUEPRINT_0022_I04-E01_R01.md'),'writer_receipt_sha256':sha(OUT/'source'/'WRITER_RECEIPT_R01.json'),'replacement_register_sha256':sha(OUT/'supporting'/register_src.name),'cross_calculation_sha256':sha(OUT/'supporting'/calc_src.name)},'scoped_replacements':[{'before':x,'after':y} for x,y in replacements],'fact_references':{'body_refs':len(refs),'register_ids':len(reg_ids),'unresolved':missing},'register_rows':len(reg),'cross_calculation_rows':len(calcs),'tables_in_word':len(reopened.tables),'sections':len(reopened.sections),'table_row_policy':'data rows remain splittable; no cantSplit property emitted','preflight_checks':checks,'preflight_failures':[k for k,v in checks.items() if v is not True],'visual_status':'NOT_RUN','semantic_status':'NOT_RUN','github_readback':'NOT_RUN','formal_acceptance':'NOT_ASSERTED'}
(OUT/'qa'/'BUILD_RECEIPT_R02.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('CANDIDATE',CAND);print('DOCX_SHA256',receipt['candidate_sha256']);print('DOCX_BYTES',receipt['candidate_bytes']);print('TABLES',len(reopened.tables),'SECTIONS',len(reopened.sections),'REGISTER',len(reg),'CALCS',len(calcs));print('CHECKS',json.dumps(checks,ensure_ascii=False));print('FAILURES',json.dumps(receipt['preflight_failures'],ensure_ascii=False))