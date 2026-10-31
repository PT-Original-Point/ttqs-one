from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
Q=Path('docs/ttqs-quality-20261016/quality-review/0047_R08')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,o): Path(p).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
DOCX=Q/'candidate/0047_R08.docx'
packet=Q/'review/REVIEW_PACKET_R08.md'
prompt=Q/'review/REVIEW_PROMPT_R08.txt'
raw=Q/'review/opencode_v2_review_R01/stdout.raw.txt'
stderr=Q/'review/opencode_v2_review_R01/stderr.raw.txt'
answer=Q/'review/opencode_v2_review_R01/independent_semantic_review_R01.md'
response=answer.read_text(encoding='utf-8')
expected='b8cc8e4473e9cd7ad93f21c0cb9503865e683e3b802ac70577fbd8db3524d447'
if sha(DOCX)!=expected: raise AssertionError('candidate SHA changed after review')
if expected not in response: raise AssertionError('review output not bound to exact candidate SHA')
if 'Final overall verdict\n**PASS**' not in response: raise AssertionError('review overall PASS missing')
if any(x in response for x in ['**1. Correct document type and official mapping — PARTIAL**','**1. Correct document type and official mapping — FAIL**']): raise AssertionError('criterion 1 failed')
if 'Font-floor compliance (body ≥10.5 pt / table ≥9.5 pt) is therefore **UNKNOWN**.' not in response: raise AssertionError('review scope limit missing')
if 'did **not** view a PNG or inspect any pixels/rendering' not in response: raise AssertionError('review visual scope limit missing')
if len(stderr.read_bytes())!=0: raise AssertionError('review stderr is non-empty; inspect manually')

exe=Path(r'C:/Users/J/AppData/Local/Programs/@opencode-aidesktop/resources/opencode-cli.exe')
rec={
 'project_id':'TTQS_ONE','doc_id':'0047','requirement_id':'I10-E02','candidate_revision':'R08',
 'candidate_sha256':expected,'candidate_sha256_our_readback_after_review':sha(DOCX),
 'review_route':'OpenCode CLI V2, headless run; no UI or Computer Use',
 'cli_path':str(exe),'cli_version':'2.0.29','cli_sha256':'8c5725848e2fc5867410f1bcaa9ba8e21f74c79180a9d0feb40bf1b75318e940',
 'requested_model':'opencode/deepseek-v4.1-flash-free','runtime_model_identity':'NOT_RETURNED_BY_CLI_OUTPUT',
 'provider_model_id_readback':'opencode models listed this exact model before run; runtime inference backend not independently attested',
 'open_code_session_id':'ses_eb8bb1cfdffeZWgrCrnyzp63It','cli_exit_code':0,
 'started_utc':'2026-10-17T00:30:58.8333733Z','ended_utc':'2026-10-17T00:32:32.1027505Z',
 'packet_path':'review/REVIEW_PACKET_R08.md','packet_sha256':sha(packet),
 'prompt_path':'review/REVIEW_PROMPT_R08.txt','prompt_sha256':sha(prompt),
 'stdout_path':'review/opencode_v2_review_R01/stdout.raw.txt','stdout_sha256':sha(raw),'stdout_bytes':raw.stat().st_size,
 'stderr_path':'review/opencode_v2_review_R01/stderr.raw.txt','stderr_sha256':sha(stderr),'stderr_bytes':0,
 'review_response_path':'review/opencode_v2_review_R01/independent_semantic_review_R01.md','review_response_sha256':sha(answer),
 'reported_verdict':'PASS','verdict_layer':'INDEPENDENT_SEMANTIC_REVIEW_OF_SUPPLIED_PACKET_ONLY',
 'reviewer_scope_limits':['Reviewer transcribed candidate/PDF hashes from supplied packet and did not recompute binary hashes.','Reviewer did not open original DOCX, inspect rendered PNG pixels, measure fonts, or access the official source PDF/runtime source map.','Reviewer did not verify runtime model identity beyond the requested model string.'],
 'criteria':'10/10 PASS according to the independent response; reviewer logged non-blocking terminology, criterion-label, unexercised-threshold, and two-year-sample observations.',
 'no_tool_or_filesystem_access_observed':'CLI stream contains only a text response; no tool call event was emitted.',
 'candidate_unchanged_during_review':True,'formal_acceptance':'NOT_CLAIMED',
 'created_utc':datetime.now(timezone.utc).isoformat()
}
dump(Q/'review/opencode_execution_receipt_R01.json',rec)

