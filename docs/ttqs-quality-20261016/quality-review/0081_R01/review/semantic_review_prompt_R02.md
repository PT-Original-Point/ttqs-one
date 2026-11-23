# 獨立 exact-SHA 語意驗收：DOCX 0081 R02

本次為唯讀審查。不得修改、建立、覆寫任何來源、文件、收據、影像或 GitHub 檔案；不得使用 Computer Use；不得提交或推送。你不是 0081 Builder。請直接檢查所附 DOCX 位元組與正文，不可只讀 Builder 自評或 Markdown 藍圖。若無法實際讀取某附件，明確標示限制，不得推測 PASS。

## 候選身分（先核對）
- DOCX：`docs/ttqs-quality-20261016/quality-review/0081_R01/candidate/0081_R02.docx`
- 預期 SHA-256：`5b77683da206a9973f132c2222775aa22d96ffb7b24042cdb6230d6875db04e3`
- 正文 SHA-256：`653bc92095889fa0b3c39a3d126bce86245aa902f8649da054119a47ddb71640`
- Word 輸出 PDF：`docs/ttqs-quality-20261016/quality-review/0081_R01/qa/0081_R02_word_render.pdf`，13 頁；視覺收據逐頁列出頁圖雜湊。
- 身分不符時停止語意裁定，回報 IDENTITY FAIL。

## 權威來源與唯一 Blueprint
- Human Mission：所附 `01_HUMAN_MISSION_AND_ACCEPTANCE.md`，SHA-256 `07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8`。
- 文類逐指標寫作手冊：`02_GENRE_WRITING_MANUAL.md`，SHA-256 `7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa`。
- 157 方框藍圖：`03_157_CHECKBOX_BLUEPRINTS.md`，SHA-256 `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216`；本件第 086 項。
- 官方訓練機構佐證文件資料表 PDF：所附來源 SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；印刷第 6 頁 17b。
- Unique Blueprint：`UNIQUE_BLUEPRINT_0081_R01.md`，SHA-256 `ea24a5986af99c2c6b8e68075e64c2e1d0a8702ab3c4434d94120191de3fde18`。
- 上游比較 DOCX 0080 R05 SHA-256 `5a4d400b472d2b6f0cfcec23bd1cd908f468d3ba857aea19dba8b699b375055b`，只用於上游已核實事實與文類區分。

## 精確映射
DOCX 0081 = I17B-E03 = 指標 17b = 官方方框序號 086。不要把文件編號與方框流水號互換。官方 17b 要求的結案報告與課後課程檢討行動計畫查核，以及 157 項 086「結案與行動計畫查核：課後改善進度及下一班驗證」是本件用途。0080/085 是課程評量與改課決定；0079/084 是個別學習建議；0082/088 才是訓練後行為轉移調查。

## 必查項目
1. 候選 exact SHA、實際 DOCX 文字與表格；禁止以 Builder 收據代替檢查。
2. 是否是 0081 結案及課後行動查核文類；遮住標題是否仍能辨認用途；是否能與 0080、0079、0082 區分，且沒有把文件號與官方方框號混淆。
3. 對 17b 官方 0–3 分級及第 086 項的實質符合度：0080 A1–A7 逐項查核、進度/所需證據、EQ1–EQ7、決定、缺件、重啟與升級、結案要項、下一班驗證與可重用空白表單是否完整、可直接操作。
4. 抽核交叉文件事實：上游案件 SYN-0073-2026-A01、0080 的 A1–A7、弱題 Q01/Q17/Q18/Q19 各 11/16、12 人合成新班與 0080 16 人基線分開、0082 行為轉移邊界。不得把不同班次的分數說成因果效果。
5. 獨立重算：C1–C5 為 20/24、15/24、18/24、16/24、16/24，合計 85/120=70.83%、平均 7.08/10；學科 198/240=82.50%；Q01 9/12、Q17 8/12、Q18 10/12、Q19 8/12；12 個逐人向量合計、6 PASS/6 HOLD；P05 與 P11 的重大錯誤覆蓋規則是否一致。`8/10 且無重大錯誤`必須維持 PROPOSED，不能變成官方或本會政策。
6. `SAMPLE/SYNTHETIC`、`PROPOSED`、`NOT_EXECUTED`、`REAL=UNKNOWN/HOLD`、`formal_acceptance=NOT_GRANTED` 邊界是否全程清楚；不得捏造本會核准、簽名、人員、事件、成效或第三方原件。
7. 所附 23 列替換清冊是否每筆對應正文定位、所需真實來源/替換、驗證規則與 REAL 狀態；0079 個別卡片細節須排除。
8. Word 輸出 PDF 13 頁與附圖：頁 1 的 §1.3 表頭孤行已由 R02 移到下一頁，請核對；如只能讀取 PDF 而不能目視所有影像，需說明實際範圍。標出其餘跨頁表格、可讀性或版面限制。

## 回覆格式
- `observed_docx_sha256`、`identity`、`verdict`（PASS / PARTIAL / FAIL）。
- 明確指出檢視的實際位元組與附件範圍。
- 逐項結果（1–8）及支持證據，正文印刷頁/節/表定位。
- 缺陷表：嚴重度、精確定位、證據、最小必要修正；沒有缺陷要明寫 none。
- `REAL=UNKNOWN/HOLD`；`formal_acceptance=NOT_GRANTED`。此審查只給 exact-SHA 候選語意結果，不代表正式接受。
