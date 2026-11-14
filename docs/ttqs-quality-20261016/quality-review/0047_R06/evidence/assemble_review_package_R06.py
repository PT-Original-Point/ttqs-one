from __future__ import annotations
import hashlib, json, shutil, zipfile
from pathlib import Path
from docx import Document

ROOT=Path(__file__).resolve().parents[1]
QUALITY=ROOT.parent
WORKTREE=ROOT.parents[3]
R01=QUALITY/'0047_R01'
R02=QUALITY/'0047_R02'
R03=QUALITY/'0047_R03'
R04=QUALITY/'0047_R04'
R05=QUALITY/'0047_R05'
R06=ROOT
RUNTIME=Path(r'E:/TTQS/TTQS_ONE_CODEX_RUNTIME')
BLUEPRINT=RUNTIME/'CONTROL'/'BLUEPRINT_CURRENT.jsonl'
INVENTORY=RUNTIME/'MASTER'/'SOURCE_CHECK_20261004'/'checkbox_inventory.json'
HIST=R01/'evidence'/'historical_build_receipt_0047.json'

def sha(p:Path)->str: return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p:Path,obj):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Exact official Blueprint source row and checkbox source object.
blue_raw=BLUEPRINT.read_bytes()
blue_line=None
for line in blue_raw.splitlines(keepends=True):
 try: item=json.loads(line)
 except Exception: continue
 if item.get('deliverable_id')=='0047':
  blue_line=line; blue_obj=item; break
if blue_line is None: raise RuntimeError('0047 Blueprint row not found')
blue_out=R06/'inputs'/'UNIQUE_BLUEPRINT_0047.jsonl'
blue_out.parent.mkdir(parents=True,exist_ok=True)
blue_out.write_bytes(blue_line)
inv_raw=INVENTORY.read_bytes(); inv=json.loads(inv_raw)
boxes=inv['boxes']; selected=boxes[47]
if selected.get('source_box_id')!='P03-B09' or selected.get('page')!=3 or selected.get('page_checkbox_order')!=9:
 raise AssertionError('official checkbox sequence 048 mapping mismatch')
official_text=blue_obj.get('official_requirement_text')
if blue_obj.get('requirement_id')!='I10-E02' or '課程之評估' not in official_text:
 raise AssertionError('Blueprint mapping mismatch')
checkbox={
 'official_checkbox_sequence':48,'array_index_zero_based':47,'source_box_id':selected['source_box_id'],
 'page':selected['page'],'page_checkbox_order':selected['page_checkbox_order'],
 'official_text_from_blueprint':official_text,'inventory_extracted_block':selected.get('extracted_block'),
 'inventory_other_flag':selected.get('other'),
 'inventory_path':'E:/TTQS/TTQS_ONE_CODEX_RUNTIME/MASTER/SOURCE_CHECK_20261004/checkbox_inventory.json',
 'inventory_file_sha256':sha(INVENTORY),'inventory_declared_sha256':inv.get('sha256'),
 'blueprint_path':'E:/TTQS/TTQS_ONE_CODEX_RUNTIME/CONTROL/BLUEPRINT_CURRENT.jsonl',
 'blueprint_file_sha256':sha(BLUEPRINT),'blueprint_selected_line_sha256_including_original_crlf':hashlib.sha256(blue_line).hexdigest(),
 'blueprint_selected_line_sha256_without_line_ending':hashlib.sha256(blue_line.rstrip(b'\\r\\n')).hexdigest(),
 'historical_build_receipt_row_sha256_unreconciled':json.loads(HIST.read_text(encoding='utf-8')).get('blueprint_row_hash'),
 'mapping_status':'DOCX 0047 = I10-E02 = official checkbox 048 (P03-B09); document ID and checkbox serial are distinct.'
}
dump(R06/'inputs'/'official_checkbox_048.json',checkbox)

