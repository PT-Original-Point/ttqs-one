# TTQS ONE｜每兩小時原生排程與 Codex GOAL 真正復工（2026-10-21 Human 最新覆寫）

> `COMMAND=HUMAN_20261021_TWO_HOUR_GOAL_RESUME_OVERRIDE`
>
> **HUMAN LATEST**：原每小時（60m）改為 **每兩小時（120m）**。本節優先於下方 2026-10-16 每小時歷史條款及 R07 的舊停工判定；只更新 TTQS_ONE 已批准的可逆候選施工與相關排程，絕不自動核准正式接受、新費用、身份、OAuth/MFA 或高風險權限。
>
> **狀態**：CANDIDATE／GitHub 施工指示。寫入 GitHub 不等於 Windows 任務已修改、Codex GOAL 已 resume 或真正排程續工已 PASS。與較舊 control plane 有衝突時標 `SPEC_CONTROL_PLANE_REBASE_REQUIRED`，不因舊規格阻擋合法可逆施工。

## ACTIVE｜P0 先判斷「排程觸發」和「GOAL 恢復」兩件不同的事

- Human 2026-10-21 17:25 台灣截圖：Codex GOAL 顯示「目標已暫停」，舊每小時排程仍於約 16:16／17:15 傳送 `TTQS_GITHUB_COMMAND_PREFLIGHT_V1`，只回答無 READY。**有送達訊息的證據，沒有真實 Writer/Word 或 QA 續工的證據；不是排程完全未觸發。**
- GitHub R07 S12 收據：`BUILD_QUEUE.json` 上次修改 2026-10-19 03:24:56+08:00；115 筆 PENDING 但沒有顯式 READY；把 `PENDING` 當不可施工是自鎖。R07 已有 0099 R17（SHA-256 `293be2dc0e3e0162fa368272851baed27e92990b4ac1871228ec37b51546776b`）及 QA，不能重建。
- 0097 R08 Word COM PDF 匯出超過 180 秒失敗，只擋**0097 R08 的渲染/視覺車道**；18 個 `WINWORD.EXE /Automation -Embedding` 用途 UNKNOWN，不是 18 個已確認 Writer，嚴禁一律 kill。
- 在 Windows 原生 GOAL 介面先查 `/goal` 的目標、paused 與可取得的真正理由；用 OS PID/command-line、未結工作/owner 與 GitHub fresh-read 排除重複派工，之後才用官方原生 `/goal resume` 恢復原 GOAL。**不要 `/goal clear`，也不要單純重設長目標造成 usage history 重置**。Goal 標成 active、但沒有合法作業與產物，不算恢復成功。

## ACTIVE｜P1 不再依賴舊佇列顯示 READY 才能施工

`READY` 必須由 Human 目前 Mission、官方需求、既有 crosswalk、上游來源、候選工件、受信 QA、實際 OS Writer 推導**下一個可逆階段**，不得只看 `BUILD_QUEUE.state`。至少分：

`READY_SOURCE_PACKET`（官方具名來源可讀、專屬 source packet 缺）→ `READY_BLUEPRINT`（專屬章節、真題目、計算與 SAMPLE/REAL）→ `READY_WRITER`（上游具體且無活躍同一 writer）→ `READY_DETERMINISTIC_QA` → `READY_FRESH_REVIEW` → `READY_SCOPED_REPAIR`。

第三方 REAL 原件仍 UNKNOWN 時可製作不造假的 SAMPLE 完整示例與原件索取流程，但正式升格/真實替換維持 Human Gate。沒有 `READY` 字串 ≠ 沒有 `READY_SOURCE_PACKET`。單個 provider/渲染器故障只擋該 Lane。

