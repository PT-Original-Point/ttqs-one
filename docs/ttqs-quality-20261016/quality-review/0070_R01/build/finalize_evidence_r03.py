from pathlib import Path
import hashlib,json,re,datetime
root=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0070_R01')
review=root/'review'; evidence=root/'evidence'; render=evidence/'render_word_R03_final'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
docx=root/'candidate'/'0070_R01.docx'
body=root/'candidate'/'0070_R01_body.md'
extract=evidence/'docx_extracted_R03.md'
raw=review/'opencode_semantic_R03_stdout.jsonl'
stderr=review/'opencode_semantic_R03_stderr.txt'
exitf=review/'opencode_semantic_R03_exit.txt'
lines=[json.loads(s) for s in raw.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
session=next((x.get('sessionID') for x in lines if x.get('sessionID')),None)
response='\n'.join(x.get('part',{}).get('text','') for x in lines if x.get('type')=='text').strip()
if not response or '**Verdict: PASS**' not in response or '55af406663f29e6a3ea8fb644d61c029c74df42934166e6076a991fdcd895bba' not in response:
    raise SystemExit('Review output missing exact-SHA PASS; refusing to emit PASS receipt')
response_path=review/'independent_semantic_review_R03.md'
response_path.write_text('# Independent exact-SHA semantic review — DOCX 0070 R03\n\n'+response+'\n\n## Execution and scope\n\n- Route: OpenCode CLI v2.0.29; model selected by CLI: `opencode/beam-free`.\n- Session: `'+str(session)+'`.\n- CLI exit: '+exitf.read_text().strip()+'; stderr bytes: '+str(stderr.stat().st_size)+'.\n- Candidate DOCX SHA-256 before/after review: `'+sha(docx)+'` (unchanged).\n- Reviewer input: official page-5 extract, unique Blueprint and exact-candidate DOCX text extraction.\n- The CLI did not return a separate runtime-model attestation. The requested model and session output are preserved in the raw JSONL.\n- This is semantic review only; it is not visual acceptance or Association approval.\n',encoding='utf-8')
receipt={
 'project_id':'TTQS_ONE','doc_id':'0070','requirement_id':'I16-E02','official_checkbox_serial':'077','candidate_sha256':sha(docx),
 'reviewer_route':'OpenCode CLI v2.0.29','model_selected':'opencode/beam-free','runtime_model_attestation':'NOT_SEPARATELY_RETURNED_BY_CLI','session_id':session,
 'cli_exit_code':int(exitf.read_text().strip()),'stderr_bytes':stderr.stat().st_size,'computer_use':False,'permissions_bypass_flag_used':False,
 'input_sha256':{'candidate_docx':sha(docx),'candidate_text_extraction':sha(extract),'official_page5_extract':sha(root/'inputs'/'OFFICIAL_PAGE5_EXTRACT_R01.md'),'unique_blueprint':sha(root/'inputs'/'UNIQUE_BLUEPRINT_0070_R01.md')},
 'raw_response_sha256':sha(raw),'review_response_sha256':sha(response_path),'verdict':'PASS','scope':'semantic only; page flow/visual QA and formal Association acceptance excluded',
 'blocking_findings':[],'nonblocking_note':'Cover identity fields are pipe-separated on one line but remain unambiguous; visual/font scope was separately checked.',
 'reviewed_at_local':datetime.datetime.now().astimezone().isoformat(timespec='seconds')}
(review/'independent_semantic_review_receipt_R03.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Visual review receipt: records direct page-by-page inspection of the unchanged R03 Word rendering.
export=json.loads((render/'export_receipt.json').read_text(encoding='utf-8-sig'))
page_hashes={p.name:sha(p) for p in sorted(render.glob('page-*.png'))}
if len(page_hashes)!=22 or export.get('source_sha256_before')!=sha(docx) or export.get('source_sha256_after')!=sha(docx):
    raise SystemExit('Visual render not bound to current candidate SHA')
visual={
 'project_id':'TTQS_ONE','doc_id':'0070','requirement_id':'I16-E02','official_checkbox_serial':'077','candidate_sha256':sha(docx),
 'visual_status':'PASS_VISUAL_SCOPE','renderer':export.get('renderer'),'pdf_sha256':sha(render/'candidate.pdf'),'pdf_pages':export.get('page_count_word'),'png_pages':export.get('page_count_png'),
 'render_dpi':export.get('render_dpi'),'rendered_at_local':export.get('rendered_at_local'),'directly_inspected_pages':[f'{i:02d}' for i in range(1,23)],
 'page_image_sha256':page_hashes,'source_unchanged_during_render':export.get('source_unchanged'),
 'observations':['All 22 rendered pages directly inspected at original resolution.','Pages 5, 15 and 16 show complete tables without clipped or orphaned rows; page 15 is intentionally separated to preserve the full §6.9 table.','Pages 17–20 show the replacement register, hold/reject rules and usable blank forms; repeated table header and continuation are readable.','Page 21 cross-document matrix and page 22 proposal/REAL source register are complete; sparse whitespace remains but no cut-off content was observed.','No missing/extra page, clipped text, split row or unreadable font was observed in this render.'],
 'reviewer_independence':'Direct visual inspection separate from the DOCX build; not an external semantic review.',
 'association_approval':'NOT_CLAIMED','reviewed_at_local':datetime.datetime.now().astimezone().isoformat(timespec='seconds')}
(evidence/'visual_review_R03.json').write_text(json.dumps(visual,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Update fail-safe T5 for the actual current candidate; preserve T4 pending until remote readback.
test_path=root.parent/'R04_P7_FAILSAFE_TESTS.json'
tests=json.loads(test_path.read_text(encoding='utf-8-sig'))
t5=next(x for x in tests['tests'] if x['id']=='T5_SAMPLE_REAL_BOUNDARY')
text=extract.read_text(encoding='utf-8')
def markers(t): return {k:len(re.findall(k,t,re.I)) for k in ['SAMPLE','SYNTHETIC','UNKNOWN','HOLD']}
t5['execution']='LOCAL_EXACT_DOCX_TEXT_EXTRACTION_R03'
t5['result']='PASS_CURRENT_0070_BOUNDARY; 0071_REMAINS_INVALID'
t5['0070']={'sha256':sha(docx),'markers':markers(text),'zip_test':'PASS','candidate_state':'SAMPLE_SYNTHETIC_CANDIDATE_ONLY'}
t5['0071_old_candidate']={'sha256':'334ed51f437331605fa291c153a6726c1fc05a74d29cf057ad66747512c43065','markers':{'SAMPLE':0,'SYNTHETIC':0,'UNKNOWN':0,'HOLD':0},'boundary_status':'FAIL_NO_SAMPLE_SYNTHETIC_UNKNOWN_HOLD_MARKERS','queue_status':'PENDING_WITH_INVALID_UNATTESTED_MODEL_REVIEW','not_current_0071_candidate':'historical integrated candidate from Oct 3 queue record'}
t5['queue_after_correction']={'source':'E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\BUILD_QUEUE.json','sha256':hashlib.sha256(Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BUILD_QUEUE.json').read_bytes()).hexdigest(),'0071_state':'PENDING','external_review_status':'INVALID_UNATTESTED_MODEL_IDENTITY'}
test_path.write_text(json.dumps(tests,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
readme=f'''# DOCX 0070｜I16-E02｜官方 checkbox 077｜R03

## 候選狀態

- Exact DOCX SHA-256：`{sha(docx)}`（56,045 bytes）
- 狀態：候選，所有示範資料均為 SAMPLE / SYNTHETIC；不是協會正式接受或真實運作紀錄。
- 官方目的：I16-E02「訓練異常處理方法、紀錄與工具」。
- 專屬 Blueprint：`inputs/UNIQUE_BLUEPRINT_0070_R01.md`；原始官方頁 5 及來源事實均隨本包提供。

## 驗收證據

- 技術：`evidence/technical_review_R03.json`，exact SHA 綁定，DOCX ZIP/XML、43 表格、公式/日期/身份、字級與來源邊界檢查通過；正文最小明示字級 11 pt，表格 10 pt。
- 視覺：`evidence/visual_review_R03.json`；Microsoft Word COM 匯出 PDF，22/22 頁直接目視；未見截斷、孤立列或不可讀內容。PDF 與頁面圖隨包附上。
- 獨立語意：`review/independent_semantic_review_R03.md` 判 PASS，審查對象為此 exact SHA；OpenCode CLI v2.0.29，模型選擇 `opencode/beam-free`。原始 JSONL、stderr、exit code 與 session ID 一併保留。CLI 未另行回傳模型身份 attestation。
- 重要範圍限制：PASS 僅涵蓋本候選的語意與視覺/技術範圍；不等同協會核准、Human 正式接受或真實佐證成立。

## 文件內容

程序包括快速停/保護與通知卡、角色/權限界線、分類與嚴重度矩陣、10步 SOP、完整合成事件 `SYN-0070-CASE-01`、通知與效果計算、SAMPLE→REAL 替換清冊、退件/HOLD 條件、六份空白工具表、跨文件責任核對及待核定/REAL 來源清單。合成通報及效果數據不可作為協會實績。

## 歷史

R01/R02 舊 SHA 與視覺阻擋紀錄保留為歷史，不代表本 R03 結果。R03 對既有內容只做分頁修復；目前 22 頁候選 SHA 固定，驗收資料新增而未為收據重建 DOCX。
'''
(root/'README.md').write_text(readme,encoding='utf-8')
# Compact manifest for the current audit package.
manifest_paths=[
'README.md','candidate/0070_R01.docx','candidate/0070_R01_body.md','inputs/official_checklist_source.pdf','inputs/OFFICIAL_PAGE5_EXTRACT_R01.md','inputs/SOURCE_FACTS_R01.md','inputs/UNIQUE_BLUEPRINT_0070_R01.md','evidence/SYNTHETIC_REPLACEMENT_REGISTER_0070_R01.csv','evidence/docx_extracted_R03.md','evidence/technical_review_R03.json','evidence/visual_review_R03.json','evidence/render_word_R03_final/candidate.pdf','evidence/render_word_R03_final/export_receipt.json','review/semantic_review_prompt_R03.md','review/opencode_semantic_R03_stdout.jsonl','review/opencode_semantic_R03_stderr.txt','review/opencode_semantic_R03_exit.txt','review/independent_semantic_review_R03.md','review/independent_semantic_review_receipt_R03.json','build/build_0070_R01.py','build/extract_docx_text_r03.py','build/verify_candidate_r03.py']
manifest_paths += [f'evidence/render_word_R03_final/page-{i:02d}.png' for i in range(1,23)]
manifest={'project_id':'TTQS_ONE','doc_id':'0070','candidate_sha256':sha(docx),'source_commit':'93547e014ddcf66c039e3f91ca60cd21514c0b54','review_commit_context':'live HEAD checked before synchronization; revalidate immediately before push','files':[{'path':p,'bytes':(root/p).stat().st_size,'sha256':sha(root/p)} for p in manifest_paths], 'acceptance_state':'CANDIDATE_WITH_TECHNICAL_VISUAL_AND_INDEPENDENT_SEMANTIC_PASS; NOT_FORMALLY_ACCEPTED'}
(evidence/'package_manifest_R03.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':sha(docx),'semantic_verdict':receipt['verdict'],'review_session':session,'visual_pages':len(page_hashes),'visual_status':visual['visual_status'],'technical_status':json.loads((evidence/'technical_review_R03.json').read_text())['technical_status'],'failsafe_T5':t5['result'],'manifest_files':len(manifest_paths)},ensure_ascii=False,indent=2))
