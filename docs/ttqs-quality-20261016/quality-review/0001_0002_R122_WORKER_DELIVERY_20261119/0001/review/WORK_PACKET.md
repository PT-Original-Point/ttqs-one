# TTQS ONE independent semantic review packet
work_id: TTQS_ONE_0001_I01-E01_SEMANTIC_REVIEW_R01_20261119
doc_id: 0001
requirement_id: I01-E01
reviewer: W2 Antigravity CLI (must differ from the substantive writer)
role: read-only semantic/usability review; do not edit the DOCX or claim promotion
candidate_filename: 0001_I01-E01_R01.docx
candidate_docx_sha256: 2C643258ADD377789F1A04F9FFE0FAEBF53CB2AEEE38EC0B7234E5BDA92BC0BB
candidate_extracted_text_sha256: 0109D57D9047282FA6EAAE075708BB10A66BB12E9B74FE60F71C0FCB752566E5
review_basis_limit: official PDF bytes are hash-verified as 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709; page text was not extracted in this task. Use the exact requirement wording and Blueprint below; treat cited page/manual/website locators as unverified unless the candidate explicitly caveats them.

## Review instructions
Review the exact candidate identified above. Return ONLY one JSON object with keys:
doc_id, candidate_docx_sha256, status (PASS/FAIL/BLOCKED), checks (requirement_fit, genre_mechanics, title_blind_identification, evaluator_usability, SAMPLE_SYNTHETIC_boundary, synthetic_fact_register, calculation_consistency, evidence_scope_and_source_limits, negative_neighbor_separation), findings (array of objects with severity BLOCKING or NONBLOCKING, exact section/table/row locator, issue, correction_needed), and limitations.
PASS only if all required acceptance tests below are supported by this exact candidate text. A nonblocking style preference must not cause FAIL. Do not suggest a full rewrite. Do not review pagination or visual layout. Do not assert external source verification absent in this packet. Do not write files, invoke tools, or change the candidate.
Check formulas against the supplied sample facts. Check that no actual association performance, approval, signature, third-party result or real staff is invented. Determine whether SAMPLE values and replacement register are coherent. Point to locators, not general impressions.

## Official requirement, crosswalk and unique Blueprint record
 (full source record SHA-256 3EC552BCF35E43E067C376AFCBB431A01A82F3284A987331106BF99CC1658C9E)
{
  "deliverable_id": "0001",
  "requirement_id": "I01-E01",
  "final_filename": "0001__中長程業務發展策略地圖.docx",
  "document_genre": "策略／計畫文件｜中長程業務發展策略地圖",
  "document_purpose": "本件專屬焦點：中長程業務發展策略地圖；需直接回應的官方佐證要求為：中長程的業務發展規劃策略地圖。 （p.13；OOO手冊中第O頁； 官網首頁）；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。",
  "primary_user_or_reader": "供理監事、主管與執行人員把官方要求轉為可執行的方向、責任、時程與衡量方式。",
  "evidence_role": "以源頭策略或計畫證明要求如何落地；提供目標、責任、基準與決策依據。 本文件只擁有 I01-E01 的直接紀錄／分析口徑；不得吞併其他要求的事實。",
  "required_sections": "文件用途與決策範圍；官方要求與適用界線；現況、需求與可驗證來源；目標對象、價值與服務範圍；策略／計畫主軸與因果關係；目標、基準、指標與計算口徑；工作分解、責任與協作；資源、時程與里程碑；風險、假設及應變門檻；檢討頻率、決策紀錄與修訂；完整合成示例與真實資料替換清單；證據索引、限制與版本核對",
  "required_tables_or_figures": "欄位—定義—來源—填寫者—驗證規則；完整合成填寫列及欄位解說；問題／例外—修正—覆核及追蹤；官方要求—表單欄位—附件定位追溯表",
  "required_fields_or_questions": "合成資料識別碼；日期欄位及合成標示；責任角色代碼；來源／附件位置欄位；判定、理由、覆核及後續行動",
  "required_calculations_or_analysis": "若此表單有數量、金額、期間或比例，明列定義、分子分母與逐步算例；若沒有，明示不適用並提供至少一個欄位驗證／完整度判斷示例。",
  "required_cross_references": "同要求分件 0002；相鄰要求 I01-E02；共用原始來源時只引用核實結果，不複製別份文件正文。",
  "real_data_required": "升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。",
  "third_party_evidence_required": "若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。",
  "prohibited_fabrication": "不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。",
  "title_blind_test": "遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『中長程業務發展策略地圖』並證明『中長程的業務發展規劃策略地圖。 （p.13；OOO手冊中第O頁； 官網首頁）』；若可無修改移作其他要求即失敗。",
  "negative_choice_neighbors": "0003《目標市場需求調查問卷》（I01-E02）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0002《策略因果鏈與三年KPI對照表》（I01-E01）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。",
  "acceptance_tests": "移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『中長程業務發展策略地圖』，且能指出直接回應『中長程的業務發展規劃策略地圖。 （p.13；OOO手冊中第O頁； 官網首頁）』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。"
}


