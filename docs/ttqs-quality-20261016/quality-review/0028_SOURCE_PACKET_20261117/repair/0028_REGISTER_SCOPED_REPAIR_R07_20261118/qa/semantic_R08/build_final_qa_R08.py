from pathlib import Path
from hashlib import sha256
import json,datetime
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118')
qa=base/'qa';sem=qa/'semantic_R08';vis=qa/'visual_R08_wordcom'
files={
 'source_manifest':base.parent.parent/'SOURCE_PACKET_MANIFEST.json',
 'source_packet':base.parent.parent/'source'/'SOURCE_PACKET_0028_I05-E02_R01.md',
 'blueprint':base.parent.parent/'blueprint'/'UNIQUE_BLUEPRINT_0028_I05-E02_R01.md',
 'static':base/'STATIC_QA_R07.json','math':base/'MATH_QA_R07.json',
 'layout':qa/'DOCX_LAYOUT_REPAIR_R08.json',
 'docx_qa':qa/'DOCX_DETERMINISTIC_QA_R08_RECHECK.json',
 'visual':vis/'FULL_PAGE_VISUAL_QA_R08.json',
 'wordcom':vis/'WORD_COM_RENDER_R08.json',
 'w1':sem/'W1_COMPLETION_R08.json',
 'candidate':base/'candidate_0028_R08_20261118.docx',
 'html':base/'candidate_0028_R07_20261118.html',
}
def H(p):return sha256(p.read_bytes()).hexdigest().upper()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
static=read(files['static']);math=read(files['math']);layout=read(files['layout']);docxqa=read(files['docx_qa']);visual=read(files['visual']);render=read(files['wordcom']);w1=read(files['w1'])
candidate_sha=H(files['candidate'])
checks={
 'source_packet_and_blueprint_bound':H(files['source_packet'])=='5D1939E0C98AF5E3E115B55BA9D41F56203A7C3A5977C7134816E3AB36783243' and H(files['blueprint'])=='4934FE46F7EAFCE899C7FEC7A8A08B06AC504E59CCAECB4EBBDDC50F08CE8095',
 'static_html_qa_pass':static['result']=='PASS_STATIC_HTML_ONLY',
 'math_qa_pass':math['result']=='PASS_DETERMINISTIC_MATH_AND_FACT_REGISTER_R07',
 'layout_repair_pass':layout['visible_body_text_unchanged'] and layout['non_document_package_parts_byte_identical'] and layout['removed_empty_paragraph_count']==89,
 'docx_deterministic_qa_pass_same_sha':docxqa['result']=='PASS_DOCX_DETERMINISTIC_QA_R08' and docxqa['candidate_docx_sha256']==candidate_sha,
 'word_native_pdf_same_sha':render['result']=='PASS_WORD_NATIVE_PDF_EXPORTED' and render['candidate_docx_sha256']==candidate_sha,
 'full_page_visual_pass_same_sha':visual['result']=='PASS_FULL_PAGE_VISUAL_R08' and visual['candidate_docx_sha256']==candidate_sha and visual['page_count']==21,
 'w1_semantic_pass_same_sha':w1['review_decision']=='PASS' and w1['candidate_docx_sha256']==candidate_sha and w1['served_model']=='UNKNOWN',
}
if not all(checks.values()):raise SystemExit('FINAL_QA_PRECOMMIT_CHECK_FAILED:'+','.join(k for k,v in checks.items() if not v))
receipt={
 'schema':'TTQS_ONE_0028_FINAL_QA_R08',
 'work_id':'TTQS_ONE_0028_I05-E02_FINAL_CANDIDATE_QA_R08_20261118',
 'doc_id':'0028','requirement_id':'I05-E02',
 'candidate_path':'candidate_0028_R08_20261118.docx','candidate_sha256':candidate_sha,'candidate_bytes':files['candidate'].stat().st_size,
 'source_html_sha256':H(files['html']),
 'source_packet_sha256':H(files['source_packet']),'blueprint_sha256':H(files['blueprint']),
 'evidence':{
  'static_html_qa':{'file':'STATIC_QA_R07.json','file_sha256':H(files['static']),'result':static['result'],'candidate_html_sha256':static['candidate_html_sha256']},
  'deterministic_math_qa':{'file':'MATH_QA_R07.json','file_sha256':H(files['math']),'result':math['result'],'candidate_html_sha256':math['candidate_html_sha256']},
  'scoped_layout_repair':{'file':'qa/DOCX_LAYOUT_REPAIR_R08.json','file_sha256':H(files['layout']),'removed_whitespace_only_paragraphs':layout['removed_empty_paragraph_count']},
  'docx_deterministic_qa':{'file':'qa/DOCX_DETERMINISTIC_QA_R08_RECHECK.json','file_sha256':H(files['docx_qa']),'result':docxqa['result'],'body_font_min_pt':docxqa['body_font_min_pt'],'table_font_min_pt':docxqa['table_font_min_pt']},
  'word_visual':{'file':'qa/visual_R08_wordcom/FULL_PAGE_VISUAL_QA_R08.json','file_sha256':H(files['visual']),'pdf_sha256':render['pdf_sha256'],'page_count':visual['page_count'],'result':visual['result']},
  'w1_semantic_review':{'file':'qa/semantic_R08/W1_COMPLETION_R08.json','file_sha256':H(files['w1']),'route':w1['route'],'requested_model':w1['requested_model'],'served_model':'UNKNOWN','decision':w1['review_decision'],'findings_count':len(w1['findings']),'cost_usd':w1['cost_usd'],'token_usage':w1['token_usage'],'process_exit_code':w1['process_exit_code'],'session_id':w1['session_id']},
 },
 'checks':checks,
 'candidate_status':'CANDIDATE_SAMPLE_SYNTHETIC',
 'formal_acceptance':'NOT_CLAIMED',
 'github_sync':'PENDING_SAME_REF_RAW_BYTE_READBACK_AFTER_COMMIT',
 'next_action':'Commit only this deliverable and necessary evidence to PR #92 branch after fresh HEAD and shared-write check; then raw-read candidate from the same ref and compare SHA-256.',
 'human_gate':'NONE',
 'measured_at_local':datetime.datetime.now().astimezone().isoformat()
}
out=qa/'FINAL_QA_R08.json'
if out.exists():raise SystemExit('FINAL_QA_R08_EXISTS')
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'result':'PASS_FINAL_QA_R08_PRE_GITHUB_READBACK','candidate_sha256':candidate_sha,'checks':checks,'receipt_sha256':H(out),'receipt':str(out)},ensure_ascii=False))

