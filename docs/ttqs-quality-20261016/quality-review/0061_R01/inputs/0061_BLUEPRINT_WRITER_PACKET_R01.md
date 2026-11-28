# 0061 Blueprint 專屬隔離來源封包 R01

本封包只供 TTQS_ONE / doc_id 0061。本機 HEAD: 9edb57e3cf10e0a96d6f2654a841824a5bc216f0
遠端 branch 在封包建立前已讀回相同 HEAD；此次只提供來源與專屬輸入，不授權 Worker 存取整個工作區。
所有規格以 Git blob SHA 識別；候選映射列的 historical_blueprint_source 僅供追溯，歷史正文禁止當模板。

## 來源 manifest (SHA-256 / Git blob)
{
  "01_HUMAN_MISSION_AND_ACCEPTANCE.md": {
    "path": "docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md",
    "git_blob_sha": "538bedb9d87e8465f43151933b4a5c1bfa4bbc4e"
  },
  "02_GENRE_WRITING_MANUAL.md": {
    "path": "docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md",
    "git_blob_sha": "4ff863d9f534b6359fc1c7c1685bd8cce02da886"
  },
  "03_157_CHECKBOX_BLUEPRINTS.md": {
    "path": "docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md",
    "git_blob_sha": "8c2bbe7ca9dcbb03088a48934b9e57e7147ede63"
  },
  "04_CODEX_GOAL_24X7_EXECUTION.md": {
    "path": "docs/ttqs-quality-20261016/04_CODEX_GOAL_24X7_EXECUTION.md",
    "git_blob_sha": "62e3dd7dfd8579b6bc97952ffa6236e7494f3b4d"
  },
  "06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md": {
    "path": "docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md",
    "git_blob_sha": "263aaca84891bba8dca087875804343c3670e921"
  },
  "official_source.pdf": {
    "path": "docs/ttqs-quality-20261016/quality-review/0037_R07/inputs/official_source.pdf",
    "sha256": "805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709",
    "extracted_page": 5
  },
  "0060_R08.docx": {
    "path": "docs/ttqs-quality-20261016/quality-review/0060_R01/candidate/0060_R08.docx",
    "sha256": "92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3"
  },
  "0060_R08_register.csv": {
    "path": "docs/ttqs-quality-20261016/quality-review/0060_R01/sidecar/0060_R08_SYNTHETIC_REPLACEMENT_REGISTER.csv",
    "sha256": "ADD1F2BCF77C77DF6BA921E1DFA68494AC867A3E3368B795AA56C439AA824C4B"
  },
  "0060_R08_reviewer_receipt.md": {
    "path": "docs/ttqs-quality-20261016/quality-review/0060_R01/review/opencode_v2_semantic_R08/independent_review_receipt_R08.md",
    "sha256": "9528A766E582936AE17D0CD5674F02CE2165069B64BAFA03220D7E65925507C3"
  }
}

## Human Mission / association facts and safety limits
# TTQS ONE｜原始點協會逐方框高品質文件總施工契約（Human 2026-10-16 候選）

> **身分：CANDIDATE／Human 新版施工方向的公開規格草案。** 此檔非正式 TTQS 評核結果，不自動覆寫已接受 Mission，不代表任何歷史 DOCX 已驗收。適用專案僅為 TTQS_ONE；與舊 canonical 有差異時標示 SPEC_CONTROL_PLANE_REBASE_REQUIRED，依 Human 最新 Mission 合法執行已批准的可逆施工，正式接受仍要證據。
>
> **最高要求：AI 交付成熟、完整、真正有內容的專屬 Word；Human 核實、修正、刪除及正式核定，不是補填一百多份空白考卷。**

## 0. 目標、基準、證據

- 目標：替「屏東縣原始點關懷協會」建立符合其真實定位的小規模訓練機構 PDDRO 文件體系；包括可操作的辦訓制度、完整可修改的示範文件、可信的資料與來源追溯。該組織名稱可由 2026-10-05 GitHub 備份的文件名稱確認；其法定資料、活動、會員、管理角色、經費、成果均須另外查實，不得因檔名推定現役事實。
- 公開依據：勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》9 頁，https://ttqs.wda.gov.tw/download_files/6475978659d646f58e3eddc3b1ea51d9/TTQS%E6%9F%A5%E6%A0%B8%E4%BD%90%E8%AD%89%E6%96%87%E4%BB%B6%E8%B3%87%E6%96%99%E8%A1%A8-%E8%A8%93%E7%B7%B4%E6%A9%9F%E6%A7%8B%E7%89%88.pdf 。規格用獨立中文改寫與內容設計，不逐字轉載整本受保護教材。適用法規、評核表、標準作業手冊應依最新正式版本核對。
- 方框基準：157 格、129 個具名佐證、28 個「其他：」。28 個「其他」未具體命名真正獨特且適法的補充需求前，保持 BLOCKED_UNTIL_UNIQUE_OTHER_NAMED，不做 28 份「其他.docx」。歷史 142 DOCX 是專案舊版規劃序列，**不是官方要求或已達標數量**；比對舊 registry 之後再決定具體 1:N 拆件。
- 已讀 GitHub：2026-10-05 submission 分支上傳 2,324 個歷史 DOCX/版本（含重複、失敗、未驗收）；非合格總數。使用者轉交 2026-10-15 Codex 稽核曾列 24 個活躍可開啟 ID 與 4 件內部 exact-SHA reviewer PASS；未經本檔在 Windows OS 上重讀，不冒充 LIVE/正式 TTQS 接受。
- 分類：LIVE／CANONICAL／CANDIDATE／HISTORICAL／UNKNOWN。來源、日期、適用範圍、原件定位、核准身分各自記錄；未知不能填 0、已完成或 PASS。
- 儲存庫是公開的。不要提交個資、真實學員名單、未公開財務、簽章、醫療資料、未公開合約、密碼、金鑰、Token、私密照片或第三方證明；此規格僅含公開要求、去識別可公開建議、清楚標示的 SAMPLE。