## Shared SAMPLE scenario
 (planning illustration only; not actual association data)
- SYN-ORG-01: fictional community-care training institution; never state this as the real status of 屏東縣原始點關懷協會.
- SYN-PERIOD-01: illustrative planning window 2026-2028. All actual baselines and performance are UNKNOWN and must be replaced with verified records.
- SYN-A1-01: Strategy axis 1, standardize course design and delivery. Metric: internally reviewed standard course designs / 3 planned courses. SAMPLE baseline 2025: 0/3; targets 2026 1/3, 2027 2/3, 2028 3/3.
- SYN-A2-01: Strategy axis 2, improve post-training follow-up coverage. Metric: valid completed follow-ups / eligible completers. For arithmetic demonstration only, denominator is 50: SAMPLE 2025 20/50=40%; targets 2026 25/50=50%, 2027 30/50=60%, 2028 35/50=70%. Real denominator must be recalculated each period from verified completion roster and lawful consent scope.
- SYN-A3-01: Strategy axis 3, improve evidence traceability. Metric: sampled records with all required fields and retrievable source / sampled records. Demonstration denominator 20: SAMPLE 2025 14/20=70%; targets 2026 16/20=80%, 2027 18/20=90%, 2028 19/20=95%.
- SYN-ROLE-01: fictional strategy sponsor role code; not a real person or authorization.
- SYN-ROLE-02: fictional implementation coordinator role code; not a real person or authorization.
- SYN-REVIEW-01: illustrative quarterly review; a gap of 10 percentage points from a target triggers a cause analysis and corrective proposal. This is not an official threshold or current association policy.
- SYN-RISK-01: contact/follow-up requires lawful authority and minimum necessary data. Without consent or verifiable source, mark HOLD; exclude from numerator; do not infer performance.
- SYN-BUDGET-01: actual budget, approvals, real staff, courses, participants and outcomes are UNKNOWN. Do not invent money, signatures, approvals or achievements.
Each deliverable must include its own replacement register listing these IDs, document locator, authoritative replacement source and responsible role. Register every additional synthetic fact under a new ID. The two documents may cite the same IDs but must not copy each other's prose or alter values.


