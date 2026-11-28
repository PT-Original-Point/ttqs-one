# Bounded independent semantic review — 0026 R03

PROJECT_ID=TTQS_ONE
WORK_ID=TTQS_ONE_0026_I04-E05_R03_EXACT_SHA_INDEPENDENT_SEMANTIC_W1_20261124
DOC_ID=0026
REQUIREMENT_ID=I04-E05
ROLE=W1 OpenCode v2 CLI independent semantic reviewer; text-only
REQUESTED_ROUTE=opencode/hy4-flash-free
CANDIDATE_SHA256=bdf30057cf9327b2cb10e72458c6d0d95727e48323c14eeb6ad9fd814c5b6692
CANDIDATE_BYTES=73412
SOURCE_PACKET_SHA256=6e8a1bef2f63d098fcc446de275724d95fbf4f1d326de52f8059070ccd91e110
UNIQUE_BLUEPRINT_SHA256=fa02a9846e50c46815220aef2888e5a45518cfafc21b0decbbc8c6542e247876

## Instructions
Review the complete R03 candidate body below against the authoritative source packet and unique blueprint. Return PASS/PARTIAL/FAIL; list only material blockers with precise section/table locators and brief evidence. Check operational usability, authority boundaries, lifecycle states/dates, arithmetic, replacement register, requirement coverage, and SAMPLE/REAL truth boundary. No edits, tools, visual review, or assumptions of real approval. The actual serving model must remain UNKNOWN unless provider evidence proves it. Echo the exact candidate SHA in your response.

R02 exact-SHA review found two blockers; independently verify these repairs and inspect the whole document for residual material blockers:
- §18.3 version/effective determination moved from 2026-10-08 to 2026-10-05, before the 2026-10-05 announcement. Confirm this lifecycle is coherent with 2026-10-12 effectiveness and the governing source/blueprint.
- Timeline status on 2026-10-05 changed from CURRENT to APPROVED; 2026-10-12 remains the effective date and CURRENT transition. Confirm the document never represents a not-yet-effective version as CURRENT.

Nonblocking style observations from R02 are not grounds for a rebuild unless they materially violate the existing quality contract.

## Authoritative source packet

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

## Complete candidate body in document order