inventory=Path(r'E:/TTQS/TTQS_ONE_CODEX_RUNTIME/MASTER/SOURCE_CHECK_20261004/checkbox_inventory.json')
inv=json.loads(inventory.read_text(encoding='utf-8'))
boxes={b.get('source_box_id'):b for b in inv['boxes']}
expected_boxes={'P03-B07':7,'P03-B09':9,'P03-B10':10}
source_check={'source_inventory_sha256':sha(inventory),'source_blueprint_sha256':'406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e','verified_rows':{}}
for bid,order in expected_boxes.items():
 b=boxes[bid]
 if b.get('page')!=3 or b.get('page_checkbox_order')!=order: raise AssertionError(f'inventory box mismatch {bid}')
 source_check['verified_rows'][bid]={'page':b['page'],'page_checkbox_order':b['page_checkbox_order'],'extracted_block':b.get('extracted_block'),'other':b.get('other')}
validation={
 'project_id':'TTQS_ONE','doc_id':'0047','requirement_id':'I10-E02','checkbox_sequence':48,
 'candidate_sha256':expected,'review_status':'PASS_SEMANTIC_ONLY',
 'review_response_sha256':sha(answer),'cli_receipt_sha256':sha(Q/'review/opencode_execution_receipt_R01.json'),
 'official_neighbor_boxes_readback':source_check,
 'cross_checks_by_local_integrator':{
  'candidate_sha_recomputed_after_review':'PASS',
  'R08_visual_technical_QA':'PASS; all 8 page PNGs directly inspected locally; this is not an independent reviewer pixel audit',
  'reviewer_exact_sha_scope':'PASS_WITH_LIMITATION; report quotes exact SHA supplied in the packet; reviewer did not hash binary',
  '0045_P03_B07_and_0048_P03_B10':'PASS; verified against official source checkbox inventory SHA above',
  'reviewer_scope_limit_preserved':'PASS; no claim of independent pixel/font/source-PDF review',
  'formal_acceptance':'NOT_CLAIMED'
 },
 'independent_review_nonblocking_observations':[
  'same fulfillment metric uses several Chinese labels; reviewers found mapping inferable but terminology varies',
  'short criterion labels and longer criterion labels are not explicitly keyed in the body',
  'the >=4.00 but incomplete threshold branch is described but not exercised by the two sample cases',
  'only two synthetic years are shown; they are not represented as actual association years',
  'reviewer says register fact keys are external sidecar rather than embedded in report body'
 ],
 'disposition':'No material FAIL/PARTIAL finding. Retain R08; do not rebuild for non-blocking observations. Formal association acceptance remains separate.'
}
dump(Q/'review/review_validation_R01.json',validation)

qa_path=Q/'evidence/R08_VISUAL_TECHNICAL_QA.json'
qa=json.loads(qa_path.read_text(encoding='utf-8'))
qa['independent_semantic_review']='PASS_SEMANTIC_ONLY exact candidate SHA; OpenCode CLI V2 review of the exact-SHA supplied packet; runtime model identity not returned; no pixels/font/source-PDF review by that reviewer.'
qa['independent_semantic_review_response_sha256']=sha(answer)
qa['formal_acceptance']='NOT_CLAIMED; candidate remains SAMPLE/SYNTHETIC and not association-approved.'
dump(qa_path,qa)

