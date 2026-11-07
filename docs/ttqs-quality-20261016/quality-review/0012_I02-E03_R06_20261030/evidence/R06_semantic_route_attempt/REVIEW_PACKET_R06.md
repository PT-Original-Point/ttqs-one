# 0012 / I02-E03 R06 獨立語意差異審查包

R06 candidate DOCX SHA-256: f4c7a8242cb5ae0c4c038d546b2d45cac938028a521ea6ffcb5cc02334c03d13

R05 baseline DOCX SHA-256: a90340289d360a7705fad8137db3a33b648a126ca67b1454d66c0b9288f9d9b5

審查範圍：僅針對 R05 已獨立語意 PASS 但有明示 Finding 的修補差異，以及這些差異在 R06 的定位與一致性；其餘未改正文只有在差異證據支持時才可沿用 R05 範圍。請明確判定能否沿用，不能則標 PARTIAL，不得自行擴大成全文件 PASS。

## 官方要求與唯一 Blueprint 對照
{
  "document_id": "0012",
  "requirement_id": "I02-E03",
  "official_checkbox_text": "補助參與機構公開招生課程或進階課程優惠辦法之規定。",
  "official_requirement_text": "補助參與機構公開招生課程或進階課程優惠辦法之規定。",
  "official_evidence_table_page": "1",
  "official_source_readback_status": "PDF_TEXT_EXACT_PAGE_MATCH",
  "official_requirement_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
  "unique_blueprint_row_sha256": "0ebf302b8b3601be6c645573e9e12887242c8e64a2244d5cf738a35ee2f5fc04",
  "blueprint_file_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
  "negative_neighbors": [
    "0011 / I02-E02",
    "0013 / I02-E04"
  ],
  "unique_blueprint_row": {
    "document_genre": "專屬佐證紀錄｜補助參與機構公開招生課程或進階課程優惠辦法之_制度文件",
    "document_purpose": "本件專屬焦點：補助參與機構公開招生課程或進階課程優惠辦法之_制度文件；需直接回應的官方佐證要求為：補助參與機構公開招生課程或進階課程優惠辦法之規定。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。",
    "evidence_role": "保存此項要求專屬的原始紀錄或證據索引；不代替第三方原件。 本文件只擁有 I02-E03 的直接紀錄／分析口徑；不得吞併其他要求的事實。",
    "required_sections": "紀錄目的、責任及適用界線；官方要求拆解與證明路徑；來源、形成時點及納入規則；欄位定義及證據位置；完整合成紀錄示例；核對、計算與一致性判定；例外、缺證及更正軌跡；真實原件與合成示例的區別；覆核、保管及調閱規則；相關要求及文件交叉引用；真實資料替換清單；附件索引與版本",
    "required_tables_or_figures": "欄位—定義—來源—填寫者—驗證規則；完整合成填寫列及欄位解說；問題／例外—修正—覆核及追蹤；官方要求—表單欄位—附件定位追溯表",
    "required_fields_or_questions": "合成資料識別碼；日期欄位及合成標示；責任角色代碼；來源／附件位置欄位；判定、理由、覆核及後續行動",
    "required_calculations_or_analysis": "若此表單有數量、金額、期間或比例，明列定義、分子分母與逐步算例；若沒有，明示不適用並提供至少一個欄位驗證／完整度判斷示例。",
    "required_cross_references": "同要求分件 無；相鄰要求 I02-E02, I02-E04；共用原始來源時只引用核實結果，不複製別份文件正文。",
    "real_data_required": "升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。",
    "third_party_evidence_required": "若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。",
    "prohibited_fabrication": "不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。",
    "title_blind_test": "遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『補助參與機構公開招生課程或進階課程優惠辦法之_制度文件』並證明『補助參與機構公開招生課程或進階課程優惠辦法之規定。』；若可無修改移作其他要求即失敗。",
    "negative_choice_neighbors": "0011《與訓練政策有關之訓練產品與市場定位_制度文件》（I02-E02）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0013《公開公布訓練機構年度訓練課程_完整工作稿》（I02-E04）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。",
    "acceptance_tests": "移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『補助參與機構公開招生課程或進階課程優惠辦法之_制度文件』，且能指出直接回應『補助參與機構公開招生課程或進階課程優惠辦法之規定。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。"
  }
}

## R05 既有獨立審查原始回覆
# 獨立語意／可用性審查 — 0012 / I02-E03

