# 0045 R01 — 訓練資源採購與甄選管理辦法

## 身分與狀態

- 文件編號：0045
- 官方 Unique Requirement：I10-E01
- 官方方框流水號：047
- 版本：R01 候選
- DOCX SHA-256：`c40f401fade386d831b5ba170f9cb17a24313de84474cd957a92ecf8d75a7049`
- 狀態：候選文件；技術與版面檢查完成；獨立語意審查待完成；未正式核定、未推升。

文件依官方要求建立訓練需求與規格、資源組合評估、評選、採購／契約、交付驗收及後續管理流程。實例中的個案、廠商、評分、日期、價格、契約代碼、成效與門檻皆為 SAMPLE / SYNTHETIC；不代表原始點協會曾作成決議、採購、簽約、付款或完成訓練。正式使用前須以有權限的真實來源逐項替換，並依協會有效核定程序審查。

## 來源與對應

- 官方需求來源：`DRIVE_OFFICIAL_EVIDENCE_TABLE.pdf` 第 3 頁；SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。
- Unique Blueprint：`inputs/BLUEPRINT_0045_AND_NEIGHBORS.jsonl`，來源 commit `2587613e597904ba0630aa8a48d3bd4c6c3d9c47`；來源檔 SHA-256 `f2aaf52a7bc78d975f854244dabb1faaf393c3e53758267895ff9cf3bd6d43fc`。
- 文件編號 0045、需求 I10-E01 與官方方框 047 是三個不同欄位，勿互換。
- 歷史 R04 候選 SHA-256 `aebdeeef7da6944c5bb092f6e23c7f0825357e6866006e32971b3c8d8c81b535` 僅作失敗差異與回歸證據；未作為正文或版型模板。

## 驗收資料

- `evidence/build_receipt_R01.json`：候選、來源、計算及狀態收據。
- `evidence/technical_static_QA_R01.json`：DOCX 封裝、資料筆數及數學重算結果。
- `evidence/visual_layout_review_R01.json`：12 頁渲染及逐頁版面檢視範圍。
- `evidence/render_R01_final/0045_R01.pdf` 與 `page-01.png` 至 `page-12.png`：Word 唯讀匯出後的 PDF 及 150 dpi 頁面影像。
- `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`：105 筆合成事實、責任角色、替換來源及印刷頁碼定位。
- `evidence/historical_R04_review_receipt.json` 與 `inputs/historical_candidate_disposition.md`：歷史版本隔離及失敗處置。
- `evidence/build_0045_r01.py`、`evidence/finalize_receipts_R01.py`：建置與驗收收據產生來源。

## 計算與案例界線

示範權重合計 100%；兩名合成評選者的逐項原始分數與平均值均保留。加權結果為 A 82.0、B 88.0、C 77.0。回饋 10/12 = 83.3%，平均 42/10 = 4.2/5。各數字皆可在正文重算，並已在技術收據記錄。門檻、價格級距、保留期間與角色權限皆為示範參數，不宣稱是現行協會制度或法律要求。

## 審查界線

版面視覺檢查：PASS（12 頁已逐頁檢視）。技術檢查：PASS（DOCX ZIP 完整、計算重算一致、105 筆合成替換資料）。OpenCode CLI v2 獨立語意審查：PARTIAL（精確 SHA 綁定於 review/opencode_v2_review_R01/EXECUTION_RECEIPT_R01.json）；未發現阻擋缺陷，但列出替換簿欄位及內部引用修復項。故此 DOCX 仍是候選，不得作為正式核定或真實採購紀錄。

R01 獨立語意審查已透過 OpenCode CLI v2 完成，裁定 PARTIAL；原始輸出、封包、執行收據及逐項結論見 `review/opencode_v2_review_R01/`。此裁定只屬於 R01 exact SHA，不升格為核准或 REAL。
