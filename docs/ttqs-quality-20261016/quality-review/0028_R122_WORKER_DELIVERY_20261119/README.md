# 0028 / I05-E02 — R10 候選交付

狀態：CANDIDATE；本資料夾不是 REAL 或 FORMAL_ACCEPTED 宣告。

- DOCX SHA-256：`b818f9ce6363db5fb6850cfd9f0449715633e70bcc6760a74b5bd5e3002fad2d`
- 技術 QA：`qa/technical/DETERMINISTIC_QA_R10.json`，同 SHA，`checks_pass=true`；正文最小字級 10.5 pt、表格最小 9.5 pt，25/25 合成 ID，無空列、未填佔位字或缺少必要修補。
- 全頁視覺：`qa/visual/VISUAL_REVIEW_R10_SAVEAS2_R02.json`，同 SHA；Word COM 匯出 PDF 後逐頁檢視 17/17 頁，無裁切、重疊或缺字。第 6 頁留白為 LOW 非阻斷觀察，不因頁數經濟性重修。
- 獨立語意審查：W2 `qa/semantic/W2/W2_READBACK_R01.json`，同 SHA，10 項 PASS、0 FAIL/UNKNOWN，總判 PASS。請求模型為 `gemini-3.8-flash-high`；供應端實際服務模型為 UNKNOWN，因 CLI 無獨立 provider telemetry。此前 W1 撰稿 Owner 與此 W2 Reviewer 不同。
- 撰稿來源：`worker/W1_writer/` 與 `candidate/lineage/BUILD_RECEIPT_R01.json`；R01 正文 SHA 與 W1 原始正文 SHA 一致。R10 僅做有界版面/定位修正，未改字級。
- 正式來源、crosswalk、專屬 Blueprint、合成事實清冊與源文件 SHA 收據在 `inputs/`。
- 原始視覺 PDF 與 17 頁 PNG 在 `0028_I05-E02_R10.pdf` 及 `qa/visual/pages/`。
- `FILE_HASH_MANIFEST.json` 記錄本封裝中每個檔案的位元組數與 SHA-256（不自我雜湊）。

此封裝只把可驗證候選和品質證據交付至 PR #92；不表示正式核准或 REAL 成果。