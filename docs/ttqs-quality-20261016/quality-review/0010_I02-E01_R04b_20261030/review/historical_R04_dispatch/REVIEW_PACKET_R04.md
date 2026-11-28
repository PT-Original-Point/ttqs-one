# 0010/I02-E01 R04 reviewer packet

## Review request
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\qa\REVIEW_REQUEST_R04.md
source_sha256=59bbb5503b7bc2c2420ebfd876c748e649f3345084cebe203b4cf7acc1dd7dcd
source_bytes=2338

# 0010 / I02-E01 R04 exact-SHA independent semantic review

Requested OpenCode route: opencode/deepseek-v4.1-flash-free. Review only the attached files. Do not use tools, browse, run commands, edit files, or claim any local verification you did not perform. Return only one JSON object.

The candidate Markdown SHA-256 is 131b703267feebfbef3ec49fc8aa9beaab2ded0818415e9e5d86771b84925d90. The paired SAMPLE/SYNTHETIC register SHA-256 is 6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc. Bind every conclusion to these exact values. The candidate and register are not a DOCX, not REAL evidence, and not formally accepted.

Review the entire R04 body and all 157 register rows against the attached official requirement extract, exact unique Blueprint row, source binding, R03 review, and R04 deterministic receipt. In particular determine whether R03 SEM-01 through SEM-04 were repaired, whether prior arithmetic and 157 fact values remain consistent, and whether new material defects exist. Do not promote the unresolved Blueprint scope conflict to PASS. Actual roster, authority, learner records, approvals, real execution and association acceptance remain UNKNOWN.

Check: official/Blueprint binding and genre; title-blind identity; negative-neighbor separation from 0009 and 0011; question/rubric/weight/gates and score calculations; complete SAMPLE/SYNTHETIC worked example; contiguous renderable GFM register table, exact sidecar identity, field-level scenario/retest locators and REAL replacement checks; human use/hold/reject rules; truth boundary; and any meaning-changing issue introduced in R04.

JSON schema:
{
  "receipt_type":"independent_exact_sha_semantic_review",
  "review_id":"0010-I02-E01-R04",
  "reviewed_at_utc":"ISO-8601",
  "candidate_sha256":"...",
  "register_sha256":"...",
  "verdict":"PASS|PARTIAL|FAIL",
  "scope":"...",
  "checks":[{"id":"...","result":"PASS|PARTIAL|FAIL","locator":"...","reason":"..."}],
  "findings":[{"id":"...","severity":"critical|major|moderate|minor","locator":"...","evidence":"...","required_repair":"..."}],
  "limitations":["..."],
  "does_not_claim":["REAL evidence","formal acceptance","unresolved Blueprint scope"]
}
For a clean review, findings must be an empty array. Use PARTIAL or FAIL for substantive defects. Avoid unsupported legal or association claims.

## Official requirement extract
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\source\OFFICIAL_REQUIREMENT_EXTRACT_R04.txt
source_sha256=65ab23c7a778753d7fb60160bc54621c0978f1776262bfc46b6a3f95626a7823
source_bytes=473

OFFICIAL_SOURCE=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf
OFFICIAL_SOURCE_SHA256=805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709
LOCATOR=printed page 1, indicator 2
EXACT_REQUIREMENT_TEXT=對學員訓練成果有評核標準的訂定及說明。
STATUS=Exact phrase was extracted from the local official PDF and independently matched in the R03 exact-SHA review; no REAL association evidence is implied.

## Exact current Blueprint row
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\source\BLUEPRINT_ROW_0010_I02-E01_R04.json
source_sha256=47b3387d2f97aeed2b42efe602ffcc9070c664d2e9da4a119d50d378354d3236
source_bytes=7230

{"deliverable_id":"0010","requirement_id":"I02-E01","final_filename":"0010__學員訓練成果評核標準與說明.docx","document_genre":"分析／評估報告｜學員訓練成果評核標準與說明","document_purpose":"本件專屬焦點：學員訓練成果評核標準與說明；需直接回應的官方佐證要求為：對學員訓練成果有評核標準的訂定及說明。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。","primary_user_or_reader":"供主管與決策者讀取資料、理解計算、判斷差距並採取具體決策。","evidence_role":"呈現方法、完整合成或已驗證結果、分析、限制及可追溯決策；不得冒充實績。 本文件只擁有 I02-E01 的直接紀錄／分析口徑；不得吞併其他要求的事實。","source_of_truth":"官方查核佐證表精確原文『對學員訓練成果有評核標準的訂定及說明。』，表內頁次 1，讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH；REQ_157_MAP 對應 I02-E01；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。","required_sections":"摘要、用途與決策問題；官方要求及分析範圍；資料來源、樣本與納入排除；指標定義、分母與計算方法；完整示範資料及逐步計算；分群／趨勢／差異結果；圖表解讀及品質限制；發現、原因與證據強度；結論與可執行建議；責任人、期限與追蹤指標；合成資料聲明及真實替換清單；附件索引、覆核與版本","required_tables_or_figures":"資料欄位—定義—分母—來源—限制字典；合成明細／彙總結果與逐步計算；分群比較／差距優先排序矩陣；結論—證據—建議—責任—追蹤指標表；官方要求—結果—證據位置—覆核追溯表","required_fields_or_questions":"對外承諾是什麼？；誰有權核准例外？；如何證明公開揭露且版本一致？；本文件中哪一段/哪一表直接證明：「對學員訓練成果有評核標準的訂定及說明。」？；分析母數及排除說明；計算口徑與四捨五入；建議決策及適用限制；合成事實替換登錄鍵","required_calculations_or_analysis":"政策檢討完成率=已完成項/應完成項。不得稱為組織實績。","required_cross_references":"同要求分件 無；相鄰要求 I01-E06, I02-E02；共用原始來源時只引用核實結果，不複製別份文件正文。","real_data_required":"升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。","third_party_evidence_required":"若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。","prohibited_fabrication":"不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。","title_blind_test":"遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『學員訓練成果評核標準與說明』並證明『對學員訓練成果有評核標準的訂定及說明。』；若可無修改移作其他要求即失敗。","negative_choice_neighbors":"0009《年度績效目標訂定與分析紀錄》（I01-E06）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0011《與訓練政策有關之訓練產品與市場定位_制度文件》（I02-E02）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。","acceptance_tests":"移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『學員訓練成果評核標準與說明』，且能指出直接回應『對學員訓練成果有評核標準的訂定及說明。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。","document_role":"analysis_report","official_requirement_text":"對學員訓練成果有評核標準的訂定及說明。","official_checkbox_text":"對學員訓練成果有評核標準的訂定及說明。","official_evidence_table_page":"1","official_source_readback_status":"PDF_TEXT_EXACT_PAGE_MATCH","official_visually_checked_pages":"","requirement_deliverable_siblings":"0010","docx_body_template_policy":"FROM_SOURCE_ONLY; old body is discovery evidence only and prohibited as rebuild template; Wave005 R3 0031-0040 quality-height references only; Wave001-004 tainted; old Wave005 invalid; Wave006 prohibited.","synthetic_population_rule":"缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。","historical_blueprint_source":"5f6f8eb29270797c1c2ecea57ab351e8992fd92a00154fa496299183b2df2061","historical_body_use":"PROHIBITED","source_map_notes":"129 exact official requirement rows + reconciled 142-ID crosswalk; official source PDF and exact Drive readback evidence are recorded in runtime SOURCE/CONTROL maps."}

## Current source binding
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\source\SOURCE_BINDING_R04.json
source_sha256=ba6d5563500a77482160eaad3b1426962d7d69a488e0db3709aaca929685ea66
source_bytes=1156

{
  "receipt_type": "exact_source_binding",
  "doc_id": "0010",
  "requirement_id": "I02-E01",
  "official_requirement": "對學員訓練成果有評核標準的訂定及說明。",
  "official_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
  "official_pdf_locator": "printed p.1, indicator 2",
  "blueprint_file_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
  "blueprint_row_sha256": "3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d",
  "r03_candidate_sha256": "7427c8e7b5b3c95164f9f5928869b8220c2bd21f3cfeae9ef50df6de4db69a51",
  "r03_register_sha256": "3de22c208a3e527a09581436a7896567daa171242d3b4380d55964547008a67e",
  "r03_review_sha256": "14f2ee950aba6cf044c1583ead5a312f91db2d0d7b029685825339a28fde5f57",
  "r03_deterministic_qa_sha256": "34f900e93a1458799818ac30323cc4ed2cffdd4c914a1979432eddf57a9d755d",
  "scope_limitations_preserved": [
    "Blueprint outward training-policy/public-disclosure fields applicability remains PARTIAL/UNKNOWN.",
    "No actual roster, authorization, learner, assessment or association record supplied; REAL remains UNKNOWN."
  ]
}

## R03 independent review
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\reviewer\SEMANTIC_PRE_REVIEW_R03.json
source_sha256=14f2ee950aba6cf044c1583ead5a312f91db2d0d7b029685825339a28fde5f57
source_bytes=18103