**審查邊界聲明**：僅審閱本 packet 內文；未讀取檔案、未執行工具、未瀏覽、未目視檢查任何頁面。所有結論僅綁定本 packet 所述 candidate DOCX SHA-256 `a90340289d360a7705fad8137db3a33b648a126ca67b1454d66c0b9288f9d9b5`。Receipts 僅作背景脈絡，不作為語意證據。

## 總體判定：**PASS**（獨立語意審查層級）

- document_id：**0012**
- requirement_id：**I02-E03**
- 藝術狀態：CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED（與文內首頁聲明一致）

## 各面向查核

| 查核項 | 結果 | 依據 |
|---|---|---|
| 官方要求回應／文類機制 | PASS | §1.1 逐字引官方原文；制度文件文類具備角色（§4）、輸入、判斷控制點（§2、§5 步驟4/6/7）、異常（§5 HOLD、§6）、輸出（§5 步驟7/8、§10.1） |
| Unique Blueprint 職責 | PASS | 12 節 required sections 全部有對應正文；required tables 4 項實質到位（T6/F7 欄位驗證、T7-8 示例與例外覆核、T11 追溯表）；required fields 五類齊備（S12-EX-001、SAMPLE 日期、S-*角色碼、S-ATT 索引、判定/理由/覆核/後續） |
| 作業可用性 | PASS | §5 十步流程可直接執行；§9.3 完整度判定示例實用；首頁 30 秒說明含目的、讀者、SAMPLE 狀態 |
| 算術／內部一致性 | PASS | T9 逐列重算通過：E=max(0,6000−0−0)=6000；6000×20%=1200；B=min(1200,1500,4000,7000,6000)=1200；應付 4800；餘額 7000−1200=5800。案例日期順序一致（申請 11-02 < 截止 11-10 < 課程 12-04）；HOLD 終態在首頁、T7、T8、§10.1、§12 全域一致 |
| SAMPLE/SYNTHETIC vs REAL 邊界 | **PASS（最強項）** | 42 項合成事實全部登錄 §12/T12 且附替換路徑與責任角色；三個 S-ATT 索引明示無實體檔；身分、預算、公告原件誠實標 UNKNOWN/HOLD（T7 六列）；無任何把示例升格為真實的措辭 |
| 虛構核准／第三方事實 | PASS | T8 第三列明示「無核定角色、不捏造簽名、核准日或決議」；T4 SAMPLE 註記真人聲明不存在；全稿無簽章、無機構實績宣稱 |
| 標題盲測 | PASS | §11 標題盲辨段列出足夠專屬機制（參與身分、費率/上限、折抵算式、利益衝突、申復、課後對帳），不可無修改移作 0011 或 0013 |
| 負向鄰項區隔 | PASS | §1.3 與 §11 雙重排除 0011（市場定位：本稿無市場調查）與 0013（年度課程清單：本稿無年度總表），並指出可核對差異章節 |

## 發現（findings）

| # | 定位 | 嚴重度 | 內容 |
|---|---|---|---|
| F1 | §5 步驟1–10 對照 SYN-037／SYN-038／SYN-039 | **MEDIUM** | 登錄簿聲稱「形式檢查 3 個工作日、資格審查 5 個工作日、通知 2 個工作日、補件 5 個工作日」位於第 5 節，但萃取正文的 §5 十個步驟中未出現任何具體天數；§5 導言「下列天數均在第 12 節列為 SAMPLE 參數」暗示天數應在該節可見。三列登錄的文內定位目前不可由正文核對。屬追溯性瑕疵，非邊界或算術瑕疵；建議升 CURRENT 前在 §5 導言補列天數或改登錄定位。 |
| F2 | SYN-022 vs T9 | LOW | 登錄簿稱「示例**牌庫**額度」而正文 T9 為「示例**額度總額**」，名稱不一致且「牌庫」非制度文件常用語；值 12,000 一致。建議統一措辭以利評核閱讀。 |
| F3 | T6 欄位結構 vs Blueprint required table | LOW | 「欄位—定義—來源—填寫者—驗證規則」未以逐欄形式呈現：來源與填寫者資訊併入「填寫／驗證規則」與「REAL替換必取證據」欄。實質覆蓋到位，schema 未逐字對齊。 |
| F4 | §13 | LOW | 文末含「Blueprint row SHA-256」等評核工程術語；首頁 30 秒說明無此問題，僅尾端溯源段。 |

## UNKNOWN／HOLD 事項（不發明、不補作）

