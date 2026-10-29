# 0010/I02-E01 R04b independent semantic review packet

## Review request bound to exact R04b Word SHA
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\reviewer\OPENCODE_R04b\REVIEW_REQUEST_R04b.md
source_sha256=f50a3743f4866693837e20f89c067442c568e56532664fc38b0a5ad225c9b887
source_bytes=3019

# 0010 / I02-E01 R04b exact-SHA independent semantic review

Requested route: OpenCode v2 CLI `opencode/deepseek-v4.1-flash-free` when its recorded provider cooldown has expired. Review only the attached text packet; no tools, browsing, file edits, or claims of unperformed local checks. Return one JSON object matching the schema below.

Exact Word candidate SHA-256: `9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe`.
Source Markdown SHA-256: `b16f1c4e9f674b6b6a1258a09192a87f40d4e92430810091fe2eadfe228aba47`.
Word text extraction SHA-256: `41212d79d37d23144c4305141f4e3b13e048a0e0dd02e51e64d01edd5ab30e74`.
SAMPLE/SYNTHETIC register SHA-256: `6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc`.
Official requirement: `對學員訓練成果有評核標準的訂定及說明。` (printed p.1, indicator 2).
Unique Blueprint file SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; row SHA-256: `3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d`.

Review the complete R04b body, extracted Word text and all 157 register rows. Verify R03 semantic findings and R04 changes remain repaired; question/LO allocation, 0–4 rubric, case and retest math, thresholds, atomic fact locators, case/retest provenance, title-blind genre and rejection of negative neighbors 0009/I01-E06 and 0011/I02-E02; practical use by a small volunteer association; consistency between Markdown, extracted Word text, register and exact candidate SHA; and SAMPLE/REAL boundary. Identify precise section/table/field locators for every finding. Do not promote unresolved Blueprint outward-policy/public-disclosure scope beyond PARTIAL/UNKNOWN. No actual learner, roster, authorizer, assessment or association approval evidence was supplied. Do not call synthetic material REAL, adopted, effective or formally accepted.

Technical/visual receipts are supplied for context but do not substitute for this independent semantic review. Do not perform layout review unless a concrete text-layout issue appears in the extracted content; the Word render is separately bound to the exact DOCX SHA.

JSON schema:
{
  "receipt_type":"independent_exact_sha_semantic_review",
  "review_id":"0010-I02-E01-R04b",
  "reviewed_at_utc":"ISO-8601",
  "candidate_sha256":"9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
  "source_markdown_sha256":"b16f1c4e9f674b6b6a1258a09192a87f40d4e92430810091fe2eadfe228aba47",
  "extracted_text_sha256":"41212d79d37d23144c4305141f4e3b13e048a0e0dd02e51e64d01edd5ab30e74",
  "register_sha256":"6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc",
  "verdict":"PASS|PARTIAL|FAIL",
  "scope":"...",
  "checks":[{"id":"...","result":"PASS|PARTIAL|FAIL","locator":"...","reason":"..."}],
  "findings":[{"id":"...","severity":"critical|major|moderate|minor","locator":"...","evidence":"...","required_repair":"..."}],
  "limitations":["..."],
  "does_not_claim":["REAL evidence","formal acceptance","unresolved Blueprint scope"]
}

## Official requirement extract
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\source\OFFICIAL_REQUIREMENT_EXTRACT_R04.txt
source_sha256=65ab23c7a778753d7fb60160bc54621c0978f1776262bfc46b6a3f95626a7823
source_bytes=473

OFFICIAL_SOURCE=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf
OFFICIAL_SOURCE_SHA256=805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709
LOCATOR=printed page 1, indicator 2
EXACT_REQUIREMENT_TEXT=對學員訓練成果有評核標準的訂定及說明。
STATUS=Exact phrase was extracted from the local official PDF and independently matched in the R03 exact-SHA review; no REAL association evidence is implied.

## Exact current unique Blueprint row
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

## R03 independent semantic review
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

## Exact R04b source body
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\worker\0010_I02-E01_R04b.md
source_sha256=b16f1c4e9f674b6b6a1258a09192a87f40d4e92430810091fe2eadfe228aba47
source_bytes=45123

# 學員訓練成果評核標準與說明｜R04

**狀態：SAMPLE/SYNTHETIC 候選稿；未核准、未生效。對應 Word 檔另以 CANDIDATE 狀態管理；其存在不代表機構已採用、已實際施測或獨立驗收通過。** 所有示例題目、作答、角色、覆核事件、行為、日期若有、數值及分析均為虛構，不指稱真實學員、協會採用、實際施測或實際覆核。

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

## Exact R04b Word extraction
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\reviewer\OPENCODE_R04b\DOCX_TEXT_EXTRACT_R04b.txt
source_sha256=41212d79d37d23144c4305141f4e3b13e048a0e0dd02e51e64d01edd5ab30e74
source_bytes=49789

# Extracted text from exact Word candidate
docx_sha256=9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe

[P1] 0010 學員訓練成果評核標準與說明
[P2] 狀態：SAMPLE/SYNTHETIC 候選稿；未核准、未生效。對應 Word 檔另以 CANDIDATE 狀態管理；其存在不代表機構已採用、已實際施測或獨立驗收通過。 所有示例題目、作答、角色、覆核事件、行為、日期若有、數值及分析均為虛構，不指稱真實學員、協會採用、實際施測或實際覆核。
[P3] 1. 官方要求及範圍
[P4] 官方《TTQS查核佐證文件資料表—訓練機構版》第1頁指標2原文：「對學員訓練成果有評核標準的訂定及說明。」本件說明學習目標、題目與任務、評分錨點、權重、門檻及覆核，範圍為學員結果。0009/I01-E06是組織年度績效目標；0011/I02-E02是訓練政策及產品／市場定位，均非本件替代品。
[P5] F-05 CONTROL_SCOPE_CONFLICT：PARTIAL/UNKNOWN。 Blueprint列另列對外承諾／公開揭露與政策檢討完成率；官方I02-E01原文未支持這些額外政策欄位，範圍待權責控制者確認。本稿不擴張承諾、不加政策指標、不改Blueprint，也不聲稱完全符合Blueprint。此衝突不停止本次候選修補。
[P6] 2. 流程及紀錄
[P7] 紀錄至少包含目標／題本版本、受控代碼、逐題答案、每項原始等級與證據、主評角色、獨立覆核角色及已完成事件、計算、門檻、補救、複評、更正及來源定位。角色指派不等於覆核完成。
[P9] 3. 唯一目標配題及分母
[P10] LO1「10題」是Q1–Q10子集。全卷固定20題，每題1分、總分母20；四目標互斥且總和20。
[P11] 4. SAMPLE/SYNTHETIC完整題本、四選項及鍵
[P12] 作答指示：20題單選、限時20分鐘；答對1分，答錯／空白／多選0分。共同情境為虛構櫃台詢問；只採各題已給資訊，未提供授權、身分及狀態均為未知。
[P13] 答案鍵Q1–Q20依序：B, A, B, B, B, A, B, A, A, A, B, A, A, A, A, A, A, A, A, A。鍵與題本版本綁定，不一致即HOLD。
[P15] 5. 構面及權重
[P16] 知識20題×1=20；P1–P4各10分、合計40；C1–C5各5分、合計25；M1–M3各5分、合計15；總分100。實作使用腳本CASE-SYN-17：虛構來訪者問申請進度，未附可核對授權、系統狀態未提供。受評者須確認需求、說用途、辨識授權缺口、停止受限存取、記錄已知／未知／來源／責任／下一步，並作清楚交接及理解確認；評核者只照讀卡片、不提示。不得假設身分已驗證或查看／揭露受限資料。
[P17] SAMPLE/SYNTHETIC 情境控制卡（CASE-SYN-17）
[P18] 本卡只設定評核輸入；不是實際個案、授權、申請紀錄或系統查詢結果。未知欄位不得由受評者或評核者補猜。
[P20] 6. 主文整合的指標專屬0–4錨點
[P21] 公式仍為等級÷4×指標權重；下表是唯一專屬定級標準。
[P23] 7. 門檻、複評及HOLD
[P24] 總分=知識+P+C+M，保留精確值加總後顯示兩位。通過須同時：總分≥70/100、知識≥12/20、實作≥28/40、P3≥3/4。權重及門檻是候選內規值，非官方指定。版本不明、證據缺漏、利益衝突、核算不一致或獨立覆核未完成時HOLD，不發布能力判定。
[P26] 8. SAMPLE/SYNTHETIC逐題答卷與首次計算
[P27] 作答按Q1–Q20順序。§4答案鍵與下列向量逐題比較即可重算知識分。此例D皆為錯答。
[P28] 9. 每一評等的原始SAMPLE/SYNTHETIC行為證據
[P29] EV為合成原始觀察記錄；每個等級以§6相同指標的行為錨點定級，證據句明列觀察行為，可逐列重評。主評角色是指派欄；覆核完成事件另列§10。
[P30] 10. 覆核事件與職責分離（SAMPLE/SYNTHETIC）
[P31] ROLE-EVAL-SYN為被指派主評碼，ROLE-REVIEW-SYN為另一獨立覆核碼。事件欄列出模擬核對範圍及重算結果，區分指派與完成；不代表真人、資格或實際發生。
[P32] 11. 複評新觀察及沿用追溯
[P33] SYN-003知識新卷仍17/20，並重評全部四項P，新的評等[3,3,3,3]、30/40。SYN-004知識新卷14/20；P3新評3，P1=4、P2=3、P4=3沿用首次SF-073/SF-074/SF-076，非新觀察。
[P34] SYN-003複評覆核事件REV-SYN-003-R1核對新知識答卷及四項新EV；總分17+30+22.50+12.50=82.00。SYN-004事件REV-SYN-004-R1核對新知識答卷、新P3 EV、P1/P2/P4首次來源、計算；實作(4+3+3+3)×2.5=32.50，總分14+32.50+22.50+11.25=80.25。兩例均符合四門檻。沿用值不冒充新觀察。
[P36] 12. 彙總及分母
[P37] 四是合成有效首次個案數；差距可重疊。均值先用精確值算，再於顯示時四捨五入。
[P38] 13. 小型志工協會配置
[P39] 每案至少兩名不同、無衝突人員分任主評和獨立覆核；其中一人可兼任非評分的排程、版本保管及通知。預先指定已完成本量尺校準且經協會授權的跨場次備援；外部覆核者僅在權責主管事前授權、保密及可追溯委任後使用，不假設人選存在。不可同人兼主評與覆核、覆核自己的評分或辦理自己涉衝突案件申訴。若沒有合格覆核者／授權備援、衝突未分離或覆核未完成，HOLD。真實名冊及資格均UNKNOWN。
[P40] 14. 負向鄰項、真實替換及限制
[P41] 0009/I01-E06是組織年度績效目標分析；0011/I02-E02是訓練政策、產品與市場定位。本件只評學員訓練結果。真實採用前須取得核准課程目標、題本、公告、逐題答卷、觀察原件、角色資格及實際覆核紀錄；逐項替換合成資料並重算。缺原件維持UNKNOWN/HOLD。本文不宣稱真實採用、核准、學員、成果或實際覆核。
[P43] 15. 原子SAMPLE/SYNTHETIC替換登錄
[P44] 每列是一題（含其選項）、一個答案鍵、一份答卷向量、一個指標觀察、角色／事件或單一結果；有類型、個案、精確值、本文欄位和真實替換來源／核查方式。登錄在所有被引用資料之後。

