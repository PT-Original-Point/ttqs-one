from pathlib import Path
from hashlib import sha256
import json
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0132_I19-E21_SOURCE_PREP_R01_20261024')
rev=root/'review'/'W2_EXACT_SHA_20261026'
def h(p):return sha256(p.read_bytes()).hexdigest()
raw=json.loads((rev/'ANTIGRAVITY_STDOUT.txt').read_text(encoding='utf-8'))
dispatch=json.loads((rev/'DISPATCH_RESULT.json').read_text(encoding='utf-8-sig'))
dispatch.update({'cli_version':'1.4.7','cli_executable':'C:/Users/J/AppData/Local/agy/bin/agy.exe','native_model_attestation':'ABSENT','actual_model_identity':'UNKNOWN','native_tool_calls':'No tool-call field in native JSON; stdout is a single response envelope. Computer Use was not invoked in this run.'})
(rev/'DISPATCH_RESULT.json').write_text(json.dumps(dispatch,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
source={'source_packet_sha256':'43c41b7f5eaf5114bf7d9a6d7da11b6097275527784b94579680b5c5847cd0c0','source_packet_git_blob':'b5e48be84d6536c21f6bba80de7abdd3d5ea80a1','unique_blueprint_sha256':'a888bb09f0e5cf523cc1626ad65049f11f78f0bd8bd4d8ba679b26073904e7ca','unique_blueprint_git_blob':'16fb436302d350b91611facd93610412aa7f88d0','official_extract_sha256':'5358d9ccdd3f2903cae85db3551e9d8263a0a76cb1d27c35f6bd2aa6dfc20ef9','official_extract_git_blob':'fa1bfb2de0a1d8649d53b84db33ee47d9b6b120e','neighbor_crosswalk_sha256':'c9c0b42e6b74e4cd19fa17c5566462abf0ce844fffa0fda6a7f0b335bfdf99bf','neighbor_crosswalk_git_blob':'c898ee88644ccf808d436a6a9e2ddf0eb02100f1'}
math={
 'pre_N':66,'pre_D':13,'pre_rate_pct':19.696969696969695,
 'post_N':70,'post_D':8,'post_rate_pct':11.428571428571429,
 'post_minus_pre_percentage_points':-8.268398268398266,'relative_decline_pct':41.97802197802199,
 'defective_unit_change_pct':-38.46153846153847,'inspected_volume_change_pct':6.0606060606060606,
 'batch_rates_pct':{'SYN-B1':20.0,'SYN-B2':20.833333333333336,'SYN-B3':18.181818181818183,'SYN-A1':14.285714285714285,'SYN-A2':12.0,'SYN-A3':8.333333333333334},
 'primary_reason_totals':{'pre':{'cutting':6,'sewing':4,'edge':3,'sum':13},'post':{'cutting':3,'sewing':3,'edge':2,'sum':8}},
 'chart_consistency':'Both embedded PNGs visually inspected; values and sample/cause annotations match text and calculations.'
}
adj={
 'project_id':'TTQS_ONE','doc_id':'0132','internal_requirement_id':'I19-E21','project_157_index':145,'official_section':'I19-L3','official_page':8,'official_text':'個人產品不良件數有下降趨勢。','printed_official_checkbox_serial':'UNKNOWN',
 'source_commit':'1db5e97bd173cfe802aba752198204d97bf90270','branch':'work/ttqs-one-document-quality-contract-20261016','pr':92,
 'candidate':{'path':str(root/'candidate'/'0132_I19-E21_CANDIDATE_R01.docx'),'sha256':'e2f263c2c130d1939ebdaab1a253700935c54c8a26c937b8a77e7000a9a2d925','git_blob':'7ada5d133193314794700661ad7ca309da9c02dc','unchanged_during_review':True},
 'independent_reviewer':{'route':'Antigravity CLI','cli_version':'1.4.7','requested_model':'gemini-3.8-flash-high','actual_model_identity':'UNKNOWN (native JSON contains no model identifier; no fallback can be ruled in/out from identity metadata)','native_status':raw.get('status'),'conversation_id':raw.get('conversation_id'),'exit_code':0,'elapsed_seconds':dispatch['elapsed_seconds'],'returned_tokens':raw.get('usage'),'exact_sha_verdict':'PASS (text-semantic scope)','response_sha256':dispatch['response_sha256'],'stdout_sha256':dispatch['stdout_sha256'],'stderr_sha256':dispatch['stderr_sha256'],'prompt_sha256':dispatch['prompt_sha256'],'tool_event_evidence':'Native response envelope has fields conversation_id,status,response,duration_seconds,num_turns,usage; no tool-event field; prompt explicitly barred tool use.'},
 'adjudication':{'semantic_status':'PASS_TEXT_SEMANTIC','substantive_findings':0,'verified_scope':['official requirement mapping and document genre','title-blind distinction from 0131 and 0133','operational data collection and denominator logic','six synthetic batches and pooled math','primary-cause sums','confounder disclosure and no causal overclaim','HOLD/REJECT rules','SAMPLE/REAL boundary and replacement register','embedded chart values against text'],
   'nonblocking_admin_note':{'locator':'Table 1, row 文件版本／狀態','text':'The immutable as-built candidate says it had not yet received independent semantic review. That statement was true when the DOCX was built, but is now stale after this review. It is a volatile QA-status snapshot, not TTQS evidence content; candidate bytes were preserved to avoid a metadata-only rebuild. This receipt is the current review-status authority.'},
   'overall_candidate_state':'CANDIDATE; text-semantic scope PASS; formal acceptance NOT_GRANTED; REAL evidence UNKNOWN; no document mutation.'},
 'math_recalculation':math,'source_readback':source,
 'existing_technical_visual_qa':{'technical':'PASS','visual':'PASS','page_count':10,'all_10_pages_visually_inspected':True,'candidate_sha_bound':'e2f263c2c130d1939ebdaab1a253700935c54c8a26c937b8a77e7000a9a2d925'},
 'limits':['Reviewer model identity is UNKNOWN.','Semantic review is not formal Human acceptance.','Visual QA is a separate existing receipt; Antigravity reviewer did not claim to inspect rendered pages.','No REAL source material was provided.']}
(rev/'SEMANTIC_REVIEW_ADJUDICATION.json').write_text(json.dumps(adj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
status={'project_id':'TTQS_ONE','doc_id':'0132','requirement_id':'I19-E21','candidate_sha256':adj['candidate']['sha256'],'source_commit':adj['source_commit'],'independent_semantic_review':'PASS_TEXT_SEMANTIC','review_scope':'exact-SHA text semantic only; model identity UNKNOWN','technical_qa':'PASS','visual_qa':'PASS (existing receipt; 10/10 pages)','formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN','candidate_mutated':False,'sync_status':'PENDING_GITHUB_RAW_BYTE_READBACK'}
(rev/'INDEPENDENT_SEMANTIC_REVIEW_STATUS_0132_R01_20261026.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
readme='''# 0132 R01D exact-SHA semantic review package\n\n- Candidate: `0132_I19-E21_CANDIDATE_R01.docx`\n- Candidate SHA-256: `e2f263c2c130d1939ebdaab1a253700935c54c8a26c937b8a77e7000a9a2d925` (unchanged during review)\n- Requirement: `I19-E21`, doc_id `0132`, 157 index 145 / I19-L3 / official p.8; printed checkbox serial UNKNOWN.\n- Independent CLI text-semantic result: PASS on exact SHA. Requested model was `gemini-3.8-flash-high`; actual model identity UNKNOWN because the native envelope lacks an identity field. No Computer Use was invoked.\n- Technical and visual QA remain existing exact-SHA PASS receipts (10 pages, all inspected); this review does not replace them.\n- Formal acceptance is NOT_GRANTED; REAL evidence is UNKNOWN.\n- The DOCX has one now-stale as-built review-status sentence in Table 1; see adjudication. The artifact was not rewritten for a volatile status-only field.\n\nFiles preserve the exact prompt, source-bound input manifest, extracted candidate text, raw CLI stdout/stderr, original reviewer response, dispatch receipt, independent adjudication, and status.\n'''
(rev/'README.md').write_text(readme,encoding='utf-8',newline='\n')
for n in ['REVIEW_PROMPT.txt','INPUT_MANIFEST.json','0132_R01_EXACT_SHA_SEMANTIC_PAYLOAD_V2.txt','ANTIGRAVITY_STDOUT.txt','ANTIGRAVITY_STDERR.txt','DISPATCH_RESULT.json','REVIEWER_RESPONSE.md','SEMANTIC_REVIEW_ADJUDICATION.json','INDEPENDENT_SEMANTIC_REVIEW_STATUS_0132_R01_20261026.json','README.md']:
 p=rev/n
 print(f'{n}\t{p.stat().st_size}\t{h(p)}')
print('TOKEN_USAGE='+json.dumps(raw.get('usage'),ensure_ascii=False))