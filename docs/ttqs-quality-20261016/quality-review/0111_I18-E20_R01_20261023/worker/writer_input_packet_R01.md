# INPUT 1: SOURCE PACKET
# 0111 I18-E20 Source Packet

## Authority and scope
- Project: TTQS ONE; deliverable ID: 0111; official requirement ID: I18-E20.
- Exact official checkbox text: 「提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。」
- Official evidence table: page 7. The exact checkbox was visually checked in the page image and appears in the retained full page-7 extraction after whitespace normalization. An initial pypdf extraction returned only 793 characters and omitted the target item; the packet now uses the existing full extraction bound to the same PDF SHA, and records this discrepancy in source_stage_receipt_0111_R02.json.
- Requirement-to-deliverable crosswalk row: I18-E20 → 0111 only; title: 特殊績效及社會面成果證據登錄表.
- Internal Blueprint index / official checkbox serial: NOT ASSERTED. Bind by doc_id + requirement ID + exact checkbox text; do not infer checkbox numbering from deliverable ID.
- Blueprint source: CONTROL/BLUEPRINT_CURRENT.jsonl, file SHA-256 `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`.
- Crosswalk source: CONTROL/TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv, file SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`.
- Official PDF: `TTQS查核佐證文件資料表-訓練機構版 (2).pdf`, SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Historical corpus lists old 0111 files as discovery/inventory only. Historical DOCX body reuse is prohibited; do not use them as writing templates or evidence.

## Distinct purpose
This is a document-specific analysis/evaluation report and evidence registry for social or other special training outcomes stated by target customers and learners. It is not the I18-E19 survey/action-plan package (0110), not the I18-E21 licensing/return-training rate report (0112), and not a financial performance report. Adjacent requirements may be named only as boundaries; do not import their sample facts or conclusions.

## Required analysis and use
Use the complete current unique Blueprint JSON attached. It requires purpose, evidence scope, population/inclusion/exclusion, source and field definitions, denominator and formula, complete worked SAMPLE/SYNTHETIC case, group comparison/trend, findings and evidence strength, limitations, actionable recommendations, roles/deadlines/follow-up measures, synthetic replacement register, attachment index and version/review controls. Required tables include a data dictionary, detailed sample data and recomputation, group/difference priority matrix, evidence-to-finding-to-action trace, and official requirement crosswalk.

## Evidence and integrity limits
No current REAL outcome data, authorized third-party originals, customer/learner statements, signed approvals, or source locations are supplied in this packet. Therefore the manuscript must be a complete SAMPLE/SYNTHETIC worked example only. It must not say that 原始點協會 ran a real course, achieved an outcome, received an award, or obtained third-party confirmation. Use synthetic role codes and `SYN-` IDs; every synthetic date, count, percentage, statement, decision, source locator, and outcome must map to a replacement-register key and exact section/table/field. Mark all sample paths as fictional examples, never actual repository locations.

## Source text
The printed page 7 lists the 4-point evidence class, including the exact I18-E20 checkbox quoted above. The attached `source/official_source_page7_text.txt` is the PDF text extraction for that page. The page image inspected in the source workspace is from the same PDF SHA above.


# INPUT 2: UNIQUE BLUEPRINT JSON
{
  "deliverable_id": "0111",
  "requirement_id": "I18-E20",
  "final_filename": "0111__特殊績效及社會面成果證據登錄表.docx",
  "document_genre": "分析／評估報告｜特殊績效及社會面成果證據登錄表",
  "document_purpose": "本件專屬焦點：特殊績效及社會面成果證據登錄表；需直接回應的官方佐證要求為：提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。",
  "primary_user_or_reader": "供主管與決策者讀取資料、理解計算、判斷差距並採取具體決策。",
  "evidence_role": "呈現方法、完整合成或已驗證結果、分析、限制及可追溯決策；不得冒充實績。 本文件只擁有 I18-E20 的直接紀錄／分析口徑；不得吞併其他要求的事實。",
  "source_of_truth": "官方查核佐證表精確原文『提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。』，表內頁次 7，讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH；REQ_157_MAP 對應 I18-E20；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。",
  "required_sections": "摘要、用途與決策問題；官方要求及分析範圍；資料來源、樣本與納入排除；指標定義、分母與計算方法；完整示範資料及逐步計算；分群／趨勢／差異結果；圖表解讀及品質限制；發現、原因與證據強度；結論與可執行建議；責任人、期限與追蹤指標；合成資料聲明及真實替換清單；附件索引、覆核與版本",
  "required_tables_or_figures": "資料欄位—定義—分母—來源—限制字典；合成明細／彙總結果與逐步計算；分群比較／差距優先排序矩陣；結論—證據—建議—責任—追蹤指標表；官方要求—結果—證據位置—覆核追溯表",
  "required_fields_or_questions": "原件是否由真正第三方/主管機關出具？；能否回查出具者/日期/事件？；是否取得必要授權？；本文件中哪一段/哪一表直接證明：「提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。」？；目前證據強度對應哪一分級？缺什麼資料才可升到下一級？；分析母數及排除說明；計算口徑與四捨五入；建議決策及適用限制；合成事實替換登錄鍵",
  "required_calculations_or_analysis": "原件取得率=已驗證原件/應取得原件。不得稱為組織實績。",
  "required_cross_references": "同要求分件 無；相鄰要求 I18-E19, I18-E21；共用原始來源時只引用核實結果，不複製別份文件正文。",
  "real_data_required": "升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置；第三方出具者；原件編號/日期；可回查聯絡/查證方式。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。",
  "third_party_evidence_required": "若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。",
  "prohibited_fabrication": "不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。 不得代替第三方/政府/雇主/媒體/保險或證照機構製造「已出具」原件。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。",
  "title_blind_test": "遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『特殊績效及社會面成果證據登錄表』並證明『提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。』；若可無修改移作其他要求即失敗。",
  "negative_choice_neighbors": "0110《問卷調查及課後行動計畫評估表等顯示目標客戶及_可直接使用成品》（I18-E19）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0112《輔導考照及學員回訓率追蹤分析表》（I18-E21）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。",
  "acceptance_tests": "移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『特殊績效及社會面成果證據登錄表』，且能指出直接回應『提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。",
  "document_role": "analysis_report",
  "official_requirement_text": "提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。",
  "official_checkbox_text": "提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。",
  "official_evidence_table_page": "7",
  "official_source_readback_status": "PDF_TEXT_EXACT_PAGE_MATCH",
  "official_visually_checked_pages": "",
  "requirement_deliverable_siblings": "0111",
  "docx_body_template_policy": "FROM_SOURCE_ONLY; old body is discovery evidence only and prohibited as rebuild template; Wave005 R3 0031-0040 quality-height references only; Wave001-004 tainted; old Wave005 invalid; Wave006 prohibited.",
  "synthetic_population_rule": "缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。",
  "historical_blueprint_source": "be446cb69473a7b5b62b780abd03abbd461480c8c2b4f6a38c46d2741577924a",
  "historical_body_use": "PROHIBITED",
  "source_map_notes": "129 exact official requirement rows + reconciled 142-ID crosswalk; official source PDF and exact Drive readback evidence are recorded in runtime SOURCE/CONTROL maps."
}


# INPUT 3: WRITER BRIEF
# Writer brief — 0111 I18-E20

Write a complete, usable Traditional-Chinese evaluator-facing analysis report and evidence registry for a volunteer community association. Do not write a template outline. Deliver finished prose and completed SAMPLE/SYNTHETIC tables. Use only the attached official source packet and unique Blueprint. Do not consult or copy historical 0111 DOCX bodies.

## Exact scope
- Document 0111 / I18-E20 / official checkbox: 「提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。」.
- The task is the social/other special-performance statement from target customers and learners. Distinguish 0110 I18-E19 (survey plus after-course action plan) and 0112 I18-E21 (licensing and return-training tracking). Do not copy or merge their facts.
- Use an illustrative community-service accessibility outcome as a wholly fictional worked example. Label each relevant page/table and every dataset `SAMPLE / SYNTHETIC — NOT ASSOCIATION REAL PERFORMANCE`. State that no REAL source evidence was provided and formal acceptance is not granted.

## Required finished contents
Follow all 12 required sections and all required tables in the attached UNIQUE_BLUEPRINT_0111_R01.json. Include: (1) concise executive summary and use instructions; (2) eligibility and evidence-strength rubric E0–E3; (3) population, sampling, inclusion/exclusion, response and denominator definitions; (4) field dictionary with source, owner role code, validation and limitations; (5) a complete synthetic record with at least 8 target-customer codes and 8 learner codes, separated denominators; (6) baseline/follow-up comparison with explicit calculation and percentage-point delta; (7) an original-evidence acquisition-rate example using verified-originals / required-originals and a clear HOLD if no genuine source exists; (8) evidence-to-claim-to-recommendation trace; (9) exceptions, disagreement, missing-source and correction workflow; (10) actionable recommendations with role codes, dates and follow-up measures; (11) official requirement-to-field-to-location crosswalk; (12) at least 24 individually keyed synthetic replacement-register rows, each with a locator and the real replacement evidence needed.

## Arithmetic fixture (must be followed exactly or explain a more complete internally consistent alternative)
- Reporting window is synthetic: 2026-04-01 through 2026-06-30.
- Target-customer sample: 8 eligible, 8 responses; baseline outcome count 3/8 (37.5%); follow-up outcome count 6/8 (75.0%); change = +3 respondents and +37.5 percentage points. State this is descriptive synthetic data, not causal proof.
- Learner sample: 8 eligible, 8 responses; 6/8 (75.0%) report a specified application; this is not certificate pass rate, satisfaction rate, or a second customer denominator.
- Synthetic originals required in the illustrative completeness check: 2; genuine originals actually supplied to this task: 0; verified originals 0/2 = 0%. Make clear these are sample planning quantities only and no original document is fabricated or attached.
- When calculating rates, define numerator, denominator, unit, window, exclusions, rounding, and N/A/HOLD rule.

## Integrity and review controls
Never invent REAL people, organizations, course records, awards, signatures, approvals, third-party source documents, or association decisions. Use synthetic role codes only, no names. Include rejection/hold thresholds for incomplete denominators, unsupported attribution, missing consent, conflicting records, and absent originals. Use only fictional sample paths under `SAMPLE_ONLY/0111/`. Avoid empty fields and future-tense placeholders: complete the sample end-to-end while preserving an actual REAL section as UNKNOWN/HOLD. Keep table text readable at 9.5pt minimum when later laid out.

## Output contract
Return only the full manuscript in Markdown, Traditional Chinese, with tables in Markdown. No commentary, no code, no DOCX generation, no claims of actual model/provider identity. Aim for a complete but concise report of roughly 6,000–8,000 Chinese characters. Every computed value must recalculate from the displayed rows.


# INPUT 4: OFFICIAL PAGE 7 TEXT EXTRACT

7
項目 評核指標項目
內涵說明（以下為
例，但不以此為
限）
常見參考佐證資料
（並註明資料來源及頁碼）
的效果。
4分 目標客戶及學員
認為訓練有顯著具體
績效。
認為訓練有達成能力提升的效
果。
 執行目標客戶及學員滿意度調查
及分析（系統及流程面） 。
 提出目標客戶及學員對訓練達能
力提升之說明（學習技能面） 。
 學員培訓前後自我評量表 及雷達
分析圖呈現提升效果。
 指導學員參加技能競賽獲獎。
 感謝函。
 證照獲取率。
 其他：
3分之常見參考佐證資料：
 問卷調查及課後行動計 畫評估表
等顯示目標客戶及學員認為訓練
有績效改善的效果。
 提出目標客戶及學員對訓練達組
織績效改善之說明（財務面） 。
 高證照通過率之證明資料。
 提高薪資紀錄。
 社群網站知識討論區，人員使用
網站頻率高。
 其他：
4分之常見參考佐證資料：
 問卷調查及課後行動計 畫評估表
等顯示目標客戶及學員認為訓練
對組織績效的改善 及提升均有顯
著的效果。
 提出目標客戶及學員對訓練達特
殊 績 效 之 說 明 （ 社 會 面 、 其
他） 。
 輔導考照 及 學 員 回 訓 率 持 續 提
高。
 會員人數逐年增加。
 其他：

19. 訓 練 系 統 的 市
場功能
─ 目標市場
及顧客的價
值創造
評分標準：
1分 目標市場及顧客
價值均有提升，然而
未有具體紀錄及評
量。
2分 目標市場及顧客
價值均有部分提升效
果。
1 分之常見參考佐證資料：
 目標市場及顧客價值均有提 升，
然而未有具體紀錄及評量。
 提出心得與知識分享執行成效
（系統及流程面） 。
 口頭說明學員訓後就業狀況，但
未有具體紀錄及評量。
 學員考照通過率有增加，但未有