[TABLE 1: 6 rows x 3 columns]
[T1R1] 步驟 | 責任 | 必要紀錄／控制
[T1R2] 目標映射與版本 | 課程負責人、核定者 | 課程目標、題本、答案鍵、量尺、門檻、版本及評核前公告
[T1R3] 施測 | 主評核者 | 逐題原始作答、題本版本、各指標原始行為證據
[T1R4] 獨立覆核 | 未參與該案原評分者 | 重新核答案、證據、錨點、計算、門檻；記錄差異及結論
[T1R5] 回饋複評 | 課程負責人及評核角色 | 差距、練習、新題版本；清楚標示新評或首次沿用
[T1R6] 保存分析 | 紀錄管理者 | 受控學員碼至原件、計算、覆核及通知的索引

[TABLE 2: 6 rows x 6 columns]
[T2R1] 目標 | 題號 | 題數 | 構念 | 目標內分母／全卷分母 | 答案鍵
[T2R2] LO1 | Q1–Q10 | 10 | 流程、需求、用途、結案 | 10/20 | §4 Q1–Q10
[T2R3] LO2 | Q11–Q14 | 4 | 授權、最少必要、停止升級 | 4/20 | §4 Q11–Q14
[T2R4] LO3 | Q15–Q17 | 3 | 來源、未知、交接 | 3/20 | §4 Q15–Q17
[T2R5] LO4 | Q18–Q20 | 3 | 溝通、理解、承諾界線 | 3/20 | §4 Q18–Q20
[T2R6] 合計 | Q1–Q20 | 20 | 四項構念 | 20/20 | 逐題鍵

[TABLE 3: 21 rows x 6 columns]
[T3R1] 題 | 題幹 | A | B | C | D
[T3R2] Q1 | 櫃台接待第一步 | 查全檔 | 釐清需求並說明用途 | 先承諾 | 索取無關資料
[T3R3] Q2 | 只問進度時 | 確認具體事項 | 查看全部 | 交付全檔 | 結束
[T3R4] Q3 | 用途未明時 | 先複製 | 告知用途並確認 | 擴大查詢 | 自行改用途
[T3R5] Q4 | 必要資料缺漏 | 猜填 | 標未知並查證 | 填常見值 | 刪除
[T3R6] Q5 | 超出服務範圍 | 保證成功 | 說明限制並指引管道 | 私下查詢 | 不記錄
[T3R7] Q6 | 結案前 | 確認已做與未完 | 只說完成 | 保證結果 | 不告知
[T3R8] Q7 | 部分已知部分待查 | 全記完成 | 分列已知待查 | 刪除待查 | 猜測
[T3R9] Q8 | 對方更正資料 | 留更正軌跡 | 無痕覆寫 | 選方便值 | 忽略
[T3R10] Q9 | 交接未結事項 | 列需求步驟未決接手人 | 交所有資料 | 只寫處理 | 不指定
[T3R11] Q10 | 結案記錄 | 可核對處置及下一步 | 評價個性 | 保證未知 | 取代原件
[T3R12] Q11 | 沒有授權可否查受限資料 | 可以 | 先核授權用途 | 先查後補 | 旁人代查
[T3R13] Q12 | 僅授權一項查詢 | 只查必要資料 | 看全檔 | 下載 | 轉傳
[T3R14] Q13 | 授權範圍不明 | 停止並確認 | 最大範圍解讀 | 先揭露 | 推測
[T3R15] Q14 | 第三人無授權索資料 | 只說公開流程 | 口頭透露 | 傳截圖 | 讓其查看
[T3R16] Q15 | 如何記錄來源 | 區分陳述核實未知 | 全寫核實 | 不註來源 | 補足
[T3R17] Q16 | 日期未核實 | 標未知並記查證 | 填今天 | 估日期 | 留白
[T3R18] Q17 | 交接追溯欄 | 角色已做依據下一步 | 評語 | 背景 | 模糊寫處理
[T3R19] Q18 | 說明狀態 | 清楚中性說已知未知 | 保證 | 縮寫 | 責怪
[T3R20] Q19 | 確認理解 | 請對方說下一步並澄清 | 問懂否即結束 | 假設點頭 | 不給問
[T3R21] Q20 | 結果未核實 | 說未知及管道不保證 | 保證核准 | 暗示完成 | 可能說事實

[TABLE 4: 6 rows x 3 columns]
[T4R1] 控制欄位 | SAMPLE/SYNTHETIC值 | 評核操作及停辦條件
[T4R2] 情境代碼／情境內容 | CASE-SYN-17；虛構服務進度詢問 | 同一版腳本供同次示範；更換版本須重新核對題本與評核錨點。
[T4R3] 可核對授權 | 未提供；UNKNOWN | 受評者先確認授權及用途；未核實前停止受限存取，不索取或揭露超出必要範圍的資料。
[T4R4] 系統狀態 | 未提供；UNKNOWN | 不可推定已受理、完成、核准或拒絕；只能說明目前無可核實狀態並交代查證管道。
[T4R5] 狀態來源及擷取時間 | 未提供；UNKNOWN | 評核者不得把口述、推測或本示範資料當作系統原件；須記錄查證來源與時間或明列未知。
[T4R6] REAL替換核對 | 實際核定情境及其授權／狀態原件尚未提供 | 採 REAL 前核對正式情境版本、用途授權、適用範圍、狀態來源及擷取時間；任一缺失或衝突即 UNKNOWN/HOLD。

[TABLE 5: 13 rows x 6 columns]
[T5R1] 指標 | 4級 | 3級 | 2級 | 1級 | 0級
[T5R2] P1需求流程 | 獨立依序確認需求用途處置結案 | 步驟正確小漏自改 | 漏必要步驟提示後補 | 多步錯仍未改 | 未作或捏造
[T5R3] P2紀錄 | 標來源區分已知未知一致 | 核心正確小漏自補 | 漏重要欄提示後補 | 多處錯未改 | 無紀錄或不實
[T5R4] P3授權核心 | 先核用途最少取用疑即停升級 | 未越權且完成確認 | 提示後、存取前停止 | 提示後仍嘗試越權 | 未授權存取揭露即HOLD
[T5R5] P4交接 | 處置合宜交代接手未決下一步 | 正確主要交接全 | 漏欄提示後補 | 處置不符 | 無處置或捏造
[T5R6] C1需求 | 準確指出需求目標限制未知 | 正確小漏 | 提示後區分 | 推測當需求 | 無法指出
[T5R7] C2依據 | 逐結論連來源標未知 | 主要正確小漏自改 | 漏重要依據提示後補 | 多項無據 | 偽造
[T5R8] C3行動 | 全程符合需求授權流程 | 主要合宜小差自改 | 一步提示後改 | 不符未改 | 違核心
[T5R9] C4完整 | 來源步驟角色未知下一步全 | 核心完整 | 漏欄提示補 | 多欄缺漏 | 不實
[T5R10] C5限制 | 區分結果未知限制升級 | 正確說明主要限制 | 漏限制提示補 | 誇大未改 | 捏造
[T5R11] M1溝通 | 清楚中性尊重完整 | 清楚有禮 | 含糊提示後澄清 | 仍不清或不尊重 | 威嚇拒溝通
[T5R12] M2理解授權 | 確認理解授權後才前進 | 兩者完成 | 提示後補一項 | 提示後仍漏 | 未確認即存取
[T5R13] M3下一步 | 說明責任步驟未知界線 | 清楚無保證 | 漏項提示補 | 無據承諾 | 未知說成保證

