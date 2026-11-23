from pathlib import Path
import hashlib,json,datetime
base=Path(r'docs/ttqs-quality-20261016/quality-review/0073_R01')
files=[
'candidate/0073_R04_body.md','candidate/0073_R08.docx',
'inputs/UNIQUE_BLUEPRINT_0073_R01.md','inputs/calculation_summary_R01.json','inputs/learner_feedback_R01.csv','inputs/learner_scores_R01.csv','inputs/question_summary_R01.csv','inputs/returned_forms_R01.csv','inputs/stakeholder_feedback_R01.csv','inputs/synthetic_replacement_register_R01.csv',
'evidence/body_repair_R04.json','evidence/build_receipt_R07.json','evidence/build_receipt_R08.json','evidence/qa_validator_correction_R07.md','evidence/docx_extracted_R08.md','evidence/technical_review_R07_v2.json','evidence/visual_review_R07.json','evidence/technical_review_R08.json','evidence/visual_review_R08.json','evidence/semantic_review_bundle_R08.md','evidence/R08_COMPLETION_RECEIPT.md','evidence/P7_TEST_RECEIPT_0073_R08.json','evidence/render_R08/0073_R08_word_export.pdf',
'review/opencode_semantic_R07_exit.txt','review/opencode_semantic_R07_stderr.txt','review/opencode_semantic_R07_stdout.jsonl','review/semantic_review_bundle_R07.md','review/opencode_semantic_R08_exit.txt','review/opencode_semantic_R08_stderr.txt','review/opencode_semantic_R08_stdout.jsonl','review/independent_semantic_review_R08.md','review/semantic_review_receipt_R08.json',
'worker/WRITER_TASK_R01.md','worker/opencode_writer_R01_body_returned.md','worker/opencode_writer_R01_exit.txt','worker/opencode_writer_R01_stderr.txt','worker/opencode_writer_R01_stdout.jsonl','worker/build_0073_R08_docx.py','worker/technical_qa_R08.py','worker/prepare_review_R08.py','worker/capture_semantic_R08.py','worker/prepare_closeout_R08.py','worker/manifest_R08.py']
files += [str(p.relative_to(base)).replace('\\','/') for p in sorted((base/'evidence/render_R08').glob('page-*.png'))]
entries=[]
for rel in files:
 p=base/rel
 if not p.is_file(): raise SystemExit(f'MISSING {p}')
 b=p.read_bytes(); entries.append({'path':rel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
manifest={'schema':'TTQS_ONE_0073_R08_PUBLIC_PACKAGE_MANIFEST.v1','project_id':'TTQS_ONE','document_id':'0073','requirement_id':'I17A-E01','official_checkbox_serial':'080','candidate_sha256':hashlib.sha256((base/'candidate/0073_R08.docx').read_bytes()).hexdigest(),'official_source':{'repository_path':'docs/ttqs-quality-20261016/quality-review/0072_R01/inputs/official_source.pdf','sha256':'805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709'},'official_blueprint_blob':'8c2bbe7ca9dcbb03088a48934b9e57e7147ede63','source_contract_blobs':{'mission':'538bedb9d87e8465f43151933b4a5c1bfa4bbc4e','genre_manual':'4ff863d9f534b6359fc1c7c1685bd8cce02da886','blueprints':'8c2bbe7ca9dcbb03088a48934b9e57e7147ede63','goal_execution':'62e3dd7dfd8579b6bc97952ffa6236e7494f3b4d','hourly_resume':'60ae010c58140e1710ed24016085c6dfaf6ffaee','external_audit':'263aaca84891bba8dca087875804343c3670e921'},'files':entries,'file_count':len(entries),'all_worked_data':'SAMPLE/SYNTHETIC; REAL=UNKNOWN/HOLD','acceptance':'CANDIDATE ONLY; not formal acceptance'}
(base/'evidence/PACKAGE_MANIFEST_R08.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'file_count':len(entries),'png_count':len([x for x in entries if '/page-' in x['path']]),'total_bytes':sum(x['bytes'] for x in entries),'docx_sha256':manifest['candidate_sha256'],'manifest_sha256':hashlib.sha256((base/'evidence/PACKAGE_MANIFEST_R08.json').read_bytes()).hexdigest()},ensure_ascii=False,indent=2))

