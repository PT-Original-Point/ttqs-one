from pathlib import Path
from hashlib import sha256
import json,datetime
qa=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118\qa\semantic_R08')
stdout=(qa/'W1_STDOUT_R08.jsonl').read_bytes();stderr=(qa/'W1_STDERR_R08.txt').read_bytes()
events=[]
for line in stdout.decode('utf-8-sig').splitlines():
    if line.strip(): events.append(json.loads(line))
texts=[e.get('part',{}).get('text','') for e in events if e.get('type')=='text']
if len(texts)!=1: raise SystemExit(f'EXPECTED_ONE_TEXT_RETURN_FOUND_{len(texts)}')
review=json.loads(texts[0])
finish=[e for e in events if e.get('type')=='step_finish']
if len(finish)!=1 or finish[0].get('part',{}).get('reason')!='stop': raise SystemExit('W1_TERMINAL_EVENT_NOT_CLEAN_STOP')
expected={'work_id':'TTQS_ONE_0028_I05-E02_W1_SEMANTIC_REVIEW_R08_20261118','candidate_docx_sha256':'1EB4E9D26F761B57885AF7DC304BB76324AD85C7513FC858C82AF199D5273F70','extracted_text_sha256':'B999DF1D0A681825C4CD57D7E6220F21E32CC7660EF5FF6983EE3FD8D6474D79','requested_model':'opencode/nemotron-3.5-lightning-free'}
for k,v in expected.items():
    if review.get(k)!=v: raise SystemExit('W1_BINDING_MISMATCH_'+k)
if review.get('decision')!='PASS': raise SystemExit('W1_DECISION_NOT_PASS')
if review.get('served_model')!='UNKNOWN': raise SystemExit('UNEXPECTED_SERVED_MODEL_VALUE')
sha=lambda b:sha256(b).hexdigest().upper()
receipt={'schema':'TTQS_ONE_0028_W1_REVIEW_RETURN_R08','work_id':expected['work_id'],'candidate_docx_sha256':expected['candidate_docx_sha256'],'extracted_text_sha256':expected['extracted_text_sha256'],'requested_model':expected['requested_model'],'served_model':'UNKNOWN','decision':review['decision'],'findings':review.get('findings',[]),'scope_checks':review.get('scope_checks'),'rationale':review.get('rationale'),'session_id':'ses_e13123512ffeJ5gWsYAbKX4J3r','process_id':14464,'process_terminal_event':finish[0],'process_exit_code':'UNKNOWN_NOT_CAPTURED_LAUNCHER_FAILED_AFTER_START','stdout_sha256':sha(stdout),'stdout_bytes':len(stdout),'stderr_sha256':sha(stderr),'stderr_bytes':len(stderr),'returned_review_json_sha256':sha(texts[0].encode('utf-8')),'cost_usd':next((e.get('cost') for e in events if e.get('type')=='step_finish'),None),'token_usage':next((e.get('tokens') for e in events if e.get('type')=='step_finish'),None),'return_recovered_at_local':datetime.datetime.now().astimezone().isoformat(),'result':'PASS_W1_EXACT_SHA_SEMANTIC_REVIEW_R08','exit_code_claimed':False}
out=qa/'W1_REVIEW_RETURN_R08.json'
if out.exists():raise SystemExit('W1_RETURN_RECEIPT_EXISTS')
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['decision','candidate_docx_sha256','served_model','session_id','process_exit_code','cost_usd','token_usage','result','stdout_sha256']},ensure_ascii=False))

