# W1 bounded review packet
work_id: TTQS_ONE_0026_I04-E05_W1_SEMANTIC_REVIEW_R12_20261118
role: independent semantic and usability reviewer; read-only
candidate_path: E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0026_R12_REPAIR_20261118\candidate\0026_I04-E05_CANDIDATE_R12.docx
candidate_sha256: 56E4449F06C8CF0D4DC13579A386EEEA88E59A8403FF9C1E1EF036FDCAAC7491
source_packet_sha256: 6E8A1BEF2F63D098FCC446DE275724D95FBF4F1D326DE52F8059070CCD91E110
unique_blueprint_sha256: FA02A9846E50C46815220AEF2888E5A45518CFAFC21B0DECBBC8C6542E247876
official_source_pdf_sha256: 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709
requested_model_route: opencode/big-pickle (free route from local OpenCode model catalog)
provider_served_model: UNKNOWN unless the response proves it
scope: assess exact candidate against official I04-E04 source, blueprint and prior five scoped findings. Do not perform visual review; 27-page visual inspection is tracked separately. Do not edit files, run commands, call tools, or claim formal acceptance. Return JSON only with exact candidate SHA, verdict, checks, findings (severity/location/evidence/required repair), served model if explicitly exposed else UNKNOWN, and no promotion authority. Candidate is SAMPLE/SYNTHETIC; no real person records are included.

## Prior R11 W1 review (source of the five repair findings)
{"work_id":"TTQS_ONE_0026_I04-E05_W1_SEMANTIC_REVIEW_R11_20261117","candidate_docx_sha256":"9cc64931396acd3c674bcba3d11bfb504918c1b0105dc12cb93734b2991f7625","source_packet_sha256":"6e8a1bef2f63d098fcc446de275724d95fbf4f1d326de52f8059070ccd91e110","blueprint_sha256":"fa02a9846e50c46815220aef2888e5a45518cfafc21b0decbbc8c6542e247876","verdict":"PASS","checks":{"source_fit":"PASS","genre_mechanics":"PASS","scope_negative_neighbors":"PASS","authority_state_boundaries":"PASS","synthetic_truth_and_coherence":"PASS","functional_usability":"PASS","internal_consistency":"PASS","exact_sha_binding":"PASS"},"findings":[{"id":"F-001","severity":"minor","location":"7.3 節「應簽收對象總數（含…兼任專案顧問 7 人）」；表單二 ST-021/ST-022/ST-026 列","evidence":"7.3 列「兼任專案顧問 7 人」，但表單二僅 3 名兼任顧問（趙/錢/李顧問，ST-021/022/026）；應簽收總數 28 人仍一致。","required_repair":"對齊 7.3 分類與表單二職稱人數，或明確定義「兼任專案顧問」之涵蓋對象。"},{"id":"F-002","severity":"minor","location":"表一序號 2、16、17「示範保存期限」欄","evidence":"序號 2 TTQS-SOP-ADM-001（CANDIDATE）填「5年」；序號 16/17（同為 CANDIDATE）填「UNKNOWN（正式保存期限須依真實權責確認）」，候選件保存期限處理不一致。","required_repair":"所有 CANDIDATE 件一致標示保存期限 UNKNOWN，或一致套用 4.9 示範年限並加註「候選示範」。"},{"id":"F-003","severity":"minor","location":"封面版次行；表一序號 2；表單五 SMP-03","evidence":"封面「版次：V1.0-CANDIDATE」；表一序號 2「現行版次 V1.0」；表單五 SMP-03「V1.0-CANDIDATE」，版次標籤格式不一致。","required_repair":"統一版次欄格式（版號與狀態分欄，或全面加註 -CANDIDATE）。"},{"id":"F-004","severity":"minor","location":"封面「最新生效日」行；表單六 TR-07；對比 2.5 節狀態定義","evidence":"封面「（當前標記：PENDING_APPROVAL / CANDIDATE）」與表單六 TR-07「候選註記：PENDING_APPROVAL」將工程候選同時掛「待核准」；2.5 定義 PENDING_APPROVAL 為「跨部門審查已通過，正送權責主管簽署」，與 CANDIDATE（未送審）未清楚分離。","required_repair":"統一為 CANDIDATE（或 DRAFT），移除 PENDING_APPROVAL 標記。"},{"id":"F-005","severity":"minor","location":"synthetic_fact_register FACT-0026-024；對比 6.2 Plan 與表一","evidence":"FACT-0026-024 值為「14 件 CURRENT；總清冊 15 筆，排除 1 件 CANDIDATE」；候選文件 6.2 與表一為「14 件 CURRENT、3 件 CANDIDATE（合計 17 筆）」。候選文件本身一致，屬登記表側口徑不符。","required_repair":"更正 FACT-0026-024 為 17 筆／3 件 CANDIDATE，或說明 15 筆口徑。"}],"human_gate":"NONE","review_scope":"Semantic/usability review of exact candidate DOCX SHA 9cc64931396acd3c674bcba3d11bfb504918c1b0105dc12cb93734b2991f7625 only, against official source I04-E05 and the Unique Blueprint; no visual re-review, no formal acceptance, no REAL replacement or Human Gate determination."}