- 官方佐證表之**出版版次／發布日期**：packet 內無此資訊 → **UNKNOWN**。要求原文的身分由 packet 所錄來源 SHA 與頁次 1 及 PDF_TEXT_EXACT_PAGE_MATCH 狀態支持；版次中繼資料不在本審查可核對範圍。
- 真實參與身分、課程公告/分類/價目原件、真實預算、法定期限、個資保存年限：正文均已正確標 UNKNOWN/HOLD（T7、T8、SYN-032/033/034/040/041），與「缺真實資料即 HOLD 不得核准」的設計一致。
- 字體下限（10.5pt／9.5pt）與版面：屬視覺／技術範疇，receipts 僅為脈絡，**本審查未目視、不予認證**，維持該 receipt 原標示之 PENDING/PASS_LAYOUT_ONLY 狀態不變。

## 效力聲明

- 本審查為語意／可用性層級 PASS，不含視覺複核、法律審查、協會核定或正式接受。
- FORMAL_ACCEPTANCE：**NOT_GRANTED**。

## R06 §5（期限修補定位）
5. 標準作業流程

本節時限是建議服務標準，必須經核定並先行公告；下列天數均在第 12 節列為 SAMPLE 參數。法定期限或正式公告另有要求時，以核實後的規定為準。

## R06 §12（完整示例及合成事實清冊）
12. SYNTHETIC replacement register｜逐事實替換清冊

本表每列只登錄合成值或 SAMPLE 制度參數。欄位中的 S-ATT-* 是虛構索引碼，沒有隨稿附上原始附件。REAL替換時須取得該列所列原件、正式資料或權責核定，重新計算並重做覆核；不可只把名稱改成真人或把示例狀態改為核准。