{
  "receipt_type": "TTQS_ONE_INDEPENDENT_SEMANTIC_REVIEW",
  "review_date": "2026-10-29",
  "target": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\\worker\\0010_I02-E01_R03.md",
    "expected_sha256": "7427c8e7b5b3c95164f9f5928869b8220c2bd21f3cfeae9ef50df6de4db69a51",
    "sha256_before_review": "7427c8e7b5b3c95164f9f5928869b8220c2bd21f3cfeae9ef50df6de4db69a51",
    "sha256_after_review": "7427c8e7b5b3c95164f9f5928869b8220c2bd21f3cfeae9ef50df6de4db69a51",
    "bytes": 43198,
    "lines_reviewed": 365,
    "pipe_table_lines": 292,
    "candidate_bytes_modified": false,
    "pipe_delimited_blocks": 13
  },
  "synthetic_sidecar": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\\worker\\SYNTHETIC_REGISTER_R03.md",
    "expected_sha256": "3de22c208a3e527a09581436a7896567daa171242d3b4380d55964547008a67e",
    "sha256_before_review": "3de22c208a3e527a09581436a7896567daa171242d3b4380d55964547008a67e",
    "sha256_after_review": "3de22c208a3e527a09581436a7896567daa171242d3b4380d55964547008a67e",
    "lines_read": 166,
    "fact_rows": 157,
    "unique_fact_ids": 157,
    "embedded_rows": 157,
    "embedded_and_sidecar_rows_equal": true,
    "sidecar_bytes_modified": false
  },
  "reviewer_independence": {
    "role": "separate semantic-review turn; no candidate or sidecar edits made",
    "method": "reviewer independently read the complete Markdown body and every table/register row; writer and deterministic receipts were treated as claims to verify, not semantic proof"
  },
  "sources": {
    "official_pdf": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\SOURCES\\TTQS查核佐證文件資料表-訓練機構版 (2).pdf",
      "sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
      "locator": "PDF page 1, indicator 2",
      "exact_requirement": "對學員訓練成果有評核標準的訂定及說明。",
      "result": "HASH_MATCH_AND_TEXT_CONFIRMED"
    },
    "blueprint": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\BLUEPRINT_CURRENT.jsonl",
      "sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
      "row_locator": "JSONL line 10; deliverable_id=0010; requirement_id=I02-E01",
      "row_sha256": "3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d",
      "applicability": "PARTIAL/UNKNOWN: row carries outward-policy/disclosure and policy-review fields whose scope relation to the official learner-assessment requirement is not resolved; candidate explicitly preserves this conflict without claiming full conformity"
    },
    "R02_terminal_review": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_LUNA_TEXT_DRAFT_R02_20261029\\reviewer\\SEMANTIC_REVIEW_R02.json",
      "sha256": "25ba55cc8776cfa272f9f7571274ad5676ef43da31861b4fc4acc006d0fa66ff",
      "verdict": "FAIL",
      "result": "READ; all eleven findings and recalculation block reviewed against R03"
    },
    "R03_writer_receipt": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\\worker\\WRITER_RECEIPT_R03.json",
      "sha256": "e43f49c14c594f6a97a59ddb1841b1481121b3bd7fbb41bfb4835cd85b02ab9f",
      "result": "READ_AND_CROSS_CHECKED"
    },
    "R03_deterministic_receipt": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\\qa\\DETERMINISTIC_MATH_AND_REGISTER_R03.json",
      "sha256": "34f900e93a1458799818ac30323cc4ed2cffdd4c914a1979432eddf57a9d755d",
      "result": "HASH_MATCH_AND_READ; structural/math results checked independently within this review"
    }
  },
  "scope": {
    "read": "All 365 candidate lines and all 13 pipe-delimited content blocks, including the broken table-like register rows; all 166 lines and 157 fact rows of the sidecar; complete R02 terminal review; R03 writer and deterministic receipts; official PDF page 1 text and exact Blueprint row.",
    "checks": [
      "official requirement match and Blueprint row identity",
      "R02 findings F-01 through F-11 disposition",
      "20-item key and LO1-LO4 item allocation",
      "four first-attempt and two retest answer vectors",
      "all displayed score vectors, four-gate outcomes, §12 rates and means",
      "SF-073/074/076 carry-forward and SF-099..102/SF-112 new-retake provenance",
      "157 unique register facts and embedded/sidecar equality",
      "small-association role separation, backup and conflict controls",
      "SAMPLE/REAL boundary and negative-neighbor separation"
    ],
    "not_reviewed": [
      "DOCX existence or visual layout",
      "Word pagination, typography or rendered appearance",
      "Human approval, adoption, real execution or formal acceptance"
    ]
  },
  "overall": {
    "verdict": "PARTIAL",
    "disposition": "Repairable text candidate; do not treat this review as formal acceptance.",
    "semantic_acceptance": "NOT_GRANTED",
    "docx_visual_qa": "NOT_PERFORMED",
    "human_or_association_acceptance": "NOT_ASSERTED"
  },
  "dimension_results": {
    "official_requirement_and_title_blind_scope": "PASS_WITH_BLUEPRINT_SCOPE_CAUTION",
    "negative_neighbors_0009_and_0011": "PASS; body identifies learner-result assessment as distinct from annual organizational targets and policy/product-market positioning",
    "objective_allocation": "PASS; LO1=10, LO2=4, LO3=3, LO4=3; total 20 with denominator 20",
    "answer_key": "PASS; all 20 keyed options match the stated best response in each question",
    "weights_and_thresholds": "PASS; knowledge 20 + P 40 + C 25 + M 15 = 100; gate total>=70, knowledge>=12/20, practical>=28/40, P3>=3/4 consistently applied",
    "first_attempt_answer_and_score_recalculation": "PASS_WITH_SYNTHETIC_INPUT_LIMITATION",
    "retest_carry_forward_and_new_observation_provenance": "PASS",
    "section_12_denominators_and_means": "PASS",
    "R02_addendum_integration_and_stale_13_2_13_3_locators": "PASS; single integrated body, no §13.2/§13.3 references found",
    "atomic_register_content_and_identity": "PASS_FOR_157_UNIQUE_MATCHING_ROWS; Markdown table syntax and some locator/replacement detail remain PARTIAL",
    "case_level_rating_evidence_and_independent_review_events": "PASS_WITH_SAMPLE_LIMITATION; all 4 first cases have 20-item vectors and 12 criterion observations; two retests have new vectors and five new P observations; actual evidence and persons remain synthetic/unknown",
    "small_association_feasibility": "PARTIAL; two-person separation, admin role combination, backup/external authorization and HOLD rules are present; real capacity and slot/hour scheduling remain unknown",
    "SAMPLE_REAL_boundary": "PASS; no real learner, implementation, approval, signature or completed real review is asserted"
  },
  "recalculation": {
    "question_key": "Q1-Q20 = B,A,B,B,B,A,B,A,A,A,B,A,A,A,A,A,A,A,A,A; checked against all question prompts/options.",
    "first_attempts": {
      "SYN-001": "16/20; P (4+3+3+4)*2.5=35; C (3+4+3+3+4)*1.25=21.25; M (3+3+4)*1.25=12.50; total 84.75; all gates pass.",
      "SYN-002": "13/20; P (3+3+3+3)*2.5=30; C (3+3+2+3+3)*1.25=17.50; M (3+2+3)*1.25=10; total 70.50; all gates pass.",
      "SYN-003": "17/20; P (2+2+1+2)*2.5=17.50; C (4+4+3+3+4)*1.25=22.50; M (4+3+3)*1.25=12.50; total 69.50; total, practical and P3 gates fail.",
      "SYN-004": "11/20; P (4+3+2+3)*2.5=30; C (4+3+4+3+4)*1.25=22.50; M (3+3+3)*1.25=11.25; total 74.75; knowledge and P3 gates fail."
    },
    "retests": {
      "SYN-003": "new 17/20 knowledge and new P [3,3,3,3]=30; C 22.50 and M 12.50 carried; total 82.00; all gates pass.",
      "SYN-004": "new 14/20 knowledge; P [4,3,3,3]=32.50 with P1/P2/P4 tied to first-assessment SF-073/SF-074/SF-076 and P3 new; C 22.50 and M 11.25 carried; total 80.25; all gates pass."
    },
    "rates": "Initial pass 2/4=50%; retest participation 2/4=50%; post-retest attainment 4/4=100%; initial P3 below 3: 2/4=50%; practical below 28: 1/4=25%; knowledge below 12: 1/4=25%. Denominator remains four valid synthetic first assessments.",
    "means": "Initial-pass pair: 14.50/20, 32.50/40, 19.375->19.38/25, 11.25/15, 77.625->77.63/100. Remediation pair: 14.00/20, 23.75/40, 22.50/25, 11.875->11.88/15, 72.125->72.13/100. Rounding occurs only for display."
  },
  "R02_finding_disposition": [
    {
      "id": "F-01",
      "result": "PASS",
      "locator": "§3 table, rows LO1-LO4; §4 Q1-Q20",
      "note": "One unambiguous 10/4/3/3 allocation totals 20; no contradictory LO1=20 row."
    },
    {
      "id": "F-02",
      "result": "PASS_WITH_LIMITATION",
      "locator": "§6 rubric table",
      "note": "Indicator-specific anchors are integrated in the body. Actual policy calibration is not evidenced and remains outside this synthetic example."
    },
    {
      "id": "F-03",
      "result": "PASS_WITH_SAMPLE_LIMITATION",
      "locator": "§4, §5, §8-§9",
      "note": "Complete 20 questions/options/key, one scenario script, four learner answer vectors and 48 first-attempt criterion observations are present. They are synthetic demonstrations, not external originals."
    },
    {
      "id": "F-04",
      "result": "PASS_WITH_REAL_IDENTITY_UNKNOWN",
      "locator": "§9-§11",
      "note": "Distinct evaluator/reviewer role codes and case/retest review event IDs now state review scope and recalculation; no actual staff identity or completed real review is claimed."
    },
    {
      "id": "F-05",
      "result": "PASS",
      "locator": "§11; embedded register IDs SF-073/074/076, SF-099..102, SF-110..113",
      "note": "SYN-003 SF-099..102 are new retest P1-P4 observations. SYN-004 SF-073/074/076 and SF-110/111/113 are carried first-attempt values; SF-112 points to the new P3 retest EV."
    },
    {
      "id": "F-06",
      "result": "PARTIAL",
      "locator": "§15; sidecar rows CASE-SYN-17, SYN-NO-AUTH, SYN-STATUS-UNK, RET-003, RET-004",
      "note": "The 157 facts are atomic, unique and row-identical between embedded register and sidecar; old §13.2/§13.3 locators and grouped SF-137..146 are absent. However, §15 table syntax is broken by a blank line immediately after its header separator; several retest-result locators are section-only and scenario verification instructions are role-focused."
    },
    {
      "id": "F-07",
      "result": "PASS",
      "locator": "§1-§15",
      "note": "No post-body repair addendum; content is integrated in one numbered body and the register follows the case/retest facts."
    },
    {
      "id": "F-08",
      "result": "PASS_AS_CAUTION; BLUEPRINT_CONFORMITY_PARTIAL_UNKNOWN",
      "locator": "§1 paragraph 2 and exact Blueprint row required_fields_or_questions/required_calculations_or_analysis",
      "note": "The scope conflict is explicitly disclosed; unsupported policy or market assertions were not added."
    },
    {
      "id": "F-09",
      "result": "PARTIAL",
      "locator": "§13",
      "note": "R03 replaces a three-person minimum with two distinct primary/reviewer roles, permits one non-scoring administrator combination, and provides authorized backup/external-review and HOLD rules. Actual roster/qualifications and schedulable hours remain UNKNOWN."
    },
    {
      "id": "F-10",
      "result": "PASS",
      "locator": "§1, §14 and status declaration",
      "note": "The body is title-blind identifiable as learner outcome assessment, separates neighboring requirements, and keeps all examples SAMPLE/SYNTHETIC."
    },
    {
      "id": "F-11",
      "result": "PASS_FOR_DISPLAYED_ARITHMETIC",
      "locator": "§3, §5-§8, §11-§12",
      "note": "Question counts, all displayed first/retest scores, thresholds, rates and means independently recalculate; arithmetic does not authenticate real evidence."
    }
  ],
  "findings": [
    {
      "id": "SEM-01",
      "severity": "major",
      "result": "PARTIAL",
      "scope": "candidate and synthetic-register table usability",
      "locator": "Candidate §15 lines 205-208; sidecar lines 6-9",
      "evidence": "Both files put a blank line between the Markdown header separator and the first data row. Under standard GitHub-flavored Markdown table parsing this terminates the table before any fact row; blank breaks later also divide the 157 rows. The deterministic parser counted pipe-delimited records but did not validate rendered Markdown table structure.",
      "impact": "The replacement register data are present and exact-match, but the principal evaluator-facing register is not a single usable Markdown table as currently authored.",
      "recommended_repair": "Remove blank lines within the table or repeat a valid header/separator for each intentionally separate table block; preserve all 157 rows and recheck Markdown rendering."
    },
    {
      "id": "SEM-02",
      "severity": "moderate",
      "result": "PARTIAL",
      "scope": "synthetic register locators and real replacement routes",
      "locator": "Sidecar rows RET-003/RET-004; CASE-SYN-17, SYN-NO-AUTH, SYN-STATUS-UNK",
      "evidence": "RET-003/RET-004 use only §11 as locator instead of a named paragraph/table row/field. Scenario facts use Case ID “合成情境／角色”; their replacement route mentions an approved scenario original, but its verification instruction is mainly about roster, role separation, appointment and date rather than the specific scenario authorization/status fields.",
      "impact": "Most register rows have precise item or EV locators, but these rows do not provide equally direct fact-to-field and source-verification linkage.",
      "recommended_repair": "Give each retest total a named calculation paragraph/row locator; identify the shared scenario case key and specify verification against the approved scenario/version and each named premise."
    },
    {
      "id": "SEM-03",
      "severity": "moderate",
      "result": "PARTIAL",
      "scope": "small-association operating feasibility",
      "locator": "§13",
      "evidence": "R03 requires two distinct conflict-free people per case, permits one to combine only non-scoring administration, specifies trained/authorized backup and conditionally authorized external review, prohibits self-review and requires HOLD when independent coverage is unavailable. It gives no person-slot/hour estimate or limited-volume scheduling example; actual staffing, qualifications and availability are explicitly UNKNOWN.",
      "impact": "The earlier three-person-capacity concern is materially mitigated, and no real staffing claim is fabricated; operational schedulability cannot yet be evaluated.",
      "recommended_repair": "Before any REAL adoption, populate a synthetic-to-real scheduling example only from an authorized roster and actual availability; retain the two-person separation and HOLD rule."
    },
    {
      "id": "SEM-04",
      "severity": "moderate",
      "result": "PARTIAL; SIDECAR_RECEIPT_ONLY",
      "scope": "writer receipt consistency, not candidate arithmetic",
      "locator": "WRITER_RECEIPT_R03.json construction.synthetic_register and synthetic_register.fact_rows; deterministic receipt checks.writer_receipt_count_claim_consistent",
      "evidence": "Writer receipt SHA e43f49c14c594f6a97a59ddb1841b1481121b3bd7fbb41bfb4835cd85b02ab9f says “120 fact rows” in construction prose but its structured field is 157. Deterministic receipt SHA 34f900e93a1458799818ac30323cc4ed2cffdd4c914a1979432eddf57a9d755d reports 157 embedded rows, 157 sidecar rows, 157 unique matching IDs, and isolates the inconsistent writer count. This review independently confirmed the same counts and row equality.",
      "impact": "Receipt metadata is internally inconsistent. It is not a body arithmetic error: all displayed calculations and the 157 embedded/sidecar facts reconcile.",
      "recommended_repair": "Correct or supersede the writer receipt count prose through its own controlled receipt process; do not alter the candidate body solely for this metadata discrepancy."
    },
    {
      "id": "SEM-05",
      "severity": "scope",
      "result": "PARTIAL/UNKNOWN",
      "scope": "Blueprint applicability",
      "locator": "Exact Blueprint row 0010/I02-E01; candidate §1 paragraph 2",
      "evidence": "The exact official requirement is learner outcome assessment. The row also requires outward training-policy/public-disclosure fields and a policy-review completion calculation; their applicability to this document is unresolved. R03 accurately discloses the conflict and declines to assert full Blueprint conformity.",
      "impact": "This is a source-scope uncertainty, not an arithmetic or source-identity failure. It prevents a full Blueprint conformity PASS.",
      "recommended_repair": "Keep PARTIAL/UNKNOWN pending authorized scope clarification; do not infer an association decision."
    }
  ],
  "scope_unknowns": [
    "No actual course, learner, assessment, qualified roster, real record or approval was supplied; no real-world implementation or result is inferred.",
    "Blueprint scope conflict remains unresolved; the review does not decide which additional policy fields are authoritative for I02-E01.",
    "No DOCX was created or inspected; no visual/layout conclusion is made."
  ],
  "preservation": {
    "requested_output_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\\reviewer\\SEMANTIC_PRE_REVIEW_R03.json",
    "only_requested_review_json_written": true,
    "candidate_modified": false,
    "sidecar_modified": false,
    "R02_review_modified": false,
    "no_DOCX_or_GitHub_file_created_or_modified": true
  }
}