**立即驗收樣本**：`official_129_to_142_crosswalk.csv` 將 `I18-E08` 綁定 `0100 | 0101`，專案 157 指標索引 109：「訓練前後自評量表與真雷達圖數據」。0100 是學員訓練前後自評表，0101 是能力提升雷達分析報告；官方 PDF 第 7 頁及 `03_157_CHECKBOX_BLUEPRINTS.md` 已可核。先查 OS／GitHub 是否已有新工件或 active Writer；若沒有，至少可合法進行來源包及 UNIQUE Blueprint。可沿 0099 已驗算的合成案例（8 人×5 維×前後2次=80 格，前測75／後測117，平均增加5.25），但必須檢查跨文件 fact ID、一致性、分母與完整替換清冊，絕不宣稱真實學員成效。0100、0101 是兩種不同文類，不能換標題複製。

## ACTIVE｜P2 排程改 120 分鐘，只有一個真正派工主人

1. 在桌面 App 「已排程」先讀回**現有** `TTQS ONE hourly quality GOAL` 原生 task ID、綁定 thread、enabled、last/next run、prompt、project/local vs worktree、執行帳戶、最近三次真實 run。原生排程仍顯示舊名稱不表示已修復。
2. 若它可以在相同**有權存取本機 E:\TTQS**的 Context 真正續工，就只**編輯同一任務**成 `Every 2 hours`；原生進階重複規則支援時用 `RRULE:FREQ=HOURLY;INTERVAL=2`，確認台灣本地時區及下一次時間。**不得創建另一條同功能任務**。重寫保存的 prompt，改用「P1 階段 READY＋OS live owner＋回收成果」的短前置規則，禁止兩小時空轉長篇報告。
3. 若同對話排程**只傳訊息到 paused Goal、無法取得本機工件或建立 Writer**，先暫停舊任務並從原生介面讀回，然後在同一已授權本機專案用唯一 standalone scheduled task 作受限 120m 恢復；必須驗證能讀真實 DOCX、單一 owner、原生 working directory、真實 Worker 和 GitHub exact-SHA readback。若 standalone 只能隔離工作樹且看不到受信 E:\TTQS，不能稱已復工。
4. **成本最佳方案**：若原生 Scheduled 每次喚醒都需要 GPT-6 呼叫，且已存在合格 Windows Task Scheduler/原生 Codex Worker 入口，優先由**唯一** Windows OS 120m deterministic L0 任務檢查 Git/OS/hash；**無 material delta 時 0 高階模型呼叫**，有 READY 或真故障才調用一次受信 CLI。修改前保存既有任務 XML/Action/Principal，查明 `TTQS_ONE_Codex_Supervisor` 歷史任務是否仍適用，不能因名稱相同就重啟舊 launcher。OS 路線啟用前先停用同作用 Codex App 派工，避免雙主。
5. 只有 **Native schedule interval=120m、唯一 owner、實際計時觸發、同來源 OS readback、合法 Source/Blueprint/Word/QA delta 或精確 blocker** 全部證實，才叫 `AUTONOMOUS_RESUME=PASS`。只收到排程文字 = `SCHEDULE_TRIGGER=PASS / WORKER_RESUME=FAIL`。

## ACTIVE｜P3 施工與安全／成本邊界

- 0099 R17 已是候選；0097 R08 Word 匯出維持精確受限，0100/0101 可獨立合法開始。沒活躍 Writer 才派新工作，同一寫入範圍不得雙主；未知 GitHub/OS 寫入先同來源讀回，不能盲重送。
- OpenCode v2 CLI 只用當日**實際可用**免費模型做有界內容或審查；Antigravity CLI 只請求 `gemini-3.8-flash-high`，不允許 Computer Use、檔案工具 Writer、危險權限繞過、模型 fallback 或未授權付費。Windows 原生工具建 DOCX、公式/字級/視覺檢查。
- GOAL 完成的條件是 Human 真正已接受的範圍與受信文件品質，不是 Queue empty、沒有明示 READY、GOAL 暫停、Word 卡住或 129/142 個名稱看起來齊。28 個未具名「其他」維持 BLOCKED_UNTIL_UNIQUE_OTHER_NAMED；正式 HUMAN_ACCEPTED/REAL_REPLACED 獨立。
- 每兩小時僅需最多 1 頁增量；沒有實質差異且用 OS L0 → 0 大模型呼叫。不要再把 12MB 歷史報告遞迴附進新報告，不重做已同 SHA 通過的正文或 QA。

