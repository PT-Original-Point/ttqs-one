from pathlib import Path
import hashlib,json
root=Path(r'E:\TTQS\_github_sync_0064')
base=root/'docs/ttqs-quality-20261016/quality-review/0075_R01'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
docx=base/'candidate/0075_R02.docx'; r01=base/'candidate/0075_R01.docx'; pdf=base/'evidence/0075_R02_word_render_ca81a479.pdf'; render=base/'evidence/render_word_R02'
body=base/'candidate/0075_R01_body.md'; register=base/'inputs/SYNTHETIC_REPLACEMENT_REGISTER_0075_R01.csv'
review=base/'evidence/semantic_review_receipt_R02.json'; visual=base/'evidence/visual_review_R02.json'; technical=base/'evidence/technical_review_R02.json'
sem=json.loads(review.read_text(encoding='utf-8')); vis=json.loads(visual.read_text(encoding='utf-8')); tech=json.loads(technical.read_text(encoding='utf-8'))
sem['non_blocking_note']='Reviewer suggests optional colocation of M2/M3 protocol details; the review states these requirements are present through sections 7, 9, and 10.2. No repair was required for the PASS verdict.'
review.write_text(json.dumps(sem,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
repair={
 'schema':'TTQS_ONE_0075_LAYOUT_REPAIR_R02.v1','document_id':'0075','requirement_id':'I17A-E03','official_checkbox_serial':'082',
 'predecessor':{'path':'candidate/0075_R01.docx','sha256':sha(r01),'status':'SUPERSEDED_LAYOUT_DEFECT'},
 'finding':'On Word-rendered page 15, the 10.1 pre-course checklist heading and its repeated header were stranded at the page foot without a body row; page 16 repeated the header and contained all rows.',
 'repair':'R02 builder sets keep-with-next on the specific 10.1 checklist header cell paragraphs; heading and header now move with the first body row to page 16.',
 'scope':'Layout-only; OOXML body-order text extraction is identical between R01 and R02.',
 'extracted_text_sha256':'8e2939355b5eedc7bf859b6b2b6884350a91bf27cd839312f8c152a80e6e948f',
 'final_candidate_sha256':sha(docx),'final_pages':21,'rebuild_justified':True,'remaining_layout_defects':'NONE_OBSERVED in all 21 rendered pages.'
}
(base/'evidence/layout_repair_R02.json').write_text(json.dumps(repair,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
status={
 'schema':'TTQS_ONE_CANDIDATE_STATUS.v1','project_id':'TTQS_ONE','document_id':'0075','requirement_id':'I17A-E03','official_checkbox_serial':'082','indicator':'17a',
 'candidate':{'revision':'R02','path':'candidate/0075_R02.docx','sha256':sha(docx),'status':'CANDIDATE_ONLY'},
 'quality':{'technical':'TECHNICAL_PASS','visual':'PASS_WITH_SCOPE','semantic':'PASS','semantic_reviewer':'OpenCode CLI v2.0.29 opencode/beam-free; separate session from Writer','blocking_findings':0,'pages_rendered_and_inspected':21,'register_rows':110},
 'remaining_scope':['Human print-device fidelity not tested.','Semantic reviewer read the exact text extraction bound to this DOCX SHA; reviewer did not independently recompute binary SHA.','Optional non-blocking reviewer suggestion: colocate M2/M3 protocol fields in their own tables; required details are cross-referenced in sections 7, 9, and 10.2.'],
 'formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN/HOLD','overall':'CANDIDATE_QA_PASS_WITH_SCOPE_NOT_FORMALLY_ACCEPTED',
 'source_hashes':{'body_sha256':sha(body),'replacement_register_sha256':sha(register),'technical_receipt_sha256':sha(technical),'visual_receipt_sha256':sha(visual),'semantic_receipt_sha256':sha(review),'pdf_sha256':sha(pdf),'rendered_pages':len(list(render.glob('page-*.png')))}
}
(base/'evidence/candidate_status_R02.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
readme=f'''# DOCX 0075 R02 — I17A-E03 / 官方勾選 082\n\n- 成品：candidate/0075_R02.docx\n- SHA-256：{sha(docx)}\n- 狀態：候選文件；技術 PASS、21 頁目視 PASS_WITH_SCOPE、OpenCode V2 beam-free 獨立語意 PASS。\n- 法人正式接受：NOT_GRANTED；真實活動及佐證：REAL=UNKNOWN/HOLD。\n- R02 只修復 R01 第 15 頁 10.1 表頭孤立的版面問題；R01/R02 正文抽取完全相同。\n- 全案例、問卷數據、計畫、時程、預算和量尺均為 SAMPLE/SYNTHETIC；110 列替換清冊列明真實資料替換及 HOLD 規則。\n- OpenCode reviewer 的非阻擋建議是把 M2/M3 的分散協定欄位放在同表；本次不為非必要排版改動重建。\n- 渲染 PDF、逐頁影像、原始 Writer/Reviewer CLI 回應及 SHA 收據均保留於本資料夾。\n\n詳見 evidence/candidate_status_R02.json、technical_review_R02.json、visual_review_R02.json、semantic_review_receipt_R02.json、layout_repair_R02.json。\n'''
(base/'README_0075_R02.md').write_text(readme,encoding='utf-8')
print(json.dumps({'docx_sha256':sha(docx),'r01_sha256':sha(r01),'repair_receipt':sha(base/'evidence/layout_repair_R02.json'),'status':status['overall'],'semantic_reviewer_session':sem['reviewer_session_id'],'formal_acceptance':'NOT_GRANTED'},ensure_ascii=False,indent=2))
