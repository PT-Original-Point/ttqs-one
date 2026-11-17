# TTQS ONE W1 獨立語意審查工作包
work_id: TTQS_ONE_0029_I05-E03_W1_SEMANTIC_REVIEW_R12_20261117
doc_id: 0029
requirement_id: I05-E03
candidate_status: CANDIDATE
candidate_path: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CANDIDATES\0029_I05-E03_R01\0029_I05-E03_CANDIDATE_R12.docx
candidate_sha256: 6b3150ba1bb3609bb7c14f8b5d8989d09d0da30506baa2b74f504eba4df7b289
candidate_body_sha256: 920fa41e41be3fd0309b95a2f74423f496975e48a662cd2d85cef0b00c2dbc3d
review_packet_is_read_only: true

請審查下列同一候選的語意、官方需求忠實度、策略／計畫文類可操作性、合成事實及計算一致性、SAMPLE/REAL界線、至少兩個負向近鄰拒絕，以及 R08 已知 minor findings 是否在本版妥善收斂。候選目前仍是 CANDIDATE。不得修改檔案或做視覺評價。只檢查 exact candidate body 與所附權威來源／Blueprint／facts。若有缺陷，只回報具體 severity、locator、evidence、required_action；不要重寫全文。回覆單一 JSON，欄位為 work_id、candidate_sha256、decision(PASS/FAIL)、findings、negative_neighbor_result、synthetic_register_result、calculation_result、source_alignment、limitations。

## Previous exact-SHA review context
R08 review findings are historical context only and must not be carried forward automatically. A fresh W1 review of exact R11 SHA d6ee269caa01269aed194734a63610a25c678ad38d56cc2be39b3ecf9e60ef0d returned PASS with three minor findings and one optional informational improvement. Response receipt SHA-256 f6306846b00a91a862fe6daeb65b961e4c60ad696fc30d4f3b99ddd70790aab7.
1. The printed version trace ended at R10 while the candidate was R11. R12 now adds the R11/R12 revision events and external-receipt trace.
2. Purpose text appeared to disclaim performance reporting while reporting sample outcomes. R12 now says it does not replace a full training-results evaluation report and scopes its content to planning, measurement, judgment, and synthetic demonstration.
3. Scope excluded practical execution while examples described execution. R12 now qualifies real delivery/performance as excluded and states the operational steps are synthetic demonstrations only.
4. Optional: reviewer suggested a reason column; not required for semantic PASS because rationale is present in adjacent sections and the review marked it informational.
Re-evaluate the full current exact body and all requirement, calculation, fact/register, sample/real, and negative-neighbor checks. Confirm whether each previous minor finding is closed. No visual claim, no file changes, no automatic promotion.
## Source packet manifest
{
  "task": "TTQS_ONE_0029_I05-E03_SOURCE_PACKET_R01_20261117",
  "doc_id": "0029",
  "requirement_id": "I05-E03",
  "official_source_pdf": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\SOURCES\\TTQS查核佐證文件資料表-訓練機構版 (2).pdf",
  "official_source_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
  "official_page": 2,
  "crosswalk_file_sha256": "1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679",
  "crosswalk_row_sha256": "c881fdb874a5af6ea06a589279676fd6be9c852e83951ec42866332c55fe0ae6",
  "blueprint_file_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
  "blueprint_line": 29,
  "blueprint_row_sha256": "c178080a9a69454148bf607398bc9a0cfb3837fd5394d0dccfe1d1aa349bf573",
  "facts_sha256": "ab14e24c85d285f49fb6d89bbf6e3fe8b830ce12117aed9a61c43205a295ec35",
  "packet_sha256": "d14d9fbd6733d84fd6ec1c798980a440e43577c555df631609bf8266ff13eaf8",
  "state": "READY_WRITER",
  "created_utc": "2026-11-16T21:05:32.558286+00:00"
}

## Official source text
 
2 
項目 評核指標項目 
內涵說明（以下為
例，但不以此為
限） 
常見參考佐證資料 
（並註明資料來源及頁碼） 
系
統
性 
4.訓練品質
管 理 的
系 統 化
文 件 資
訊 
展示文件（如：訓練
手冊、訓練體系圖
表、程序或辦法等相
關文件）以說明訓練
機構如何運作TTQS
管理系統。 
展示此文件如何核
准、公告、更新、保
存紀錄。 
 訓練需求的定期調查與分析。 
 不同訓練課程的設計與規劃方
向。 
 訓練的提供方式及選擇的指標。 
 訓練結果的評估 、訓練實施的依
據及標準化作業流程（SOP）。 
 機構如何運作 TTQS 管理系統及
如何核准、公告、更新、保存紀
錄的證明資料。 
 其他： 
 
連
結
性 
5.訓練規劃
及 經 營
目 標 的
連結性 
說明對外訓練發展課
程及年度營運計畫之
連結性。 
展現訓練發展重點課
程的行動計畫。 
 學員訓練 及訓練機構年度事業計
畫的相關資料。 
 訓練課程體系 及訓練機構業務策
略方向的相關資料。 
 訓練規劃 及達到客戶課程績效目
標的證明資料。 
 其他： 
能
力 
6.訓練機構
的 行 政
管 理 能
力 及 訓
練 主 管
相 關 職
能 
展現訓練單位有適當
的分工及人員有足夠
的訓練相關能力以執
行對外訓練業務。 
展現訓練部門主管具
備能充分了解訓練單
位發展方向訂定及執
行之能力。 
 工作經驗的相關受訓證明。 
 專業訓練人員 職能評估方法等證