# Synthetic replacement register, with precise rendered page/table/field locators.
hist=json.loads(HIST.read_text(encoding='utf-8'))
facts=hist['synthetic_facts']
if len(facts)!=25: raise AssertionError(f'expected 25 synthetic facts, got {len(facts)}')
loc={
 '0047-FE1-001':'p.1, document control line: version/status/effective date.',
 '0047-FE1-002':'p.1 document status; pp.5-6 annual case tables, 資料狀態 column.',
 '0047-FE1-003':'p.7, 評量方式與判定 > 評分量尺 table.',
 '0047-FE1-004':'pp.5 and 7, 評分構面與示範分數 / 判斷依據 tables.',
 '0047-FE1-005':'pp.2 and 5, 指標定義及計算方法; 加權計算與總分 table.',
 '0047-FE1-006':'pp.2 and 7, score-interpretation rule and 示範判讀門檻 bullets.',
 '0047-FE1-007':'pp.4-5 and 7, data dictionary; 履約檢核結果與判讀; 履約檢核項目.',
 '0047-FE1-008':'pp.2 and 5, 資料來源、樣本與納入排除; 年度案例明細 tables.',
 '0047-FE1-009':'p.5, 年度案例明細與逐步計算 > 評分構面與示範分數, first case period.',
 '0047-FE1-010':'p.5, same table, first case label.',
 '0047-FE1-011':'p.5, 評分構面與示範分數, 2024 first case four score cells.',
 '0047-FE1-012':'p.5, 履約檢核結果與判讀, 2024 completed/due cell.',
 '0047-FE1-013':'pp.2 and 5, weighted calculation narrative and 2024 weighted score/rate cells.',
 '0047-FE1-014':'pp.3 and 5, 發現與證據強度; 2024 case judgment cell.',
 '0047-FE1-015':'p.5, 評分構面與示範分數, second case period.',
 '0047-FE1-016':'p.5, same table, second case label.',
 '0047-FE1-017':'p.5, 評分構面與示範分數, 2025 second case four score cells.',
 '0047-FE1-018':'p.5, 履約檢核結果與判讀, 2025 completed/due cell.',
 '0047-FE1-019':'pp.2 and 5, weighted calculation narrative and 2025 weighted score/rate cells.',
 '0047-FE1-020':'pp.3 and 5, summary/trend reading; 2025 case judgment cell.',
 '0047-FE1-021':'pp.3 and 6, combined calculations and 分群比較及差距優先排序矩陣.',
 '0047-FE1-022':'p.3, 發現、原因與證據強度; 結論與可執行建議.',
 '0047-FE1-023':'p.6, 結論、證據、建議、責任與追蹤指標 table, sample deadline cells.',
 '0047-FE1-024':'pp.1, 3, and 6, user/role descriptions and sample responsibility-role cells.',
 '0047-FE1-025':'pp.3 and 6, conclusion/actions and follow-up tracking table.'
}
register=[]
for f in facts:
 if f.get('source_status')!='SAMPLE/SYNTHETIC': raise AssertionError(f"fact not synthetic: {f.get('fact_id')}")
 item=dict(f)
 item['document_locator']=loc[item['fact_id']]
 item['real_replacement_required']=True
 item['real_replacement_acceptance']='Replace only from a traceable original; verify by the responsible role; recompute linked totals and judgments; retain source location and reviewer evidence; keep sample labels on any facts not replaced.'
 register.append(item)
dump(R06/'register'/'SYNTHETIC_REPLACEMENT_REGISTER_0047_R06.json',{
 'doc_id':'0047','candidate_revision':'R06','candidate_sha256':'be27651b17ac2759b6eab5391fb330df6b68a978d41c47fe618fef9f3a6c0976',
 'source_receipt':'../0047_R01/evidence/historical_build_receipt_0047.json','source_receipt_sha256':sha(HIST),
 'count':len(register),'all_source_status':'SAMPLE/SYNTHETIC','central_register_sync':'NOT_CLAIMED','facts':register
})

