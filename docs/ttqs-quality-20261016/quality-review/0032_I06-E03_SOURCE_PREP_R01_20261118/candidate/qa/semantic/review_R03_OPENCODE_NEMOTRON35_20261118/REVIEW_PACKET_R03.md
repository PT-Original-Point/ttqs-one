# 0032 I06-E03 R03 exact-SHA independent semantic review

## Work envelope
- work_id: TTQS_ONE_0032_I06-E03_SEMANTIC_REVIEW_R03_NEMOTRON35_20261118
- Role: independent semantic/usability reviewer; do not edit files or make layout claims.
- Requested route: opencode/nemotron-3.5-lightning-free; provider-served model remains UNKNOWN unless your own receipt proves it.
- Stop condition: return one strict JSON object with verdict PASS/CONDITIONAL/FAIL, exact candidate SHA, exact extracted text SHA, concrete findings/locators, and limitations. Do not claim formal association acceptance.
- Candidate: 0032_I06-E03_R03_LAYOUT_FLOW_REPAIR.docx; bytes 55201; SHA-256 C0A0FB1FB346EAC6EEF2B7DE209E455185CF76CF4563C62FBCB96FCC2A9C546B
- Extracted text: EXTRACTED_TEXT_R03.txt; bytes 30162; SHA-256 50D2706E066629ABF3FB2DA7DD3434E5D92B939A66B70B07FDCB52FB615181F2
- Requirement: I06-E03, official evidence table item 6, training institution capacity to execute external training and manager planning/execution competency.
- Document status: CANDIDATE only.

## Exact evidence bindings
- Source packet SHA-256: 3540D60A59D0B11F53E45D73F25C2EDD53D8E0BCED015B39790530E902E5CED0
- Unique Blueprint SHA-256: 71CFFB64FDAE734A2DCEA333339BED77A6D15F471577EFBFDB60AD5694D80C46
- R03 scoped layout-repair receipt SHA-256: 510C820A1A1A35FA5A8EAAF0B316C67B7EF4B61CE7D1C67EDCA67CE07D3D81E4
- R03 deterministic technical QA receipt SHA-256: 2E9BE9F94B5DC02508DC68F2AD961BC53316F636755F5502FBFAAB1EE0327E0F; summary {'status': 'PASS', 'check_count': 27, 'pass_count': 27, 'failure_count': 0, 'unknown_count': 0, 'failures': [], 'unknowns': [], 'errors': []}
- R03 body text SHA-256: BADBC5E8CC0101B5CA3C84B0AA5AA7F27BCEF0ABAF357E677FC86ACB2E40E378; unchanged from R01/R02
- R03 table text SHA-256: A13FAFB79ED59D778048C8C4451069B94ED5050B52095BE1A2ADEEFB130D4756; unchanged from R01/R02
- Prior independent R02 review verdict: PASS; it was bound to candidate 0094D7D72654A072076325BD7F69237C059B87BCC248314D623CDAC074B038B2 and extracted text 78A569D2AA6B89550787D981925EDBB0C30BBC84BC053C1C98F7BE85F9DC9B7F. It is context only and does not establish this R03 review.
- R03 delta: removed four page-break-only paragraphs before sections 4, 5, 7 and 8. All text nodes, body text hash, and table text hash are unchanged. R03 text extraction paragraph indices therefore differ from R02; assess the full R03 extracted text below.
- Important limitation: Word COM visual render for R03 exceeded ten minutes, produced no PDF, and is BLOCKED. Do not pass or claim visual QA; review semantic scope only.

## Review scope
Independently assess exact R03 full extracted body against the official source packet and unique Blueprint below. Check required genre/mechanics, completeness/coherence, calculations and ratios, evaluator usability, source traceability, SAMPLE/SYNTHETIC versus REAL/UNKNOWN boundaries, absence of placeholders/blank forms, no fabricated third-party evidence, negative-neighbor boundaries for 0030/I06-E01, 0031/I06-E02, and 0033/I07-E01. If a defect exists, give a precise paragraph/table locator and minimum repair. Do not use the prior R02 review as a substitute for reading the full text. Visual layout is outside your review scope.

## Official source packet
# SOURCE_PACKET_0032_I06-E03_R01

**Stage:** `READY_SOURCE_PACKET`  
**doc_id:** `0032`  
**requirement_id:** `I06-E03`  
**正式需求名稱：** 訓練機構具備執行訓練業務相關職能的說明  
**crosswalk 文件標題：** 訓練機構具備執行訓練業務相關職能的說明_完整工作稿

## 1. 正式對照

正式 129 需求至 142 交付物 crosswalk 的對應列：

| 欄位 | 正式值 |
|---|---|
| requirement_id | I06-E03 |
| deliverable_count | 1 |
| split_extra_count | 0 |
| deliverable_ids | 0032 |
| document_titles | 訓練機構具備執行訓練業務相關職能的說明_完整工作稿 |

來源檔：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\DRIVE_READBACKS\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv`  
SHA-256: `1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679`

R04 evidence mirror `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\INPUTS\R04\04_EVIDENCE\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv` was read-only checked and has the same SHA-256.

## 2. 官方佐證資料表與頁面定位

官方來源：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\DRIVE_READBACKS\DRIVE_OFFICIAL_EVIDENCE_TABLE.pdf`  
文件名稱：附件四十六「TTQS 人才發展品質管理系統【查核佐證文件資料表】—訓練機構版」  
SHA-256: `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709`  
頁面定位：PDF 第 2 頁（頁面印刷頁碼 2），「能力」類別、第 6 項。頁面已以原始 PDF 位元組擷取文字並視覺核對。

### 第 6 項原文摘錄

> 能力  
> 6.訓練機構的行政管理能力及訓練主管相關職能  
> 展現訓練單位有適當的分工及人員有足夠的訓練相關能力以執行對外訓練業務。  
> 展現訓練部門主管具備能充分了解訓練單位發展方向訂定及執行之能力。  
> 常見參考佐證資料：  
> - 工作經驗的相關受訓證明。  
> - 專業訓練人員職能評估方法等證明。  
> - 訓練機構具備執行訓練業務相關職能的說明。  
> - 其他。

## 3. 本件來源導出的範圍

本件說明訓練機構執行對外訓練業務的組織能力，以及訓練部門主管理解發展方向、訂定並執行的能力。內容須呈現適當分工、人員訓練相關能力、能力如何支援對外訓練，以及可追溯的佐證位置。

