from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json, subprocess, re
root=Path(r'E:\TTQS\_github_sync_0064')
pkg=root/'docs'/'ttqs-quality-20261016'/'quality-review'/'0076_R01'
ev=pkg/'evidence'; rev=pkg/'review'; wi=pkg/'worker'
def h(p): return sha256(p.read_bytes()).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=root,text=True,encoding='utf-8').strip()
docx=pkg/'candidate'/'0076_R01.docx'
stdout=rev/'opencode_semantic_R01_stdout.jsonl'
semantic=rev/'independent_semantic_review_R01.md'
vis=json.loads((ev/'visual_review_R01.json').read_text(encoding='utf-8'))
extract=json.loads((ev/'docx_extraction_receipt_R01.json').read_text(encoding='utf-8'))
# The CLI run is complete, exit 0, and model output has been preserved verbatim in JSONL.
attached=[
 rev/'semantic_review_prompt_R01.md',pkg/'inputs'/'UNIQUE_BLUEPRINT_0076_R01.md',pkg/'inputs'/'SOURCE_PACKET_0076_R01.md',
 rev/'docx_extracted_R01.md',ev/'docx_extraction_receipt_R01.json',ev/'technical_review_R01.json',ev/'visual_review_R01.json',
 pkg/'inputs'/'SYNTHETIC_ASSESSMENT_DATA_0076_R01.csv',pkg/'inputs'/'SYNTHETIC_ITEM_ANALYSIS_0076_R01.csv',
 pkg/'inputs'/'SYNTHETIC_CALCULATION_CHECK_0076_R01.json',pkg/'inputs'/'SYNTHETIC_REPLACEMENT_REGISTER_0076_R01.csv',
 pkg/'inputs'/'upstream_snapshots'/'official_evidence_table_source.pdf'
]
dispatch={
 'schema':'TTQS_ONE_0076_SEMANTIC_REVIEW_DISPATCH_R01.v1','document_id':'0076','requirement_id':'I17B-E01','official_checkbox_serial':'084',
 'candidate_docx_sha256':h(docx),'candidate_docx_bytes':docx.stat().st_size,
 'route':'OpenCode CLI v2','cli_version':'2.0.29','model':'opencode/beam-free','session_id':'ses_eae64f03cffezJNEC42vjxpWiV',
 'computer_use':False,'review_only':True,'process_exit_code':int((rev/'opencode_semantic_R01_exit.txt').read_text(encoding='utf-8')),
 'stdout_path':'review/opencode_semantic_R01_stdout.jsonl','stdout_sha256':h(stdout),'stdout_bytes':stdout.stat().st_size,
 'stderr_path':'review/opencode_semantic_R01_stderr.txt','stderr_sha256':h(rev/'opencode_semantic_R01_stderr.txt'),'stderr_bytes':(rev/'opencode_semantic_R01_stderr.txt').stat().st_size,
 'review_path':'review/independent_semantic_review_R01.md','review_sha256':h(semantic),'review_bytes':semantic.stat().st_size,
 'prompt_sha256':h(rev/'semantic_review_prompt_R01.md'),
 'attached_inputs':[{'path':str(f.relative_to(pkg)).replace('\\','/'),'sha256':h(f),'bytes':f.stat().st_size} for f in attached],
 'verdict':'PASS','scope_limitations':['Reviewer relied on source packet and Unique Blueprint for official requirement wording; its PDF text decoding was not usable.','Reviewer relied on supplied visual receipt and did not independently inspect page images.'],
 'formal_acceptance':'NOT_GRANTED','composite_checkbox_state':'PARTIAL','real_status':'UNKNOWN/HOLD',
 'completed_utc':datetime.now(timezone.utc).isoformat()
}
(ev/'semantic_review_dispatch_R01.json').write_text(json.dumps(dispatch,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# R04 P0-P8 continuation checkpoint. Readback remains pending until the package is pushed.
r04=root/'docs'/'ttqs-quality-20261016'/'quality-review'/'R04_P0_P8_20261019'
head=git('rev-parse','HEAD'); remote=git('rev-parse','origin/work/ttqs-one-document-quality-contract-20261016')
visual_pdf=ev/'render_word_R01'/'0076_R01_word_render.pdf'
status={
 'schema':'TTQS_ONE_R04_CONTINUATION_0076_R01.v1','project_id':'TTQS_ONE','command':'TTQS_ONE_CODEX_NATIVE_WORKER_RECOVERY_SYNC_R04',
 'source_attachment_sha256':'3330de8de26275c5e51f299982d87c250bb7e030c9838badafc369e26ee29c35',
 'current_source_commit':'e43dbf8da93b1738ecb30c591010d3ca123d2ab6','current_local_head_before_sync':head,'current_remote_tracking_head_before_sync':remote,
 'P0_readonly_preflight':{'status':'VERIFIED','checks':['Live GitHub PR #92/branch head checked before build and worker dispatch.','No active 0076 Writer or reviewer before dispatch; OpenCode persistent service was not treated as document owner.','One OpenCode Writer completed; its task process exited before review dispatch.','No Antigravity/Computer Use dispatch.']},
 'P1_reconciliation':{'status':'VERIFIED','historical_0076_candidate_sha256':'f0099863f55cd9a180b502c1fc5d03b303aa8ea38b14b74f4783afdb2b8e4471','decision':'Historical candidate was a different course/date/sample and lacked complete keyed instrument; new 0076 candidate was required. Unrelated previously qualified DOCX were not rebuilt.'},
 'P2_cli_recovery':{'status':'APPLIED','writer':{'route':'OpenCode CLI v2','version':'2.0.29','model':'opencode/deepseek-v4.1-flash-free','session_id':'ses_eae7040e2ffervxNMrBSrt9W0J','exit_code':0,'computer_use':False},'reviewer':{'route':'OpenCode CLI v2','version':'2.0.29','model':'opencode/beam-free','session_id':'ses_eae64f03cffezJNEC42vjxpWiV','exit_code':0,'computer_use':False},'antigravity':'No new dispatch; route remains paused pending its authorized headless CLI path; no Computer Use or permission bypass.'},
 'P3_worker_return':{'status':'APPLIED','body_sha256':'00266efaeefb061c61c84c2478f5cc96ad09289c7f711286e6c4a31181cbe95f','docx_sha256':'885fe403b46144639034a3f6b26c2b74916c22c7b5a5a971628136f376a115f3','worker_stdout_sha256':h(wi/'opencode_writer_R01_stdout.jsonl'),'register_sha256':h(pkg/'inputs'/'SYNTHETIC_REPLACEMENT_REGISTER_0076_R01.csv'),'details':'Original worker body and raw output retained; two pre-build editorial corrections are separately receipted; builder did not modify unrelated DOCX.'},
 'P4_github_sync':{'status':'PENDING_PACKAGE_PUSH_AND_BYTE_READBACK','package_path':'docs/ttqs-quality-20261016/quality-review/0076_R01/','remote_readback_required':True},
 'P5_scheduler_and_cost':{'status':'VERIFIED_UNCHANGED','scheduler':'One existing thread-bound hourly task retained; no scheduler/session/control-platform created.','model_cost':'OpenCode writer and independent reviewer each consumed a model call; not represented as zero cost.'},
 'P6_next_ready':{'status':'QUEUED_AFTER_0076_SYNC','document_id':'0077','requirement_id':'I17B-E01','official_checkbox_serial':'084','function':'Learner reflection report, distinct from 0076 assessment record.'},
 'P7_five_tests':{
  'T1':'PASS inherited R04 fixture-only/no-op check; does not claim a scheduled wake test.',
  'T2':'PASS inherited route-isolation check for historical 0055 work.',
  'T3':'PASS inherited exact-SHA reuse/no-duplicate-review check.',
  'T4':'PENDING; current 0076 package requires GitHub blob readback and hash comparison.',
  'T5':'PASS; 0076 clearly SAMPLE/SYNTHETIC, candidate-only, REAL=UNKNOWN/HOLD, no formal acceptance; checkbox 084 remains composite PARTIAL.'},
 'P8_result':{'status':'CANDIDATE_READY_FOR_REMOTE_SYNC','technical':'PASS exact DOCX SHA','visual':'PASS_LAYOUT_VISUAL all 26 pages inspected; PDF SHA '+h(visual_pdf),'semantic':'PASS independent OpenCode CLI v2 beam-free; exact DOCX SHA bound via extraction receipt','candidate_sha256':h(docx),'page_count':vis['page_count'],'checkbox_084':'PARTIAL; 0077/0078/0079 and real sources still outstanding','formal_acceptance':'NOT_GRANTED','real_status':'UNKNOWN/HOLD'},
 'updated_utc':datetime.now(timezone.utc).isoformat()
}
(r04/'R04_CONTINUATION_0076_R01.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# public-facing scan of high-risk secret formats in text files only
patterns=[re.compile(r'ghp_[A-Za-z0-9]{30,}'),re.compile(r'github_pat_[A-Za-z0-9_]{30,}'),re.compile(r'AKIA[0-9A-Z]{16}'),re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),re.compile(r'(?i)Bearer\s+[A-Za-z0-9._-]{30,}')]
findings=[]
for f in pkg.rglob('*'):
 if f.is_file() and f.suffix.lower() in {'.md','.txt','.json','.csv','.py','.log','.xml'}:
  b=f.read_bytes()
  try:t=b.decode('utf-8-sig')
  except UnicodeDecodeError:continue
  for pat in patterns:
   if pat.search(t): findings.append(str(f.relative_to(root)))
if findings: raise SystemExit('possible secret patterns: '+repr(findings))
# manifest excludes its own bytes to avoid recursion
manifest_path=ev/'package_manifest_R01.json'
files=sorted(f for f in pkg.rglob('*') if f.is_file() and f!=manifest_path)
manifest={
 'schema':'TTQS_ONE_0076_PACKAGE_MANIFEST_R01.v1','document_id':'0076','requirement_id':'I17B-E01','official_checkbox_serial':'084',
 'candidate_docx_sha256':h(docx),'candidate_status':'CANDIDATE_ONLY','formal_acceptance':'NOT_GRANTED','real_status':'UNKNOWN/HOLD','checkbox_084':'PARTIAL',
 'file_count_excluding_manifest':len(files),'total_bytes_excluding_manifest':sum(f.stat().st_size for f in files),
 'manifest_scope':'All files under this package except this manifest itself; paths are package-relative. Contains synthetic candidate material, public official-source PDF, source snapshots, raw worker/reviewer outputs, technical/visual/semantic receipts and full render evidence.',
 'secret_scan':'PASS for high-confidence credential/private-key patterns in UTF-8 text files; not a substitute for review of any newly added private source.',
 'files':[{'path':str(f.relative_to(pkg)).replace('\\','/'),'bytes':f.stat().st_size,'sha256':h(f)} for f in files],
 'created_utc':datetime.now(timezone.utc).isoformat()
}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'docx_sha256':h(docx),'semantic':dispatch['verdict'],'semantic_sha256':h(semantic),'visual_status':vis['visual_status'],'visual_pages':vis['page_count'],'package_files':len(files)+1,'package_bytes':manifest['total_bytes_excluding_manifest']+manifest_path.stat().st_size,'secret_scan':'PASS','pre_sync_head':head,'remote_tracking':remote},ensure_ascii=False))
