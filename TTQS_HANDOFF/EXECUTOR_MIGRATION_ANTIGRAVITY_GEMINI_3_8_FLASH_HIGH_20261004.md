# TTQS_ONE 執行者切換：Codex + Antigravity / Gemini 3.8 Flash High — 2026-10-04

人類最新明確命令：
- 從現在起，TTQS_ONE 停用 OpenCode / Muse Spark 1.3 Free，不再派任何新工作給 OpenCode。
- 第二執行者改為 WIN10 本機的 Antigravity，模型固定為 Gemini 3.8 Flash High。
- WIN10 沒有 MCP；不得依賴 MCP、Win11 Factory 或遠端橋接來控制 Antigravity。
- 由目前已在 WIN10 本機工作的 Codex 直接發現、啟動、派工、讀回 Antigravity。
- 速度優先：盡可能把可外包的內容生成、修復與獨立複核工作交給 Antigravity。
- Codex 保留唯一 canonical 控制權與發布權。
- 不降低任何既有 TTQS 文件品質 gate。

## 執行架構

### Codex
保留：
- 唯一 canonical dispatcher
- queue / checkpoint / CURRENT / central synthetic/replacement register 唯一共享寫入者
- deterministic gate 整合
- promotion
- Antigravity 產物的 fresh isolated semantic review
- Antigravity 不可用時的合法備援工作

Codex 應避免長時間內容生成，除非：
- Antigravity 不可用；
- exact repair 只能由 Codex 完成；
- 需要獨立複核 Antigravity 產物。

### Antigravity + Gemini 3.8 Flash High
優先承接：
1. 新文件 content payload 生成；
2. exact content repair；
3. Codex 產物的獨立 semantic review；
4. 其他不需 canonical shared mutation 的長時間模型工作。

優先使用目前已證明的「content payload -> 固定 renderer」管線：
- 模型只生成 content.json；
- 固定 host renderer 生成 DOCX；
- static/layout/receipt gates 照舊；
- builder 不自行重寫 renderer。

## WIN10 本機路由

Codex 必須在 WIN10 本機自行 fresh-discover Antigravity：
- executable / launcher
- running process
- CLI / local service / session interface
- project/workspace context
- available model identity

不得猜執行檔、port、模型 slug。
不得要求 Human 手動搬運工作。

路由優先：
1. Antigravity 官方本機 CLI / background service / session interface；
2. 其他官方本機 headless route；
3. 若只能透過可見 GUI，先回報真正 Human Gate，不得自行做會搶焦點的滑鼠鍵盤自動化。

## 模型
唯一允許的 Antigravity 模型：
Gemini 3.8 Flash High

必須驗證實際使用模型。
不得偷偷換成其他 Gemini 或其他模型。

## 工作隔離
Antigravity：
- 不直接寫 CURRENT
- 不直接改 canonical queue
- 不直接改 central synthetic register
- 不直接改 supervisor / scheduler
- 只寫 isolated task workspace / payload / candidate / receipt / review result

Codex：
- 驗證 exact work_id / deliverable_id / evidence hashes / candidate SHA
- 再做共享 mutation 與 promotion

## 並行
預設允許：
- 1 個 Antigravity 長工
- 1 個 Codex 控制／review／integrate 工作

若 Antigravity 官方本機 route 明確支援多 session 且沒有 quota / collision / shared-fact 衝突，可由 Codex以 2-worker bounded experiment 驗證後再增加。

禁止：
- 同一 deliverable 雙 build owner
- shared_fact_group 衝突
- 自產自審
- 因並行降低品質 gate

## OpenCode 停用
OpenCode / Muse：
- ACTIVE_DISPATCH_DISABLED = true
- 不再 quota probe
- 不再 BUILD
- 不再 REVIEW
- 不再 REPAIR
- 不得作 acceptance prerequisite

歷史 OpenCode receipts / review evidence / logs 保留作 provenance，不刪除既有已驗證證據。

## 立即執行
Codex 下一個合法動作：
1. 不打斷已經穩定寫入的 candidate / deterministic gate。
2. 停止任何尚未開始的 OpenCode dispatch。
3. 在 WIN10 本機 fresh-discover Antigravity 官方執行路徑。
4. 驗證 Gemini 3.8 Flash High。
5. 做一個 harmless smoke。
6. smoke PASS 後立即把下一個 READY content build 派給 Antigravity。
7. Codex 同時處理 renderer/gates/review/promotion，不等 Antigravity 空轉。