## Exact candidate body text extracted from the DOCX
0001 中長程業務發展策略地圖
SAMPLE / SYNTHETIC ONLY：本文件所有策略、基準、目標、角色、日期、里程碑、判定與範例皆為合成示範。真實機構資料、核准、簽章、預算、班次、參與者與成果皆為 UNKNOWN；不得宣稱實績、正式核准或第三方原件。
0. 快速摘要
目的：將官方要求「中長程的業務發展規劃策略地圖。」轉為可執行的策略方向、責任分工、時程、衡量方式與檢討機制。
讀者：理監事、主管與執行人員。
使用時點：年度計畫制定、每季檢討、新專案啟動前、外部說明前。
操作：先確認官方要求與界線，再讀三條策略軸與因果關係，接著查任務、角色、里程碑、風險與例外處理。
輸出：策略地圖、三年示意方向、責任分工、例外處理流程、事實替換簿與證據索引。
狀態：SAMPLE / SYNTHETIC ONLY；REAL 資料與核准仍待核實。
1. 文件用途與決策範圍
本文件專屬焦點為「中長程業務發展策略地圖」，用於把官方要求轉成可執行方向、責任、時程與衡量方式。本文件不提供 KPI 稽核矩陣、不作市場調查結論，也不把擬真工作稿標示為 REAL。
決策範圍包括：2026-2028 規劃期、三條策略軸、任務分解、角色代碼、里程碑、風險應變、檢討頻率與修訂規則。決策範圍不包括：真實預算核准、人事任命、對外服務承諾、個資合法範圍判定、正式簽章或第三方原件取得。
2. 官方要求與適用界線
官方要求原文：「中長程的業務發展規劃策略地圖。」（來源登錄：官方表 I01-E01；本執行沿用控制列登錄之頁次／手冊／官網引用，未重新抽取 PDF 頁面文字，不得宣稱外部引用已重新驗證。）
本文件只擁有 I01-E01 的直接紀錄／分析口徑，不得吞併其他要求的事實。0001 與 0002 同屬 I01-E01，但 0001 負責策略方向、因果關係與實施路徑；0002 負責策略因果鏈與三年 KPI 對照。0003 屬 I01-E02，負責目標市場需求調查，不得由本文件代作。
3. 現況、需求與可驗證來源
已核實來源為官方 PDF 雜湊、Blueprint、crosswalk 與 PR HEAD；機構現況、課程、參與者、成果、預算與核准皆未核實。SYN-ORG-01 為虛構社區照顧訓練機構，僅供規劃示範，不得描述為屏東縣原始點關懷協會的真實狀態。
需求判斷：官方要求需要一份中長程策略地圖，但本文件只能提供合成示範；REAL 升格前必須逐項取得正式日期、真實人名／角色、核准／簽章、真實班次／課程、實際數字／比例、真實附件與檔案位置。
4. 目標對象、價值與服務範圍
主要讀者為理監事、主管與執行人員。本文件價值在於把抽象要求轉為方向、責任、基準與決策依據。使用時點為年度計畫、每季檢討、新專案啟動與外部說明前。
服務範圍以 SYN-ORG-01 示範三項：課程設計與提供標準化、訓後追蹤覆蓋率提升、證據可追溯性提升。這三項是策略方向示範，不代表機構已提供服務或已有成果。
5. 策略主軸與因果關係
三條策略軸為：A1 課程設計與提供標準化；A2 訓後追蹤覆蓋率提升；A3 證據可追溯性提升。因果鏈為：標準化課程設計提升提供一致性，一致性使訓後追蹤可執行，追蹤結果回寫紀錄，完整紀錄支撐決策與覆核。0002 將承接 KPI 對照與公式驗證；本文件不重製其稽核矩陣。
6. 目標、基準、指標與計算口徑
所有數值皆為 SAMPLE/SYNTHETIC，僅供算例。分母、單位、期間與 N/A 條件必須清楚；真實基準與績效皆 UNKNOWN。
策略軸與因果指標
基準目標與差距判定
佐證責任與後續處置
計算口徑示例（SYN-A2-01）：20/50=0.40=40%；25/50=0.50=50%；30/50=0.60=60%；35/50=0.70=70%。A1 與 A3 同樣以分子除以分母，四捨五入至整數百分比。若同意追蹤範圍或抽樣母體改變，分母必須重算，目標不得硬性沿用。
本文件無金額計算；預算、費用與成本皆為 UNKNOWN（SYN-BUDGET-01）。若未來納入金額，必須先登錄新合成資料識別碼，明列定義、分子分母、期間、四捨五入與 N/A 條件。
欄位驗證／完整度判斷示例：
來源／附件位置空白或無法定位：判定「不完整」，不得進入檢討結論。
分母來源未核實：標記 HOLD，分子不計入，不得推論績效（SYN-RISK-01）。
角色代碼未登錄：退回補件。
日期未標 SAMPLE：退回，避免誤認 REAL。
7. 工作分解、責任與協作
SYN-ROLE-01 為虛構策略贊助角色代碼，SYN-ROLE-02 為虛構執行協調角色代碼；皆非真實人名或授權。實際姓名、職務與授權必須以核實紀錄替換。
8. 資源、時程與里程碑
實際預算、核准、真實員工、課程、參與者與成果皆 UNKNOWN（SYN-BUDGET-01）。下表日期為合成示範（SYN-TIME-01），不代表已排定或已核准行事曆。
資源清單：文件模板、會議紀錄、課程設計資料、結訓與追蹤紀錄、同意紀錄、抽樣紀錄、來源定位索引、版本控制。金額、採購與人事配置皆未登錄，不得填入數字。
9. 風險、假設及應變門檻
SYN-RISK-01：聯絡與追蹤需要合法權限與最小必要資料；無同意或可驗證來源時標記 HOLD，排除分子，不得推論績效。SYN-REVIEW-01：每季檢討若與目標差距達 10 個百分點，觸發原因分析與改善提案；此為示範門檻，不是官方或協會現行制度。
假設：所有基準與目標皆為合成示範；實際機構可能已有不同課程、追蹤能力與紀錄成熟度。若真實資料與示範方向衝突，以核實資料與正式核准為準，並更新本文件版本。
10. 檢討頻率、決策紀錄與修訂
檢討頻率為每季一次（SYN-REVIEW-01 示範），年度至少一次策略回顧。本文件不宣稱已建立正式治理制度或已獲核准。
修訂規則：任何 REAL 資料替換、角色替換、期間變更或公式變更都必須更新版本、登錄替換簿並保留舊版追溯。
11. 完整合成示例與真實資料替換清單
以下為完整填入的 SAMPLE 範例，不是真實機構紀錄。SYN-EX-01 登錄此範例列；SYN-TIME-01 登錄其日期。
替換登記簿：
12. 證據索引、限制與版本核對
限制：本執行已驗證 PDF 檔案雜湊，但未獨立重新抽取頁面文字；p.13、手冊頁次與官網引用沿用控制列登錄，不得宣稱已重新驗證。本文件不含 REAL 資料、正式核准、簽章、第三方原件或機構實績。