## R03 deterministic QA
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\qa\DETERMINISTIC_MATH_AND_REGISTER_R03.json
source_sha256=34f900e93a1458799818ac30323cc4ed2cffdd4c914a1979432eddf57a9d755d
source_bytes=4594

{
  "receipt_type": "deterministic_math_and_register_reconciliation",
  "doc_id": "0010",
  "requirement_id": "I02-E01",
  "text_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\\worker\\0010_I02-E01_R03.md",
  "text_sha256": "7427c8e7b5b3c95164f9f5928869b8220c2bd21f3cfeae9ef50df6de4db69a51",
  "register_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\\worker\\SYNTHETIC_REGISTER_R03.md",
  "register_sha256": "3de22c208a3e527a09581436a7896567daa171242d3b4380d55964547008a67e",
  "writer_receipt_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R03_20261029\\worker\\WRITER_RECEIPT_R03.json",
  "writer_receipt_sha256": "e43f49c14c594f6a97a59ddb1841b1481121b3bd7fbb41bfb4835cd85b02ab9f",
  "checks": {
    "embedded_register_rows_157": true,
    "embedded_register_ids_unique": true,
    "sidecar_register_rows_157": true,
    "sidecar_register_ids_unique": true,
    "embedded_and_sidecar_ids_match": true,
    "answer_key_has_20_items": true,
    "SYN-001_all_scores_and_gate_recalculate": true,
    "SYN-002_all_scores_and_gate_recalculate": true,
    "SYN-003_all_scores_and_gate_recalculate": true,
    "SYN-004_all_scores_and_gate_recalculate": true,
    "four_initial_cases_present": true,
    "SYN-003_retest_knowledge_recalculates": true,
    "SYN-004_retest_knowledge_recalculates": true,
    "SYN-003_retest_total_and_gate_recalculate": true,
    "SYN-004_retest_total_and_gate_recalculate": true,
    "writer_receipt_count_claim_consistent": false,
    "writer_output_sha_matches": true,
    "writer_register_sha_matches": true
  },
  "initial_case_recalculation": {
    "SYN-001": {
      "answers": 20,
      "knowledge_calculated": 16,
      "knowledge_shown": 16,
      "P_calculated": 35.0,
      "P_shown": 35.0,
      "C_calculated": 21.25,
      "C_shown": 21.25,
      "M_calculated": 12.5,
      "M_shown": 12.5,
      "total_calculated": 84.75,
      "total_shown": 84.75,
      "P3": 3,
      "gate_calculated": "通過",
      "gate_shown": "通過"
    },
    "SYN-002": {
      "answers": 20,
      "knowledge_calculated": 13,
      "knowledge_shown": 13,
      "P_calculated": 30.0,
      "P_shown": 30.0,
      "C_calculated": 17.5,
      "C_shown": 17.5,
      "M_calculated": 10.0,
      "M_shown": 10.0,
      "total_calculated": 70.5,
      "total_shown": 70.5,
      "P3": 3,
      "gate_calculated": "通過",
      "gate_shown": "通過"
    },
    "SYN-003": {
      "answers": 20,
      "knowledge_calculated": 17,
      "knowledge_shown": 17,
      "P_calculated": 17.5,
      "P_shown": 17.5,
      "C_calculated": 22.5,
      "C_shown": 22.5,
      "M_calculated": 12.5,
      "M_shown": 12.5,
      "total_calculated": 69.5,
      "total_shown": 69.5,
      "P3": 1,
      "gate_calculated": "未達",
      "gate_shown": "未達"
    },
    "SYN-004": {
      "answers": 20,
      "knowledge_calculated": 11,
      "knowledge_shown": 11,
      "P_calculated": 30.0,
      "P_shown": 30.0,
      "C_calculated": 22.5,
      "C_shown": 22.5,
      "M_calculated": 11.25,
      "M_shown": 11.25,
      "total_calculated": 74.75,
      "total_shown": 74.75,
      "P3": 2,
      "gate_calculated": "未達",
      "gate_shown": "未達"
    }
  },
  "retest_recalculation": {
    "SYN-003": {
      "knowledge": 17,
      "P_vector": [
        3,
        3,
        3,
        3
      ],
      "P_score": 30.0,
      "C_carried": 22.5,
      "M_carried": 12.5,
      "total": 82.0,
      "gate": "通過"
    },
    "SYN-004": {
      "knowledge": 14,
      "P_vector": [
        4,
        3,
        3,
        3
      ],
      "P_score": 32.5,
      "C_carried": 22.5,
      "M_carried": 11.25,
      "total": 80.25,
      "gate": "通過"
    }
  },
  "embedded_register_rows": 157,
  "sidecar_register_rows": 157,
  "writer_receipt_embedded_count_claim": 120,
  "status": "PASS_WITH_RECEIPT_FINDING",
  "finding": "Writer receipt construction text says 120 embedded fact rows, while exact text and sidecar each contain 157 unique matching IDs; receipt metadata needs a non-content correction/reconciliation.",
  "limitations": [
    "Deterministic arithmetic/register scope only; no independent semantic acceptance, DOCX, visual QA, or Human acceptance."
  ],
  "checked_at": "2026-10-29T23:15:29.420071+08:00"
}

## R04 deterministic QA
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\qa\DETERMINISTIC_QA_R04.json
source_sha256=20a165093020236003c25e4216ca8019de3afab0fda60268729b3ec37bea7754
source_bytes=1393

{
  "receipt_type": "deterministic_scoped_repair_qa",
  "doc_id": "0010",
  "requirement_id": "I02-E01",
  "revision": "R04",
  "candidate_text_sha256": "131b703267feebfbef3ec49fc8aa9beaab2ded0818415e9e5d86771b84925d90",
  "sidecar_register_sha256": "6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc",
  "checks": {
    "official_pdf_hash_matches_r03_binding": true,
    "blueprint_file_hash_matches_r03_binding": true,
    "unique_blueprint_row_hash_matches_r03_binding": true,
    "embedded_register_157_unique_rows": true,
    "sidecar_register_157_unique_rows": true,
    "embedded_sidecar_ids_identical_and_ordered": true,
    "gfm_header_separator_valid_both_tables": true,
    "no_blank_line_splits_any_data_row": true,
    "scenario_case_keys_and_field_locators_repaired": true,
    "retest_locators_are_specific": true,
    "numeric_fact_values_unchanged": true,
    "retest_arithmetic_unchanged": true,
    "blueprint_scope_unknown_preserved": true,
    "writer_receipt_157_count_reconciled": true
  },
  "status": "PASS_WITHIN_DETERMINISTIC_SCOPE",
  "limitations": [
    "No semantic PASS; independent exact-SHA review still required.",
    "No DOCX or Word visual QA; later stages must bind to the R04 text SHA.",
    "Blueprint applicability conflict, real data and formal acceptance remain UNKNOWN."
  ],
  "checked_at_utc": "2026-10-29T16:06:21.603220+00:00"
}

## R04 repair receipt
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\qa\R04_REPAIR_RECEIPT.json
source_sha256=14f0c4f4626905581ba8ba5bbf5600d07b8db443ed37b69462d3714c94bf36f1
source_bytes=1765

{
  "receipt_type": "bounded_semantic_finding_repair",
  "doc_id": "0010",
  "requirement_id": "I02-E01",
  "from_revision": "R03",
  "to_revision": "R04",
  "r03_candidate_sha256": "7427c8e7b5b3c95164f9f5928869b8220c2bd21f3cfeae9ef50df6de4db69a51",
  "r03_register_sha256": "3de22c208a3e527a09581436a7896567daa171242d3b4380d55964547008a67e",
  "r03_exact_sha_review_sha256": "14f2ee950aba6cf044c1583ead5a312f91db2d0d7b029685825339a28fde5f57",
  "r04_candidate_sha256": "131b703267feebfbef3ec49fc8aa9beaab2ded0818415e9e5d86771b84925d90",
  "r04_register_sha256": "6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc",
  "changes": [
    "Made the §15 embedded and sidecar registers contiguous GFM tables without blank separators; retained all 157 fact IDs and values.",
    "Added a visibly SAMPLE/SYNTHETIC scenario control card for CASE-SYN-17 with authorization, status, source/time and REAL replacement checks.",
    "Changed the three scenario facts to the concrete CASE-SYN-17 key and field-level locators with explicit hold/verification conditions.",
    "Changed RET-003 and RET-004 from section-only locators to the named §11 calculation paragraph and its specific case total."
  ],
  "preserved": [
    "All 157 fact IDs and values, question items, rubric weights, gates, first-attempt scores and retest arithmetic.",
    "R03 historical candidate, review, and receipts remain unchanged."
  ],
  "not_resolved_or_not_claimed": [
    "Blueprint scope conflict remains PARTIAL/UNKNOWN.",
    "Actual roster/qualification, real authorization, execution, learner records, Human or association acceptance remain UNKNOWN.",
    "No DOCX or Word visual QA has been produced for R04."
  ],
  "recorded_at_utc": "2026-10-29T16:06:21.580189+00:00"
}

## R04 writer receipt reconciliation
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\worker\WRITER_RECEIPT_RECONCILIATION_R04.json
source_sha256=485e273cc16547163fb763222ea8a36846a22b6f87f06ccbeca513df69c0abd5
source_bytes=1517

{
  "receipt_type": "writer_receipt_count_reconciliation",
  "doc_id": "0010",
  "requirement_id": "I02-E01",
  "revision": "R04",
  "supersedes_only": "R03 writer-receipt prose count; does not rewrite the historical R03 receipt",
  "historical_r03_writer_receipt_sha256": "e43f49c14c594f6a97a59ddb1841b1481121b3bd7fbb41bfb4835cd85b02ab9f",
  "historical_inconsistency": "R03 construction prose says 120 fact rows; its structured field and the verified embedded/sidecar register each contain 157.",
  "r04_candidate_text": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\\worker\\0010_I02-E01_R04.md",
    "sha256": "131b703267feebfbef3ec49fc8aa9beaab2ded0818415e9e5d86771b84925d90"
  },
  "r04_embedded_register": {
    "rows": 157,
    "unique_ids": 157,
    "sha256": "131b703267feebfbef3ec49fc8aa9beaab2ded0818415e9e5d86771b84925d90"
  },
  "r04_sidecar_register": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\\worker\\SYNTHETIC_REGISTER_R04.md",
    "rows": 157,
    "unique_ids": 157,
    "sha256": "6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc"
  },
  "row_ids_identical": true,
  "content_claim_corrected_to": 157,
  "arithmetic_or_real_evidence_claim": "No arithmetic was changed. This is a receipt reconciliation, not evidence of REAL activity or formal acceptance.",
  "recorded_at_utc": "2026-10-29T16:06:21.574217+00:00"
}

## R04 complete candidate
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\worker\0010_I02-E01_R04.md
source_sha256=131b703267feebfbef3ec49fc8aa9beaab2ded0818415e9e5d86771b84925d90
source_bytes=44641

# 學員訓練成果評核標準與說明｜R04

**狀態：SAMPLE/SYNTHETIC 文字候選；未核准、未生效、未建 DOCX。** 所有示例題目、作答、角色、覆核事件、行為、日期若有、數值及分析均為虛構，不指稱真實學員、協會採用、實際施測或實際覆核。