本件是機構能力說明，不是個人工作經驗證明、職能評估方法文件或特定課程需求／設計文件。crosswalk 相鄰列確認：0030/I06-E01 是工作經驗相關受訓證明；0031/I06-E02 是專業訓練人員職能評估方法等證明；0033/I07-E01 是課程計畫配合客戶、受訓者與職能需求的證明。這些是邊界索引，不是本件內容模板。

## 4. 真實資料狀態

本次核對的正式 crosswalk 與官方佐證表沒有提供協會實際組織、人員、任職經歷、訓練紀錄、主管決策或第三方原件。以上事實均為 **UNKNOWN**，不可據此聲稱實際人員具備資格或協會已執行特定訓練。後續示例中的虛構人名、日期、數量、能力判定、課程或結果須逐項標為 **SAMPLE/SYNTHETIC** 並登錄唯一 fact_id；不得製作或暗示真實第三方證明、簽名、證書或核准。

## 5. doc_id 佔用檢查範圍

檢查範圍限定為目前工作目錄的 `E:\TTQS\docs\ttqs-quality-20261016\quality-review`。在該目錄的路徑／檔名及結構化文字 metadata 中，未找到 0032 或 I06-E03 的既有 source packet、Blueprint、candidate 或 active-owner 記錄；本次 doc_id 專屬輸出目錄建立前不存在。0031 的 Writer 階段依本次 Human 指示視為另一個作用範圍，0030 不重複使用。此檢查不對目前 quality-review 以外的 owner 狀態作推論。

## 6. 本階段界線

本包只完成來源定位與需求綁定；沒有建立 DOCX、沒有派發模型，也沒有更動 shared queue、CURRENT、dashboard 或 GitHub。



## Document-specific Blueprint
# UNIQUE_BLUEPRINT_0032_I06-E03_R01

**Stage:** `READY_UNIQUE_BLUEPRINT`  
**doc_id:** `0032`  
**requirement_id:** `I06-E03`  
**Blueprint genre:** 訓練機構對外訓練執行能力與主管職能說明  
**正式 crosswalk 標題：** 訓練機構具備執行訓練業務相關職能的說明_完整工作稿

## 1. 唯一驗收目的

以一份可供日常管理與抽查的機構能力說明，讓讀者能沿著「誰負責、需要什麼能力、如何執行對外訓練、主管如何依發展方向設定並落實工作、證據在哪裡」逐項核對。

Blueprint 依據正式 crosswalk 的 I06-E03／0032 對應及官方佐證資料表 PDF 第 2 頁、第 6 項。官方明示：訓練單位須有適當分工及足夠訓練相關能力以執行對外訓練；訓練部門主管須能理解發展方向並具訂定、執行能力。官方列出的佐證方向包括工作經驗相關受訓證明、專業訓練人員職能評估方法等證明、機構執行訓練業務相關職能說明及其他。0032 的正文重點是機構能力如何組合並運作；個人證明只作可追溯的交叉引用，不代替本件。

## 2. 成品專屬結構與 mechanics

### A. 一頁閱讀摘要

用敘述與小型責任／能力摘要回答：

- 對外訓練服務與本說明涵蓋的管理範圍。
- 主要角色如何分工，關鍵工作如何有代理或替代安排。
- 哪些能力支撐訓練業務由準備到結案的執行。
- 主管如何從發展方向訂出工作目標、安排資源並追蹤執行。
- 真實證據、UNKNOWN 項目與 SAMPLE/SYNTHETIC 示範如何區分。

真實組織資料不足時不得寫成協會現行事實；明確標出 `REAL SOURCE`、`UNKNOWN` 或 `SAMPLE/SYNTHETIC` 狀態。

### B. 角色、分工與備援矩陣

每列代表一項必要職責或經正式核實的實際職務，不用未證實人名補欄。欄位至少包括：

| 欄位 | 專屬填寫機制 |
|---|---|
| 職責／工作節點 | 訓練行政、課務協調、師資與資源協調、執行紀錄、成效資料彙整等；若僅為角色分類，標為 Blueprint 設計，實際職稱待來源核實 |
| 主責與決策權 | 說明可自行處理及須升級事項；無正式授權資料標 UNKNOWN |
| 備援安排 | 列替代角色、交接資料及啟動條件；無來源不得聲稱已有備援 |
| 所需訓練相關能力 | 說明工作所需能力，並與已證明能力分欄 |
| 能力佐證 | 引用已核實紀錄、文件名稱及頁碼；不存在時標 UNKNOWN |
| 執行產出 | 指向可檢查的流程紀錄或輸出，不以空白表格代替說明 |

矩陣後說明工作交接、同時多項任務的分派，以及主責缺席或資源不足時的決策路徑。虛構職位、人員或能力判定須標 SAMPLE/SYNTHETIC 並逐項有 fact_id。

### C. 對外訓練執行能力鏈

以流程圖或表格呈現「輸入—負責角色—控制點—輸出／留存紀錄—異常處置」：

1. 接收並界定訓練服務任務與責任邊界。
2. 確認可承接的課務、人力、師資協調及行政資源。
3. 排定責任、時程、交接及必要備援。
4. 執行訓練服務並維持可追溯的行政與過程紀錄。
5. 彙整執行與結果資料，完成交付及後續檢討。
6. 人力、師資、場地、時程或紀錄不足時，呈現暫停、調整、替補或升級分支。

每個節點須有責任角色、控制點、輸出紀錄及例外分支。沒有真實流程文件時，現況標 UNKNOWN；演練不得寫成既有制度或實際成績。

### D. 人員能力與適配檢視

對矩陣中的實際角色逐項呈現所需能力及其與對外訓練任務的關係、可接受證據種類與評估方法、結果來源定位、能力缺口、補強安排、責任人及複核點。個人受訓／經歷證明及職能評估方法文件只作交叉引用；來源未提供時標 UNKNOWN。不得創設官方通過門檻、評分公式或實際證照。

### E. 訓練主管方向設定與執行閉環

`發展方向來源 → 主管解讀 → 可檢查的工作目標 → 責任／資源配置 → 執行追蹤 → 偏差處置 → 檢討與下一輪`

每個環節列主管實際決策或產出、支持來源、執行證據及頁碼。分開「主管能力要求」與「已由真實資料證明的主管表現」。沒有策略文件、會議決議、目標、追蹤或檢討原件時標 UNKNOWN，不得代主管杜撰決議或簽核。

### F. 完整 SAMPLE/SYNTHETIC 能力演練

後續成品須以一個內部一致的演練，展示角色分派、能力覆蓋、備援、執行檢核點及異常升級如何支援對外訓練。演練要求：