## 1. 每個方框都有自己的正確文件類型（genre）

一個 checkbox 是一個獨立要求，但其實際完整成品可能是 1:N 份。以「評核委員打開要看到什麼內容」反推 Word，而不是取到標題就生四段通用說明。

| 類型 | 必須真正寫出的內容 | 一票否決的假成品 |
|---|---|---|
| 策略地圖 | 看得見的因果圖：宗旨/受眾→需求→訓練類別→能力→活動→成果→三年指標，責任與風險 | 七個標題、純 SWOT、只有口號 |
| 市場調查 | 可以發放的真問卷、填答完整示例、樣本執行紀錄、分母分子、交叉分析、結論與決策 | 只說「調查、分析、改善」 |
| 訓練政策／公告 | 實際政策條文、服務對象、招生規則、品質承諾、課程頁/EDM 文案、對外揭露版本 | 一句「應對外公告」 |
| SOP | 角色、輸入、入口、步驟、分支、檢查點、例外、期限、輸出、紀錄、版控 |「規劃→執行→紀錄」 |
| 會議 | 具體議題、資料、相異意見、方案比較、決議、負責人、期限、追蹤 | 只有日期、參與者、結論三空欄 |
| 課程設計 | 職能落差、可測目標、單元教學、師資、教材、選員、設備、評量設計、目標對應矩陣 | 單頁「課程名稱、師資、時間」 |
| 採購遴選 | 準則/權重、候選者比較、利益迴避、採購流程、例外、契約、履約後評、完整示例計算 | 資源採購一般性文字 |
| 結案報告 | 班別、需求/目標、實際執行、學員/出勤、教學品質、師資、預算/實支、訓後效果、異常、改善追蹤 | 只列財務五欄 |
| 17a–17d | 反應、學習、行為、成果，逐層不同工具、樣本、指標、分析、改善；與 18/19 相接 | 用滿意度假扮就業/營運績效 |
| 複合項目 | 考試、心得、照片索引、職涯建議等不同文件各自成篇、共享 case_id | 把四種產物擠成一張事件表 |
| 第三方原件 | 原件取得需求、請求稿、保管清冊、例證位置；正式原件仍待真實來源 | 假感謝函、假保險、假證照、假雇主或公文 |

## 2. 原始點協會的適切性與低維護成本

先讀取實際可追索的 association source sheet：正式名稱/核准、宗旨、課程與對象、辦訓歷程、真實管理人力與志工分工、授權層級、年度策略、財務限制、可查原始成果。每欄有 source、date、locator、REAL/UNKNOWN、replacement；找不到就保持未知。
- 不發明大型企業式專責委員會、管理部門或 ERPs；小型協會可以提出精簡角色/志工與行政分工的建議制度，但不得說這就是「本會現行組織」。合法簽核人依真實章程/授權查核。
- 健康促進、社區關懷、志工培育、照護知能、非醫療傳統整復推拿教育等**只在真實來源或已標 SAMPLE 情境**中採用；不能聲稱醫療治療、臨床療效、醫療執照或依法未取得之資格。不同課程案例不強迫共用一個。
- 中長期可設定階段性策略與 KPI 算法，不無來源鎖死三年班數、人數、收入、獲獎、會費與就業率。財務/資格/雇主成果未證實則不得偽裝現況。
- 优先使用協會可負擔的 Word、Excel、簡易索引、合法有權限的既有雲端資料夾；不自行發明第二套全職行政與系統。

## 3. 每份 DOCX 第一頁與正文的內容品質

