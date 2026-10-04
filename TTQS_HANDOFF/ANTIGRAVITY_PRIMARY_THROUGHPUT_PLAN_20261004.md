# TTQS_ONE Antigravity 主力生產模式 — 2026-10-04

人類最新要求：WIN10 的 Antigravity / Gemini 3.8 Flash High 是主力施工者；Codex 很慢，應退出長時間內容生成，主要做派工、檢查、獨立複核、整合與發布。

## 核心分工
Antigravity 優先負責：
- 新文件 content.json
- 精確內容修復
- 下一批文件來源整理與內容準備
- Codex 產物的獨立語意複核
- 其他長時間模型工作

Codex 只優先負責：
- 選下一批 READY 文件
- 建立不可變工作包
- 共享資料衝突檢查
- Antigravity 產物的 fresh isolated 語意複核
- 精確缺陷定位
- CURRENT 發布與中央紀錄更新

固定主機程式負責：
- content.json -> DOCX
- 收據與 SHA
- OOXML/static
- 版面檢查
- 重複度與其他機械檢查

Codex 不得再用長時間模型工作做以上機械檢查。

## 生產線
Antigravity 並行生成 content.json
-> 固定 renderer 立即轉 DOCX
-> deterministic gates 立即執行
-> 通過者進 Codex 短複核佇列
-> PASS 後由 Codex 發布
-> FAIL 只把 exact locator 退給原 Antigravity 修復

各階段流水化，不得等上一份完全發布後才開始下一份。

## Antigravity 自適應並行
起始：
- 2 個 Antigravity content workers
- 1 個 Codex review/control worker

若兩個 Antigravity worker 各完成至少 2 個不同文件，且沒有模型額度錯誤、工作區衝突、共享事實衝突、輸出互蓋：
- 自動升到 3 個 Antigravity workers

若升到 3 後 30 分鐘內有效候選吞吐較 2 workers 提升至少 20%，且錯誤率沒有明顯增加：
- 可升到 4 個 Antigravity workers

最大先到 4，不再自行擴張。

若出現：
- provider quota / session collision
- 有效候選吞吐下降
- 連續工作區衝突
- 主機 CPU 或記憶體長時間高負載造成實際變慢

則自動降一級，不等待 Human。

## 緩衝區
維持 2~4 份已通過 deterministic gate、等待 Codex 語意複核的候選。

如果等待複核候選 < 2：
- Antigravity 優先 BUILD

如果等待複核候選 >= 4：
- 不再盲目堆積新 BUILD
- Antigravity 改做 exact repair 或下一批來源/內容準備

## 禁止
- Codex 長時間寫 content.json，除非 Antigravity 不可用
- 每份文件重新寫 renderer
- 模型自行做 Word/PDF/版面機械檢查
- 同一文件雙 build owner
- 自產自審
- 不同 worker 寫同一工作目錄
- 同時施工 shared_fact_group 重疊文件
- 因速度降低任何現有品質 gate

## 目標
真正指標是每 30 分鐘：
- 新增有效 content payload
- 新增有效 DOCX candidate
- 新增 CURRENT
不是 log 數量、喚醒次數或控制程式修改量。