- 每頁明確標 SAMPLE/SYNTHETIC，不用真實第三方名稱、證明或簽名。
- 每個虛構人員、日期、數量、時數、能力判定、結果或決策登錄唯一 fact_id。
- 示範數據可重算；容量或覆蓋率列分子、分母、fact_id 和算式。
- 比率稱為示範管理指標，不宣稱為官方 TTQS 公式或評分門檻。
- 以明確缺口處置結果結束，不用「待填」或空表收尾。

### G. 證據索引與事實狀態

文末索引列主張、來源文件／紀錄、頁碼或段落、來源性質、支持範圍及狀態：

- `REAL SOURCE`：有可定位且可核對的真實來源。
- `UNKNOWN`：本次來源未提供，尚無法確認。
- `SAMPLE/SYNTHETIC`：演練創作事實，並有唯一 fact_id。

第三方證明、真實人員身分或資格、真實訓練成果和外部核准須由可核對原件支持；無原件保持 UNKNOWN。

## 3. 範圍邊界與負向近鄰

- 0030／I06-E01 的工作經驗相關受訓證明不作本件主體。
- 0031／I06-E02 的專業訓練人員職能評估方法等證明不作本件主體；需要時只交叉引用。
- 0033／I07-E01 的客戶、受訓者與職能需求配合之課程計畫不作本件主體。
- 不以個人證照清冊、單一課程企劃、通用組織介紹或政策口號取代機構執行能力說明。
- 不把角色示例、管理指標或 SAMPLE 演練說成官方原文、協會現況或正式評核結果。

## 4. 獨立驗收條件

1. 讀者能從角色矩陣、能力鏈和主管閉環辨認本件功能。
2. 分工與備援清楚，角色要求、已證明能力及缺口沒有混為一談。
3. 執行流程有責任、控制點、紀錄輸出和異常處置。
4. 主管能力主張有真實來源定位，或標 UNKNOWN／SAMPLE/SYNTHETIC。
5. SAMPLE 數字可重算、fact_id 完整，沒有假造第三方原件、資格、核准或實績。
6. 0030、0031、0033 的功能未被本件吸收或混寫；文件不是空表或泛用標題集合。

## 5. 專屬來源綁定

- Formal crosswalk: `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\DRIVE_READBACKS\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv`
- Crosswalk SHA-256: `1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679`
- Official evidence source: `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\DRIVE_READBACKS\DRIVE_OFFICIAL_EVIDENCE_TABLE.pdf`, PDF page 2 / printed page 2 / item 6.
- Official source SHA-256: `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709`

本 Blueprint 是 0032 專用規劃，不含 peer DOCX 正文，也不構成 DOCX、外部事實或正式接受。



