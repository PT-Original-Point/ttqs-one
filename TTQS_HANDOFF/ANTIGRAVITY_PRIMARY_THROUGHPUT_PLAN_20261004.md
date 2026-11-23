# TTQS_ONE Antigravity 額度感知主力生產模式 — 2026-10-04

人類修正：Antigravity 有使用額度，禁止把「速度快」誤解為「可無限多開」。OpenCode / Muse 已因供應端 quota 無法繼續，TTQS_ONE 不得在 Antigravity 重演同一錯誤。

## 核心原則
- Antigravity / Gemini 3.8 Flash High 仍是主力長工。
- Codex 主要做派工、機械檢查協調、獨立複核、整合與發布。
- 預設只開 1 個 Antigravity 長工。
- 不再自動 2 -> 3 -> 4 擴張。
- 只有在取得可驗證的 Antigravity 使用額度資訊，並量出每份「最終通過文件」的實際額度成本後，才允許短時間增加第 2 個 worker。
- 未證明額度餘裕前，最大並行 Antigravity=1。

## 額度帳本
每次 Antigravity 呼叫都記錄：
- 開始/結束時間
- deliverable_id / work_id
- 實際模型
- 成功/失敗/被限額
- 若官方介面有提供：五小時剩餘額度、每週剩餘額度、重設時間、輸入/輸出 token 或其他官方用量欄位
- 是否產生有效 content.json
- 是否最後進 CURRENT

不得用 log 長度或請求數假裝 token 用量。

## 三份樣本估算
先用單 worker 完成最多 3 份不同 family 的真實 READY 文件：
- 記錄每份前後的官方額度差
- 計算每份有效 payload / 每份 CURRENT 的額度成本
- 若官方不暴露數字，標 UNKNOWN，不得猜

只有有可驗證 headroom 且三份樣本沒有 rate-limit / quota / session 錯誤，才可短時間測第 2 worker。

## Antigravity 工作優先級
額度只花在高價值模型工作：
1. 新文件 content.json
2. exact content repair
3. SAMPLE/SYNTHETIC substantive content
4. Codex 無法快速完成的語意長工

預設不要用 Antigravity 做：
- renderer
- static/layout
- SHA/receipt
- queue/checkpoint
- 重複來源讀取
- Codex 可在短時間完成的 acceptance readback
- 週期性 availability probe

## Codex
Codex 做：
- 派工
- 來源快取與 evidence packet
- 固定 renderer / deterministic gates 的控制
- Antigravity 產物 fresh review
- promotion
- 額度帳本與速率控制

若 Antigravity 被限額：
- 立刻停止 Antigravity 新長工
- 不輪流拿正式 TTQS lane 探 quota
- Codex 繼續 deterministic work、review、promotion 與必要 BUILD
- 等官方 reset / usage state 證明恢復後才重新派 Antigravity

## OpenCode 歷史額度追溯
停止 OpenCode 新呼叫，但離線整理既有 OpenCode logs/session exports：
- 第一次 structured quota 時間
- 成功呼叫數
- quota 拒絕數
- Retry-After / cooldown
- 若 metadata 存在則輸入/輸出 tokens
- session/model
- 每次成功與拒絕的時間序列

只做離線讀取；禁止再送 OpenCode probe。

## 產量指標
每 30 分鐘看：
- 新有效 payload
- 新有效 DOCX candidate
- 新 CURRENT
- Antigravity 成功任務數
- Antigravity 額度拒絕數
- 官方五小時/每週餘額（若可取得）
- 每份 CURRENT 的估算額度成本

速度目標是「在不提前耗盡 Antigravity 的前提下，最大化評核前最終通過文件數」。