## ACTIVE｜P4 Native 驗收回報（缺資料保留 UNKNOWN）

```text
PROJECT_ID=TTQS_ONE
SCHEDULE_TASK_ID=<same native ID>
SCHEDULE_OWNER=<Codex desktop local|standalone local|Windows OS>
OLD_INTERVAL=60m
NEW_INTERVAL=120m|NOT_APPLIED
NATIVE_LAST_RUN=<timestamp>
NATIVE_NEXT_RUN=<timestamp>
EXACT_OS_GOAL_STATE=<active|paused and reason|UNKNOWN>
OS_WRITER_OWNER=<PID + exact work_id|NONE|UNKNOWN>
QUEUE_LAST_WRITE=<timestamp>
READY_SOURCE_PACKET=<0100/0101 or fresh other item>
SCHEDULED_TRIGGER=<PASS|FAIL|UNKNOWN>
REAL_WORKER_RESUME=<PASS|FAIL|NOT_TESTED>
FIRST_WORK_SHA=<exact source packet/Blueprint/Word/QA or NONE>
GITHUB_EXACT_READBACK=<commit/blob/SHA or UNKNOWN>
TOKEN_IF_NO_DELTA=<zero verified|UNKNOWN>
NEXT_SINGLE_LEGAL_ACTION=<precise>
```

---

## HISTORICAL｜以下保留 2026-10-16 60 分鐘規格原文供稽核，不再作為目前時程權威
# TTQS ONE｜每小時自動喚醒 Codex 並接續 GOAL（2026-10-16 Human 最新授權）

**PROJECT_ID=TTQS_ONE**  
**Human 命令：在高品質文件 GOAL 完成前，每 60 分鐘由 Codex App 原生 Thread Scheduled Task（優先）或既有 Windows Task Scheduler（備援二擇一）喚醒／檢查；合法 READY 且沒有活躍 Writer 時續工，無實質差異不浪費高級模型。**  
**狀態：CANDIDATE，寫入 GitHub 不等於 Windows 已安裝、排程已啟用或產品已完成。**

## 0. 首選：Codex App 原生 Scheduled／Thread automation（不新建第二個 Supervisor）

依 OpenAI 目前官方 Scheduled tasks 文件（https://learn.chatgpt.com/docs/automations）：桌面 app 支援 project-scoped scheduled tasks，並能建立**附著於現有 Codex 對話**的 thread scheduled task。此類 task 定時回到同一條對話，比另起新任務更適合本次「同一 TTQS GOAL 自我喚醒」。有自訂排程時，可選 Cron 0 * * * *（Asia/Taipei、每小時整點），或 UI 提供的 Every 1 hour。官方亦提醒：本機專案排程需電腦開啟、app 保持運行、專案仍在本機可用；排程本身不是把雲端 ChatGPT 變成 24/7 Windows 常駐服務。

