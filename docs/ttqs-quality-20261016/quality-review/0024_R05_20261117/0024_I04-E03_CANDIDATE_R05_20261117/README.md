# 0024 I04-E03 候選 R05

狀態：CANDIDATE / NOT FORMALLY ACCEPTED。此提交保存一份具名需求候選及其來源與驗收證據，不代表協會正式採用。

## 候選與品質範圍

- DOCX SHA-256：84d2c704b7ae3830a061291077c28ff0786df7c471290d2bbec39da3f917cb12（58,131 bytes）。
- 修補範圍：僅將附錄 B 標題移至新頁，修正可見版次及同件替換登錄；未重寫正文。
- 技術 QA：PASS。DOCX/OOXML 可讀、來源與 Blueprint 綁定、官方要求詞句、SAMPLE/REAL 邊界、字級、空白佔位、表格及加權計算檢查通過。
- 視覺 QA：PASS。34 頁 PDF 與 34 張頁面圖；所有 34 頁經三張完整頁面聯絡表逐頁檢視，修改區及密集頁另以全尺寸檢查。無裁切、重疊、溢出或頁緣內容遺失。
- W1 獨立語意審查：PASS，精確綁定同一 DOCX SHA。Reviewer 回報 5 項低度追蹤點，皆非阻擋；其未自行重算 DOCX/文字 SHA，本地已重算並核對原始回覆 SHA。
- 審查請求模型為 opencode/longcat-2.5-free；供應端實際模型 UNKNOWN。未把任何綁定舊版候選的 W2 PASS 拼入 R05。

## 來源與保真

官方需求、I04-E03 對照、專屬 Blueprint、原始頁面讀回、R05 修補收據、技術/視覺/語意收據及 W1 原始輸入/輸出均隨附。完整位元組 SHA-256 列於 PACKAGE_MANIFEST.json。候選與品質 PASS 不等於正式接受。