## Existing exact source packet
# 0026 I04-E05 來源包 R01

PROJECT_ID=TTQS_ONE
WORK_ID=TTQS_ONE_0026_I04-E05_SOURCE_PREP_R01_20261116
DOC_ID=0026
REQUIREMENT=I04-E05

## 官方來源定位

- 正式來源：OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf，第 2 頁；檔案 SHA-256：805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709。
- 第 2 頁文字讀回 SHA-256：3c295e8861ad7775a78583e9111df61ac8733a7cf40d771f942363f00572de9c。
- 官方要求：訓練品質管理的系統化文件資訊；展示訓練機構如何運作 TTQS 管理系統，以及文件如何核准、公告、更新、保存紀錄。
- 官方列示的同項佐證包括：訓練需求定期調查與分析、不同訓練課程設計方向、訓練提供方式選擇、訓練結果評估及實施 SOP、以及本件系統運作與文件控制證明。

## 正式交叉對照

- Crosswalk 檔案 SHA-256：1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679。
- 對應列：{'requirement_id': 'I04-E05', 'deliverable_count': '1', 'split_extra_count': '0', 'deliverable_ids': '0026', 'document_titles': '機構如何運作TTQS管理系統及如何核准、公告_可直接使用成品'}
- 142 個歷史交付序號中，此項對應 0026；本項與 0025（單件課程評估與實施 SOP）分離。
- 鄰近文件只作負向範圍界線，不得複製正文：[{'requirement_id': 'I04-E01', 'deliverable_count': '1', 'split_extra_count': '0', 'deliverable_ids': '0022', 'document_titles': '訓練需求的定期調查與分析_分析報告'}, {'requirement_id': 'I04-E02', 'deliverable_count': '1', 'split_extra_count': '0', 'deliverable_ids': '0023', 'document_titles': '不同訓練課程的設計與規劃方向_制度文件'}, {'requirement_id': 'I04-E03', 'deliverable_count': '1', 'split_extra_count': '0', 'deliverable_ids': '0024', 'document_titles': '訓練的提供方式及選擇的指標_制度文件'}, {'requirement_id': 'I04-E04', 'deliverable_count': '1', 'split_extra_count': '0', 'deliverable_ids': '0025', 'document_titles': '訓練評估與實施標準化作業程序SOP'}]

## 157 Blueprint 精確具名需求

- Master Blueprint SHA-256：ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216。
- 專屬需求列：023｜**TTQS 文件批准/公告/保存：授權分層、修訂紀錄與版控**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

## 官方第 2 頁原始文字讀回

 
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

## R12 執行規格來源

- PR92_R12_EXECUTION_SPEC_R12_20261026.md SHA-256：8385bb2d33cb8497cc0864625d1da57b96536014b134ced1e7f9b1b05225d23e；此為相容施工契約，不改變以上官方來源。

