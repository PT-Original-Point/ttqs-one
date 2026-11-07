from pathlib import Path
from hashlib import sha256
import csv,json,shutil,subprocess,datetime
root=Path(r'E:\TTQS\_github_sync_0064')
base=root/'docs'/'ttqs-quality-20261016'/'quality-review'
out=base/'0077_R01'
if (out/'candidate'/'0077_R01_body.md').exists() or (out/'candidate'/'0077_R01.docx').exists(): raise SystemExit('0077_R01 candidate already exists; do not regenerate its source packet blindly')
(out/'inputs'/'upstream_snapshots').mkdir(parents=True,exist_ok=True)
(out/'candidate').mkdir(exist_ok=True);(out/'evidence').mkdir(exist_ok=True);(out/'review').mkdir(exist_ok=True);(out/'worker').mkdir(exist_ok=True)
s76=base/'0076_R01'
copy_map={
 s76/'inputs'/'upstream_snapshots'/'0073_R08.docx':out/'inputs'/'upstream_snapshots'/'0073_R08.docx',
 s76/'inputs'/'upstream_snapshots'/'0074_R01.docx':out/'inputs'/'upstream_snapshots'/'0074_R01.docx',
 s76/'inputs'/'upstream_snapshots'/'0075_R02.docx':out/'inputs'/'upstream_snapshots'/'0075_R02.docx',
 s76/'candidate'/'0076_R01.docx':out/'inputs'/'upstream_snapshots'/'0076_R01.docx',
 s76/'inputs'/'upstream_snapshots'/'official_evidence_table_source.pdf':out/'inputs'/'upstream_snapshots'/'official_evidence_table_source.pdf'}
for src,dst in copy_map.items():
 if not src.exists(): raise SystemExit(f'missing source {src}')
 shutil.copy2(src,dst)