[TABLE 1]
項目 | 內容
文件編號 | 0001
要求編號 | I01-E01
檔名 | 0001__中長程業務發展策略地圖.docx
文類 | 策略／計畫文件｜中長程業務發展策略地圖
狀態 | SAMPLE / SYNTHETIC ONLY（非 REAL）
同要求分件 | 0002《策略因果鏈與三年KPI對照表》（I01-E01）
相鄰要求 | I01-E02《目標市場需求調查問卷》（0003）
規劃期間 | 2026-2028（SYN-PERIOD-01，合成期間）

[TABLE 2]
欄位 | 定義 | 來源 | 填寫者 | 驗證規則
文件編號 | 本文件唯一識別碼 | Blueprint 0001 | 文件管理角色 | 必須等於 0001
要求編號 | 對應官方要求編號 | Blueprint / crosswalk | 文件管理角色 | 必須等於 I01-E01
規劃期間 | 策略規劃起訖期間 | SYN-PERIOD-01 | SYN-ROLE-01 | 必須標示 SAMPLE；真實期間以核實計畫為準
狀態 | REAL / SAMPLE / SYNTHETIC 判定 | Blueprint | 文件管理角色 | 未核實前只能標 SAMPLE/SYNTHETIC
責任角色代碼 | 執行或覆核角色代碼 | SYN-ROLE-01/02 | 任務負責人 | 必須為已登錄角色代碼
來源／附件位置 | 可追溯的檔案、頁面或紀錄位置 | 本文件證據索引 | 填表人 | 空白或無法定位則判定不完整
判定 | 通過、不完整、HOLD 或需補件 | 執行與覆核紀錄 | SYN-ROLE-01 | 必須附理由、覆核者與後續行動