明。 
 訓練機構具備執行訓練業務相關
職能的說明。 
 其他： 
設計 
（Design） 
7.訓練需求相關
的職能分析及
應用 
展現課程設計過程中
有適當的確認客戶或
市場訓練需求，據以
進行適當的職能落差
分析。 
展現職能分析與運用
之方法及紀錄。 
 訓練課程計畫配合客戶 及受訓者
需求、職能需求的調查規劃的證
明。 
 針對學員做職能盤點或職能分析
並據以規劃適切課程的證明資
料。 
 對相關職能分析 及運用的方法均
能適時檢討隨時改進。 
 有課程設計進度表、課程規劃流
程圖說明、訓練規劃書等佐證資
料。 
 其他： 
8.訓練方案的系
統設計 
展現訓練發展課程規
劃時，有適當的訓練
課程設計流程。 
展 現 有 適 當 的 訓
練 方 案 產 出 ， 如
訓 練 目 標 、 訓 練
 相關文件紀錄能顯示近年來訓練
目標、訓練方法、課程時程安
排、師資遴選、學員遴選條件、
訓練教材、設施與環境、訓練評
估方法等的檢討及改善過程。 
 針對訓練方案的系統設計能適時
## Crosswalk row
{
  "requirement_id": "I05-E03",
  "deliverable_count": "1",
  "split_extra_count": "0",
  "deliverable_ids": "0029",
  "document_titles": "訓練規劃及達到客戶課程績效目標的證明資料_可直接使用成品"
}

## Unique blueprint row
{
  "deliverable_id": "0029",
  "requirement_id": "I05-E03",
  "final_filename": "0029__訓練規劃及達到客戶課程績效目標的證明資料_可直接使用成品.docx",
  "document_genre": "策略／計畫文件｜訓練規劃及達到客戶課程績效目標的證明資料_可直接使用成品",
  "document_purpose": "本件專屬焦點：訓練規劃及達到客戶課程績效目標的證明資料_可直接使用成品；需直接回應的官方佐證要求為：訓練規劃及達到客戶課程績效目標的證明資料。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。",
  "primary_user_or_reader": "供理監事、主管與執行人員把官方要求轉為可執行的方向、責任、時程與衡量方式。",
  "evidence_role": "以源頭策略或計畫證明要求如何落地；提供目標、責任、基準與決策依據。 本文件只擁有 I05-E03 的直接紀錄／分析口徑；不得吞併其他要求的事實。",
  "source_of_truth": "官方查核佐證表精確原文『訓練規劃及達到客戶課程績效目標的證明資料。』，表內頁次 2，讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH；REQ_157_MAP 對應 I05-E03；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。",
  "required_sections": "文件用途與決策範圍；官方要求與適用界線；現況、需求與可驗證來源；目標對象、價值與服務範圍；策略／計畫主軸與因果關係；目標、基準、指標與計算口徑；工作分解、責任與協作；資源、時程與里程碑；風險、假設及應變門檻；檢討頻率、決策紀錄與修訂；完整合成示例與真實資料替換清單；證據索引、限制與版本核對",
  "required_tables_or_figures": "欄位—定義—來源—填寫者—驗證規則；完整合成填寫列及欄位解說；問題／例外—修正—覆核及追蹤；官方要求—表單欄位—附件定位追溯表",
  "required_fields_or_questions": "合成資料識別碼；日期欄位及合成標示；責任角色代碼；來源／附件位置欄位；判定、理由、覆核及後續行動",
  "required_calculations_or_analysis": "若此表單有數量、金額、期間或比例，明列定義、分子分母與逐步算例；若沒有，明示不適用並提供至少一個欄位驗證／完整度判斷示例。",
  "required_cross_references": "同要求分件 無；相鄰要求 I05-E02, I06-E01；共用原始來源時只引用核實結果，不複製別份文件正文。",
  "real_data_required": "升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。",
  "third_party_evidence_required": "若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。",
  "prohibited_fabrication": "不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。",
  "title_blind_test": "遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『訓練規劃及達到客戶課程績效目標的證明資料_可直接使用成品』並證明『訓練規劃及達到客戶課程績效目標的證明資料。』；若可無修改移作其他要求即失敗。",
  "negative_choice_neighbors": "0028《訓練課程體系及訓練機構業務策略方向的相關資料_完整工作稿》（I05-E02）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0030《工作經驗的相關受訓證明_可直接使用成品》（I06-E01）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。",
  "acceptance_tests": "移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『訓練規劃及達到客戶課程績效目標的證明資料_可直接使用成品』，且能指出直接回應『訓練規劃及達到客戶課程績效目標的證明資料。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。",
  "document_role": "strategy_plan",
  "official_requirement_text": "訓練規劃及達到客戶課程績效目標的證明資料。",
  "official_checkbox_text": "訓練規劃及達到客戶課程績效目標的證明資料。",
  "official_evidence_table_page": "2",
  "official_source_readback_status": "PDF_TEXT_EXACT_PAGE_MATCH",
  "official_visually_checked_pages": "",
  "requirement_deliverable_siblings": "0029",
  "docx_body_template_policy": "FROM_SOURCE_ONLY; old body is discovery evidence only and prohibited as rebuild template; Wave005 R3 0031-0040 quality-height references only; Wave001-004 tainted; old Wave005 invalid; Wave006 prohibited.",
  "synthetic_population_rule": "缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。",
  "historical_blueprint_source": "2774c00840ec3d6c6d99ee65a36e0a97c7f3ddc87edeadd77d184c8310aadd59",
  "historical_body_use": "PROHIBITED",
  "source_map_notes": "129 exact official requirement rows + reconciled 142-ID crosswalk; official source PDF and exact Drive readback evidence are recorded in runtime SOURCE/CONTROL maps."
}