## Full R03 extracted candidate text
[P001] 訓練機構職能與對外訓練執行能力評核
[P002] 機構分工、人員能力、主管規劃與執行
[P003] SAMPLE/SYNTHETIC　模擬評核與改善追蹤
[P005] 使用目的
[P006] 本文件提供一套可操作的內部能力評核、證據判讀、計分、改善及複評示例。真實使用時逐項以可核對來源替換附錄所列示例值；無來源的事實維持UNKNOWN。
[P007] 外部師資身份、資格、採購原件與第三方證明均未提供或製作。資格或授權未核實時，流程必須停止；本例分數不能放行真實服務。
[P008] 官方需求定位：附件四十六《TTQS人才發展品質管理系統查核佐證文件資料表－訓練機構版》第2頁、第6項。
[P010] 一 評核結論與操作規則
[P011] 基準演練為61.25/100，低於本文件自訂的75分示例門檻；關鍵職能主責覆蓋3/5=60%，備援覆蓋2/5=40%。結論為「需改善，不得據此宣稱真實機構具備承接能力」。改善後示例複評75/100，只表示演練資料符合本文件自訂規則。
[P013] 評核步驟
[P014] 確認期間、範圍、授權、資料來源及個資界線；不清楚即標UNKNOWN。
[P015] 逐題查看可定位證據，不以口頭主張或本文件示例材料當真實證明。
[P016] 按0至4級錨點記分，寫證據、限制與理由；無證據不可推估。
[P017] 差距轉成有責任、期限、驗收條件及複評的改善行動。
[P018] 複評使用同一規則；第三方原件或真實授權未取得時仍標UNKNOWN。
[P019] 證據判讀
[P022] 二 組織分工與代理安排
[P023] 六個角色代碼及配置皆為SAMPLE/SYNTHETIC，不是真實員工名冊或核定組織圖。小型機構可兼任，但仍須有決策覆核、資料存取與缺席代理控制；真實兼任和授權須另以來源核實。
[P025] 關鍵工作覆蓋
[P027] 基準演練主責達標3/5=60%，備援2/5=40%。師資核驗與訓後追蹤主責未達基準；講師資格原件仍UNKNOWN。缺合格師資、核准或資源時，ROLE-04停止流程、ROLE-01在授權內升級；不得因容量充足而承諾服務。
[P029] 三 職能基準與能力矩陣
[P030] 0至4級是本文件的SAMPLE/SYNTHETIC內部練習尺，不是官方TTQS能力級別。示例規則要求關鍵職能主責至少3級、備援至少2級（SYN-RUBRIC-01）。
[P033] 角色能力評分
[P035] 能力分數要有工作樣本、受控紀錄、模擬操作或有效評估支持。真實人員受訓、任職與證照資料未提供時不得補造；可交叉索引正式I06-E01／I06-E02來源，未取得即UNKNOWN。
[P036] 四 對外訓練服務執行能力鏈
[P037] 本流程評估機構能否協調訓練服務，不取代客戶／市場需求分析或個別課程需求論證。每步均列責任、控制、輸出與例外。
[P039] 容量及訓後追蹤計算
[P041] 外部師資資格、採購授權或第三方契約未取得真實原件時，服務流程不得因容量足夠而放行。
[P042] 五 訓練主管規劃與執行能力
[P043] 官方第6項要求主管理解訓練單位發展方向，並具訂定與執行能力。以下方向、目標、日期及數據都是SAMPLE/SYNTHETIC（SYN-DIR-01）。
[P045] 主管評核提問
[P046] 發展方向依據哪份有效來源？版本及核准狀態為何？
[P047] 主管如何將方向轉成目標、分母、期限、責任及資源？
[P048] 師資資格或資源不足時，誰能停止服務、誰可核准替代？
[P049] 偏差如何轉成改善，誰覆核完成證據並決定複評？
[P050] 缺少策略或決議時，是否記UNKNOWN而非補寫？
[P052] 六 評核題項與證據判讀
[P053] 每題須記錄實際來源、定位、狀態及理由。下列觀察與分數皆為SAMPLE/SYNTHETIC，不是實際機構評語。
[P054] Q01 組織分工與代理
[P055] 評核問題：主要工作是否有主責、決策界線、交接與缺席備援？
[P056] 應查證據：ROLE矩陣、授權、交接、例外流程。
[P057] 示例判讀：SYN-EV-01呈現6個角色代碼和升級路徑；真實授權UNKNOWN。
[P058] 示例分數：3/4；權重15；關鍵題；Fact ID SYN-SCORE-01。
[P059] 實際評核紀錄：來源名稱／版本 ______　頁碼／欄位 ______　REAL SOURCE／UNKNOWN／SAMPLE/SYNTHETIC ______　評核理由 ______
[P060] Q02 人員能力覆蓋
[P061] 評核問題：每項關鍵職能是否有達內部基準的主責及備援？
[P062] 應查證據：能力基準、證據、主責與備援達標表。
[P063] 示例判讀：關鍵功能主責3/5=60%，備援2/5=40%；C03及C06未達。
[P064] 示例分數：2/4；權重10；關鍵題；Fact ID SYN-SCORE-01。
[P065] 實際評核紀錄：來源名稱／版本 ______　頁碼／欄位 ______　REAL SOURCE／UNKNOWN／SAMPLE/SYNTHETIC ______　評核理由 ______
[P066] Q03 師資資格與採購控制
[P067] 評核問題：是否核實資格、採購授權、利益衝突，資料不足時會停止？
[P068] 應查證據：核驗欄位、授權路徑、缺件停止條件。
[P069] 示例判讀：有模擬流程，無第三方資格原件；身份和資格UNKNOWN。
[P070] 示例分數：2/4；權重15；關鍵題；Fact ID SYN-SCORE-01。
[P071] 實際評核紀錄：來源名稱／版本 ______　頁碼／欄位 ______　REAL SOURCE／UNKNOWN／SAMPLE/SYNTHETIC ______　評核理由 ______
[P072] Q04 訓練服務完整執行鏈
[P073] 評核問題：受理、課程準備、招生、資源、交付、評估與結案是否有責任和例外處置？
[P074] 應查證據：端到端流程、控制點、紀錄與分支。
[P075] 示例判讀：SYN-FLOW-01至08連貫；模擬12人/16席/8小時。
[P076] 示例分數：3/4；權重15；關鍵題；Fact ID SYN-SCORE-01。
[P077] 實際評核紀錄：來源名稱／版本 ______　頁碼／欄位 ______　REAL SOURCE／UNKNOWN／SAMPLE/SYNTHETIC ______　評核理由 ______
[P078] 七 評核題項與證據判讀續
[P079] 每題須記錄實際來源、定位、狀態及理由。下列觀察與分數皆為SAMPLE/SYNTHETIC，不是實際機構評語。
[P080] Q05 紀錄與證據追溯
[P081] 評核問題：主張是否追到來源、版本、日期、責任、頁碼和資料狀態？
[P082] 應查證據：文件索引及缺件標記。
[P083] 示例判讀：示例索引有2筆模擬紀錄缺定位。
[P084] 示例分數：2/4；權重10；一般題；Fact ID SYN-SCORE-01。
[P085] 實際評核紀錄：來源名稱／版本 ______　頁碼／欄位 ______　REAL SOURCE／UNKNOWN／SAMPLE/SYNTHETIC ______　評核理由 ______
[P086] Q06 主管方向轉化與規劃
[P087] 評核問題：主管能否把發展方向轉成目標、責任、期限與資源？
[P088] 應查證據：方向、核准、目標、分母與責任者。
[P089] 示例判讀：SYN-DIR-01示例方向連到開課前5工作日、90%目標；真實策略UNKNOWN。
[P090] 示例分數：3/4；權重15；關鍵題；Fact ID SYN-SCORE-01。
[P091] 實際評核紀錄：來源名稱／版本 ______　頁碼／欄位 ______　REAL SOURCE／UNKNOWN／SAMPLE/SYNTHETIC ______　評核理由 ______
[P092] Q07 資源監控與異常處置
[P093] 評核問題：是否監控容量、師資、設備、時程和資料缺口並按條件停止／升級？
[P094] 應查證據：資源核對、觸發條件、決策紀錄。
[P095] 示例判讀：可算容量但基準未及早啟動備援；師資缺件須停止。
[P096] 示例分數：2/4；權重10；一般題；Fact ID SYN-SCORE-01。
[P097] 實際評核紀錄：來源名稱／版本 ______　頁碼／欄位 ______　REAL SOURCE／UNKNOWN／SAMPLE/SYNTHETIC ______　評核理由 ______
[P098] Q08 改善與複評閉環
[P099] 評核問題：差距是否有原因、措施、責任、期限、驗收及複評？
[P100] 應查證據：改善表、完成證據、複評記錄。
[P101] 示例判讀：有改善計畫但基準尚未完成複評。
[P102] 示例分數：2/4；權重10；一般題；Fact ID SYN-SCORE-01。
[P103] 實際評核紀錄：來源名稱／版本 ______　頁碼／欄位 ______　REAL SOURCE／UNKNOWN／SAMPLE/SYNTHETIC ______　評核理由 ______
[P104] 一致性與評分錨點
[P106] 證據衝突時記錄來源與範圍，採可支持的最低結論並要求澄清；示例分數不可取代真實評核。
[P107] 八 加權計分與基準判定
[P108] 公式：單題加權分=權重×級別÷4；總分為各題加權分加總。權重總和100。權重、分數與門檻均為SAMPLE/SYNTHETIC示例（SYN-RUBRIC-01）。
[P110] 計算核對：11.25+5.00+7.50+11.25+5.00+11.25+5.00+5.00=61.25/100（SYN-SCORE-01）。
[P112] 本計分尺不是TTQS官方公式、法定門檻或協會採認結果。
[P114] 九 差距改善與責任追蹤
[P115] 改善要處理實際能力缺口，不以補文件外觀代替操作能力。以下角色、期限和驗收都是SAMPLE/SYNTHETIC（SYN-ACT-01至05）。
[P117] 每次追蹤必填
[P120] 十 複評與關閉判定
[P121] 複評日期及結果為SAMPLE/SYNTHETIC（SYN-REEVAL-01）。複評沿用相同題目、權重、錨點與關鍵題，查看改善後新證據。
[P123] 複評操作
[P124] 逐題記錄前後分數、新證據名稱與定位。
[P125] 只有補文件但無實際操作，不提高分數。
[P126] 關鍵題未達或資格未核實，維持限制並指定責任人。
[P127] 關閉改善前核對責任、日期、覆核者、證據位置及剩餘UNKNOWN。
[P128] 本示例複評不表示協會或外部單位核可。
[P130] 十一 證據索引與真實性界線
[P131] 下列為模擬材料索引，並非實際原始紀錄。真實替換須列原始文件名稱、版本、日期、責任角色及印刷頁碼。
[P134] 保持UNKNOWN的資料
[P135] 真實組織圖、授權、代理、人員身份與任職經歷。
[P136] 真實受訓紀錄、職能評估原件及主管能力證明。
[P137] 發展方向、年度計畫、會議決議、資源核准及執行追蹤。
[P138] 講師身份、資格證書、採購報價、合約、利益衝突及第三方核准。
[P139] 真實學員名冊、出席、課程評價、訓後追蹤與成果。
[P140] 正式文件保存期限、個資政策與正式評核分數。
[P142] 十二 SAMPLE/SYNTHETIC替換清冊
[P143] 所有示例角色、日期、數字、能力級別、分數、證據代碼、改善決定及結果均以唯一Fact ID追溯。只可用可核對真實來源替換；不得偽造第三方原件。
[P145] 官方來源與限制
[P147] 真實替換後重新核對每個Fact ID、來源定位、分母、算式、第三方原件及資料狀態；不得沿用本示例分數。

