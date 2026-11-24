import csv,hashlib,json,os,zipfile
from datetime import datetime
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
ROOT=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0092_R01_OPENCODE_WRITER_R01\0092_R05_SCOPED_REPAIR_F031_F033_20261125')
docpath=ROOT/'candidate'/'0092_R05_SYNTHETIC_CANDIDATE.docx'
regpath=ROOT/'sources'/'0092_R05_SYNTHETIC_REPLACEMENT_REGISTER.csv'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks={}; findings=[]
checks['candidate_exists']=docpath.is_file()
checks['register_exists']=regpath.is_file()
with zipfile.ZipFile(docpath) as z: checks['zip_integrity']=z.testzip() is None
D=Document(str(docpath)); checks['python_docx_opens']=True
text='\n'.join([p.text for p in D.paragraphs]+[c.text for t in D.tables for row in t.rows for c in row.cells])
checks['no_repaired_blank_heading']='9.3 調閱紀錄表（空白工作表）' not in text
checks['no_known_access_placeholders']=not any(s in text for s in ['（實際調閱後填）','（依既有索引）','（具體目的）','（實際人員及依據）'])
checks['fact_total_33_consistent']=('全部 33 筆合成事實' in text and '33 個合成事實' in text and '33 筆均為合成且未替換' in text)
checks['no_replacement_character']='\ufffd' not in text
headers=['調閱日期時間','文件索引／版本','調閱目的','調閱人／授權依據','遮蔽範圍','歸還／銷毀處理']
access=next((t for t in D.tables if len(t.rows)>=2 and [c.text.strip() for c in t.rows[0].cells]==headers),None)
checks['six_column_access_log_found']=access is not None
checks['access_sample_row_complete']=bool(access and all(c.text.strip() for c in access.rows[1].cells) and all(('SYNTHETIC' in c.text or 'SAMPLE' in c.text) for c in access.rows[1].cells))
def cant_split(row):
 trpr=row._tr.trPr
 return bool(trpr is not None and trpr.find(qn('w:cantSplit')) is not None)
checks['access_data_row_can_split']=bool(access and not cant_split(access.rows[1]))
ledger=next((t for t in D.tables if len(t.rows)==34 and len(t.columns)==4 and '事實 ID' in t.rows[0].cells[0].text),None)
checks['internal_fact_ledger_33_rows']=bool(ledger and len(ledger.rows)==34)
new_ids=['0092-F028-E4','0092-F029-E4','0092-F030-E4','0092-F031-E4','0092-F032-E4','0092-F033-E4']
checks['internal_new_fact_ids']=bool(ledger and all(any(fid in c.text for row in ledger.rows for c in row.cells) for fid in new_ids))
with regpath.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.reader(f))
ids=[r[0].split(' ',1)[0] for r in rows[1:] if r]
checks['external_register_33_unique_facts']=len(rows)==34 and len(set(ids))==33
checks['external_new_fact_ids']=all(fid in ids for fid in new_ids)
f031_codes=['SYNTHETIC-ROLE-REC-01','SYNTHETIC-AUTH-REF-01']
internal_f031=next((row for row in ledger.rows if any('0092-F031-E4' in c.text for c in row.cells)),None) if ledger else None
external_f031=next((row for row in rows[1:] if row and row[0].startswith('0092-F031-E4')),None)
checks['f031_codes_in_docx_ledger']=bool(internal_f031 and all(code in ' '.join(c.text for c in internal_f031.cells) for code in f031_codes))
checks['f031_codes_in_external_register']=bool(external_f031 and all(code in ' '.join(external_f031) for code in f031_codes))
outcome='示範文件副本已歸還檔案保管位置'
internal_f033=next((row for row in ledger.rows if any('0092-F033-E4' in c.text for c in row.cells)),None) if ledger else None
external_f033=next((row for row in rows[1:] if row and row[0].startswith('0092-F033-E4')),None)
main_f033=any(outcome in c.text for t in D.tables for row in t.rows for c in row.cells)
checks['f033_single_sample_outcome_in_main_log']=main_f033
checks['f033_outcome_in_internal_register']=bool(internal_f033 and outcome in ' '.join(c.text for c in internal_f033.cells))
checks['f033_outcome_in_external_register']=bool(external_f033 and outcome in ' '.join(external_f033))
checks['f033_marked_synthetic']=bool(internal_f033 and any(tag in ' '.join(c.text for c in internal_f033.cells) for tag in ('SYNTHETIC','SAMPLE')) and external_f033 and any(tag in ' '.join(external_f033) for tag in ('SYNTHETIC','SAMPLE')))
checks['revision_r05_logged']=any(row.cells and row.cells[0].text.strip()=='R05' for t in D.tables for row in t.rows)
body_sizes=[]; table_sizes=[]
for p in D.paragraphs:
 for r in p.runs:
  if r.text.strip() and r.font.size: body_sizes.append(r.font.size.pt)
for t in D.tables:
 for row in t.rows:
  for c in row.cells:
   for p in c.paragraphs:
    for r in p.runs:
     if r.text.strip() and r.font.size: table_sizes.append(r.font.size.pt)
checks['body_font_floor']=not body_sizes or min(body_sizes)>=10.5
checks['table_font_floor']=not table_sizes or min(table_sizes)>=9.5
checks['no_latex_delimiters']=not any(s in text for s in ['\\frac','\\text{','\\begin{','$$'])
failures=[k for k,v in checks.items() if v is not True]
receipt={'schema':'ttqs-one-technical-qa-v1','project_id':'TTQS_ONE','doc_id':'0092','revision':'R05','candidate_docx_path':str(docpath),'candidate_docx_bytes':docpath.stat().st_size,'candidate_docx_sha256':sha(docpath),'replacement_register_path':str(regpath),'replacement_register_bytes':regpath.stat().st_size,'replacement_register_sha256':sha(regpath),'checks':checks,'failures':failures,'technical_status':'PASS_TECHNICAL' if not failures else 'FAIL_TECHNICAL','semantic_status':'PENDING_INDEPENDENT_REVIEW','visual_status':'PENDING_WORD_NATIVE_RENDER_AND_PAGE_QA','formal_acceptance':'NOT_CLAIMED','scope':'Exact SHA technical validation of OOXML/parse, 33-fact internal and external register, F031 synthetic actor/authority codes, F033 single return outcome consistency, access table mechanics, font floors, revision record, and formula markers. Visual and semantic acceptance are separate.','verified_at_local':datetime.now().astimezone().isoformat()}
out=ROOT/'qa'/'R05_TECHNICAL_QA_R01.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'technical_status':receipt['technical_status'],'candidate_sha256':receipt['candidate_docx_sha256'],'register_sha256':receipt['replacement_register_sha256'],'checks':checks,'failures':failures,'receipt':str(out)},ensure_ascii=True,indent=2))