[TABLE]
ID | 合成事實／參數及值 | 文內定位 | REAL替換所需原件／查核路徑 | 責任角色與替換控制
SYN-001 | 機構名稱「晨星社區學習協會」為虛構 | 第 7、8 節 | 機構正式登記資料及正式參與名冊 | 資格審查人核對版本、識別碼與有效期
SYN-002 | 機構識別碼 S-ORG-01 | 第 7、12 節 | 正式機構識別資料 | 承辦不得自行編造或沿用樣例碼
SYN-003 | 案件編號 S12-EX-001 | 第 7–10 節 | 正式系統唯一案件編號及原始時間戳 | 承辦以系統生成值取代
SYN-004 | 申請窗口角色 S-APP-01；無真人姓名及聯絡方式 | 第 7 節 | 機構授權文件及必要聯絡資料 | 承辦驗授權；受限存取聯絡資料
SYN-005 | 提名人代碼 S-LEARNER-01 | 第 7 節 | 合法且最少必要的身分／機構關係來源 | 資格審查人核實；不得從案例推定
SYN-006 | 申請日 2026-11-02 | 第 7、8 節 | 正式收件系統不可修改時間戳 | 承辦記錄時區並保存原始日誌
SYN-007 | 課程代碼 S-ADV-01 | 第 7–9 節 | 核定課程目錄中的正式課程代碼與版本 | 課程窗口核對公告一致性
SYN-008 | 課程名稱「進階服務設計工作坊」 | 第 7–9 節 | 正式課程公告及核定名稱 | 課程窗口逐字核對，不以樣例名稱代替
SYN-009 | 課程類別「進階課程」 | 第 7–9 節 | 有權核定的類別定義及課程目錄列 | 資格審查人留存分類依據
SYN-010 | 預定課程日 2026-12-04 | 第 7、8 節 | 正式課程日程、異動與開課紀錄 | 課程窗口以最新公告讀回
SYN-011 | 公告截止日 2026-11-10 | 第 7 節 | 已發布公告版本及發布時間戳 | 承辦保存公告快照，不事後改期
SYN-012 | S-ATT-01 為虛構課程公告索引，無實體檔 | 第 7、8 節 | 正式公告原始檔／頁面及版本 | 承辦記錄實際來源URL或檔案位置、讀取日
SYN-013 | S-ATT-02 為虛構身分附件索引，無實體檔 | 第 7、8 節 | 正式參與身分及授權原件 | 資格審查人從授權保管來源核實
SYN-014 | S-ATT-03 為虛構價目附件索引，無實體檔 | 第 7、8 節 | 正式價目、收費條件及有效日期 | 計算人保存原始頁面／文件及版本
SYN-015 | 申請理由「希望提升機構服務流程設計能力」為合成文字 | 第 7 節 | 真實訓練需求、提名理由及其合法來源 | 資格審查人不得將示例理由當成機構需求
SYN-016 | 公告學費 F = NTD 6,000 | 第 7–9 節 | 核定價目及適用該期課程的收費來源 | 計算人讀原件，覆核人獨立取值
SYN-017 | 其他支持 O = NTD 0 | 第 7–9 節 | 申請人聲明及可查核的其他支持／帳務紀錄 | 資格審查與財務交叉核對
SYN-018 | 排除費用 X = NTD 0 | 第 9 節 | 核定費用範圍及課程價目明細 | 權責核定適用項目；計算人重算
SYN-019 | 進階課程示例費率 r = 20% | 第 8、9、12 節 | 有權核定的正式參數表及公告版本 | 權責角色核定；不得引用本樣稿數值
SYN-020 | 個人示例上限 C₁ = NTD 1,500 | 第 8、9 節 | 正式個人上限及使用紀錄台帳 | 財務讀取已承諾／已使用額，覆核人重算
SYN-021 | 機構示例剩餘上限 C₂ = NTD 4,000 | 第 8、9 節 | 正式機構上限及承諾／使用台帳 | 財務按適用期間重讀，不沿用示例餘額
SYN-022 | 示例額度總額 = NTD 12,000 | 第 8、9 節 | 真實預算核定文件及可用科目 | 有權預算角色與財務共同核實
SYN-023 | 此前示例承諾額 = NTD 5,000 | 第 8、9 節 | 有效承諾台帳與逐案核定紀錄 | 財務核對承諾範圍及截點
SYN-024 | 示例可用額 C₃ = NTD 7,000 | 第 9 節 | 由核定額度減正式承諾額重新計算 | 不直接替換結果；依原始台帳重算
SYN-025 | 合格費用 E = NTD 6,000 | 第 9 節 | F、O、X 的正式來源及核定規則 | 計算人與覆核人分別重算
SYN-026 | 未封頂金額 NTD 1,200（6,000 × 20%） | 第 9 節 | 正式費用與核定費率 | 計算人留式，覆核人獨立驗算
SYN-027 | 最終示例優惠 B = NTD 1,200 | 第 8、9 節 | 全部上限、可用餘額、核定及其他支持來源 | 只有正式核定後才能成為可執行金額
SYN-028 | 示例應付學費 NTD 4,800 | 第 9 節 | 正式費用、正式核定折抵及收費紀錄 | 財務依核定結果對帳；不可依本算例收款
SYN-029 | 假設折抵後餘額 NTD 5,800 | 第 9 節 | 正式可用額與正式折抵承諾帳 | 重新計算；不得記為實際預算餘額
SYN-030 | 審查角色 S-REV-02 及「無已知關係」聲明均為虛構 | 第 4、8 節 | 真實審查人名冊、逐案聲明、主管迴避決定 | 每位 REAL 審查人逐案簽認並保留覆核
SYN-031 | 受理角色 S-ADM-01 | 第 8 節 | 正式值勤／派案紀錄 | 承辦主管核對實際派案及權限
SYN-032 | 申請機構之實際參與身分 UNKNOWN | 第 8 節 | 官方或經授權的現行參與名冊／文件 | 原件可重讀並記錄定位後方可判斷
SYN-033 | 課程公告、正式分類及價目原件均未提供 | 第 7、8 節 | 課程主責單位的正式公告、分類及價目 | 不得以 S-ATT 索引宣稱原件存在
SYN-034 | 真實預算、其他支持及可用餘額均 UNKNOWN | 第 8、9 節 | 核定預算、財務台帳、其他支持來源 | 財務與獨立覆核人讀取同一截點
SYN-035 | 案例最終判定 HOLD；未核准、未折抵、未支付、未保留名額 | 第 8、10 節 | 有權人員依正式規範與原始證據作成的真實書面決定 | 不得把樣例判定改寫為協會決定
SYN-036 | SAMPLE狀態變更日 2026-11-02、2026-11-03 | 第 8 節 | 真實系統時間戳、審查紀錄及可追溯事件 | 示例日期不作真實時間線
SYN-037 | 建議補件期限 5 個工作日 | 第 5、6 節 | 核定辦法、公告及適用法規 | 權責核定並先公告後適用
SYN-038 | 建議承辦形式檢查 3 個工作日、資格審查 5 個工作日 | 第 5 節 | 核定服務標準及合法期限核驗 | 權責核定；法定期限優先
SYN-039 | 建議通知 2 個工作日內完成 | 第 5 節 | 核定服務標準及送達程序 | 權責核定並保留送達證據
SYN-040 | 建議申復及回覆期限各 10 個工作日 | 第 10 節 | 現行法規及核定申復程序 | 法務核驗後再公告；不可宣稱法定權利期限
SYN-041 | 建議逐案課後對帳期限及報告頻率尚未設定 | 第 10 節 | 核定辦法、帳務及課程管理程序 | 由權責單位核定並登錄正式版本
SYN-042 | 本文版本 S0.1、狀態為草案且無生效日 | 封面、文末 | 正式文管系統版本及權責核定／公告紀錄 | 未核定前維持草案，不建立生效日期
[/TABLE]