**先在實際 Windows Codex App 讀回：**
1. Scheduled/Automations 是否已可使用？同一個 TTQS GOAL thread 已有 scheduler 嗎？讀回 task ID、thread ID、repo/工作目錄、模型、sandbox、enabled/paused、週期、last/next run。從 app UI 或原生支援動作建立/更新，不猜造 app 的內部 JSON/SQLite 格式，不直接修改私有排程 DB。
2. 若本機 app 支援**thread scheduled task**，只建立或更新**一個**綁定現在 TTQS ONE GOAL thread、每 60 分鐘一次的 task，任務 prompt 以本檔「第 2 節 deterministic L0」為共同內容，並引用 01–04 完整品質規格；每次醒來讀當前來源/queue/OS worker，必要時合法續工，沒有進展不重複消耗模型工具或重派同一寫入。
3. 它必須使用真正可存取 E:\TTQS 工作區的本機執行環境，不是隔離到無法讀取 Windows DOCX 的雲端聊天；排程 sandbox/工具/授權要做有界 smoke，不能預設有 elevated 權限。若選工作樹模式與現有真實 DOCX 工作目錄隔離，必須先驗證能讀到相同正式工件；否則選合格 local project mode 並保證單 Writer。
4. 每次觸發前，重用既有 OS/queue/GOAL 驗證；若已有同一範圍 Worker alive，僅記錄並結束該次；不得因 thread 已醒就開第二個 Builder。GOAL 的最終完成/正式接受經可信 readback 後，使用**原生 Scheduled 管理功能**停止或封存這個 recurrence；不能僅靠模型最後一句「完成」。
5. 驗收：從 Codex app 原生 Scheduled 頁讀回 task enabled/active、每小時觸發設定、綁定的 thread、last/next run、一次實際執行紀錄、再次執行時保留同一 GOAL/工作狀態，並與 OS Worker/queue 的同來源 readback 比對。未實測不得宣稱 24/7 已生效。
6. 原有 TTQS_ONE_Codex_Supervisor 若已擔任長時 Worker 執行主體，可以繼續作為 Worker，但不能同時再設同功能 hourly re-dispatch trigger 造成雙主；如有兩個候選排程，指定唯一 hourly wake owner，另一個關閉重複觸發或保留純 Worker 功能，不刪除歷史。

**重要的成本實情**：Codex App 原生 Scheduled 在每次定時回到對話時可能已經觸發一個模型執行；它不能保證「完全沒有 material delta 時零模型呼叫」。如果本專案要求嚴格的零空轉模型成本，則優先讓既有 Windows Task Scheduler 執行 deterministic L0（OS process、Git/hash、queue 檢查），只有發現需要 Codex 續工時才叫醒模型。這是基於『無實質變化不呼叫高階模型』的合法路由選擇，不是新增第二套排程。兩種方案擇一，須將選擇及實際成本條件寫入 readback。

**只有在這個 Codex 原生 Scheduled 功能不支援/本機不可用、或無法以本機權限實際接續 GOAL 時，才選以下 Windows Task Scheduler fallback。** 兩者擇一，不能互相當額外核准 Gate、不能雙重整點派工。

---

## 0B. 2026-10-16 七小時無交付：同對話排程失去工作活性之修復

Human 當日提供的 Codex 畫面/回報顯示：Scheduled task ID = ttqs-one-hourly-quality-goal-resume，target thread = 01a14098-b269-79e3-b07c-56e96557fe07，設定 ACTIVE / HOURLY；但先前 smoke = NOT_TESTED，Codex 自己表示「同一對話的排程等待目前回合結束」，Windows 舊 TTQS_ONE_Codex_Supervisor 則是 Disabled。此為 HUMAN-PROVIDED OBSERVATION，不是直接 Windows 現場讀回。GitHub PR #92 最後內容更新約為 2026-10-16 01:38 Asia/Taipei，並不能證明之後本機 DOCX 沒有變化。

**禁止把排程設定 ACTIVE 當成長時 Worker 已在執行**。Codex 須先查 Scheduled「近期執行」的 start/end/status/error、每小時預定觸發時段、Windows OS process/Task Scheduler、0031 候選與 QA 的檔案 mtime+SHA、最後一個實質工作變化時間，據此判定：
- NO_SCHEDULED_TURN：排程根本沒有觸發；找精確原因（同 thread 活躍、app 沒運作、PC 睡眠、task paused、工具審批等）。
- TURN_STARTED_NO_WORK：排程進入但沒有開任何合法 READY 工作，查來源、Sandbox 路徑、OS owner、舊 pause 與 prompt，勿自報完成。
- WORKER_ALIVE_NO_DELTA：程序真正存活但長時沒有實質工作；查正在等 I/O、CLI model、配額/人工批准。不可從一個標記直接推定死鎖。
- WORK_COMPLETED_LOCAL_ONLY：本機確有新的 DOCX/QA，可讀回 exact SHA；GitHub 未上傳不代表本機沒工作。