第一頁用平實台灣繁中 30 秒說清：文件是什麼、回答哪個指標/方框、誰用、實際內容所在、對應案例/來源、SAMPLE/REAL。此頁只是導引，**不能占滿一頁後正文只留空格**。
- 人類正文嚴禁出現原料欄位、JSON、括號鍵值、程式碼、技術控制字串（如 rubric_descriptions、competency_name、question）、AI 附註、內部 SHA / queue metadata、泛用「先看這裡」表格。
- 正文字級至少 10.5 pt，表格至少 9.5 pt；表格標頭清楚，跨頁重複表頭；不得壓字、截字、孤頁、大片空白表，不能靠縮小至 6–8pt 偷渡內容。
- 可發放給學員的問卷允許必要的空答欄，但必須**另有已完整填好的 SAMPLE 答卷與分析**；空的訓後執行紀錄不得冒充示範實績。
- 每一種文類有自己必備章節與欄位。詳見 02_GENRE_WRITING_MANUAL.md；每個方框的專屬內容見 03_157_CHECKBOX_BLUEPRINTS.md。

## 4. SAMPLE/REAL 及第三方原件不可造假

缺少真實營運事件資料時，生成成熟完整的 SYNTHETIC_COMPLETE_DRAFT：合理日期、角色、調查問卷和樣本、計算過程、數據、會議內容、決議、追蹤、改善並前後一致。每項虛構事實進 SYNTHETIC_REPLACEMENT_REGISTER：
- fact_id；case_id；doc_id；段落/表格定位；值；假設理由；引用同一事實的其他 doc；正式替換所需原始來源；待核實之真正負責人；狀態。
- 展示 DOCX 必須明顯標「完整示範資料／非協會實際辦訓、認證、簽署或核准紀錄」，且文中批准用「示範判定」「預擬方案」等措辭，絕不混入「本文件已由本會主管正式審定」等假權威。
- 感謝函、政府函、聘書、保險、證照、銀行/會計、雇主證明、學員就業、薪資調整、媒體報導、獎項與簽章：只可寫可用的索取稿/格式示例/取得台帳，不偽造已出具的第三方原件；未取得正式原件要標 UNKNOWN/PENDING_REAL_SOURCE。這不妨礙其他候選示範文件繼續生產。

## 5. 每個交付件的專屬 Blueprint 欄位

checkbox_id、indicator、page、requirement_summary、doc_id、document_genre、why_this_document_exists、reader、source_facts_with_page_locator、case_id、章節清單、專用表格及欄位、問題/選項/量尺、必要圖表、計算/分母、流程分支、SAMPLE 假設、與其他文件 fact_id 交叉索引、需要第三方原件、禁止造假、相似錯件（negative_neighbor）、拒收條件、source_SHA、blueprint_hash、artifact_SHA、fresh_review_source、promotion_status。

不可在未讀既有 142 序列前自動重編文件號。凡複合需求須以實際文件用途拆件、建立 1:N；29? 不得憑空新增「其他」件數。28 個 Other 一律保持未命名封鎖，不湊數。

## 6. 硬驗收與反模板，不是數字抽樣就通過

任何以下問題**一票否決**：
1. 文件類型錯誤：感謝函變問卷、策略圖變章節樹、成果移轉變空泛會議、結案變只有會計欄。
2. 問卷沒有完整題目/選項/量尺；評估沒有評分準則/實測示範；分析沒有分母/期間/來源/可理解解釋；SOP 沒有決策與異常。
3. 以「待填／待核／空白表／保持空白／會後填寫」充當完成內容。僅清楚隔離的 REAL 替換區、可發放原始表件可以合法例外，且另有完成示例。
4. 不同題材的文件大量共用同一段落骨架、表格 schema 或近義換字正文。共同封面/固定註記不計入實質正文相似度。
5. 沒有 SAMPLE 明示或未登錄 synthetic；公式不合、時間顛倒、cross-doc fact_id 矛盾、虛假核定或第三方原件。
6. DOCX 損毀、無法開啟、無法人眼閱讀、內容鍵值外露、字級縮過限、頁面裁切與大量空頁。
7. 新 SHA 只由 builder 自評 PASS，沒有獨立 review 綁同一精確內容；GitHub merge、CI exit 0 不等於文件正式驗收。

**Fresh semantic reviewer 的工作**：遮掉檔名、頁眉與通用前言，只讀中央內容做 title-blind 類型辨認；與最相似的三個錯件需求比較（negative-neighbor），必須能說出為什麼此件獨特、內容錯誤定位；實際讓訓練行政可使用它完成工作；追蹤 P→D→Do→R→O 與 SAMPLE/REAL；內容不一致要具體標記正文位置。

**證據層次**：DRAFT → BUILT → STATIC_VERIFIED → FRESH_SEMANTIC_VERIFIED → CURRENT_CANDIDATE；後續 HUMAN_ACCEPTED / REAL_REPLACED 是獨立身份。不能只因新增審查欄位就將原 exact SHA 的既有 PASS 降級；若真有同一 exact SHA 的實際內容錯誤，用定位與反例退件。

## 7. 歷史退件案例（固定回歸）