[TABLE 3]
界線項目 | 本文件處理方式
官方原文 | 原文引用，不改寫
文件身分 | 依 Blueprint 0001 唯一列判定
同要求分件 | 只交叉引用 0002，不複製其 KPI 稽核正文
相鄰要求 | 只標示 0003 範圍，不納入市場調查題項或結論
未核實資料 | 標示 UNKNOWN 或 SAMPLE/SYNTHETIC
第三方原件 | 只說明所需原件與取得路徑，不代製、仿簽或冒充

[TABLE 4]
來源 | 核實結果 | 本文件使用方式
官方 PDF | SHA-256 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709 | 引用要求 wording 與來源定位，不重製全文
Blueprint row 0001 | SHA-256 3EC552BCF35E43E067C376AFCBB431A01A82F3284A987331106BF99CC1658C9E | 文件身分、章節、欄位、驗收
Blueprint row 0002 | SHA-256 ACF45A45F488364BF14F3FD3A73530EA8F1C37BF2EC02E0CF532EC20E9F05D4C | 區分同要求分件身分
Crosswalk | SHA-256 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679 | 區分 0001／0002
PR HEAD | 00ed19b422dd8764dae588b1c26dd60643e91848 | 基線確認；分支無 0001/0002 候選 DOCX

[TABLE 5]
策略軸 | 核心問題 | 因果輸出 | 本文件擁有內容 | 不屬於本文件
A1 課程設計與提供標準化 | 課程設計是否一致可審查 | 標準課程設計數增加 | 方向、任務、責任、里程碑 | 課程市場需求統計
A2 訓後追蹤覆蓋率提升 | 結訓者是否被合法有效追蹤 | 有效完成追蹤數增加 | 追蹤流程、同意與最小必要資料 | 個資法律最終判定
A3 證據可追溯性提升 | 紀錄是否可定位與重算 | 完整可追溯樣本增加 | 欄位、來源定位、覆核流程 | 第三方原件取得

[TABLE 6]
近鄰文件 | 本文件不包含 | 可核對差異欄位／章節
0002《策略因果鏈與三年KPI對照表》 | KPI 稽核矩陣、跨年比較、公式驗證結論 | §6 只列方向性指標；KPI 細項、公式與稽核結果交 0002
0003《目標市場需求調查問卷》 | 問卷題項、量尺、抽樣與市場需求結論 | §4 僅列服務範圍示範；不納入調查題項或需求統計

[TABLE 7]
策略軸 | 指標 | 分子 | 分母
A1 | 內部審查通過的標準課程設計數／規劃課程數 | 通過審查的標準課程設計數 | 規劃課程數
A2 | 有效完成追蹤數／合格結訓且同意追蹤數 | 有效完成追蹤數 | 合格結訓且同意追蹤數
A3 | 所有必要欄位完整且來源可取回的樣本數／抽樣紀錄數 | 完整可追溯樣本數 | 抽樣紀錄數

[TABLE 8]
策略軸 | 2025 基準（SAMPLE） | 2026 目標（SAMPLE）
A1 | 0/3 | 1/3
A2 | 20/50=40% | 25/50=50%
A3 | 14/20=70% | 16/20=80%

[TABLE 9]
策略軸 | 2027 目標（SAMPLE） | 2028 目標（SAMPLE）
A1 | 2/3 | 3/3
A2 | 30/50=60% | 35/50=70%
A3 | 18/20=90% | 19/20=95%