[TABLE 6: 5 rows x 8 columns]
[T6R1] 個案 | 逐題向量 | 知識 | P向量 /40 | C向量 /25 | M向量 /15 | 總分 | 門檻
[T6R2] SYN-001 | B,A,B,B,B,A,B,A,A,A,B,A,A,A,A,A,D,D,D,D | 16/20 | [4,3,3,4]=35 | [3,4,3,3,4]=21.25 | [3,3,4]=12.5 | 84.75 | 通過
[T6R3] SYN-002 | B,A,B,B,B,A,B,A,A,A,B,A,A,D,D,D,D,D,D,D | 13/20 | [3,3,3,3]=30 | [3,3,2,3,3]=17.5 | [3,2,3]=10 | 70.50 | 通過
[T6R4] SYN-003 | B,A,B,B,B,A,B,A,A,A,B,A,A,A,A,A,A,D,D,D | 17/20 | [2,2,1,2]=17.5 | [4,4,3,3,4]=22.5 | [4,3,3]=12.5 | 69.50 | 未達
[T6R5] SYN-004 | B,A,B,B,B,A,B,A,A,A,B,D,D,D,D,D,D,D,D,D | 11/20 | [4,3,2,3]=30 | [4,3,4,3,4]=22.5 | [3,3,3]=11.25 | 74.75 | 未達

[TABLE 7: 49 rows x 7 columns]
[T7R1] EV ID | 個案 | 階段 | 指標 | 原始合成觀察 | 等級 | 主評角色
[T7R2] EV-SYN-001-P1-F | SYN-001 | 首次 | P1 | 獨立依序確認需求用途處置結案 | 4 | ROLE-EVAL-SYN
[T7R3] EV-SYN-001-P2-F | SYN-001 | 首次 | P2 | 核心正確小漏自補 | 3 | ROLE-EVAL-SYN
[T7R4] EV-SYN-001-P3-F | SYN-001 | 首次 | P3 | 未越權且完成確認 | 3 | ROLE-EVAL-SYN
[T7R5] EV-SYN-001-P4-F | SYN-001 | 首次 | P4 | 處置合宜交代接手未決下一步 | 4 | ROLE-EVAL-SYN
[T7R6] EV-SYN-001-C1-F | SYN-001 | 首次 | C1 | 正確小漏 | 3 | ROLE-EVAL-SYN
[T7R7] EV-SYN-001-C2-F | SYN-001 | 首次 | C2 | 逐結論連來源標未知 | 4 | ROLE-EVAL-SYN
[T7R8] EV-SYN-001-C3-F | SYN-001 | 首次 | C3 | 主要合宜小差自改 | 3 | ROLE-EVAL-SYN
[T7R9] EV-SYN-001-C4-F | SYN-001 | 首次 | C4 | 核心完整 | 3 | ROLE-EVAL-SYN
[T7R10] EV-SYN-001-C5-F | SYN-001 | 首次 | C5 | 區分結果未知限制升級 | 4 | ROLE-EVAL-SYN
[T7R11] EV-SYN-001-M1-F | SYN-001 | 首次 | M1 | 清楚有禮 | 3 | ROLE-EVAL-SYN
[T7R12] EV-SYN-001-M2-F | SYN-001 | 首次 | M2 | 兩者完成 | 3 | ROLE-EVAL-SYN
[T7R13] EV-SYN-001-M3-F | SYN-001 | 首次 | M3 | 說明責任步驟未知界線 | 4 | ROLE-EVAL-SYN
[T7R14] EV-SYN-002-P1-F | SYN-002 | 首次 | P1 | 步驟正確小漏自改 | 3 | ROLE-EVAL-SYN
[T7R15] EV-SYN-002-P2-F | SYN-002 | 首次 | P2 | 核心正確小漏自補 | 3 | ROLE-EVAL-SYN
[T7R16] EV-SYN-002-P3-F | SYN-002 | 首次 | P3 | 未越權且完成確認 | 3 | ROLE-EVAL-SYN
[T7R17] EV-SYN-002-P4-F | SYN-002 | 首次 | P4 | 正確主要交接全 | 3 | ROLE-EVAL-SYN
[T7R18] EV-SYN-002-C1-F | SYN-002 | 首次 | C1 | 正確小漏 | 3 | ROLE-EVAL-SYN
[T7R19] EV-SYN-002-C2-F | SYN-002 | 首次 | C2 | 主要正確小漏自改 | 3 | ROLE-EVAL-SYN
[T7R20] EV-SYN-002-C3-F | SYN-002 | 首次 | C3 | 一步提示後改 | 2 | ROLE-EVAL-SYN
[T7R21] EV-SYN-002-C4-F | SYN-002 | 首次 | C4 | 核心完整 | 3 | ROLE-EVAL-SYN
[T7R22] EV-SYN-002-C5-F | SYN-002 | 首次 | C5 | 正確說明主要限制 | 3 | ROLE-EVAL-SYN
[T7R23] EV-SYN-002-M1-F | SYN-002 | 首次 | M1 | 清楚有禮 | 3 | ROLE-EVAL-SYN
[T7R24] EV-SYN-002-M2-F | SYN-002 | 首次 | M2 | 提示後補一項 | 2 | ROLE-EVAL-SYN
[T7R25] EV-SYN-002-M3-F | SYN-002 | 首次 | M3 | 清楚無保證 | 3 | ROLE-EVAL-SYN
[T7R26] EV-SYN-003-P1-F | SYN-003 | 首次 | P1 | 漏必要步驟提示後補 | 2 | ROLE-EVAL-SYN
[T7R27] EV-SYN-003-P2-F | SYN-003 | 首次 | P2 | 漏重要欄提示後補 | 2 | ROLE-EVAL-SYN
[T7R28] EV-SYN-003-P3-F | SYN-003 | 首次 | P3 | 提示後仍嘗試越權 | 1 | ROLE-EVAL-SYN
[T7R29] EV-SYN-003-P4-F | SYN-003 | 首次 | P4 | 漏欄提示後補 | 2 | ROLE-EVAL-SYN
[T7R30] EV-SYN-003-C1-F | SYN-003 | 首次 | C1 | 準確指出需求目標限制未知 | 4 | ROLE-EVAL-SYN
[T7R31] EV-SYN-003-C2-F | SYN-003 | 首次 | C2 | 逐結論連來源標未知 | 4 | ROLE-EVAL-SYN
[T7R32] EV-SYN-003-C3-F | SYN-003 | 首次 | C3 | 主要合宜小差自改 | 3 | ROLE-EVAL-SYN
[T7R33] EV-SYN-003-C4-F | SYN-003 | 首次 | C4 | 核心完整 | 3 | ROLE-EVAL-SYN
[T7R34] EV-SYN-003-C5-F | SYN-003 | 首次 | C5 | 區分結果未知限制升級 | 4 | ROLE-EVAL-SYN
[T7R35] EV-SYN-003-M1-F | SYN-003 | 首次 | M1 | 清楚中性尊重完整 | 4 | ROLE-EVAL-SYN
[T7R36] EV-SYN-003-M2-F | SYN-003 | 首次 | M2 | 兩者完成 | 3 | ROLE-EVAL-SYN
[T7R37] EV-SYN-003-M3-F | SYN-003 | 首次 | M3 | 清楚無保證 | 3 | ROLE-EVAL-SYN
[T7R38] EV-SYN-004-P1-F | SYN-004 | 首次 | P1 | 獨立依序確認需求用途處置結案 | 4 | ROLE-EVAL-SYN
[T7R39] EV-SYN-004-P2-F | SYN-004 | 首次 | P2 | 核心正確小漏自補 | 3 | ROLE-EVAL-SYN
[T7R40] EV-SYN-004-P3-F | SYN-004 | 首次 | P3 | 提示後、存取前停止 | 2 | ROLE-EVAL-SYN
[T7R41] EV-SYN-004-P4-F | SYN-004 | 首次 | P4 | 正確主要交接全 | 3 | ROLE-EVAL-SYN
[T7R42] EV-SYN-004-C1-F | SYN-004 | 首次 | C1 | 準確指出需求目標限制未知 | 4 | ROLE-EVAL-SYN
[T7R43] EV-SYN-004-C2-F | SYN-004 | 首次 | C2 | 主要正確小漏自改 | 3 | ROLE-EVAL-SYN
[T7R44] EV-SYN-004-C3-F | SYN-004 | 首次 | C3 | 全程符合需求授權流程 | 4 | ROLE-EVAL-SYN
[T7R45] EV-SYN-004-C4-F | SYN-004 | 首次 | C4 | 核心完整 | 3 | ROLE-EVAL-SYN
[T7R46] EV-SYN-004-C5-F | SYN-004 | 首次 | C5 | 區分結果未知限制升級 | 4 | ROLE-EVAL-SYN
[T7R47] EV-SYN-004-M1-F | SYN-004 | 首次 | M1 | 清楚有禮 | 3 | ROLE-EVAL-SYN
[T7R48] EV-SYN-004-M2-F | SYN-004 | 首次 | M2 | 兩者完成 | 3 | ROLE-EVAL-SYN
[T7R49] EV-SYN-004-M3-F | SYN-004 | 首次 | M3 | 清楚無保證 | 3 | ROLE-EVAL-SYN