def h(p): return sha256(p.read_bytes()).hexdigest()
rows=[
('P01','NEEDS_CLARIFICATION','先問服務對象目前最想處理哪件事，再用自己的話複述確認；不要因為趕時間替對方選答案。','預計在下一次服務接待先用一個開放問題，再重述需求請對方確認。','若一個人同時提出兩項急迫需求，如何協助排序而不越權仍不清楚。','以兩句話練習「先問—再確認」，完成後只記練習日期，不記服務對象身分。','希望有一張需求澄清句型卡。'),
('P02','PRIVACY_CONSENT','記錄敏感資訊前要先說明目的與用途，並確認必要同意；沒有必要的內容不要抄進交接。','預計先說明記錄用途，再確認是否可記必要欄位。','遇到對方無法清楚表達同意時應找誰協助仍需確認。','先向主管角色確認適用的同意與升級流程；未確認前不記敏感細節。','希望課程提供不同情境的同意說明範例。'),
('P03','RECORD_ACCURACY','把親眼觀察、對方原話與自己的推測分開；不確定就標示待確認，不把推論寫成事實。','預計用「觀察／原話／待確認」三欄整理練習案例。','不同工作者對同一件事理解不同時，如何保留差異並更正紀錄需多練習。','使用一則合成案例各自寫紀錄，再對照哪些句子屬事實、哪些屬推測。','希望提供更正前後的紀錄對照例。'),
('P04','CLOSED_LOOP_HANDOFF','交接不能只說「已處理」；要有接手角色、下一步、期限與接收確認。','預計在模擬交班用四項欄位逐一核對。','若接手人未回覆，何時再次聯繫或升級仍不熟。','按示範流程演練一次未回覆的交接，僅記模擬完成情形。','希望有電話與文字交接的分開範例。'),
('P05','NEEDS_CLARIFICATION','先弄清楚對方要的是資訊、陪同還是轉介，再說明本角色能提供的範圍。','預計在服務前先問「您希望我協助哪一部分？」並確認理解。','多方家屬意見不同時，如何確認服務對象自己的意願需要再討論。','用角色扮演練習回到本人需求並記錄待確認事項。','希望加一段家屬同場的界線案例。'),
('P06','PRIVACY_CONSENT','同意不是一次勾選就永遠有效；用途變更或需要新增資料時，應重新說明並依流程處理。','預計在新增記錄欄位前先核對用途與授權。','既有紀錄需要提供給其他合作角色時，應如何查核權限仍需確認。','列出需向授權窗口確認的問題，不自行複製或轉傳資料。','希望有用途變更與資料分享的流程圖。'),
('P07','RECORD_ACCURACY','好紀錄要簡短、可追溯並能讓下一位接手；不能為了完整而抄入不必要的個資。','預計使用最小必要欄位記錄時間、事件與待辦。','怎樣判斷某欄位「必要」需結合實際規範。','拿合成交接單逐欄說明保存理由；無法說明的欄位先標待審。','希望有欄位保留與刪除的判斷例。'),
('P08','CLOSED_LOOP_HANDOFF','結束一次談話前要確認誰負責聯絡、何時回覆；交接對方要覆述收到的事項。','預計用接手人、下一步、日期、狀態四欄做模擬交接。','跨班別交接時如何處理尚未取得回覆的事項需要練習。','在合成情境演練未結案清單，將未回覆項目保留為待辦。','希望安排不同班別的接力演練。'),
('P09','NEEDS_CLARIFICATION','先確認對方的目標和目前限制，再提供可選方案，不以自己的偏好代替對方決定。','預計先詢問希望達成的結果與可接受的時間，再共同排下一步。','對方暫時無法決定時，怎麼安排回訪而不形成壓力仍需學習。','練習提供兩個中性選項並詢問是否需要時間思考。','希望有避免誘導選擇的對話例。'),
('P10','ROLE_BOUNDARY','遇到超出志工角色、可能涉及安全或專業判斷的情況，不自行承諾；先停下並依升級程序求助。','預計把「停止、保護、通知授權角色、留下必要紀錄」寫成口袋提示。','不同緊急程度的升級時限必須依正式規範確認。','向授權窗口確認現行緊急聯絡流程；未確認前保持HOLD。','希望用情境卡練習什麼時候立即升級。'),
('P11','PRIVACY_CONSENT','在錄音、拍照或轉傳資料前須確認目的、同意與授權；不因教學方便就擴大蒐集。','預計使用合成素材練習辨識哪些內容不能拍攝或傳送。','已拍攝但用途改變時的處理方式仍需主管依規範說明。','遇到不確定素材先停止分享並詢問授權窗口。','希望課程清楚說明素材保留與刪除程序。'),
('P12','NEEDS_CLARIFICATION','提問後要讓對方修正自己的理解；複述不是替對方做結論。','預計在模擬服務中使用「我理解的是…有沒有需要更正？」。','對方不願回答時如何尊重拒答並留下必要狀態需要練習。','用拒答情境演練如何停止追問、記錄待確認並交由適當角色。','希望增加沉默或拒答的處理示例。'),
('P13','RECORD_ACCURACY','若發現紀錄錯誤，應保留原始內容與更正軌跡，寫明理由、時間及授權角色。','預計在合成系統截圖上練習提出更正申請，不直接覆寫。','不同系統的更正權限和版本留存規則需依協會現行制度確認。','把需確認的系統問題列給管理角色；未確認不操作真實紀錄。','希望有一份更正申請範例。'),
('P14','CLOSED_LOOP_HANDOFF','交接資訊要讓下一位知道目前狀態與未完成原因，不能只留下名字或電話。','預計在模擬單加入目前狀態、下一步、期限及接收確認。','多個待辦互相依賴時如何排序仍需和團隊一起練習。','用合成情境標出依賴項，確認先後順序並標示尚未驗證事項。','希望用兩個服務情境比較交接寫法。'),
('P15','RECORD_ACCURACY','記錄應讓人知道資料從何而來；未核實的內容要標示來源或待查，不可補成看似確定。','預計在模擬紀錄每一項事實旁標註來源類型。','口頭轉述和原始文件不一致時，如何記錄差異需再討論。','先保留兩種說法及待查狀態，再依授權取得可核實來源。','希望有口頭轉述與原件不符的案例。'),
('P16','NEEDS_CLARIFICATION','課堂練習提醒我先問清楚當事人希望的協助，再確認下一步由誰負責。','預計在模擬交接開始前先列需求與限制，再請接手角色確認。','若當事人更改目標，怎麼更新既有計畫並通知接手者仍需練習。','以合成案例演練目標變更，保留前後版本與待確認事項。','希望安排一次完整的需求改變與重新交接演練。')]
themes={
 'NEEDS_CLARIFICATION':'需求澄清與尊重服務對象決定',
 'PRIVACY_CONSENT':'隱私、用途及同意界線',
 'RECORD_ACCURACY':'最小必要、事實與更正軌跡',
 'CLOSED_LOOP_HANDOFF':'具接手人、下一步、期限與接收確認的交接',
 'ROLE_BOUNDARY':'角色界線與安全升級'}