## R06 §13（控制資料與接受狀態）
13. 版本、保管及附件索引

文件識別：0012／I02-E03；草案版次 S0.1。

草擬日期：2026-10-29（本次文字草稿製作日，不是制度生效日）。

文件狀態：SAMPLE／SYNTHETIC；法規、權責、參數、預算與資料治理待核。

官方需求定位：TTQS 訓練機構版查核佐證文件資料表第 1 頁；本案唯一 Blueprint 的列位與來源版本記錄於受控文件管理側錄。

官方佐證 PDF：TTQS查核佐證文件資料表-訓練機構版 (2).pdf；本機來源 SHA-256 為 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709。

本稿沒有附課程公告、參與名冊、價目、預算、法規意見、簽章或核准原件；S-ATT-01至S-ATT-03都是虛構索引。

REAL替換後應另建正式版次與完整附件目錄，記錄原件檔名、來源、版本、頁次、取得日期、雜湊、存取權限及覆核者；不得覆寫或刪除本 SAMPLE 草稿。

本稿的檢查紀錄與適用範圍以各自收據為準；不構成法規審查、協會核准或正式接受。不得標示為 REAL 或生效辦法。

## R06 synthetic replacement register（完整）
ID,合成事實／參數及值,文內定位,REAL替換所需原件／查核路徑,責任角色與替換控制
SYN-001,機構名稱「晨星社區學習協會」為虛構,第 7、8 節,機構正式登記資料及正式參與名冊,資格審查人核對版本、識別碼與有效期
SYN-002,機構識別碼 S-ORG-01,第 7、12 節,正式機構識別資料,承辦不得自行編造或沿用樣例碼
SYN-003,案件編號 S12-EX-001,第 7–10 節,正式系統唯一案件編號及原始時間戳,承辦以系統生成值取代
SYN-004,申請窗口角色 S-APP-01；無真人姓名及聯絡方式,第 7 節,機構授權文件及必要聯絡資料,承辦驗授權；受限存取聯絡資料
SYN-005,提名人代碼 S-LEARNER-01,第 7 節,合法且最少必要的身分／機構關係來源,資格審查人核實；不得從案例推定
SYN-006,申請日 2026-11-02,第 7、8 節,正式收件系統不可修改時間戳,承辦記錄時區並保存原始日誌
SYN-007,課程代碼 S-ADV-01,第 7–9 節,核定課程目錄中的正式課程代碼與版本,課程窗口核對公告一致性
SYN-008,課程名稱「進階服務設計工作坊」,第 7–9 節,正式課程公告及核定名稱,課程窗口逐字核對，不以樣例名稱代替
SYN-009,課程類別「進階課程」,第 7–9 節,有權核定的類別定義及課程目錄列,資格審查人留存分類依據
SYN-010,預定課程日 2026-12-04,第 7、8 節,正式課程日程、異動與開課紀錄,課程窗口以最新公告讀回
SYN-011,公告截止日 2026-11-10,第 7 節,已發布公告版本及發布時間戳,承辦保存公告快照，不事後改期
SYN-012,S-ATT-01 為虛構課程公告索引，無實體檔,第 7、8 節,正式公告原始檔／頁面及版本,承辦記錄實際來源URL或檔案位置、讀取日
SYN-013,S-ATT-02 為虛構身分附件索引，無實體檔,第 7、8 節,正式參與身分及授權原件,資格審查人從授權保管來源核實
SYN-014,S-ATT-03 為虛構價目附件索引，無實體檔,第 7、8 節,正式價目、收費條件及有效日期,計算人保存原始頁面／文件及版本
SYN-015,申請理由「希望提升機構服務流程設計能力」為合成文字,第 7 節,真實訓練需求、提名理由及其合法來源,資格審查人不得將示例理由當成機構需求
SYN-016,"公告學費 F = NTD 6,000",第 7–9 節,核定價目及適用該期課程的收費來源,計算人讀原件，覆核人獨立取值
SYN-017,其他支持 O = NTD 0,第 7–9 節,申請人聲明及可查核的其他支持／帳務紀錄,資格審查與財務交叉核對
SYN-018,排除費用 X = NTD 0,第 9 節,核定費用範圍及課程價目明細,權責核定適用項目；計算人重算
SYN-019,進階課程示例費率 r = 20%,第 8、9、12 節,有權核定的正式參數表及公告版本,權責角色核定；不得引用本樣稿數值
SYN-020,"個人示例上限 C₁ = NTD 1,500",第 8、9 節,正式個人上限及使用紀錄台帳,財務讀取已承諾／已使用額，覆核人重算
SYN-021,"機構示例剩餘上限 C₂ = NTD 4,000",第 8、9 節,正式機構上限及承諾／使用台帳,財務按適用期間重讀，不沿用示例餘額
SYN-022,"示例額度總額 = NTD 12,000",第 8、9 節,真實預算核定文件及可用科目,有權預算角色與財務共同核實
SYN-023,"此前示例承諾額 = NTD 5,000",第 8、9 節,有效承諾台帳與逐案核定紀錄,財務核對承諾範圍及截點
SYN-024,"示例可用額 C₃ = NTD 7,000",第 9 節,由核定額度減正式承諾額重新計算,不直接替換結果；依原始台帳重算
SYN-025,"合格費用 E = NTD 6,000",第 9 節,F、O、X 的正式來源及核定規則,計算人與覆核人分別重算
SYN-026,"未封頂金額 NTD 1,200（6,000 × 20%）",第 9 節,正式費用與核定費率,計算人留式，覆核人獨立驗算
SYN-027,"最終示例優惠 B = NTD 1,200",第 8、9 節,全部上限、可用餘額、核定及其他支持來源,只有正式核定後才能成為可執行金額
SYN-028,"示例應付學費 NTD 4,800",第 9 節,正式費用、正式核定折抵及收費紀錄,財務依核定結果對帳；不可依本算例收款
SYN-029,"假設折抵後餘額 NTD 5,800",第 9 節,正式可用額與正式折抵承諾帳,重新計算；不得記為實際預算餘額
SYN-030,審查角色 S-REV-02 及「無已知關係」聲明均為虛構,第 4、8 節,真實審查人名冊、逐案聲明、主管迴避決定,每位 REAL 審查人逐案簽認並保留覆核
SYN-031,受理角色 S-ADM-01,第 8 節,正式值勤／派案紀錄,承辦主管核對實際派案及權限
SYN-032,申請機構之實際參與身分 UNKNOWN,第 8 節,官方或經授權的現行參與名冊／文件,原件可重讀並記錄定位後方可判斷
SYN-033,課程公告、正式分類及價目原件均未提供,第 7、8 節,課程主責單位的正式公告、分類及價目,不得以 S-ATT 索引宣稱原件存在
SYN-034,真實預算、其他支持及可用餘額均 UNKNOWN,第 8、9 節,核定預算、財務台帳、其他支持來源,財務與獨立覆核人讀取同一截點
SYN-035,案例最終判定 HOLD；未核准、未折抵、未支付、未保留名額,第 8、10 節,有權人員依正式規範與原始證據作成的真實書面決定,不得把樣例判定改寫為協會決定
SYN-036,SAMPLE狀態變更日 2026-11-02、2026-11-03,第 8 節,真實系統時間戳、審查紀錄及可追溯事件,示例日期不作真實時間線
SYN-037,建議補件期限 5 個工作日,第 5、6 節,核定辦法、公告及適用法規,權責核定並先公告後適用
SYN-038,建議承辦形式檢查 3 個工作日、資格審查 5 個工作日,第 5 節,核定服務標準及合法期限核驗,權責核定；法定期限優先
SYN-039,建議通知 2 個工作日內完成,第 5 節,核定服務標準及送達程序,權責核定並保留送達證據
SYN-040,建議申復及回覆期限各 10 個工作日,第 10 節,現行法規及核定申復程序,法務核驗後再公告；不可宣稱法定權利期限
SYN-041,建議逐案課後對帳期限及報告頻率尚未設定,第 10 節,核定辦法、帳務及課程管理程序,由權責單位核定並登錄正式版本
SYN-042,本文版本 S0.1、狀態為草案且無生效日,封面、文末,正式文管系統版本及權責核定／公告紀錄,未核定前維持草案，不建立生效日期


