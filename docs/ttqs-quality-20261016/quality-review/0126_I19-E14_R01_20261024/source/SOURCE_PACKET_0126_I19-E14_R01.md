# DOCX 0126 / I19-E14 專屬來源包 R01

## 權威與精確對應

- 專案：TTQS ONE；交付文件編號：0126；官方方框編號：I19-E14。兩種編號不可互換。
- 官方方框原文：**進行訓後薪資調查，部份訓後學員微幅調薪。**
- 官方查核佐證文件資料表：第 8 頁；本機 PDF 文字抽取確認原文存在（空白與 PDF 換行正規化後比對），不是視覺逐像素驗證。
- 對應正式交付名稱：`0126__訓後薪資變化調查與分析表.docx`。
- 文類：分析／評估報告，必須呈現訓後薪資調查的資料口徑、可重算分析、限制與決策，不可做成一般薪資名冊或泛用成果報告。

## 來源定位與版本

- 本機官方 PDF：`SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf`；SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。
- PDF 第 8 頁（pypdf index 7）文字抽取 SHA-256：`57c6b33d70b665bd41b8d58ff58f5c0d78f9c2c751ccd9c6dd1b740b2fbf374e`；抽取 681 字元；官方原句移除空白後精確存在。
- GitHub PR #92 候選分支來源基準：`dda88f97bd24844c8c718800f0a096f488fd9df3`。
- 官方 PDF GitHub 路徑 `quality-review/0037_R07/inputs/official_source.pdf` 的 Git blob SHA：`9c7621decdad585b743bf2b3d949ee5518b7bee0`；這是 Git blob SHA，不是檔案 SHA-256。
- 目前 142 文件 Blueprint 輸入：`CONTROL\BLUEPRINT_CURRENT.jsonl`；本機 SHA-256 `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`；PR 分支同路徑 Git blob SHA `cab446ede479001334289d18062e6b8bb2340dc3`。0126 精確 JSON 列 SHA-256 `bc640157d7f6e462de26a1b021af414be182b737319df3573ebbdfed34813cc6`，逐欄複本見 `BLUEPRINT_ROW_0126_I19-E14.json`。
- 本機 129→142 對照表 SHA-256：`1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`；本輪未取得其 GitHub 原始位元組，故只作本機 crosswalk 證據，不冒稱遠端讀回。

## 專屬範圍與鄰件排除

本件只回答「有同意且薪資資料可驗證的訓後學員，在一致追蹤期間是否出現薪資變化、幅度如何，以及資料支持到什麼證據強度」。

- 0125 / I19-E13 是所學運用於職務的追蹤紀錄；職務運用不等同薪資變化，本件不能代替其觀察紀錄。
- 0127 / I19-E16 是目標市場及顧客價值量化效益；市場／顧客指標不得混入個人薪資結果。
- 本件不能推論協會整體績效、就業品質、訓練因果或所有學員薪資提升。

## 資料使用界線

目前沒有提供可驗證的協會訓後薪資 REAL 原始資料、受訪同意、薪資證明、正式核准或第三方原件。任何初稿數字必須逐項標為 `SAMPLE / SYNTHETIC ONLY`，以匿名角色碼示範完整方法，並列 replacement register。不得把示範薪資、日期、樣本、調查回覆、核准或成效說成原始點協會實績。未獲授權的個資及薪資證明不得上傳公開 GitHub。

## 歷史版本隔離

歷史檔 `1905_0126__I19-E14__01__訓後薪資變化調查與分析表__R02.docx` SHA-256 `14b0cd010606b9f609b829c525378c14c00cf73d510ec7370bc6dc7bae13ae45`；20 段落、7 表格、抽取文字約 1,153 字元。該檔只供檔案沿革識別；Blueprint 規定 `historical_body_use=PROHIBITED`，不得複製、改寫或作新稿模板；本輪未找到它的現行 exact-SHA QA 收據。

## 建置前必需條件

Writer 必須先依 `UNIQUE_BLUEPRINT_0126_I19-E14_R01.md` 產生完整正文，至少包括方法、完整合成明細、公式逐步計算、分群、圖表數據、限制、決策和 replacement register。只交標題、空白問卷或摘要即退件。完成文字後由 Windows Word 建立 DOCX，並分別作技術／逐頁視覺與獨立 exact-SHA 語意驗收。