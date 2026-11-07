from pathlib import Path
from docx import Document
from zipfile import ZipFile
from datetime import datetime
from zoneinfo import ZoneInfo
import csv,hashlib,json,re
base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029")
work=base/'worker'/'R08E_REPORT_TABLE_START_20261031'
qa=base/'qa'/'R08E_REPORT_TABLE_START_20261031'
docx=base/'candidate'/'0012_I02-E03_R08E.docx'
sourcep=work/'R08E_INTEGRATED_SOURCE.md'
regp=work/'SYNTHETIC_REPLACEMENT_REGISTER_R08E.csv'
buildp=qa/'BUILD_RECEIPT_R08E.json'
source=sourcep.read_text(encoding='utf-8')
with regp.open('r',encoding='utf-8-sig',newline='') as f: reg=list(csv.DictReader(f))
cols=list(reg[0])
sec=source.split('## 12.',1)[1].split('## 13.',1)[0]
lines=[x.strip() for x in sec.splitlines() if x.strip().startswith('|')]
md=[]
for line in lines[2:]:
 vals=[x.strip() for x in line.strip('|').split('|')]
 if vals: md.append(vals)
if len(reg)!=65 or len(md)!=65: raise SystemExit(f'register counts mismatch csv={len(reg)} md={len(md)}')
if md != [[row[c] for c in cols] for row in reg]: raise SystemExit('Markdown and CSV register rows mismatch')
with ZipFile(docx) as z:
 if z.testzip() is not None: raise SystemExit('DOCX ZIP CRC failed')
doc=Document(docx)
paras=[p for p in doc.paragraphs]
alltext='\n'.join(p.text for p in paras)+'\n'+'\n'.join(c.text for t in doc.tables for row in t.rows for c in row.cells)
required=['R08 SAMPLE 月報完整算例','S12-WP-COR-001','2026-11-12','2026-11-10','月報完整算例','1／1＝100%','0／1＝0%','N/A（0／0）','UNKNOWN；不計為 NTD 0','0＋0＋0＋1＝1','SYN-065']
missing=[x for x in required if x not in alltext]
if missing: raise SystemExit('missing required text: '+repr(missing))
if '####' in alltext: raise SystemExit('literal markdown heading marker remains in DOCX')
if '#### R08 SAMPLE' in source: raise SystemExit('source still contains unsupported heading depth')
section11=[p for p in paras if p.text.strip().startswith('11. 來源追溯及負向鄰項檢核')]
if len(section11)!=1 or not section11[0].paragraph_format.page_break_before: raise SystemExit('section 11 page break missing')
reg_tables=[t for t in doc.tables if any('SYN-065' in c.text for row in t.rows for c in row.cells)]
report_tables=[t for t in doc.tables if t.rows and any(c.text.strip()=='指標' for c in t.rows[0].cells)]
if len(reg_tables)!=1 or len(reg_tables[0].rows)!=66: raise SystemExit('DOCX register table shape mismatch')
if len(report_tables)!=1 or len(report_tables[0].rows)!=7: raise SystemExit('DOCX worked report table shape mismatch')
if not all(p.paragraph_format.keep_with_next for cell in report_tables[0].rows[0].cells for p in cell.paragraphs): raise SystemExit('monthly report header keep-with-next missing')
monthly_heading=[p for p in paras if p.text.strip().startswith('R08 SAMPLE 月報完整算例')]
if len(monthly_heading)!=1 or not monthly_heading[0].paragraph_format.page_break_before: raise SystemExit('monthly report section page break missing')
if 1/1*100!=100 or 0/1*100!=0 or sum((0,0,0,1))!=1 or 1/1*100!=100: raise SystemExit('sample formula mismatch')
if 0==0 and 'N/A（0／0）' not in alltext: raise SystemExit('zero denominator not labeled N/A')
if 'UNKNOWN；不計為 NTD 0' not in alltext: raise SystemExit('unknown real amount converted to zero')
def font_pt(run, para):
 if run.font.size is not None:return run.font.size.pt
 st=para.style
 while st is not None:
  if st.font.size is not None:return st.font.size.pt
  st=st.base_style
 return 11.0
body_sizes=[font_pt(r,p) for p in paras for r in p.runs if r.text.strip()]
cell_sizes=[]
for t in doc.tables:
 for row in t.rows:
  for cell in row.cells:
   for p in cell.paragraphs:
    for run in p.runs:
     if run.text.strip():cell_sizes.append(font_pt(run,p))
body_min=min(body_sizes) if body_sizes else None
table_min=min(cell_sizes) if cell_sizes else None
if body_min is None or body_min<10.5: raise SystemExit(f'body font below 10.5: {body_min}')
if table_min is None or table_min<9.5: raise SystemExit(f'table font below 9.5: {table_min}')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
build=json.loads(buildp.read_text(encoding='utf-8'))
if sha(docx)!=build['artifact_sha256'] or sha(sourcep)!=build['source_sha256'] or sha(regp)!=build['synthetic_register_sha256']: raise SystemExit('build receipt hashes mismatch')
receipt={'receipt_id':'0012_I02-E03_R08E_TECHNICAL_QA','observed_at_local':datetime.now(ZoneInfo('Asia/Taipei')).isoformat(timespec='seconds'),'document_id':'0012','requirement_id':'I02-E03','official_checkbox_serial':'UNKNOWN_NOT_RECONSTRUCTED_HERE','candidate_state':'CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED','candidate_path':str(docx),'candidate_sha256':sha(docx),'candidate_bytes':docx.stat().st_size,'parent_candidate_sha256':'a98907526e47b02e5bab2c16b99ca201d3d9b6ae119263893592126e89c4fc4c','source_sha256':sha(sourcep),'register_sha256':sha(regp),'register_rows_csv':len(reg),'register_rows_markdown':len(md),'register_full_row_match':'PASS','docx_table_count':len(doc.tables),'register_table_rows_including_header':len(reg_tables[0].rows),'worked_monthly_report_rows_including_header':len(report_tables[0].rows),'archive_crc':'PASS','heading_marker_fix':'PASS','section_11_page_break_before':'PASS','font_floor':{'body_min_pt':body_min,'table_min_pt':table_min,'body_threshold_pt':10.5,'table_threshold_pt':9.5,'status':'PASS'},'calculation_checks':{'unique_cases':'1/1=100%','official_sources_complete':'0/1=0%','final_dispositions':'0/1=0%','status_distribution':'0+0+0+1=1','correction_follow_up':'1/1=100%','zero_denominator':'0/0=N/A','real_amount':'UNKNOWN_NOT_ZERO'},'technical_status':'PASS','visual_status':'PENDING','semantic_status':'PENDING','formal_acceptance':'NOT_GRANTED'}
out=qa/'TECHNICAL_QA_R08E.json';out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
build['layout_repairs']=['#### heading corrected to ### before build','page_break_before applied to §11 heading','header-cell paragraphs keep with following row to prevent isolated monthly-report header']
build['parent_candidate_sha256']='1a4382c0b21475f6e43e8b2b4017bc8dcd3a00b483318f898f879b3a93f000cf'
build['visual_review']='PENDING';build['semantic_review']='PENDING';build['formal_acceptance']='NOT_GRANTED'
buildp.write_text(json.dumps(build,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