## 1. 官方要求及範圍

官方《TTQS查核佐證文件資料表—訓練機構版》第1頁指標2原文：「對學員訓練成果有評核標準的訂定及說明。」本件說明學習目標、題目與任務、評分錨點、權重、門檻及覆核，範圍為學員結果。0009/I01-E06是組織年度績效目標；0011/I02-E02是訓練政策及產品／市場定位，均非本件替代品。

**F-05 CONTROL_SCOPE_CONFLICT：PARTIAL/UNKNOWN。** Blueprint列另列對外承諾／公開揭露與政策檢討完成率；官方I02-E01原文未支持這些額外政策欄位，範圍待權責控制者確認。本稿不擴張承諾、不加政策指標、不改Blueprint，也不聲稱完全符合Blueprint。此衝突不停止本次候選修補。

## 2. 流程及紀錄

|步驟|責任|必要紀錄／控制|
|---|---|---|
|目標映射與版本|課程負責人、核定者|課程目標、題本、答案鍵、量尺、門檻、版本及評核前公告|
|施測|主評核者|逐題原始作答、題本版本、各指標原始行為證據|
|獨立覆核|未參與該案原評分者|重新核答案、證據、錨點、計算、門檻；記錄差異及結論|
|回饋複評|課程負責人及評核角色|差距、練習、新題版本；清楚標示新評或首次沿用|
|保存分析|紀錄管理者|受控學員碼至原件、計算、覆核及通知的索引|

紀錄至少包含目標／題本版本、受控代碼、逐題答案、每項原始等級與證據、主評角色、獨立覆核角色及已完成事件、計算、門檻、補救、複評、更正及來源定位。角色指派不等於覆核完成。

## 3. 唯一目標配題及分母

LO1「10題」是Q1–Q10子集。全卷固定20題，每題1分、總分母20；四目標互斥且總和20。

|目標|題號|題數|構念|目標內分母／全卷分母|答案鍵|
|---|---|---:|---|---|---|
|LO1|Q1–Q10|10|流程、需求、用途、結案|10/20|§4 Q1–Q10|
|LO2|Q11–Q14|4|授權、最少必要、停止升級|4/20|§4 Q11–Q14|
|LO3|Q15–Q17|3|來源、未知、交接|3/20|§4 Q15–Q17|
|LO4|Q18–Q20|3|溝通、理解、承諾界線|3/20|§4 Q18–Q20|
|合計|Q1–Q20|20|四項構念|20/20|逐題鍵|

## 4. SAMPLE/SYNTHETIC完整題本、四選項及鍵

作答指示：20題單選、限時20分鐘；答對1分，答錯／空白／多選0分。共同情境為虛構櫃台詢問；只採各題已給資訊，未提供授權、身分及狀態均為未知。
|題|題幹|A|B|C|D|
|---|---|---|---|---|---|
|Q1|櫃台接待第一步|查全檔|釐清需求並說明用途|先承諾|索取無關資料|
|Q2|只問進度時|確認具體事項|查看全部|交付全檔|結束|
|Q3|用途未明時|先複製|告知用途並確認|擴大查詢|自行改用途|
|Q4|必要資料缺漏|猜填|標未知並查證|填常見值|刪除|
|Q5|超出服務範圍|保證成功|說明限制並指引管道|私下查詢|不記錄|
|Q6|結案前|確認已做與未完|只說完成|保證結果|不告知|
|Q7|部分已知部分待查|全記完成|分列已知待查|刪除待查|猜測|
|Q8|對方更正資料|留更正軌跡|無痕覆寫|選方便值|忽略|
|Q9|交接未結事項|列需求步驟未決接手人|交所有資料|只寫處理|不指定|
|Q10|結案記錄|可核對處置及下一步|評價個性|保證未知|取代原件|
|Q11|沒有授權可否查受限資料|可以|先核授權用途|先查後補|旁人代查|
|Q12|僅授權一項查詢|只查必要資料|看全檔|下載|轉傳|
|Q13|授權範圍不明|停止並確認|最大範圍解讀|先揭露|推測|
|Q14|第三人無授權索資料|只說公開流程|口頭透露|傳截圖|讓其查看|
|Q15|如何記錄來源|區分陳述核實未知|全寫核實|不註來源|補足|
|Q16|日期未核實|標未知並記查證|填今天|估日期|留白|
|Q17|交接追溯欄|角色已做依據下一步|評語|背景|模糊寫處理|
|Q18|說明狀態|清楚中性說已知未知|保證|縮寫|責怪|
|Q19|確認理解|請對方說下一步並澄清|問懂否即結束|假設點頭|不給問|
|Q20|結果未核實|說未知及管道不保證|保證核准|暗示完成|可能說事實|
答案鍵Q1–Q20依序：B, A, B, B, B, A, B, A, A, A, B, A, A, A, A, A, A, A, A, A。鍵與題本版本綁定，不一致即HOLD。

## 5. 構面及權重

知識20題×1=20；P1–P4各10分、合計40；C1–C5各5分、合計25；M1–M3各5分、合計15；總分100。實作使用腳本CASE-SYN-17：虛構來訪者問申請進度，未附可核對授權、系統狀態未提供。受評者須確認需求、說用途、辨識授權缺口、停止受限存取、記錄已知／未知／來源／責任／下一步，並作清楚交接及理解確認；評核者只照讀卡片、不提示。不得假設身分已驗證或查看／揭露受限資料。

### SAMPLE/SYNTHETIC 情境控制卡（CASE-SYN-17）

本卡只設定評核輸入；不是實際個案、授權、申請紀錄或系統查詢結果。未知欄位不得由受評者或評核者補猜。

|控制欄位|SAMPLE/SYNTHETIC值|評核操作及停辦條件|
|---|---|---|
|情境代碼／情境內容|CASE-SYN-17；虛構服務進度詢問|同一版腳本供同次示範；更換版本須重新核對題本與評核錨點。|
|可核對授權|未提供；UNKNOWN|受評者先確認授權及用途；未核實前停止受限存取，不索取或揭露超出必要範圍的資料。|
|系統狀態|未提供；UNKNOWN|不可推定已受理、完成、核准或拒絕；只能說明目前無可核實狀態並交代查證管道。|
|狀態來源及擷取時間|未提供；UNKNOWN|評核者不得把口述、推測或本示範資料當作系統原件；須記錄查證來源與時間或明列未知。|
|REAL替換核對|實際核定情境及其授權／狀態原件尚未提供|採 REAL 前核對正式情境版本、用途授權、適用範圍、狀態來源及擷取時間；任一缺失或衝突即 UNKNOWN/HOLD。|



## 6. 主文整合的指標專屬0–4錨點

公式仍為等級÷4×指標權重；下表是唯一專屬定級標準。
|指標|4級|3級|2級|1級|0級|
|---|---|---|---|---|---|
|P1需求流程|獨立依序確認需求用途處置結案|步驟正確小漏自改|漏必要步驟提示後補|多步錯仍未改|未作或捏造|
|P2紀錄|標來源區分已知未知一致|核心正確小漏自補|漏重要欄提示後補|多處錯未改|無紀錄或不實|
|P3授權核心|先核用途最少取用疑即停升級|未越權且完成確認|提示後、存取前停止|提示後仍嘗試越權|未授權存取揭露即HOLD|
|P4交接|處置合宜交代接手未決下一步|正確主要交接全|漏欄提示後補|處置不符|無處置或捏造|
|C1需求|準確指出需求目標限制未知|正確小漏|提示後區分|推測當需求|無法指出|
|C2依據|逐結論連來源標未知|主要正確小漏自改|漏重要依據提示後補|多項無據|偽造|
|C3行動|全程符合需求授權流程|主要合宜小差自改|一步提示後改|不符未改|違核心|
|C4完整|來源步驟角色未知下一步全|核心完整|漏欄提示補|多欄缺漏|不實|
|C5限制|區分結果未知限制升級|正確說明主要限制|漏限制提示補|誇大未改|捏造|
|M1溝通|清楚中性尊重完整|清楚有禮|含糊提示後澄清|仍不清或不尊重|威嚇拒溝通|
|M2理解授權|確認理解授權後才前進|兩者完成|提示後補一項|提示後仍漏|未確認即存取|
|M3下一步|說明責任步驟未知界線|清楚無保證|漏項提示補|無據承諾|未知說成保證|

## 7. 門檻、複評及HOLD

總分=知識+P+C+M，保留精確值加總後顯示兩位。通過須同時：總分≥70/100、知識≥12/20、實作≥28/40、P3≥3/4。權重及門檻是候選內規值，非官方指定。版本不明、證據缺漏、利益衝突、核算不一致或獨立覆核未完成時HOLD，不發布能力判定。

## 8. SAMPLE/SYNTHETIC逐題答卷與首次計算

作答按Q1–Q20順序。§4答案鍵與下列向量逐題比較即可重算知識分。此例D皆為錯答。
|個案|逐題向量|知識|P向量 /40|C向量 /25|M向量 /15|總分|門檻|
|---|---|---:|---|---|---|---:|---|
|SYN-001|B,A,B,B,B,A,B,A,A,A,B,A,A,A,A,A,D,D,D,D|16/20|[4,3,3,4]=35|[3,4,3,3,4]=21.25|[3,3,4]=12.5|84.75|通過|
|SYN-002|B,A,B,B,B,A,B,A,A,A,B,A,A,D,D,D,D,D,D,D|13/20|[3,3,3,3]=30|[3,3,2,3,3]=17.5|[3,2,3]=10|70.50|通過|
|SYN-003|B,A,B,B,B,A,B,A,A,A,B,A,A,A,A,A,A,D,D,D|17/20|[2,2,1,2]=17.5|[4,4,3,3,4]=22.5|[4,3,3]=12.5|69.50|未達|
|SYN-004|B,A,B,B,B,A,B,A,A,A,B,D,D,D,D,D,D,D,D,D|11/20|[4,3,2,3]=30|[4,3,4,3,4]=22.5|[3,3,3]=11.25|74.75|未達|

## 9. 每一評等的原始SAMPLE/SYNTHETIC行為證據