## R06 deterministic technical receipt（僅背景，不代替語意判斷）
{
  "receipt_id": "0012_I02-E03_R06_DETERMINISTIC_TECHNICAL_QA",
  "document_id": "0012",
  "requirement_id": "I02-E03",
  "artifact_state": "CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED",
  "artifact_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\\candidate\\0012_I02-E03_R06.docx",
  "artifact_sha256": "f4c7a8242cb5ae0c4c038d546b2d45cac938028a521ea6ffcb5cc02334c03d13",
  "artifact_bytes": 61872,
  "source_draft_sha256": "e0664cff8178fc77190e2615b6077dec7b38931645e2a832d89c248fb351f8d6",
  "official_requirement_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
  "blueprint_file_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
  "blueprint_row_sha256": "0ebf302b8b3601be6c645573e9e12887242c8e64a2244d5cf738a35ee2f5fc04",
  "tables": 12,
  "table_rows_including_headers": 138,
  "empty_cells": 0,
  "synthetic_register_ids": 42,
  "source_fragment_count": 223,
  "source_fragments_missing": [],
  "formula_recalculation": {
    "eligible_fee_E": 6000,
    "benefit_B": 1200,
    "payable_fee": 4800,
    "remaining_limit": 5800
  },
  "checks": {
    "zip_integrity": true,
    "python_docx_open": true,
    "official_requirement_source_sha_exact": true,
    "source_draft_sha_exact": true,
    "blueprint_current_file_sha_exact": true,
    "blueprint_row_sha_exact": true,
    "official_requirement_text_present": true,
    "negative_neighbors_0011_0013_distinguished": true,
    "all_42_synthetic_ids_present": true,
    "twelve_markdown_tables_built": true,
    "register_has_header_plus_42_rows": true,
    "no_empty_table_cells": true,
    "sample_hold_boundary_present": true,
    "required_operational_mechanics_present": true,
    "no_blank_form_placeholder_terms": true,
    "all_source_lines_preserved_in_docx": true,
    "build_receipt_candidate_sha_matches": true,
    "body_run_min_font_at_least_10_5": true,
    "table_run_min_font_at_least_9_5": true,
    "sample_formula_arithmetic_consistent": true,
    "independent_semantic_review_not_misreported": true,
    "formal_acceptance_not_misreported": true
  },
  "technical_status": "PASS",
  "semantic_status": "PENDING_INDEPENDENT_REVIEW",
  "visual_status": "PENDING",
  "formal_acceptance": "UNKNOWN"
}