[TABLE 8: 5 rows x 5 columns]
[T8R1] 個案 | 主評角色 | 覆核角色 | 完成事件ID | 獨立核對資料及重算結果
[T8R2] SYN-001 | ROLE-EVAL-SYN | ROLE-REVIEW-SYN | REV-SYN-001 | 20答題、12筆EV、構面及門檻；重算16、84.75，通過
[T8R3] SYN-002 | ROLE-EVAL-SYN | ROLE-REVIEW-SYN | REV-SYN-002 | 20答題、12筆EV、構面及門檻；重算13、70.50，通過
[T8R4] SYN-003 | ROLE-EVAL-SYN | ROLE-REVIEW-SYN | REV-SYN-003 | 20答題、12筆EV及門檻；重算17、69.50，實作/P3未達
[T8R5] SYN-004 | ROLE-EVAL-SYN | ROLE-REVIEW-SYN | REV-SYN-004 | 20答題、12筆EV及門檻；重算11、74.75，知識/P3未達

[TABLE 9: 3 rows x 4 columns]
[T9R1] 新測驗向量 | 個案 | Q1–Q20逐題作答 | 答對分母
[T9R2] RET-SYN-003 | SYN-003 | B,A,B,B,B,A,B,A,A,A,B,A,A,A,A,A,A,D,D,D | 17/20
[T9R3] RET-SYN-004 | SYN-004 | B,A,B,B,B,A,B,A,A,A,B,A,A,A,D,D,D,D,D,D | 14/20

[TABLE 10: 6 rows x 6 columns]
[T10R1] EV ID | 個案 | 新觀察／指標 | 原始合成行為 | 等級 | 來源性質
[T10R2] EV-SYN-003-P1-R1 | SYN-003 | P1 | 新情境依序確認需求用途並結案 | 3 | 新複評
[T10R3] EV-SYN-003-P2-R1 | SYN-003 | P2 | 新紀錄標來源及未知，提示後補重要欄 | 3 | 新複評
[T10R4] EV-SYN-003-P3-R1 | SYN-003 | P3 | 先辨識授權缺口，停止存取並升級 | 3 | 新複評
[T10R5] EV-SYN-003-P4-R1 | SYN-003 | P4 | 新交接列接手、未決及下一步 | 3 | 新複評
[T10R6] EV-SYN-004-P3-R1 | SYN-004 | P3 | 自行辨識授權缺口、停止查詢、未存取揭露 | 3 | 新P3複評

[TABLE 11: 9 rows x 3 columns]
[T11R1] 統計 | 算法 | SAMPLE/SYNTHETIC結果
[T11R2] 首次通過率 | 2/4 | 50%
[T11R3] 複評參與率 | 2/4 | 50%
[T11R4] 複評後達標率 | 4/4 | 100%
[T11R5] 首次P3未達 | 2/4 | 50%
[T11R6] 首次實作未達 | 1/4 | 25%
[T11R7] 首次知識未達 | 1/4 | 25%
[T11R8] 首次通過組均值：知識／實作／案例／溝通／總分 | 兩例平均 | 14.50 / 32.50 / 19.375(19.38) / 11.25 / 77.625(77.63)
[T11R9] 補救組均值：知識／實作／案例／溝通／總分 | 兩例平均 | 14.00 / 23.75 / 22.50 / 11.875(11.88) / 72.125(72.13)