[TABLE 01]
[T01R001] 文件識別 | 評核範圍 | 資料性質
[T01R002] 0032｜I06-E03 | 行政分工、人員訓練相關能力、訓練主管依發展方向規劃與執行。 | 全篇示例值均為SAMPLE/SYNTHETIC；不是協會實績、第三方證明、核准或正式評核結果。

[TABLE 02]
[T02R001] 面向 | 基準示例 | 複評示例 | 限制
[T02R002] 加權總分 | 61.25/100 | 75/100 | SYN-SCORE-01；非官方分數
[T02R003] 主責能力覆蓋 | 3/5=60% | 5/5=100% | SYN-COVER-01
[T02R004] 備援能力覆蓋 | 2/5=40% | 5/5=100% | SYN-COVER-01
[T02R005] 30日追蹤回收 | 7/12=58.3% | 10/12=83.3% | SYN-FOLLOW-01；模擬彙總
[T02R006] 第三方資格原件 | UNKNOWN | UNKNOWN | 不表示師資資格已核實

[TABLE 03]
[T03R001] 檢查點 | 評核員確認
[T03R002] 來源 | 產生者、日期、版本，是否為可核對來源。
[T03R003] 適用性 | 是否直接支持該題及期間。
[T03R004] 完整性 | 責任、必要欄位、分母、例外處置是否完整。
[T03R005] 可追溯 | 文件名、頁碼／欄位、責任及狀態；缺件標UNKNOWN。

[TABLE 04]
[T04R001] 角色／責任 | 工作分工 | 決策界線 | 代理與升級 | Fact ID
[T04R002] ROLE-01 / SYN-P01 / 訓練部門主管 | 理解發展方向、設定目標、配置責任與資源、處理重大例外、主持檢討。 | 課程承接與重大資源缺口在授權內決定；核准者身份UNKNOWN。 | ROLE-02代辦日常追蹤；授權事項升級。 | SYN-ROLE-01 / SYN-COMP-01
[T04R003] ROLE-02 / SYN-P02 / 訓練業務負責人 | 整合服務任務、課程計畫與時程，協調角色並追蹤準備。 | 在核准範圍內排程；範圍或資源改變回報主管。 | ROLE-03支援行政；課務決策由主管確認。 | SYN-ROLE-02 / SYN-COMP-02
[T04R004] ROLE-03 / SYN-P03 / 招生與學員行政 | 報名、通知、名冊、出席、學員服務及資料最小化。 | 依核准條件執行；資格、申訴或個資疑義升級。 | ROLE-02依清單支援，不共用帳密。 | SYN-ROLE-03 / SYN-COMP-03
[T04R005] ROLE-04 / SYN-P04 / 師資與採購程序管理 | 維護師資需求、資格核驗欄位、採購程序與利益衝突檢查。 | 資格、原件或授權未確認即停止聘任／採購。 | ROLE-05可代管資源清單，不代替資格核驗。 | SYN-ROLE-04 / SYN-COMP-04
[T04R006] ROLE-05 / SYN-P05 / 場務與教學資源管理 | 核對場地、設備、教材版本、安全及替代方案。 | 資源超出容量時暫停或提出替代方案。 | ROLE-04支援場地清單；外部資格仍由ROLE-04核驗。 | SYN-ROLE-05 / SYN-COMP-05
[T04R007] ROLE-06 / SYN-P06 / 成效資料與文件管理 | 彙整回饋、訓後追蹤、文件索引、改善狀態與複評證據。 | 只用去識別彙總；保存期限與外部原件依真實政策核實。 | ROLE-03依清單備份；分析由ROLE-06覆核。 | SYN-ROLE-06 / SYN-COMP-06/07

[TABLE 05]
[T05R001] 關鍵職能 | 主責示例 | 備援示例 | 基準判定 | Fact ID
[T05R002] 課務規劃與排程 | ROLE-02/C01=3 | ROLE-03/C01=2 | 達標 | SYN-COVER-01
[T05R003] 招生與學員行政 | ROLE-03/C02=3 | ROLE-02/C02=2 | 達標 | SYN-COVER-01
[T05R004] 師資資格與採購控制 | ROLE-04/C03=2 | 無合格備援 | 未達標 | SYN-COVER-01
[T05R005] 場地設備與教學資源 | ROLE-05/C04=3 | ROLE-04/C04=3 | 達標 | SYN-COVER-01
[T05R006] 成效評估與訓後追蹤 | ROLE-06/C06=2 | ROLE-02/C06=2 | 未達標 | SYN-COVER-01

[TABLE 06]
[T06R001] 級別 | 示例判準
[T06R002] 0 | 無可用證據或無法執行
[T06R003] 1 | 能說明概念，仍需逐步指導
[T06R004] 2 | 可依清單協助執行，紀錄或例外處理不完整
[T06R005] 3 | 可獨立依程序完成，留下可追溯紀錄並處理常見例外
[T06R006] 4 | 能穩定執行、檢查結果、改善程序並協助他人

