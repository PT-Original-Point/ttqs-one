# TTQS ONE 0025 exact-SHA independent semantic review

work_id: TTQS_ONE_0025_I04-E04_INDEPENDENT_SEMANTIC_REVIEW_R05_LONGCAT_20261119
doc_id: 0025
requirement_id: I04-E04
candidate_sha256: B72A65EA05D118C6479747280DBA768AC27ECB0B2A335FDD61C0FA2A32D9FC2D
source_packet_sha256: 46112EDAD5C828AD4B53F4415A519E16BAD74151136D8795F75D053FEF075F23
blueprint_sha256: D63626B36BE27FCB98EB51AFF7BAAAEB8019723B88661A349311420D9E259B90
blueprint_022_row_sha256: 35480951C5DF124DFD96F43A6BA613305F120C5D962A45C515343E0D94E6BB1C

## Authoritative target
Official source: OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf, p. 2, SHA256 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709. Required item: 「訓練結果的評估、訓練實施的依據及標準化作業流程（SOP）。」
Crosswalk exact row SHA256 1F6B41070A71898A4C32DDF0BBB490A2E03E9F3C19426B0C7A2878E286A1AED2: I04-E04 -> doc_id 0025, 「訓練評估與實施標準化作業程序SOP」.
Unique Blueprint 022: 「訓練評估及 SOP：角色、流程分支、控制點、表單」; requires source location, substantive core procedure/example, decision/result, and links to facts in adjacent documents, with no blank-form substitution.
Evaluate the following full text as an operational SOP: source-bound inputs; roles/RACI; triggers and ordered steps; branches and controls; populated forms; formulas, denominators and thresholds; coherent complete SAMPLE/SYNTHETIC example and fact register; separation from I04-E01/E02/E03/E05; truth boundary and UNKNOWN treatment; evaluator usability.

## Candidate revision and targeted prior findings
R04 SHA256 4C45BB9B7924CCB698C0CDD7E2E13062F3C93E87AE84907AFC363074104B7A55 had two blocking findings:
- Table 8-H SYN-EV-03 claimed 4 modules while the coherent case had 3.
- Table 6-A / 8-F confused an individual 80-point threshold with the descriptive group post-test average.
R05 makes only three table-cell changes: Table 6-A explicitly says no group-average threshold and scopes 80 points to individual evaluation; Table 8-F repeats that distinction; Table 8-H SYN-EV-03 says 3 modules. All other table cells and non-table body paragraphs match R04 exactly.
R05 exact-SHA static and arithmetic QA: PASS_STATIC_PENDING_SEMANTIC, 28 tables, 1,142 cells, no empty cells or external relationships, 10 Form F calculations recomputed, SAMPLE roster recomputed (18, 16 valid/attended, pre sum 960, post sum 1,360, 14 initial passes). Word native open/PDF and 19-page visual review passed separately. Those are supplied as context, not a substitute for your independent semantic judgment. Do not claim layout or formal acceptance in your verdict.
The reviewer is not the substantive Writer of 0025. Review this exact SHA only; do not edit/rebuild. Treat only concrete material defects that prevent the stated requirement or create false operational claims as blocking. Optional wording/style/LOW issues belong in nonblocking_findings and must not trigger a rewrite.

## Required response
Return exactly one valid JSON object, no Markdown fence. Keys:
candidate_sha256, verdict (PASS/PARTIAL/FAIL), blocking_findings (array; each finding has locator, requirement, evidence, minimal_repair), nonblocking_findings (array), scope_checked, source_and_blueprint_bound, no_real_or_approval_fabrication, sampled_values_and_register_consistent, cross_document_scope, reviewer_note.
If there is no material blocker, verdict PASS. Bind the result to the exact candidate SHA above.