- 002 市場需求調查：只有「對象／蒐集／分析」而無問卷、樣本、分布、分析結論。
- 061 成果移轉檢討：僅泛用會議格式，缺學習運用、實際行動計畫、追蹤與成效。
- 072 結案：只剩會計期間、收入、成本與對帳表，無完整訓練閉環。
- 084 考試＋心得＋照片＋職涯建議：複合不同用途被壓成一張事件紀錄。
- 094 訓後調查：連題目、答案選項、量尺都沒有。
- 104 感謝函：變成問卷統計，甚至可能偽裝第三方來函。
- Wave005 舊 0031–0040 多用「待填、待核、空白表」、曾沿用 CP006 位元，Human 已宣布舊 PREVIEW_READY 失效；新候選 0031 仍有 rubric_descriptions 等原料/「正式審定」誤導；0032/0033/0039 部分有待驗缺陷。**不能把這段歷史 finding 當成本次 OS 直接確認的每件現狀。**

根因修復：受影響範圍依確切污染證據評估；從官方要求、可核實原始資料與專屬 Blueprint 重建，不能拿失敗 Word 或別份成品正文改標題。不要每遇缺陷就疊一套新 Validator/Bus/DB/多重人工 Gate。

## 8. 自動長時作業的合法邊界

Human 2026-10-16 已要求：已批准的可逆 CANDIDATE 文件重建、獨立 QA、回收成果、修補缺陷繼續由 Codex/合格原生 Worker 自動進行，十件一批是非阻擋回報，不必逐批求准。若先前 pause=true，先從 OS/實際 Policy 定位其來源和作用範圍；Human 最新授權可解除舊控制對可逆候選施工的過時限制，**不能**自行解鎖正式送審、簽章、付款、Production、身份、OAuth/MFA 等真正保留的 Human Gate。
- 長時 24/7 是合格 Windows 原生 Worker/OS Scheduler 的目標（有額度、服務可用與裝置運作前提）；ChatGPT Web/暫時對話不是 24/7 daemon。沒有實際 OS 存活與定時器 readback，不能說已啟動背景執行。
- 一個 BUILD、一個 REVIEW，可並行不同文件；同一資料與 CURRENT/shared register 僅一個寫入 owner。先沿用專案已驗證工具，不因缺 Factory MCP 阻止本機。
- 未見實質變更，L0 只做 hash/Git/原生事件，不浪費高階模型；配額或單個 Worker 故障只阻該 lane，其他 READY 工作繼續。
- 專案正式來源與候選新方向牴觸時標 SPEC_CONTROL_PLANE_REBASE_REQUIRED；舊權威為遷移證據，不是永久自鎖條件。

## 9. 合格完成定義

每一份能打開的 DOCX 都必須：對準官方具名需求、是對的文類、內容具體而非待填、專用圖/表/問卷/流程有效、數學與樣本因果鏈一致、SAMPLE/REAL 清楚、第三方原件不造假、跨文件 trace、fresh reviewer 綁 exact SHA、版面可閱讀、易找且可供 Human 隨機開檔。129 個具名需求按其性質對到完整作品/第三方來源取得流程，28 個 Other 有清楚非具名處理；正式 TTQS 送審須 Human 核實與 REAL 證據。

**檔案存在 ≠ 內容合格；內部 QA ≠ TTQS 官方分數；SAMPLE 完整 ≠ 協會已實際執行。**
 
## Official genre-writing guidance: Indicator 14
## 指標 14｜訓練資料系統化（五項）

**分類編碼**：文件種類、機密等級、保存期、權限與實例編碼。
**檔案管理**：索引欄位、進出庫、權限範例、版本/備份/復原；不能憑空聲稱現成 ERP。
**全套建檔**：從需求到 Outcome 的逐檔資料清單，能以可點擊路徑追溯。
**查詢功能**：查詢用途、實際測試查詢與結果、失敗查詢及改善。
**資訊效率**：檢索速度的試驗方法、條件、樣本、測次與結果；非實測數據須標 SAMPLE。

## Exact official checkbox 066 and adjacent items

066｜**檔案管理系統：索引、權限、檢索、備援**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

067｜**訓練文件建檔：需求到成果原件清冊、真實定位**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

068｜**查詢/持續改善：查詢案例、失敗紀錄、改善**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

## Source-first construction rules
# CODEX GOAL｜TTQS ONE 原始點協會高品質 Word 長時自動施工命令（CANDIDATE）

COMMAND=TTQS_ONE_REBUILD_FROM_SOURCE_QUALITY_FIRST
PROJECT_ID=TTQS_ONE
HUMAN_MISSION_DATE=2026-10-16
OUTPUT=FULLY_WORKED_DOCX_PER_NAMED_CHECKBOX
MODE=AUTONOMOUS_REVERSIBLE_CANDIDATE_CONSTRUCTION
SPEC_BRANCH=work/ttqs-one-document-quality-contract-20261016

## 1. 這次不能再交低品質模板

