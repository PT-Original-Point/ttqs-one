# TTQS ONE｜現役精簡施工規則 R12.2（2026-11-18）

PROJECT_ID=TTQS_ONE
REPO=PT-Original-Point/ttqs-one
PR=92
BRANCH=work/ttqs-one-document-quality-contract-20261016
RUNTIME=E:\TTQS\TTQS_ONE_CODEX_RUNTIME

Human 已表示原生 Codex GOAL 改為 R12.2。此 GitHub 更新不代表 Windows GOAL、CLI Worker 或排程已套用。Human 最新明確 Mission/Spec 優先；01_HUMAN_MISSION_AND_ACCEPTANCE.md、02_GENRE_WRITING_MANUAL.md、03_157_CHECKBOX_BLUEPRINTS.md 依當下文件需求引用。10/26 R12 長篇指揮書、06 舊事故、HOTFIX5/6、舊 queue 只供精確故障追溯，不再強制每次完整閱讀或重跑舊任務；相容的安全與品質保護仍有效。

## 1. 目標與最短交付路徑
- 為屏東縣原始點關懷協會按官方 129 個具名方框、正式 129→142 crosswalk（複合需求按用途拆件），交付成熟可編輯、可直接調閱的 DOCX。28 個未命名「其他」不湊數；142 個歷史序號不等於 142 件合格。
- 文類/官方要求/專屬 Blueprint 必須精確；缺 REAL 時需完整、可重算且可操作的 SAMPLE/SYNTHETIC 案例與逐事實替換清冊。不得偽造正式核准、簽章、外部原件；正文無 JSON/控制欄位；正文≥10.5pt、表格≥9.5pt，Word 原生全頁可讀。
- 新 Session、故障、未知外部效果或實質內容變動才做有界 OS/GitHub/候選 SHA 恢復。已確認來源及同 SHA、同範圍 QA 不重查。依當前 READY 選最短合法交付：已通過品質只缺 readback → 完成；來源/Blueprint 齊備缺 DOCX → 立即 Writer；既有候選有真阻斷缺陷 → 最小修復；缺材料 → 補來源/Blueprint。
- 不以歷史固定 doc_id 名單優先於最新 READY；非阻斷 LOW 建議登錄，不觸發無限修版。同一邏輯缺陷連續兩次沒有外部新事實或改善，暫停該 scope 返工查根因，其他 READY 照常。

## 2. 已授權、實際可用時全力外包
- Codex 是唯一協調、整合與 GitHub 共享寫入 owner，不預設親自全文撰稿。優先將可獨立驗收的來源/Blueprint 實質分析、專屬 SAMPLE 正文、局部內容修補與獨立語意審查委派既有 W1 OpenCode v2 CLI、W2 Antigravity CLI。Codex 聚焦任務拆分、數學/來源確定性 QA、Word DOCX/全頁渲染、候選採納及 remote raw-byte readback。
- 有兩個不同 doc_id 的獨立 READY，且 W1/W2 各自已驗證 CLI、實際可用的授權模型/配額、工作權限及互不衝突的寫入範圍，應同時真正派工，不只做模型型錄查詢或保持 serve/GUI 存活。但不以 Worker 永遠 BUSY 為目標，不派空任務。
- 一個 Worker 可寫文件 A，另一個可審另一份已固定 SHA 的文件 B；同一文件的 Writer 不能自審。相同 doc/revision、共享 SAMPLE register/CURRENT、GitHub ref 之修改只准一個有效寫入 owner。各 CLI 採已驗證的安全、非互動、有界原生方式，不使用 Computer Use、危險授權、未知付費服務或隱性模型 fallback。
- 派工與回收需確切 work_id、doc_id、source/Blueprint/候選 SHA、範圍、真實 OS PID/session、起迄、原始 stdout/stderr、採納內容/審查結論及錯誤。serve PID、GUI PID、requested model、exit0、Token 消耗、Worker 自稱 PASS、429/空回覆都不等於有效工作；served-model 缺實際證據填 UNKNOWN。
- 某路由 429、權限、網路或模型身分無法驗證，只封鎖受影響 lane；不盲重試、繞過配額或無授權轉付費。所有合法模型都不可用時，先完成不同文件的確定性 READY；需要模型的精確工作標 BLOCKED，不假稱已全力外包。高成本主模型不應無必要重做原本合格的 Worker 工作。

## 3. 品質、讀回、續作
- Builder 不得自授 PASS；同候選 SHA 需有適用的技術/計算、Word 原生全頁視覺、與 Builder 獨立之語意/文類/近鄰/防複製審查。TEXT_ONLY≠VISUAL，CANDIDATE≠REAL/Human 正式接受。僅修真正違反驗收契約且有精確位置的缺陷。
- GitHub 共享寫入：fresh HEAD/同 path prestate → exact scope/必要競爭保護 → 單次派送 → 同 ref Git Blob/原始位元組 SHA-256 讀回；結果不明不盲重送。公開 repo 不上傳個資、真實學員、Token 或未公開第三方原件。
- 每階段終態後，有合法 READY 與仍活躍的執行會話，就立即下一件；唯一原生 120m 排程僅故障補漏、不是施工節流。GOAL ACTIVE、面板 HTTP200、排程通知、OpenCode serve PID 不代表背景 Writer 活躍。
- Human Gate 僅策略/Mission重大變更、Production/正式接受、新費用、法律契約/身分、OAuth/MFA、不可逆權限擴張及重大不明外部效果。已批准可逆候選不因換 Session 重問。

## 4. 真產能短回報
只有材料變更才短報：fresh HEAD、W1/W2 真派工與回收（work_id/PID/終態）、新不同 doc_id 合格 DOCX 淨增量、具名需求覆蓋、候選 SHA/QA/remote bytes、受阻車道、下一合法 READY。未知填 UNKNOWN。不得以 commit、版本、Worker 呼叫、Token 或長篇稽核報告冒充完成。

歷史完整原文可由 Git history 取得，未刪除必要執行收據。