## Synthetic facts
{
  "work_id": "TTQS_ONE_0029_I05-E03_W2_WRITER_R01_20261117",
  "doc_id": "0029",
  "requirement_id": "I05-E03",
  "status": "SAMPLE_SYNTHETIC_ONLY",
  "facts": [
    {
      "key": "SYN-0029-001",
      "item": "fictional customer case label",
      "value": "SAMPLE-CUST-01",
      "unit": "label",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-002",
      "item": "fictional course label",
      "value": "SAMPLE-COURSE-01",
      "unit": "label",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-003",
      "item": "sample period label",
      "value": "SAMPLE-PERIOD-01",
      "unit": "label; no real calendar dates",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-004",
      "item": "planned course sessions",
      "value": 5,
      "unit": "sessions",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-005",
      "item": "planned/registered learners denominator",
      "value": 10,
      "unit": "learners",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-006",
      "item": "customer target attendance rate",
      "value": 85,
      "unit": "percent; threshold >=85%",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-007",
      "item": "planned attendance seat-sessions",
      "value": 50,
      "unit": "seat-sessions; 10 x 5",
      "source_type": "synthetic_calculation"
    },
    {
      "key": "SYN-0029-008",
      "item": "attended seat-sessions",
      "value": 46,
      "unit": "seat-sessions",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-009",
      "item": "attendance rate",
      "value": 92,
      "unit": "percent; 46/50 x 100",
      "source_type": "derived_synthetic"
    },
    {
      "key": "SYN-0029-010",
      "item": "learners meeting sample completion rule",
      "value": 9,
      "unit": "learners",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-011",
      "item": "customer target completion rate",
      "value": 80,
      "unit": "percent; threshold >=80%",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-012",
      "item": "completion rate",
      "value": 90,
      "unit": "percent; 9/10 x 100",
      "source_type": "derived_synthetic"
    },
    {
      "key": "SYN-0029-013",
      "item": "satisfaction scale maximum",
      "value": 5,
      "unit": "points; integer response scale 1-5",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-014",
      "item": "valid satisfaction responses",
      "value": 9,
      "unit": "responses",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-015",
      "item": "aggregate satisfaction score",
      "value": 40,
      "unit": "points; total across 9 valid responses",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-016",
      "item": "mean satisfaction",
      "value": 4.44,
      "unit": "points out of 5; 40/9 rounded to 2 decimals; 4.4 to 1 decimal",
      "source_type": "derived_synthetic"
    },
    {
      "key": "SYN-0029-017",
      "item": "paired pre/post assessment count",
      "value": 9,
      "unit": "learners",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-018",
      "item": "pre-assessment total and mean",
      "value": "558 total points; 62/100 mean",
      "unit": "points",
      "source_type": "synthetic_calculation"
    },
    {
      "key": "SYN-0029-019",
      "item": "post-assessment total and mean",
      "value": "738 total points; 82/100 mean",
      "unit": "points",
      "source_type": "synthetic_calculation"
    },
    {
      "key": "SYN-0029-020",
      "item": "customer target post-assessment mean",
      "value": 80,
      "unit": "points out of 100; threshold >=80",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-021",
      "item": "customer target mean gain",
      "value": 10,
      "unit": "points; threshold >=10",
      "source_type": "synthetic"
    },
    {
      "key": "SYN-0029-022",
      "item": "mean score gain",
      "value": 20,
      "unit": "points; 82-62",
      "source_type": "derived_synthetic"
    },
    {
      "key": "SYN-0029-023",
      "item": "sample conclusion",
      "value": "all four sample targets meet or exceed thresholds; derived only from the fictional aggregate case",
      "unit": "decision statement",
      "source_type": "derived_synthetic"
    },
    {
      "key": "SYN-0029-024",
      "item": "truth boundary",
      "value": "SAMPLE only; no real customer, contract, approval, delivery, attendee, survey, score record, customer acceptance or formal adoption is asserted; all real baselines UNKNOWN",
      "unit": "truth boundary",
      "source_type": "mandatory_label"
    }
  ]
}