## 事實邊界與狀態

本機無可信任的協會實際核准、公告、修訂或保存原件可支持此範例為真實紀錄。所有流程日期、人名、角色指派、文件版本、公告管道、簽收、稽核結果與保存期限只能標記 SAMPLE/SYNTHETIC。不得聲稱協會已採行、主管已實際核准或第三方已查驗。正式生效與 REAL 替換另依 Human Gate。


## Unique Blueprint
# 0026 I04-E05 專屬 Blueprint R01

## 文件目的與文類

建立一份專屬「TTQS 管理系統運作與受控文件生命週期作業規範」，直接回答官方第 2 頁 I04 第 4 項：系統如何運作、文件如何核准/公告/更新/保存。包含操作 SOP、權責矩陣、受控文件台帳、公告簽收、修訂/作廢/保存流程、檢索與定期檢查，以及一組完整 SAMPLE/SYNTHETIC 走讀。文件為候選制度文件，不宣稱已核准或生效。

## 範圍與負向近鄰

- 納入：治理責任、TTQS PDRO/自我檢查連結、文件需求至草案/審查/核准/發布/公告/取得/更新/作廢/封存/檢索的閉環；權限、版控、公告及收據留存；例外與回復；可操作表單及完整示例。
- 不重做 0022 需求調查分析、0023 課程設計方向、0024 訓練提供方式評分、0025 單件課程評估/實施 SOP。僅引用文件 ID 或通用交接，不複製其正文。
- 不把候選文件說成實際核准、公告、稽核或協會採用證據。

## 必須交付的章節機制

1. 封面、候選/合成資料聲明、官方需求定位與本文件使用界線。
2. 目的、適用範圍、名詞、控制原則及文件層級/識別規則。
3. 權責與授權矩陣：起草、內容審查、品質/法遵審查（適用時）、核准、管制/發布、使用者；缺少實際姓名/授權時狀態 UNKNOWN。
4. 受控文件生命週期決策流程：需求→分類/敏感級別→起草→審查→核准→版次/生效判定→公告與取用→訓練/簽收（適用時）→定期審查→修訂/緊急修訂/拒絕→舊版撤回→封存→保存/處置→檢索測試。
5. 版號/狀態/生效日規則，未核准草案不得標 CURRENT；紙本/數位受控副本識別及離線版本處理。
6. 公告與簽收：公告對象/管道/截止、送達失敗/未讀/逾期升級、歷程記錄。不能用假簽收。
7. 分類、存取最小權限、備份、查找、保存與處置。沒有正式法定期限來源時，只能給示範性 SAMPLE 期間並要求核實，不得稱法規期限。
8. 例外處理、風險、PDRO 自我檢查與持續改善指標，寫清分子/分母/排除和未知值，不以未知視為通過。
9. 至少一個完整 SAMPLE/SYNTHETIC 文件修訂走讀，含核准（僅虛構角色）、公告、簽收、舊版封存、檢索及可追溯記錄。
10. 可直接複製使用的已填範例表單/台帳與替換清冊，無空白表單交差；所有示例資料需對應 Synthetic Fact IDs。

## 需達成的文件品質

- 一般正文至少 10.5 pt、表格至少 9.5 pt；Word 原生可開啟。
- 明確標示 CANDIDATE / SAMPLE/SYNTHETIC，不冒充正式制度或組織真實績效。
- 確定性核對每個流程時間線、版號、狀態轉換、簽收/通知數、比率/分母一致。
- 不採用同儕文件正文作模板；僅共用官方來源、交叉對照與合成事實 ID。


## Official source page 2 readback
 
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