## Full candidate text extracted from the exact R05 DOCX
訓練評估與實施標準化作業程序SOP
TTQS_ONE｜交付件 doc_id 0025｜需求 I04-E04｜候選文件識別：TTQS-I04-E04-SOP-0025
狀態：CANDIDATE　內含 SAMPLE／SYNTHETIC 示範　未核準、未公告、未生效
真相邊界（必讀）：本文件是候選（CANDIDATE）撰寫成果，不是機構正式核準、公告或生效的 SOP，也不代表任何 REAL 訓練活動、REAL 人員、REAL 成績、REAL 決策、REAL 會議或 REAL 成效。文中所有課程、日期、學員、名額、分數、問卷、會議、決策與結案值，凡標示 SAMPLE／SYNTHETIC 或 SYN- 者，皆為合成示例，目的僅在演示流程、公式、分支與表單操作，不得作為機構實績或對外證明，亦不得改寫成實際辦訓紀錄。凡未取得可驗證來源的機構事實（正式文件代碼、職稱、人員、代理授權、核定門檻、生效狀態、保存期限、個資權限等）一律標示 UNKNOWN，並在第 10 節列明所需證據。本文件不發明 REAL 門檻，不暗示協會、政府、評審或第三方已核準、認可、公告或使用本文件。
0. 文件識別與適用界線
### TABLE 1
表 0-A：文件／流程識別（FORM A，候選例值）
欄位 | 內容
文件名稱 | 訓練評估與實施標準化作業程序SOP（與 crosswalk 指定名稱完全一致）
需求編號 | I04-E04
交付件 doc_id | 0025
專案 | TTQS_ONE
候選文件代碼 | TTQS-I04-E04-SOP-0025（REAL 正式代碼 UNKNOWN）
版次 | R01-CANDIDATE
狀態 | CANDIDATE；未核準、未公告、未生效、未實施
撰寫角色 | W1 獨立文件撰稿者（功能角色；真實姓名、授權 UNKNOWN）
撰寫日期 | 2026-11-17（合成作業日；非生效日、非核準日）
適用範圍 | 每一次訓練期程之：課程依據核對、課前就緒、依計畫實施與偏差記錄、評估收集與驗證、指標計算與獨立檢查、判定、補救與追蹤、結案與可追溯。
不涵蓋（相鄰需求） | I04-E01 需求調查／分析、I04-E02 課程設計／規劃、I04-E03 訓練提供方式選擇、I04-E05 TTQS 文件資訊／文件管制。本文件只交叉連結其事實識別，不複製其專屬正文。
變更理由 | 初始 candidate 版本；整合 I04-E04 官方摘錄、crosswalk 第 20 行與 Blueprint 第 022 列。
0.1 權威來源摘錄（精確定位）
官方來源：OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf，第 2 頁，項次「4. 訓練品質管理的系統化文件資訊」。原文引錄（bounded exact extract）：
「訓練結果的評估、訓練實施的依據及標準化作業流程（SOP）。」
同頁並要求以文件說明 TTQS 管理系統如何運作，以及文件如何核準、公告、更新與保存紀錄；該制度細節屬 I04-E05（doc_id 0026），本文件不另造，僅保留自身文件識別與證據索引欄位。
0.2 來源定位與版本綁定（SHA-256）
### TABLE 2
表 0-B：來源綁定（已讀回雜湊；任何來源變更即停止沿用）
來源 | 定位 | SHA-256 | 用途
0025 來源包 | SOURCE_PACKET_0025_I04-E04_R01.md | 46112EDAD5C828AD4B53F4415A519E16BAD74151136D8795F75D053FEF075F23 | 範圍、摘錄、來源選擇
來源包 Manifest | SOURCE_PACKET_MANIFEST.json | 3827AE4E91F5FD2120BDDA926F45CD39A1F81C51C4156D10079AF128409A5DA1 | 來源包位元組與來源綁定
官方評核表 | OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf，第 2 頁 | 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709 | 正式需求依據
官方頁面文字讀回 | OFFICIAL_SOURCE_PAGE2_READBACK_R01.txt | 3C295E8861AD7775A78583E9111DF61AC8733A7CF40D771F942363F00572DE9C | 核對原文及上下文
129-to-142 crosswalk | CROSSWALK_129_TO_142_R01.csv（全檔） | 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679 | 指定 I04-E04 對應 0025
crosswalk 第 20 行 | I04-E04,1,0,0025,訓練評估與實施標準化作業程序SOP | 1F6B41070A71898A4C32DDF0BBB490A2E03E9F3C19426B0C7A2878E286A1AED2 | 文件編號及需求名稱
Blueprint 主檔 | BLUEPRINT_157_CHECKBOXES_LIVE_R01.md | AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216 | 指定第 022 列
Blueprint 第 022 列 | 022｜訓練評估及 SOP：角色、流程分支、控制點、表單… | 35480951C5DF124DFD96F43A6BA613305F120C5D962A45C515343E0D94E6BB1C | 文類及最低內容要求
0.3 狀態與授權聲明
本文件為 CANDIDATE；起草者不宣稱批準、接受、生效或採用。
真實機構職稱、代理人、授權階層、核準者、公告日期、保存位置與保存期限皆為 UNKNOWN，須由機構正式來源替換。
所有 SAMPLE 資料僅為流程示範，門檻值（80 分、85%、4.0/5、85%）為 SAMPLE 門檻，不是機構 LIVE 規則。
1. 目的、範圍與定義
1.1 目的
建立一套訓練執行者可按步驟操作、主管可依權責處置、評核者可抽查來源與計算的標準作業程序，串起「核定課程依據 → 課前確認 → 實際實施紀錄 → 評估資料 → 判讀 → 補救／改善 → 結案及紀錄定位」，使每一次訓練期程的實施與評估皆可重現、可稽核、可改善。
1.2 範圍與不涵蓋
本 SOP 管理訓練如何依據核定內容實施、如何評估結果，以及結果如何導致處置與改善。需求分析（I04-E01）、課程設計（I04-E02）、教學方式選擇（I04-E03）及 TTQS 文件管制（I04-E05）屬相鄰需求；本文件只引用其必要事實識別，不重做其專業判斷，不複製其正文、表格或案例。
1.3 定義
### TABLE 3
表 1-A：作業定義
用語 | 定義
核定課程依據 | 經機構核定程序通過的課程目標、對象、時數、模組、教材與評量方式等執行基準。若未取得核定證據，狀態為 UNKNOWN，不得稱為已核定。
期程識別碼 | 為每一次訓練期程建立的唯一識別碼（本文件範例：SYN-0025-TRAIN-01），用於串連所有表單、紀錄與證據。
有效評估 | 工具版本明確、母體與有效樣本可界定、缺漏與無效值已記錄、且可回溯至原始作答的評估資料。
母體／有效樣本 | 母體指符合評估資格的人；有效樣本指通過完整性與有效性檢核的實際可用資料。分母必須明確揭露。
偏差 | 計畫值與實際值不一致，或實施偏離核定依據之事項；須記錄原因、影響、決策與證據。
補救 | 針對未達標或偏差所採取的矯正與再評估措施；未回收佐證前維持 OPEN。
結案 | 紀錄完整、計算可重現、偏差與改善均有狀態、證據定位清楚，並經有權角色核定關閉。未結事項不得標示完成。
UNKNOWN | 未取得可驗證來源之事項；應列明所需證據，不得以推算、慣例或樣本填補。
SAMPLE／SYNTHETIC | 合成示範值，僅用於展示流程，不具機構制度效力。
2. 依據、輸入與輸出
2.1 作業依據
官方評核表第 2 頁「訓練結果的評估、訓練實施的依據及標準化作業流程（SOP）」。
crosswalk 第 20 行：I04-E04,1,0,0025,訓練評估與實施標準化作業程序SOP。
機構正式之課程核定、評量、門檻、權責與文件管制來源（目前 UNKNOWN，見第 10 節）。
2.2 輸入
### TABLE 4
表 2-A：輸入清冊
輸入ID | 項目 | 說明與狀態
I-01 | 課程目標與對象 | 引用已核定之課程目標與對象（屬 I04-E02 產出；本來源未附 REAL 文件，文件代碼／SHA 為 UNKNOWN）。
I-02 | 期程安排 | 日期、起訖時間、時數、模組數；SAMPLE：SYN-0025-TRAIN-01、2026-05-12、180 分鐘、3 模組。
I-03 | 名冊與報名 | 登記名單與人數；SAMPLE：18 人（SYN-P01–SYN-P18）。REAL 名冊為 UNKNOWN。
I-04 | 教材與資源版次 | 教材、教具、場地與設備之版本；SAMPLE：SYN-MAT-01 v1.0。REAL 版次的 SHA／代碼 UNKNOWN。
I-05 | 評量工具與版本 | 前測、後測、問卷之名稱、版本與編製依據；SAMPLE：SYN-TOOL-PRE v1.0、SYN-TOOL-POST v1.0、SYN-TOOL-SUR v1.0。REAL 工具為 UNKNOWN。
I-06 | 核定門檻與目標 | 機構正式核定之出席、評量、滿意度、補救等門檻。REAL 來源 UNKNOWN；本文件不自行設定 LIVE 門檻，示例值一律標示 SAMPLE。
I-07 | 場地／設備／資料保護措施 | 場地、資訊設備、個資與紀錄保護安排；SAMPLE：SYN-VEN-01、SYN-DP-01。REAL 措施與權責 UNKNOWN。
I-08 | 表單與紀錄格式 | 本文件第 8 節之 FORM A–H；實際機構表單代碼 UNKNOWN，應以機構正式表單替換。
2.3 輸出
### TABLE 5
表 2-B：輸出清冊
輸出ID | 產出 | 內容
O-01 | 期程識別碼 | SYN-0025-TRAIN-01（SAMPLE）
O-02 | 課前就緒檢核表 | FORM B；含符合／不符合／UNKNOWN 與證據位置
O-03 | 實施與偏差紀錄 | FORM D；計畫值／實際值分欄、偏差原因與處置
O-04 | 出席、評量、問卷原始與驗證紀錄 | FORM E；匿名／受控合成 ID、缺漏與無效原因
O-05 | 指標計算與獨立檢查紀錄 | FORM F 計算工作表＋SYN-EV-09 獨立檢查紀錄
O-06 | 判定與決策紀錄 | FORM G；判定結果、決策角色、依據、狀態
O-07 | 改善／補救追蹤 | FORM G 補救列；OPEN／CLOSED 與驗證方式
O-08 | 結案與證據索引 | FORM H；受控位置、識別碼、版次、可得時之 SHA
3. 角色與責任（RACI）
3.1 功能角色定義（非機構真實職稱）
### TABLE 6
表 3-A：功能角色（真實姓名、職銜、代理權與授權來源皆為 UNKNOWN）
角色碼 | 功能角色 | 職掌輪廓（待機構授權文件核實）
FR-01 | 訓練承辦／協調 | 受理期程、彙整依據、協調資源、彙整判定與結案。
FR-02 | 講師／執行者 | 課前準備、依計畫實施、即時記錄出席與偏差、執行補救。
FR-03 | 評估與資料覆核員 | 收集與驗證評估資料、執行公式計算、維護可追溯性。
FR-04 | 決策主管 | 核定判定、核準補救與結案、處理升級事項。
FR-05 | 紀錄保管者 | 受控保存、調閱與證據索引管理。
FR-06 | 獨立計算檢查者 | 與計算者不同人，獨立重算並核對分子分母與判讀。
3.2 RACI（每項活動恰好一個 A，至少一個 R）
### TABLE 7
表 3-B：RACI 責任表（FORM C；代理與授權依據 UNKNOWN）
活動 | R | A | C | I | 代理／授權依據
1. 受理及核對課程依據（建立期程識別碼、凍結依據版本） | FR-01 | FR-04 | FR-03 | FR-02 | UNKNOWN（須機構授權表）
2. 課前就緒確認（角色、場地、教材、名冊、評量、資料保護） | FR-02 | FR-01 | FR-04 | FR-05 | UNKNOWN
3. 依計畫實施與即時偏差記錄 | FR-02 | FR-01 | FR-04 | FR-05 | UNKNOWN
4. 評估資料收集與驗證（版本、母體、有效樣本、缺漏） | FR-03 | FR-01 | FR-02 | FR-04 | UNKNOWN
5. 指標計算（依公式重算並記錄） | FR-03 | FR-04 | FR-01 | FR-06 | UNKNOWN
6. 獨立計算檢查（不同人重算核對） | FR-06 | FR-04 | FR-03 | FR-01 | UNKNOWN（須明定獨立性）
7. 形成判定（依機構核定門檻判讀） | FR-03 | FR-04 | FR-01 | FR-02 | UNKNOWN
8. 改善及補救執行 | FR-02 | FR-01 | FR-03 | FR-04 | UNKNOWN
9. 補救複測與結案提報 | FR-03 | FR-01 | FR-06 | FR-04 | UNKNOWN
10. 結案受控歸檔與可追溯 | FR-05 | FR-04 | FR-01 | FR-03 | UNKNOWN（保存期限依 I04-E05／機構來源）
檢核：上表每一列有且僅有一個 A；每一列至少一個 R。FR-06 與 FR-03 分屬不同人，計算與檢查具獨立性；此為功能設計，非機構事實。若機構要併肩作業，須由機構正式來源另行核定並留存授權證據。
4. 流程總覽與觸發
4.1 觸發
每一個經受理的訓練期程各觸發一次本流程，並建立唯一期程識別碼。實際開課頻率、受理窗口與提前期為 UNKNOWN，須由機構正式排程與權責來源核定。
4.2 階段流程
### TABLE 8
表 4-A：端到端階段與產出
階段 | 階段名稱 | 主要責任 | 關鍵產出 | 進入下一階條件
T1 | 受理及依據凍結 | FR-01／FR-04 | 期程識別碼、依據版本與來源 | 依據齊備；缺核準證據者標 UNKNOWN，不得稱已核定
T2 | 課前就緒 | FR-02／FR-01 | FORM B 就緒檢核 | 全部關鍵項符合，或完成有條件放行／暫停決策
T3 | 開課確認 | FR-02 | 當日出席與環境確認 | 名冊、場地、教材、評量工具就定位
T4 | 實施與偏差記錄 | FR-02 | FORM D 實施與偏差 | 計畫值／實際值分欄完整；偏差即時登錄
T5 | 評估收集與驗證 | FR-03 | FORM E 原始與驗證 | 有效樣本與缺漏原因可回溯
T6 | 計算與覆核 | FR-03／FR-06 | FORM F、SYN-EV-09 | 公式、分子分母、單位一致；獨立重算吻合
T7 | 判定 | FR-04 | 判定結果與依據 | 有核定門檻；否則標「無法判定／UNKNOWN」
T8 | 決策／補救 | FR-04／FR-02 | FORM G 決策與措施 | 措施、責任、期限來源、驗證方式明確
T9 | 複測與結案 | FR-03／FR-01 | 補救結果、結案判定 | 未結事項為 OPEN 不得結案
T10 | 歸檔與可追溯 | FR-05 | FORM H 證據索引 | 位置、識別碼、版次、SHA（可得時）齊備
5. 作業步驟（每一步皆為可操作控制）
步驟 1：受理及核對課程依據
### TABLE 9
項目 | 內容
責任角色 | R：FR-01；A：FR-04；C：FR-03；I：FR-02
輸入 | 課程目標、對象、時數、模組、教材、評量方式與核定證據。
操作 | 建立唯一期程識別碼；逐項核對依據文件的名稱、版本、來源與可讀回識別；將本 SOP 所需之實施基準自 sniffed 來源分離，避免把 SAMPLE 基準當成 REAL 核定。
控制點 | CP-01 依據版本凍結：欄位、版次、SHA 未查得者標 UNKNOWN，不得稱為「已核準」。
輸出／紀錄 | O-01 期程識別碼；FORM A 識別列。
完成條件 | 期程識別碼唯一且所有基準項目有狀態（符合／不符合／UNKNOWN）與證據位置。
失敗／例外分支 | 缺核定證據 → 標 UNKNOWN，照常進行內部準備但不得宣稱正式核定；基準相互衝突 → 提交 FR-04 裁量，必要時暫停受理。
步驟 2：課前就緒
### TABLE 10
項目 | 內容
責任角色 | R：FR-02；A：FR-01；C：FR-04；I：FR-05
輸入 | 核定依據、名冊、教材、場地設備、評量工具、資料保護措施。
操作 | 逐項檢核執行角色、場地／工具、教材、名冊、評量工具及資料保護；記錄符合／不符合／UNKNOWN 與證據位置。
控制點 | CP-02 關鍵資源gate：角色、場地、教材、評量工具任一項不符合即不得無條件開課；須由 FR-04 裁量暫停或升級。
輸出／紀錄 | FORM B 課前就緒檢核表；未解事項清單。
完成條件 | 全部關鍵項「符合」，或完成核定之有條件放行／暫停決策並留跡。
失敗／例外分支 | 不符合 → 改正後復核；無法改正 → 暫停或升級至 FR-04；已知高風險 → 啟動第 7 節安全／個資升級分支。
步驟 3：依計畫實施與即時偏差記錄
### TABLE 11
項目 | 內容
責任角色 | R：FR-02；A：FR-01；C：FR-04；I：FR-05
輸入 | 核定模組、時數、教材版次、名冊、場地與評量工具。
操作 | 開課前確認名冊與環境；實施中記錄實際日期、起訖時間、模組、出席、講師、教材版次；計畫值與實際值分欄保存。
控制點 | CP-03 偏差即時登錄：任何計畫值與實際值不一致須當場或於期限內登原因、影響、決策與證據。
輸出／紀錄 | FORM D 實施與偏差紀錄；出席與/fabric 證據 SYN-EV-03、SYN-EV-04。
完成條件 | 所有模組與時數皆有計畫值／實際值；偏差都有識別碼與處置。
失敗／例外分支 | 偏差影響目標達成 → 通知 FR-01／FR-04，決定續行、調整或暫停；涉及安全／個資 → 直接升級。
步驟 4：評估收集與驗證
### TABLE 12
項目 | 內容
責任角色 | R：FR-03；A：FR-01；C：FR-02；I：FR-04
輸入 | 評量工具版次、母體名冊、原始作答、問卷回收。
操作 | 記錄工具版本、母體、有效樣本數、缺漏與無效值、可回溯性與資料權限；分辨「未出席」「未回覆」「無效作答」。
控制點 | CP-04 可回溯性：分子分母可回至原始資料；不可驗證者標 UNKNOWN，不估算補值。
輸出／紀錄 | FORM E 明細與驗證註記；SYN-EV-04～SYN-EV-07。
完成條件 | 每項指標之母體、有效樣本、缺漏處理皆有明文與證據位置。
失敗／例外分支 | 工具不可比、版本不明、母體不清 → 標 UNKNOWN；必要時補取來源或改期再測。
步驟 5：指標計算與獨立檢查
### TABLE 13
項目 | 內容
責任角色 | 計算 R：FR-03／A：FR-04；獨立檢查 R：FR-06／A：FR-04
輸入 | FORM D、FORM E 之已驗證資料。
操作 | 依第 6 節公式重算；記錄執行者、時間、結果與資料位置；由 FR-06 以不同人身份重算核對。
控制點 | CP-05 計算可重現＋獨立性：分子／分母／單位一致，且計算者與檢查者不同人；不一致即回到步驟 4。
輸出／紀錄 | FORM F 計算工作表；SYN-EV-09 獨立計算檢查紀錄。
完成條件 | 計算與獨立檢查吻合，或差異已解釋並留痕。
失敗／例外分支 | 分母為 0、樣本不完整、工具不可比 → 輸出 UNKNOWN，不得產生數值 PASS。
步驟 6：形成判定
### TABLE 14
項目 | 內容
責任角色 | R：FR-03（擬判）；A：FR-04（核定判定）；C：FR-01；I：FR-02
輸入 | FORM F 指標結果、機構核定門檻與版本。
操作 | 逐項對照核定目標與門檻，記錄判定的依據版本與缺漏處理。
控制點 | CP-06 門檻來源gate：門檻不存在或版本不明時，判定為「無法判定／UNKNOWN」；撰稿者與執行者均不得自設 REAL 門檻。
輸出／紀錄 | 判定結果；FORM G 判定列。
完成條件 | 每項指標有判定（達成／未達成／個別未達／UNKNOWN）與證據。
失敗／例外分支 | 無檻額 → 補取機構核定來源；母體不足 → 補取資料；不得以求平均值或抽樣推斷冒充全員結論。
步驟 7：改善及補救
### TABLE 15
項目 | 內容
責任角色 | R：FR-02；A：FR-01；C：FR-03；I：FR-04
輸入 | 未達標的指標或偏差、決策要求。
操作 | 記錄措施、責任角色、期限來源、驗證方式與預計／實際狀態；補救後安排複測。
控制點 | CP-07 未結不得結案：未回收之補救證據維持 OPEN，直到複測與驗證完成。
輸出／紀錄 | FORM G 補救列；SYN-EV-11 複測紀錄。
完成條件 | 每項未達或偏差有措施、責任、期限來源與驗證方式。
失敗／例外分支 | 補救未完成 → 保持 OPEN 並向 FR-04 報告；涉及重大外溢效果 → 升級。
步驟 8：結案及可追溯
### TABLE 16
項目 | 內容
責任角色 | R：FR-05；A：FR-04；C：FR-01；I：FR-03
輸入 | FORM B–G、所有 SAMPLE／REAL 證據與索引。
操作 | 核對紀錄完整、計算可重現、偏差與改善皆有狀態；記錄受控位置／識別碼／版次／可得時之 SHA。
控制點 | CP-08 結案gate：未結事項 OPEN 不得結案；受控保存、公告與許可權細節引用 I04-E05／機構來源，不在本文件發明。
輸出／紀錄 | FORM H 證據索引；結案判定。
完成條件 | 全部控制項有狀態；證據可定位；結案經 FR-04 核定。
失敗／例外分支 | 證據缺漏 → 回補或標 UNKNOWN；跨文件定位失聯 → 該連結標 UNKNOWN，不以近鄰文件推測。
6. 指標、公式與判讀
### TABLE 17
表 6-A：指標與公式（分子／分母／單位／缺值行為；門檻除標明 SAMPLE 外均為 UNKNOWN）
指標 | 公式（分子 ÷ 分母） | 單位 | 缺值／0 行為 | 門檻與來源
出席率 | 實到人數 ÷ 登記人數 × 100% | % | 登記人數為 0 或名冊不可界 → UNKNOWN；缺席不得視為 0 分。 | SAMPLE 目標 ≥85%；REAL 門檻 UNKNOWN
實施符合度 | 依計畫完成之必備控制項數 ÷ 計畫必備控制項總數 × 100% | % | 總數為 0 或來源不明 → UNKNOWN；不得用估計值充數。 | SAMPLE 目標 100%（3/3）；REAL 門檻 UNKNOWN
前測平均 | 有效前測總分 ÷ 有效前測份數 | 分 | 未測／未出席不入分子分母；有效份數為 0 → UNKNOWN。 | 無門檻（描述性）；REAL 標準 UNKNOWN
後測平均 | 有效後測總分 ÷ 有效後測份數 | 分 | 同上；缺測者不入分母。 | 無群體平均門檻（描述性）；個人後測 80 分為 SAMPLE 個人評量標準，不得套用於平均值；REAL 群體平均目標 UNKNOWN
前後測平均差 | 有效配對後測平均 − 有效配對前測平均 | 百分點（pp） | 僅限同時具有效前後測之配對；配對數為 0 → UNKNOWN。 | 無門檻（描述性）；REAL 標準 UNKNOWN
有效評量通過率 | 達標之有效評量份數 ÷ 有效評量份數 × 100% | % | 依 SAMPLE 個人檻標計；份數為 0 → UNKNOWN；缺席者不入分母。 | SAMPLE 群體目標 ≥85%；REAL 門檻 UNKNOWN
問卷回覆率 | 有效回覆份數 ÷ 符合資格人數 × 100% | % | 符合資格人數為 0 或資格不明 → UNKNOWN；未回覆不列入有效份數。 | SAMPLE 參考 ≥85%；REAL 門檻 UNKNOWN
平均滿意度 | 有效量表總分 ÷ 有效回覆份數 | 分／5 | 有效回覆為 0 → UNKNOWN；單題漏答依工具規定處理，不得自行補值。 | SAMPLE 目標 ≥4.0/5；REAL 門檻 UNKNOWN
補救成功率 | 補救後達標人數 ÷ 完成補救且複測人數 × 100% | % | 完成複測人數為 0 → UNKNOWN；未複測者留在 Open，不入分母。 | SAMPLE 目標 100%；REAL 門檻 UNKNOWN
補救後出席者達標率 | 補救後達標人數 ÷ 原出席人數 × 100% | % | 原出席人數為 0 → UNKNOWN；缺席者不入分母。 | SAMPLE 參考 100%；REAL 門檻 UNKNOWN
判讀通則：（1）先確認指標的母體、工具版本與有效樣本；（2）分母為 0、樣本不完整或工具不可比時，輸出 UNKNOWN，不得產生數值 PASS；（3）任何 REAL 檻額均須有機構核定來源，否則僅能以 SAMPLE 呈現；（4）計算結果與判定分別記錄，並由不同人獨立檢查。
7. 決策、偏差與改善
### TABLE 18
表 7-A：決策與例外分支
分支 | 觸發 | 動作 | 決策角色 | 輸出／狀態
B1 | 資料不足／缺漏／工具不可比 | 暫不判定，補取來源或改正工具 | FR-04 | 判定＝UNKNOWN；補取任務 OPEN
B2 | 實施與核定依據不一致（偏差） | 記偏差，評定影響，依權責處置 | FR-04 | 偏差單；續行／調整／暫停決策
B3 | 安全、個資或重大外部效果疑慮 | 立即升級，必要時停止或移轉 | FR-04 | 升級紀錄；依法令與機構程序處理
B4 | 資料完整且全部達標 | 記錄公式、分子分母與證據 | FR-04 | 判定＝達成；可結案
B5 | 群體目標未達成 | 啟動改善／補救計畫並追蹤 | FR-04 | FORM G；措施 OPEN 直至驗證
B6 | 個體未達（群體仍可能達標） | 個別補救、複測、追蹤 | FR-01 | FORM G；個別OPEN→CLOSED
B7 | 檻額不存在或版本不明 | 不得自設閾值；判定「無法判定／UNKNOWN」 | FR-04 | 待補機構核定來源
偏差處理原則：每一偏差須有偏差ID、原因、影響、決策者與依據、處置與證據；本案例（SYN-0025-TRAIN-01）偏差登錄為 SYN-DEV-01：0 項（無偏差），屬已完成之零事件紀錄，非空白模板。若未來發生偏差，同一表格增列即可。
8. 表單、紀錄與跨文件連結
FORM A（文件／流程識別）見表 0-A；FORM C（角色責任）見表 3-B。以下表單皆以 SYN-0025-TRAIN-01（SAMPLE）填入範例列，均為合成資料。
FORM B：課程依據與課前就緒檢核
### TABLE 19
表 8-B：課前就緒（SAMPLE 例列）
項 | 檢查項 | 證據／識別 | 狀態 | 證據位置 | 未解事項
1 | 課程目標與對象之核定依據 | SYN-EV-01（v1.0） | SAMPLE 符合 | 工作表 §9.1 | REAL 核定文件 UNKNOWN
2 | 名冊與報名 | SYN-EV-04（18 人） | SAMPLE 符合 | FORM E | REAL 名冊 UNKNOWN
3 | 教材與教具版次 | SYN-MAT-01 v1.0 | SAMPLE 符合 | FORM D | REAL 版次 SHA UNKNOWN
4 | 評量工具及版本 | SYN-TOOL-PRE/POST/SUR v1.0 | SAMPLE 符合 | FORM E／F | REAL 工具 UNKNOWN
5 | 場地與設備 | SYN-VEN-01 | SAMPLE 符合 | FORM D | REAL 場地紀錄 UNKNOWN
6 | 資料保護與調閱權限 | SYN-DP-01 | SAMPLE 符合 | SYN-EV-02 | REAL 權限規程 UNKNOWN
7 | 執行與評量角色就位 | SYN-FR-02、SYN-FR-03 | SAMPLE 符合 | SYN-MTG-01 | 真人姓名／授權 UNKNOWN
FORM D：實施與偏差紀錄
### TABLE 20
表 8-D：實施與偏差（SAMPLE 例列）
期程ID | 項目 | 計畫值 | 實際值 | 差異 | 證據 | 偏差／處置
SYN-0025-TRAIN-01 | 模組數 | 3 | 3 | 0 | SYN-EV-03 | SYN-DEV-01：無偏差
SYN-0025-TRAIN-01 | 實施時數（分鐘） | 180 | 180 | 0 | SYN-EV-03 | SYN-DEV-01：無偏差
SYN-0025-TRAIN-01 | 講師 | SYN-FR-02 | SYN-FR-02 | — | SYN-EV-03 | —
SYN-0025-TRAIN-01 | 教材版次 | v1.0 | v1.0 | — | SYN-EV-03 | —
SYN-0025-TRAIN-01 | 出席 | 18 登記 | 16 實到 | 2 缺席 | SYN-EV-04 | 缺席不入評量分母
SYN-0025-TRAIN-01 | 實施符合度 | 3/3 ＝ 100%；180/180 ＝ 100% | SYN-EV-08 | 達 SAMPLE 目標
FORM E：出席與評量明細（SAMPLE，合成身分）
### TABLE 21
表 8-E：18 名學員明細（SYN-P01–SYN-P18；SAMPLE 合成值）
學員ID | 出席 | 前測 | 後測 | SAMPLE 個人檻 80 | 補救／註記
SYN-P01 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P02 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P03 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P04 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P05 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P06 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P07 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P08 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P09 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P10 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P11 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P12 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P13 | 出席 | 60 | 90 | 達標 | 不須補救
SYN-P14 | 出席 | 60 | 91 | 達標 | 不須補救
SYN-P15 | 出席 | 60 | 44 | 未達標 | 2026-05-19 複測 80 → 達標
SYN-P16 | 出席 | 60 | 55 | 未達標 | 2026-05-19 複測 82 → 達標；問卷未回覆
SYN-P17 | 缺席 | — | — | 未評量 | 缺席，不入評量分母
SYN-P18 | 缺席 | — | — | 未評量 | 缺席，不入評量分母
有效前測 16 份（P01–P16）、有效後測 16 份（P01–P16）；P17、P18 缺席，其缺值為真實缺測，不得補值或列入分母。
FORM F：評估結果摘要（公式重算）
### TABLE 22
表 8-F：指標計算與判定（SAMPLE）
指標 | 分子 | 分母 | 公式 | 結果 | 單位 | SAMPLE 檻額／判定
出席率 | 16 | 18 | 16÷18×100% | 88.89 | % | ≥85% → 達成
實施符合度（模組） | 3 | 3 | 3÷3×100% | 100 | % | 100% → 達成
前測平均 | 960 | 16 | 960÷16 | 60 | 分 | 描述性
後測平均 | 1,360 | 16 | 1360÷16 | 85 | 分 | 描述性；個人後測 80 分僅適用個人通過率，不作群體平均門檻；REAL 群體平均目標 UNKNOWN
前後測平均差 | 85−60 | 16 配對 | 後測平均−前測平均 | 25 | pp | 描述性
有效評量通過率（初次） | 14 | 16 | 14÷16×100% | 87.5 | % | ≥85% → 達成
問卷回覆率 | 15 | 16 | 15÷16×100% | 93.75 | % | ≥85% → 達成
平均滿意度 | 66 | 15 | 66÷15 | 4.4 | 分／5 | ≥4.0/5 → 達成
補救成功率 | 2 | 2 | 2÷2×100% | 100 | % | 100% → 達成
補救後出席者達標率 | 16 | 16 | 16÷16×100% | 100 | % | 100% → 達成
分子分母可回至表 8-E；分母為 0 或樣本不完整時該列為 UNKNOWN。SAMPLE 檻額僅示範，不具機構制度效力。
FORM G：決策／改善追蹤
### TABLE 23
表 8-G：決策與補救（SAMPLE 例列）
決策ID | 觸發 | 結果／判定 | 提出／決策 | 措施與期限來源 | 驗證 | 狀態
SYN-DEC-01 | 群體目標 | 87.5% ≥ 85%，群體達成 | SYN-FR-03／SYN-FR-04 | 不取消個別補救 | FORM F | CLOSED
SYN-DEC-02 | P15 後測 44 未達 | 需補救 | SYN-FR-03／SYN-FR-04 | 2026-05-19 重點複習＋複測（SAMPLE 期限） | 複測 80 分 | CLOSED
SYN-DEC-03 | P16 後測 55 未達 | 需補救 | SYN-FR-03／SYN-FR-04 | 2026-05-19 重點複習＋複測（SAMPLE 期限） | 複測 82 分 | CLOSED
SYN-DEC-04 | 結案覆核 | 全部 SAMPLE 目標達成；2 件補救已驗證 | SYN-FR-06／SYN-FR-04 | 2026-05-20 獨立核算並結案 | SYN-EV-09 | CLOSED
FORM H：跨文件／證據索引
### TABLE 24
表 8-H：證據索引與相鄰文件事實連結（不複製同儕正文）
證據ID | 需求／文件 | 識別／位置 | 使用欄位 | 關聯理由／狀態
SYN-EV-01 | I04-E04 課程依據 | SYN-0025-BASIS v1.0 | FORM B1、§9 | SAMPLE；REAL 核定文件 UNKNOWN
SYN-EV-02 | I04-E04 就緒檢核 | SYN-MTG-01 課前會議 | FORM B6/B7 | SAMPLE；會議紀錄為合成
SYN-EV-03 | I04-E04 實施紀錄 | SYN-0025-TRAIN-01 | FORM D | SAMPLE；3 模組、時數、講師、教材
SYN-EV-04 | I04-E04 出席 | SYN-P01–P18 | FORM D／E | SAMPLE；18 登記、16 出席
SYN-EV-05 | I04-E04 前測 | SYN-TOOL-PRE v1.0 | FORM E／F | SAMPLE；16 份
SYN-EV-06 | I04-E04 後測 | SYN-TOOL-POST v1.0 | FORM E／F | SAMPLE；16 份
SYN-EV-07 | I04-E04 問卷 | SYN-TOOL-SUR v1.0 | FORM F | SAMPLE；15 份有效
SYN-EV-08 | I04-E04 計算工作表 | §6、§9 | FORM F | SAMPLE；可重算
SYN-EV-09 | I04-E04 獨立檢查 | SYN-FR-06 | FORM F | SAMPLE；計算者與檢查者不同人
SYN-EV-10 | I04-E04 偏差登記 | SYN-DEV-01 | FORM D | 0 項（無偏差）
SYN-EV-11 | I04-E04 補救複測 | 2026-05-19 | FORM G | SAMPLE；P15＝80、P16＝82
SYN-EV-12 | I04-E04 結案 | SYN-DEC-01–04、SYN-MTG-02 | FORM G | SAMPLE；2026-05-20 結案
SYN-XREF-01 | I04-E01 需求分析 | doc_id／SHA UNKNOWN | I-01 | 僅連結目標來源；不重做需求調查
SYN-XREF-02 | I04-E02 課程設計 | doc_id／SHA UNKNOWN | I-01、I-02 | 僅核對執行基準；不複製教案
SYN-XREF-03 | I04-E03 提供方式（doc_id 0024） | 0024／I04-E03 | FORM D | 僅核對核定方式是否落實並留偏差
SYN-XREF-04 | I04-E05 文件管制（doc_id 0026） | 0026／I04-E05 | §0.3、§10 | 核準／公告／保存制度引用，不另造
SYN-XREF-05 | 官方評核表第 2 頁 | 805386B7…34709 | §0.1、§2.1 | 需求依據
SYN-XREF-06 | crosswalk 第 20 行 | 1F6B4107…6A1AED2 | §0、§2.1 | I04-E04↔0025 綁定
SYN-XREF-07 | Blueprint 第 022 列 | 35480951…E6BB1C | 全文件 | 文類與最低內容要求
9. 完整 SAMPLE／SYNTHETIC 工作案例
9.1 案例敘述（全部合成，非實際辦訓）
SYN-0025-TRAIN-01「資料保護基礎」（SAMPLE）：2026-05-12 實施，計畫 3 個模組、180 分鐘；現場由 SYN-FR-02（SAMPLE 講師）以 SYN-MAT-01 v1.0（SAMPLE 教材）執行，登記 18 人（SYN-P01–SYN-P18，SAMPLE 合成身分），實到 16 人（P01–P16），P17、P18 缺席。課前由 SYN-MTG-01（2026-05-08，SAMPLE 會議）完成就緒檢核。
前測每人 60 分（P01–P16，合計 960、平均 60）。後測 P01–P13 各 90 分、P14 91 分、P15 44 分、P16 55 分，合計 1,360、平均 85，前後測平均差 25 個百分點。以 SAMPLE 個人檻 80 分 計，P01–P14 共 14 人達標，P15、P16 未達，初次通過率 14/16＝87.5%；雖達 SAMPLE 群體目標 ≥85%，但不取消個別補救。
問卷方面，16 名出席者中 15 份有效回覆（SYN-P16 未回覆，SAMPLE），其中 9 份 4 分、6 份 5 分，總分 66，平均 66/15＝4.4/5，回覆率 15/16＝93.75%。2026-05-19 進行補救複測（SAMPLE）：P15 得 80、P16 得 82，2/2 達 SAMPLE 個人檻；原 16 名出席者之達標比例成為 (14+2)/16＝100%。
決策：SYN-DEC-01 群體目標達成；SYN-DEC-02／03 對 P15、P16 個別補救並複測；SYN-DEC-04 由 SYN-FR-06（SAMPLE 獨立檢查者）於 2026-05-20 核算並結案，全程維持 SAMPLE。此案例不構成長期工作績效、訓練移轉或組織成果之證據。
9.2 案例資料重算（可核對）
### TABLE 25
表 9-A：SAMPLE 案例關鍵計算
計算 | 算式 | 結果 | 單位
出席率 | 16 ÷ 18 × 100% | 88.89 | %
實施符合度 | 3 ÷ 3 × 100%（180 ÷ 180） | 100 | %
前測平均 | 960 ÷ 16 | 60 | 分
後測平均 | 1,360 ÷ 16 | 85 | 分
前後測平均差 | 85 − 60 | 25 | pp
初次通過率 | 14 ÷ 16 × 100% | 87.5 | %
問卷回覆率 | 15 ÷ 16 × 100% | 93.75 | %
平均滿意度 | 66 ÷ 15 | 4.4 | 分／5
補救成功率 | 2 ÷ 2 × 100% | 100 | %
補救後達標率 | 16 ÷ 16 × 100% | 100 | %
9.3 決策路徑（與第 7 節分支對應）
### TABLE 26
表 9-B：SAMPLE 決策路徑
階段 | 分支 | 判定／動作 | 證據
計算與覆核 | — | 公式重算完成；FR-06 獨立檢查吻合 | FORM F、SYN-EV-09
判定 | B4（群體達成） | 87.5% ≥ 85%，但保留個別補救 | SYN-DEC-01
判定 | B6（個別未達） | P15、P16 個別補救 | SYN-DEC-02／03
補救 | B6 | 2026-05-19 複測 80／82，OPEN→CLOSED | SYN-EV-11
結案 | B4 | 2026-05-20 核算結案 | SYN-DEC-04、SYN-MTG-02
9.4 合成事實替換清冊（SAMPLE／SYNTHETIC REGISTER）
### TABLE 27
表 9-C：合成值清冊（fact_id、值、使用位置、生成依據、需替換的 REAL 原件）
fact_id | 合成值（含單位／分母） | 使用位置 | 生成／計算依據 | 需替換的 REAL 原件（類型／來源／版次或SHA） | 隱私／責任／驗證
SYN-0025-001 | 課程／期程 SYN-0025-TRAIN-01「資料保護基礎」 | 全文件 | SAMPLE 設計 | 機構課程核定來源；來源／版次／SHA 皆 UNKNOWN | 不涉真人；FR-01 替換；未驗證
SYN-0025-002 | 2026-05-08、2026-05-12、2026-05-19、2026-05-20（日均） | §9、FORM B／G | SAMPLE 設計 | 機構排程、會議與補救紀錄；真實日期 UNKNOWN | FR-01；未驗證
SYN-0025-003 | 18 登記；SYN-P01–P16 出席；P17–P18 缺席 | FORM D／E | SAMPLE 點名設計 | 簽到表／點名紀錄；真實名冊 UNKNOWN | 合成ID 替代真名；FR-05 保管
SYN-0025-004 | 3 模組；180 分鐘；3/3；180/180 | FORM D | SAMPLE 實施設計 | 實施紀錄；真實 module／時數 UNKNOWN | FR-02；未驗證
SYN-0025-005 | SAMPLE 檻：80 分；85%；4.0/5；85% 出席 | §6、FORM F | SAMPLE 檻額設計 | REAL 檻額 UNKNOWN；須機構正式目標文件 | FR-04 核定；未替換
SYN-0025-006 | 前測 16×60＝960；後測 13×90＋91＋44＋55＝1,360 | FORM E／F | SAMPLE 評量設計 | 前測／後測原始作答；真實分數 UNKNOWN | 合成ID；FR-03 保管
SYN-0025-007 | 15 有效回覆；9×4＋6×5＝66；4.4/5；93.75% | FORM F | SAMPLE 問卷設計 | 問卷原始回收；真實回覆 UNKNOWN | 合成ID；FR-03
SYN-0025-008 | 88.89%／100%／60／85／25pp／87.5%／93.75%／4.4／100%／16/16 | §6、§9.2 | 由 003–007 重算 | 計算工作表；真實指標 UNKNOWN | FR-03 計算、FR-06 檢查
SYN-0025-009 | 補救 2026-05-19；P15 80、P16 82；2/2；16/16 | FORM G | SAMPLE 補救設計 | 補救與複測紀錄；真實補救 UNKNOWN | FR-02 執行、FR-03 驗證
SYN-0025-010 | SYN-DEC-01–04；SYN-MTG-01–02；SYN-FR-01–06；2026-05-20 結案 | §8-G／§9 | SAMPLE 決策設計 | 決策紀錄、會議紀錄；真實決策／人員 UNKNOWN | 真人 UNKNOWN；FR-04
SYN-P01–P18 | 18 名合成學員（完整 ID 範圍；逐項明細見表 8-E） | FORM E | SAMPLE 身分設計 | 真實名冊（須依個資規定處理）；未取得 | 以合成ID 去識別化
SYN-FR-01–06 | 6 個功能角色（完整代號範圍；職責見表 3-A） | 全文件 | SAMPLE 功能設計 | 機構職掌／授權文件；真名 UNKNOWN | 真人 UNKNOWN；FR-04 指派
SYN-MTG-01–02 | 課前就緒 2026-05-08；結案 2026-05-20 | FORM B／G | SAMPLE 會議設計 | 會議紀錄；真實會議 UNKNOWN | FR-01；未驗證
SYN-EV-01–12 | 12 項 SAMPLE 文件／紀錄識別（完整代號範圍） | FORM H | SAMPLE 文件設計 | 實際憑證／表單；未取得 | FR-05 保管
SYN-DEV-01 | 偏差事件 0 項（無偏差） | FORM D | SAMPLE 實施結果 | 偏差登錄；若未來有偏差須補 | FR-01；已記錄
SYN-TOOL-01–03 | SYN-TOOL-PRE／POST／SUR v1.0 | FORM B／E／F | SAMPLE 工具設計 | 實際評量工具與版次；未取得 | FR-03；未驗證
替換原則：上列每一合成值在納入 REAL 文件時，均須由對應責任角色以機構正式來源替換並重新驗算；REAL 來源位置、版次與 SHA 未取得前維持 UNKNOWN。清冊與本文一對一可追溯，未有孤立合成值。
9.5 案例宣告
本案例為 SAMPLE／SYNTHETIC，僅演示 SOP 步驟、公式、分支與表單之操作方式。不得解讀為該機構曾舉辦「資料保護基礎」課程、曾收取任何費用、曾獲得任何成績、滿意度、決策、核可或成果；亦不得據以主張協會、政府或第三方之核準或認可。
10. 限制、UNKNOWN 待解事項與文件狀態
10.1 限制
本文件為 CANDIDATE，尚未經機構任何程序核準、公告或生效；不得標示為 REAL、APPROVED、EFFECTIVE 或 CURRENT。
所有 SAMPLE 值不具制度效力；SAMPLE 檻額（80 分、85%、4.0/5、85%）僅為示範，不是 LIVE 規則。
若受篇幅或來源限制而無法取得機構門檻、授權或保存制度，一律標 UNKNOWN，不得以慣例、產業標準或一般最佳實務冒充答案。
本 SOP 不管轄長期工作績效、訓練移轉或組織成果；相關結論須另有來源與量測工具。
I04-E05 之文件核準、公告、版控、保存期限與銷毀程序，不在本文件重複建制，僅交叉連結。
10.2 UNKNOWN 待解事項與所需證據
### TABLE 28
表 10-A：未知事項與待取來源
未知事項 | 現狀 | 解決所需證據
機構正式文件代碼、版次、生效日 | 候選代碼 TTQS-I04-E04-SOP-0025；餘 UNKNOWN | 機構文件管制清單／受控文件目錄與核準紀錄
撰寫、覆核、核準人員與簽核層級 | 功能角色 FR-01–FR-06；真人 UNKNOWN | 機構組織規程、職務代理人表、授權與核決權限表
課程核定依據（目標、時數、教材、評量） | SAMPLE；REAL UNKNOWN | 核定之課程計畫／教學計畫與核定紀錄
各項門檻與目標（出席、評量、滿意度、補救） | 僅 SAMPLE 示範 | 機構正式教育訓練目標與評核標準之核定影本
實施與評估之 REAL 資料 | SAMPLE 案例 | 點名／簽到、原始作答、問卷回收、計算工作表
保存期限、調閱權限與銷毀程序 | UNKNOWN | 機構保存年限表、個資管理規程（並參 I04-E05／doc_id 0026）
實際開課頻率與受理窗口 | UNKNOWN | 機構年度訓練排程與受理規定
升級、停課與補救期限之權責 | UNKNOWN | 機構事故／偏差處理與核準權限規定
外部核準、認可、證明或成效 | 未取得；不得聲稱 | 如有，須提供可驗證之第三方正本（本文件不主動推定）
10.3 文件狀態
最終狀態：CANDIDATE／未核準／未公告／未生效。本文件實現 I04-E04 官方摘錄與 Blueprint 第 022 列之必要性：來源定位、角色、流程分支、控制點、表單、公式、判讀、決策與跨文件連結均以可操作形式呈現；案例為完整一致的 SAMPLE／SYNTHETIC。任何修改都必須重算本文件 SHA 並重新執行對應之技術檢查與獨立語意審查。本文件不構成批準、接受、生效、採用或 REAL 績效之主張。