AI 幾十次失敗是因為只換標題、泛用四段式、沒有實際題目、沒有原始資料、資料不一致、表格空白、文件類型錯置、內部 JSON/鍵值直接洩漏到 Word，且自稱品質已經 PASS。本次 Human Mission：AI 要先把完整、合理、可操作的成熟文件做出來，讓 Human 只核實、修改與核定，絕不是讓 Human 填空白考卷。每件必須能由評核委員直接閱讀與逐項調閱。不得因生成 142 份或任何退出碼而聲稱完成。

## 2. 本次完整施工規格

必須先完整讀取 GitHub 本分支 docs/ttqs-quality-20261016/ 底下：
01_HUMAN_MISSION_AND_ACCEPTANCE.md
02_GENRE_WRITING_MANUAL.md
03_157_CHECKBOX_BLUEPRINTS.md
05_HOURLY_NATIVE_WAKE_RESUME.md：Human 明確批准每 60 分鐘喚醒目前這條 Codex GOAL；優先用 Codex App 原生同對話 Scheduled task，不可用才借現有 Windows Task Scheduler，兩者不可雙主。必須真正安裝、讀回、煙測，未知不得說 ACTIVE。

三份是一起生效的 Human 最新 CANDIDATE 細化契約，不得只讀這份 GOAL。官方 PDF 訓練機構版參考佐證 157 格、129 具名和 28 個 Other 的逐格核對，必須比對現有正式 Blueprint 與 142 份生產序列；方框號不是 DOCX 號，不得自行重編。每個方框/拆件都要自己的 genre、獨有章節、圖表/問卷、計算、分母、來源、示範與可驗收結果。不能把其他文類的正文套過來。

## 3. 精確專案與新鮮接管

從 PT-Original-Point/ttqs-one 的正式 Mission/Spec、原生 Issue/PR/accepted 工作讀回當前權威；本次候選分支沒有主權，與舊控制矛盾標 SPEC_CONTROL_PLANE_REBASE_REQUIRED，舊控制僅作切換前證據，不得阻塞 Human 新授權的合法可逆候選文件施工。
在 Windows 實際讀 E:\TTQS\TTQS_ONE_CODEX_RUNTIME 的 CONTROL、WORK、CURRENT、BUILD_QUEUE、SYNTHETIC_REPLACEMENT_REGISTER、最新 DOCX exact SHA/OS Worker/Pause/任務排程。核對 Google Drive 中央總庫、原始資料庫、GitHub 2026-10-05 submission 分支。不能把 repo 2,324 歷史 DOCX/版本當成合格成品；2026-10-15 報告的 24 active ID、4 reviewer PASS、Wave005 0031/0032/0033/0039 FAIL 都要新鮮檢驗。2026-10-05 舊 deadline 已過期，不當作當前權威。
查 pause=true 具體來源和受影響 lane；Human 2026-10-16 明確批准可逆候選重建/QA 自動繼續，但不能擅自解除 Production、簽署、資金、契約、個資、第三方或其他真正 Human Gate。

## 4. Source-first，完整做對一份才前進

對每個 READY deliverable：
A. 定位官方獨立 checkbox、既有 Blueprint、精確 doc_id 與必要 source。
B. 讀協會真實來源、相關既有合法文書、歷史成品（只借可核實事實，絕不借用失敗正文）、官方規範與可合法借鏡的公開優良案例。
C. 先寫獨特的內容大綱/專用表格欄/真實題目/圖/計算/決策，不能只有四大段與空欄。完稿要具備實際用處，市場調查有問卷＋數據＋結果；SOP 有角色、流程分支、輸入與輸出；結案有完整訓練閉環；成果移轉有30/60/90天追蹤；不同文件 genre 各自完整。
D. 真實缺資料就寫可用、邏輯一致、數字可重算的 SAMPLE/SYNTHETIC 完成示例，標示非實績並於既有 replacement register 逐個 fact_id 註冊；不得寫假核准、假簽名、假證書、感謝函、媒體報導、保單或就業證明。
E. 寫真正成熟、可打開的中文 DOCX。第一頁30秒看懂用途/資料性質；正文字級至少10.5pt、表格至少9.5pt；不能暴露 rubric_descriptions/competency_name/question/JSON/程式碼或技術 metadata。
F. 先跑確定性檢查，再由不同於本文件 Builder 的 fresh reviewer 以 exact SHA 讀實際正文，執行 title-blind、負向相鄰需求、專用功能、跨文件數字/日期、SAMPLE/REAL、正式可讀性；只驗證實際修復文件，不以自評 PASS 升格。
G. 個別 FAIL 附具體段落/表格 locator，從官方+真來源+Unique Blueprint 修復；不要再把失敗 Word 或旁邊 Word 當模板。兩次無實質進展停該 lane 做根因審核，其他 READY 正常繼續。
H. 單一 writer 序列化共享 register/CURRENT，候選交付附 exact SHA、QA 收據、來源與替換清冊。十件是一批非阻擋報告，不需 Human 反覆發「繼續」。

## 5. 優先處理現在已知問題