EV為合成原始觀察記錄；每個等級以§6相同指標的行為錨點定級，證據句明列觀察行為，可逐列重評。主評角色是指派欄；覆核完成事件另列§10。
|EV ID|個案|階段|指標|原始合成觀察|等級|主評角色|
|---|---|---|---|---|---:|---|
|EV-SYN-001-P1-F|SYN-001|首次|P1|獨立依序確認需求用途處置結案|4|ROLE-EVAL-SYN|
|EV-SYN-001-P2-F|SYN-001|首次|P2|核心正確小漏自補|3|ROLE-EVAL-SYN|
|EV-SYN-001-P3-F|SYN-001|首次|P3|未越權且完成確認|3|ROLE-EVAL-SYN|
|EV-SYN-001-P4-F|SYN-001|首次|P4|處置合宜交代接手未決下一步|4|ROLE-EVAL-SYN|
|EV-SYN-001-C1-F|SYN-001|首次|C1|正確小漏|3|ROLE-EVAL-SYN|
|EV-SYN-001-C2-F|SYN-001|首次|C2|逐結論連來源標未知|4|ROLE-EVAL-SYN|
|EV-SYN-001-C3-F|SYN-001|首次|C3|主要合宜小差自改|3|ROLE-EVAL-SYN|
|EV-SYN-001-C4-F|SYN-001|首次|C4|核心完整|3|ROLE-EVAL-SYN|
|EV-SYN-001-C5-F|SYN-001|首次|C5|區分結果未知限制升級|4|ROLE-EVAL-SYN|
|EV-SYN-001-M1-F|SYN-001|首次|M1|清楚有禮|3|ROLE-EVAL-SYN|
|EV-SYN-001-M2-F|SYN-001|首次|M2|兩者完成|3|ROLE-EVAL-SYN|
|EV-SYN-001-M3-F|SYN-001|首次|M3|說明責任步驟未知界線|4|ROLE-EVAL-SYN|
|EV-SYN-002-P1-F|SYN-002|首次|P1|步驟正確小漏自改|3|ROLE-EVAL-SYN|
|EV-SYN-002-P2-F|SYN-002|首次|P2|核心正確小漏自補|3|ROLE-EVAL-SYN|
|EV-SYN-002-P3-F|SYN-002|首次|P3|未越權且完成確認|3|ROLE-EVAL-SYN|
|EV-SYN-002-P4-F|SYN-002|首次|P4|正確主要交接全|3|ROLE-EVAL-SYN|
|EV-SYN-002-C1-F|SYN-002|首次|C1|正確小漏|3|ROLE-EVAL-SYN|
|EV-SYN-002-C2-F|SYN-002|首次|C2|主要正確小漏自改|3|ROLE-EVAL-SYN|
|EV-SYN-002-C3-F|SYN-002|首次|C3|一步提示後改|2|ROLE-EVAL-SYN|
|EV-SYN-002-C4-F|SYN-002|首次|C4|核心完整|3|ROLE-EVAL-SYN|
|EV-SYN-002-C5-F|SYN-002|首次|C5|正確說明主要限制|3|ROLE-EVAL-SYN|
|EV-SYN-002-M1-F|SYN-002|首次|M1|清楚有禮|3|ROLE-EVAL-SYN|
|EV-SYN-002-M2-F|SYN-002|首次|M2|提示後補一項|2|ROLE-EVAL-SYN|
|EV-SYN-002-M3-F|SYN-002|首次|M3|清楚無保證|3|ROLE-EVAL-SYN|
|EV-SYN-003-P1-F|SYN-003|首次|P1|漏必要步驟提示後補|2|ROLE-EVAL-SYN|
|EV-SYN-003-P2-F|SYN-003|首次|P2|漏重要欄提示後補|2|ROLE-EVAL-SYN|
|EV-SYN-003-P3-F|SYN-003|首次|P3|提示後仍嘗試越權|1|ROLE-EVAL-SYN|
|EV-SYN-003-P4-F|SYN-003|首次|P4|漏欄提示後補|2|ROLE-EVAL-SYN|
|EV-SYN-003-C1-F|SYN-003|首次|C1|準確指出需求目標限制未知|4|ROLE-EVAL-SYN|
|EV-SYN-003-C2-F|SYN-003|首次|C2|逐結論連來源標未知|4|ROLE-EVAL-SYN|
|EV-SYN-003-C3-F|SYN-003|首次|C3|主要合宜小差自改|3|ROLE-EVAL-SYN|
|EV-SYN-003-C4-F|SYN-003|首次|C4|核心完整|3|ROLE-EVAL-SYN|
|EV-SYN-003-C5-F|SYN-003|首次|C5|區分結果未知限制升級|4|ROLE-EVAL-SYN|
|EV-SYN-003-M1-F|SYN-003|首次|M1|清楚中性尊重完整|4|ROLE-EVAL-SYN|
|EV-SYN-003-M2-F|SYN-003|首次|M2|兩者完成|3|ROLE-EVAL-SYN|
|EV-SYN-003-M3-F|SYN-003|首次|M3|清楚無保證|3|ROLE-EVAL-SYN|
|EV-SYN-004-P1-F|SYN-004|首次|P1|獨立依序確認需求用途處置結案|4|ROLE-EVAL-SYN|
|EV-SYN-004-P2-F|SYN-004|首次|P2|核心正確小漏自補|3|ROLE-EVAL-SYN|
|EV-SYN-004-P3-F|SYN-004|首次|P3|提示後、存取前停止|2|ROLE-EVAL-SYN|
|EV-SYN-004-P4-F|SYN-004|首次|P4|正確主要交接全|3|ROLE-EVAL-SYN|
|EV-SYN-004-C1-F|SYN-004|首次|C1|準確指出需求目標限制未知|4|ROLE-EVAL-SYN|
|EV-SYN-004-C2-F|SYN-004|首次|C2|主要正確小漏自改|3|ROLE-EVAL-SYN|
|EV-SYN-004-C3-F|SYN-004|首次|C3|全程符合需求授權流程|4|ROLE-EVAL-SYN|
|EV-SYN-004-C4-F|SYN-004|首次|C4|核心完整|3|ROLE-EVAL-SYN|
|EV-SYN-004-C5-F|SYN-004|首次|C5|區分結果未知限制升級|4|ROLE-EVAL-SYN|
|EV-SYN-004-M1-F|SYN-004|首次|M1|清楚有禮|3|ROLE-EVAL-SYN|
|EV-SYN-004-M2-F|SYN-004|首次|M2|兩者完成|3|ROLE-EVAL-SYN|
|EV-SYN-004-M3-F|SYN-004|首次|M3|清楚無保證|3|ROLE-EVAL-SYN|

## 10. 覆核事件與職責分離（SAMPLE/SYNTHETIC）

ROLE-EVAL-SYN為被指派主評碼，ROLE-REVIEW-SYN為另一獨立覆核碼。事件欄列出模擬核對範圍及重算結果，區分指派與完成；不代表真人、資格或實際發生。
|個案|主評角色|覆核角色|完成事件ID|獨立核對資料及重算結果|
|---|---|---|---|---|
|SYN-001|ROLE-EVAL-SYN|ROLE-REVIEW-SYN|REV-SYN-001|20答題、12筆EV、構面及門檻；重算16、84.75，通過|
|SYN-002|ROLE-EVAL-SYN|ROLE-REVIEW-SYN|REV-SYN-002|20答題、12筆EV、構面及門檻；重算13、70.50，通過|
|SYN-003|ROLE-EVAL-SYN|ROLE-REVIEW-SYN|REV-SYN-003|20答題、12筆EV及門檻；重算17、69.50，實作/P3未達|
|SYN-004|ROLE-EVAL-SYN|ROLE-REVIEW-SYN|REV-SYN-004|20答題、12筆EV及門檻；重算11、74.75，知識/P3未達|

## 11. 複評新觀察及沿用追溯

|新測驗向量|個案|Q1–Q20逐題作答|答對分母|
|---|---|---|---:|
|RET-SYN-003|SYN-003|B,A,B,B,B,A,B,A,A,A,B,A,A,A,A,A,A,D,D,D|17/20|
|RET-SYN-004|SYN-004|B,A,B,B,B,A,B,A,A,A,B,A,A,A,D,D,D,D,D,D|14/20|

SYN-003知識新卷仍17/20，並重評全部四項P，新的評等[3,3,3,3]、30/40。SYN-004知識新卷14/20；P3新評3，P1=4、P2=3、P4=3沿用首次SF-073/SF-074/SF-076，非新觀察。
|EV ID|個案|新觀察／指標|原始合成行為|等級|來源性質|
|---|---|---|---|---:|---|
|EV-SYN-003-P1-R1|SYN-003|P1|新情境依序確認需求用途並結案|3|新複評|
|EV-SYN-003-P2-R1|SYN-003|P2|新紀錄標來源及未知，提示後補重要欄|3|新複評|
|EV-SYN-003-P3-R1|SYN-003|P3|先辨識授權缺口，停止存取並升級|3|新複評|
|EV-SYN-003-P4-R1|SYN-003|P4|新交接列接手、未決及下一步|3|新複評|
|EV-SYN-004-P3-R1|SYN-004|P3|自行辨識授權缺口、停止查詢、未存取揭露|3|新P3複評|

SYN-003複評覆核事件REV-SYN-003-R1核對新知識答卷及四項新EV；總分17+30+22.50+12.50=82.00。SYN-004事件REV-SYN-004-R1核對新知識答卷、新P3 EV、P1/P2/P4首次來源、計算；實作(4+3+3+3)×2.5=32.50，總分14+32.50+22.50+11.25=80.25。兩例均符合四門檻。沿用值不冒充新觀察。

## 12. 彙總及分母

四是合成有效首次個案數；差距可重疊。均值先用精確值算，再於顯示時四捨五入。
|統計|算法|SAMPLE/SYNTHETIC結果|
|---|---|---:|
|首次通過率|2/4|50%|
|複評參與率|2/4|50%|
|複評後達標率|4/4|100%|
|首次P3未達|2/4|50%|
|首次實作未達|1/4|25%|
|首次知識未達|1/4|25%|
|首次通過組均值：知識／實作／案例／溝通／總分|兩例平均|14.50 / 32.50 / 19.375(19.38) / 11.25 / 77.625(77.63)|
|補救組均值：知識／實作／案例／溝通／總分|兩例平均|14.00 / 23.75 / 22.50 / 11.875(11.88) / 72.125(72.13)|

## 13. 小型志工協會配置

每案至少兩名不同、無衝突人員分任主評和獨立覆核；其中一人可兼任非評分的排程、版本保管及通知。預先指定已完成本量尺校準且經協會授權的跨場次備援；外部覆核者僅在權責主管事前授權、保密及可追溯委任後使用，不假設人選存在。不可同人兼主評與覆核、覆核自己的評分或辦理自己涉衝突案件申訴。若沒有合格覆核者／授權備援、衝突未分離或覆核未完成，HOLD。真實名冊及資格均UNKNOWN。

## 14. 負向鄰項、真實替換及限制

0009/I01-E06是組織年度績效目標分析；0011/I02-E02是訓練政策、產品與市場定位。本件只評學員訓練結果。真實採用前須取得核准課程目標、題本、公告、逐題答卷、觀察原件、角色資格及實際覆核紀錄；逐項替換合成資料並重算。缺原件維持UNKNOWN/HOLD。本文不宣稱真實採用、核准、學員、成果或實際覆核。

## 15. 原子SAMPLE/SYNTHETIC替換登錄