## Exact R12 extracted candidate body
訓練規劃及達到客戶課程績效目標的證明資料（SAMPLE/SYNTHETIC 可直接使用成品）
要求編號：I05-E03
交付件 ID：0029
文件性質：策略／計畫文件；SAMPLE/SYNTHETIC 合成示範，非 REAL
SAMPLE/SYNTHETIC 示範文件｜所有真實客戶、交付、出席、成績及採用狀態均依來源標示 UNKNOWN。
一、文件用途與決策範圍
（一）文件目的
本文件把官方查核要求「訓練規劃及達到客戶課程績效目標的證明資料。」轉化為機構可執行、可閱讀、可追溯的訓練規劃與績效目標證明資料。本文件不取代訓練手冊或完整訓練成果評估報告；僅就客戶課程績效目標呈現規劃、衡量與判定之證明口徑及合成示範。核心是呈現「訓練規劃如何連結客戶課程績效目標」，並提供目標、基準、指標、公式、分工、時程、里程碑、風險、檢討與替換的完整說明。本件是策略／計畫與績效目標證據，不是訓練手冊、訓練體系圖或完整訓練成果評估報告。
（二）讀者與使用時點
本文件的主要讀者為理監事、訓練主管與執行人員。理監事可據以判斷訓練發展方向是否與客戶課程績效目標一致、是否可問責；訓練主管可據以確認需求、目標、分工、衡量與檢討是否完整；執行人員可據以確認自己的產出、欄位、時點與交付位置。使用時點包括：規劃起動時、規劃中對齊目標與分工時、規劃完成準備提交佐證時，以及每期檢討與修訂時。首頁即清楚說明目的、讀者、使用時點、操作、輸出與 SAMPLE／REAL 狀態，不使用評核工程內部術語。
（三）操作方式與輸出
操作上，由訓練主管指定各功能角色，依本文件欄位填入的目標、分子、分母、公式、來源與判定，並檢附來源或附件位置；再由指定覆核者檢查判定與理由。輸出一份可追溯的證明資料，內容包含目標與達成值、計算過程、判定、限制與替換清冊，供內部營運與外部評核閱讀。
（四）決策範圍
本文件支援的決策包括：是否啟動一個客戶課程的訓練規劃、要訂定哪些可衡量目標、誰負責何項產出、何時完成衡量、何時檢討與修訂，以及是否將合成資料替換為真實資料。本文件不支援的決策包括：真實合約條件、退費、客訴、法律責任、未登錄的外部成果，以及任何非本件要求所屬的課程體系或個人受訓事實。
（五）SAMPLE／REAL 狀態
本文件狀態為 SAMPLE/SYNTHETIC。文中所有客戶、課程、期間、人數、比例、分數、目標與結論，均為合成示範，不是機構實績，不可稱為協會實績或真實成果。凡涉及真實客戶契約、委託、核准、實際受訓、課程交付、出席、問卷、成績原始資料、客戶驗收或正式採用，本文件均無對應真實基準，全部標示 UNKNOWN。本文件不提供任何真實服務承諾，不使用任何虛構服務承諾，不創造履約、驗收、退費、客訴、契約或法律義務。
二、官方要求與適用界線
（一）官方原文與讀取狀態
官方查核佐證表第2頁「連結性」項下，項目5「訓練規劃及經營目標的連結性」之常見參考佐證資料，列有「訓練規劃及達到客戶課程績效目標的證明資料。」。本文件逐字引用該句，不改寫、不擴張、不代替鄰項文件。官方 PDF 第2頁已逐字核對；本件對應要求 I05-E03 與交付件 0029。本文件只擁有 I05-E03 的直接紀錄與分析口徑，不吞併其他要求的事實。
（二）適用界線
本文件只處理「訓練規劃及達到客戶課程績效目標的證明資料」此一直接口徑。下列事項屬於鄰項文件，本文件不代替、不合併、不複製其專屬事實：
1. 0028《訓練課程體系及訓練機構業務策略方向的相關資料_完整工作稿》（I05-E02）：處理訓練課程體系與機構業務策略方向，非本件。
2. 0030《工作經驗的相關受訓證明_可直接使用成品》（I06-E01）：處理個人工作經驗與受訓證明，非本件。
本文件不借用 0028 的課程體系或策略事實，也不借用 0030 的個人工作經驗證明內容。若需要該等事實，應回各該文件取得。
（三）負向近鄰測試
遮蔽本件標題、檔名與編號後，讀者仍可依下列專屬機制辨認本件：本文件的核心欄位為「客戶課程績效目標」「出席率」「完成率」「前後測平均與增益」「滿意度平均」，並以「客戶目標」「達成值」「判定」三欄構成追溯鏈；操作上要求把目標、分母、分子、公式、逐步計算與判定並列，且明確區分已提供目標與 UNKNOWN 目標。此組合專屬於 I05-E03 的證明資料，與 0028 的課程體系圖、0030 的個人受訓年資與證明文件不同。若把本件無修改移作 0028 或 0030，將缺少其各自必要的欄位或章節，故可拒絕至少兩個錯誤近鄰。
三、現況、需求與可驗證來源
（一）現況
本文件面對的現況是：機構需要對外說明訓練規劃如何與客戶課程績效目標連結，並提出可驗證的證明資料。目前沒有可立即引用的真實客戶契約、委託或核准紀錄，也沒有實際受訓、交付、出席、問卷或成績原始資料。因此本文件先以合成示範建立格式與計算口徑，待真實資料到位後替換。
（二）需求與來源
需求直接來自官方查核佐證表第2頁第5項。可驗證來源依優先序為：官方來源PDF的頁次紀錄、交付件對照紀錄，以及未來取得的真實客戶委託文件、課程計畫、出缺席紀錄、問卷原始回收、前後測成績與客戶驗收文件。凡未取得原件者，一律標示 UNKNOWN，不得以擬真工作稿冒充。
（三）缺 REAL 時的處理
本文件採「缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example」之原則。每一筆合成事實都登錄於文件末的「合成事實替換清冊」，記載鍵、值、類型、正文定位、真實替換原件與 REAL 狀態。任何空白不得以未完成欄位或未來式充當本文內容；真實資料缺口必須明確列為 UNKNOWN，並交代合法取得與替換步驟。
四、目標對象、價值與服務範圍
（一）目標對象
本件以「客戶課程」為對象，合成客戶代碼為 SAMPLE-CUST-01，合成課程標籤為 SAMPLE-COURSE-01，合成期間為 SAMPLE-PERIOD-01。目標對象包含：委託訓練的客戶、受訓學員、執行訓練的機構功能角色，以及核閱本文件的理監事與主管。本文件以功能角色描述分工，不指名真人；訓練主管依組織既有職掌確認責任者，正式紀錄以可追溯的職務與交付責任為準。
（二）價值
本文件提供的價值在於：把客戶課程績效目標講清楚、把衡量公式與判定講清楚、把誰負責、何時完成、如何覆核與檢討講清楚，使訓練規劃不只是課程表，而能成為可被查核、被檢討、被修訂的證明資料。對理監事而言，這是權責與方向的確認；對主管而言，這是目標與分工的根據；對執行人員而言，這是操作與交付的依據。
（三）服務範圍
服務範圍涵蓋：目標對象確認、需求與職能落差確認、課程規劃與班次安排、出席與完成追蹤、學習評量前後測、滿意度回收、證據索引與限制說明。不涵蓋真實合約義務、真實辦訓履約、退費、客訴、法律責任，以及未登錄的外部成果。正文所述執行與紀錄僅為合成流程示範，不代表實際辦訓或履約。本文件提供可執行的證明格式與合成示範，不代表真實辦訓成果。
五、策略／計畫主軸與因果關係
（一）策略主軸
本文件的策略主軸是「目標—執行—衡量—檢討」的因果鏈，說明訓練規劃如何導致客戶課程績效目標的達成。這個主軸把「訓練規劃」與「客戶課程績效目標」用可衡量的欄位連起來，使兩者不是各說各話，而是有共同的分母、分子、公式與判定。
（二）因果鏈
1. 目標設定：由客戶課程需求與機構年度營運方向，訂出可衡量目標，即出席率、完成率、後測平均、平均增益。
2. 規劃投入：依目標設計課程 SAMPLE-COURSE-01、安排班次、規劃學員遴選與評量方式。
3. 執行與紀錄：依班次執行，留下出席、完課與評量紀錄。
4. 衡量：以固定公式計算出席率、完成率、前後測平均與增益、滿意度平均。
5. 判定：把達成值與客戶示範目標比較，判定達成、超標或未達成。
6. 檢討與修訂：依判定結果決定是否調整課程、班次、評量或客戶溝通。
（三）因果假設與檢討
本件的因果假設必須被紀錄與被檢討：若目標、投入、執行、衡量任一環有落差，結論即可能改變。因此每個目標都應有對應的執行活動與證據，不可只有目標而沒有執行與證據。若某項目標未達成，應回到規劃投入與執行紀錄找原因，而非直接修改目標或數據。
因果鏈階段
規劃投入
衡量欄位
產出
目標設定
客戶需求與營運方向
四項客戶示範目標
目標值
規劃投入
課程與班次、評量設計
班次、受訓人數
班次表與規劃席次
執行與紀錄
授課、出缺席、評量、問卷
出席席次、完成人數、前後測、問卷
原始紀錄
衡量
公式計算
達成值
計算結果
判定
與目標比較
判定
達成／超標／未達成
檢討與修訂
異常排查
修訂事項
下一版規劃
六、目標、基準、指標與計算口徑
（一）已提供與未提供的目標
本文件只判定四項已提供的客戶示範目標：出席率、完成率、後測平均、平均增益。滿意度雖有計算值，但客戶示範目標未提供，保持 UNKNOWN，不判定。完成定義與個別條件未提供，保持 UNKNOWN。本文件不增列任何目標值。
（二）出席率
定義：實際出席席次除以規劃出席席次。
分子：實際出席席次 46（合成值 SYN-0029-008）。
分母：規劃出席席次 50（合成值 SYN-0029-007，由受訓學員數 10 乘以班次 5 得 10×5=50）。
公式：46/50×100 = 92%。
客戶示範目標：出席率 ≥ 85%（合成值 SYN-0029-006）。
判定：92% ≥ 85%，達成且超標。
（三）完成率
定義：達成完成狀態的學員數除以受訓學員數。
分子：達成完成狀態學員數 9（合成值 SYN-0029-010）。
分母：受訓學員數 10（合成值 SYN-0029-005）。
公式：9/10×100 = 90%。
客戶示範目標：完成率 ≥ 80%（合成值 SYN-0029-011）。
判定：90% ≥ 80%，達成且超標。
限制：「9人達成完成狀態」為給定合成彙總值；完成定義與個別條件未提供，本文件標示 UNKNOWN，不自行增補測驗門檻、時數、簽到規則等個人完成條件。
（四）前後測平均與平均增益
定義：對同一批學員於課前與課後施測，計算平均並求增益。
配對人數：9 人（合成值 SYN-0029-017）。
學員人數補充：本合成案例共 10 名受訓學員，其中 9 人完成前後測配對（SYN-0029-017）；其餘 1 人未配對的具體原因及其個別分數均為 UNKNOWN，本文不作推定。
前測：總分 558 點，平均 558/9 = 62/100（合成值 SYN-0029-018）。
後測：總分 738 點，平均 738/9 = 82/100（合成值 SYN-0029-019）。
平均增益：82 − 62 = 20 分（合成值 SYN-0029-022）。
客戶示範目標：後測平均 ≥ 80 分（合成值 SYN-0029-020）、平均增益 ≥ 10 分（合成值 SYN-0029-021）。
判定：後測平均 82 ≥ 80，達成且超標；平均增益 20 ≥ 10，達成且超標。
限制：不得編造個別分數或量表回答；本件只有彙總值。
（五）滿意度平均
定義：有效問卷分數總分除以有效回收份數，量尺為 1 至 5 整數。
量尺最大值：5（合成值 SYN-0029-013）。
有效回收份數：9（合成值 SYN-0029-014）。
總分：40 分（合成值 SYN-0029-015）。
公式：40/9 = 4.44/5，四捨五入至小數一位為 4.4/5（合成值 SYN-0029-016）。
客戶示範目標：未提供，保持 UNKNOWN，不得增列其他門檻。
判定：因目標未知，不判定達成與否，僅呈現計算值。
（六）計算口徑總表
指標
分子
分母
公式
達成值
客戶示範目標
判定
出席率
46席次
50席次
46/50×100
92%
≥85%
達成
完成率
9人
10人
9/10×100
90%
≥80%
達成
後測平均
738點
9人
738/9
82/100
≥80
達成
平均增益
82−62
—
82−62
20分
≥10
達成
前測平均
558點
9人
558/9
62/100
UNKNOWN
不判定
滿意度平均
40分
9份
40/9
4.44/5（顯示4.4/5）
UNKNOWN
不判定
判讀補充：計算口徑總表判定欄的「達成」是「達成或超標」的合併簡稱；需區分超標時，以各指標正文的判定文字為準。
（七）欄位—定義—來源—填寫者—驗證規則
欄位
定義
來源
填寫者
驗證規則
客戶課程目標
本課程要達成的可衡量目標與目標值
客戶委託文件或確認紀錄
訓練需求角色
目標值須可核算，來源可查
分子
計算達成值所用的實際數量
出缺席表、完成清冊、評量紀錄、問卷回收
各功能角色
與原始紀錄一致
分母
計算達成值所用的基準數量
課程計畫、報名或出缺席統計
各功能角色
與原始紀錄一致
公式
分子除以分母再乘以100或計算平均／增益
本文件計算口徑
評量角色
可被展示數據重算
達成值
依公式得到的結果
由分子分母計算
評量角色
四捨五入與N/A條件清楚
判定
與客戶示範目標比較的結果
目標值與達成值
訓練主管
只依已提供目標判定
來源／附件位置
佐證原件的檔名、頁碼或存放位置
合法來源原件
文件管制角色
定位可回放
期間
本次規劃與計量的範圍
訓練計畫
訓練需求角色
以 SAMPLE-PERIOD-01 代表，無日曆日期
責任角色
負責該欄位的功能角色
依各表所列功能角色
訓練主管
真人與正式分工依合法內部職務紀錄核對；SAMPLE不設定真人
狀態
SAMPLE 或 REAL
文件管制角色判定
文件管制角色
無原件不得標 REAL
七、工作分解、責任與協作
（一）工作分解
把本件拆成可交付工作項，每項有產出、責任角色、來源與驗證規則。角色以功能角色表示，不指定真人。
工作項
產出
責任角色
協作角色
驗證規則
客戶需求與目標確認
客戶課程目標四項與目標值
訓練需求角色
客戶目標對應功能角色
目標值須可核算，來源可查
課程與班次規劃
課程 SAMPLE-COURSE-01 班次表
課程設計角色
訓練行政角色
班次×學員數＝規劃席次
出席追蹤
出席紀錄與席次統計
訓練行政角色
訓練講師功能角色
分子分母可追溯
完課追蹤
完成狀態清冊
訓練行政角色
評量角色
完成定義 UNKNOWN 須揭露
前後測評量
前測／後測成績與平均
評量角色
訓練講師功能角色
配對人數一致
滿意度回收
有效問卷與總分
訓練行政角色
學員
有效份數與總分一致
判定與檢討
判定表與檢討紀錄
訓練主管
所有功能角色
判定只依已提供目標
證據索引
附件定位與版本核對
文件管制角色
訓練主管
定位可回放