先 fresh-read Wave005 0031/0032/0033/0039 和 0054：0031 不得殘留鍵值原料、不實正式核定；0032 需真正正確的能力/組織適配；0039 真正會議議題/決議/追蹤；0054 依 exact SHA 完成 fresh review。不能因舊文字誤傷一件內容已合格的另一 SHA。其餘 READY 工作按最有高品質產值優先。保留 28 個 OTHER 不亂生文件。

## 6. 真正長期連續執行

GOAL：持續把 129 個具名官方 checkbox 的需要文件做成高品質、可調閱的完整 Word，依必要複合要求拆件，達到實質語意/閱讀/一致性驗收；完成率只計 fresh semantically verified 的具名需求，不計檔名、空模板或歷史版本。

24/7 執行只能透過當前 Windows 合格原生長時 Worker 或 OS Task Scheduler（有主機開機、配額、網路及平台限制），不是 ChatGPT Web 或這個 Chat 會永久執行。先讀既有 scheduler/job/Worker，優先重用，不創造第二套 agent bus、主管服務、DB/MCP。沒有真實 OS 持續排程，就標 UNKNOWN/NOT_INSTALLED，不自報背景工作。
單 BUILD lane ＋另一獨立 REVIEW lane 可在不同文件並行，同一寫入範圍一個有效 writer。模型失敗、quota、429、傳輸、單份文件失敗只阻該 lane，其他 READY 繼續；無實質差異時 deterministic L0 不呼叫高階模型。必要共享寫入採 fresh prestate、exact scope、必要 CAS/冪等、一次派發、同來源讀回，未知不盲重試。

## 7. 真實交付與 Human Gate

每次非阻擋進度摘要包含：正式 Spec 與候選 Spec/ref/SHA、文件新 SHA/位置、獨立 QA/失敗定位、SAMPLE replacement delta、已覆蓋的具名 checkbox、READY 與範圍明確的阻擋、真實 OS Worker 狀態、下一個合法動作。正式 TTQS 送審、簽章、法律/契約、外部不可逆權限擴張、新費用、Production、OAuth/MFA、無法釐清的重大外部效果與最終正式 package 才是 Human Gate。這不是要求每10份審批。

**現在就先新鮮讀控制/來源/實際 OS worker、確認最近一個可逆 READY 文件、建立專屬大綱並重建成熟 DOCX，獨立 QA、發布可調閱候選、繼續下一份。不得只回「已理解」。**
 
## Exact current deliverable mapping row for doc_id 0061
{
  "deliverable_id": "0061",
  "requirement_id": "I14-E02",
  "final_filename": "0061__訓練檔案管理系統_完整工作稿.docx",
  "document_genre": "專屬佐證紀錄｜訓練檔案管理系統_完整工作稿",
  "document_purpose": "本件專屬焦點：訓練檔案管理系統_完整工作稿；需直接回應的官方佐證要求為：訓練檔案管理系統。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。",
  "primary_user_or_reader": "供執行人員、主管與評核閱讀者追溯要求、事實、證據位置及覆核狀態。",
  "evidence_role": "保存此項要求專屬的原始紀錄或證據索引；不代替第三方原件。 本文件只擁有 I14-E02 的直接紀錄／分析口徑；不得吞併其他要求的事實。",
  "source_of_truth": "官方查核佐證表精確原文『訓練檔案管理系統。』，表內頁次 5，讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH；REQ_157_MAP 對應 I14-E02；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。",
  "required_sections": "紀錄目的、責任及適用界線；官方要求拆解與證明路徑；來源、形成時點及納入規則；欄位定義及證據位置；完整合成紀錄示例；核對、計算與一致性判定；例外、缺證及更正軌跡；真實原件與合成示例的區別；覆核、保管及調閱規則；相關要求及文件交叉引用；真實資料替換清單；附件索引與版本",
  "required_tables_or_figures": "欄位—定義—來源—填寫者—驗證規則；完整合成填寫列及欄位解說；問題／例外—修正—覆核及追蹤；官方要求—表單欄位—附件定位追溯表",
  "required_fields_or_questions": "合成資料識別碼；日期欄位及合成標示；責任角色代碼；來源／附件位置欄位；判定、理由、覆核及後續行動",
  "required_calculations_or_analysis": "若此表單有數量、金額、期間或比例，明列定義、分子分母與逐步算例；若沒有，明示不適用並提供至少一個欄位驗證／完整度判斷示例。",
  "required_cross_references": "同要求分件 無；相鄰要求 I14-E01, I14-E03；共用原始來源時只引用核實結果，不複製別份文件正文。",
  "real_data_required": "升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。",
  "third_party_evidence_required": "若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。",
  "prohibited_fabrication": "不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。",
  "title_blind_test": "遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『訓練檔案管理系統_完整工作稿』並證明『訓練檔案管理系統。』；若可無修改移作其他要求即失敗。",
  "negative_choice_neighbors": "0060《訓練資料與訓練過程及成果的紀錄與分類，均有系_可直接使用成品》（I14-E01）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0062《完整的訓練文件建檔資料_完整工作稿》（I14-E03）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。",
  "acceptance_tests": "移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『訓練檔案管理系統_完整工作稿』，且能指出直接回應『訓練檔案管理系統。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。",
  "document_role": "evidence_record",
  "official_requirement_text": "訓練檔案管理系統。",
  "official_checkbox_text": "訓練檔案管理系統。",
  "official_evidence_table_page": "5",
  "official_source_readback_status": "PDF_TEXT_EXACT_PAGE_MATCH",
  "official_visually_checked_pages": "",
  "requirement_deliverable_siblings": "0061",
  "docx_body_template_policy": "FROM_SOURCE_ONLY; old body is discovery evidence only and prohibited as rebuild template; Wave005 R3 0031-0040 quality-height references only; Wave001-004 tainted; old Wave005 invalid; Wave006 prohibited.",
  "synthetic_population_rule": "缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。",
  "historical_blueprint_source": "16d34ab6c7188aba8cc28fcd6a1354c04e03030b1aba3e6a261b481170d33f8b",
  "historical_body_use": "PROHIBITED",
  "source_map_notes": "129 exact official requirement rows + reconciled 142-ID crosswalk; official source PDF and exact Drive readback evidence are recorded in runtime SOURCE/CONTROL maps."
}

