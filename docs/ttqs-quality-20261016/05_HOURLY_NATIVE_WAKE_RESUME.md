# TTQS ONE｜每小時自動喚醒 Codex 並接續 GOAL（2026-10-16 Human 最新授權）

**PROJECT_ID=TTQS_ONE**  
**Human 命令：在高品質文件 GOAL 完成前，每 60 分鐘讓 Windows 原生工作排程器執行一次有界檢查；如果 Codex/Worker 沒有工作而存在合法 READY 任務，接續原有生產。無實質差異則不浪費高級模型。**  
**狀態：CANDIDATE，寫入 GitHub 不等於 Windows 已安裝、排程已啟用或產品已完成。**

## 1. 重用舊排程，不允許雙主

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

**只有原生 Windows Task 已安裝、已啟用、確實每小時觸發，且安全恢復工作的實測證據完整時，才可回報每小時 Codex 自動喚醒已完成。GitHub 文件自身不具 OS 安裝效果。**