fields=['learner_code','primary_theme','learning_takeaway','planned_application','unresolved_gap','next_step_proposed','support_request']
data=out/'inputs'/'REFLECTION_SYNTHETIC_DATA_0077_R01.csv'
with data.open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['sample_case_id','learner_code','primary_theme_code','primary_theme_label','learning_takeaway','planned_application_not_actual','unresolved_gap','next_step_proposed_not_executed','support_request','record_status'])
 for r in rows:w.writerow(['SYN-0073-2026-A01',r[0],r[1],themes[r[1]],*r[2:],'SAMPLE/SYNTHETIC; REAL=UNKNOWN/HOLD'])
register=out/'inputs'/'SYNTHETIC_REPLACEMENT_REGISTER_0077_R01.csv'
with register.open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['replacement_id','source_path','source_row','field_name','synthetic_value','required_real_source_or_replacement','verification_rule','real_status'])
 idx=0
 for i,r in enumerate(rows,2):
  vals={'learner_code':r[0],'primary_theme':themes[r[1]],'learning_takeaway':r[2],'planned_application_not_actual':r[3],'unresolved_gap':r[4],'next_step_proposed_not_executed':r[5],'support_request':r[6]}
  for field,val in vals.items():
   idx+=1;w.writerow([f'SYN-0077-{idx:03d}','REFLECTION_SYNTHETIC_DATA_0077_R01.csv',i,field,val,'Authorized original learner reflection or approved attributable record; pseudonymized identifier; documented collection date and consent','Check provenance and consent; do not infer; separate refusal/blank from zero; restrict access','REAL=UNKNOWN/HOLD'])
 for name,val,source in [
  ('sample_case_id','SYN-0073-2026-A01','Authorized class/case record'),('course_title','志工服務溝通與紀錄交接實務','Approved course plan and actual class record'),('sample_date','2026-08-15 (synthetic scenario only)','Verified attendance/implementation record'),('cohort_n','16 synthetic rows','Actual eligible reflection count and disposition log'),('primary_theme_counts','5,3,4,3,1 synthetic coded counts','Recode authorized original responses with versioned codebook and reviewer check'),('action_options','Seven proposed, not executed sample actions','Approved meeting decision, named role, due date, follow-up evidence'),('consent_and_privacy','Synthetic safeguards only','Actual privacy notice, consent/decline evidence, retention policy')]:
  idx+=1;w.writerow([f'SYN-0077-{idx:03d}','SOURCE_PACKET_0077_R01.md','case-level',name,val,source,'Verify official source; document provenance and authorization; keep missing evidence on HOLD','REAL=UNKNOWN/HOLD'])
# Derive fresh source IDs and hash provenance from live Git tree.
branch='origin/work/ttqs-one-document-quality-contract-20261016'
manual_sha=subprocess.check_output(['git','rev-parse',f'{branch}:docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md'],cwd=root,text=True).strip()
blue_sha=subprocess.check_output(['git','rev-parse',f'{branch}:docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md'],cwd=root,text=True).strip()
source_commit=subprocess.check_output(['git','rev-parse',branch],cwd=root,text=True).strip()
contract_files={}
for name in ['01_HUMAN_MISSION_AND_ACCEPTANCE.md','02_GENRE_WRITING_MANUAL.md','03_157_CHECKBOX_BLUEPRINTS.md']:
 rel='docs/ttqs-quality-20261016/'+name
 raw=subprocess.check_output(['git','cat-file','blob',f'{branch}:{rel}'],cwd=root)
 dst=out/'inputs'/'upstream_snapshots'/name
 dst.write_bytes(raw)
 contract_files[name]=h(dst)