[TABLE 10]
任務編號 | 策略軸 | 工作內容 | 責任角色 | 協作 | 輸出
T1 | A1 | 建立課程設計檢查表與審查流程 | SYN-ROLE-02 | SYN-ROLE-01 | 課程設計審查紀錄
T2 | A1 | 建立標準課程版本與變更紀錄 | SYN-ROLE-02 | 課程提供人員 | 版本紀錄
T3 | A2 | 建立結訓名冊與同意追蹤範圍 | SYN-ROLE-02 | 資料管理角色 | 追蹤母體清單
T4 | A2 | 執行訓後追蹤並記錄結果 | SYN-ROLE-02 | 聯絡窗口 | 追蹤紀錄
T5 | A3 | 建立紀錄欄位與來源定位規則 | SYN-ROLE-01 | SYN-ROLE-02 | 欄位定義表
T6 | A3 | 執行抽樣覆核與例外追蹤 | SYN-ROLE-02 | SYN-ROLE-01 | 覆核紀錄
T7 | 全軸 | 每季彙整策略進度與決策紀錄 | SYN-ROLE-01 | SYN-ROLE-02 | 季度檢討紀錄

[TABLE 11]
期間 | 里程碑 | 責任角色 | 所需資源 | 狀態
2026 Q1（SAMPLE） | 確認策略軸、角色代碼與欄位定義 | SYN-ROLE-01 | 文件、會議紀錄、版本控制 | SAMPLE
2026 Q2（SAMPLE） | 完成 A1 檢查表與 A3 欄位規則 | SYN-ROLE-02 | 課程資料、紀錄表 | SAMPLE
2026 Q3（SAMPLE） | 建立 A2 追蹤母體與同意範圍 | SYN-ROLE-02 | 結訓名冊、同意紀錄 | SAMPLE
2026 Q4（SAMPLE） | 第一次年度策略檢討與替換簿更新 | SYN-ROLE-01 | 檢討紀錄、決策紀錄 | SAMPLE
2027（SAMPLE） | A1/A2/A3 目標提升與例外修正 | SYN-ROLE-02 | 課程、追蹤、抽樣資料 | SAMPLE
2028（SAMPLE） | 三年方向回顧與下一期規劃 | SYN-ROLE-01 | 歷年紀錄、決策紀錄 | SAMPLE

[TABLE 12]
問題／例外 | 修正 | 覆核及追蹤
追蹤母體缺同意紀錄 | 先標記 HOLD，補取得合法同意或縮小資料範圍 | SYN-ROLE-01 覆核；列入季度例外表
課程設計無審查紀錄 | 不計入 A1 分子，補審查後重算 | SYN-ROLE-02 補件，SYN-ROLE-01 覆核
紀錄欄位缺失或來源無法定位 | 標記不完整，補欄位與來源索引 | SYN-ROLE-02 修正，下次抽樣複查
目標差距達 10 個百分點（SAMPLE） | 提出原因分析與改善提案 | 季度檢討會決議，更新替換簿
預算或核准未知 | 不填金額，列為待核事項 | SYN-ROLE-01 追蹤至核實

[TABLE 13]
欄位 | 定義 | 來源 | 填寫者 | 驗證規則
檢討日期 | 實際檢討日期 | 會議紀錄 | SYN-ROLE-01 | 必須標示 SAMPLE 或 REAL
指標結果 | 分子／分母與百分比 | §6 口徑 | SYN-ROLE-02 | 必須可由展示數據重算
差距判定 | 是否達標或差距 | SYN-REVIEW-01 | SYN-ROLE-01 | 門檻若非官方，必須標示示範
決策內容 | 採納、暂缓、修正或升級 | 檢討會議 | SYN-ROLE-01 | 不得宣稱正式核准
覆核者 | 覆核角色代碼 | 角色登錄 | SYN-ROLE-01 | 必須為登錄代碼
修訂版本 | 文件版本與日期 | 版本控制 | 文件管理角色 | 版本變更必附原因