# R05 and R06 layout receipts.
sha_r04=sha(R04/'candidate'/'0047_R04.docx'); sha_r05=sha(R05/'candidate'/'0047_R05.docx'); sha_r06=sha(R06/'candidate'/'0047_R06.docx')
if sha_r06!='be27651b17ac2759b6eab5391fb330df6b68a978d41c47fe618fef9f3a6c0976': raise AssertionError('R06 exact SHA drift')
r05_receipt={
 'doc_id':'0047','revision':'R05','status':'SUPERSEDED_LAYOUT_FAIL_HISTORY','parent_revision':'R04','parent_sha256':sha_r04,
 'candidate':'0047_R05/candidate/0047_R05.docx','candidate_sha256':sha_r05,
 'change_scope':'PRESENTATION_ONLY_THRESHOLD_TABLE_TO_BULLETS','body_values_changed':False,
 'layout_result':'FAIL','rendered_page_count':8,'visual_inspection':'All 8 pages inspected directly; pages 1-7 readable and complete; page 8 blank.',
 'located_defect':'R05 placed all content on page 7 but retained the empty terminal paragraph after the replaced table, which overflowed to a wholly blank page 8.',
 'disposition':'Preserved as failed iteration history; R06 removes only that empty terminal paragraph. No semantic acceptance transfers.'
}
dump(R05/'evidence'/'R05_LAYOUT_REPAIR_RECEIPT.json',r05_receipt)
pdf=R06/'evidence'/'render_R06'/'0047_R06.pdf'
pages=sorted((R06/'evidence'/'render_R06').glob('page-*.png'),key=lambda p:int(p.stem.split('-')[1]))
if len(pages)!=7: raise AssertionError(f'expected 7 rendered pages, got {len(pages)}')
r06_receipt={
 'doc_id':'0047','revision':'R06','status':'CANDIDATE_ONLY','candidate_sha256':sha(R06/'candidate'/'0047_R06.docx'),
 'parent_revision':'R05','parent_sha256':sha_r05,'change_scope':'PRESENTATION_ONLY_REMOVE_OVERFLOWING_EMPTY_TERMINAL_PARAGRAPH',
 'reason':'R05 had a wholly blank page 8 caused by the empty paragraph after the final threshold bullet; R06 removes that empty paragraph only.',
 'render_engine':'documents skill render_docx.py with project-bundled LibreOffice',
 'rendered_pdf':'evidence/render_R06/0047_R06.pdf','rendered_pdf_sha256':sha(pdf),'rendered_page_count':len(pages),
 'direct_visual_inspection':{'scope':'every page 1 through 7','result':'PASS','pages':[{'page':i+1,'image':p.name,'sha256':sha(p),'observed':'Readable text and tables; no clipping, overlap, broken table, orphan table row, empty page, or split heading.'} for i,p in enumerate(pages)]},
 'layout_findings_resolved':['Threshold summary is a compact four-item list and all four conditions remain legible.','Data dictionary continues to page 5 with repeated header.','Annual example tables and comparison/action tables are readable.','No trailing blank page remains.'],
 'calculation_recheck':{'case_2024_weighted_score':'(4+4+3+2)/4=3.25','case_2024_fulfillment':'3/4=75.0%','case_2025_weighted_score':'(4+4+4+4)/4=4.00','case_2025_fulfillment':'4/4=100.0%','combined_fulfillment':'(3+4)/(4+4)=87.5%','mean_score':'(3.25+4.00)/2=3.625, displayed 3.63','score_change':'4.00-3.25=0.75','rate_change':'100.0%-75.0%=25.0 percentage points'},
 'body_and_table_values_changed_in_R06':False,'text_change_in_R05_representation':'Only duplicated threshold table was represented as four bullets; threshold predicates and outcomes remain unchanged.',
 'font_check':'Explicit body text minimum 10.5 pt; table text minimum 9.5 pt; inherited-size runs are styled by paragraph/style and visually readable.',
 'independent_semantic_review':'PENDING exact R06 SHA; R01 review applies only to R01 exact SHA.',
 'formal_acceptance':'NOT CLAIMED; all data remain SAMPLE/SYNTHETIC.'
}
dump(R06/'evidence'/'R06_VISUAL_TECHNICAL_QA.json',r06_receipt)
# Verify ZIP CRC and Word opens, plus sample register has 25 complete unique records.
with zipfile.ZipFile(R06/'candidate'/'0047_R06.docx') as z:
 bad=z.testzip()
 if bad: raise AssertionError(f'DOCX zip integrity failed at {bad}')
Document(R06/'candidate'/'0047_R06.docx')
if len({x['fact_id'] for x in register})!=25: raise AssertionError('fact IDs are not unique')

