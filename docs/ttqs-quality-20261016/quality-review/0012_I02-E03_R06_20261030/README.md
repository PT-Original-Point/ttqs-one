# 0012 / I02-E03 — R06 候選與驗收狀態

此資料夾保存 0012（官方要求 I02-E03）R06 候選及其來源、修補清冊、技術／版面收據與外包審查原始收據。文件目前仍是 SAMPLE/SYNTHETIC 候選，未獲協會正式接受。

- R06 DOCX SHA-256：f4c7a8242cb5ae0c4c038d546b2d45cac938028a521ea6ffcb5cc02334c03d13
- 前版 R05 SHA-256：a90340289d360a7705fad8137db3a33b648a126ca67b1454d66c0b9288f9d9b5（保留；其語意 PASS 只屬於 R05）
- 確定性技術驗收：PASS；12 表、138 列、42 個合成識別碼、無空白表格格、算式與字級檢查通過。
- Word 原生 PDF：17 頁；R06 版面檢查 PASS。所有改動頁均逐頁目視。
- 語意驗收：尚未通過。OpenCode v2.2.3 在 2026-10-30 19:21:46 +08:00 收到免費模型供應端 HTTP 429 provider.free-limit，沒有審查回覆；請求模型為 opencode/glm-5.3-flash-free，實際模型與 token 使用量 UNKNOWN。供應端回報 retryAfterMs=47,577,000；未盲目重試。
- 因 R06 SHA 與 R05 不同，不把 R05 的語意 PASS 跨 SHA 搬用；R06 僅能在完成限定差異審查後判定。
- 真實協會資料、正式核准與簽章未提供，REAL／正式接受維持 UNKNOWN/HOLD。

## 修補範圍

依 R05 獨立審查的 F1/F2/F4 作局部修補：將 SYN-037/038/039 的 SAMPLE 時限放入 §5 對應步驟並保留法定期限優先；統一 SYN-022 用語；將 §13 的 Blueprint row hash 工程語言改為受控管理側欄參照。R05 原檔未改寫。

## 收據

- evidence/receipts/：建置、技術、視覺、修補與狀態收據。
- evidence/prior_R05_semantic_review/：R05 原始審查回覆及原始派工終態，僅供歷史基線。
- evidence/R06_semantic_route_attempt/：R06 限定差異審查包、prompt、OpenCode stdout/stderr、terminal receipt；可見本次 429 且沒有語意回覆。
- evidence/0012_I02-E03_R06_WORD_NATIVE.pdf 與 evidence/pages/：17 頁 Word 輸出及頁面影像。
