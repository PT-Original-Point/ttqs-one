from pathlib import Path
import csv,json,hashlib,sys
sys.stdout.reconfigure(encoding='utf-8')
control=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL')
pkg=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03')
cross=control/'TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv'
blue=control/'BLUEPRINT_CURRENT.jsonl'
manual=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\03_157_CHECKBOX_BLUEPRINTS.md')
rows=list(csv.DictReader(cross.open(encoding='utf-8-sig',newline='')))
selected=[r for r in rows if r['requirement_id'] in ['I11-E04','I12-E01','I12-E02','I12-E04']]
bp_rows={}
for i,line in enumerate(blue.read_text(encoding='utf-8-sig').splitlines(),1):
 d=json.loads(line)
 if d.get('deliverable_id') in ['0052','0053','0054','0056']:
  bp_rows[d['deliverable_id']]={'line':i,'deliverable_id':d['deliverable_id'],'requirement_id':d.get('requirement_id'),'document_genre':d.get('document_genre'),'document_purpose':d.get('document_purpose'),'official_requirement_text':d.get('official_requirement_text'),'official_evidence_table_page':d.get('official_evidence_table_page'),'official_source_readback_status':d.get('official_source_readback_status')}
seq_lines=[(i,line) for i,line in enumerate(manual.read_text(encoding='utf-8').splitlines(),1) if '056｜' in line or '056|' in line]
obj={'crosswalk_path':str(cross),'crosswalk_sha256':hashlib.sha256(cross.read_bytes()).hexdigest(),'crosswalk_rows':selected,'blueprint_path':str(blue),'blueprint_file_sha256':hashlib.sha256(blue.read_bytes()).hexdigest(),'blueprint_rows':bp_rows,'checkbox_instruction_source':{'path':str(manual),'sha256':hashlib.sha256(manual.read_bytes()).hexdigest(),'matching_lines':seq_lines,'scope_note':'The 056 sequence is in the current 157-checkbox writing specification; the official page-4 table independently confirms the I12-E01 substance but does not print a sequence number.'}}
out=pkg/'inputs/NEIGHBOR_CROSSWALK_AND_BLUEPRINT_R03.json'
out.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'file':str(out),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'crosswalk_sha256':obj['crosswalk_sha256'],'blueprint_sha256':obj['blueprint_file_sha256'],'neighbor_rows':[r['requirement_id']+':'+r['deliverable_ids'] for r in selected],'checkbox_spec_line':seq_lines},ensure_ascii=False,indent=2))