[TABLE 14]
欄位 | 填寫內容（SAMPLE）
合成資料識別碼 | SYN-EX-01
日期欄位及合成標示 | 2026-03-31（SAMPLE；實際日期以核實會議／決策紀錄為準）
責任角色代碼 | SYN-ROLE-02
來源／附件位置欄位 | SAMPLE/附件定位/SYN-EX-01（非真實檔案路徑）
策略軸 | A2 訓後追蹤覆蓋率提升
指標結果 | 25/50=50%（SAMPLE）
判定 | 需補件
理由 | 同意追蹤範圍尚未核實，分母可能變動
覆核 | SYN-ROLE-01
後續行動 | 補取得同意紀錄後重算；未核實前不宣稱績效

[TABLE 15]
合成資料識別碼 | 文件位置 | 權威替換來源 | 責任角色 | 替換方式
SYN-ORG-01 | §3、§4 | 機構登記、章程、服務範圍核定文件 | SYN-ROLE-01 | 以核實機構資料替換，不得沿用虛構名稱
SYN-PERIOD-01 | §1、§8 | 核准計畫期間與年度行事曆 | SYN-ROLE-01 | 以真實計畫期程替換
SYN-A1-01 | §5、§6、§11 | 課程清單與設計審查紀錄 | SYN-ROLE-02 | 以實際課程數與審查結果重算
SYN-A2-01 | §6、§11 | 結訓名冊與同意追蹤範圍 | SYN-ROLE-02 | 重算分母與分子
SYN-A3-01 | §6、§11 | 抽樣紀錄與來源定位 | SYN-ROLE-02 | 重算抽樣結果
SYN-ROLE-01 | §7、§11 | 職務分工與授權紀錄 | 真實主管／理事會 | 以實際角色與姓名替換，不得冒充授權
SYN-ROLE-02 | §7、§11 | 執行分工與指派紀錄 | 真實主管 | 以實際角色與姓名替換
SYN-REVIEW-01 | §9、§10 | 協會既定檢討制度或核准辦法 | SYN-ROLE-01 | 以實際門檻替換，不得宣稱官方標準
SYN-RISK-01 | §9、§11 | 同意書與個資處理依據 | SYN-ROLE-02 | 以合法授權與最小必要資料替換
SYN-BUDGET-01 | §8 | 預算書、採購或人事核定 | SYN-ROLE-01 | 補入真實金額與核准紀錄
SYN-EX-01 | §11 | 會議、決策或檢討紀錄 | SYN-ROLE-01 | 以真實紀錄替換整列
SYN-TIME-01 | §8、§11 | 年度行事曆與決策日期 | SYN-ROLE-01 | 以真實日期替換

[TABLE 16]
官方要求 | 表單欄位 | 附件定位
中長程的業務發展規劃策略地圖。 | 文件編號、要求編號、策略軸、任務、角色、里程碑、檢討欄位 | 官方 PDF 表 I01-E01；本文件 §5-§11
可追溯來源 | 來源／附件位置 | §3 來源表與本節
合成資料識別 | 合成資料識別碼 | §11 替換登記簿

[TABLE 17]
核對項目 | 內容
文件編號 | 0001
要求編號 | I01-E01
檔名 | 0001__中長程業務發展策略地圖.docx
Blueprint row 0001 SHA-256 | 3EC552BCF35E43E067C376AFCBB431A01A82F3284A987331106BF99CC1658C9E
Blueprint row 0002 SHA-256 | ACF45A45F488364BF14F3FD3A73530EA8F1C37BF2EC02E0CF532EC20E9F05D4C
Crosswalk SHA-256 | 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679
官方 PDF SHA-256 | 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709
PR HEAD | 00ed19b422dd8764dae588b1c26dd60643e91848
狀態 | SAMPLE / SYNTHETIC ONLY（非 REAL）
字體下限 | 正文至少 10.5pt；表格至少 9.5pt；資訊不足時加頁，不縮小字體
