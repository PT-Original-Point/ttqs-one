from pathlib import Path
import json,hashlib,datetime
b=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0119_I19-E07_SOURCE_PREP_R01_20261024')
root=b/'candidate_R01H'; qa=root/'qa_R01H'; bundle=qa/'review_bundle_R01H'
c=root/'0119__目標市場及顧客價值部分提升證據分析表_R01H.docx'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
response_path=bundle/'antigravity_response_R01H.txt'; response=json.loads(response_path.read_text(encoding='utf-8'))
dispatch=json.loads((bundle/'dispatch_receipt_R01H.json').read_text(encoding='utf-8'))
inputs=json.loads((bundle/'review_input_manifest_R01H.json').read_text(encoding='utf-8'))
tech=json.loads((qa/'technical_content_QA_R01H.json').read_text(encoding='utf-8'))
visual=json.loads((qa/'visual_inspection_receipt_R01H.json').read_text(encoding='utf-8'))
build=json.loads((root/'build_receipt_R01H.json').read_text(encoding='utf-8'))
assert sha(c)==dispatch['candidate_sha256']==response['binding']['docx_sha256']
assert inputs['candidate_text_sha256']==dispatch['candidate_text_sha256']==response['binding']['extracted_text_sha256']
assert dispatch['actual_model_from_init']=='gemini-3.8-flash-high' and dispatch['exit_code']==0 and not dispatch['timed_out'] and dispatch['tool_call_count']==0
assert response['verdict']=='PASS' and response['binding']['formal_acceptance']=='NOT_GRANTED'
assert all(row.get('verdict')=='PASS' for row in response['checklist_10_rows']) and len(response['checklist_10_rows'])==10
assert response.get('blockers')==[]
assert tech['all_checks_pass'] is True and tech['docx_sha256']==sha(c)
assert visual['verdict']=='PASS_LAYOUT' and visual['docx_sha256']==sha(c) and len(visual['page_images'])==23
assert build['candidate_sha256']==sha(c)
receipt={'work_id':dispatch['work_id'],'doc_id':'0119','requirement_id':'I19-E07','candidate':'R01H','candidate_docx_sha256':sha(c),'candidate_extracted_text_sha256':inputs['candidate_text_sha256'],'reviewer':'Antigravity CLI 1.4.7','requested_model':dispatch['requested_model'],'actual_model_from_init':dispatch['actual_model_from_init'],'cli_pid':dispatch['pid'],'cli_exit_code':dispatch['exit_code'],'timed_out':dispatch['timed_out'],'tool_calls':dispatch['tool_call_count'],'actual_model_and_dispatch_integrity':dispatch['dispatch_integrity'],'usage':dispatch['usage'],'original_response_path':str(response_path),'original_response_sha256':sha(response_path),'prompt_sha256':dispatch['prompt_sha256'],'source_packet_sha256':inputs['source_packet_sha256'],'unique_blueprint_sha256':inputs['unique_blueprint_sha256'],'mapping_sha256':inputs['mapping_sha256'],'official_pdf_sha256':inputs['official_pdf_sha256'],'official_page8_text_sha256':inputs['official_page8_text_sha256'],'scope':'independent semantic review of the complete extracted exact-SHA document text and official/source/Blueprint mapping; 10 review rows and all recomputation audits checked; excludes visual inspection, real association evidence and formal acceptance','reviewer_verdict':response['verdict'],'checklist_rows':len(response['checklist_10_rows']),'all_checklist_rows_pass':True,'blockers':response['blockers'],'nonblocking_findings':response['nonblocking_findings'],'coordinator_adjudication':'PASS for semantic scope only: binding SHAs and mapping inputs match current local files; all 10 checklist rows PASS; response has zero blockers; calculations independently match technical QA; local all-page visual QA separately PASS.','visual_receipt_sha256':sha(qa/'visual_inspection_receipt_R01H.json'),'technical_receipt_sha256':sha(qa/'technical_content_QA_R01H.json'),'semantic_status':'PASS_EXACT_SHA_SEMANTIC_SCOPE','formal_acceptance':'NOT_GRANTED','sample_real_status':'SAMPLE_SYNTHETIC_ONLY','adjudicated_at_local':datetime.datetime.now().astimezone().isoformat()}
(qa/'independent_semantic_review_receipt_R01H.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Update only status metadata in receipts; never alter the accepted candidate bytes.
build.update({'visual_review':'PASS_LAYOUT_ALL_23_PAGES','semantic_review':'PASS_EXACT_SHA_SEMANTIC_SCOPE','semantic_review_receipt':'qa_R01H/independent_semantic_review_receipt_R01H.json','formal_acceptance':'NOT_GRANTED'})
(root/'build_receipt_R01H.json').write_text(json.dumps(build,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
tech['independent_semantic_review']={'status':'PASS_EXACT_SHA_SEMANTIC_SCOPE','receipt':'independent_semantic_review_receipt_R01H.json','reviewed_docx_sha256':sha(c),'review_response_sha256':sha(response_path),'formal_acceptance':'NOT_GRANTED'}
(qa/'technical_content_QA_R01H.json').write_text(json.dumps(tech,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':sha(c),'semantic_review':'PASS_EXACT_SHA_SEMANTIC_SCOPE','review_response_sha256':sha(response_path),'review_receipt_sha256':sha(qa/'independent_semantic_review_receipt_R01H.json'),'visual':'PASS_LAYOUT_ALL_23_PAGES','formal_acceptance':'NOT_GRANTED','checklist_passes':10,'blockers':0},ensure_ascii=True))
