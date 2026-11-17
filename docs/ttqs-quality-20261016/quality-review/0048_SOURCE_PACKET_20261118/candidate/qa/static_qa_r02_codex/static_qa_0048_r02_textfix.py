from pathlib import Path
import sys,json,hashlib,re,zipfile
from xml.etree import ElementTree as ET
sys.path.insert(0,r'C:\Users\J\AppData\Local\Temp\ttqs_one_0035_r02_kepler_deps_20261118')
from docx import Document
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0048_SOURCE_PACKET_20261118')
cand=base/'candidate/0048_I10-E03_R02_SCOPED_REPAIR_TEXTFIX.docx';bodyp=base/'scoped_repair_w1_longcat_r02/WORKER_BODY_R02_TYPOFIX.md';src=base/'OFFICIAL_REQUIREMENT_EXTRACT.md';bp=base/'UNIQUE_BLUEPRINT_ROW.json';br=base/'candidate/qa/build_r02_codex/BUILD_RECEIPT_0048_I10-E03_R02_TEXTFIX.json'
out=base/'candidate/qa/static_qa_r02_codex/STATIC_QA_RECEIPT_0048_R02_TEXTFIX.json';out.parent.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def status(ok):return 'PASS' if ok else 'FAIL'
doc=Document(cand);full='\n'.join([p.text for p in doc.paragraphs]+[c.text for t in doc.tables for row in t.rows for c in row.cells]);source=src.read_text(encoding='utf-8');body=bodyp.read_text(encoding='utf-8')
ids=set(re.findall(r'\bSYN-[A-Z0-9]+(?:-[A-Z0-9]+)*\b',full))
reg_table=next((t for t in doc.tables if t.rows and '記錄鍵' in t.rows[0].cells[0].text),None)
registered=set(c.text.strip() for row in reg_table.rows[1:] for c in row.cells[:1]) if reg_table else set()
blank=[];rows=0
for ti,t in enumerate(doc.tables,1):
 for ri,row in enumerate(t.rows,1):
  rows+=1
  for ci,c in enumerate(row.cells,1):
   if not c.text.strip():blank.append([ti,ri,ci])
placeholder=re.findall(r'待填|待核|待補|TODO|TBD|\[\s*\]|_{3,}|＿{2,}',full,re.I)
checks={}
checks['candidate_sha_binding']=sha(cand)==json.loads(br.read_text(encoding='utf-8-sig'))['outputs']['docx']['sha256']
checks['official_requirement_exact']=('大型採購均辦理會議通過、師資遴聘後亦經過會議或審查通過並留有紀錄' in full and '大型採購均辦理會議通過、師資遴聘後亦經過會議或審查通過並留有紀錄' in source)
checks['doc_requirement_identity']='0048' in full and 'I10-E03' in full
checks['two_examples_complete_8of8']=full.count('8 ÷ 8 × 100% = 100.0%')==2 and all(k in full for k in ['SYN-ATT-001（第 1 頁）','SYN-ATT-002（第 1 頁）','委員意見欄','分母 8'])
checks['synthetic_ids_all_registered']=bool(reg_table) and ids.issubset(registered)
checks['all_table_cells_populated']=not blank
checks['placeholder_scan_clear']=not placeholder
checks['typo_repaired']='已附中附件位置' not in full and '已附上附件位置' in full
checks['required_floor_fonts']=all((r.font.size is None or r.font.size.pt>=9.5) for p in doc.paragraphs for r in p.runs) and all((r.font.size is None or r.font.size.pt>=9.5) for t in doc.tables for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs)
checks['bounded_scope']='0048' in full and not any(x in full for x in ['0033 內容','0034 內容','0036 內容'])
checks['sample_real_boundary']='SAMPLE／SYNTHETIC' in full and 'UNKNOWN' in full and '不得' in full
with zipfile.ZipFile(cand) as z: zipbad=z.testzip();ET.fromstring(z.read('word/document.xml'))
checks['ooxml_valid']=zipbad is None
report={'work_id':'0048-I10-E03-STATIC-QA-R02-TEXTFIX','candidate_sha256':sha(cand),'candidate_bytes':cand.stat().st_size,'overall_static_gate':status(all(checks.values())),'checks':{k:status(v) for k,v in checks.items()},'evidence':{'tables':len(doc.tables),'table_rows_including_headers':rows,'registered_id_count':len(registered),'body_id_count':len(ids),'unregistered_ids':sorted(ids-registered),'blank_cells':blank,'placeholder_hits':placeholder,'paragraph_count':len(doc.paragraphs),'body_sha256':sha(bodyp),'source_sha256':sha(src),'blueprint_row_sha256':sha(bp),'zip_bad_member':zipbad},'formal_acceptance':'NOT_CLAIMED'}
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(report,ensure_ascii=False))
