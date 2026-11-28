# DOCX 0036 R13｜課程設計進度與訓練規劃

**候選文件。R12 語意審查保持其原 exact SHA；R12 補充視覺審查為 PARTIAL。R13 修復三項定位版面問題，本機技術與 19 頁視覺檢查完成，R13 獨立 exact-SHA 語意與全頁視覺審查已 PASS（僅示範成品品質）；真實 checkbox 036 佐證未證實。未正式接受或升格。**

## 官方對應

- DOCX 0036 = I07-E04 = 官方方框 036。
- 官方來源、Unique Blueprint、Mapping 與 85 筆合成替換登錄均延續 R12；來源 SHA 見 `PROGRESS.json` 和 `inputs/`。

## R13 精確修復

獨立 reviewer 對 R12 exact SHA 補查全部 19 頁後，判定 visual supplement PARTIAL：第 15 頁例外控制表與第 16 頁完整合成案例走讀續頁沒有重複表頭；第 17 頁空白交接欄太短。R13 只重複這兩表的首列表頭並擴大空白填寫欄。表單仍留白，不代表已交接。

`word/document.xml` 是相對 R12 唯一改變的 DOCX package part。R13 DOCX SHA-256：`0ea26e673d363f3d16c2cd8e66611c4920a70d111f3705c617a1cfc62687242f`。

擴大表單後曾出現一頁空白。根因是原本獨立的手動分頁段落在表單增高後被推到空白頁，接著又將附表 A-1 推至下一頁。R13 最終版移除該獨立分頁段落，讓 Word 自然分頁；最終 PDF 19 頁、無空白頁。兩份失敗分頁 PDF、頁面影像及 SHA 保存在 `evidence/` superseded iteration 資料夾，沒有混作最終驗收。

## 驗收

- 最終 Word COM PDF SHA-256：`d05668efb4b9ef3ffa2820b56c0eddd086274e3ae3673ac84035c7ecaa5099a7`，共 19 頁；19 張 PNG。
- 第 15、16 頁表格續頁重複欄位表頭；第 17 頁填寫欄加長；A-1/A-2 附表分別在第 18/19 頁，無空白頁。
- 詳細技術、視覺與修復收據：`review/0036_R13_technical_and_visual_receipt_R01.json`。
- R13 exact-SHA 獨立語意與19頁視覺審查：PASS（只代表 SAMPLE/SYNTHETIC 成品品質；真實 checkbox 036 佐證 NOT EVIDENCED）。審查原文見 `review/0036_R13_independent_semantic_visual_review_R01.md`；候選未正式接受或升格。