# Record this hourly-command application as partial; 0036/0043 and remaining command items are not marked done.
command={
 'project_id':'TTQS_ONE','goal_thread_id':'01a14098-b269-79e3-b07c-56e96557fe07',
 'source_repository':'PT-Original-Point/ttqs-one','branch':'work/ttqs-one-document-quality-contract-20261016',
 'source_command_path':'docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md',
 'historical_anchor_commit':'92d3d97acbd3c0a8c4dcad66e66468f5cafc3536',
 'live_branch_head_verified_before_build':'688ffdd76623798912bcdd5b4925a2f69c40b088',
 'source_command_blob_sha':'70449889fd464106fe204496004bee13018d4a51',
 'DISCOVERED':{'status':'PASS','evidence':'Full current 06 command read from GitHub at verified live head; exact blob SHA recorded.'},
 'APPLICABLE':{'status':'PASS','evidence':'Human-authorized reversible candidate QA/sync; no formal acceptance or protected source change.'},
 'APPLIED':{'status':'PARTIAL','evidence':'0047 R04-R06 layout defect was isolated; R06 candidate and exact-SHA visual/technical evidence created. 0036 visual supplement and latest 0043 reconciliation remain outstanding.'},
 'VERIFIED':{'status':'PARTIAL','evidence':'R06 exact candidate SHA rendered and all seven pages directly inspected; no independent semantic verdict yet; this does not verify the entire 06 command.'},
 'BLOCKED':{'status':'NONE_FOR_0047_LAYOUT','evidence':'No current layout blocker; semantic independent review is in progress.'},
 'candidate_sha256':sha(R06/'candidate'/'0047_R06.docx'),
 'automation':'Existing automation unchanged: ttqs-one-hourly-quality-goal-resume; no second scheduler created.',
 'scope_remaining':['Independent semantic review of 0047 R06 exact SHA','0036 R08/R12 visual-scope reconciliation without rebuilding R08','Fresh latest-state reconciliation and recovery of 0043','Other named stable candidates and remaining 06 findings'],
 'candidate_state':'CANDIDATE_ONLY_SAMPLE_SYNTHETIC_NOT_HUMAN_ACCEPTED'
}
dump(R06/'evidence'/'COMMAND_06_APPLICATION.json',command)

readme='''# 0047 R06 review package\n\n## Identity and status\n\n- Document ID: 0047\n- Official requirement: I10-E02\n- Official checkbox: sequence 048, source box P03-B09, page 3, page order 9\n- Genre: analysis/evaluation report\n- Candidate DOCX SHA-256: `'''+sha(R06/'candidate'/'0047_R06.docx')+'''`\n- State: CANDIDATE ONLY. All annual values, labels, ratings, roles, thresholds, recommendations, and outcomes are SAMPLE/SYNTHETIC. No association execution, approval, signature, vendor, contract, or third-party evidence is claimed.\n\n## R06 layout result\n\nThe repeated four-row demonstration-threshold table had caused the final row to orphan even after font reductions (R03 and R04). R05 retained a blank final page after table-to-list reflow. R06 removes only the empty terminal paragraph that created the blank page. It preserves all substantive content and the four threshold predicates/results. R06 is seven pages; every page was directly inspected. See `evidence/R06_VISUAL_TECHNICAL_QA.json` and `evidence/render_R06/`.\n\n## Arithmetic\n\n- 2024 example: `(4+4+3+2)/4 = 3.25`; `3/4 = 75.0%`.\n- 2025 example: `(4+4+4+4)/4 = 4.00`; `4/4 = 100.0%`.\n- Combined fulfillment: `(3+4)/(4+4) = 87.5%`.\n- Mean score: `(3.25+4.00)/2 = 3.625`, shown as 3.63.\n- Differences: +0.75 score; +25.0 percentage points.\n\n## Source and synthetic traceability\n\n`inputs/UNIQUE_BLUEPRINT_0047.jsonl` is the exact current Blueprint row. `inputs/official_checkbox_048.json` binds the deliverable to the original checkbox inventory. `register/SYNTHETIC_REPLACEMENT_REGISTER_0047_R06.json` has all 25 fact-level SAMPLE/SYNTHETIC entries with value, section, rendered page/table locator, calculation/basis, replacement action, and responsible role. The source historical R01 build receipt is preserved under `../0047_R01/evidence/`. No central register synchronization is claimed.\n\n## Review lineage\n\nR01 has a historical semantic PASS tied only to R01's exact SHA; its old visual defect remains in history. R02, R03, R04, and R05 each have a documented layout failure and remain preserved as historical candidates. R06 is a new exact-SHA visual/technical candidate. Independent semantic review is pending for R06 and must be recorded against its exact SHA. No Human formal acceptance is claimed.\n'''
(R06/'README.md').write_text(readme,encoding='utf-8')
print(json.dumps({'docx_sha256':sha(R06/'candidate'/'0047_R06.docx'),'pdf_sha256':sha(pdf),'register_count':len(register),'blueprint_selected_line_sha_incl_eol':hashlib.sha256(blue_line).hexdigest(),'inventory_raw_sha256':sha(INVENTORY),'rendered_pages':len(pages),'package':'assembled'},ensure_ascii=True,indent=2))
