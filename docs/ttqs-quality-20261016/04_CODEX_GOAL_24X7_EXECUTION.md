# TTQS ONE｜R12.3 現役交接覆寫（2026-11-27）

COMMAND=TTQS_ONE_R12_3_INTEGRATOR_HANDOFF_DOT_R123_20261127
PROJECT_ID=TTQS_ONE
REPO=PT-Original-Point/ttqs-one
PR=92

依 R12.3 交接立即收束既有候選：0031 `fff554e6b1424f4485b99956dcaf5183a76f2864ede454386d9315cd55d8d78e`、0055 `85c329617ef7146ad1569fc3ebd841ab7ce5a0c5e183cbabc7ac6474109ded94`、0134 `f09248f678ba6cc13e426440a3a0be0d04652d4e0203be8a54fd917a37c814f5`。SHA 是待核候選識別，不代表通過；0134 為 R02 內容、R03 版面嘗試。0091 R11 維持隔離，不得上傳或放行。

Dot 唯一負責派工、監督、獨立稽核、候選品質裁決、拒收／返工、成果回收與交付驗證；Codex 負責施工、Word 製作、確定性技術檢查，並是唯一共享狀態／PR #92 寫入與整合者，不取得競爭派工或品質裁決權。Codex 只可整合 Dot 已按 exact SHA 明確核准的候選。W1/W2 只在 Dot 派發的隔離範圍工作。核驗同一候選 SHA 的必要技術／計算、Word 原生全頁視覺及獨立語意範圍；只對同 SHA 且有效的證據沿用。跨版視覺繼承須逐頁比對頁面影像位元組，直接檢視所有變動頁。完成後由 PR 同 ref 讀回原始位元組、核對檔案 SHA-256，再更新既有品質索引。沒有讀回前不得標交付或品質合格。

此覆寫只改交接角色與候選收束方式；不改模型、速度、排程、費用、正式接受或 SAMPLE/REAL Gate，不新增並存規格或控制機制。以下 R12.2 內容繼續適用於未被本覆寫明確取代的項目。

# TTQS ONE｜R12.2 GOAL 輕量銜接（2026-11-18）

PROJECT_ID=TTQS_ONE
REPO=PT-Original-Point/ttqs-one
PR=92
BRANCH=work/ttqs-one-document-quality-contract-20261016
STATUS=GITHUB_CANDIDATE; WINDOWS_GOAL_READBACK=UNKNOWN

Human 已表示在 Codex App 修改原生 GOAL 至 R12.2；本檔只是 GitHub 候選施工規則，不修改或證明原生 GOAL 已保存。

目標：依官方 129 個具名方框、正式 crosswalk/142 歷史序號及必要複合拆件，為屏東縣原始點關懷協會交付完整高品質、可編輯的 SAMPLE/SYNTHETIC DOCX；28 個「其他」未命名不得湊數，不偽造 REAL、外部證明、簽章或核准。

執行：
1. 新 session、故障、未知效果或材料差異才做有界 OS/GitHub/候選 SHA readback；不每次全文讀 10/26 R12、06 舊事故或全部歷史。
2. 選最短合法交付路徑；既有同 SHA、同範圍已通過的 QA/正文不得重做。非阻斷 LOW 意見不開新一輪全文修版。
3. 可授權且實際可用的 W1 OpenCode v2/W2 Antigravity CLI 優先承擔獨立文稿、來源分析、局部修補與獨立語意；不同 doc_id 可按資源並行。Codex 聚焦唯一派工/整合、確定性數學/來源 QA、Word 原生全頁檢查、GitHub raw-byte readback。
4. 派工成功要有實際 OS work_id/PID/session、原始輸出與可採用正文/審查，絕不以 serve PID、requested model、exit0 或 Worker 自稱 PASS 判定。受限配額/安全規則只封精確 lane，不轉未授權付費、不繞過平台；沒材料差異不叫模型。
5. 活躍合法工作階段每段終態即接下一 READY，120 分鐘唯一原生排程只是故障補漏，非時間配額。缺原生 Windows 存活/自然觸發證據標 UNKNOWN。
6. 品質與安全完整繼承 Human 最新 Mission、AGENTS.md、必要 01～03 文類及驗收：完整可重算 SAMPLE、正確文類、同候選 SHA 技術/Word 全頁/真正獨立語意、SAMPLE/REAL、GitHub bytes、Human 正式 Gate。
7. 實際產能只計不同 doc_id 完整合格可取回 DOCX 與具名需求淨覆蓋；不按提交、版本、Worker 數、Token、報告長度計功。僅 material delta 才短回報。

舊 R11/R12 特定文件待辦、60m、歷史 pause/429 與長篇指揮，由 Git history 和 R12 原件保存；只有同類事故重現時按需讀，不是現役復工 Gate。