## R12 synthetic fact register
fact_id,value,use_location,status
FACT-0026-001,臺灣卓越培訓發展協會（示範虛擬機構）,"document_markdown 1.1節, 1.2節, 表單六",SAMPLE_SYNTHETIC
FACT-0026-002,鄭博元（示範最高管理代表 / 執行長）,"document_markdown 3.2節, 7.2節, 表單二, 表單三",SAMPLE_SYNTHETIC
FACT-0026-003,林志榮（示範品質管理代表 / 品保處主管）,"document_markdown 3.2節, 7.2節, 表單一, 表單三",SAMPLE_SYNTHETIC
FACT-0026-004,陳雅婷（示範訓練教務專案副理 / 業務主管）,"document_markdown 3.2節, 7.2節, 表單二, 表單三",SAMPLE_SYNTHETIC
FACT-0026-005,張淑芳（示範文件管制專員 / 文管人員）,"document_markdown 3.2節, 7.2節, 7.4節, 表單一, 表單二, 表單四; 表單五 P251; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-006,吳宗翰（示範內部稽核員 / 查驗人員）,"document_markdown 3.2節, 7.2節, 7.5節, 表單三, 表單四, 表單五; 表單五 P250/P251; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-007,TTQS-SOP-QA-002,"document_markdown 7.1節, 7.2節, 表單一, 表單三, 表單四, 表單五",SAMPLE_SYNTHETIC
FACT-0026-008,TTQS 內部品質稽核作業規範,"document_markdown 7.1節, 7.2節, 表單一, 表單三",SAMPLE_SYNTHETIC
FACT-0026-009,V1.2,"document_markdown 7.1節, 7.2節, 7.4節, 表單三, 表單四",SAMPLE_SYNTHETIC
FACT-0026-010,V2.0,"document_markdown 7.1節, 7.2節, 表單一, 表單二, 表單三, 表單五",SAMPLE_SYNTHETIC
FACT-0026-011,2026-10-05 09:30,"document_markdown 7.2節 步驟1, 表單三",SAMPLE_SYNTHETIC
FACT-0026-012,2026-10-08 14:00,document_markdown 7.2節 步驟3,SAMPLE_SYNTHETIC
FACT-0026-013,2026-10-11 16:30：TOP 知會備查（非核准）,"document_markdown 7.2步驟5, 表單三; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-014,2026-10-12 09:00,"document_markdown 7.2節 步驟6, 7.3節, 表單二",SAMPLE_SYNTHETIC
FACT-0026-015,2026-10-16 00:00,"document_markdown 7.2節 步驟9, 表單一",SAMPLE_SYNTHETIC
FACT-0026-016,28 人,"document_markdown 6.2節, 7.3節, 表單二; 表單五 T8R2; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-017,25 人,"document_markdown 7.3節, 表單二",SAMPLE_SYNTHETIC
FACT-0026-018,3 人,"document_markdown 7.3節, 表單二",SAMPLE_SYNTHETIC
FACT-0026-019,28 人,"document_markdown 6.2節, 7.3節, 表單二; 表單五 T8R2; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-020,100.0%,"document_markdown 6.2節, 7.3節, 表單二",SAMPLE_SYNTHETIC
FACT-0026-021,12 份列管副本：8 份紙本 + 4 份離線 USB,"document_markdown 6.2, 7.4, 表單四; SAMPLE/SYNTHETIC; 表單四 T7R1-R3/P245; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-022,12 份中 8 份紙本回收、4 份 USB 重新連線回讀後處理,"document_markdown 6.2, 7.4, 表單四; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-023,100.0%（僅在 12/12 回收或連線憑證／版次回讀證據齊備時）,"document_markdown 6.2, 7.4, 表單四; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-024,14 件 CURRENT；總清冊 17 筆；3 件 CANDIDATE（與文件表一及 6.2 一致）,"document_markdown 5.1, 6.2 Plan denominator; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-025,UNKNOWN（納管分子、CURRENT 第二／三階母數、屆期審查母數均待逐件證據）,document_markdown 6.2 Plan/Design/Review; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-026,UNKNOWN（不推估未有證據支持的合格率）,document_markdown 6.2 Plan/Design/Review; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-027,4 件 CURRENT 文件,document_markdown 6.2 Outcome and 7.5 SMP-01/02/04/05; SAMPLE/SYNTHETIC; 表單五 T8R1-R5; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-028,4/4 件 CURRENT 抽樣通過示範檢索／版次核對,document_markdown 6.2 Outcome and 7.5; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-029,100.0%（4/4 CURRENT；僅示範數據）,document_markdown 6.2 Outcome and 7.5; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-030,5.60 分鐘（CURRENT 四件平均 22.4 ÷ 4）,document_markdown 6.2 and 7.5; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-031,15 分鐘,"document_markdown 4.10節, 6.2節, 7.5節; 表單五 P256; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-032,3 年,"document_markdown 4.9節, 表單一",SAMPLE_SYNTHETIC
FACT-0026-033,5 年,"document_markdown 4.9節, 表單一",SAMPLE_SYNTHETIC
FACT-0026-034,永久保存,"document_markdown 4.9節, 表單一",SAMPLE_SYNTHETIC
FACT-0026-035,ARCH-2026-QA-002,"document_markdown 7.4節, 表單四; 表單四 T7R1; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-036,2026-10-14 09:00（公告後 48 小時提醒）,"document_markdown 7.2步驟7, 7.3, 表單二; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-037,2026-10-15 12:00（第三工作日未簽收主管升級）,"document_markdown 4.4, 7.2步驟8, 7.3, 表單二; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-038,2026-10-16 15:30（4 份離線 USB 重新連線後回讀憑證／版次狀態）,"document_markdown 7.4, 表單四; SAMPLE/SYNTHETIC; 表單四 P241/T7R3; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-039,5/5 檢索機制與標籤識別演練；其中 1 件 CANDIDATE 不計入 CURRENT 合規率,document_markdown 7.5; SAMPLE/SYNTHETIC; 表單五 P253-T8R5; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-040,22.4 分鐘 CURRENT 四件耗時合計（4.2 + 6.5 + 7.8 + 3.9）,"document_markdown 6.2, 7.5; SAMPLE/SYNTHETIC",SAMPLE_SYNTHETIC
FACT-0026-041,TTQS-REC-ADM-003（候選表單編號；非 REAL 登錄）,表單一 T4R16; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-042,TTQS-REC-ADM-004（候選表單編號；非 REAL 登錄）,表單一 T4R17; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-043,WDL-2026-009（示範撤回紀錄單號）,表單四 P240; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-044,2026-10-16（示範撤回日期）,表單四 P241; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-045,8 份實體紙本（CP-01 1份 + CP-02~08 7份）,表單四 T7R1-R2; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-046,12 份副本總數（8份紙本 + 4份離線媒體）,表單四 P245/T7R1-R3; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-047,12/12 份收回，撤回率 100.0%，遺失/外流 0 份（示範結論）,表單四 P245; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-048,2031-10-16（示範封存期限；實際保存年限 UNKNOWN）,表單四 P245; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-049,AUD-RET-2026-Q4（示範調閱測試編號）,表單五 P248; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-050,2026-10-20 10:30–11:30（示範測試期間）,表單五 P249; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-051,2 名現場教務專員配合測試（示範人數）,表單五 P251; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-052,5 件抽測文件：4件 CURRENT + 1件 CANDIDATE；候選僅核對檢索及標籤,表單五 P253-P255/T8R1-R5; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-053,5/5 件調出且指定版次/狀態標籤相符，檢索及標籤核對率 100.0%（非 CURRENT 合規率）,表單五 P255; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-054,五件調閱耗時：252、390、306、468、234 秒,表單五 P256; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-055,"耗時合計 1,650 秒 = 27.5 分鐘（示範值）",表單五 P256; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-056,平均調閱 5.50 分鐘（27.5 ÷ 5；示範值）,表單五 P256; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
FACT-0026-057,示範結論僅限 5 件依指定版次與標籤規則完成調閱，不代表真實 TTQS 符合性,表單五 P257-P258; SAMPLE/SYNTHETIC,SAMPLE_SYNTHETIC