### 同對話排程的受限情境

若**有證據**顯示目前對話長時間處於 active turn，造成 hourly in-thread task 過了至少一個應執行時段仍無新回合：**不要再次建立另一個同對話 hourly 排程**。先使用 Codex 原生 Scheduled 管理功能**暫停/停用**原本的 thread 綁定 task，讀回確定它不再會重複派工。接著，在相同可存取 E:\TTQS 實際 DOCX 的本機專案下，使用一個**standalone scheduled task**，每 60 分鐘產生獨立 run/thread；它每次 fresh-read repo 本契約/正式 Source/OS Worker/Queue/Pending effects，不依賴前一個 GUI 長回合完成，也不靠 Chat 記憶推論施工狀態。

- standalone task 的 prompt 必須含 project_id、精確 repo/ref、工作目錄、目前 GOAL 規格、唯讀 L0 preflight、只接續 READY、單 Writer 與 fail-closed 外部效果確認、只在可信完成時停止、確切產物與回報欄位。
- Codex Scheduled 若只能選隔離 worktree，必須現場證明它可實際讀寫受權限保護的 E:\TTQS 工件；否則不能假稱能繼續 Word 生產。若限制無法突破，**改走本機已存在的 Windows Task Scheduler**，以確定性 L0 偵測與官方 CLI/原生 Worker 做分工；任一時刻只有一個 hourly dispatch owner。
- 原生 scheduled task 每個觸發本身可能花費模型額度；若需要「無差異完全零模型呼叫」，使用 Windows OS 的 deterministic L0 作唯一每小時觸發，僅 READY/故障需續工時再喚醒模型。
- 如果原同一對話**真的還有活躍的 writer**，獨立 task 只能偵測，不得直接再開第二個 writer；一切以 Windows 真正 OS 存活、工作 ID/寫入 owner/檔案變更/外部效果為證。
- 以官方 Scheduled 近期執行頁或 Task Scheduler 原生結果做**真實 scheduled smoke**：不僅設定 ACTIVE，要觀察至少一個定時執行事件，有開始/結束時間、同來源來源 readback、0031 或其他 READY 的 bounded 工作證據。無法做 Run now 就等下一次真實觸發；不得為了通過煙測竄改官方完成數。
- 原先卡住的對話要先確認是否有未結外部寫入/正工作的 worker，之後才合法終止或結束該 GUI turn；避免丟失尚未持久化的成果。

**驗收失敗修正條件**：每一小時至少要留下原生觸發讀回；存在合法 READY 且沒有活躍 worker 的情況，必須有真正 worker resume 與文件/QA delta 或精確失敗原因。只呈現「已排程、正在思考」一律 PARTIAL/UNKNOWN，不得 PASS。

---

## 1. Windows 備援：重用舊排程，不允許雙主

2026-10-05 GitHub 歷史 WORKLOG（不是本次 LIVE）記載曾有 Windows Task Scheduler 任務 TTQS_ONE_Codex_Supervisor；某次觀測為 Disabled、Hidden=true、Principal=J，Action 為 wscript.exe //B //NoLogo，透過 supervisor_hidden_launcher.vbs 執行有限的一個 supervisor turn（--max-docs 1）。先做 Windows fresh readback：舊名字、Action、Principal、Triggers、Settings、LastRunTime、LastTaskResult、Enabled、目前實際工作程序、其他 TTQS 排程、BUILD_QUEUE、CURRENT 和 Writer owner。不得把 10/05 歷史狀態冒充現在狀態。