## Official evidence-table PDF: page 5 text extraction
5 
項目 評核指標項目 
內涵說明（以下為
例，但不以此為
限） 
常見參考佐證資料 
（並註明資料來源及頁碼） 
進訓練成果轉移的
達成並展現適當資
料說明。 
 業主提供回訓或相關機制、學
習心得交流的平台、證照、實
習或其他相關機制的建議或協
助，展現訓練成果轉移的達成
並展現連接性執行。 
 其他： 
14.訓練資料分
類與建檔
及管理資
訊系統化 
展現訓練流程相關
文件有適當系統化
紀錄，並有分析及
運用紀錄。 
對訓練流程相關文
件或紀錄有適當的
保存及建檔。 
 訓練資料與訓練過程及成果的
紀錄與分類，均有系統化歸納
方法編碼。 
 訓練檔案管理系統。 
 完整的訓練文件建檔資料。 
 是否提供查詢功能，並具持續
改善機制。 
 資訊系統化程度及檢索速度。 
 其他： 
查核 
（Review） 
15. 評估報告及
定 期 性 綜 合
分析 
展現定期的課後檢討
紀錄及適當的審查檢
討改善機制。 
課後檢討紀錄應展現
學員建議及回饋、訓
練需求、訓練目標、
訓練方法等之檢討。 
 訓後定期性綜合檢討或管理審查
制度會議紀錄。 
 訓練的結案報告，包括資源的運
用、財務的支配、訓練成果的展
現、檢討及改進的方法。 
 訓練執行評估指標分析及相關統
計分析。 
 訓後改善建議追蹤報告。 
 其他： 
16. 管控及異常
矯正處理 
展現整體訓練過程
中，有持續管控且符
合程序要求，並彙整
結果進行定期（年
度）審查。 
建立適當的程序辦
法，訓練流程異常
時，應有紀錄及因應
措施，必要時採取適
當矯正措施防止再
發。 
 訓練流程的管控方法及紀錄。 
 訓練異常處理方法、紀錄與工
具。 
 訓練的內外稽核流程與紀錄。 
 其他： 
成果 
（Outcome） 
17. 訓練
成果評估
的多元性
和完整性 
17a 
反應
評估 
0分 未執行。 
1分 執行滿意度調
查。 
2分 依滿意度調查分
析，學員/講師回
饋，彙整分析作為下
次課程規劃之修正依
據。 
 課後滿意度調查分析與課後檢討
講師、學員、人資、部門主管等
利益關係人的建議回饋紀錄。 
 課程結案報告（含問卷調查統計
分析、課程規劃紀 錄等含對後續
課程的開課建議事項）。 
 依反應評估進行課程改善的行動
方案。
 
## Related 0060 R08 reviewer receipt; candidate only, not association formal acceptance
# 0060 R08 independent review receipt

## Candidate and authority
- DOCX ID: 0060
- Official requirement: I14-E01
- Official checkbox: 065
- Candidate: `candidate/0060_R08.docx`
- Exact SHA-256: `92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3` (71,613 bytes)
- The run record verifies the same SHA before and after review (`candidate_unchanged=true`).

## Independent review
- Route: OpenCode CLI v2.0.29; requested model `opencode/mimo-v2.6-flash-free`
- Status: **PASS**, CLI exit code 0; 1,295.007 seconds; stderr empty.
- Review packet SHA-256: `A199AF449FDAF991FFFA09C66585D76B873A3CADCA120E31AE1A70CB3E0C8645`
- Raw stdout SHA-256: `E996ADFD3E90BBE42CCA3142F9A3B842379B50746FC00ADFF39FA38E5D93A34D` (6,362,140 bytes)
- Extracted reviewer response SHA-256: `3FF43230E66AD33375DC06A35A2AC6EF52B492F586DF01473D0E1121B7452E23`
- Run receipt: `review/opencode_v2_semantic_R08/attempt01_mimo_v2_6_flash_free/run_R08_attempt01.json`
- Reviewer response: `review/opencode_v2_semantic_R08/independent_review_response_R08.md`