[TABLE 07]
[T07R001] 代碼／職能 | 責任角色 | 基準 | 基準示例判讀 | 證據／Fact ID
[T07R002] C01 訓練服務規劃與課務排程 | ROLE-02 | 3 | ROLE-02=3 | SYN-EV-01 / SYN-COMP-02
[T07R003] C02 招生、學員行政與服務 | ROLE-03 | 3 | ROLE-03=3 | SYN-EV-02 / SYN-COMP-03
[T07R004] C03 師資資格查核及採購控制 | ROLE-04 | 3 | ROLE-04=2；外部資格UNKNOWN | SYN-EV-03 / SYN-COMP-04
[T07R005] C04 場地、教材、設備與替代方案 | ROLE-05 | 3 | ROLE-05=3；ROLE-04備援=3 | SYN-EV-04 / SYN-COMP-05
[T07R006] C05 文件版本、紀錄完整性與資料保護 | ROLE-03/06 | 3 | ROLE-03=2；ROLE-06=2 | SYN-EV-05 / SYN-COMP-03/06
[T07R007] C06 訓練成效彙整與訓後追蹤 | ROLE-06 | 3 | ROLE-06=2；首輪7/12=58.3% | SYN-EV-06 / SYN-COMP-07
[T07R008] C07 發展方向轉化為工作目標 | ROLE-01 | 3 | ROLE-01=3；真實方向UNKNOWN | SYN-EV-07 / SYN-COMP-01
[T07R009] C08 資源配置、執行監督及異常升級 | ROLE-01/05 | 3 | ROLE-01=2；ROLE-05=3 | SYN-EV-08 / SYN-COMP-01/05
[T07R010] C09 檢討改善與複評 | ROLE-01/06 | 3 | ROLE-01=2；ROLE-06=2 | SYN-EV-08 / SYN-COMP-01/06

[TABLE 08]
[T08R001] 角色 | 示例角色 | 示例級別 | 限制 | Fact ID
[T08R002] ROLE-01 | 訓練部門主管 | C07=3；C08=2；C09=2 | SAMPLE/SYNTHETIC；不代表實際員工能力。 | SYN-ROLE-01 / SYN-COMP-01
[T08R003] ROLE-02 | 訓練業務負責人 | C01=3；C04=3；C06=2 | SAMPLE/SYNTHETIC；不代表實際員工能力。 | SYN-ROLE-02 / SYN-COMP-02
[T08R004] ROLE-03 | 招生與學員行政 | C02=3；C05=2 | SAMPLE/SYNTHETIC；不代表實際員工能力。 | SYN-ROLE-03 / SYN-COMP-03
[T08R005] ROLE-04 | 師資與採購程序管理 | C03=2；C04=3 | SAMPLE/SYNTHETIC；不代表實際員工能力。 | SYN-ROLE-04 / SYN-COMP-04
[T08R006] ROLE-05 | 場務與教學資源管理 | C04=3；C08=3 | SAMPLE/SYNTHETIC；不代表實際員工能力。 | SYN-ROLE-05 / SYN-COMP-05
[T08R007] ROLE-06 | 成效資料與文件管理 | C05=2；C06=2；C09=2 | SAMPLE/SYNTHETIC；不代表實際員工能力。 | SYN-ROLE-06 / SYN-COMP-06/07

[TABLE 09]
[T09R001] 節點 | 負責 | 控制點 | 輸出紀錄 | 缺口處置 | Fact ID
[T09R002] 1 任務受理 | ROLE-02 | 界定服務責任與核准來源；需求分析依正式相鄰需求處理。 | 任務摘要、版本索引。 | 範圍或授權不清即回問／升級。 | SYN-FLOW-01
[T09R003] 2 課程規劃 | ROLE-02 | 覆核課程目標、時程、教材版本與資源。 | 準備表、時程、教材清單。 | 未覆核或時程衝突即暫停公告。 | SYN-FLOW-02
[T09R004] 3 師資與採購 | ROLE-04 | 核對真實資格原件、授權、利益衝突與服務條件。 | 核驗清單及原件索引；目前UNKNOWN。 | 缺件即停止聘任／採購，不付款。 | SYN-FLOW-03
[T09R005] 4 招生及學員行政 | ROLE-03 | 按核准條件登錄、通知、名冊與出席，最小化資料。 | 去識別名冊摘要、通知、出席彙總。 | 資格、容量或個資疑義即停止該項並升級。 | SYN-FLOW-04
[T09R006] 5 場地與資源 | ROLE-05 | 開課前核對容量、設備、教材、安全及替代方案。 | readiness checklist與缺口處置。 | 容量或關鍵資源不符即改期／停止。 | SYN-FLOW-05
[T09R007] 6 訓練交付 | ROLE-02/05 | 按核准安排執行，記錄版本、出席及變更。 | 執行與變更紀錄；不造簽名。 | 重大變更由主管決定並留痕。 | SYN-FLOW-06
[T09R008] 7 成效及訓後追蹤 | ROLE-06 | 彙整回饋與30日追蹤，列分母、回收、缺漏。 | 去識別摘要、追蹤表。 | 回收不足則提醒並保留未回覆數。 | SYN-FLOW-07
[T09R009] 8 結案與索引 | ROLE-06 | 核對版本、來源、日期、責任、位置及政策。 | 結案索引與改善清單。 | 缺來源或保存政策則標UNKNOWN。 | SYN-FLOW-08

[TABLE 10]
[T10R001] 指標 | 算式 | 判讀與限制
[T10R002] 容量利用 | 12名模擬學員÷16席=75%（SYN-CASE-01） | 示例容量；真實場地安全與核定容量UNKNOWN。
[T10R003] 首輪追蹤 | 7/12=58.3%（SYN-FOLLOW-01） | 示例目標80%；未回覆者保留在分母。
[T10R004] 改善後追蹤 | 10/12=83.3%（SYN-FOLLOW-01） | 第二班模擬值；不是實際成效。

[TABLE 11]
[T11R001] 管理閉環 | 示例內容 | 真實應查來源 | 示例判讀
[T11R002] 方向來源 | 提升中小企業實務訓練服務的可預測性與可追溯性 | 核准策略文件與版本。 | 模擬；真實方向UNKNOWN。
[T11R003] 主管解讀 | 轉成課務準備、角色備援、資料追溯三項工作重點。 | 主管解讀、責任分派或有效會議紀錄。 | 非實際決策。
[T11R004] 可測目標 | 模擬課程於開課前5個工作日完成 readiness packet 的比例達90% | 核准目標、期間、分母與責任。 | 非協會正式KPI。
[T11R005] 資源配置 | ROLE-02整合；ROLE-03行政；ROLE-04師資程序；ROLE-05資源；ROLE-06追蹤。 | 正式授權、資源核准及代理文件。 | 真實授權UNKNOWN。
[T11R006] 執行追蹤 | 開課前檢查師資、招生、教材、場地、索引及缺口。 | 有日期、責任、狀態與例外的紀錄。 | 基準監控有缺口。
[T11R007] 偏差處置 | 資格或授權未核實即停止；容量不足重排；回收不足啟動提醒。 | 真實事件、決策及結果。 | 流程演練；真實事件UNKNOWN。
[T11R008] 檢討複評 | A01至A05改善及同尺複評。 | 責任、期限、驗收證據與複評紀錄。 | 基準複評未完成。