## R06 full-page visual receipt（僅版面範圍）
{
  "project_id": "TTQS_ONE",
  "doc_id": "0012",
  "requirement_id": "I02-E03",
  "work_id": "TTQS-0012-R06-WORD-VISUAL-QA-20261030",
  "candidate_sha256": "f4c7a8242cb5ae0c4c038d546b2d45cac938028a521ea6ffcb5cc02334c03d13",
  "pdf_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\\qa\\render_R06\\0012_I02-E03_R06_WORD_NATIVE.pdf",
  "pdf_sha256": "10bbf705680be2b2a8c15fe66fbb4ee236e6c6fa7c842ee5967c4bd4dab97488",
  "pdf_bytes": 696783,
  "render_method": "Microsoft Word COM ExportAsFixedFormat, then Poppler pdftoppm at 120 dpi",
  "observed_at_local": "2026-10-30T19:19:07.4101593+08:00",
  "page_count": 17,
  "visual_coverage": "ALL_17_PAGES_OVERVIEW; full-resolution direct inspection on changed pages 5,6,7,8,9,15,17 and prior direct inspection of page 16; pages 1-4,10-14,16 pixel-identical to inspected R05 render",
  "r05_pixel_identical_pages": [
    "page-01.png",
    "page-02.png",
    "page-03.png",
    "page-04.png",
    "page-10.png",
    "page-11.png",
    "page-12.png",
    "page-13.png",
    "page-14.png",
    "page-16.png"
  ],
  "changed_pages": [
    {
      "page": "page-05.png",
      "reason": "pixels changed"
    },
    {
      "page": "page-06.png",
      "reason": "pixels changed"
    },
    {
      "page": "page-07.png",
      "reason": "pixels changed"
    },
    {
      "page": "page-08.png",
      "reason": "pixels changed"
    },
    {
      "page": "page-09.png",
      "reason": "pixels changed"
    },
    {
      "page": "page-15.png",
      "reason": "pixels changed"
    },
    {
      "page": "page-17.png",
      "reason": "pixels changed"
    }
  ],
  "direct_inspection_findings": [
    "All changed pages 5, 6, 7, 8, 9, 15 and 17 inspected at full resolution; no clipping, overlap or table overflow observed.",
    "§5 sample service-time additions remain legible and within page margins.",
    "Pages 6-9 application, review and calculation tables remain readable; page 9 worked arithmetic is internally rendered without clipping.",
    "Page 15 SYN register rows remain readable and within landscape page bounds.",
    "SYN-037 to SYN-039 and section 13 remain readable on pages 16-17; page 16 is pixel-identical to R05.",
    "All 17 pages are present; no blank trailing page."
  ],
  "scope_limitations": [
    "Visual/layout only; not semantic acceptance, legal review, association approval or formal acceptance."
  ],
  "visual_verdict": "PASS_LAYOUT_ONLY_EXACT_SHA",
  "changed_pages_directly_inspected": [
    "page-05.png",
    "page-06.png",
    "page-07.png",
    "page-08.png",
    "page-09.png",
    "page-15.png",
    "page-17.png"
  ],
  "page_image_sha256": {
    "page-12.png": "42039f6acd630eb4f8d89a79f26a9a5b8d0ba0eef3e54bc1594866bd67b181a6",
    "page-15.png": "720560ee2dc3486ece85acd2d2c94679ea6ebb1beebbfc6d5aeef21447ee91d1",
    "page-10.png": "2c328a8789f9d333157d23b23c02e15549bb293e152b6370a955629f39c602b7",
    "page-16.png": "a5b5d9623f54e341bd5ba909a1bb8c5822b063485cdb6a360e20c0fe2cb68f52",
    "page-02.png": "99b4bb438b28ba434cf0454cf33efbc9eac4126398436c9882401ac96482893b",
    "page-08.png": "7a90a6dea8925ced1a59cf117b7d94bb2355327d145c56eda613f470ca4ec0cd",
    "page-06.png": "be9e96c4311b2f44dbc42883952e40498f37444e82ec46f1f7618f11da92eb6a",
    "page-05.png": "64759ca2ede849821f115ebe13786b1648e5366c5c6f33d6fff3db00558c1008",
    "page-11.png": "d7d6e95769517dde8e23f5bf3fcefe6cb7a412cbb531d255d8ac609202dfe6e9",
    "page-01.png": "f1f1bc06e6e01d9319ac5c0e9ae37c9c33c514839dee2b6c2c62cf4535517104",
    "page-04.png": "5d1dce9354f2d7bfa2280bb0f94edc065f11b792304bb6a7874b140c84ea5cfe",
    "page-07.png": "a3fcc2a711eca176ccc324f16b788d316a3fa1af50574139604654dff59b229a",
    "page-14.png": "cc5f39ec4d5643a6b736b53a54e5e9c7e592c1e5b477c2fdc3fa542ed1c50f75",
    "page-09.png": "6819c50dba0ee3e0f926504d865890d180790f553fb2172a5882edf5d40c3947",
    "page-03.png": "5f5199ac9035c22e52cae6976a6a02733f16d8fc3662306d36cc553ce27bc33f",
    "page-17.png": "61ad01c3fc394d532c84bf4fbea0de2a38dcbdc821aed61039abce772adc4aaf",
    "page-13.png": "bfa6bf574c1c7b70818577e14c009b1949f1538fd269de9642a118b1beb7b8f3"
  },
  "contact_sheet_sha256": "2dc9c9ad2ad19b168502e0ba70c9c8b166270e888c3e73e1946916a40a1449ff"
}

## R06 source draft copy SHA-256
{
  "source_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\\worker\\luna_subagent_draft_R01_R06_scoped_repair.md",
  "source_sha256": "e0664cff8178fc77190e2615b6077dec7b38931645e2a832d89c248fb351f8d6",
  "register_sha256": "e61696b0c5161f98666b3e87e3a6de60a1f2f72a096ccc7a8e3cd1e7c2959ed9"
}