每列是一題（含其選項）、一個答案鍵、一份答卷向量、一個指標觀察、角色／事件或單一結果；有類型、個案、精確值、本文欄位和真實替換來源／核查方式。登錄在所有被引用資料之後。
|Fact ID|類型|Case ID|精確值|精確欄位定位|真實替換來源及核查|
|---|---|---|---|---|---|
|Q-Q1|合成題目與四選項|共用題本|櫃台接待第一步; A 查全檔; B 釐清需求並說明用途; C 先承諾; D 索取無關資料|§4題表Q1|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q2|合成題目與四選項|共用題本|只問進度時; A 確認具體事項; B 查看全部; C 交付全檔; D 結束|§4題表Q2|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q3|合成題目與四選項|共用題本|用途未明時; A 先複製; B 告知用途並確認; C 擴大查詢; D 自行改用途|§4題表Q3|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q4|合成題目與四選項|共用題本|必要資料缺漏; A 猜填; B 標未知並查證; C 填常見值; D 刪除|§4題表Q4|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q5|合成題目與四選項|共用題本|超出服務範圍; A 保證成功; B 說明限制並指引管道; C 私下查詢; D 不記錄|§4題表Q5|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q6|合成題目與四選項|共用題本|結案前; A 確認已做與未完; B 只說完成; C 保證結果; D 不告知|§4題表Q6|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q7|合成題目與四選項|共用題本|部分已知部分待查; A 全記完成; B 分列已知待查; C 刪除待查; D 猜測|§4題表Q7|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q8|合成題目與四選項|共用題本|對方更正資料; A 留更正軌跡; B 無痕覆寫; C 選方便值; D 忽略|§4題表Q8|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q9|合成題目與四選項|共用題本|交接未結事項; A 列需求步驟未決接手人; B 交所有資料; C 只寫處理; D 不指定|§4題表Q9|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q10|合成題目與四選項|共用題本|結案記錄; A 可核對處置及下一步; B 評價個性; C 保證未知; D 取代原件|§4題表Q10|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q11|合成題目與四選項|共用題本|沒有授權可否查受限資料; A 可以; B 先核授權用途; C 先查後補; D 旁人代查|§4題表Q11|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q12|合成題目與四選項|共用題本|僅授權一項查詢; A 只查必要資料; B 看全檔; C 下載; D 轉傳|§4題表Q12|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q13|合成題目與四選項|共用題本|授權範圍不明; A 停止並確認; B 最大範圍解讀; C 先揭露; D 推測|§4題表Q13|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q14|合成題目與四選項|共用題本|第三人無授權索資料; A 只說公開流程; B 口頭透露; C 傳截圖; D 讓其查看|§4題表Q14|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q15|合成題目與四選項|共用題本|如何記錄來源; A 區分陳述核實未知; B 全寫核實; C 不註來源; D 補足|§4題表Q15|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q16|合成題目與四選項|共用題本|日期未核實; A 標未知並記查證; B 填今天; C 估日期; D 留白|§4題表Q16|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q17|合成題目與四選項|共用題本|交接追溯欄; A 角色已做依據下一步; B 評語; C 背景; D 模糊寫處理|§4題表Q17|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q18|合成題目與四選項|共用題本|說明狀態; A 清楚中性說已知未知; B 保證; C 縮寫; D 責怪|§4題表Q18|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q19|合成題目與四選項|共用題本|確認理解; A 請對方說下一步並澄清; B 問懂否即結束; C 假設點頭; D 不給問|§4題表Q19|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q20|合成題目與四選項|共用題本|結果未核實; A 說未知及管道不保證; B 保證核准; C 暗示完成; D 可能說事實|§4題表Q20|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|KEY-Q1|合成答案鍵|共用題本|B|§4答案鍵Q1|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q2|合成答案鍵|共用題本|A|§4答案鍵Q2|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q3|合成答案鍵|共用題本|B|§4答案鍵Q3|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q4|合成答案鍵|共用題本|B|§4答案鍵Q4|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q5|合成答案鍵|共用題本|B|§4答案鍵Q5|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q6|合成答案鍵|共用題本|A|§4答案鍵Q6|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q7|合成答案鍵|共用題本|B|§4答案鍵Q7|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q8|合成答案鍵|共用題本|A|§4答案鍵Q8|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q9|合成答案鍵|共用題本|A|§4答案鍵Q9|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q10|合成答案鍵|共用題本|A|§4答案鍵Q10|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q11|合成答案鍵|共用題本|B|§4答案鍵Q11|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q12|合成答案鍵|共用題本|A|§4答案鍵Q12|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q13|合成答案鍵|共用題本|A|§4答案鍵Q13|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q14|合成答案鍵|共用題本|A|§4答案鍵Q14|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q15|合成答案鍵|共用題本|A|§4答案鍵Q15|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q16|合成答案鍵|共用題本|A|§4答案鍵Q16|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q17|合成答案鍵|共用題本|A|§4答案鍵Q17|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q18|合成答案鍵|共用題本|A|§4答案鍵Q18|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q19|合成答案鍵|共用題本|A|§4答案鍵Q19|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q20|合成答案鍵|共用題本|A|§4答案鍵Q20|同版核准答案鍵與未參與出題者覆核。|
|ANS-SYN-001-FIRST|逐題作答向量|SYN-001|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:D,Q18:D,Q19:D,Q20:D|§8 SYN-001-FIRST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-002-FIRST|逐題作答向量|SYN-002|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:D,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D|§8 SYN-002-FIRST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-003-FIRST|逐題作答向量|SYN-003|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:A,Q18:D,Q19:D,Q20:D|§8 SYN-003-FIRST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-004-FIRST|逐題作答向量|SYN-004|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:D,Q13:D,Q14:D,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D|§8 SYN-004-FIRST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-003-RETEST|逐題作答向量|SYN-003|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:A,Q18:D,Q19:D,Q20:D|§8 SYN-003-RETEST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-004-RETEST|逐題作答向量|SYN-004|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D|§8 SYN-004-RETEST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|EV-SYN-001-P1-F|合成原始行為及評等|SYN-001|等級4；獨立依序確認需求用途處置結案|§9 SYN-001 P1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-P2-F|合成原始行為及評等|SYN-001|等級3；核心正確小漏自補|§9 SYN-001 P2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-P3-F|合成原始行為及評等|SYN-001|等級3；未越權且完成確認|§9 SYN-001 P3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-P4-F|合成原始行為及評等|SYN-001|等級4；處置合宜交代接手未決下一步|§9 SYN-001 P4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C1-F|合成原始行為及評等|SYN-001|等級3；正確小漏|§9 SYN-001 C1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C2-F|合成原始行為及評等|SYN-001|等級4；逐結論連來源標未知|§9 SYN-001 C2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C3-F|合成原始行為及評等|SYN-001|等級3；主要合宜小差自改|§9 SYN-001 C3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C4-F|合成原始行為及評等|SYN-001|等級3；核心完整|§9 SYN-001 C4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C5-F|合成原始行為及評等|SYN-001|等級4；區分結果未知限制升級|§9 SYN-001 C5表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-M1-F|合成原始行為及評等|SYN-001|等級3；清楚有禮|§9 SYN-001 M1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-M2-F|合成原始行為及評等|SYN-001|等級3；兩者完成|§9 SYN-001 M2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-M3-F|合成原始行為及評等|SYN-001|等級4；說明責任步驟未知界線|§9 SYN-001 M3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-P1-F|合成原始行為及評等|SYN-002|等級3；步驟正確小漏自改|§9 SYN-002 P1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-P2-F|合成原始行為及評等|SYN-002|等級3；核心正確小漏自補|§9 SYN-002 P2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-P3-F|合成原始行為及評等|SYN-002|等級3；未越權且完成確認|§9 SYN-002 P3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-P4-F|合成原始行為及評等|SYN-002|等級3；正確主要交接全|§9 SYN-002 P4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C1-F|合成原始行為及評等|SYN-002|等級3；正確小漏|§9 SYN-002 C1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C2-F|合成原始行為及評等|SYN-002|等級3；主要正確小漏自改|§9 SYN-002 C2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C3-F|合成原始行為及評等|SYN-002|等級2；一步提示後改|§9 SYN-002 C3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C4-F|合成原始行為及評等|SYN-002|等級3；核心完整|§9 SYN-002 C4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C5-F|合成原始行為及評等|SYN-002|等級3；正確說明主要限制|§9 SYN-002 C5表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-M1-F|合成原始行為及評等|SYN-002|等級3；清楚有禮|§9 SYN-002 M1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-M2-F|合成原始行為及評等|SYN-002|等級2；提示後補一項|§9 SYN-002 M2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-M3-F|合成原始行為及評等|SYN-002|等級3；清楚無保證|§9 SYN-002 M3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P1-F|合成原始行為及評等|SYN-003|等級2；漏必要步驟提示後補|§9 SYN-003 P1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P2-F|合成原始行為及評等|SYN-003|等級2；漏重要欄提示後補|§9 SYN-003 P2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P3-F|合成原始行為及評等|SYN-003|等級1；提示後仍嘗試越權|§9 SYN-003 P3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P4-F|合成原始行為及評等|SYN-003|等級2；漏欄提示後補|§9 SYN-003 P4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C1-F|合成原始行為及評等|SYN-003|等級4；準確指出需求目標限制未知|§9 SYN-003 C1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C2-F|合成原始行為及評等|SYN-003|等級4；逐結論連來源標未知|§9 SYN-003 C2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C3-F|合成原始行為及評等|SYN-003|等級3；主要合宜小差自改|§9 SYN-003 C3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C4-F|合成原始行為及評等|SYN-003|等級3；核心完整|§9 SYN-003 C4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C5-F|合成原始行為及評等|SYN-003|等級4；區分結果未知限制升級|§9 SYN-003 C5表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-M1-F|合成原始行為及評等|SYN-003|等級4；清楚中性尊重完整|§9 SYN-003 M1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-M2-F|合成原始行為及評等|SYN-003|等級3；兩者完成|§9 SYN-003 M2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-M3-F|合成原始行為及評等|SYN-003|等級3；清楚無保證|§9 SYN-003 M3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-P1-F|合成原始行為及評等|SYN-004|等級4；獨立依序確認需求用途處置結案|§9 SYN-004 P1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-P2-F|合成原始行為及評等|SYN-004|等級3；核心正確小漏自補|§9 SYN-004 P2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-P3-F|合成原始行為及評等|SYN-004|等級2；提示後、存取前停止|§9 SYN-004 P3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-P4-F|合成原始行為及評等|SYN-004|等級3；正確主要交接全|§9 SYN-004 P4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C1-F|合成原始行為及評等|SYN-004|等級4；準確指出需求目標限制未知|§9 SYN-004 C1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C2-F|合成原始行為及評等|SYN-004|等級3；主要正確小漏自改|§9 SYN-004 C2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C3-F|合成原始行為及評等|SYN-004|等級4；全程符合需求授權流程|§9 SYN-004 C3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C4-F|合成原始行為及評等|SYN-004|等級3；核心完整|§9 SYN-004 C4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C5-F|合成原始行為及評等|SYN-004|等級4；區分結果未知限制升級|§9 SYN-004 C5表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-M1-F|合成原始行為及評等|SYN-004|等級3；清楚有禮|§9 SYN-004 M1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-M2-F|合成原始行為及評等|SYN-004|等級3；兩者完成|§9 SYN-004 M2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-M3-F|合成原始行為及評等|SYN-004|等級3；清楚無保證|§9 SYN-004 M3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P1-R1|合成原始行為及評等|SYN-003|等級新複評；3|§11複評列EV-SYN-003-P1-R1|該次新複評原始觀察表，非首次來源。|
|EV-SYN-003-P2-R1|合成原始行為及評等|SYN-003|等級新複評；3|§11複評列EV-SYN-003-P2-R1|該次新複評原始觀察表，非首次來源。|
|EV-SYN-003-P3-R1|合成原始行為及評等|SYN-003|等級新複評；3|§11複評列EV-SYN-003-P3-R1|該次新複評原始觀察表，非首次來源。|
|EV-SYN-003-P4-R1|合成原始行為及評等|SYN-003|等級新複評；3|§11複評列EV-SYN-003-P4-R1|該次新複評原始觀察表，非首次來源。|
|EV-SYN-004-P3-R1|合成原始行為及評等|SYN-004|等級新P3複評；3|§11複評列EV-SYN-004-P3-R1|該次新複評原始觀察表，非首次來源。|
|ROLE-EVAL-SYN|角色碼|合成情境／角色|指定主評角色碼|§9主評欄|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|ROLE-REVIEW-SYN|角色碼|合成情境／角色|指定獨立覆核角色碼|§10覆核欄|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-001|覆核事件ID|合成情境／角色|模擬獨立核對，16/20及84.75一致|§10 SYN-001列|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-002|覆核事件ID|合成情境／角色|模擬獨立核對，13/20及70.50一致|§10 SYN-002列|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-003|覆核事件ID|合成情境／角色|模擬獨立核對，17/20及69.50一致|§10 SYN-003列|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-004|覆核事件ID|合成情境／角色|模擬獨立核對，11/20及74.75一致|§10 SYN-004列|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-003-R1|覆核事件ID|合成情境／角色|模擬核對新答卷及四項新P評等|§11複評說明|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-004-R1|覆核事件ID|合成情境／角色|模擬核對新答卷、新P3及沿用SF來源|§11複評說明|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|CASE-SYN-17|情境代碼|CASE-SYN-17|虛構服務進度詢問|§5 SAMPLE/SYNTHETIC情境控制卡：情境代碼、授權、狀態及來源時間|REAL替換時核對實際核定情境版本、用途授權範圍、狀態原件及擷取時間；缺項或衝突即UNKNOWN/HOLD，不以本SAMPLE推定。|
|SYN-NO-AUTH|情境事實|CASE-SYN-17|未附可核對授權|§5情境控制卡：可核對授權欄|查實際核定情境的授權原件、用途及適用範圍；無證據即停止受限存取並記UNKNOWN/HOLD。|
|SYN-STATUS-UNK|情境事實|CASE-SYN-17|系統狀態未提供|§5情境控制卡：系統狀態、來源及擷取時間欄|核對具權限的狀態原件／查詢輸出與擷取時間；沒有可核實來源就維持UNKNOWN，不宣稱受理或核准。|
|N-01|合成計算結果|合成班次|2/4=50%|§12列1|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-02|合成計算結果|合成班次|2/4=50%|§12列2|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-03|合成計算結果|合成班次|4/4=100%|§12列3|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-04|合成計算結果|合成班次|2/4=50%|§12列4|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-05|合成計算結果|合成班次|1/4=25%|§12列5|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-06|合成計算結果|合成班次|1/4=25%|§12列6|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|M-01|合成計算結果|合成班次|14.50,32.50,19.375,11.25,77.625|§12列7|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|M-02|合成計算結果|合成班次|14.00,23.75,22.50,11.875,72.125|§12列8|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|RET-003|合成計算結果|合成班次|82.00=17+30+22.50+12.50|§11複評計算段：SYN-003總分算式及門檻|依該段列示的新知識答卷、四項新P觀察、沿用C/M分數與權重重算；核對未四捨五入分值及四門檻。|
|RET-004|合成計算結果|合成班次|80.25=14+32.50+22.50+11.25|§11複評計算段：SYN-004總分算式及門檻|依該段列示的新知識答卷、新P3、沿用P1/P2/P4及C/M分數重算；核對未四捨五入分值及四門檻。|
|SF-073|合成更正定位|SYN-004首次P1沿用|4；§8首次P向量第1格|§8表SYN-004首次P向量第1格|核首次評分原件，不作新評。|
|SF-074|合成更正定位|SYN-004首次P2沿用|3；§8首次P向量第2格|§8表SYN-004首次P向量第2格|核首次評分原件，不作新評。|
|SF-076|合成更正定位|SYN-004首次P4沿用|3；§8首次P向量第4格|§8表SYN-004首次P向量第4格|核首次評分原件，不作新評。|
|SF-099|合成更正定位|SYN-003新P1複評|3；EV-SYN-003-P1-R1|§11複評新觀察EV-SYN-003-P1-R1|新複評觀察原件，不得沿用。|
|SF-100|合成更正定位|SYN-003新P2複評|3；EV-SYN-003-P2-R1|§11複評新觀察EV-SYN-003-P2-R1|新複評觀察原件，不得沿用。|
|SF-101|合成更正定位|SYN-003新P3複評|3；EV-SYN-003-P3-R1|§11複評新觀察EV-SYN-003-P3-R1|新授權情境觀察。|
|SF-102|合成更正定位|SYN-003新P4複評|3；EV-SYN-003-P4-R1|§11複評新觀察EV-SYN-003-P4-R1|新交接觀察，不得沿用。|
|SF-110|合成更正定位|SYN-004首次P1沿用|4；SF-073|§11沿用首次SF-073|核首次來源，不造新觀察。|
|SF-111|合成更正定位|SYN-004首次P2沿用|3；SF-074|§11沿用首次SF-074|核首次來源，不造新觀察。|
|SF-112|合成更正定位|SYN-004新P3複評|3；EV-SYN-004-P3-R1|§11新P3觀察EV-SYN-004-P3-R1|新P3複評觀察原件。|
|SF-113|合成更正定位|SYN-004首次P4沿用|3；SF-076|§11沿用首次SF-076|核首次來源，不造新觀察。|
|SCORE-SYN-001-knowledge|合成衍生分數|SYN-001|16/20|§8表 SYN-001 knowledge欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-001-practical|合成衍生分數|SYN-001|35/40|§8表 SYN-001 practical欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-001-case|合成衍生分數|SYN-001|21.25/25|§8表 SYN-001 case欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-001-communication|合成衍生分數|SYN-001|12.5/15|§8表 SYN-001 communication欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-001-total|合成衍生分數|SYN-001|84.75/100|§8表 SYN-001 total欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-knowledge|合成衍生分數|SYN-002|13/20|§8表 SYN-002 knowledge欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-practical|合成衍生分數|SYN-002|30/40|§8表 SYN-002 practical欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-case|合成衍生分數|SYN-002|17.5/25|§8表 SYN-002 case欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-communication|合成衍生分數|SYN-002|10/15|§8表 SYN-002 communication欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-total|合成衍生分數|SYN-002|70.50/100|§8表 SYN-002 total欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-knowledge|合成衍生分數|SYN-003|17/20|§8表 SYN-003 knowledge欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-practical|合成衍生分數|SYN-003|17.5/40|§8表 SYN-003 practical欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-case|合成衍生分數|SYN-003|22.5/25|§8表 SYN-003 case欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-communication|合成衍生分數|SYN-003|12.5/15|§8表 SYN-003 communication欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-total|合成衍生分數|SYN-003|69.50/100|§8表 SYN-003 total欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-knowledge|合成衍生分數|SYN-004|11/20|§8表 SYN-004 knowledge欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-practical|合成衍生分數|SYN-004|30/40|§8表 SYN-004 practical欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-case|合成衍生分數|SYN-004|22.5/25|§8表 SYN-004 case欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-communication|合成衍生分數|SYN-004|11.25/15|§8表 SYN-004 communication欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-total|合成衍生分數|SYN-004|74.75/100|§8表 SYN-004 total欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-retest-knowledge|合成複評數值|SYN-003|17/20|§11複評計算列 SYN-003|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-003-retest-practical|合成複評數值|SYN-003|30/40|§11複評計算列 SYN-003|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-003-retest-total|合成複評數值|SYN-003|82.00/100|§11複評計算列 SYN-003|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-004-retest-knowledge|合成複評數值|SYN-004|14/20|§11複評計算列 SYN-004|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-004-retest-practical|合成複評數值|SYN-004|32.50/40|§11複評計算列 SYN-004|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-004-retest-total|合成複評數值|SYN-004|80.25/100|§11複評計算列 SYN-004|依新答卷、新EV及明列沿用原始分數重算。|

