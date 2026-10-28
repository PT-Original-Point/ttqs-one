# 0127 / I19-E16 R06 候選證據包

## 狀態

這是原始點協會文件 0127（官方 I19-E16）的可逆候選，不是正式接受、REAL 成果或送審版本。Word 原生輸出為 12 頁。

- DOCX SHA-256：`c6c9a6270f429052aa959f9ae6fdca10ebd02a308a33b9d28c84e7d36ad48008`
- Word-native PDF SHA-256：`a7d388d47387c7180077a4423bf9c3a02a119a8bf5b8a394a2dfa1d2a4dd5b6c`
- 唯一 Blueprint：`0127/I19-E16`；官方來源定位：查核佐證資料表第 8 頁。
- R06 保留兩構面、8 案市場樣本、24 組配對顧客樣本與附錄 A/B。所有樣本皆為 SAMPLE/SYNTHETIC；無可證實的協會 REAL 課程、客戶、交易、問卷、核准或成效原件。

## 本次修正及檢核

R06 從 R05 移除一頁低密度、會隨候選狀態變動的附錄 C 候選驗收快照；相同的驗收狀態留在外部 QA 收據。正文前段及原有 19 張表均逐項比對未變；Appendix C 刪除後表格數由 20 張變為 19 張。Word COM 隱藏匯出成功，PDF 為 12 頁；全頁目視完成，最終頁為有實質替換清冊的第 12 頁。正文直接字級最低 10.5 pt，表格最低 9.5 pt。CSV 確定性重算：市場 A/B 潛客 32/48、首購 8/15、轉換率 25.00%/31.25%；顧客問卷各期 72 個題項、總分 234/288、均分 3.25/4.00。

## 獨立語意審查

R06 exact-SHA 語意審查目前 **沒有判定**。唯一一次 OpenCode V2.1.4 CLI 指定 `opencode/deepseek-v4.1-flash-free` 的審查呼叫回傳 HTTP 429 `Free usage limit reached`，沒有模型審查正文；實際供應模型身分及 token 用量均 UNKNOWN，未切換模型，也未付費。依回傳的 `retryAfterMs=41208000` 暫停此免費推論路由，直到釋放窗口或出現新的帳戶／服務證據。

歷史 Antigravity R01 語意回覆只對舊候選 SHA `1fa7dd73f2e62520c0d27dedfadebe8c8ddf3096f40b7928b8c715794fe4b59a`，範圍為文字語意、不含視覺；其中供應端模型身分仍 UNKNOWN。因此它不是 R06 的 exact-SHA PASS，也不授予正式接受。對 R06 的語意審查及正式接受均仍待完成。

## 檔案

- `candidate/`：可直接開啟的 DOCX 候選。
- `render/`：Microsoft Word 原生 PDF。
- `source/`：官方定位、唯一 Blueprint、crosswalk 證據、合成 CSV 及 replacement register。
- `qa/`：本機 exact-SHA 技術／數學／逐頁目視收據、R06 Appendix C 最小修正、Word 原生匯出、OpenCode 429 原始收據與歷史 Writer 失敗資料。
- `qa/history/`：R01 舊 SHA 的 Antigravity 原始回覆及收據，只供歷史追溯。

此包未包含個人識別資料或 REAL 協會原件。`manifest.json` 列出本包其他檔案的 byte count 與 SHA-256。候選仍為 CANDIDATE；Human 正式接受未授予。