在執行 Windows PowerShell 的 Codex 主機先以以下原生唯讀命令尋找：
- Get-ScheduledTask -TaskName 'TTQS_ONE_Codex_Supervisor' -ErrorAction SilentlyContinue | Format-List *
- Get-ScheduledTaskInfo -TaskName 'TTQS_ONE_Codex_Supervisor' -ErrorAction SilentlyContinue
- Get-Command codex -ErrorAction SilentlyContinue
- 檢查 TTQS 同名或相關 Task Scheduler job、Windows 真實 process command line、實際檔案路徑和目前有效排程。
- 若有舊任務，修改前先以 Export-ScheduledTask 讀取和保存原生 XML；保留能確定安全回復的原始設定。
- 確認舊 supervisor 是不是實際能喚醒 Codex/合格 Worker。不能因任務名字含 Codex 就當作已驗證；若只有 Antigravity 派工功能，確認是否能滿足本次 GOAL 恢復，必要時改用本機已存在的合格 Codex CLI resume entrypoint。
- 若既有排程已覆蓋每一小時且安全接續，直接保留，不疊加第二個排程；若需要改為明確的 60 分鐘，精確修改這一個 TTQS 專用任務，保留原本 Action、Principal、Task 層級必要權限與其他正當消費方。
- 若目前任務是 Disabled，先查停用命令的授權範圍，確定只恢復最新 Human 已授權的可逆候選文件/QA，不解鎖正式送審、PROD、簽章、付款、法律、機密與 OAuth。

## 2. 每小時觸發後的 deterministic L0 程序

1. 驗證 project_id=TTQS_ONE 和最新正式來源與 Human GOAL；不讀其他專案。
2. 根據 accepted requirement/Blueprint、可開啟的實體 DOCX、原生 exact-SHA 驗收及可信完成收據確認 GOAL_DONE。不得以 142 個檔名、2,324 個備份副本、Queue empty、Worker 自評 PASS/exit 0 假稱完成。129 個具名需求的每一適當交付件都需獨立可讀可用，28 Other 若仍無獨特名稱保持 BLOCKED_UNTIL_UNIQUE_OTHER_NAMED；正式 Human 終驗另有保留判定。
3. 若 GOAL 已正式接受完成，停止下一次模型施工並將原生 Task Scheduler 任務設為 Disabled（保留原始執行收據與歷史）；同來源讀回。若僅等待最終 Human 接受，僅作便宜狀態檢查，不每小時重呼叫大模型。
4. 讀 Windows 真正存活的 Worker/Process/Session、Task Scheduler 近況、單一寫入 owner。RUNNING 註記不能證明 OS 程序存活；程序一時無回應不能擅自殺掉或開雙主。
5. 讀既有 BUILD_QUEUE / exact work_id、尚未確認的共享外部效果、可用模型/配額與 blocker。區分 READY / BLOCKED_EXACT_LANE / WAITING_REVIEW / UNKNOWN。
6. 有 Worker 仍在工作，這次不另派；僅記錄狀態。沒有可合法執行的 READY、沒有新成果/狀態差異、配額/執行憑證不足時，退出，不呼叫高階模型。
7. 無活躍 Worker 而有真正 READY、現有合格 CLI 和權限可用時，調用既有 Codex GOAL resume entrypoint 一次，從最近 accepted task/queue/newest artifact 開始而不是重做整批；可逆 DOCX/QA 工作無須人類每小時介入。
8. UNKNOWN 或 PARTIAL 外部效果一律先同 provider readback，不能盲重送，只停受影響 lane；模型錯誤/429 不阻擋其他獨立 READY。
9. 一小時是最低成本健康檢查／事故恢復頻率，不中斷正在進行的長時生產，不保證每小時恰好完成一份 Word。

## 3. Windows Task Scheduler 合約

