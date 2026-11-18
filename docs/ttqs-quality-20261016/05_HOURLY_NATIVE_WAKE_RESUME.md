# TTQS ONE｜R12.2 唯一 120 分鐘故障補漏（2026-11-18）

PROJECT_ID=TTQS_ONE
SCHEDULE=EXISTING_120M_ONLY
PURPOSE=WATCHDOG_NOT_THROTTLE
WINDOWS_NATIVE_EFFECTIVE=UNKNOWN

這是 GitHub 候選規格，不等於 Codex App 原生 Scheduled Prompt 已更新或 Windows Worker 已啟動。舊 60m/Hourly、Supervisor 及歷史事故仍在 Git history，不再是現役施工節奏。

1. 只從原生介面讀回現有唯一排程的 task ID、thread/workspace、enabled、120m、last/next run、實際 prompt、自然觸發及可否接觸 E:\TTQS。不得另建重複派工排程或修改私有 TOML/DB 假稱套用。
2. 合格本機 session 有合法 READY 即連續工作，不等兩小時。排程只在真正中斷/未結效果時讀 OS work_id/PID、來源/候選 SHA、現有收據、GitHub HEAD，安全恢復受影響工作。
3. 既有 W1 OpenCode v2、W2 Antigravity CLI 若有不同獨立 READY 且路由實際可用/授權/安全，優先真正外包並行；必須有 native OS 派工和可採用原始成果。serve/GUI PID、面板 HTTP200、通知或 requested model 都不是 Writer 成功證據。
4. 本次無材料差異則 L0 只用原生 OS/Git/hash，不喚醒高階模型；但 Codex 原生 Scheduled 本身可能消耗額度，不能保證零 Token。429、權限、Word 失敗只隔離精確車道，不繞過配額，不停止其他 READY。
5. 同一 doc/revision、共享 register/CURRENT/GitHub ref 避免雙主；未知外部寫入先同來源讀回，不能盲重送。保留同候選 SHA QA、SAMPLE/REAL、Human 費用/Production/身分/正式接受 Gate。
6. 分開驗證 CONFIGURED_120M、NATURAL_TRIGGER、OS_WORKER_EXECUTED、MATERIAL_DELTA、GITHUB_RAW_BYTE_READBACK，未知寫 UNKNOWN。只報新 DOCX/QA 真增量、候選 SHA、精確阻擋及下一 READY，不寫重複長篇工作日誌。