（二）協作原則
各功能角色只對自己的產出負責，但必須交付可被他人驗證的來源或附件位置。跨角色交接以表單欄位為之，不以口頭或未登錄管道為之。本文件以功能角色描述流程，真實責任人維持 UNKNOWN，不留未指定的責任欄。取得正式分工原件後，依其職稱和責任界線更新索引，不得捏造人名。任何第三方正式簽章、證書或外部機構事實，須由合法來源取得可核對原件；本文件只提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。
八、資源、時程與里程碑
（一）資源
本件所需資源為：人力（各功能角色）、文件（目標、課程、出缺席、評量、問卷）、系統或表單（紀錄與計算），以及文件管制（版本、附件位置）。本文件不編列金額，不新增未登錄的經費或資源數字。
（二）時程與里程碑
本件使用合成期間 SAMPLE-PERIOD-01，不寫實際日曆日期。里程碑以階段表示：
1. 目標與需求階段：確認四項客戶示範目標與計算口徑。
2. 規劃階段：完成班次與評量設計，得出規劃席次。
3. 執行階段：執行課程並留下出席、完課、前後測、問卷紀錄。
4. 衡量階段：計算達成值與判定。
5. 檢討階段：依判定提出修訂並記錄。
6. 提交階段：整理證據索引、限制與版本核對，形成可提交的證明資料。
里程碑
交付物
完成判定
附件位置
目標與需求
目標與口徑表
四項目標與公式齊備
UNKNOWN（真實附件未提供）
規劃
班次表與評量設計
班次×人數＝規劃席次
UNKNOWN（真實附件未提供）
執行
原始紀錄
出席、完課、前後測、問卷
UNKNOWN（真實附件未提供）
衡量
計算與判定表
達成值與判定一致
UNKNOWN（真實附件未提供）
檢討
檢討與修訂紀錄
修訂事項有責任與期限
UNKNOWN（真實附件未提供）
提交
證明資料與版本核對
索引、限制、版本齊備
UNKNOWN（真實附件未提供）
九、風險、假設及應變門檻
（一）主要風險與假設
1. 目標未提供風險：客戶未明確提供四項目標時，本件無法判定，只能呈現計算值。應變：向客戶取得書面目標或確認無目標。
2. 完成定義未知風險：完成定義與個別條件未提供。假設：先以給定合成彙總值呈現，不自行增補。應變：向客戶或權責單位取得完成定義後替換。
3. 滿意度目標未知風險：目標未提供，不得增列。應變：取得目標後再判定。
4. 資料真實性風險：若以合成資料充為真實，將造成誤導。應變：全程標示 SAMPLE/SYNTHETIC，替換時須取得原件。
5. 資料缺漏風險：出席、評量或問卷缺漏時，分母可能改變。應變：明列缺漏與 N/A 條件，不以插補充數。
（二）應變門檻
本件不使用虛構的履約或驗收門檻。凡涉及目標未達、資料缺漏或定義未知，處置方式為：揭露限制、向合法來源取得原件，或維持 UNKNOWN，不自行降低或提高目標。
十、檢討頻率、決策紀錄與修訂
（一）檢討頻率
本件建議在每次課程衡量後與每期文件檢討時檢視。此為本件運作建議，非外部承諾。
（二）決策紀錄
真實檢討紀錄應包含日期、議題、證據、決議、責任角色與期限；本件真實決策紀錄為 UNKNOWN。合成判定卡（非實際會議或決議）：期間 SAMPLE-PERIOD-01；議題為四項客戶示範目標；依據為本件合成彙總與計算表；判定為四項均達成或超標（SYN-0029-023）；責任功能角色為訓練主管；真實決議與期限均為 UNKNOWN。此卡僅示範記錄口徑，不表示曾有實際會議、客戶確認或機構決策。
（三）修訂
修訂應更新合成事實替換清冊與版本核對表，確保每一版都可回放。任何時候都不得把 SAMPLE 內容改為 REAL，除非已取得可核對原件並完成替換程序。
問題／例外
修正
覆核
追蹤
完成定義未知
揭露為 UNKNOWN，不增補個人條件
訓練主管
取得權責來源後重新判定；目前 UNKNOWN
滿意度目標未知
不判定，僅呈現計算值
訓練主管
目標原件取得後再判定；目前 UNKNOWN
無真實客戶契約
不宣稱委託或核准
文件管制角色
取得委託文件後替換
無實際出席與成績
不宣稱實訓成果
文件管制角色
取得原始資料後替換
十一、完整合成示例與真實資料替換清單
（一）完整合成示例（SAMPLE/SYNTHETIC）
以下示例以前後一致的合成事實構成，客戶 SAMPLE-CUST-01、課程 SAMPLE-COURSE-01、期間 SAMPLE-PERIOD-01。
1. 受訓學員數 10 人，班次 5 場，規劃席次 10×5＝50 席次。
2. 實際出席 46 席次，出席率 46/50×100＝92%，高於客戶示範目標 85%。
3. 達成完成狀態 9 人，完成率 9/10×100＝90%，高於客戶示範目標 80%；完成定義 UNKNOWN。
4. 前後測配對 9 人，前測 558/9＝62，後測 738/9＝82，增益 20；後測平均高於 80、增益高於 10。
5. 滿意度 40/9＝4.44/5（顯示 4.4/5），目標 UNKNOWN，不判定。
6. 結論：四項已提供客戶示範目標均達成或超標；僅由合成彙總推導。
合成欄位
值
說明
客戶代碼
SAMPLE-CUST-01
合成客戶標籤；真實客戶名稱 UNKNOWN
課程標籤
SAMPLE-COURSE-01
合成課程標籤；真實課程名稱 UNKNOWN
期間標籤
SAMPLE-PERIOD-01
無日曆日期
規劃班次
5
合成
受訓學員數
10
完成率分母
規劃席次
50
10×5
實際出席席次
46
出席率分子
出席率
92%
46/50×100
達成完成人數
9
完成率分子
完成率
90%
9/10×100
前後測配對人數
9
前測後測同一批
前測總分／平均
558／62
558/9
後測總分／平均
738／82
738/9
平均增益
20
82−62
滿意度量尺
1–5
整數
有效問卷份數
9
滿意度分母
滿意度總分
40
9份加總
滿意度平均
4.44/5（4.4/5）
40/9
客戶示範目標
出席≥85%、完成≥80%、後測≥80、增益≥10
四項
判定
四項均達成／超標
滿意度不判定
（二）真實資料替換步驟
1. 確認要替換的合成鍵。
2. 從合法來源取得可核對原件，例如客戶委託文件、課程計畫、出缺席表、前後測成績、問卷原始回收、客戶驗收文件。
3. 在合成事實替換清冊中填入真實值、類型、定位與 REAL 狀態。
4. 以原件重算公式，更新判定。
5. 更新版本核對表與附件定位。
6. 未取得的項目維持 UNKNOWN，不以合成值冒充。
十二、證據索引、限制與版本核對
（一）證據索引
本件直接證據為官方來源第2頁文字，定位已明列。真實客戶與執行附件不在本件現有來源中，附件位置一律標示 UNKNOWN；依法取得原件後依替換步驟建立索引並重算，不以預留欄位表示已完成。
官方要求
表單欄位
附件定位
狀態
訓練規劃及達到客戶課程績效目標的證明資料。
目標／分子／分母／公式／判定
官方來源第2頁
已引用
出席率
46/50×100=92%
UNKNOWN；合法替換來源：出缺席表
SAMPLE計算可重算
完成率
9/10×100=90%
UNKNOWN；合法替換來源：完成清冊
SAMPLE計算可重算
後測平均
738/9=82
UNKNOWN；合法替換來源：後測紀錄
SAMPLE計算可重算
平均增益
82−62=20
UNKNOWN；合法替換來源：前測與後測紀錄
SAMPLE計算可重算
滿意度平均
40/9=4.44
UNKNOWN；合法替換來源：問卷原始回收
SAMPLE計算可重算
（二）限制
1. 本件為 SAMPLE/SYNTHETIC，非機構實績，不可稱為協會實績。
2. 沒有真實客戶契約、委託、核准、實際受訓、交付、出席、問卷、成績原始資料、客戶驗收或正式採用，全部真實基準 UNKNOWN。
3. 完成定義與個別條件、滿意度目標均未提供，保持 UNKNOWN。
4. 不得編造個別分數或量表回答。
5. 不提供服務承諾、不創造義務。

