# 0022 / I04-E01 — R01 候選交付

狀態：CANDIDATE SAMPLE/SYNTHETIC；未宣稱 REAL 或 FORMAL_ACCEPTED。

- 候選 DOCX：`R01_candidate/0022_I04-E01_R01.docx`
- DOCX SHA-256：`859b09906f9e7045e7c55090e81ab5aa84fa610423988bc870559bfdf0bb8f2f`
- 技術 QA：`R01_candidate/qa/technical_qa.json`，對同一 SHA；Q10 人數、排行表與合成登錄數一致，預算加總與來源資料相符，XML/DOCX 可讀，9 頁渲染證據存在。
- 視覺 QA：`R01_candidate/qa/visual_review_receipt.json`，同 SHA，9 頁 PASS。
- 獨立語意：`R01_candidate/qa/semantic_review_receipt.json`；W2 R05 對 Q10 唯一差異及其算術／排序影響完成 scoped PASS，同 SHA；其他未變章節沿用 R04 PASS。請求路線為 `gemini-3.8-flash-high`，實際服務模型為 UNKNOWN。
- W2 原始封包、stdout/stderr、終態與正文均保存在 `R01_candidate/source/worker/W2_R04_TEXT_ONLY/`、`W2_R05_TEXT_ONLY/` 等資料夾；R02 工具拒絕與 R03/R04 歷史回覆也保留供追溯。
- `inputs/` 保存官方需求 PDF、需求 crosswalk、觀測資料、計算稽核、合成登錄及 R02 局部修補來源。
- `FILE_HASH_MANIFEST.json` 綁定封裝檔案位元組；套件內 `.gitattributes` 停用換行轉換，以維持原始收據位元組。

本次是既有候選與 QA 的回收同步，未重派 Worker，未改 DOCX 內容。