## R04 complete sidecar register
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\worker\SYNTHETIC_REGISTER_R04.md
source_sha256=6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc
source_bytes=28004

# 0010/I02-E01 R04｜SAMPLE/SYNTHETIC原子登錄

## 15. 原子SAMPLE/SYNTHETIC替換登錄

每列是一題（含其選項）、一個答案鍵、一份答卷向量、一個指標觀察、角色／事件或單一結果；有類型、個案、精確值、本文欄位和真實替換來源／核查方式。登錄在所有被引用資料之後。
|Fact ID|類型|Case ID|精確值|精確欄位定位|真實替換來源及核查|
|---|---|---|---|---|---|
|Q-Q1|合成題目與四選項|共用題本|櫃台接待第一步; A 查全檔; B 釐清需求並說明用途; C 先承諾; D 索取無關資料|§4題表Q1|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q2|合成題目與四選項|共用題本|只問進度時; A 確認具體事項; B 查看全部; C 交付全檔; D 結束|§4題表Q2|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q3|合成題目與四選項|共用題本|用途未明時; A 先複製; B 告知用途並確認; C 擴大查詢; D 自行改用途|§4題表Q3|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q4|合成題目與四選項|共用題本|必要資料缺漏; A 猜填; B 標未知並查證; C 填常見值; D 刪除|§4題表Q4|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q5|合成題目與四選項|共用題本|超出服務範圍; A 保證成功; B 說明限制並指引管道; C 私下查詢; D 不記錄|§4題表Q5|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q6|合成題目與四選項|共用題本|結案前; A 確認已做與未完; B 只說完成; C 保證結果; D 不告知|§4題表Q6|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q7|合成題目與四選項|共用題本|部分已知部分待查; A 全記完成; B 分列已知待查; C 刪除待查; D 猜測|§4題表Q7|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q8|合成題目與四選項|共用題本|對方更正資料; A 留更正軌跡; B 無痕覆寫; C 選方便值; D 忽略|§4題表Q8|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q9|合成題目與四選項|共用題本|交接未結事項; A 列需求步驟未決接手人; B 交所有資料; C 只寫處理; D 不指定|§4題表Q9|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q10|合成題目與四選項|共用題本|結案記錄; A 可核對處置及下一步; B 評價個性; C 保證未知; D 取代原件|§4題表Q10|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q11|合成題目與四選項|共用題本|沒有授權可否查受限資料; A 可以; B 先核授權用途; C 先查後補; D 旁人代查|§4題表Q11|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q12|合成題目與四選項|共用題本|僅授權一項查詢; A 只查必要資料; B 看全檔; C 下載; D 轉傳|§4題表Q12|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q13|合成題目與四選項|共用題本|授權範圍不明; A 停止並確認; B 最大範圍解讀; C 先揭露; D 推測|§4題表Q13|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q14|合成題目與四選項|共用題本|第三人無授權索資料; A 只說公開流程; B 口頭透露; C 傳截圖; D 讓其查看|§4題表Q14|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q15|合成題目與四選項|共用題本|如何記錄來源; A 區分陳述核實未知; B 全寫核實; C 不註來源; D 補足|§4題表Q15|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q16|合成題目與四選項|共用題本|日期未核實; A 標未知並記查證; B 填今天; C 估日期; D 留白|§4題表Q16|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q17|合成題目與四選項|共用題本|交接追溯欄; A 角色已做依據下一步; B 評語; C 背景; D 模糊寫處理|§4題表Q17|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q18|合成題目與四選項|共用題本|說明狀態; A 清楚中性說已知未知; B 保證; C 縮寫; D 責怪|§4題表Q18|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q19|合成題目與四選項|共用題本|確認理解; A 請對方說下一步並澄清; B 問懂否即結束; C 假設點頭; D 不給問|§4題表Q19|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|Q-Q20|合成題目與四選項|共用題本|結果未核實; A 說未知及管道不保證; B 保證核准; C 暗示完成; D 可能說事實|§4題表Q20|核定課程題本同題號、四選項及版本，逐項替換並覆核。|
|KEY-Q1|合成答案鍵|共用題本|B|§4答案鍵Q1|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q2|合成答案鍵|共用題本|A|§4答案鍵Q2|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q3|合成答案鍵|共用題本|B|§4答案鍵Q3|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q4|合成答案鍵|共用題本|B|§4答案鍵Q4|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q5|合成答案鍵|共用題本|B|§4答案鍵Q5|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q6|合成答案鍵|共用題本|A|§4答案鍵Q6|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q7|合成答案鍵|共用題本|B|§4答案鍵Q7|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q8|合成答案鍵|共用題本|A|§4答案鍵Q8|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q9|合成答案鍵|共用題本|A|§4答案鍵Q9|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q10|合成答案鍵|共用題本|A|§4答案鍵Q10|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q11|合成答案鍵|共用題本|B|§4答案鍵Q11|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q12|合成答案鍵|共用題本|A|§4答案鍵Q12|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q13|合成答案鍵|共用題本|A|§4答案鍵Q13|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q14|合成答案鍵|共用題本|A|§4答案鍵Q14|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q15|合成答案鍵|共用題本|A|§4答案鍵Q15|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q16|合成答案鍵|共用題本|A|§4答案鍵Q16|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q17|合成答案鍵|共用題本|A|§4答案鍵Q17|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q18|合成答案鍵|共用題本|A|§4答案鍵Q18|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q19|合成答案鍵|共用題本|A|§4答案鍵Q19|同版核准答案鍵與未參與出題者覆核。|
|KEY-Q20|合成答案鍵|共用題本|A|§4答案鍵Q20|同版核准答案鍵與未參與出題者覆核。|
|ANS-SYN-001-FIRST|逐題作答向量|SYN-001|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:D,Q18:D,Q19:D,Q20:D|§8 SYN-001-FIRST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-002-FIRST|逐題作答向量|SYN-002|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:D,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D|§8 SYN-002-FIRST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-003-FIRST|逐題作答向量|SYN-003|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:A,Q18:D,Q19:D,Q20:D|§8 SYN-003-FIRST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-004-FIRST|逐題作答向量|SYN-004|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:D,Q13:D,Q14:D,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D|§8 SYN-004-FIRST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-003-RETEST|逐題作答向量|SYN-003|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:A,Q18:D,Q19:D,Q20:D|§8 SYN-003-RETEST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|ANS-SYN-004-RETEST|逐題作答向量|SYN-004|Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D|§8 SYN-004-RETEST逐題向量|該案原始答卷；逐題依同版鍵重算。|
|EV-SYN-001-P1-F|合成原始行為及評等|SYN-001|等級4；獨立依序確認需求用途處置結案|§9 SYN-001 P1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-P2-F|合成原始行為及評等|SYN-001|等級3；核心正確小漏自補|§9 SYN-001 P2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-P3-F|合成原始行為及評等|SYN-001|等級3；未越權且完成確認|§9 SYN-001 P3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-P4-F|合成原始行為及評等|SYN-001|等級4；處置合宜交代接手未決下一步|§9 SYN-001 P4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C1-F|合成原始行為及評等|SYN-001|等級3；正確小漏|§9 SYN-001 C1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C2-F|合成原始行為及評等|SYN-001|等級4；逐結論連來源標未知|§9 SYN-001 C2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C3-F|合成原始行為及評等|SYN-001|等級3；主要合宜小差自改|§9 SYN-001 C3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C4-F|合成原始行為及評等|SYN-001|等級3；核心完整|§9 SYN-001 C4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-C5-F|合成原始行為及評等|SYN-001|等級4；區分結果未知限制升級|§9 SYN-001 C5表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-M1-F|合成原始行為及評等|SYN-001|等級3；清楚有禮|§9 SYN-001 M1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-M2-F|合成原始行為及評等|SYN-001|等級3；兩者完成|§9 SYN-001 M2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-001-M3-F|合成原始行為及評等|SYN-001|等級4；說明責任步驟未知界線|§9 SYN-001 M3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-P1-F|合成原始行為及評等|SYN-002|等級3；步驟正確小漏自改|§9 SYN-002 P1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-P2-F|合成原始行為及評等|SYN-002|等級3；核心正確小漏自補|§9 SYN-002 P2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-P3-F|合成原始行為及評等|SYN-002|等級3；未越權且完成確認|§9 SYN-002 P3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-P4-F|合成原始行為及評等|SYN-002|等級3；正確主要交接全|§9 SYN-002 P4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C1-F|合成原始行為及評等|SYN-002|等級3；正確小漏|§9 SYN-002 C1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C2-F|合成原始行為及評等|SYN-002|等級3；主要正確小漏自改|§9 SYN-002 C2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C3-F|合成原始行為及評等|SYN-002|等級2；一步提示後改|§9 SYN-002 C3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C4-F|合成原始行為及評等|SYN-002|等級3；核心完整|§9 SYN-002 C4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-C5-F|合成原始行為及評等|SYN-002|等級3；正確說明主要限制|§9 SYN-002 C5表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-M1-F|合成原始行為及評等|SYN-002|等級3；清楚有禮|§9 SYN-002 M1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-M2-F|合成原始行為及評等|SYN-002|等級2；提示後補一項|§9 SYN-002 M2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-002-M3-F|合成原始行為及評等|SYN-002|等級3；清楚無保證|§9 SYN-002 M3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P1-F|合成原始行為及評等|SYN-003|等級2；漏必要步驟提示後補|§9 SYN-003 P1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P2-F|合成原始行為及評等|SYN-003|等級2；漏重要欄提示後補|§9 SYN-003 P2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P3-F|合成原始行為及評等|SYN-003|等級1；提示後仍嘗試越權|§9 SYN-003 P3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P4-F|合成原始行為及評等|SYN-003|等級2；漏欄提示後補|§9 SYN-003 P4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C1-F|合成原始行為及評等|SYN-003|等級4；準確指出需求目標限制未知|§9 SYN-003 C1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C2-F|合成原始行為及評等|SYN-003|等級4；逐結論連來源標未知|§9 SYN-003 C2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C3-F|合成原始行為及評等|SYN-003|等級3；主要合宜小差自改|§9 SYN-003 C3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C4-F|合成原始行為及評等|SYN-003|等級3；核心完整|§9 SYN-003 C4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-C5-F|合成原始行為及評等|SYN-003|等級4；區分結果未知限制升級|§9 SYN-003 C5表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-M1-F|合成原始行為及評等|SYN-003|等級4；清楚中性尊重完整|§9 SYN-003 M1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-M2-F|合成原始行為及評等|SYN-003|等級3；兩者完成|§9 SYN-003 M2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-M3-F|合成原始行為及評等|SYN-003|等級3；清楚無保證|§9 SYN-003 M3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-P1-F|合成原始行為及評等|SYN-004|等級4；獨立依序確認需求用途處置結案|§9 SYN-004 P1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-P2-F|合成原始行為及評等|SYN-004|等級3；核心正確小漏自補|§9 SYN-004 P2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-P3-F|合成原始行為及評等|SYN-004|等級2；提示後、存取前停止|§9 SYN-004 P3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-P4-F|合成原始行為及評等|SYN-004|等級3；正確主要交接全|§9 SYN-004 P4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C1-F|合成原始行為及評等|SYN-004|等級4；準確指出需求目標限制未知|§9 SYN-004 C1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C2-F|合成原始行為及評等|SYN-004|等級3；主要正確小漏自改|§9 SYN-004 C2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C3-F|合成原始行為及評等|SYN-004|等級4；全程符合需求授權流程|§9 SYN-004 C3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C4-F|合成原始行為及評等|SYN-004|等級3；核心完整|§9 SYN-004 C4表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-C5-F|合成原始行為及評等|SYN-004|等級4；區分結果未知限制升級|§9 SYN-004 C5表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-M1-F|合成原始行為及評等|SYN-004|等級3；清楚有禮|§9 SYN-004 M1表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-M2-F|合成原始行為及評等|SYN-004|等級3；兩者完成|§9 SYN-004 M2表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-004-M3-F|合成原始行為及評等|SYN-004|等級3；清楚無保證|§9 SYN-004 M3表列|該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。|
|EV-SYN-003-P1-R1|合成原始行為及評等|SYN-003|等級新複評；3|§11複評列EV-SYN-003-P1-R1|該次新複評原始觀察表，非首次來源。|
|EV-SYN-003-P2-R1|合成原始行為及評等|SYN-003|等級新複評；3|§11複評列EV-SYN-003-P2-R1|該次新複評原始觀察表，非首次來源。|
|EV-SYN-003-P3-R1|合成原始行為及評等|SYN-003|等級新複評；3|§11複評列EV-SYN-003-P3-R1|該次新複評原始觀察表，非首次來源。|
|EV-SYN-003-P4-R1|合成原始行為及評等|SYN-003|等級新複評；3|§11複評列EV-SYN-003-P4-R1|該次新複評原始觀察表，非首次來源。|
|EV-SYN-004-P3-R1|合成原始行為及評等|SYN-004|等級新P3複評；3|§11複評列EV-SYN-004-P3-R1|該次新複評原始觀察表，非首次來源。|
|ROLE-EVAL-SYN|角色碼|合成情境／角色|指定主評角色碼|§9主評欄|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|ROLE-REVIEW-SYN|角色碼|合成情境／角色|指定獨立覆核角色碼|§10覆核欄|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-001|覆核事件ID|合成情境／角色|模擬獨立核對，16/20及84.75一致|§10 SYN-001列|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-002|覆核事件ID|合成情境／角色|模擬獨立核對，13/20及70.50一致|§10 SYN-002列|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-003|覆核事件ID|合成情境／角色|模擬獨立核對，17/20及69.50一致|§10 SYN-003列|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-004|覆核事件ID|合成情境／角色|模擬獨立核對，11/20及74.75一致|§10 SYN-004列|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-003-R1|覆核事件ID|合成情境／角色|模擬核對新答卷及四項新P評等|§11複評說明|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|REV-SYN-004-R1|覆核事件ID|合成情境／角色|模擬核對新答卷、新P3及沿用SF來源|§11複評說明|實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。|
|CASE-SYN-17|情境代碼|CASE-SYN-17|虛構服務進度詢問|§5 SAMPLE/SYNTHETIC情境控制卡：情境代碼、授權、狀態及來源時間|REAL替換時核對實際核定情境版本、用途授權範圍、狀態原件及擷取時間；缺項或衝突即UNKNOWN/HOLD，不以本SAMPLE推定。|
|SYN-NO-AUTH|情境事實|CASE-SYN-17|未附可核對授權|§5情境控制卡：可核對授權欄|查實際核定情境的授權原件、用途及適用範圍；無證據即停止受限存取並記UNKNOWN/HOLD。|
|SYN-STATUS-UNK|情境事實|CASE-SYN-17|系統狀態未提供|§5情境控制卡：系統狀態、來源及擷取時間欄|核對具權限的狀態原件／查詢輸出與擷取時間；沒有可核實來源就維持UNKNOWN，不宣稱受理或核准。|
|N-01|合成計算結果|合成班次|2/4=50%|§12列1|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-02|合成計算結果|合成班次|2/4=50%|§12列2|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-03|合成計算結果|合成班次|4/4=100%|§12列3|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-04|合成計算結果|合成班次|2/4=50%|§12列4|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-05|合成計算結果|合成班次|1/4=25%|§12列5|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|N-06|合成計算結果|合成班次|1/4=25%|§12列6|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|M-01|合成計算結果|合成班次|14.50,32.50,19.375,11.25,77.625|§12列7|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|M-02|合成計算結果|合成班次|14.00,23.75,22.50,11.875,72.125|§12列8|由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。|
|RET-003|合成計算結果|合成班次|82.00=17+30+22.50+12.50|§11複評計算段：SYN-003總分算式及門檻|依該段列示的新知識答卷、四項新P觀察、沿用C/M分數與權重重算；核對未四捨五入分值及四門檻。|
|RET-004|合成計算結果|合成班次|80.25=14+32.50+22.50+11.25|§11複評計算段：SYN-004總分算式及門檻|依該段列示的新知識答卷、新P3、沿用P1/P2/P4及C/M分數重算；核對未四捨五入分值及四門檻。|
|SF-073|合成更正定位|SYN-004首次P1沿用|4；§8首次P向量第1格|§8表SYN-004首次P向量第1格|核首次評分原件，不作新評。|
|SF-074|合成更正定位|SYN-004首次P2沿用|3；§8首次P向量第2格|§8表SYN-004首次P向量第2格|核首次評分原件，不作新評。|
|SF-076|合成更正定位|SYN-004首次P4沿用|3；§8首次P向量第4格|§8表SYN-004首次P向量第4格|核首次評分原件，不作新評。|
|SF-099|合成更正定位|SYN-003新P1複評|3；EV-SYN-003-P1-R1|§11複評新觀察EV-SYN-003-P1-R1|新複評觀察原件，不得沿用。|
|SF-100|合成更正定位|SYN-003新P2複評|3；EV-SYN-003-P2-R1|§11複評新觀察EV-SYN-003-P2-R1|新複評觀察原件，不得沿用。|
|SF-101|合成更正定位|SYN-003新P3複評|3；EV-SYN-003-P3-R1|§11複評新觀察EV-SYN-003-P3-R1|新授權情境觀察。|
|SF-102|合成更正定位|SYN-003新P4複評|3；EV-SYN-003-P4-R1|§11複評新觀察EV-SYN-003-P4-R1|新交接觀察，不得沿用。|
|SF-110|合成更正定位|SYN-004首次P1沿用|4；SF-073|§11沿用首次SF-073|核首次來源，不造新觀察。|
|SF-111|合成更正定位|SYN-004首次P2沿用|3；SF-074|§11沿用首次SF-074|核首次來源，不造新觀察。|
|SF-112|合成更正定位|SYN-004新P3複評|3；EV-SYN-004-P3-R1|§11新P3觀察EV-SYN-004-P3-R1|新P3複評觀察原件。|
|SF-113|合成更正定位|SYN-004首次P4沿用|3；SF-076|§11沿用首次SF-076|核首次來源，不造新觀察。|
|SCORE-SYN-001-knowledge|合成衍生分數|SYN-001|16/20|§8表 SYN-001 knowledge欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-001-practical|合成衍生分數|SYN-001|35/40|§8表 SYN-001 practical欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-001-case|合成衍生分數|SYN-001|21.25/25|§8表 SYN-001 case欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-001-communication|合成衍生分數|SYN-001|12.5/15|§8表 SYN-001 communication欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-001-total|合成衍生分數|SYN-001|84.75/100|§8表 SYN-001 total欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-knowledge|合成衍生分數|SYN-002|13/20|§8表 SYN-002 knowledge欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-practical|合成衍生分數|SYN-002|30/40|§8表 SYN-002 practical欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-case|合成衍生分數|SYN-002|17.5/25|§8表 SYN-002 case欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-communication|合成衍生分數|SYN-002|10/15|§8表 SYN-002 communication欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-002-total|合成衍生分數|SYN-002|70.50/100|§8表 SYN-002 total欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-knowledge|合成衍生分數|SYN-003|17/20|§8表 SYN-003 knowledge欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-practical|合成衍生分數|SYN-003|17.5/40|§8表 SYN-003 practical欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-case|合成衍生分數|SYN-003|22.5/25|§8表 SYN-003 case欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-communication|合成衍生分數|SYN-003|12.5/15|§8表 SYN-003 communication欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-total|合成衍生分數|SYN-003|69.50/100|§8表 SYN-003 total欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-knowledge|合成衍生分數|SYN-004|11/20|§8表 SYN-004 knowledge欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-practical|合成衍生分數|SYN-004|30/40|§8表 SYN-004 practical欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-case|合成衍生分數|SYN-004|22.5/25|§8表 SYN-004 case欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-communication|合成衍生分數|SYN-004|11.25/15|§8表 SYN-004 communication欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-004-total|合成衍生分數|SYN-004|74.75/100|§8表 SYN-004 total欄|由逐題答卷／EV及§7公式重算；核分母及門檻。|
|SCORE-SYN-003-retest-knowledge|合成複評數值|SYN-003|17/20|§11複評計算列 SYN-003|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-003-retest-practical|合成複評數值|SYN-003|30/40|§11複評計算列 SYN-003|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-003-retest-total|合成複評數值|SYN-003|82.00/100|§11複評計算列 SYN-003|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-004-retest-knowledge|合成複評數值|SYN-004|14/20|§11複評計算列 SYN-004|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-004-retest-practical|合成複評數值|SYN-004|32.50/40|§11複評計算列 SYN-004|依新答卷、新EV及明列沿用原始分數重算。|
|SCORE-SYN-004-retest-total|合成複評數值|SYN-004|80.25/100|§11複評計算列 SYN-004|依新答卷、新EV及明列沿用原始分數重算。|