readme='''# 0047 R08 review package\n\n- Candidate DOCX: `candidate/0047_R08.docx`\n- Exact SHA-256: `'''+expected+'''`\n- Official mapping: DOCX 0047 = I10-E02 = checkbox 048 / P03-B09 (page 3, checkbox order 9).\n- Revision R08 corrects one simplified-Chinese character in the negative-neighbor heading. It leaves all numeric content, tables and sample values unchanged.\n- Candidate status: CANDIDATE ONLY; no Human formal acceptance, association approval, real event, contract, supplier, signature, or real outcome is claimed. All 25 fact IDs are SAMPLE/SYNTHETIC.\n- Visual/technical QA: 8-page PDF and 8 PNGs; every page was directly inspected. DOCX CRC, Word parsing, 25-row register, formula checks, 10.5 pt body and 9.5 pt table direct-size floors pass. Page 8 contains the complete final scale/checkpoint section; it is not blank.\n- Independent semantic review: PASS for 10 criteria within the supplied packet, exact candidate SHA as stated. Review output: `review/opencode_v2_review_R01/independent_semantic_review_R01.md`; raw CLI event stream and stderr are preserved beside it. The reviewer did not hash the binary, view page pixels, measure fonts or access the external source PDF; these limitations are retained. OpenCode v2.0.29 CLI requested `opencode/deepseek-v4.1-flash-free`; provider runtime model identity was not returned.\n- The reviewer logged minor non-blocking wording/label consistency items and the two-year synthetic sample limit. These are disclosed in `review/review_validation_R01.json`; no additional rebuild is justified by those comments.\n- Official neighbor boxes 0045/P03-B07 and 0048/P03-B10 have been independently confirmed against the official inventory in `evidence/REVIEW_INPUT_MANIFEST_R08.json` and `review/review_validation_R01.json`.\n- R06 reviewer history remains PARTIAL for missing named neighbor boundaries; R07 added the boundary text; R08 fixes the one-character heading defect.\n'''
(Q/'README.md').write_text(readme,encoding='utf-8')
progress={
 'project_id':'TTQS_ONE','doc_id':'0047','requirement_id':'I10-E02','official_checkbox_sequence':48,'candidate_revision':'R08',
 'candidate_path':'candidate/0047_R08.docx','candidate_sha256':expected,'candidate_status':'CANDIDATE_ONLY',
 'visual_technical':'PASS_LOCAL_DIRECT_8_PAGE_VISUAL_AND_TECHNICAL_CHECKS',
 'independent_semantic_review':'PASS_SEMANTIC_ONLY exact SHA; OpenCode CLI V2; packet-scope limitations retained',
 'synthetic_register':'25/25 SAMPLE/SYNTHETIC facts with locators and replacement actions',
 'formal_acceptance':'NOT_GRANTED_NOT_REQUESTED',
 'antigravity_dispatch':'NOT_ATTEMPTED; route paused by existing 0044 incident after four denials/three repairs',
 'next_action':'Synchronize candidate and review evidence to existing GitHub PR #92 branch with exact SHA readback; then continue next lawful READY document.',
 'updated_utc':datetime.now(timezone.utc).isoformat()
}
dump(Q/'PROGRESS_R08.json',progress)

# Refresh manifest after review; it lists each package file other than itself.
files=[]
for p in sorted(Q.rglob('*')):
 if p.is_file() and p.name!='REVIEW_INPUT_MANIFEST_R08.json':
  files.append({'path':str(p.relative_to(Q)),'sha256':sha(p),'bytes':p.stat().st_size})
manifest={'project_id':'TTQS_ONE','doc_id':'0047','revision':'R08','candidate_sha256':expected,'rendered_pdf_sha256':sha(Q/'evidence/render_R08/0047_R08.pdf'),'source_blueprint_file_sha256':'406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e','source_inventory_file_sha256':sha(inventory),'register_count':25,'page_count':8,'review_status':'PASS_SEMANTIC_ONLY_WITH_DECLARED_SCOPE','review_response_sha256':sha(answer),'files':files}
dump(Q/'evidence/REVIEW_INPUT_MANIFEST_R08.json',manifest)
print(json.dumps({'candidate_sha256':sha(DOCX),'review_verdict':'PASS_SEMANTIC_ONLY','review_response_sha256':sha(answer),'inventory_rows_verified':list(source_check['verified_rows']),'file_count_manifest':len(files),'manifest_sha256':sha(Q/'evidence/REVIEW_INPUT_MANIFEST_R08.json')},ensure_ascii=False,indent=2))