[TABLE 12]
[T12R001] 級別 | 證據錨點
[T12R002] 0 | 無資料或不適用，不推定完成。
[T12R003] 1 | 只有口頭或敘述主張。
[T12R004] 2 | 部分流程／紀錄存在，但缺欄、定位或例外處理。
[T12R005] 3 | 證據完整、適用、可追溯，顯示執行與常見例外處理。
[T12R006] 4 | 除3級外，有可重複監控、複盤及改善證據。

[TABLE 13]
[T13R001] 題項 | 權重 | 級別 | 加權分 | 關鍵題 | Fact ID
[T13R002] Q01 組織分工與代理 | 15 | 3 | 11.25 | 是 | SYN-SCORE-01
[T13R003] Q02 人員能力覆蓋 | 10 | 2 | 5.00 | 是 | SYN-SCORE-01
[T13R004] Q03 師資資格與採購控制 | 15 | 2 | 7.50 | 是 | SYN-SCORE-01
[T13R005] Q04 訓練服務完整執行鏈 | 15 | 3 | 11.25 | 是 | SYN-SCORE-01
[T13R006] Q05 紀錄與證據追溯 | 10 | 2 | 5.00 | 否 | SYN-SCORE-01
[T13R007] Q06 主管方向轉化與規劃 | 15 | 3 | 11.25 | 是 | SYN-SCORE-01
[T13R008] Q07 資源監控與異常處置 | 10 | 2 | 5.00 | 否 | SYN-SCORE-01
[T13R009] Q08 改善與複評閉環 | 10 | 2 | 5.00 | 否 | SYN-SCORE-01

[TABLE 14]
[T14R001] 演練規則 | 條件 | 基準結果
[T14R002] 總分 | 至少75/100 | 61.25，未達
[T14R003] 關鍵題 | Q01、Q02、Q03、Q04、Q06均至少3級 | Q02=2、Q03=2，未達
[T14R004] 關鍵角色 | 主責3級以上且備援2級以上 | 3/5及2/5，未達
[T14R005] 結論 | 改善後須同尺複評 | 開啟A01至A05；第三方資格保持UNKNOWN。

[TABLE 15]
[T15R001] ID | 差距 | 改善措施 | 責任 | 期限 | 驗收條件 | Fact ID
[T15R002] A01 | 師資資格程序及採購控制未達基準 | 演練身份欄、資格原件狀態、授權、衝突及缺件停止；第三方原件仍UNKNOWN。 | ROLE-04；ROLE-01覆核 | 2026-07-20 | 模擬清單欄位均有狀態；缺件即停止。 | SYN-ACT-01
[T15R003] A02 | 主責／備援覆蓋3/5及2/5不足 | ROLE-02主持兩次交叉代理演練，ROLE-03/05完成交接，ROLE-06覆核索引。 | ROLE-02；ROLE-01覆核 | 2026-07-21 | 5/5主責達3級、備援達2級；留下模擬評估。 | SYN-ACT-02
[T15R004] A03 | 訓後追蹤7/12=58.3%，低於示例目標80% | ROLE-06建立30日提醒與未回覆分類，只保留去識別彙總。 | ROLE-06；ROLE-03支援 | 2026-07-23 | 第二班回收10/12=83.3%，列明未回覆3人與限制。 | SYN-ACT-03
[T15R005] A04 | 基準索引2筆模擬紀錄缺定位 | ROLE-03補來源、版本、日期、責任、頁碼／位置與狀態；不編保存年限。 | ROLE-03；ROLE-06覆核 | 2026-07-23 | 9/9筆模擬索引定位欄完整。 | SYN-ACT-04
[T15R006] A05 | 主管尚未固定檢核資源偏差 | ROLE-01設定開課前5工作日 readiness packet 目標並建立停辦／升級檢點。 | ROLE-01；ROLE-02供資料 | 2026-07-21 | 第二輪演練10筆中9筆達標=90%，另1筆有升級紀錄。 | SYN-ACT-05

[TABLE 16]
[T16R001] 欄位 | 操作規則
[T16R002] 狀態 | 未開始／進行中／待證據／已完成／逾期；由實際責任人確認。
[T16R003] 證據位置 | 文件名稱、版本、日期、頁碼／欄位及狀態；缺件標UNKNOWN。
[T16R004] 覆核者 | 由未執行該項工作者核對；自述不等於完成。
[T16R005] 逾期處置 | 記原因、服務風險、暫行控制及升級決定。
[T16R006] 關閉條件 | 先看證據和實際操作，再關閉；本表示例狀態不代表真實完成。

[TABLE 17]
[T17R001] 項目 | 模擬複評 | 判讀
[T17R002] 日期 | 2026-09-02 | 示例日期，非真實評核日期。
[T17R003] 八題級別 | 3、3、3、3、3、3、3、3 | 每題都是模擬分數。
[T17R004] 加權總分 | 75/100 | 各題3/4，總權重100。
[T17R005] 關鍵題 | Q01、Q02、Q03、Q04、Q06均3級 | 達自訂示例門檻，非官方結果。
[T17R006] 主責／備援 | 主責5/5=100%；備援5/5=100%。 | 角色及級別為演練資料。
[T17R007] 目標追蹤 | 9/10=90%。 | 模擬檢核值。
[T17R008] 訓後追蹤 | 10/12=83.3%。 | 模擬彙總值。
[T17R009] 第三方原件 | UNKNOWN | 無真實講師資格／採購原件，不得宣稱核實。

[TABLE 18]
[T18R001] 索引 | 示例材料 | 支持範圍 | 狀態／限制
[T18R002] SYN-EV-01 | 角色分工與代理演練 | 責任、決策邊界、交接與例外 | 模擬；非實際組織圖／會議紀錄
[T18R003] SYN-EV-02 | 人員能力矩陣與評核摘要 | 職能基準、示例評分、缺口與複評 | 模擬；非實際員工證明
[T18R004] SYN-EV-03 | 師資採購核驗流程清單 | 資格、授權、衝突及停止點 | 模擬；沒有供應商資料或第三方原件
[T18R005] SYN-EV-04 | 課程準備與資源readiness摘要 | 排程、場地、教材、設備及容量 | 模擬；非實際課程紀錄
[T18R006] SYN-EV-05 | 文件索引示範 | 來源、版本、日期、責任、定位 | 模擬；不代表真實保存政策
[T18R007] SYN-EV-06 | 課後回饋及30日追蹤彙總 | 分母、回收率、限制及改善觸發 | 模擬；無學員個資
[T18R008] SYN-EV-07 | 方向至目標的主管規劃鏈 | 方向、目標、資源、追蹤與檢討 | 模擬；非真實策略核定或簽核
[T18R009] SYN-EV-08 | 改善與複評索引 | 責任、期限、驗收及複評結果 | 模擬；非正式評核結果