files={p.name:h(p) for p in copy_map.values()}
files.update(contract_files)
unique=f'''# DOCX 0077 Unique Blueprint R01\n\nDerived mapping for this candidate only; not an official document or approval.\n\n## Exact mapping\n- DOCX ID: 0077\n- Unique requirement: I17B-E01\n- Official checkbox serial: 084\n- Indicator: 17b learning\n- Document genre: learner reflection report (學員心得報告)\n- Official evidence table: training-institution version, page 6; source PDF SHA-256 {h(out/'inputs'/'upstream_snapshots'/'official_evidence_table_source.pdf')}\n- Source branch head at packet creation: {source_commit}\n- Writing manual blob: {manual_sha}\n- 157-checkbox Blueprint blob: {blue_sha}\n\n## Official scope and distinct function\nOfficial checkbox 084 groups exam record, learner reflection, photo/activity records, and post-training career-planning advice. It requires at least four different functional products. This document is only the learner reflection report; it does not replace 0076 assessment, 0078 photo/activity index, or 0079 individual post-training plan. It is not checkbox 085 (course evaluation and wrong-answer/course-change decision), checkbox 086 (closeout/action-plan verification), or 0073 satisfaction survey. Keep checkbox 084 PARTIAL/HOLD until all sibling functions and genuine source paths are verified.\n\n## Genre and content requirements\nA usable report must contain a precisely identified cohort and collection process; consent, privacy and non-retaliation safeguards; the reflection prompts; fully completed, traceable sample learner entries; a stated coding method with denominators; theme analysis; learning gaps; bounded course-improvement recommendations; proposed owners/next checks; and a usable blank form for real collection. Use learner-centered language. Do not score reflections as exam results or satisfaction ratings. Distinguish reflection, intention, observed behavior, and verified result.\n\n## Synthetic case boundaries\n- Case: SYN-0073-2026-A01; course: 志工服務溝通與紀錄交接實務; scenario date: 2026-08-15, not a verified actual class date.\n- P01-P16 are synthetic scenario tokens reused for sample continuity with 0074/0076; there is no claimed real identity mapping. 0073 S01-S16 survey codes have no P-to-S crosswalk.\n- The attached 16 reflection rows are invented examples for demonstrating coding and use; they are not learner statements and not evidence of attendance, completion, satisfaction, behavior or outcomes.\n- Primary theme counts are derived only from the attached synthetic rows (one primary code per row); never infer correlation with 0073 satisfaction scores or 0074/0076 test scores.\n- 0075 Option B remains PROPOSED/PENDING APPROVAL. Any action/date/owner in this document is SAMPLE/PROPOSED/NOT EXECUTED.\n\n## Required failure/HOLD conditions\nHold or reject entries that lack a traceable actual source, consent basis, date/course context, or authorized collection role; contain direct identifiers or unnecessary sensitive details; are staff-written but attributed to learners; duplicate, selective, or altered responses; conflate blanks/refusals with negative answers; or state plans as completed results. Never fabricate quotes, signatures, approvals, attendance, photos, credentials or impacts.\n\n## Source snapshot hashes\n'''+''.join(f'- {k}: SHA-256 `{v}`\n' for k,v in files.items())+f'- 0076 current candidate DOCX: SHA-256 `{h(s76/"candidate"/"0076_R01.docx")}`\n- Synthetic reflection rows: SHA-256 `{h(data)}`\n- Synthetic replacement register: SHA-256 `{h(register)}`\n'
(out/'inputs'/'UNIQUE_BLUEPRINT_0077_R01.md').write_text(unique,encoding='utf-8')
packet=f'''# 0077 R01 source packet\n\n## Authority\nCurrent source branch head: `{source_commit}`. Official 157-checkbox source blob: `{blue_sha}`; writing manual blob: `{manual_sha}`. The official training-institution evidence PDF is included as `upstream_snapshots/official_evidence_table_source.pdf`, SHA-256 `{h(out/'inputs'/'upstream_snapshots'/'official_evidence_table_source.pdf')}`. Its p.6 I17b checkbox 084 names exam, learner reflection, photos/records and post-training career advice. The current 157-checkbox Blueprint gives checkbox 084 a minimum of four distinct functional products.\n\n## Artifact identity\nThis writer assignment is only DOCX 0077 / I17B-E01 / checkbox 084 / learner reflection report. 0076 is exam/practical assessment, 0078 is real-photo/activity index, and 0079 is individual post-training career/learning guidance. 0073 is satisfaction survey (17a); 0074 is written pre/post assessment record (17a); 0075 is proposed improvement action (17a). Nearby 085 and 086 have distinct purposes.\n\n## Linked synthetic case\nCase `SYN-0073-2026-A01`; course `志工服務溝通與紀錄交接實務`; scenario date `2026-08-15` is synthetic and is not asserted as a real class. Included upstream DOCX hashes: 0073 R08 `{files['0073_R08.docx']}`, 0074 R01 `{files['0074_R01.docx']}`, 0075 R02 `{files['0075_R02.docx']}`, 0076 R01 `{files['0076_R01.docx']}`. Upstream 0073 reports Q5 54/15=3.60/5 and 8/15=53.33% positive; these are survey facts and are not reflection results. 0074/0076 use 16 synthetic P tokens and assessment values; the reflection data is an independent illustrative response set, not derived from test scores. 0075 Option B is PROPOSED/PENDING APPROVAL, not executed.\n\n## Dataset and denominator rules\n`REFLECTION_SYNTHETIC_DATA_0077_R01.csv` contains 16 invented, completed reflection examples, one row per fictional P01-P16. Each row has one primary theme code only. Theme counts are computed from the attached CSV; no score/mean is calculated. 0073 S01-S16 have no asserted crosswalk to P01-P16. Blank, declined, invalid or missing real responses must be reported separately, never coded as zero or silently excluded. The CSV values are all sample text and cannot be represented as actual quotations.\n\nPrimary-code definitions: `NEEDS_CLARIFICATION` = needs clarification / respecting learner or service-user choice; `PRIVACY_CONSENT` = privacy, purpose and consent; `RECORD_ACCURACY` = minimum-necessary records, facts and correction traceability; `CLOSED_LOOP_HANDOFF` = receiver, next step, due date and acknowledgment; `ROLE_BOUNDARY` = role limits and safety escalation. The dataset and register SHA-256 are `{h(data)}` and `{h(register)}`.\n\n## Public-use and replacement limits\nAll real-source fields remain `REAL=UNKNOWN/HOLD`. The replacement register identifies each synthetic field, where it appears, the genuine source needed, and a verification rule. Never upload private learner reflections or consent records to this public repository. A real version requires permission, restricted storage, authorized staff, retention/deletion rules and exact-source verification.\n\n## Prior acceptance state\n0076 candidate SHA `{h(s76/"candidate"/"0076_R01.docx")}` has technical PASS, 26-page visual PASS and independent exact-SHA semantic PASS, but is not formally accepted; checkbox 084 remains PARTIAL. Those receipts do not establish that 0077 is real or formally accepted.\n'''
packet=packet.replace('## Artifact identity',f"Contract snapshots included (SHA-256): 01 `{contract_files['01_HUMAN_MISSION_AND_ACCEPTANCE.md']}`; 02 `{contract_files['02_GENRE_WRITING_MANUAL.md']}`; 03 `{contract_files['03_157_CHECKBOX_BLUEPRINTS.md']}`.\n\n## Artifact identity")
(out/'inputs'/'SOURCE_PACKET_0077_R01.md').write_text(packet,encoding='utf-8')
receipt={'schema':'TTQS_ONE_0077_SOURCE_PACKET_R01.v1','document_id':'0077','requirement_id':'I17B-E01','official_checkbox_serial':'084','source_commit':source_commit,'mission_blob':subprocess.check_output(['git','rev-parse',f'{branch}:docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md'],cwd=root,text=True).strip(),'writing_manual_blob':manual_sha,'blueprint_blob':blue_sha,'included_upstream_hashes':files,'synthetic_data_sha256':h(data),'replacement_register_sha256':h(register),'synthetic_rows':len(rows),'primary_theme_counts':{k:sum(x[1]==k for x in rows) for k in themes},'real_status':'UNKNOWN/HOLD','candidate_status':'NOT_BUILT'}
(out/'inputs'/'SOURCE_PACKET_RECEIPT_0077_R01.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'root':str(out),'sources':files,'data_rows':len(rows),'register_rows':idx,'theme_counts':receipt['primary_theme_counts'],'source_commit':source_commit,'blueprint_blob':blue_sha},ensure_ascii=False))