[TABLE 12: 158 rows x 6 columns]
[T12R1] Fact ID | 類型 | Case ID | 精確值 | 精確欄位定位 | 真實替換來源及核查
[T12R2] Q-Q1 | 合成題目與四選項 | 共用題本 | 櫃台接待第一步; A 查全檔; B 釐清需求並說明用途; C 先承諾; D 索取無關資料 | §4題表Q1 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R3] Q-Q2 | 合成題目與四選項 | 共用題本 | 只問進度時; A 確認具體事項; B 查看全部; C 交付全檔; D 結束 | §4題表Q2 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R4] Q-Q3 | 合成題目與四選項 | 共用題本 | 用途未明時; A 先複製; B 告知用途並確認; C 擴大查詢; D 自行改用途 | §4題表Q3 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R5] Q-Q4 | 合成題目與四選項 | 共用題本 | 必要資料缺漏; A 猜填; B 標未知並查證; C 填常見值; D 刪除 | §4題表Q4 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R6] Q-Q5 | 合成題目與四選項 | 共用題本 | 超出服務範圍; A 保證成功; B 說明限制並指引管道; C 私下查詢; D 不記錄 | §4題表Q5 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R7] Q-Q6 | 合成題目與四選項 | 共用題本 | 結案前; A 確認已做與未完; B 只說完成; C 保證結果; D 不告知 | §4題表Q6 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R8] Q-Q7 | 合成題目與四選項 | 共用題本 | 部分已知部分待查; A 全記完成; B 分列已知待查; C 刪除待查; D 猜測 | §4題表Q7 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R9] Q-Q8 | 合成題目與四選項 | 共用題本 | 對方更正資料; A 留更正軌跡; B 無痕覆寫; C 選方便值; D 忽略 | §4題表Q8 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R10] Q-Q9 | 合成題目與四選項 | 共用題本 | 交接未結事項; A 列需求步驟未決接手人; B 交所有資料; C 只寫處理; D 不指定 | §4題表Q9 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R11] Q-Q10 | 合成題目與四選項 | 共用題本 | 結案記錄; A 可核對處置及下一步; B 評價個性; C 保證未知; D 取代原件 | §4題表Q10 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R12] Q-Q11 | 合成題目與四選項 | 共用題本 | 沒有授權可否查受限資料; A 可以; B 先核授權用途; C 先查後補; D 旁人代查 | §4題表Q11 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R13] Q-Q12 | 合成題目與四選項 | 共用題本 | 僅授權一項查詢; A 只查必要資料; B 看全檔; C 下載; D 轉傳 | §4題表Q12 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R14] Q-Q13 | 合成題目與四選項 | 共用題本 | 授權範圍不明; A 停止並確認; B 最大範圍解讀; C 先揭露; D 推測 | §4題表Q13 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R15] Q-Q14 | 合成題目與四選項 | 共用題本 | 第三人無授權索資料; A 只說公開流程; B 口頭透露; C 傳截圖; D 讓其查看 | §4題表Q14 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R16] Q-Q15 | 合成題目與四選項 | 共用題本 | 如何記錄來源; A 區分陳述核實未知; B 全寫核實; C 不註來源; D 補足 | §4題表Q15 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R17] Q-Q16 | 合成題目與四選項 | 共用題本 | 日期未核實; A 標未知並記查證; B 填今天; C 估日期; D 留白 | §4題表Q16 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R18] Q-Q17 | 合成題目與四選項 | 共用題本 | 交接追溯欄; A 角色已做依據下一步; B 評語; C 背景; D 模糊寫處理 | §4題表Q17 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R19] Q-Q18 | 合成題目與四選項 | 共用題本 | 說明狀態; A 清楚中性說已知未知; B 保證; C 縮寫; D 責怪 | §4題表Q18 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R20] Q-Q19 | 合成題目與四選項 | 共用題本 | 確認理解; A 請對方說下一步並澄清; B 問懂否即結束; C 假設點頭; D 不給問 | §4題表Q19 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R21] Q-Q20 | 合成題目與四選項 | 共用題本 | 結果未核實; A 說未知及管道不保證; B 保證核准; C 暗示完成; D 可能說事實 | §4題表Q20 | 核定課程題本同題號、四選項及版本，逐項替換並覆核。
[T12R22] KEY-Q1 | 合成答案鍵 | 共用題本 | B | §4答案鍵Q1 | 同版核准答案鍵與未參與出題者覆核。
[T12R23] KEY-Q2 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q2 | 同版核准答案鍵與未參與出題者覆核。
[T12R24] KEY-Q3 | 合成答案鍵 | 共用題本 | B | §4答案鍵Q3 | 同版核准答案鍵與未參與出題者覆核。
[T12R25] KEY-Q4 | 合成答案鍵 | 共用題本 | B | §4答案鍵Q4 | 同版核准答案鍵與未參與出題者覆核。
[T12R26] KEY-Q5 | 合成答案鍵 | 共用題本 | B | §4答案鍵Q5 | 同版核准答案鍵與未參與出題者覆核。
[T12R27] KEY-Q6 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q6 | 同版核准答案鍵與未參與出題者覆核。
[T12R28] KEY-Q7 | 合成答案鍵 | 共用題本 | B | §4答案鍵Q7 | 同版核准答案鍵與未參與出題者覆核。
[T12R29] KEY-Q8 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q8 | 同版核准答案鍵與未參與出題者覆核。
[T12R30] KEY-Q9 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q9 | 同版核准答案鍵與未參與出題者覆核。
[T12R31] KEY-Q10 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q10 | 同版核准答案鍵與未參與出題者覆核。
[T12R32] KEY-Q11 | 合成答案鍵 | 共用題本 | B | §4答案鍵Q11 | 同版核准答案鍵與未參與出題者覆核。
[T12R33] KEY-Q12 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q12 | 同版核准答案鍵與未參與出題者覆核。
[T12R34] KEY-Q13 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q13 | 同版核准答案鍵與未參與出題者覆核。
[T12R35] KEY-Q14 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q14 | 同版核准答案鍵與未參與出題者覆核。
[T12R36] KEY-Q15 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q15 | 同版核准答案鍵與未參與出題者覆核。
[T12R37] KEY-Q16 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q16 | 同版核准答案鍵與未參與出題者覆核。
[T12R38] KEY-Q17 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q17 | 同版核准答案鍵與未參與出題者覆核。
[T12R39] KEY-Q18 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q18 | 同版核准答案鍵與未參與出題者覆核。
[T12R40] KEY-Q19 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q19 | 同版核准答案鍵與未參與出題者覆核。
[T12R41] KEY-Q20 | 合成答案鍵 | 共用題本 | A | §4答案鍵Q20 | 同版核准答案鍵與未參與出題者覆核。
[T12R42] ANS-SYN-001-FIRST | 逐題作答向量 | SYN-001 | Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:D,Q18:D,Q19:D,Q20:D | §8 SYN-001-FIRST逐題向量 | 該案原始答卷；逐題依同版鍵重算。
[T12R43] ANS-SYN-002-FIRST | 逐題作答向量 | SYN-002 | Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:D,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D | §8 SYN-002-FIRST逐題向量 | 該案原始答卷；逐題依同版鍵重算。
[T12R44] ANS-SYN-003-FIRST | 逐題作答向量 | SYN-003 | Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:A,Q18:D,Q19:D,Q20:D | §8 SYN-003-FIRST逐題向量 | 該案原始答卷；逐題依同版鍵重算。
[T12R45] ANS-SYN-004-FIRST | 逐題作答向量 | SYN-004 | Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:D,Q13:D,Q14:D,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D | §8 SYN-004-FIRST逐題向量 | 該案原始答卷；逐題依同版鍵重算。
[T12R46] ANS-SYN-003-RETEST | 逐題作答向量 | SYN-003 | Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:A,Q16:A,Q17:A,Q18:D,Q19:D,Q20:D | §8 SYN-003-RETEST逐題向量 | 該案原始答卷；逐題依同版鍵重算。
[T12R47] ANS-SYN-004-RETEST | 逐題作答向量 | SYN-004 | Q1:B,Q2:A,Q3:B,Q4:B,Q5:B,Q6:A,Q7:B,Q8:A,Q9:A,Q10:A,Q11:B,Q12:A,Q13:A,Q14:A,Q15:D,Q16:D,Q17:D,Q18:D,Q19:D,Q20:D | §8 SYN-004-RETEST逐題向量 | 該案原始答卷；逐題依同版鍵重算。
[T12R48] EV-SYN-001-P1-F | 合成原始行為及評等 | SYN-001 | 等級4；獨立依序確認需求用途處置結案 | §9 SYN-001 P1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R49] EV-SYN-001-P2-F | 合成原始行為及評等 | SYN-001 | 等級3；核心正確小漏自補 | §9 SYN-001 P2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R50] EV-SYN-001-P3-F | 合成原始行為及評等 | SYN-001 | 等級3；未越權且完成確認 | §9 SYN-001 P3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R51] EV-SYN-001-P4-F | 合成原始行為及評等 | SYN-001 | 等級4；處置合宜交代接手未決下一步 | §9 SYN-001 P4表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R52] EV-SYN-001-C1-F | 合成原始行為及評等 | SYN-001 | 等級3；正確小漏 | §9 SYN-001 C1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R53] EV-SYN-001-C2-F | 合成原始行為及評等 | SYN-001 | 等級4；逐結論連來源標未知 | §9 SYN-001 C2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R54] EV-SYN-001-C3-F | 合成原始行為及評等 | SYN-001 | 等級3；主要合宜小差自改 | §9 SYN-001 C3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R55] EV-SYN-001-C4-F | 合成原始行為及評等 | SYN-001 | 等級3；核心完整 | §9 SYN-001 C4表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R56] EV-SYN-001-C5-F | 合成原始行為及評等 | SYN-001 | 等級4；區分結果未知限制升級 | §9 SYN-001 C5表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R57] EV-SYN-001-M1-F | 合成原始行為及評等 | SYN-001 | 等級3；清楚有禮 | §9 SYN-001 M1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R58] EV-SYN-001-M2-F | 合成原始行為及評等 | SYN-001 | 等級3；兩者完成 | §9 SYN-001 M2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R59] EV-SYN-001-M3-F | 合成原始行為及評等 | SYN-001 | 等級4；說明責任步驟未知界線 | §9 SYN-001 M3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R60] EV-SYN-002-P1-F | 合成原始行為及評等 | SYN-002 | 等級3；步驟正確小漏自改 | §9 SYN-002 P1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R61] EV-SYN-002-P2-F | 合成原始行為及評等 | SYN-002 | 等級3；核心正確小漏自補 | §9 SYN-002 P2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R62] EV-SYN-002-P3-F | 合成原始行為及評等 | SYN-002 | 等級3；未越權且完成確認 | §9 SYN-002 P3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R63] EV-SYN-002-P4-F | 合成原始行為及評等 | SYN-002 | 等級3；正確主要交接全 | §9 SYN-002 P4表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R64] EV-SYN-002-C1-F | 合成原始行為及評等 | SYN-002 | 等級3；正確小漏 | §9 SYN-002 C1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R65] EV-SYN-002-C2-F | 合成原始行為及評等 | SYN-002 | 等級3；主要正確小漏自改 | §9 SYN-002 C2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R66] EV-SYN-002-C3-F | 合成原始行為及評等 | SYN-002 | 等級2；一步提示後改 | §9 SYN-002 C3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R67] EV-SYN-002-C4-F | 合成原始行為及評等 | SYN-002 | 等級3；核心完整 | §9 SYN-002 C4表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R68] EV-SYN-002-C5-F | 合成原始行為及評等 | SYN-002 | 等級3；正確說明主要限制 | §9 SYN-002 C5表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R69] EV-SYN-002-M1-F | 合成原始行為及評等 | SYN-002 | 等級3；清楚有禮 | §9 SYN-002 M1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R70] EV-SYN-002-M2-F | 合成原始行為及評等 | SYN-002 | 等級2；提示後補一項 | §9 SYN-002 M2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R71] EV-SYN-002-M3-F | 合成原始行為及評等 | SYN-002 | 等級3；清楚無保證 | §9 SYN-002 M3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R72] EV-SYN-003-P1-F | 合成原始行為及評等 | SYN-003 | 等級2；漏必要步驟提示後補 | §9 SYN-003 P1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R73] EV-SYN-003-P2-F | 合成原始行為及評等 | SYN-003 | 等級2；漏重要欄提示後補 | §9 SYN-003 P2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R74] EV-SYN-003-P3-F | 合成原始行為及評等 | SYN-003 | 等級1；提示後仍嘗試越權 | §9 SYN-003 P3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R75] EV-SYN-003-P4-F | 合成原始行為及評等 | SYN-003 | 等級2；漏欄提示後補 | §9 SYN-003 P4表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R76] EV-SYN-003-C1-F | 合成原始行為及評等 | SYN-003 | 等級4；準確指出需求目標限制未知 | §9 SYN-003 C1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R77] EV-SYN-003-C2-F | 合成原始行為及評等 | SYN-003 | 等級4；逐結論連來源標未知 | §9 SYN-003 C2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R78] EV-SYN-003-C3-F | 合成原始行為及評等 | SYN-003 | 等級3；主要合宜小差自改 | §9 SYN-003 C3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R79] EV-SYN-003-C4-F | 合成原始行為及評等 | SYN-003 | 等級3；核心完整 | §9 SYN-003 C4表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R80] EV-SYN-003-C5-F | 合成原始行為及評等 | SYN-003 | 等級4；區分結果未知限制升級 | §9 SYN-003 C5表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R81] EV-SYN-003-M1-F | 合成原始行為及評等 | SYN-003 | 等級4；清楚中性尊重完整 | §9 SYN-003 M1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R82] EV-SYN-003-M2-F | 合成原始行為及評等 | SYN-003 | 等級3；兩者完成 | §9 SYN-003 M2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R83] EV-SYN-003-M3-F | 合成原始行為及評等 | SYN-003 | 等級3；清楚無保證 | §9 SYN-003 M3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R84] EV-SYN-004-P1-F | 合成原始行為及評等 | SYN-004 | 等級4；獨立依序確認需求用途處置結案 | §9 SYN-004 P1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R85] EV-SYN-004-P2-F | 合成原始行為及評等 | SYN-004 | 等級3；核心正確小漏自補 | §9 SYN-004 P2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R86] EV-SYN-004-P3-F | 合成原始行為及評等 | SYN-004 | 等級2；提示後、存取前停止 | §9 SYN-004 P3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R87] EV-SYN-004-P4-F | 合成原始行為及評等 | SYN-004 | 等級3；正確主要交接全 | §9 SYN-004 P4表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R88] EV-SYN-004-C1-F | 合成原始行為及評等 | SYN-004 | 等級4；準確指出需求目標限制未知 | §9 SYN-004 C1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R89] EV-SYN-004-C2-F | 合成原始行為及評等 | SYN-004 | 等級3；主要正確小漏自改 | §9 SYN-004 C2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R90] EV-SYN-004-C3-F | 合成原始行為及評等 | SYN-004 | 等級4；全程符合需求授權流程 | §9 SYN-004 C3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R91] EV-SYN-004-C4-F | 合成原始行為及評等 | SYN-004 | 等級3；核心完整 | §9 SYN-004 C4表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R92] EV-SYN-004-C5-F | 合成原始行為及評等 | SYN-004 | 等級4；區分結果未知限制升級 | §9 SYN-004 C5表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R93] EV-SYN-004-M1-F | 合成原始行為及評等 | SYN-004 | 等級3；清楚有禮 | §9 SYN-004 M1表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R94] EV-SYN-004-M2-F | 合成原始行為及評等 | SYN-004 | 等級3；兩者完成 | §9 SYN-004 M2表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R95] EV-SYN-004-M3-F | 合成原始行為及評等 | SYN-004 | 等級3；清楚無保證 | §9 SYN-004 M3表列 | 該次原始觀察表及核准錨點；由獨立覆核者依原行為重評。
[T12R96] EV-SYN-003-P1-R1 | 合成原始行為及評等 | SYN-003 | 等級新複評；3 | §11複評列EV-SYN-003-P1-R1 | 該次新複評原始觀察表，非首次來源。
[T12R97] EV-SYN-003-P2-R1 | 合成原始行為及評等 | SYN-003 | 等級新複評；3 | §11複評列EV-SYN-003-P2-R1 | 該次新複評原始觀察表，非首次來源。
[T12R98] EV-SYN-003-P3-R1 | 合成原始行為及評等 | SYN-003 | 等級新複評；3 | §11複評列EV-SYN-003-P3-R1 | 該次新複評原始觀察表，非首次來源。
[T12R99] EV-SYN-003-P4-R1 | 合成原始行為及評等 | SYN-003 | 等級新複評；3 | §11複評列EV-SYN-003-P4-R1 | 該次新複評原始觀察表，非首次來源。
[T12R100] EV-SYN-004-P3-R1 | 合成原始行為及評等 | SYN-004 | 等級新P3複評；3 | §11複評列EV-SYN-004-P3-R1 | 該次新複評原始觀察表，非首次來源。
[T12R101] ROLE-EVAL-SYN | 角色碼 | 合成情境／角色 | 指定主評角色碼 | §9主評欄 | 實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。
[T12R102] ROLE-REVIEW-SYN | 角色碼 | 合成情境／角色 | 指定獨立覆核角色碼 | §10覆核欄 | 實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。
[T12R103] REV-SYN-001 | 覆核事件ID | 合成情境／角色 | 模擬獨立核對，16/20及84.75一致 | §10 SYN-001列 | 實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。
[T12R104] REV-SYN-002 | 覆核事件ID | 合成情境／角色 | 模擬獨立核對，13/20及70.50一致 | §10 SYN-002列 | 實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。
[T12R105] REV-SYN-003 | 覆核事件ID | 合成情境／角色 | 模擬獨立核對，17/20及69.50一致 | §10 SYN-003列 | 實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。
[T12R106] REV-SYN-004 | 覆核事件ID | 合成情境／角色 | 模擬獨立核對，11/20及74.75一致 | §10 SYN-004列 | 實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。
[T12R107] REV-SYN-003-R1 | 覆核事件ID | 合成情境／角色 | 模擬核對新答卷及四項新P評等 | §11複評說明 | 實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。
[T12R108] REV-SYN-004-R1 | 覆核事件ID | 合成情境／角色 | 模擬核對新答卷、新P3及沿用SF來源 | §11複評說明 | 實際受控名冊、委任及覆核記錄或核定情境原件；核實角色分離、授權及日期，不能推定。
[T12R109] CASE-SYN-17 | 情境代碼 | CASE-SYN-17 | 虛構服務進度詢問 | §5 SAMPLE/SYNTHETIC情境控制卡：情境代碼、授權、狀態及來源時間 | REAL替換時核對實際核定情境版本、用途授權範圍、狀態原件及擷取時間；缺項或衝突即UNKNOWN/HOLD，不以本SAMPLE推定。
[T12R110] SYN-NO-AUTH | 情境事實 | CASE-SYN-17 | 未附可核對授權 | §5情境控制卡：可核對授權欄 | 查實際核定情境的授權原件、用途及適用範圍；無證據即停止受限存取並記UNKNOWN/HOLD。
[T12R111] SYN-STATUS-UNK | 情境事實 | CASE-SYN-17 | 系統狀態未提供 | §5情境控制卡：系統狀態、來源及擷取時間欄 | 核對具權限的狀態原件／查詢輸出與擷取時間；沒有可核實來源就維持UNKNOWN，不宣稱受理或核准。
[T12R112] N-01 | 合成計算結果 | 合成班次 | 2/4=50% | §12列1 | 由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。
[T12R113] N-02 | 合成計算結果 | 合成班次 | 2/4=50% | §12列2 | 由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。
[T12R114] N-03 | 合成計算結果 | 合成班次 | 4/4=100% | §12列3 | 由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。
[T12R115] N-04 | 合成計算結果 | 合成班次 | 2/4=50% | §12列4 | 由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。
[T12R116] N-05 | 合成計算結果 | 合成班次 | 1/4=25% | §12列5 | 由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。
[T12R117] N-06 | 合成計算結果 | 合成班次 | 1/4=25% | §12列6 | 由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。
[T12R118] M-01 | 合成計算結果 | 合成班次 | 14.50,32.50,19.375,11.25,77.625 | §12列7 | 由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。
[T12R119] M-02 | 合成計算結果 | 合成班次 | 14.00,23.75,22.50,11.875,72.125 | §12列8 | 由原始答卷、EV表及明列公式重新計算；核對分子分母及未四捨五入值。
[T12R120] RET-003 | 合成計算結果 | 合成班次 | 82.00=17+30+22.50+12.50 | §11複評計算段：SYN-003總分算式及門檻 | 依該段列示的新知識答卷、四項新P觀察、沿用C/M分數與權重重算；核對未四捨五入分值及四門檻。
[T12R121] RET-004 | 合成計算結果 | 合成班次 | 80.25=14+32.50+22.50+11.25 | §11複評計算段：SYN-004總分算式及門檻 | 依該段列示的新知識答卷、新P3、沿用P1/P2/P4及C/M分數重算；核對未四捨五入分值及四門檻。
[T12R122] SF-073 | 合成更正定位 | SYN-004首次P1沿用 | 4；§8首次P向量第1格 | §8表SYN-004首次P向量第1格 | 核首次評分原件，不作新評。
[T12R123] SF-074 | 合成更正定位 | SYN-004首次P2沿用 | 3；§8首次P向量第2格 | §8表SYN-004首次P向量第2格 | 核首次評分原件，不作新評。
[T12R124] SF-076 | 合成更正定位 | SYN-004首次P4沿用 | 3；§8首次P向量第4格 | §8表SYN-004首次P向量第4格 | 核首次評分原件，不作新評。
[T12R125] SF-099 | 合成更正定位 | SYN-003新P1複評 | 3；EV-SYN-003-P1-R1 | §11複評新觀察EV-SYN-003-P1-R1 | 新複評觀察原件，不得沿用。
[T12R126] SF-100 | 合成更正定位 | SYN-003新P2複評 | 3；EV-SYN-003-P2-R1 | §11複評新觀察EV-SYN-003-P2-R1 | 新複評觀察原件，不得沿用。
[T12R127] SF-101 | 合成更正定位 | SYN-003新P3複評 | 3；EV-SYN-003-P3-R1 | §11複評新觀察EV-SYN-003-P3-R1 | 新授權情境觀察。
[T12R128] SF-102 | 合成更正定位 | SYN-003新P4複評 | 3；EV-SYN-003-P4-R1 | §11複評新觀察EV-SYN-003-P4-R1 | 新交接觀察，不得沿用。
[T12R129] SF-110 | 合成更正定位 | SYN-004首次P1沿用 | 4；SF-073 | §11沿用首次SF-073 | 核首次來源，不造新觀察。
[T12R130] SF-111 | 合成更正定位 | SYN-004首次P2沿用 | 3；SF-074 | §11沿用首次SF-074 | 核首次來源，不造新觀察。
[T12R131] SF-112 | 合成更正定位 | SYN-004新P3複評 | 3；EV-SYN-004-P3-R1 | §11新P3觀察EV-SYN-004-P3-R1 | 新P3複評觀察原件。
[T12R132] SF-113 | 合成更正定位 | SYN-004首次P4沿用 | 3；SF-076 | §11沿用首次SF-076 | 核首次來源，不造新觀察。
[T12R133] SCORE-SYN-001-knowledge | 合成衍生分數 | SYN-001 | 16/20 | §8表 SYN-001 knowledge欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R134] SCORE-SYN-001-practical | 合成衍生分數 | SYN-001 | 35/40 | §8表 SYN-001 practical欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R135] SCORE-SYN-001-case | 合成衍生分數 | SYN-001 | 21.25/25 | §8表 SYN-001 case欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R136] SCORE-SYN-001-communication | 合成衍生分數 | SYN-001 | 12.5/15 | §8表 SYN-001 communication欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R137] SCORE-SYN-001-total | 合成衍生分數 | SYN-001 | 84.75/100 | §8表 SYN-001 total欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R138] SCORE-SYN-002-knowledge | 合成衍生分數 | SYN-002 | 13/20 | §8表 SYN-002 knowledge欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R139] SCORE-SYN-002-practical | 合成衍生分數 | SYN-002 | 30/40 | §8表 SYN-002 practical欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R140] SCORE-SYN-002-case | 合成衍生分數 | SYN-002 | 17.5/25 | §8表 SYN-002 case欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R141] SCORE-SYN-002-communication | 合成衍生分數 | SYN-002 | 10/15 | §8表 SYN-002 communication欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R142] SCORE-SYN-002-total | 合成衍生分數 | SYN-002 | 70.50/100 | §8表 SYN-002 total欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R143] SCORE-SYN-003-knowledge | 合成衍生分數 | SYN-003 | 17/20 | §8表 SYN-003 knowledge欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R144] SCORE-SYN-003-practical | 合成衍生分數 | SYN-003 | 17.5/40 | §8表 SYN-003 practical欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R145] SCORE-SYN-003-case | 合成衍生分數 | SYN-003 | 22.5/25 | §8表 SYN-003 case欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R146] SCORE-SYN-003-communication | 合成衍生分數 | SYN-003 | 12.5/15 | §8表 SYN-003 communication欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R147] SCORE-SYN-003-total | 合成衍生分數 | SYN-003 | 69.50/100 | §8表 SYN-003 total欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R148] SCORE-SYN-004-knowledge | 合成衍生分數 | SYN-004 | 11/20 | §8表 SYN-004 knowledge欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R149] SCORE-SYN-004-practical | 合成衍生分數 | SYN-004 | 30/40 | §8表 SYN-004 practical欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R150] SCORE-SYN-004-case | 合成衍生分數 | SYN-004 | 22.5/25 | §8表 SYN-004 case欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R151] SCORE-SYN-004-communication | 合成衍生分數 | SYN-004 | 11.25/15 | §8表 SYN-004 communication欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R152] SCORE-SYN-004-total | 合成衍生分數 | SYN-004 | 74.75/100 | §8表 SYN-004 total欄 | 由逐題答卷／EV及§7公式重算；核分母及門檻。
[T12R153] SCORE-SYN-003-retest-knowledge | 合成複評數值 | SYN-003 | 17/20 | §11複評計算列 SYN-003 | 依新答卷、新EV及明列沿用原始分數重算。
[T12R154] SCORE-SYN-003-retest-practical | 合成複評數值 | SYN-003 | 30/40 | §11複評計算列 SYN-003 | 依新答卷、新EV及明列沿用原始分數重算。
[T12R155] SCORE-SYN-003-retest-total | 合成複評數值 | SYN-003 | 82.00/100 | §11複評計算列 SYN-003 | 依新答卷、新EV及明列沿用原始分數重算。
[T12R156] SCORE-SYN-004-retest-knowledge | 合成複評數值 | SYN-004 | 14/20 | §11複評計算列 SYN-004 | 依新答卷、新EV及明列沿用原始分數重算。
[T12R157] SCORE-SYN-004-retest-practical | 合成複評數值 | SYN-004 | 32.50/40 | §11複評計算列 SYN-004 | 依新答卷、新EV及明列沿用原始分數重算。
[T12R158] SCORE-SYN-004-retest-total | 合成複評數值 | SYN-004 | 80.25/100 | §11複評計算列 SYN-004 | 依新答卷、新EV及明列沿用原始分數重算。