- 觸發：HOURLY，每 60 分鐘；OS 停機期間無法執行，不可說「主機關機也可 24/7」。視現有原生配置可設 StartWhenAvailable 補跑。
- 原生執行：沿用該專案已驗證的 Task Scheduler Supervisor/Runner 和可用 Codex CLI，不建立第二套 MCP/Database/Agent Bus/Supervisor；若現役入口不支援無人值守，須現場依官方 CLI 支援找已有的可授權 headless 模式，不能自行繞過需要的人機授權。
- 同一工作不重入：Task Scheduler MultipleInstances=IgnoreNew 或同等設定；原生 OS worker / shared-write 範圍先查 owner，防止兩個 Codex 同寫 CURRENT/REGISTER。
- 帳戶：現場驗證 Task Principal 是否可存取 E:\TTQS、已授權模型與必要資料，優先最小權限；不記錄密碼/Token，認證或 MFA 需要人類確認就回報真正 Gate，不繞過。
- 不產生額外費用、訂閱、對外部署或正式提交，除非有相應 Human 授權。
- 原生定時任務只負責叫醒／檢查，長時工作由已存在合格 OS Worker 施工；每次若沒有 material delta，不浪費模型 token。
- 若無法從相同來源確認有效 native CLI resume/啟動入口，報告 EXACT BLOCKED；不要宣稱已排程成功，也不要丟一個空的整點提醒當成自動施工。

## 4. 原生安裝及讀回驗收

A. 先記錄 prestate：舊任務 XML / trigger / principal / Action / LastTaskResult、目前 Queue/GOAL/OS worker/OLD pause 的授權與精確 blocker。
B. 重用原生 Task Scheduler：採受支持的 Windows PowerShell ScheduledTasks 或 schtasks 命令設定每 60 分鐘；保存原 Action/Principal/必要權限，不因全新 session 再問已授權的可逆施工。
C. 同來源讀回：Enabled=true、Hourly/60min、下一次觸發時間、正確 Principal、真正可執行的 Action、MultipleInstances=IgnoreNew；命令 exit 0 不等於 readback PASS。
D. 觸發一次安全且有界的實際 wake smoke test，證明本機 Task Scheduler 確實執行 L0、能找到已有 GOAL work，無重入／視窗搶焦點／不當權限擴張；需啟動 Codex 才能驗證者，必須提供真的 Codex resume 執行 ID 和有限實際成果。
E. 用測試 fixture（不可修改真實 GOAL）確認模擬完成/待 Human acceptance 時不反覆呼叫模型；真實 GOAL 接受完成才將排程停用。
F. 可用時間和持續性由 Windows OS 原生報告：關機、斷網、休眠、配額或帳戶登出均可能影響觸發與執行。若僅在使用者登入時執行，須明確寫明，不冒充已配置無人值守。
G. 既有機器/程式不可被強制中斷而造成半寫入；UNKNOWN 不盲重派。

## 5. 必須交付 Human 的實測回報欄位

PROJECT_ID=TTQS_ONE
WINDOWS_TASK_NAME=<same source readback>
TASK_INSTALL=CONFIRMED|NOT_APPLIED|PARTIAL|UNKNOWN
TASK_ENABLED=<true|false|UNKNOWN>
HOURLY_TRIGGER=<60m|UNKNOWN>
NEXT_RUN_TIME=<timestamp|UNKNOWN>
EXECUTOR_ACCOUNT=<verified nonsecret identity|UNKNOWN>
TASK_ACTION=<verified actual executable|UNKNOWN>
OVERLAP_POLICY=<IgnoreNew or verified equivalent|UNKNOWN>
CODEx_NONINTERACTIVE_ROUTE=<native proven cmd|UNKNOWN>
WORKER_ALIVE=<OS readback|UNKNOWN>
GOAL_DONE=<YES|NO|UNKNOWN>
FIRST_READY_WORK_ID=<exact|UNKNOWN>
WAKE_SMOKE=<PASS|PARTIAL|FAIL|NOT_TESTED>
READBACK_EVIDENCE=<native location/timestamp>
NEXT_LEGAL_ACTION=<one clear action>
TRUE_HUMAN_GATE=<specific genuine gate|none>

**只有 Codex 原生 Scheduled 或 Windows Task Scheduler 其中一個通道已真正註冊、已啟用、每小時觸發，且能安全續工，才可回報每小時 Codex 自動喚醒已完成。不得同時啟用兩條相同功能的派工通道。GitHub 文件自身不具主機安裝效果。**
