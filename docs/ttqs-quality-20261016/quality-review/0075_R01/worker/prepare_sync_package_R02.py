from pathlib import Path
from datetime import datetime
import hashlib,json,subprocess
root=Path(r'E:\TTQS\_github_sync_0064')
base=root/'docs/ttqs-quality-20261016/quality-review/0075_R01'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
docx=base/'candidate/0075_R02.docx'; pdf=base/'evidence/0075_R02_word_render_ca81a479.pdf'; register=base/'inputs/SYNTHETIC_REPLACEMENT_REGISTER_0075_R01.csv'
status_path=base/'evidence/candidate_status_R02.json'; sem_path=base/'evidence/semantic_review_receipt_R02.json'; vis_path=base/'evidence/visual_review_R02.json'; tech_path=base/'evidence/technical_review_R02.json'
status=json.loads(status_path.read_text(encoding='utf-8'))
status['quality']['visual']='PASS_WITH_SCOPE'; status['quality']['semantic']='PASS'; status['quality']['blocking_findings']=0
status['quality']['reviewer_session']='ses_eae841cdcffeT8KZ7QUzvmnXrm'
status['remote_sync']='PENDING'
status['source_candidate_sha256']=sha(docx)
status['source_artifact_sha256']={'register':sha(register),'semantic_receipt':sha(sem_path),'visual_receipt':sha(vis_path),'technical_receipt':sha(tech_path),'render_pdf':sha(pdf)}
status_path.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
base_head=subprocess.run(['git','rev-parse','HEAD'],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True).stdout.strip()
p8={
 'command':'TTQS_ONE_CODEX_NATIVE_WORKER_RECOVERY_SYNC_R04','project_id':'TTQS_ONE','document_id':'0075','requirement_id':'I17A-E03','official_checkbox_serial':'082',
 'source_branch':'work/ttqs-one-document-quality-contract-20261016','source_head_before_sync':base_head,
 'candidate_sha256':sha(docx),'candidate_status':'CANDIDATE_ONLY','technical':'TECHNICAL_PASS','visual':'PASS_WITH_SCOPE 21/21 pages','semantic':'PASS OpenCode V2 beam-free exact extraction bound to candidate SHA; 0 blocking findings','formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN/HOLD',
 'worker_recovery':'Writer OpenCode V2 deepseek-v4.1-flash-free completed; reviewer OpenCode V2 beam-free separate session completed; no active 0075 writer/reviewer at sync preparation; Antigravity route remains paused; no Computer Use.',
 'layout_repair':'R01 orphaned 10.1 checklist header fixed in R02; extracted DOCX body text equality verified; no unaffected document rebuilt.',
 'open_note':'Reviewer noted optional M2/M3 protocol colocation; not blocking and not rebuilt. Human print-device fidelity not tested.',
 'sync_state':'READY_TO_SYNC','next_action':'Push the complete 0075 R01/R02 evidence package to existing PR branch, then fetch and compare exact hashes.'
}
(base/'evidence/R04_P8_STATUS_0075_R02.json').write_text(json.dumps(p8,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest_path=base/'evidence/package_manifest_R02.json'
entries=[]
for p in sorted(base.rglob('*')):
 if p.is_file() and p!=manifest_path:
  entries.append({'path':p.relative_to(base).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
manifest={'schema':'TTQS_ONE_0075_R02_PACKAGE_MANIFEST.v1','document_id':'0075','requirement_id':'I17A-E03','official_checkbox_serial':'082','candidate_sha256':sha(docx),'source_head_before_sync':base_head,'file_count_excluding_manifest':len(entries),'total_bytes_excluding_manifest':sum(x['bytes'] for x in entries),'files':entries}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'base_head':base_head,'candidate_sha256':sha(docx),'files':len(entries),'bytes':sum(x['bytes'] for x in entries),'manifest_sha256':sha(manifest_path),'status_sha256':sha(status_path),'p8_sha256':sha(base/'evidence/R04_P8_STATUS_0075_R02.json')},ensure_ascii=False,indent=2))