## Complete SAMPLE/SYNTHETIC register sidecar
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

## Candidate-specific deterministic QA
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\qa\TECHNICAL_QA_R04b.json
source_sha256=fa61110644327983ec3926e506e011d1cd08d5950f95d05bce61a19fbb0ad706
source_bytes=10328

{
  "receipt_type": "technical_and_visual_review_R04b",
  "doc_id": "0010",
  "requirement_id": "I02-E01",
  "candidate_state": "CANDIDATE_SAMPLE_SYNTHETIC",
  "candidate_docx": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\\candidate\\0010_I02-E01_R04b.docx",
  "candidate_docx_sha256": "9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
  "candidate_text_sha256": "b16f1c4e9f674b6b6a1258a09192a87f40d4e92430810091fe2eadfe228aba47",
  "source_binding_sha256": "ba6d5563500a77482160eaad3b1426962d7d69a488e0db3709aaca929685ea66",
  "blueprint_copy_sha256": "47b3387d2f97aeed2b42efe602ffcc9070c664d2e9da4a119d50d378354d3236",
  "register_sha256": "6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc",
  "native_pdf_sha256": "d1d1cf56a8b886e5e776b1a00cd105d2fce1d77670507edff202d2ea65a58707",
  "native_pdf_pages": 28,
  "technical_status": "PASS_WITHIN_LISTED_DETERMINISTIC_SCOPE",
  "visual_status": "INSPECTED_WITH_LAYOUT_NOTE",
  "visual_scope": "All 28 pages inspected through seven contact sheets; full-resolution review of pages 5, 14, 16, 24, 27 and 28. Page 28 continues the final two synthetic-register rows with repeated header; the page is sparse but is not blank and has no clipped rows. No independent semantic review is implied.",
  "semantic_review": "PENDING_INDEPENDENT_EXACT_SHA_REVIEW",
  "formal_acceptance": "NOT_ACCEPTED",
  "real_evidence": "UNKNOWN_NOT_PROVIDED",
  "checks": {
    "docx_sha_bound_to_native_render": {
      "pass": true,
      "detail": {
        "docx_sha256": "9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
        "render_input_sha256": "9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe"
      }
    },
    "docx_zip_integrity": {
      "pass": true,
      "detail": null
    },
    "python_docx_parse": {
      "pass": true,
      "detail": {
        "paragraphs": 44,
        "tables": 12,
        "sections": 8
      }
    },
    "exact_official_requirement_and_locator": {
      "pass": true,
      "detail": {
        "requirement": "對學員訓練成果有評核標準的訂定及說明。",
        "official_extract_sha256": "65ab23c7a778753d7fb60160bc54621c0978f1776262bfc46b6a3f95626a7823"
      }
    },
    "official_pdf_hash_matches_binding": {
      "pass": true,
      "detail": {
        "actual": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
        "bound": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709"
      }
    },
    "unique_blueprint_file_and_row_hashes_match_binding": {
      "pass": true,
      "detail": {
        "matching_rows": 1,
        "current_file_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
        "bound_file_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
        "row_sha256": "3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d",
        "bound_row_sha256": "3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d",
        "copy_matches_current_row": true
      }
    },
    "candidate_status_and_real_boundary": {
      "pass": true,
      "detail": {
        "contains_candidate": true,
        "contains_sample_synthetic": true,
        "contains_not_approved_not_effective": true,
        "stale_not_built_phrase_present": false
      }
    },
    "synthetic_register_157_rows_and_exact_order_match": {
      "pass": true,
      "detail": {
        "sidecar_rows": 157,
        "sidecar_unique_ids": 157,
        "embedded_rows": 157,
        "ids_equal_ordered": true,
        "sidecar_sha256": "6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc"
      }
    },
    "learning_objective_rows": {
      "pass": true,
      "detail": {
        "table_row_counts": [
          6,
          6,
          21,
          6,
          13,
          5,
          49,
          5,
          3,
          6,
          9,
          158
        ]
      }
    },
    "questionnaire_20_items_4_options": {
      "pass": true,
      "detail": {
        "table_row_counts": [
          6,
          6,
          21,
          6,
          13,
          5,
          49,
          5,
          3,
          6,
          9,
          158
        ]
      }
    },
    "rubric_12_construct_indicators": {
      "pass": true,
      "detail": {
        "table_row_counts": [
          6,
          6,
          21,
          6,
          13,
          5,
          49,
          5,
          3,
          6,
          9,
          158
        ]
      }
    },
    "four_synthetic_cases": {
      "pass": true,
      "detail": {
        "table_row_counts": [
          6,
          6,
          21,
          6,
          13,
          5,
          49,
          5,
          3,
          6,
          9,
          158
        ]
      }
    },
    "evidence_and_review_tables_complete": {
      "pass": true,
      "detail": {
        "table_row_counts": [
          6,
          6,
          21,
          6,
          13,
          5,
          49,
          5,
          3,
          6,
          9,
          158
        ]
      }
    },
    "summary_and_register_table_present": {
      "pass": true,
      "detail": {
        "table_row_counts": [
          6,
          6,
          21,
          6,
          13,
          5,
          49,
          5,
          3,
          6,
          9,
          158
        ]
      }
    },
    "four_case_answer_key_weighted_math_and_outcomes": {
      "pass": true,
      "detail": {
        "answer_key_count": 20,
        "cases": [
          {
            "case_id": "SYN-001",
            "computed": [
              16.0,
              35.0,
              21.25,
              12.5,
              84.75
            ],
            "displayed": [
              16.0,
              35.0,
              21.25,
              12.5,
              84.75
            ],
            "arithmetic_matches": true,
            "displayed_outcome_matches_thresholds": true
          },
          {
            "case_id": "SYN-002",
            "computed": [
              13.0,
              30.0,
              17.5,
              10.0,
              70.5
            ],
            "displayed": [
              13.0,
              30.0,
              17.5,
              10.0,
              70.5
            ],
            "arithmetic_matches": true,
            "displayed_outcome_matches_thresholds": true
          },
          {
            "case_id": "SYN-003",
            "computed": [
              17.0,
              17.5,
              22.5,
              12.5,
              69.5
            ],
            "displayed": [
              17.0,
              17.5,
              22.5,
              12.5,
              69.5
            ],
            "arithmetic_matches": true,
            "displayed_outcome_matches_thresholds": true
          },
          {
            "case_id": "SYN-004",
            "computed": [
              11.0,
              30.0,
              22.5,
              11.25,
              74.75
            ],
            "displayed": [
              11.0,
              30.0,
              22.5,
              11.25,
              74.75
            ],
            "arithmetic_matches": true,
            "displayed_outcome_matches_thresholds": true
          }
        ]
      }
    },
    "retest_arithmetic_matches_written_results": {
      "pass": true,
      "detail": {
        "SYN-003": 82.0,
        "SYN-004": 80.25
      }
    },
    "retest_answers_new_ratings_provenance_and_all_thresholds": {
      "pass": true,
      "detail": {
        "retests": [
          {
            "case_id": "SYN-003",
            "answer_vector_count": 20,
            "displayed_knowledge": 17,
            "computed_knowledge": 17,
            "practical": 30.0,
            "P3": 3,
            "total": 82.0,
            "expected_total": 82.0,
            "all_four_thresholds_pass": true,
            "arithmetic_matches": true
          },
          {
            "case_id": "SYN-004",
            "answer_vector_count": 20,
            "displayed_knowledge": 14,
            "computed_knowledge": 14,
            "practical": 32.5,
            "P3": 3,
            "total": 80.25,
            "expected_total": 80.25,
            "all_four_thresholds_pass": true,
            "arithmetic_matches": true
          }
        ]
      }
    },
    "font_floor_body_10_5_and_table_9_5": {
      "pass": true,
      "detail": {
        "body_min_pt": 10.5,
        "table_min_pt": 9.5,
        "missing_size_runs": {
          "body": 0,
          "table": 0
        }
      }
    },
    "native_word_pdf_and_all_page_rasters_match": {
      "pass": true,
      "detail": {
        "pdf_pages": 28,
        "png_pages": 28,
        "contact_sheets": 7,
        "pdf_sha256": "d1d1cf56a8b886e5e776b1a00cd105d2fce1d77670507edff202d2ea65a58707",
        "render_receipt": {
          "route": "Microsoft Word COM native export",
          "input_docx": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\\candidate\\0010_I02-E01_R04b.docx",
          "input_docx_sha256": "9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
          "pdf_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\\qa\\render_R04b_native\\0010_I02-E01_R04b.pdf",
          "opened": true,
          "page_count": 28,
          "paragraph_count": 2039,
          "table_count": 12,
          "exported": true,
          "pdf_sha256": "d1d1cf56a8b886e5e776b1a00cd105d2fce1d77670507edff202d2ea65a58707",
          "new_word_process_ids": [],
          "error": null
        }
      }
    }
  },
  "failed_checks": [],
  "limitations": [
    "No independent semantic PASS is claimed.",
    "Blueprint outward training-policy/public-disclosure fields applicability remains PARTIAL/UNKNOWN.",
    "No actual roster, authorization, learner, assessment, or association record was supplied; all cases are SAMPLE/SYNTHETIC.",
    "Page 28 is a short continuation page; all rows are readable, but the page retains substantial whitespace."
  ],
  "checked_at_taipei": "2026-10-30T00:53:46+08:00"
}