## Verified scope and limits
- All 11 packet checks passed; the four prior R07 semantic findings were closed, register parity was 12/12, and the 66-row SAMPLE register had no blank cells or forbidden literals.
- Arithmetic and cross-table lineage were independently recomputed. The candidate matches the packet and did not change during review.
- The 26-page Word export was verified; the four changed pages (18, 19, 20, 23) were inspected directly, and 22 unchanged page images matched the R07 baseline byte-for-byte. The reviewer directly inspected 15 full-resolution pages.
- One non-blocking observation: 17 table-caption runs are 10.0 pt. The reviewer found them legible; body prose is 11 pt and table body 9.5 pt.
- The official PDF page was checked using its hash and extracted text; direct visual reading of the official PDF was unavailable to the reviewer. PDF layout claims rely on rendered page images and text extraction.
- This is an independent candidate review, not Human or association formal acceptance. The document remains a SAMPLE/SYNTHETIC candidate; no real activity or approval is asserted.

## Related exact hashes
- Word-export PDF: `B9850431F0A002E788EC21B4432F47A4F8309E067759C3A7FAB6D95AD3B43BAB`
- Synthetic replacement register: `ADD1F2BCF77C77DF6BA921E1DFA68494AC867A3E3368B795AA56C439AA824C4B`
- Visual receipt: `evidence/visual_review_R08.json`
- Technical QA receipt: `evidence/technical_qa_R08.json`
 
## Selected 0060 R08 synthetic facts (case context only; do not fabricate/alter)
fact_id,case_id,doc_id,locator,value,synthetic_assumption,real_source_to_replace,role_to_verify,status
SYN-0060-FACT-001,SYN-0060-2026-A01,0060,第一章導讀、第六章表6-1、第七章表7-1、第九章表9-1,SYN-0060-2026-A01 (簡稱 SYN60A),示範專案案號代碼，不代表真實組織專案編號,正式核定之開課專案案號,訓練經辦功能,SAMPLE
SYN-0060-FACT-002,SYN-0060-2026-A01,0060,第七章表7-1、第九章表9-1、第十一章表11-3,社區志工接待與資源轉介界線,示範課程名稱，非本會歷史開課紀錄,正式開課計畫與簡章之課程全名,教學主責功能,SAMPLE
SYN-0060-FACT-003,SYN-0060-2026-A01,0060,第九章表9-1、第十章表10-1、第十一章表11-3,2026-08-15,示範授課日期，非本會實際開課日期,實體簽到表所載之實際辦訓日期,訓練經辦功能,SAMPLE
SYN-0060-FACT-004,SYN-0060-2026-A01,0060,第九章表9-1、第十章表10-1,2026-09-14,示範成效追蹤日期，非實際調查日期,實際完成電訪或追蹤紀錄之簽署日期,檔案督導功能,SAMPLE
SYN-0060-FACT-005,SYN-0060-2026-A01,0060,第十章第二段、第十章表10-1、第十一章表11-3,12人,示範報名人數，用作計算分母,報名系統或收件清冊之核定報名總人數,訓練經辦功能,SAMPLE
SYN-0060-FACT-006,SYN-0060-2026-A01,0060,第十章第二段、第十章表10-1、第十一章表11-3,10人,示範到課人數，用作出席計算分子與評量分母,現場簽到名冊實際完成簽到之人數,訓練經辦功能,SAMPLE
SYN-0060-FACT-007,SYN-0060-2026-A01,0060,第十章第二段、第十一章表11-3,2人,示範缺席人數，構成報名總數差額,事前請假單與現場確認未到之名冊統計,訓練經辦功能,SAMPLE

## Cross-document boundary
0060=I14-E01/checkbox 065 is the classification and coding work. 0061=I14-E02/checkbox 066 must specify practical file custody, minimal permissions, retrieval controls, version handling, backup and restore workflow. 0062=I14-E03/checkbox 067 owns the complete training-file inventory and real original locators. 0063=I14-E04/checkbox 068 owns query-service cases and improvement. 0064=I14-E05/checkbox 069 owns measured retrieval-speed testing. Do not claim these adjacent deliverables are satisfied by 0061.
0060 R08 is a SAMPLE/SYNTHETIC candidate. Its candidate SHA and replacement-register SHA are above. If referencing its synthetic case, cite the existing `case_id`, `doc_id=0060`, and source `fact_id` exactly. New fictional 0061 workflow, paths, roles, access decisions, dates, IDs, backup/restore results and calculations must be marked SAMPLE/SYNTHETIC and registered fact-by-fact in the 0061 replacement register. Do not represent a sample path or operation as an actual Association system or activity.
