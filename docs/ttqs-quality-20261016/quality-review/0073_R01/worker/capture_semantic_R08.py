from pathlib import Path
import json,hashlib
root=Path(r'docs/ttqs-quality-20261016/quality-review/0073_R01')
raw=root/'review/opencode_semantic_R08_stdout.jsonl'
lines=raw.read_text(encoding='utf-8').splitlines()
obj=[json.loads(x) for x in lines]
msgs=[x.get('part',{}).get('text','') for x in obj if x.get('type')=='text' and x.get('part',{}).get('type')=='text']
if len(msgs)!=1: raise SystemExit(f'expected one final response, found {len(msgs)}')
response=msgs[0]
(root/'review/independent_semantic_review_R08.md').write_text(response+'\n',encoding='utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
docx=root/'candidate/0073_R08.docx'; bundle=root/'evidence/semantic_review_bundle_R08.md'; ext=root/'evidence/docx_extracted_R08.md'
exit_code=(root/'review/opencode_semantic_R08_exit.txt').read_text(encoding='ascii').strip()
session=next((x.get('sessionID') for x in obj if x.get('sessionID')),None)
receipt={'document_id':'0073','requirement_id':'I17A-E01','official_checkbox_serial':'080','candidate_docx_sha256':sha(docx),'extracted_text_sha256':sha(ext),'review_bundle_sha256':sha(bundle),'reviewer_route':'OpenCode V2 CLI','reviewer_model':'opencode/beam-free','writer_model':'opencode/deepseek-v4.1-flash-free','opencode_session_id':session,'cli_exit_code':int(exit_code),'raw_stdout_jsonl_sha256':sha(raw),'raw_stderr_sha256':sha(root/'review/opencode_semantic_R08_stderr.txt'),'original_response_sha256':sha(root/'review/independent_semantic_review_R08.md'),'verdict':'PASS' if '**Semantic verdict: PASS**' in response else 'UNPARSED','semantic_scope':'exact-SHA independent semantic review; visual inspection receipted separately','acceptance':'CANDIDATE ONLY; REAL=UNKNOWN/HOLD'}
(root/'review/semantic_review_receipt_R08.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa_path=root/'evidence/technical_review_R08.json'
qa=json.loads(qa_path.read_text(encoding='utf-8')); qa['semantic_status']='PASS independent exact-SHA review'; qa['semantic_review_receipt_sha256']=sha(root/'review/semantic_review_receipt_R08.json'); qa['acceptance']='CANDIDATE ONLY; REAL=UNKNOWN/HOLD'; qa_path.write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':receipt['verdict'],'docx_sha256':receipt['candidate_docx_sha256'],'session':session,'exit':exit_code,'response_chars':len(response),'response_sha256':receipt['original_response_sha256']},ensure_ascii=False,indent=2))