## Candidate-specific visual QA
source_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030\qa\VISUAL_QA_R04b.json
source_sha256=104cc4aab33924b56b74ed81e3072b98a9b6caa71623647be1171269302c2aeb
source_bytes=5539

{
  "receipt_type": "visual_review_R04b",
  "doc_id": "0010",
  "requirement_id": "I02-E01",
  "candidate_sha256": "9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
  "native_pdf_sha256": "d1d1cf56a8b886e5e776b1a00cd105d2fce1d77670507edff202d2ea65a58707",
  "native_render_receipt_sha256": "ebcdfb755205e4ec9dc3e7b618028f2b2d13f93cd167a20501444065e60a3966",
  "page_count": 28,
  "all_page_rasters": [
    {
      "page": 1,
      "sha256": "604b6152c886a65d9a2fd28d6a0562b80c851e2022494e61a56d768db5e5979f"
    },
    {
      "page": 2,
      "sha256": "2f579d1a992f694f18dec0385c976a94e880e7fe92c663e11a272090b31d66d7"
    },
    {
      "page": 3,
      "sha256": "c81b40f3cd0aef25b15f772f520ebe34e79f2a3883d27cb40f43ea1cfb6c84b5"
    },
    {
      "page": 4,
      "sha256": "e8f800a4487f51d678bd57e952fb6112315126f47fee5f10a7051941bf6bf5f8"
    },
    {
      "page": 5,
      "sha256": "93ddfd9cb017e728656132223a034254c2b3c98f746a38b4f37955359831e8c6"
    },
    {
      "page": 6,
      "sha256": "b7080da55fd597818dce42d48cceea176f2e890a85324bda4d0f3d51faf5ce24"
    },
    {
      "page": 7,
      "sha256": "cdd09e5583afb939fb311a7aa8dd5987bea58b463e63ad0a88fac631d9008cef"
    },
    {
      "page": 8,
      "sha256": "00eb2f4d1a8187cfa743b02205bcc6d2dd353793d08478953e4d4acb7bfd0518"
    },
    {
      "page": 9,
      "sha256": "38fe03bf5f4087c6f667aadac7e3bf11764dcd4f363b1c5277091c54c1f7aff2"
    },
    {
      "page": 10,
      "sha256": "939e18ffb4b4f15cd4fae9f3076498ade8c68d5cba0b818c0a55b66cc58c6123"
    },
    {
      "page": 11,
      "sha256": "f90886b0e788911edfe2fddd530f33c4ea8f057e298f288c4c5ce6318eeaadc4"
    },
    {
      "page": 12,
      "sha256": "1a5c67638eed72f8761f7507b06263054fc6ab931cb3a3bb3ed036ffbe653e8b"
    },
    {
      "page": 13,
      "sha256": "0abb47c03272e1126ecc4ceac679856e04d4d54f9ca194a7e81151d3a41d31a3"
    },
    {
      "page": 14,
      "sha256": "d9d1c9d2b98ed8fbd4b064f855edfbbde75918af83c08865436dbd184146ecb4"
    },
    {
      "page": 15,
      "sha256": "dd56b923420db0ac1d4c62e9293761f5397dc6f98c0be1abf87ece98ef7b9804"
    },
    {
      "page": 16,
      "sha256": "4cc6175a6e21322aa44bc493fa627077928b2239f784d1f94e514e8d8d158712"
    },
    {
      "page": 17,
      "sha256": "feb9382f22d58bf1a92418d103f4d159c3c040c2f74ddb96a86848bfda0cba23"
    },
    {
      "page": 18,
      "sha256": "3535c247c779f78825b66a0cb3c5ea1c6f11f2d7530dcc0dcc5fe04cdd033d1f"
    },
    {
      "page": 19,
      "sha256": "d0feaa282c48bc6347d29bfef74773cc0265124edef1e1e4ef90291839d7c042"
    },
    {
      "page": 20,
      "sha256": "2cfdf9ed2f54a78fa67437c6d95f6306be831d1f9ead6c321dc01ce73879b740"
    },
    {
      "page": 21,
      "sha256": "5a30fa15b208cb9e0a1bce3199b67978bd5838cd46241341abfca56d842072a9"
    },
    {
      "page": 22,
      "sha256": "8a216c97c7f466a433347482638ad2d5b883e100163dedc249f018b35094f0df"
    },
    {
      "page": 23,
      "sha256": "5f814e503410ce16c8fbd3448057d18971375b14d7c130a7ece62e4716748dce"
    },
    {
      "page": 24,
      "sha256": "7f6287d15fb4c962f6cff179bf2f81cbc6926ee32cd722adf86293cfb5954bbe"
    },
    {
      "page": 25,
      "sha256": "3859764dd3b3e52befab5576fbf51604674930334f7611de49be555ed0bf509d"
    },
    {
      "page": 26,
      "sha256": "e3f147cc6ec0b1dcd79ce087350c2e6cedfb58ebabaeb472c7c9c2e35e85bee6"
    },
    {
      "page": 27,
      "sha256": "6d2786eddcb33e13d0b766aa51280a343365c9866d3350d37ee29c648b828ad7"
    },
    {
      "page": 28,
      "sha256": "336956523d74b5c7a19b6b7ad8e239dfb7bbd44321667325e61fc2346260b4df"
    }
  ],
  "contact_sheets": [
    {
      "name": "sheet-001.jpg",
      "sha256": "9490e0389db11db51d69f07a41be869fcb07818465e8e7b899fa886a9fdaa348"
    },
    {
      "name": "sheet-002.jpg",
      "sha256": "4feea86538b88706b34760587c12292bb7ee4b7bd971cc3a7a9ec58fdc8263db"
    },
    {
      "name": "sheet-003.jpg",
      "sha256": "b0ef9dce34fbfd2a749773c58cc60c00d7d7bed75fac748a4583b0e88f962308"
    },
    {
      "name": "sheet-004.jpg",
      "sha256": "e83e36cd41e02d3e96618194f3607dbe0610ffd0c14b956deffb4f2255f3d243"
    },
    {
      "name": "sheet-005.jpg",
      "sha256": "2fe9de60efaad9aa809ebb3b8900bc3ce889620f5db9dfb0912ac284c4ac64aa"
    },
    {
      "name": "sheet-006.jpg",
      "sha256": "2899d65860e9f5824a95030e1ef74d1af19edde200bd3bdf9b8544a2cc7ac06f"
    },
    {
      "name": "sheet-007.jpg",
      "sha256": "d3578b37adbf998ccb3fa670cc435d49a1c92ec93bcd26b5dfe7557da5ec89ba"
    }
  ],
  "inspection_scope": {
    "contact_sheet_pages": "1-28, all seven contact sheets inspected",
    "full_resolution_pages": [
      5,
      14,
      16,
      24,
      27,
      28
    ],
    "observations": [
      "Page headings, repeated register headers, table boundaries and footers are consistent across the 28-page native Word render.",
      "Dense rubric and six-column replacement-register tables remain within page bounds; sampled full-resolution cells are legible and not clipped.",
      "Page 28 continues the last two synthetic-register rows under a repeated header. It has substantial lower-page whitespace but is not blank; both rows are readable and not split or clipped.",
      "Pages 6 and 11 have short section content with visible whitespace; no overflow, overlap or clipped content was observed."
    ]
  },
  "visual_verdict": "PASS_WITH_LAYOUT_NOTE",
  "reviewer_role": "primary visual inspection; not an independent semantic review",
  "checked_at_taipei": "2026-10-30T00:53:52+08:00"
}
