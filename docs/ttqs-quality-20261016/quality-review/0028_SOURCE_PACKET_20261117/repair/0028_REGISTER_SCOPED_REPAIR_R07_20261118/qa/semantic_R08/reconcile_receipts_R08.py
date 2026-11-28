from pathlib import Path
from hashlib import sha256
import json,datetime
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118')
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def H(b):return sha256(b).hexdigest().upper()
conv=base/'DOCX_CONVERSION_R07.json';d=load(conv)
d['word_com_status']='WORD_NATIVE_PDF_EXPORTED; exact R07 DOCX SHA bound; process PID UNKNOWN; 24-page PDF produced.'
d['word_com_pdf_sha256']='BD427EDA8C64A3859C2BC21F85DF4507BD87FC7AD6B6CD0DC587D00492539ACA'
d['word_com_page_count']=24
d['word_com_receipt_path']='qa/visual_R07_wordcom/WORD_COM_RENDER_STATUS_R07.json'
d['visual_review']='FAIL_LAYOUT_BLANK_PAGES_P21_P23; exact R07 PDF preserved; replaced by R08 scoped layout repair.'
d['semantic_review_for_docx']='SUPERSEDED_BEFORE_REVIEW_BY_R08'
d['formal_acceptance']='NOT_CLAIMED'
d['reconciled_at_tpe']=datetime.datetime.now().astimezone().isoformat()
save(conv,d)
attempt=base/'qa'/'DOCX_DETERMINISTIC_QA_R08.json';a=load(attempt)
a['diagnostic_attempt_only']=True
a['failure_class']='QA_PARSER_PATTERN_DEFECT: the initial regex omitted IDs with multiple hyphenated code segments; it counted 81, while corrected pattern counts all 91 registered IDs.'
a['candidate_document_failure']=False
a['superseded_by']='qa/DOCX_DETERMINISTIC_QA_R08_RECHECK.json'
save(attempt,a)
qa=base/'qa'/'semantic_R08';dispatch=load(qa/'W1_DISPATCH_R08.json');ret=load(qa/'W1_REVIEW_RETURN_R08_RECONCILED.json')
completion={
 'schema':'TTQS_ONE_0028_W1_COMPLETION_R08',
 'work_id':ret['work_id'],
 'dispatch_manifest_sha256':H((qa/'W1_DISPATCH_R08.json').read_bytes()),
 'review_packet_sha256':dispatch['packet_sha256'],
 'candidate_docx_sha256':ret['candidate_docx_sha256'],
 'extracted_text_sha256':ret['extracted_text_sha256'],
 'route':'OpenCode v2 CLI',
 'requested_model':ret['requested_model'],
 'served_model':'UNKNOWN',
 'process_id':ret['process_id'],
 'session_id':ret['session_id'],
 'terminal_event':ret['provider_terminal_reason'],
 'process_exit_code':ret['process_exit_code'],
 'review_decision':ret['decision'],
 'findings':ret['findings'],
 'stdout_sha256':ret['stdout_sha256'],
 'stderr_sha256':ret['stderr_sha256'],
 'review_json_sha256':ret['review_json_sha256'],
 'cost_usd':ret['cost_usd'],
 'token_usage':ret['token_usage'],
 'automatic_retry':False,
 'result':'COMPLETED_PASS_EXACT_SHA; OS exit code not captured because launcher receipt serialization failed after process start.',
 'completed_at_local':ret['return_recovered_at_local']
}
out=qa/'W1_COMPLETION_R08.json'
if out.exists():raise SystemExit('W1_COMPLETION_EXISTS')
save(out,completion)
print(json.dumps({'conversion_status':d['word_com_status'],'r07_visual':d['visual_review'],'parser_failure_clarified':a['failure_class'],'w1_decision':completion['review_decision'],'w1_cost':completion['cost_usd'],'w1_tokens':completion['token_usage'],'w1_exit':completion['process_exit_code'],'completion_receipt_sha256':H(out.read_bytes())},ensure_ascii=False))