（三）版本核對
本件版本履歷：R03 內容初稿與合成資料登錄；R04 至 R07 中間修訂；R08 版面修訂；R09 文字及欄位修訂；R10 版面修訂；R11 版本履歷精簡與文字收斂；R12 修正目的、服務範圍與版本標示的一致性（work_id TTQS_ONE_0029_I05-E03_SCOPED_TEXT_REPAIR_R12_20261117）。各階段 work_id 與候選、輸入及輸出 SHA 以外部收據為準。本件供日常機構作業及評核閱讀。
十三、合成事實替換清冊（24列）
鍵
示例值
類型
正文定位
真實替換原件
REAL狀態
SYN-0029-001
SAMPLE-CUST-01
label
客戶代碼欄、案例標題
真實客戶名稱或代碼（由合法委託文件取得）
UNKNOWN
SYN-0029-002
SAMPLE-COURSE-01
label
課程標籤欄
真實課程名稱或代碼（由課程計畫取得）
UNKNOWN
SYN-0029-003
SAMPLE-PERIOD-01
label
期間欄
真實期間（由訓練計畫取得）
UNKNOWN
SYN-0029-004
5
sessions
班次規劃
真實班次（由課程計畫取得）
UNKNOWN
SYN-0029-005
10
learners
受訓學員數、完成率分母
真實受訓人數（由報名或出缺席表取得）
UNKNOWN
SYN-0029-006
85
percent
出席率目標
真實客戶出席目標（由委託或合約文件取得）
UNKNOWN
SYN-0029-007
50
seat-sessions
規劃席次（10×5）
真實規劃席次（由班次×人數計算並附來源）
UNKNOWN
SYN-0029-008
46
seat-sessions
出席率分子
真實出席席次（由出缺席表取得）
UNKNOWN
SYN-0029-009
92
percent
出席率
真實出席率（以真實分子分母重算）
UNKNOWN
SYN-0029-010
9
learners
完成率分子
真實完成人數（由完成清冊取得）
UNKNOWN
SYN-0029-011
80
percent
完成率目標
真實客戶完成目標（由委託或合約文件取得）
UNKNOWN
SYN-0029-012
90
percent
完成率
真實完成率（以真實分子分母重算）
UNKNOWN
合成事實替換清冊（續）
鍵
示例值
類型
正文定位
真實替換原件
REAL狀態
SYN-0029-013
5
points
滿意度量尺最大值
真實量表最大值（由問卷或評量設計取得）
UNKNOWN
SYN-0029-014
9
responses
有效問卷份數
真實有效份數（由問卷回收統計取得）
UNKNOWN
SYN-0029-015
40
points
滿意度總分
真實總分（由問卷原始回收加總）
UNKNOWN
SYN-0029-016
4.44
points/5
滿意度平均
真實平均（以真實總分÷真實份數重算）
UNKNOWN
SYN-0029-017
9
learners
前後測配對人數
真實配對人數（以前後測紀錄比對）
UNKNOWN
SYN-0029-018
558/62
points
前測總分與平均
真實前測成績（由評量紀錄取得）
UNKNOWN
SYN-0029-019
738/82
points
後測總分與平均
真實後測成績（由評量紀錄取得）
UNKNOWN
SYN-0029-020
80
points/100
後測平均目標
真實後測目標（由委託或合約文件取得）
UNKNOWN
SYN-0029-021
10
points
平均增益目標
真實增益目標（由委託或合約文件取得）
UNKNOWN
SYN-0029-022
20
points
平均增益
真實增益（以真實後測平均−前測平均重算）
UNKNOWN
SYN-0029-023
四項合成目標均達成或超標
decision statement
判定結論
真實判定（以真實數據重算後判定）
UNKNOWN
SYN-0029-024
SAMPLE only；無真實客戶契約等
truth boundary
全文限制宣告
真實狀態揭露（取得原件後更新）
UNKNOWN