[TABLE 19]
[T19R001] 官方來源 | 定位 | 支持範圍
[T19R002] TTQS查核佐證文件資料表－訓練機構版 | 附件四十六，PDF第2頁／印刷頁碼2，第6項 | 適當分工、人員對外訓練能力、主管理解方向及訂定執行能力。
[T19R003] 正式129需求至142交付物crosswalk | I06-E03→0032 | 只證明需求映射，不證明組織能力。

[TABLE 20]
[T20R001] Fact ID | 示例值／範圍 | 真實替換要求
[T20R002] SYN-CASE-01 | SAMPLE/SYNTHETIC：案例、課程日期2026-06-15及2026-08-01、追蹤日期2026-07-15及2026-08-31、12名模擬學員、16席、8小時。 | 以核實的真實服務記錄、日期、名額與時數替換。
[T20R003] SYN-DIR-01 | SAMPLE/SYNTHETIC：模擬發展方向、開課前5工作日及90% readiness目標。 | 以核准策略、目標、主管決議與分母定義替換；未核准標UNKNOWN。
[T20R004] SYN-ORG-01 | SAMPLE/SYNTHETIC：六個示例角色代碼ROLE-01至ROLE-06及主責／代理安排。 | 以組織文件、授權與代理記錄替換；未核實身份維持UNKNOWN。
[T20R005] SYN-ROLE-01 | SAMPLE/SYNTHETIC：ROLE-01主管角色、職責、決策與代理。 | 以真實職務說明、授權和覆核證據替換。
[T20R006] SYN-ROLE-02 | SAMPLE/SYNTHETIC：ROLE-02訓練業務負責人職責與代理。 | 以真實分工及交接紀錄替換。
[T20R007] SYN-ROLE-03 | SAMPLE/SYNTHETIC：ROLE-03招生學員行政職責。 | 以真實流程替換，避免不必要個資。
[T20R008] SYN-ROLE-04 | SAMPLE/SYNTHETIC：ROLE-04師資與採購管理職責。 | 以真實程序替換；第三方證照、報價、契約與核准須原件，無則UNKNOWN。
[T20R009] SYN-ROLE-05 | SAMPLE/SYNTHETIC：ROLE-05場務及資源管理職責。 | 以真實場地、設備及備援紀錄替換。
[T20R010] SYN-ROLE-06 | SAMPLE/SYNTHETIC：ROLE-06成效資料與文件管理職責。 | 以真實資料治理和追蹤證據替換；保存期限需政策來源。
[T20R011] SYN-COMP-01 | SAMPLE/SYNTHETIC：主管C07=3、C08=2、C09=2。 | 以真實職能基準及可定位評估證據替換。
[T20R012] SYN-COMP-02 | SAMPLE/SYNTHETIC：業務負責人C01=3、C04=3、C06=2。 | 以真實評估證據替換。
[T20R013] SYN-COMP-03 | SAMPLE/SYNTHETIC：學員行政C02=3、C05=2。 | 以真實評估證據替換。
[T20R014] SYN-COMP-04 | SAMPLE/SYNTHETIC：師資採購C03=2、C04=3。 | 以真實內部流程能力證據替換；不造第三方原件。
[T20R015] SYN-COMP-05 | SAMPLE/SYNTHETIC：場務資源C04=3、C08=3。 | 以真實資源和異常處理證據替換。
[T20R016] SYN-COMP-06 | SAMPLE/SYNTHETIC：資料文件C05=2、C09=2。 | 以真實索引、版本和改善證據替換。
[T20R017] SYN-COMP-07 | SAMPLE/SYNTHETIC：訓後追蹤C06=2。 | 以真實去識別追蹤證據替換。
[T20R018] SYN-COVER-01 | SAMPLE/SYNTHETIC：5項關鍵職能；主責3/5=60%、備援2/5=40%；複評主責及備援各5/5=100%。 | 以核實職能清單和實際評級重算，不沿用示例分子分母。
[T20R019] SYN-FOLLOW-01 | SAMPLE/SYNTHETIC：首輪7/12=58.3%，示例目標80%；改善後10/12=83.3%。 | 以真實去識別追蹤分子分母、日期及回收紀錄替換。
[T20R020] SYN-RUBRIC-01 | SAMPLE/SYNTHETIC：0至4級錨點、8題權重15/10/15/15/10/15/10/10、總分75門檻及關鍵題至少3級。 | 本文件自訂示例規則，不是TTQS官方公式或標準；正式採用前需有權者核定。
[T20R021] SYN-SCORE-01 | SAMPLE/SYNTHETIC：基準分數3/2/2/3/2/3/2/2及加權61.25/100。 | 由評核員按真實證據重評與重算。
[T20R022] SYN-ACT-01至05 | SAMPLE/SYNTHETIC：五項改善責任角色、日期2026-07-20至2026-07-23、驗收數字及操作結果。 | 以實際責任、期限、證據及覆核結果替換。
[T20R023] SYN-REEVAL-01 | SAMPLE/SYNTHETIC：2026-09-02複評、8題各3級、75/100、覆蓋各5/5、readiness 9/10、追蹤10/12。 | 使用同一有效規則和真實改善證據複評；未知第三方資料仍UNKNOWN。
[T20R024] SYN-FLOW-01至08 | SAMPLE/SYNTHETIC：八個服務節點的責任、控制、輸出及例外流程。 | 以真實程序及記錄定位替換。
[T20R025] SYN-EV-01至08 | SAMPLE/SYNTHETIC：八筆模擬證據索引與其支持範圍。 | 以真實原件索引替換；本文件不製作簽名、資格、核准或第三方證明。

[TABLE 21]
[T21R001] 來源性質 | 內容 | 限制
[T21R002] 正式crosswalk | I06-E03對應0032，需求為訓練機構執行訓練業務相關職能說明。 | 需求映射不證明真實組織能力。
[T21R003] 官方佐證表 | PDF第2頁第6項：適當分工、人員能力及主管理解方向、訂定與執行能力。 | 不提供本文件的自訂權重、評分尺或通過門檻。

