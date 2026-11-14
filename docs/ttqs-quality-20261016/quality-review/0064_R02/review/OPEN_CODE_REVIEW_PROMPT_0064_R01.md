# TTQS ONE 0064 R01：獨立 exact-SHA 品質審查

你是本文件的獨立審查者。這是一個只讀審查工作；不得修改任何檔案、重建 DOCX、呼叫 Computer Use，或把建置者自己的技術收據當成語意 PASS。

## 審查對象與身分

- 專案：TTQS_ONE
- doc_id：0064
- 官方需求：I14-E05
- 官方查核表 checkbox 流水號：069（不是 doc_id）
- 候選：R01；狀態仍為 CANDIDATE，Human 正式接受尚未授予
- 審查時要求自行讀取並重新計算候選 SHA-256；預期審查對象 SHA：`E7A18CCC4429A69678C8C36D362F27FAC452B95E8889C894F8892DE9E5568369`

## 必讀本機資料

本審查的工作目錄為本檔所在的 `review` 目錄。請直接讀取下列檔案；不要只依賴本提示、舊收據或建置者自述。

1. `../candidate/0064_R01.docx`：唯一審查候選，先核對 SHA。
2. `docx_text_0064_R01.txt`：候選逐段與逐表抽取文字。
3. `../evidence/0064_R01.pdf` 及 `../evidence/pages/page_01.png` 至 `page_11.png`：逐頁檢視版面；圖片為同一候選 SHA 的 Word 匯出頁面。
4. `../UNIQUE_BLUEPRINT_0064_R01.md`：本件獨特 Blueprint。
5. `../inputs/official_source.pdf`：官方需求原文；核對第 5 頁的 I14-E05。
6. `../inputs/0060_R08.docx`、`../inputs/0060_R08_SYNTHETIC_REPLACEMENT_REGISTER.csv`：同案來源及其事實型態。
7. `../inputs/0061_R03.docx`、`../inputs/0061_UNIQUE_BLUEPRINT_R02.md`、`../inputs/0061_R03_SYNTHETIC_REPLACEMENT_REGISTER.csv`：相鄰需求區隔來源。
8. `../evidence/fixture/synthetic_index_0064_R01.json`、`../evidence/benchmark_runs_0064_R01.csv`、`../evidence/benchmark_summary_0064_R01.json`：合成索引、逐次結果與彙總。
9. `../evidence/0064_R01_SYNTHETIC_REPLACEMENT_REGISTER.csv`：逐項 SAMPLE/SYNTHETIC 替換清冊。
10. `final_integrity_check_0064_R01.json`、`../evidence/visual_review_0064_R01.json`：可作交叉核對線索，但不是語意 PASS 的替代品。

## 審查要點

逐項檢查並明確指出證據位置（頁碼、章節、表格列或短摘錄）：

1. 官方 I14-E05 的要求是否正確落在「資訊檢索效率測試報告」文類；doc_id、官方需求和 checkbox 是否分明。
2. 遮住封面標題後，只讀正文是否仍能辨認其為實際的檢索效率測試報告，而非管理手冊、系統建置提案或改善計畫。
3. 內容是否具體且可操作：固定母體、納排條件、環境、角色權限、日期、快取條件、逐步程序、足量查詢情境、重複測次、逐次輸出、結果摘要、重算例、失敗／退件／HOLD 條件及 SAMPLE 查詢紀錄。
4. 檢查 200 筆 raw run 對 JSON 和正文表格的一致性；正確結果率、拒絕、歧義 HOLD、未授權洩漏、p50/p95/max、單位和 nearest-rank 百分位算法是否正確。速度不能抵銷錯誤或未授權洩漏。
5. 逐項核對 0060 同案事實。`SYN-0060-FACT-003` 的 2026-08-15 是 SAMPLE 授課日期；`SYN-0060-FACT-004` 的 2026-09-14 是 SAMPLE 追蹤日期，兩者不是索引檔案形成日。0064 索引另設 2026-08-18、2026-09-18 合成形成日。不得混淆其用途；若有錯置，明確列出正文位置。
6. 檢查 0060/0061/0062/0063/0064 的用途邊界與本件獨特性，特別確保不是把 0061 的人工流程、0062 的全庫清冊或 0063 的改善機制冒充 0064 測試。
7. 檢查每項虛構資料是否明確標為 SAMPLE/SYNTHETIC；真實系統、核准、正式使用者和門檻是否維持 UNKNOWN；不得將樣本速度寫成協會實績或 TTQS 官方門檻。
8. 以小型志工協會行政人員及評核委員的使用情境判斷是否可直接照表操作、看懂結果並知道何時停止、拒絕或交由誰覆核。
9. 逐頁目視 11 頁，確認字級、表格欄寬、重複表頭、跨頁列、孤立章標、截字／亂碼、可讀性和頁面留白。
10. 確認無協會真實人員、正式系統、真實權限、部署或核准等無來源事實。

## 回覆格式

先輸出候選檔案 SHA 與是否相符。接著只可選一個總結：`PASS`、`PARTIAL`、`FAIL`。PASS 必須代表以上重要檢查皆有直接證據支持；技術自檢或文件存在本身不算 PASS。

每項 finding 使用：`[嚴重度] [頁碼/章節/表格] [PASS/FAIL] [具體理由及可核對短摘錄]`。最後列出：

- 文類與官方範圍
- 數學／資料一致性
- 同案事實與日期界線
- SAMPLE/REAL 界線
- 逐頁版面
- 是否需要修正；若需要，只寫精確最小修正項目
- 對 exact SHA 的最終 verdict

只對你實際讀到的資料下結論；無法讀取的材料或頁面標 `UNKNOWN`，不得推測為 PASS。
