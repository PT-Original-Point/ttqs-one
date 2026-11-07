from pathlib import Path
from datetime import datetime
import hashlib,json
BASE=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0100_0101_R08_SOURCE_BLUEPRINT_20261021\candidate_R09b')
REVIEW=BASE/'review'/'W2_DELTA_R01'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
response_path=REVIEW/'AGY_RESPONSE_R01.txt'
response=json.loads(response_path.read_text(encoding='utf-8'))
dispatch=json.loads((REVIEW/'AGY_DISPATCH_RECEIPT_R01.json').read_text(encoding='utf-8'))
tech=json.loads((BASE/'TECHNICAL_QA_0100_R09B.json').read_text(encoding='utf-8'))
visual=json.loads((BASE/'VISUAL_QA_0100_R09B.json').read_text(encoding='utf-8'))
doc=BASE/'0100_I18-E08_R09b.docx'; current=sha(doc)
assert current=='0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c'
assert response['candidate_sha256']==current and response['body_extraction_sha256']==dispatch['body_extraction_sha256']
assert response['verdict']=='PASS'
assert dispatch['cli_exit_code']==0 and dispatch['terminal_status']=='SUCCESS' and dispatch['requested_model_matches_cli_init']
assert not dispatch['tool_steps'] and not dispatch['browser_or_computer_tools_called']
assert tech['candidate']['sha256']==current and tech['result'].startswith('TECHNICAL_PASS')
assert visual['candidate_sha256']==current and visual['result'].startswith('VISUAL_PASS')
criteria=response['criterion_results']
assert all(criteria[k]['status']=='PASS' for k in ['F1','F2','F3','F4','no_new_material_contradiction','sample_real_boundary','scope_inheritance'])
result={
 'receipt_id':'TTQS-0100-I18-E08-R09B-INDEPENDENT-SEMANTIC-ADJUDICATION-R01',
 'generated_local':datetime.now().astimezone().isoformat(),
 'doc_id':'0100','official_requirement_id':'I18-E08','project_internal_index':109,'official_printed_checkbox_serial':'UNKNOWN',
 'candidate_state':'CANDIDATE','candidate_docx_sha256':current,'candidate_bytes':doc.stat().st_size,'body_extraction_sha256':dispatch['body_extraction_sha256'],
 'base_candidate_sha256':dispatch['baseline_docx_sha256'],'base_semantic_result':'PASS_SEMANTIC_ONLY for baseline exact SHA only; not transferred',
 'independent_reviewer':{'route':'Antigravity CLI','work_id':dispatch['work_id'],'cli_version':dispatch['cli_version'],'requested_model':dispatch['requested_model'],'cli_init_model_reported':dispatch['cli_init_model_reported'],'actual_backend_model':'UNKNOWN','no_fallback_event_observed':not dispatch['fallback_event_observed_in_output'],'terminal_status':dispatch['terminal_status'],'exit_code':dispatch['cli_exit_code'],'conversation_id':dispatch['conversation_id'],'tool_steps':dispatch['tool_steps'],'computer_use_or_browser_tools_called':dispatch['browser_or_computer_tools_called'],'usage':dispatch['usage'],'prompt_sha256':dispatch['prompt_sha256'],'reviewer_response_sha256':dispatch['response_sha256'],'reviewer_response_path':dispatch['response_path']},
 'reviewer_verdict':'PASS','review_scope':'Exact R09b DOCX SHA delta review covering every changed paragraph and table row, findings F1-F4, consistency with the 0100/0101 handoff, and inherited baseline review for unchanged body. Reviewer did not inspect visual pages.',
 'criteria':{k:v['status'] for k,v in criteria.items()},
 'findings':response['findings'],
 'local_adjudication':'PASS_SEMANTIC_DELTA_FOR_EXACT_SHA_WITH_BASELINE_INHERITANCE',
 'local_basis':['Reviewer response JSON parsed and matched candidate SHA and body extraction SHA.','R09a baseline SHA equals the independently reviewed prior candidate SHA; current structured body diff identifies the targeted R09b edits.','F1-F4 all PASS in reviewer result; unchanged 80-cell synthetic matrix was independently checked against source packet by the local deterministic QA.','Technical QA exact-SHA receipt and separate 16-page visual receipt both bind to the current DOCX SHA.'],
 'technical_qa':{'result':tech['result'],'receipt_path':str(BASE/'TECHNICAL_QA_0100_R09B.json'),'receipt_sha256':sha(BASE/'TECHNICAL_QA_0100_R09B.json')},
 'visual_qa':{'result':visual['result'],'receipt_path':str(BASE/'VISUAL_QA_0100_R09B.json'),'receipt_sha256':sha(BASE/'VISUAL_QA_0100_R09B.json'),'scope':visual['pages_inspected'],'nonblocking_observation':'Page 13 has substantial white space before section 9 on page 14; readable and no clipping. No further layout edit made.'},
 'real_evidence':'UNKNOWN/HOLD; no real learner records provided','formal_acceptance':'NOT_GRANTED','promotion':'NOT_PROMOTED',
 'limitations':['Backend-serving model identity remains UNKNOWN despite the CLI init reporting the requested slug.','Semantic reviewer performed text-only delta review; visual inspection is separate.','Prior semantic PASS applies only to baseline SHA, with inheritance limited to unchanged body; this receipt adjudicates the R09b delta.','No physical print test or association acceptance.']
}
out=BASE/'INDEPENDENT_ADJUDICATION_0100_R09B_R01.json';out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':current,'reviewer_verdict':response['verdict'],'local_adjudication':result['local_adjudication'],'technical_receipt_sha256':result['technical_qa']['receipt_sha256'],'visual_receipt_sha256':result['visual_qa']['receipt_sha256'],'adjudication_path':str(out),'adjudication_sha256':sha(out),'formal_acceptance':result['formal_acceptance'],'actual_backend_model':result['independent_reviewer']['actual_backend_model']},ensure_ascii=False))
