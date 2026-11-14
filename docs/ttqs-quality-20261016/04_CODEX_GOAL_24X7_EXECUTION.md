# TTQS ONE｜2026-10-23 R11 最新 Human GOAL 覆寫（立即連續施工、刪除時間窗自鎖）

**COMMAND=GOAL_20261023_R11_CONTINUOUS_STAGE_NO_NATIVE_RESUME_DEADLOCK**

- **最新 Human 明確變更**：TTQS ONE 120 分鐘排程只是原生故障補漏與未結工作讀回，絕非冷卻時間，也不是一次只准執行一個 READY stage。持續工作的合格本機 Codex/CLI 在前一段已終結、收據與共享寫入明確時，**立即做下一個授權 READY stage**；可以在同一活躍施工會話連續多個 stage。舊 AGENTS 固定 one BUILD+one REVIEW、one attempt per scheduling turn 與 old Canary 開工限制不再適用。
- 原生 Goal UI 若 PAUSED：先查可取得的真狀態、scope 與 owner；**只有 native 確實提供 resume 才呼叫**，無此操作時不假設 `/goal resume` 可用、不循環等待、不 `/goal clear`。在同一可授權本機 Codex 執行路徑上直接續作可逆 TTQS DOCX 工作，GOAL UI 本身的 paused/resume acceptance 分開記錄。若該原生執行路徑真受平台阻擋，就精確標 lane，並核對現有合法 Windows 入口；不建立新 daemon/DB。
- 允許不同 doc_id 與不同來源/文稿/確定性 QA 的獨立 READY 車道按 OS 資源與安全隔離**適度並行**；同一 doc/revision 寫入範圍只有一個 Writer；共享 replacement register/CURRENT、GitHub 同一 ref 需防競寫及同源讀回。過期 queue 和 R10.1/0110 的路由 PAUSED 不能當作全案停止。
- 成本：0 material delta 的原生 L0 檢查不啟動模型；Worker 先用低成本且實際可用的原生 CLI 短包，完成立刻回收/採用/QA；絕不定時自動寫長篇活動報告。真正 SAMPLE/REAL、獨立 exact-SHA QA、Word 原生可用性及 Human 保留授權不變。
- 最優先另參閱 `06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` 頂端 R11／R10.1 增量。**GitHub 指令寫入不等於 Windows 排程 Prompt 已持久改好；須由 Windows 原生 Automation 設定讀回**。

---

# TTQS ONE｜GOAL 目標持續施工修訂（Human 2026-10-21；優先於下方 10/16 舊程序）

**COMMAND=GOAL_20261021_STAGE_READY_NO_STOP_R08**  
**LATEST HUMAN SPEC**：維持高品質 129 具名需求全鏈 SAMPLE 可用 Word（28 個尚未命名的「其他」不假造），先恢復已批准的可逆 CANDIDATE 文件生產，不得以單一模型/Word 渲染故障、佇列過期、缺 READY 字面或缺 REAL 原件造成整專案停止。兩小時排程以 **`05_HOURLY_NATIVE_WAKE_RESUME.md` 頂端 2026-10-21 ACTIVE 覆寫**為準；下方舊每小時／「直接停止」若牴觸，以本段優先。

**R07 已完成的不能重做**：0099 R17 DOCX exact SHA-256 `293be2dc0e3e0162fa368272851baed27e92990b4ac1871228ec37b51546776b` 有技術、37 頁有界視覺及獨立文字語意收據，仍 CANDIDATE／非協會 REAL／NOT_FORMALLY_ACCEPTED；0097 R08 只在 Word PDF/visual lane BLOCKED，其他 source/Blueprint/Writer/QA lane 不陪停。R07 S12 的 `NEXT_READY=NONE_CONFIRMED` 是 10/21 16:14 的歷史快照，不是永久停止指令。

**立即重新導出下一步**：原生 Windows OS/PR readback → source-bound checkbox x 對應 DOCX 複合拆件 → 最新穩定工件／owner／QA → 逐階段 `READY_SOURCE_PACKET` / `READY_BLUEPRINT` / `READY_WRITER` / `READY_DETERMINISTIC_QA` / `READY_FRESH_REVIEW` / `READY_BOUNDED_REPAIR`。舊 `BUILD_QUEUE.json` 上次 10/19 的 PENDING 只作索引，不得因無顯式 READY 宣告停工。

**可立即驗收之例**：`I18-E08`（專案索引 109）在 142 份歷史 crosswalk 對應 `0100` 學員前後自評表及 `0101` 雷達分析報告。正式來源依官方 PDF 第 7 頁與現行 `03_157_CHECKBOX_BLUEPRINTS.md` 綁定；合成案例可利用 0099 已重算的 8x2x5=80 分值（前75、後117、+42，平均5.25），但分別產出不同文類、真雷達圖數據與完整 SAMPLE 替換清冊，**不得假冒真實成效**。如果 packet/unique Blueprint 尚未存在，當下至少是可逆合法的 `READY_SOURCE_PACKET` 而非 NO_READY；有現役 Writer 則先回收，不雙主。

**Goal 暫停處置**：先原生 `/goal` 取得 paused 原因、owner 與使用量，再以已批准且可復工的具體任務，在同一 Goal 使用 `/goal resume`；不要 `/goal clear` 或重設整個 Objective。必須真的產生 source/Blueprint/Writer/QA 增量才叫復工，切忌只把 Goal 狀態改成 active。

**停止條件**：正式已接受的範圍完成，或所有獨立合法車道都取得具體外部 blocker 才允許相應等待；不能因某個 Word 視覺、免費模型 429、沒有 REAL 原件或 stale queue 停全部。真正費用／身份／OAuth／簽章／Production／正式接受 Human Gate 保留。

---

## HISTORICAL｜以下為 2026-10-16 候選原規格，牴觸之續工／排程段落已被上方 Human 最新命令取代

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