0026 TTQS 管理系統運作與受控文件生命週期作業規範
候選制度文件 / CANDIDATE DOCUMENT（SAMPLE/SYNTHETIC）
Render note（DOCX）：一般正文最小 10.5 pt；表格文字最小 9.5 pt；本檔為 Markdown，轉製 DOCX 時請套用上述字級。
0. 封面與文件控制摘要
[TABLE_ROW 0] 項目 || 內容 || 狀態 / 來源
[TABLE_ROW 1] 文件編號 || TTQS-DC-0026（SF-003） || 候選文件代碼
[TABLE_ROW 2] 官方交付序號 || 0026（SF-004） || 官方 Crosswalk
[TABLE_ROW 3] 需求代碼 || I04-E05（SF-005） || 官方來源第 2 頁
[TABLE_ROW 4] 文件標題 || TTQS 管理系統運作與受控文件生命週期作業規範（SF-006） || 本文件
[TABLE_ROW 5] 候選版次 || 0.1-CANDIDATE（SF-007） || 本文件
[TABLE_ROW 6] 候選狀態 || CANDIDATE / 未核准 / 未生效（SF-008） || 本文件
[TABLE_ROW 7] 樣本文件實例 || TTQS-DC-0026-S01（SF-009） || 合成樣本
[TABLE_ROW 8] 樣本版次 || 1.0（SAMPLE）（SF-010） || 合成樣本
[TABLE_ROW 9] 樣本狀態 || APPROVED-SAMPLE / EFFECTIVE-SAMPLE（虛構角色核准）（SF-011） || 合成樣本
[TABLE_ROW 10] 樣本生效日 || 2026-10-12（SF-012） || 合成樣本
[TABLE_ROW 11] 機密等級 || Internal-Confidential（Level 2）（SF-013） || 本文件
[TABLE_ROW 12] 文件負責人 || ROLE-DOC-001 王示例（SAMPLE PERSON）（SF-020 / SF-021） || 合成樣本
[TABLE_ROW 13] 核准人 || UNKNOWN：目前無實際核准紀錄；走讀中之核准者為 ROLE-GM-001 陳示例（SAMPLE） || 狀態明示
[TABLE_ROW 14] 保存期間（樣本） || 5 年，至 2031-10-12（SF-014 / SF-015） || 合成樣本；需核實
[TABLE_ROW 15] 來源包 SHA-256 || 6e8a1bef2f63d098fcc446de275724d95fbf4f1d326de52f8059070ccd91e110 || DISPATCH_PACKET
[TABLE_ROW 16] 唯一 Blueprint SHA-256 || fa02a9846e50c46815220aef2888e5a45518cfafc21b0decbbc8c6542e247876 || DISPATCH_PACKET
1. 候選 / 合成資料聲明與使用界線
1.1 候選文件聲明
本文件為候選制度文件，目的是提供 TTQS 管理系統運作與受控文件生命週期之可操作規範。
本文件目前 不是 已核准、已公告、已生效或已被稽核採用的正式制度。
本文件中的任何「核准、公告、簽收、稽核、保存、證據」描述，除非明確標示為官方來源事實，否則均為 SAMPLE/SYNTHETIC 走讀。
實際採用前，必須由組織以 Human Gate 完成：文件審查、角色授權確認、版本核准、公告、訓練/簽收、保存設定與證據留存。
1.2 合成資料聲明
所有姓名、角色指派、日期、版本、公告管道、簽收紀錄、稽核結果、保存期限、指標結果均為 SAMPLE/SYNTHETIC。
所有合成資料均列入本檔末尾「Synthetic Fact Register (CSV-style)」，並可透過 SF-ID 交叉比對。
不得以本文件中的合成資料作為真實組織績效、真實核准或第三方查驗證據。
本文件不包含真實簽名、實際核准紀錄、第三方原件或認證聲明。
1.3 負向範圍界線
本文件不重製或取代下列鄰近交付文件正文，僅引用文件 ID 或通用交接：
[TABLE_ROW 0] 鄰近文件 || 文件 ID || 本文件處理方式
[TABLE_ROW 1] 訓練需求的定期調查與分析 || 0022 || 僅引用為需求輸入來源；不複製分析正文
[TABLE_ROW 2] 不同訓練課程的設計與規劃方向 || 0023 || 僅引用為課程設計輸入；不複製規劃正文
[TABLE_ROW 3] 訓練的提供方式及選擇的指標 || 0024 || 僅引用為提供方式輸入；不複製評分正文
[TABLE_ROW 4] 訓練評估與實施 SOP || 0025 || 僅引用為評估/實施 SOP 介面；不複製 SOP 正文
本文件只處理 I04-E05：TTQS 管理系統如何運作，以及文件如何核准、公告、更新、保存紀錄。
2. 官方需求定位與來源引用
2.1 官方來源定位
[TABLE_ROW 0] 來源項目 || 內容
[TABLE_ROW 1] 正式來源 || OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf，第 2 頁
[TABLE_ROW 2] 檔案 SHA-256 || 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709（SF-094）
[TABLE_ROW 3] 第 2 頁文字讀回 SHA-256 || 3c295e8861ad7775a78583e9111df61ac8733a7cf40d771f942363f00572de9c（SF-095）
[TABLE_ROW 4] Crosswalk SHA-256 || 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679（SF-096）
[TABLE_ROW 5] Master Blueprint SHA-256 || ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216（SF-097）
[TABLE_ROW 6] Dispatch Packet SHA-256 || 6e8a1bef2f63d098fcc446de275724d95fbf4f1d326de52f8059070ccd91e110（SF-098）
[TABLE_ROW 7] Unique Blueprint SHA-256 || fa02a9846e50c46815220aef2888e5a45518cfafc21b0decbbc8c6542e247876（SF-099）
[TABLE_ROW 8] R12 執行規格 SHA-256 || 8385bb2d33cb8497cc0864625d1da57b96536014b134ced1e7f9b1b05225d23e（SF-100）
2.2 官方要求摘要（來源事实）
官方第 2 頁 I04-E05 要求展示：訓練品質管理的系統化文件資訊；展示訓練機構如何運作 TTQS 管理系統；展示此文件如何核准、公告、更新、保存紀錄。同項佐證包括：訓練需求的定期調查與分析、不同訓練課程的設計與規劃方向、訓練的提供方式及選擇的指標、訓練結果的評估與訓練實施的依據及標準化作業流程（SOP）、機構如何運作 TTQS 管理系統及如何核准、公告、更新、保存紀錄的證明資料。
2.3 交付對應
[TABLE_ROW 0] 官方項目 || 交付序號 || 文件名稱 || 本文件責任
[TABLE_ROW 1] I04-E05 || 0026 || 機構如何運作 TTQS 管理系統及如何核准、公告（可直接使用成品） || 本文件
[TABLE_ROW 2] I04-E01 || 0022 || 訓練需求的定期調查與分析 || 僅引用
[TABLE_ROW 3] I04-E02 || 0023 || 不同訓練課程的設計與規劃方向 || 僅引用
[TABLE_ROW 4] I04-E03 || 0024 || 訓練的提供方式及選擇的指標 || 僅引用
[TABLE_ROW 5] I04-E04 || 0025 || 訓練評估與實施 SOP || 僅引用
3. 目的
建立 TTQS 管理系統中文件控制、核准、公告、更新、保存、檢索、作廢與封存的單一作業規範。
使訓練機構能展示 TTQS 管理系統如何運作，而不只是提供零散文件。
使文件生命週期每一階段都有明確輸入、輸出、責任、紀錄、版本與例外路徑。
提供可直接複製使用的已填範例表單、台帳、走讀與替換清冊。
將官方要求、候選文件狀態與合成樣本資料清楚分離，避免誤用。
4. 適用範圍
4.1 納入範圍
TTQS 管理系統相關受控文件：政策、手冊、程序、SOP、表單、紀錄、訓練教材、評估工具、公告文件。
文件需求、分類、敏感級別、起草、審查、核准、版次、生效日、公告、取用、訓練/簽收、定期審查、修訂、緊急修訂、拒絕、舊版撤回、封存、保存/處置、檢索測試。
文件權限、存取、備份、稽核軌跡、例外處理與 PDRO 自我檢查。
4.2 排除範圍
不重製 0022 至 0025 的正文或評分邏輯。
不處理非 TTQS 管理系統之一般行政文件，除非其被列為受控文件。
不聲明任何實際法律保存期限；保存期間僅為 SAMPLE 期間，使用前必須核實。
不處理真實個資跨境傳輸、雲端供應商合約等法務細節，除非組織另有制度。
5. 名詞定義
[TABLE_ROW 0] 名詞 || 定義
[TABLE_ROW 1] 受控文件 || 經分類、編號、審查、核准、發布、版本管理與保存的文件
[TABLE_ROW 2] 候選文件 || 已起草但尚未核准生效的文件；不得標示 CURRENT
[TABLE_ROW 3] CURRENT || 經核准且在生效期間內的現行版本
[TABLE_ROW 4] OBSOLETE || 已被新版本取代、不得作為作業依據的版本
[TABLE_ROW 5] 草案 || 尚未核准的文件版本，僅供審查與修改
[TABLE_ROW 6] 公告 || 向指定對象正式通知文件生效、變更或作廢
[TABLE_ROW 7] 簽收 || 使用者對已公告文件完成閱讀/理解確認的紀錄
[TABLE_ROW 8] 受控副本 || 可識別版本、受版本控制且可追溯的文件副本
[TABLE_ROW 9] 非受控副本 || 僅供參考、不得作為作業依據的副本
[TABLE_ROW 10] 封存 || 將舊版或停用文件移入保存區，保留追溯性但不供日常使用
[TABLE_ROW 11] 例外 || 偏離標準流程但經授權、有期限、有紀錄的處理
[TABLE_ROW 12] PDRO || Plan-Do-Review-Operate，本文件用於 TTQS 管理系統自我檢查
6. 控制原則
單一真相來源：受控文件台帳為版本狀態的唯一真相來源。
未核准不得生效：任何 DRAFT / CANDIDATE 版本不得標示 CURRENT。
版本可追溯：每次變更必須有版本、日期、變更原因、審查與核准紀錄。
最小權限：文件存取依角色與必要性授予。
公告先於使用：新版本或重大變更必須先公告，再要求作業使用。
簽收不得偽造：簽收必須來自系統紀錄或可驗證證據；缺失簽收不得虛報。
舊版必須撤回：新版本生效時，舊版受控副本必須回收、標示 OBSOLETE 或封存。
未知不視為通過：缺少資料、未完成檢查或未回覆者不得計為通過。
保存期間可核實：沒有正式法定期限來源時，只能使用 SAMPLE 期間並要求核實。
合成資料可替換：所有 synthetic values 必須可透過替換清冊替換為真實資料。
7. 文件層級與識別規則
7.1 文件層級
[TABLE_ROW 0] 層級 || 類型 || 範例 || 控制強度
[TABLE_ROW 1] Level 0 || 政策 / 方針 || 品質政策、訓練政策 || 高
[TABLE_ROW 2] Level 1 || TTQS 管理手冊 / 體系文件 || TTQS 管理系統說明 || 高
[TABLE_ROW 3] Level 2 || 程序 / SOP / 作業規範 || 本文件 || 高
[TABLE_ROW 4] Level 3 || 表單 / 紀錄 / 台帳 || 本文件附表 || 中高
[TABLE_ROW 5] Level 4 || 外部參考文件 || 官方指引、法規、客戶要求 || 參考
7.2 識別規則
[TABLE_ROW 0] 規則 || 說明
[TABLE_ROW 1] 文件編號格式 || TTQS-DC-####；本文件為 TTQS-DC-0026（SF-003）
[TABLE_ROW 2] 版次格式 || 主版次.次版次 或 主版次.次版次.修正版次
[TABLE_ROW 3] 草案版次 || 0.x
[TABLE_ROW 4] 核准版次 || 1.0 起
[TABLE_ROW 5] 狀態值 || DRAFT / IN REVIEW / APPROVED / CURRENT / SUPERSEDED / OBSOLETE / ARCHIVED / WITHDRAWN
[TABLE_ROW 6] 生效日 || 必須晚於或等於核准日；候選文件無生效日
[TABLE_ROW 7] 樣本標示 || 所有合成資料必須標示 SAMPLE/SYNTHETIC 或 SF-ID
8. 權責與授權矩陣
[TABLE_ROW 0] 角色代碼 || 角色 || 授權層級 || 主要職責 || 可執行生命週期動作 || 不可執行 || 授權狀態
[TABLE_ROW 1] ROLE-GM-001 || 陳示例（SAMPLE） || L4 核准者 || 最終核准、重大變更核准、緊急修訂核准 || 核准、駁回、指定代理、緊急指示 || 不得代填簽收、不得刪除稽核軌跡 || SAMPLE-ASSIGNED；實際授權 UNKNOWN
[TABLE_ROW 2] ROLE-QMS-001 || 林示例（SAMPLE） || L3 品質/系統管理者 || 內容與品質審查、PDRO 自查、指標監控 || 審查、要求修正、判定 PDRO || 不得單獨核准 Level 0/1 文件 || SAMPLE-ASSIGNED；實際授權 UNKNOWN
[TABLE_ROW 3] ROLE-DOC-001 || 王示例（SAMPLE） || L2 文件管制 || 版控、發布、台帳、封存、檢索測試 || 起草、編號、發布、作廢、封存 || 不得核准自己起草之文件 || SAMPLE-ASSIGNED；實際授權 UNKNOWN
[TABLE_ROW 4] ROLE-TRM-001 || 張示例（SAMPLE） || L2 內容負責人 || 訓練內容、課程與 SOP 介面 || 提出需求、內容審查、提出變更 || 不得核准文件、不得變更權限 || SAMPLE-ASSIGNED；實際授權 UNKNOWN
[TABLE_ROW 5] ROLE-COM-001 || 劉示例（SAMPLE） || L2 法遵/品質支援 || 法遵與風險審查（適用時） || 審查、風險登錄、要求補件 || 不得單獨發布 || SAMPLE-ASSIGNED；實際授權 UNKNOWN
[TABLE_ROW 6] ROLE-IT-001 || 黃示例（SAMPLE） || L2 系統管理 || 存取、備份、還原、系統稽核軌跡 || 權限設定、備份驗證、還原測試 || 不得核准文件內容 || SAMPLE-ASSIGNED；實際授權 UNKNOWN
[TABLE_ROW 7] ROLE-USER-GROUP || 受控文件使用者 12 人（SAMPLE） || L1 使用者 || 閱讀、使用、簽收、回報問題 || 簽收、提問、提報錯誤 || 不得修改受控文件 || SAMPLE-ASSIGNED；實際授權 UNKNOWN
[TABLE_ROW 8] ROLE-AUD-001 || 內部稽核角色（SAMPLE） || L3 稽核 || 獨立驗證流程與紀錄 || 查核、發現、追蹤改善 || 不得核准被稽核文件 || SAMPLE-ASSIGNED；實際授權 UNKNOWN
授權狀態規則：若無實際授權文件、職務代理紀錄或簽核樣本，狀態必須標記 UNKNOWN，不得推定為已授權。
9. 受控文件生命週期決策流程
9.1 流程總覽
[TABLE_ROW 0] 階段 || 輸入 || 主要動作 || 責任角色 || 輸出 || 紀錄 || SAMPLE SLA
[TABLE_ROW 1] 1 需求 || 訓練/品質/法遵/稽核需求 || 建立文件需求單 || ROLE-TRM-001 / ROLE-QMS-001 || 需求單 || DR-xxx || 3 個工作天
[TABLE_ROW 2] 2 分類/敏感級別 || 需求單 || 判定層級、機密等級、保存類別 || ROLE-DOC-001 || 分類判定 || CL-xxx || 2 個工作天
[TABLE_ROW 3] 3 起草 || 分類判定 || 建立草案、編號、版本 || ROLE-DOC-001 || DRAFT v0.x || DC-xxx || 5 個工作天
[TABLE_ROW 4] 4 內容審查 || 草案 || 內容正確性、訓練邏輯、介面檢查 || ROLE-TRM-001 || 審查意見 || RV-xxx || 5 個工作天
[TABLE_ROW 5] 5 品質/法遵審查 || 內容審查通過草案 || 品質、風險、法遵、PDRO 連結檢查 || ROLE-QMS-001 / ROLE-COM-001 || 審查報告 || QR-xxx || 5 個工作天
[TABLE_ROW 6] 6 核准 || 審查通過草案 || 核准、駁回或要求修正 || ROLE-GM-001 || 核准紀錄 || AP-xxx || 5 個工作天
[TABLE_ROW 7] 7 版次/生效判定 || 核准紀錄 || 指定版次、生效日、公告範圍 || ROLE-DOC-001 || 版次判定 || VR-xxx || 2 個工作天
[TABLE_ROW 8] 8 公告與取用 || 版次判定 || 發布公告、開放下載、權限設定 || ROLE-DOC-001 || 公告紀錄 || ANN-xxx || 生效日前 7 日
[TABLE_ROW 9] 9 訓練/簽收 || 公告紀錄 || 指定必讀對象與截止日 || ROLE-TRM-001 / ROLE-DOC-001 || 簽收追蹤 || ACK-xxx || 7 日
[TABLE_ROW 10] 10 定期審查 || CURRENT 文件 || 檢查有效性、適用性、指標 || ROLE-QMS-001 || 審查報告 || PR-xxx || 每 12 個月
[TABLE_ROW 11] 11 修訂/緊急修訂/拒絕 || 審查結果或變更請求 || 決定修訂、緊急修訂或不修訂 || ROLE-GM-001 || 修訂決定 || CR/EC/EI || 依風險
[TABLE_ROW 12] 12 舊版撤回 || 新版生效 || 回收、標示 OBSOLETE、封存 || ROLE-DOC-001 || 撤回紀錄 || OB-xxx || 5 個工作天
[TABLE_ROW 13] 13 封存 || 舊版/作廢文件 || 移入封存區、保留索引 || ROLE-DOC-001 || 封存紀錄 || AR-xxx || 5 個工作天
[TABLE_ROW 14] 14 保存/處置 || 封存文件 || 保存、到期評估、處置授權 || ROLE-QMS-001 / ROLE-GM-001 || 處置紀錄 || RT-xxx || 依保存表
[TABLE_ROW 15] 15 檢索測試 || 受控文件台帳 || 驗證可找到 CURRENT、不可誤用 OBSOLETE || ROLE-DOC-001 / ROLE-AUD-001 || 測試報告 || RTT-xxx || 每季
9.2 決策規則
需求未分類不得起草。
內容審查未通過不得進入品質/法遵審查。
品質/法遵審查未通過不得進入核准。
未核准不得發布。
未公告不得要求作業使用。
簽收未完成不得在 PDRO 中標記「訓練完成」。
舊版未撤回不得宣告新版全面取代。
未知、未回覆、未測試項目不得計為通過。
10. 版號、狀態與生效日規則
10.1 狀態定義
[TABLE_ROW 0] 狀態 || 定義 || 可否作為作業依據
[TABLE_ROW 1] DRAFT || 草案，未審查或未核准 || 否
[TABLE_ROW 2] IN REVIEW || 審查中 || 否
[TABLE_ROW 3] APPROVED || 已核准但尚未生效 || 否
[TABLE_ROW 4] CURRENT || 已核准且在生效期間內 || 是
[TABLE_ROW 5] SUPERSEDED || 已被新版取代 || 否
[TABLE_ROW 6] OBSOLETE || 作廢，不得使用 || 否
[TABLE_ROW 7] ARCHIVED || 已封存保存 || 否
[TABLE_ROW 8] WITHDRAWN || 撤回，不得使用 || 否
10.2 版號規則
[TABLE_ROW 0] 變更類型 || 版號變化 || 範例 || 是否重新公告
[TABLE_ROW 1] 草案調整 || 0.x || 0.1 → 0.2 || 否，僅審查對象
[TABLE_ROW 2] 首次核准發布 || 0.x → 1.0 || 0.9 → 1.0 || 是
[TABLE_ROW 3] 內容/流程重大變更 || 主版次 +1 || 1.0 → 2.0 || 是
[TABLE_ROW 4] 內容一般變更 || 次版次 +1 || 1.0 → 1.1 || 是
[TABLE_ROW 5] 純編輯修正 || 修正版次 +1 || 1.0 → 1.0.1 || 視影響範圍
[TABLE_ROW 6] 緊急修訂 || 主版次 +1 或次版次 +1 + EI 編號 || 1.0 → 1.1（EI-0026-001） || 是，含暫行指示
10.3 生效日規則
生效日必須由核准人或授權代理指定。
生效日不得早於核准日。
候選文件不得填寫生效日；只能填「NONE / TBD」。
若公告晚於生效日，必須記錄偏差與補救措施。
緊急修訂可設定即時生效，但必須在 5 個工作天內補齊正式公告與簽收。
11. 紙本 / 數位受控副本與離線版本處理
11.1 受控副本識別
[TABLE_ROW 0] 副本類型 || 識別方式 || 可否作業使用
[TABLE_ROW 1] 數位受控副本 || 系統版本號、狀態、生效日、下載紀錄 || 是
[TABLE_ROW 2] 紙本受控副本 || 頁首/頁尾版次、受控章戳、發行編號、持有人簽收 || 是
[TABLE_ROW 3] 非受控副本 || 浮水印「UNCONTROLLED COPY」 || 否
[TABLE_ROW 4] 離線副本 || 必須標示版本與下載日期；離線超過 30 日需重新下載 || 依版本有效性
11.2 離線版本處理
離線副本必須保留文件編號、版次、狀態、生效日。
離線副本不得修改。
使用者必須在每次使用前確認 CURRENT 版本。
若發現離線版本為 OBSOLETE，必須立即停止使用並回報 ROLE-DOC-001。
系統中止服務時，必須啟動離線受控副本清單與人工版本確認。
12. 公告與簽收管理
12.1 公告基本規則
公告必須包含：文件編號、標題、版次、生效日、公告對象、公告管道、閱讀/簽收截止日、舊版處理方式、聯絡人。
公告對象由文件內容、使用角色、訓練流程與風險決定。
公告管道至少兩種：內部系統公告 + 電子郵件；高風險文件可加會議或訓練。
公告必須可追溯：公告 ID、發送清單、時間、管道、回條。
未完成公告不得要求使用者依新版作業。
12.2 簽收規則
簽收對象 = 公告對象中被指定為必讀者。
簽收截止日 SAMPLE：公告日起 7 日（SF-101 / SF-102）。
簽收必須記錄：使用者、角色、文件編號、版次、閱讀時間、確認方式、IP/系統紀錄（若可用）。
不得虛構簽收；若系統無法取得簽收，狀態標記 UNKNOWN / NOT RECEIVED。
逾期未簽收必須升級，不得自動計為已讀。
12.3 升級 ladder
[TABLE_ROW 0] 等級 || 觸發條件 || 動作 || 責任角色 || SAMPLE SLA
[TABLE_ROW 1] L1 提醒 || 截止前 2 日未簽收 || 系統提醒 || ROLE-DOC-001 || 1 日
[TABLE_ROW 2] L2 逾期通知 || 截止日起未簽收 || 通知使用者與直屬主管 || ROLE-TRM-001 || 1 日
[TABLE_ROW 3] L3 升級 || 逾期 1 日以上 || 通知文件負責人與品質管理者 || ROLE-QMS-001 || 1 日
[TABLE_ROW 4] L4 管理介入 || 逾期 3 日以上或影響稽核 || 通知核准者，限制相關作業 || ROLE-GM-001 || 2 日
[TABLE_ROW 5] L5 例外紀錄 || 有合理原因無法簽收 || 建立例外紀錄與替代證據 || ROLE-QMS-001 || 5 日
13. 分類、存取、備份、檢索、保存與處置
13.1 分類與存取
[TABLE_ROW 0] 分類 || 定義 || 存取原則
[TABLE_ROW 1] Public || 可公開 || 全員唯讀
[TABLE_ROW 2] Internal || 內部使用 || 員工唯讀
[TABLE_ROW 3] Internal-Confidential || 機密內部 || 角色授權
[TABLE_ROW 4] Restricted || 高度敏感 || 最小權限 + 雙重授權
13.2 存取矩陣（樣本）
[TABLE_ROW 0] 群組 || 人數（SF） || 可讀 || 可下載受控副本 || 可編輯草案 || 可核准 || 可管理權限
[TABLE_ROW 1] Group A 核准/品質/文件 || 3（SF-028） || 是 || 是 || 是（指定人） || 是（ROLE-GM-001） || 是（ROLE-IT-001）
[TABLE_ROW 2] Group B 內容負責人 || 4（SF-029） || 是 || 是 || 是（指定人） || 否 || 否
[TABLE_ROW 3] Group C 一般使用者 || 5（SF-030） || 是 || 是 || 否 || 否 || 否
[TABLE_ROW 4] 合計 || 12（SF-031） || — || — || — || — || —
13.3 備份與還原
[TABLE_ROW 0] 項目 || 設定（SAMPLE）
[TABLE_ROW 1] 備份頻率 || 每日增量、每週完整
[TABLE_ROW 2] RPO || 24 小時（SF-104）
[TABLE_ROW 3] RTO || 8 小時（SF-105）
[TABLE_ROW 4] 還原測試 || 每季至少一次
[TABLE_ROW 5] 稽核軌跡保留 || 與文件保存期間一致
13.4 檢索規則
受控文件台帳必須可依文件編號、標題、版次、狀態、生效日、分類、負責人查詢。
檢索 CURRENT 文件的時間目標 ≤ 10 分鐘。
OBSOLETE / ARCHIVED 文件不得出現在一般使用者的 CURRENT 搜尋結果。
檢索失敗必須記錄為不符合事項。
13.5 保存與處置（樣本期間，非法定期限）
[TABLE_ROW 0] 記錄類型 || SAMPLE 保存期間 || 到期處理 || 說明
[TABLE_ROW 1] 核准/版本紀錄 || 5 年 || 評估封存延長或處置 || 需核實法定/契約要求
[TABLE_ROW 2] 公告與簽收紀錄 || 5 年 || 評估封存延長或處置 || 需核實
[TABLE_ROW 3] 訓練教材與評估紀錄 || 3 年 || 評估封存延長或處置 || 需核實
[TABLE_ROW 4] 稽核/不符合紀錄 || 5 年 || 評估封存延長或處置 || 需核實
[TABLE_ROW 5] 封存文件 || 5 年 || 處置需核准者授權 || 需核實
本表的保存期間為 SAMPLE，不得宣稱為法規期限。
14. 例外、更正與緊急修訂
14.1 例外類型
[TABLE_ROW 0] 類型 || 說明 || 是否需要核准者
[TABLE_ROW 1] 文件缺失 || 必要文件尚未建立 || 是
[TABLE_ROW 2] 版本偏差 || 使用者使用非 CURRENT 版本 || 是
[TABLE_ROW 3] 公告偏差 || 公告晚於生效日 || 是
[TABLE_ROW 4] 簽收偏差 || 逾期未簽收 || 是
[TABLE_ROW 5] 緊急修訂 || 安全/法遵/重大錯誤需立即修正 || 是
[TABLE_ROW 6] 系統中斷 || 無法存取文件系統 || 是
14.2 更正路徑
發現問題 → 建立不符合/變更請求。
分類影響程度：編輯、內容、流程、法遵、安全。
決定處理方式：不變更、修正現行版、新版本、緊急指示。
必要時啟動暫行指示，並設定到期日。
補齊公告、簽收、舊版撤回與台帳更新。
關閉不符合，留存證據。
14.3 緊急修訂規則
緊急修訂必須由 ROLE-GM-001 或授權代理核准。
必須發出緊急指示編號（EI-xxx），含有效期間。
有效期間不得超過 30 日，除非核准者延長並記錄原因。
緊急指示到期前必須轉為正式版本或失效。
緊急修訂仍需公告與簽收。
14.4 樣本例外紀錄
[TABLE_ROW 0] 項目 || 內容（SAMPLE）
[TABLE_ROW 1] 例外編號 || EC-0026-001（SF-072）
[TABLE_ROW 2] 類型 || minor editorial correction request（SF-073）
[TABLE_ROW 3] 發現日期 || 2026-10-20
[TABLE_ROW 4] 問題描述 || 樣本文件中某章節文字順序錯誤，不影響流程
[TABLE_ROW 5] 影響程度 || 編輯
[TABLE_ROW 6] 處理方式 || 暫行指示 EI-0026-001（SF-075），有效 2026-10-25 至 2026-11-24（SF-076 / SF-077）
[TABLE_ROW 7] 結果 || 於 2026-11-15 風險/例外審查確認無需永久變更；暫行指示依期限有效至 2026-11-24，屆期後關閉（SF-050 / SF-074 / SF-077 / SF-078）
[TABLE_ROW 8] 關閉日期 || 2026-11-24（SF-077）
15. 風險登錄
[TABLE_ROW 0] 風險編號 || 風險描述 || 可能性 || 影響 || 緩解措施 || 責任角色 || 狀態
[TABLE_ROW 1] RISK-0026-001 || 未核准草案被誤用為 CURRENT || 中 || 高 || 版本水印、台帳查詢、教育訓練 || ROLE-DOC-001 || OPEN-MONITOR
[TABLE_ROW 2] RISK-0026-002 || 公告後簽收不完整 || 中 || 中 || 升級 ladder、主管追蹤 || ROLE-TRM-001 || OPEN-MONITOR
[TABLE_ROW 3] RISK-0026-003 || 舊版副本未回收 || 中 || 中 || 回收清冊、作廢章戳 || ROLE-DOC-001 || OPEN-MONITOR
[TABLE_ROW 4] RISK-0026-004 || 存取權限過寬 || 低 || 高 || 最小權限、定期存取審查 || ROLE-IT-001 || OPEN-MONITOR
[TABLE_ROW 5] RISK-0026-005 || 保存期間未核實 || 高 || 中 || 標示 SAMPLE、法遵審查 || ROLE-COM-001 || OPEN-MONITOR
16. PDRO 自我檢查與 TTQS 連結
16.1 PDRO 對應
[TABLE_ROW 0] PDRO || 本文件內容
[TABLE_ROW 1] Plan || 文件需求、分類、權責、版本規則、保存策略
[TABLE_ROW 2] Do || 起草、審查、核准、公告、簽收、取用
[TABLE_ROW 3] Review || 定期審查、指標、稽核、不符合處理
[TABLE_ROW 4] Operate || 持續改善、版本更新、封存、處置
16.2 自我檢查表
[TABLE_ROW 0] 指標 ID || 指標名稱 || 分子 || 分母 || 排除 || 目標 || 結果 || 狀態
[TABLE_ROW 1] IND-0026-001 || 受控文件台帳完整率 || 1 || 1 || 無 || 100% || 100% || PASS
[TABLE_ROW 2] IND-0026-002 || 核准後方能生效文件率 || 1 || 1 || 無 || 100% || 100% || PASS
[TABLE_ROW 3] IND-0026-003 || 公告含完整對象清單率 || 1 || 1 || 無 || 100% || 100% || PASS
[TABLE_ROW 4] IND-0026-004 || 截止日前簽收率 || 11 || 12 || 無 || ≥95% || 91.7% || FAIL / IMPROVE
[TABLE_ROW 5] IND-0026-005 || 舊版受控副本回收率 || 3 || 3 || 無 || 100% || 100% || PASS
[TABLE_ROW 6] IND-0026-006 || 定期審查準時率 || 0 || 0 || 尚未到期之 1 件 || ≥90% || N/A || NOT DUE
[TABLE_ROW 7] IND-0026-007 || 檢索測試通過率 || 5 || 5 || 無 || 100% || 100% || PASS
[TABLE_ROW 8] IND-0026-008 || 存取審查完成率 || 1 || 1 || 無 || 100% || 100% || PASS
未知值處理：任何未回覆、未測試、未取得紀錄者，均不得計入分子；不得以未知視為通過。
17. 持續改善指標
[TABLE_ROW 0] 指標 || 公式 || 目標 || 樣本結果 || 改善行動
[TABLE_ROW 1] 公告到簽收完成天數 || 最後簽收日 - 公告日 || ≤7 日 || 9 日（2026-10-05 至 2026-10-14） || 強化主管追蹤
[TABLE_ROW 2] 簽收逾期件數 || 逾期簽收人數 || 0 || 1 || 升級 ladder
[TABLE_ROW 3] 檢索時間 || 檢索 CURRENT 文件時間 || ≤10 分鐘 || 4 分鐘 || 維持索引
[TABLE_ROW 4] 版本錯誤事件 || 使用 OBSOLETE 事件數 || 0 || 0 || 持續教育
[TABLE_ROW 5] 例外關閉率 || 已關閉例外 / 已登錄例外 || 100% || 1/1 = 100% || 維持
18. 完整 SAMPLE/SYNTHETIC 走讀
18.1 走讀摘要
本走讀展示一個受控文件從需求到封存的完整生命週期。所有資料均為 SAMPLE/SYNTHETIC。
[TABLE_ROW 0] 項目 || 內容
[TABLE_ROW 1] 文件實例 || TTQS-DC-0026-S01（SF-009）
[TABLE_ROW 2] 文件標題 || TTQS 管理系統運作與受控文件生命週期作業規範（SF-006）
[TABLE_ROW 3] 起始需求日 || 2026-09-01（SF-037）
[TABLE_ROW 4] 核准日 || 2026-10-05（SF-043）
[TABLE_ROW 5] 生效日 || 2026-10-12（SF-012）
[TABLE_ROW 6] 公告日 || 2026-10-05（SF-044）
[TABLE_ROW 7] 簽收截止日 || 2026-10-12（SF-045）
[TABLE_ROW 8] 最後簽收日 || 2026-10-14（SF-047）
[TABLE_ROW 9] 檢索測試日 || 2026-10-28（SF-048）
[TABLE_ROW 10] 定期審查到期日 || 2027-10-12（SF-051）
18.2 時間線
[TABLE_ROW 0] 日期 || 事件 || 版次 || 狀態 || 責任角色 || 紀錄編號
[TABLE_ROW 1] 2026-09-01 || 提出文件需求 || — || DRAFT REQUESTED || ROLE-TRM-001 || DR-0026-001
[TABLE_ROW 2] 2026-09-08 || 建立草案 v0.1 || 0.1 || DRAFT || ROLE-DOC-001 || DC-0026-001
[TABLE_ROW 3] 2026-09-15 || 內容審查完成，3 項意見 || 0.1 || IN REVIEW || ROLE-TRM-001 || RV-0026-001
[TABLE_ROW 4] 2026-09-18 || 修正後 v0.2 || 0.2 || DRAFT || ROLE-DOC-001 || DC-0026-002
[TABLE_ROW 5] 2026-09-22 || 品質/法遵審查，1 項發現 || 0.2 || IN REVIEW || ROLE-QMS-001 || QR-0026-001
[TABLE_ROW 6] 2026-09-25 || 修正後 v0.9 || 0.9 || IN REVIEW || ROLE-DOC-001 || DC-0026-003
[TABLE_ROW 7] 2026-10-05 || 核准 || 1.0 || APPROVED || ROLE-GM-001 || AP-0026-001
[TABLE_ROW 8] 2026-10-05 || 公告 || 1.0 || APPROVED || ROLE-DOC-001 || ANN-0026-001
[TABLE_ROW 9] 2026-10-12 || 生效與簽收截止；11/12 準時簽收 || 1.0 || CURRENT || ROLE-USER-GROUP || ACK-0026-001
[TABLE_ROW 10] 2026-10-13 || 1 人逾期，升級 || 1.0 || CURRENT || ROLE-QMS-001 || ESC-0026-001
[TABLE_ROW 11] 2026-10-14 || 最後簽收完成 || 1.0 || CURRENT || ROLE-USER-GROUP || ACK-0026-001
[TABLE_ROW 12] 2026-10-28 || 檢索測試 5/5 通過 || 1.0 || CURRENT || ROLE-DOC-001 || RTT-0026-001
[TABLE_ROW 13] 2026-10-30 || 存取審查完成 || 1.0 || CURRENT || ROLE-IT-001 || AC-0026-001
[TABLE_ROW 14] 2026-11-15 || 風險/例外審查 || 1.0 || CURRENT || ROLE-QMS-001 || RV-0026-002
[TABLE_ROW 15] 2026-11-24（SF-077） || 暫行指示屆期；例外關閉，無永久修訂 || 1.0 || CURRENT || ROLE-QMS-001 || EC-0026-001 / EI-0026-001
18.3 詳細走讀
需求（2026-09-01）：ROLE-TRM-001 提出 TTQS 管理系統運作與文件控制需求，引用 I04-E05，不複製 0022-0025 正文。
分類（2026-09-03）：判定為 Level 2 受控文件、Internal-Confidential、保存 5 年（SAMPLE）。
起草（2026-09-08）：ROLE-DOC-001 建立 v0.1，文件編號 TTQS-DC-0026-S01。
內容審查（2026-09-15）：ROLE-TRM-001 提出 3 項意見，全部於 2026-09-18 修正並發行 v0.2。
品質/法遵審查（2026-09-22）：ROLE-QMS-001 提出 1 項發現；ROLE-COM-001 確認無法遵阻擋；修正後發行 v0.9。
核准（2026-10-05）：ROLE-GM-001 以虛構角色身分核准 v1.0；本文件仍標示 SAMPLE，不構成真實核准。
版次/生效（2026-10-05）：指定 v1.0、生效日 2026-10-12、公告對象 12 人。
公告（2026-10-05）：內部系統 + 電子郵件；公告 ID ANN-0026-001；截止日 2026-10-12。
簽收（2026-10-05 至 2026-10-14）：11 人於截止日前簽收；1 人逾期，於 2026-10-13 升級，2026-10-14 完成；最終 12/12 = 100%。
舊版撤回（2026-10-12）：v0.9 的 3 份受控草案副本全部回收並銷毀，回收率 3/3 = 100%。
檢索測試（2026-10-28）：5 項查詢，5 項找到 CURRENT v1.0，0 項誤回 OBSOLETE；通過率 100%。
定期審查（到期 2027-10-12）：尚未到期，不得計為通過或失敗；狀態 NOT DUE。
18.4 走讀驗證清單
[TABLE_ROW 0] 檢查項 || 預期 || 實際（SAMPLE） || 結果
[TABLE_ROW 1] 核准日 ≤ 生效日 || 2026-10-05 ≤ 2026-10-12 || 是 || PASS
[TABLE_ROW 2] 公告日 ≤ 生效日 - 7 日 || 2026-10-05 ≤ 2026-10-05 || 是 || PASS
[TABLE_ROW 3] 簽收截止日 ≥ 公告日 || 2026-10-12 ≥ 2026-10-05 || 是 || PASS
[TABLE_ROW 4] 簽收人數 ≤ 公告對象 || 12 ≤ 12 || 是 || PASS
[TABLE_ROW 5] 舊版回收數 ≤ 發行數 || 3 ≤ 3 || 是 || PASS
[TABLE_ROW 6] 檢索通過率 || 5/5 || 5/5 || PASS
[TABLE_ROW 7] 未知項不計通過 || IND-0026-006 || NOT DUE || PASS
19. 可直接複製使用的已填範例表單 / 台帳
19.1 文件控制單（已填，SAMPLE）
[TABLE_ROW 0] 欄位 || 填寫值
[TABLE_ROW 1] 文件編號 || TTQS-DC-0026-S01（SF-009）
[TABLE_ROW 2] 文件標題 || TTQS 管理系統運作與受控文件生命週期作業規範（SF-006）
[TABLE_ROW 3] 文件層級 || Level 2（SF-034）
[TABLE_ROW 4] 機密等級 || Internal-Confidential（SF-013）
[TABLE_ROW 5] 目前版次 || 1.0（SF-010）
[TABLE_ROW 6] 目前狀態 || CURRENT（SAMPLE）
[TABLE_ROW 7] 生效日 || 2026-10-12（SF-012）
[TABLE_ROW 8] 文件負責人 || ROLE-DOC-001 王示例（SF-020 / SF-021）
[TABLE_ROW 9] 內容負責人 || ROLE-TRM-001 張示例（SF-022 / SF-023）
[TABLE_ROW 10] 品質負責人 || ROLE-QMS-001 林示例（SF-018 / SF-019）
[TABLE_ROW 11] 核准人 || ROLE-GM-001 陳示例（SAMPLE）（SF-016 / SF-017）
[TABLE_ROW 12] 備份位置 || 文件系統 + 離線索引（SAMPLE）
[TABLE_ROW 13] 保存到期日 || 2031-10-12（SF-015）
[TABLE_ROW 14] 備註 || 候選文件本體仍為 CANDIDATE；本表為走讀樣本
19.2 審查與意見紀錄（已填，SAMPLE）
[TABLE_ROW 0] 紀錄編號 || 審查類型 || 審查人 || 日期 || 意見數 || 已解決 || 結果
[TABLE_ROW 1] RV-0026-001 || 內容審查 || ROLE-TRM-001 張示例 || 2026-09-15（SF-039） || 3（SF-065） || 3（SF-066） || 通過
[TABLE_ROW 2] QR-0026-001 || 品質/法遵審查 || ROLE-QMS-001 林示例 || 2026-09-22（SF-041） || 1（SF-067） || 1（SF-068） || 通過
[TABLE_ROW 3] RV-0026-002 || 風險/例外審查 || ROLE-QMS-001 林示例 || 2026-11-15（SF-050） || 0 || 0 || 通過
19.3 核准紀錄（已填，SAMPLE / 虛構）
[TABLE_ROW 0] 欄位 || 填寫值
[TABLE_ROW 1] 核准編號 || AP-0026-001
[TABLE_ROW 2] 文件編號/版次 || TTQS-DC-0026-S01 / 1.0
[TABLE_ROW 3] 核准人 || ROLE-GM-001 陳示例（SAMPLE PERSON）
[TABLE_ROW 4] 核准日期 || 2026-10-05（SF-043）
[TABLE_ROW 5] 核准類型 || SAMPLE APPROVAL（非真實核准）
[TABLE_ROW 6] 生效日指定 || 2026-10-12（SF-012）
[TABLE_ROW 7] 附帶條件 || 必須完成公告與簽收
[TABLE_ROW 8] 紀錄狀態 || SYNTHETIC / NOT REAL APPROVAL
19.4 公告紀錄（已填，SAMPLE）
[TABLE_ROW 0] 欄位 || 填寫值
[TABLE_ROW 1] 公告編號 || ANN-0026-001（SF-069）
[TABLE_ROW 2] 文件編號/版次 || TTQS-DC-0026-S01 / 1.0
[TABLE_ROW 3] 公告日 || 2026-10-05（SF-044）
[TABLE_ROW 4] 生效日 || 2026-10-12（SF-012）
[TABLE_ROW 5] 公告對象 || 12 人（SF-031）
[TABLE_ROW 6] 對象清單編號 || AUD-0026-001（SF-071）
[TABLE_ROW 7] 公告管道 || internal portal; email（SF-070）
[TABLE_ROW 8] 簽收截止日 || 2026-10-12（SF-045）
[TABLE_ROW 9] 舊版處理 || v0.9 受控草案 3 份回收銷毀
[TABLE_ROW 10] 聯絡人 || ROLE-DOC-001 王示例
[TABLE_ROW 11] 紀錄狀態 || SYNTHETIC
19.5 簽收登錄（已填，SAMPLE，12 筆）
[TABLE_ROW 0] 簽收編號 || 使用者代碼 || 角色群組 || 文件/版次 || 閱讀日期 || 狀態 || 備註
[TABLE_ROW 1] ACK-0026-001 || U-001 || Group A || 1.0 || 2026-10-06 || 已簽收 || 準時
[TABLE_ROW 2] ACK-0026-002 || U-002 || Group A || 1.0 || 2026-10-07 || 已簽收 || 準時
[TABLE_ROW 3] ACK-0026-003 || U-003 || Group A || 1.0 || 2026-10-08 || 已簽收 || 準時
[TABLE_ROW 4] ACK-0026-004 || U-004 || Group B || 1.0 || 2026-10-06 || 已簽收 || 準時
[TABLE_ROW 5] ACK-0026-005 || U-005 || Group B || 1.0 || 2026-10-09 || 已簽收 || 準時
[TABLE_ROW 6] ACK-0026-006 || U-006 || Group B || 1.0 || 2026-10-10 || 已簽收 || 準時
[TABLE_ROW 7] ACK-0026-007 || U-007 || Group B || 1.0 || 2026-10-11 || 已簽收 || 準時
[TABLE_ROW 8] ACK-0026-008 || U-008 || Group C || 1.0 || 2026-10-07 || 已簽收 || 準時
[TABLE_ROW 9] ACK-0026-009 || U-009 || Group C || 1.0 || 2026-10-08 || 已簽收 || 準時
[TABLE_ROW 10] ACK-0026-010 || U-010 || Group C || 1.0 || 2026-10-09 || 已簽收 || 準時
[TABLE_ROW 11] ACK-0026-011 || U-011 || Group C || 1.0 || 2026-10-11 || 已簽收 || 準時
[TABLE_ROW 12] ACK-0026-012 || U-012 || Group C || 1.0 || 2026-10-14 || 已簽收 || 逾期，已升級 ESC-0026-001
統計：準時 11 人（SF-056）；逾期 1 人（SF-057）；完成 12/12 人（SF-058）；完成率 100%（SF-059）；準時率 91.7%（SF-060）。
19.6 版本 / 修訂登錄（已填，SAMPLE）
[TABLE_ROW 0] 版次 || 狀態 || 建立日期 || 核准日期 || 生效日期 || 變更摘要 || 前版 || 紀錄編號
[TABLE_ROW 1] 0.1 || SUPERSEDED || 2026-09-08（SF-038） || — || — || 初稿 || — || DC-0026-001
[TABLE_ROW 2] 0.2 || SUPERSEDED || 2026-09-18（SF-040） || — || — || 內容審查修正 3 項 || 0.1 || DC-0026-002
[TABLE_ROW 3] 0.9 || OBSOLETE || 2026-09-25（SF-042） || — || — || 品質審查修正 1 項 || 0.2 || DC-0026-003
[TABLE_ROW 4] 1.0 || CURRENT（SAMPLE） || 2026-10-05（SF-043） || 2026-10-05 || 2026-10-12（SF-012） || 首次核准發布 || 0.9 || AP-0026-001
19.7 舊版受控副本回收登錄（已填，SAMPLE）
[TABLE_ROW 0] 副本編號 || 版次 || 持有人 || 發行日期 || 回收日期 || 處理方式 || 狀態
[TABLE_ROW 1] CP-0026-001 || 0.9 || ROLE-TRM-001 || 2026-09-25 || 2026-10-12 || 銷毀 || CLOSED
[TABLE_ROW 2] CP-0026-002 || 0.9 || ROLE-QMS-001 || 2026-09-25 || 2026-10-12 || 銷毀 || CLOSED
[TABLE_ROW 3] CP-0026-003 || 0.9 || ROLE-COM-001 || 2026-09-25 || 2026-10-12 || 銷毀 || CLOSED
統計：發行 3 份（SF-052）；回收 3 份（SF-053）；銷毀 3 份（SF-054）；回收率 100%。
19.8 存取控制矩陣（已填，SAMPLE）
[TABLE_ROW 0] 群組 || 人數 || 主要角色 || 文件權限 || 審查日期 || 結果
[TABLE_ROW 1] Group A || 3（SF-028） || 核准/品質/文件 || 讀取、下載、編輯指定草案、核准、權限管理 || 2026-10-30（SF-049） || 通過
[TABLE_ROW 2] Group B || 4（SF-029） || 內容負責人 || 讀取、下載、編輯指定草案 || 2026-10-30 || 通過
[TABLE_ROW 3] Group C || 5（SF-030） || 一般使用者 || 讀取、下載 || 2026-10-30 || 通過
[TABLE_ROW 4] 合計 || 12（SF-031） || — || — || — || 通過
19.9 保存期間表（SAMPLE，需核實）
[TABLE_ROW 0] 記錄類型 || SAMPLE 保存期間 || 到期日（樣本） || 核實狀態
[TABLE_ROW 1] 核准/版本紀錄 || 5 年 || 2031-10-12（SF-015） || 未核實
[TABLE_ROW 2] 公告/簽收紀錄 || 5 年 || 2031-10-12 || 未核實
[TABLE_ROW 3] 訓練教材/評估紀錄 || 3 年 || 2029-10-12 || 未核實
[TABLE_ROW 4] 稽核/不符合紀錄 || 5 年 || 2031-10-12 || 未核實
[TABLE_ROW 5] 封存文件 || 5 年 || 2031-10-12 || 未核實
19.10 風險登錄（已填，SAMPLE）
[TABLE_ROW 0] 風險編號 || 風險 || 可能性 || 影響 || 緩解 || 責任 || 狀態
[TABLE_ROW 1] RISK-0026-001 || 未核准草案誤用 || 中 || 高 || 水印、台帳、教育 || ROLE-DOC-001 || OPEN-MONITOR
[TABLE_ROW 2] RISK-0026-002 || 簽收不完整 || 中 || 中 || 升級、主管追蹤 || ROLE-TRM-001 || OPEN-MONITOR
[TABLE_ROW 3] RISK-0026-003 || 舊版未回收 || 中 || 中 || 回收清冊、作廢章戳 || ROLE-DOC-001 || OPEN-MONITOR
[TABLE_ROW 4] RISK-0026-004 || 權限過寬 || 低 || 高 || 最小權限、定期審查 || ROLE-IT-001 || OPEN-MONITOR
[TABLE_ROW 5] RISK-0026-005 || 保存期間未核實 || 高 || 中 || 標示 SAMPLE、法遵審查 || ROLE-COM-001 || OPEN-MONITOR
19.11 PDRO 指標表（已填，SAMPLE）
[TABLE_ROW 0] 指標 ID || 指標 || 分子 || 分母 || 目標 || 結果 || 狀態
[TABLE_ROW 1] IND-0026-001 || 台帳完整率 || 1 || 1 || 100% || 100% || PASS
[TABLE_ROW 2] IND-0026-002 || 核准後生效率 || 1 || 1 || 100% || 100% || PASS
[TABLE_ROW 3] IND-0026-003 || 公告對象清單完整率 || 1 || 1 || 100% || 100% || PASS
[TABLE_ROW 4] IND-0026-004 || 截止前簽收率 || 11 || 12 || ≥95% || 91.7% || FAIL / IMPROVE
[TABLE_ROW 5] IND-0026-005 || 舊版回收率 || 3 || 3 || 100% || 100% || PASS
[TABLE_ROW 6] IND-0026-006 || 定期審查準時率 || 0 || 0 || ≥90% || N/A || NOT DUE
[TABLE_ROW 7] IND-0026-007 || 檢索測試通過率 || 5 || 5 || 100% || 100% || PASS
[TABLE_ROW 8] IND-0026-008 || 存取審查完成率 || 1 || 1 || 100% || 100% || PASS
19.12 證據索引（已填，SAMPLE）
[TABLE_ROW 0] 證據編號 || 證據名稱 || 對應章節 || 狀態 || 備註
[TABLE_ROW 1] EV-0026-001 || 文件控制單 || 19.1 || SAMPLE || 虛構
[TABLE_ROW 2] EV-0026-002 || 審查意見紀錄 || 19.2 || SAMPLE || 虛構
[TABLE_ROW 3] EV-0026-003 || 核准紀錄 || 19.3 || SAMPLE || 虛構
[TABLE_ROW 4] EV-0026-004 || 公告紀錄 || 19.4 || SAMPLE || 虛構
[TABLE_ROW 5] EV-0026-005 || 簽收登錄 || 19.5 || SAMPLE || 虛構
[TABLE_ROW 6] EV-0026-006 || 版本/修訂登錄 || 19.6 || SAMPLE || 虛構
[TABLE_ROW 7] EV-0026-007 || 舊版回收登錄 || 19.7 || SAMPLE || 虛構
[TABLE_ROW 8] EV-0026-008 || 存取矩陣 || 19.8 || SAMPLE || 虛構
[TABLE_ROW 9] EV-0026-009 || 保存期間表 || 19.9 || SAMPLE || 需核實
[TABLE_ROW 10] EV-0026-010 || PDRO 指標表 || 19.11 || SAMPLE || 虛構
20. 替換清冊（Replacement Register）
[TABLE_ROW 0] 類別 || 樣本值 / ID || 必須替換為 || 責任 || 狀態
[TABLE_ROW 1] 組織資料 || TTQS 示範訓練中心（SAMPLE）（SF-001 / SF-002） || 實際組織名稱、代碼 || 文件負責人 || 待替換
[TABLE_ROW 2] 人員姓名 || 陳示例、林示例、王示例、張示例、劉示例、黃示例（SF-017 等） || 實際人員或角色代理紀錄 || 人資/主管 || 待替換
[TABLE_ROW 3] 授權紀錄 || SAMPLE-ASSIGNED || 實際授權文件、代理紀錄、簽核樣本 || 核准者 || 待替換
[TABLE_ROW 4] 日期 || 2026-09-01 至 2027-10-12（SF-037 等） || 實際流程日期 || 文件負責人 || 待替換
[TABLE_ROW 5] 版次/狀態 || 1.0 / CURRENT（SAMPLE） || 實際核准版次與狀態 || 核准者 || 待替換
[TABLE_ROW 6] 公告管道 || internal portal; email（SF-070） || 實際公告管道 || 文件負責人 || 待替換
[TABLE_ROW 7] 簽收紀錄 || 12 筆 SAMPLE 簽收（SF-055 至 SF-058） || 實際系統簽收或可驗證證據 || 使用者/系統 || 待替換
[TABLE_ROW 8] 保存期間 || 3 年 / 5 年（SF-014） || 核實後之法定/契約期間 || 法遵/品質 || 待替換
[TABLE_ROW 9] 指標結果 || 91.7%、100% 等（SF-059 等） || 實際量測結果 || 品質管理者 || 待替換
[TABLE_ROW 10] 風險狀態 || OPEN-MONITOR || 實際風險處理狀態 || 風險負責人 || 待替換
21. 證據索引與來源引用矩陣
[TABLE_ROW 0] 證據編號 || 內容 || 來源 / 定位
[TABLE_ROW 1] SRC-001 || 官方 TTQS 證據表第 2 頁 I04-E05 || OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf p.2
[TABLE_ROW 2] SRC-002 || Crosswalk 對應列 || I04-E05 / 0026
[TABLE_ROW 3] SRC-003 || 157 Blueprint 專屬需求列 023 || TTQS 文件批准/公告/保存
[TABLE_ROW 4] SRC-004 || R12 執行規格 || 相容施工契約
[TABLE_ROW 5] SF-001 至 SF-107+ || 合成事實 ID || 本文件末尾 Synthetic Fact Register
22. 附錄 A：驗證清單
[TABLE_ROW 0] 檢查項 || 結果
[TABLE_ROW 1] 核准日 ≤ 生效日 || PASS（2026-10-05 ≤ 2026-10-12）
[TABLE_ROW 2] 公告日 ≤ 生效日 - 7 日 || PASS（2026-10-05 ≤ 2026-10-05）
[TABLE_ROW 3] 簽收完成數 ≤ 公告對象 || PASS（12 ≤ 12）
[TABLE_ROW 4] 準時簽收 + 逾期簽收 = 完成數 || PASS（11 + 1 = 12）
[TABLE_ROW 5] 舊版發行數 = 回收數 = 銷毀數 || PASS（3 = 3 = 3）
[TABLE_ROW 6] 檢索查詢數 = 通過數 || PASS（5 = 5）
[TABLE_ROW 7] 群組人數加總 = 總使用者數 || PASS（3 + 4 + 5 = 12）
[TABLE_ROW 8] IND-0026-004 = 11 / 12 || PASS（91.7%）
[TABLE_ROW 9] IND-0026-006 未到期不計通過 || PASS（NOT DUE）
[TABLE_ROW 10] 所有合成資料均列入 Fact Register || PASS（見下表）
Appendix B: Synthetic Fact Register (CSV-style)
[TABLE_ROW 0] fact_id || category || field_name || synthetic_value || unit_or_type || used_in_section || replacement_required || verification_status
[TABLE_ROW 1] SF-001 || organization || organization_name || TTQS 示範訓練中心（SAMPLE/SYNTHETIC） || text || 0/1/18/19/20 || yes || SAMPLE
[TABLE_ROW 2] SF-002 || organization || organization_code || S-ORG-001 || text || 0/18/19 || yes || SAMPLE
[TABLE_ROW 3] SF-003 || document || document_code || TTQS-DC-0026 || text || 0/7/19 || yes || SAMPLE
[TABLE_ROW 4] SF-004 || document || official_deliverable_id || 0026 || text || 0/2 || yes || OFFICIAL
[TABLE_ROW 5] SF-005 || requirement || requirement_id || I04-E05 || text || 0/2 || yes || OFFICIAL
[TABLE_ROW 6] SF-006 || document || document_title || TTQS 管理系統運作與受控文件生命週期作業規範 || text || 0/18/19 || yes || SAMPLE
[TABLE_ROW 7] SF-007 || document || candidate_version || 0.1-CANDIDATE || text || 0/10 || yes || SAMPLE
[TABLE_ROW 8] SF-008 || document || candidate_status || CANDIDATE / 未核准 / 未生效 || text || 0/1/10 || yes || SAMPLE
[TABLE_ROW 9] SF-009 || document || sample_document_instance || TTQS-DC-0026-S01 || text || 0/18/19 || yes || SAMPLE
[TABLE_ROW 10] SF-010 || document || sample_version || 1.0 || text || 0/10/19 || yes || SAMPLE
[TABLE_ROW 11] SF-011 || document || sample_status || APPROVED-SAMPLE / EFFECTIVE-SAMPLE || text || 0/18 || yes || SAMPLE
[TABLE_ROW 12] SF-012 || document || sample_effective_date || 2026-10-12 || date || 0/10/12/18/19 || yes || SAMPLE
[TABLE_ROW 13] SF-013 || document || classification || Internal-Confidential (Level 2) || text || 0/7/13/19 || yes || SAMPLE
[TABLE_ROW 14] SF-014 || retention || sample_retention_period || 5 years from 2026-10-12 || text || 0/13/19 || yes || SAMPLE-NOT-LEGAL
[TABLE_ROW 15] SF-015 || retention || sample_disposal_eligibility_date || 2031-10-12 || date || 0/13/19 || yes || SAMPLE-NOT-LEGAL
[TABLE_ROW 16] SF-016 || role || role_gm_code || ROLE-GM-001 || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 17] SF-017 || role || role_gm_name || 陳示例 (SAMPLE PERSON) || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 18] SF-018 || role || role_qms_code || ROLE-QMS-001 || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 19] SF-019 || role || role_qms_name || 林示例 (SAMPLE PERSON) || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 20] SF-020 || role || role_doc_code || ROLE-DOC-001 || text || 0/8/18/19 || yes || SAMPLE
[TABLE_ROW 21] SF-021 || role || role_doc_name || 王示例 (SAMPLE PERSON) || text || 0/8/18/19 || yes || SAMPLE
[TABLE_ROW 22] SF-022 || role || role_trm_code || ROLE-TRM-001 || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 23] SF-023 || role || role_trm_name || 張示例 (SAMPLE PERSON) || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 24] SF-024 || role || role_com_code || ROLE-COM-001 || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 25] SF-025 || role || role_com_name || 劉示例 (SAMPLE PERSON) || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 26] SF-026 || role || role_it_code || ROLE-IT-001 || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 27] SF-027 || role || role_it_name || 黃示例 (SAMPLE PERSON) || text || 8/18/19 || yes || SAMPLE
[TABLE_ROW 28] SF-028 || access || group_a_user_count || 3 || count || 13/19 || yes || SAMPLE
[TABLE_ROW 29] SF-029 || access || group_b_user_count || 4 || count || 13/19 || yes || SAMPLE
[TABLE_ROW 30] SF-030 || access || group_c_user_count || 5 || count || 13/19 || yes || SAMPLE
[TABLE_ROW 31] SF-031 || access || total_controlled_users || 12 || count || 12/13/18/19 || yes || SAMPLE
[TABLE_ROW 32] SF-032 || governance || level_0_name || Level 0 政策/方針 || text || 7 || yes || SAMPLE
[TABLE_ROW 33] SF-033 || governance || level_1_name || Level 1 TTQS 管理手冊 || text || 7 || yes || SAMPLE
[TABLE_ROW 34] SF-034 || governance || level_2_name || Level 2 程序/SOP || text || 7/19 || yes || SAMPLE
[TABLE_ROW 35] SF-035 || governance || level_3_name || Level 3 表單/紀錄 || text || 7 || yes || SAMPLE
[TABLE_ROW 36] SF-036 || governance || level_4_name || Level 4 外部參考文件 || text || 7 || yes || SAMPLE
[TABLE_ROW 37] SF-037 || lifecycle || requirement_raised_date || 2026-09-01 || date || 9/18 || yes || SAMPLE
[TABLE_ROW 38] SF-038 || lifecycle || draft_v0_1_date || 2026-09-08 || date || 9/18/19 || yes || SAMPLE
[TABLE_ROW 39] SF-039 || lifecycle || content_review_date || 2026-09-15 || date || 9/18/19 || yes || SAMPLE
[TABLE_ROW 40] SF-040 || lifecycle || draft_v0_2_date || 2026-09-18 || date || 9/18/19 || yes || SAMPLE
[TABLE_ROW 41] SF-041 || lifecycle || quality_review_date || 2026-09-22 || date || 9/18/19 || yes || SAMPLE
[TABLE_ROW 42] SF-042 || lifecycle || draft_v0_9_date || 2026-09-25 || date || 9/18/19 || yes || SAMPLE
[TABLE_ROW 43] SF-043 || lifecycle || approval_date_sample || 2026-10-05 || date || 9/18/19 || yes || SAMPLE
[TABLE_ROW 44] SF-044 || lifecycle || announcement_date_sample || 2026-10-05 || date || 9/12/18/19 || yes || SAMPLE
[TABLE_ROW 45] SF-045 || lifecycle || acknowledgement_deadline_sample || 2026-10-12 || date || 9/12/18/19 || yes || SAMPLE
[TABLE_ROW 46] SF-046 || lifecycle || escalation_date_sample || 2026-10-13 || date || 18 || yes || SAMPLE
[TABLE_ROW 47] SF-047 || lifecycle || last_acknowledgement_date_sample || 2026-10-14 || date || 17/18 || yes || SAMPLE
[TABLE_ROW 48] SF-048 || lifecycle || retrieval_test_date_sample || 2026-10-28 || date || 9/18 || yes || SAMPLE
[TABLE_ROW 49] SF-049 || lifecycle || access_review_date_sample || 2026-10-30 || date || 9/18/19 || yes || SAMPLE
[TABLE_ROW 50] SF-050 || lifecycle || risk_review_date_sample || 2026-11-15 || date || 9/14/18/19 || yes || SAMPLE
[TABLE_ROW 51] SF-051 || lifecycle || periodic_review_due_date_sample || 2027-10-12 || date || 9/16/18 || yes || SAMPLE
[TABLE_ROW 52] SF-052 || obsolete || draft_copies_issued || 3 || count || 18/19 || yes || SAMPLE
[TABLE_ROW 53] SF-053 || obsolete || draft_copies_returned || 3 || count || 18/19 || yes || SAMPLE
[TABLE_ROW 54] SF-054 || obsolete || draft_copies_destroyed || 3 || count || 18/19 || yes || SAMPLE
[TABLE_ROW 55] SF-055 || acknowledgement || ack_required_count || 12 || count || 12/18/19 || yes || SAMPLE
[TABLE_ROW 56] SF-056 || acknowledgement || ack_by_deadline_count || 11 || count || 12/16/18/19 || yes || SAMPLE
[TABLE_ROW 57] SF-057 || acknowledgement || ack_overdue_count || 1 || count || 12/18/19 || yes || SAMPLE
[TABLE_ROW 58] SF-058 || acknowledgement || ack_completion_count || 12 || count || 12/18/19 || yes || SAMPLE
[TABLE_ROW 59] SF-059 || acknowledgement || ack_completion_rate || 100% (12/12) || percent || 16/17/18/19 || yes || SAMPLE
[TABLE_ROW 60] SF-060 || acknowledgement || ack_by_deadline_rate || 91.7% (11/12) || percent || 16/17/18/19 || yes || SAMPLE
[TABLE_ROW 61] SF-061 || retrieval || retrieval_queries || 5 || count || 13/18/19 || yes || SAMPLE
[TABLE_ROW 62] SF-062 || retrieval || retrieval_pass || 5 || count || 13/18/19 || yes || SAMPLE
[TABLE_ROW 63] SF-063 || retrieval || retrieval_pass_rate || 100% (5/5) || percent || 16/18/19 || yes || SAMPLE
[TABLE_ROW 64] SF-064 || retrieval || retrieval_time_minutes || 4 || minutes || 17 || yes || SAMPLE
[TABLE_ROW 65] SF-065 || review || review_comments_raised || 3 || count || 9/19 || yes || SAMPLE
[TABLE_ROW 66] SF-066 || review || review_comments_resolved || 3 || count || 9/19 || yes || SAMPLE
[TABLE_ROW 67] SF-067 || review || quality_findings || 1 || count || 9/19 || yes || SAMPLE
[TABLE_ROW 68] SF-068 || review || quality_findings_closed || 1 || count || 9/19 || yes || SAMPLE
[TABLE_ROW 69] SF-069 || announcement || announcement_id || ANN-0026-001 || text || 9/12/19 || yes || SAMPLE
[TABLE_ROW 70] SF-070 || announcement || announcement_channels || internal portal; email || text || 12/19 || yes || SAMPLE
[TABLE_ROW 71] SF-071 || announcement || announcement_audience_list_id || AUD-0026-001 || text || 12/19 || yes || SAMPLE
[TABLE_ROW 72] SF-072 || exception || exception_id || EC-0026-001 || text || 14/19 || yes || SAMPLE
[TABLE_ROW 73] SF-073 || exception || exception_type || minor editorial correction request || text || 14 || yes || SAMPLE
[TABLE_ROW 74] SF-074 || exception || exception_status || CLOSED ON EXPIRY 2026-11-24 - no permanent change required || text || 14 || yes || SAMPLE
[TABLE_ROW 75] SF-075 || exception || emergency_instruction_id || EI-0026-001 || text || 14 || yes || SAMPLE
[TABLE_ROW 76] SF-076 || exception || emergency_instruction_valid_from || 2026-10-25 || date || 14 || yes || SAMPLE
[TABLE_ROW 77] SF-077 || exception || emergency_instruction_valid_to || 2026-11-24 || date || 14 || yes || SAMPLE
[TABLE_ROW 78] SF-078 || exception || emergency_instruction_status || CLOSED - expired on 2026-11-24; no formal version change || text || 14 || yes || SAMPLE
[TABLE_ROW 79] SF-079 || risk || risk_count || 5 || count || 15/19 || yes || SAMPLE
[TABLE_ROW 80] SF-080 || risk || risk_001_id || RISK-0026-001 || text || 15/19 || yes || SAMPLE
[TABLE_ROW 81] SF-081 || risk || risk_002_id || RISK-0026-002 || text || 15/19 || yes || SAMPLE
[TABLE_ROW 82] SF-082 || risk || risk_003_id || RISK-0026-003 || text || 15/19 || yes || SAMPLE
[TABLE_ROW 83] SF-083 || risk || risk_004_id || RISK-0026-004 || text || 15/19 || yes || SAMPLE
[TABLE_ROW 84] SF-084 || risk || risk_005_id || RISK-0026-005 || text || 15/19 || yes || SAMPLE
[TABLE_ROW 85] SF-085 || pdro || indicator_count || 8 || count || 16/19 || yes || SAMPLE
[TABLE_ROW 86] SF-086 || pdro || indicator_001_id || IND-0026-001 || text || 16/19 || yes || SAMPLE
[TABLE_ROW 87] SF-087 || pdro || indicator_002_id || IND-0026-002 || text || 16/19 || yes || SAMPLE
[TABLE_ROW 88] SF-088 || pdro || indicator_003_id || IND-0026-003 || text || 16/19 || yes || SAMPLE
[TABLE_ROW 89] SF-089 || pdro || indicator_004_id || IND-0026-004 || text || 16/19 || yes || SAMPLE
[TABLE_ROW 90] SF-090 || pdro || indicator_005_id || IND-0026-005 || text || 16/19 || yes || SAMPLE
[TABLE_ROW 91] SF-091 || pdro || indicator_006_id || IND-0026-006 || text || 16/19 || yes || SAMPLE
[TABLE_ROW 92] SF-092 || pdro || indicator_007_id || IND-0026-007 || text || 16/19 || yes || SAMPLE
[TABLE_ROW 93] SF-093 || pdro || indicator_008_id || IND-0026-008 || text || 16/19 || yes || SAMPLE
[TABLE_ROW 94] SF-094 || source || official_evidence_table_sha256 || 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709 || text || 2 || no || OFFICIAL
[TABLE_ROW 95] SF-095 || source || page2_text_sha256 || 3c295e8861ad7775a78583e9111df61ac8733a7cf40d771f942363f00572de9c || text || 2 || no || OFFICIAL
[TABLE_ROW 96] SF-096 || source || crosswalk_sha256 || 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679 || text || 2 || no || OFFICIAL
[TABLE_ROW 97] SF-097 || source || master_blueprint_sha256 || ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216 || text || 2 || no || OFFICIAL
[TABLE_ROW 98] SF-098 || source || dispatch_packet_sha256 || 6e8a1bef2f63d098fcc446de275724d95fbf4f1d326de52f8059070ccd91e110 || text || 2 || no || OFFICIAL
[TABLE_ROW 99] SF-099 || source || unique_blueprint_sha256 || fa02a9846e50c46815220aef2888e5a45518cfafc21b0decbbc8c6542e247876 || text || 2 || no || OFFICIAL
[TABLE_ROW 100] SF-100 || source || r12_execution_spec_sha256 || 8385bb2d33cb8497cc0864625d1da57b96536014b134ced1e7f9b1b05225d23e || text || 2 || no || OFFICIAL
[TABLE_ROW 101] SF-101 || sla || announcement_sla_calendar_days || 7 || days || 12 || yes || SAMPLE
[TABLE_ROW 102] SF-102 || sla || acknowledgement_sla_calendar_days || 7 || days || 12 || yes || SAMPLE
[TABLE_ROW 103] SF-103 || sla || retrieval_target_minutes || 10 || minutes || 13 || yes || SAMPLE
[TABLE_ROW 104] SF-104 || sla || backup_rpo_hours || 24 || hours || 13 || yes || SAMPLE
[TABLE_ROW 105] SF-105 || sla || backup_rto_hours || 8 || hours || 13 || yes || SAMPLE
[TABLE_ROW 106] SF-106 || sla || periodic_review_interval_years || 1 || years || 9/16 || yes || SAMPLE
[TABLE_ROW 107] SF-107 || sla || access_review_interval_months || 12 || months || 13/19 || yes || SAMPLE
End of artifact. All synthetic data is SAMPLE/SYNTHETIC and must be replaced before real use. No real approvals, signatures, third-party originals, certification, or REAL performance claims are included.
