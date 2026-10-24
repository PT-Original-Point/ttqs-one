# 0092 R03 — 第三方感謝函索取稿與證據驗證登錄表

## 身分與來源

- DOCX 編號：0092；官方需求：I17D-E06；官方清單序號：099（不同編號不可互換）。
- 官方原文：「感謝函。」；官方佐證表第 6 頁。
- 唯一 Blueprint：`BLUEPRINT_CURRENT.jsonl` 第 92 列；登錄表 SHA-256 `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`；該列 SHA-256 `86a732b30ce881b43144da8217693570281b999801d41a1b53370bfdaa97a358`。
- 本次依據分支既有最新來源 commit `d9c900d724e52699a54c209cb4515b5870e8fb9f`；第 06 契約 Git blob `263aaca84891bba8dca087875804343c3670e921`。

## 候選與驗收

- 候選檔：[`candidate/0092_R03.docx`](candidate/0092_R03.docx)
- DOCX SHA-256：`ed577847dba59d29cd1da0d1d64372a21ed07d8aee164ff044c3870ff958391b`
- 候選狀態：`CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED`。技術與版面檢查通過；獨立語意審查為 **PASS with nonblocking observations**。這不構成協會正式接受、發布、核准或 TTQS 驗收。
- Word 原生輸出 PDF 共 18 頁；18 頁均已用 140 DPI 頁面影像完整檢視。Section 3.3 及第 12 節的孤立標題／表頭已修正。
- 獨立 OpenCode v2 CLI reviewer：`opencode/mimo-v2.6-flash-free`（native session metadata）；CLI 報告成本 0，但供應商帳務仍 `UNKNOWN`。審查限完整文字抽取與來源/Blueprint 比對；reviewer 未讀 DOCX 二進位或檢視頁圖、未重算 SHA，因此二進位身分與版面驗收分別由本機 SHA 與 Word render/目視收據支援。

## 真實資料界線

全篇為 `SAMPLE / SYNTHETIC`；27 筆示範事實尚未替換；沒有第三方原件、實際寄出、第三方回覆、真人核准或簽章。本件不得代製第三方感謝函。8/8=100% 僅是合成索取表欄位完整度，不是證據有效性或評核結果。

## 非阻擋觀察

- F003、F005、F010、F011、F012、F017 的 6 個 replacement-register 正文定位使用了可唯一辨識的近義標籤，非逐字欄位名稱；reviewer 判定可由所引段落中的示例值唯一對到，不是阻擋缺陷。
- §9.3 的空白調閱工作表供未來使用，正文已明確聲明空白不代表過去曾調閱或完成查核。
- R02/R03 修訂日期是候選文件內部版本記錄，未被宣稱為協會核准或正式發布。

## 主要證據

- [`evidence/0092_R03_build_receipt.json`](evidence/0092_R03_build_receipt.json)
- [`evidence/0092_R03_TECHNICAL_QA.json`](evidence/0092_R03_TECHNICAL_QA.json)
- [`evidence/0092_R03_VISUAL_QA.json`](evidence/0092_R03_VISUAL_QA.json)
- [`evidence/SYNTHETIC_REPLACEMENT_REGISTER_0092_R03.csv`](evidence/SYNTHETIC_REPLACEMENT_REGISTER_0092_R03.csv)
- [`evidence/render/0092_R03_Word.pdf`](evidence/render/0092_R03_Word.pdf) 及 `candidate_pages/page-01.png` 至 `page-18.png`
- [`review/opencode_0092_R03_review_response.md`](review/opencode_0092_R03_review_response.md)：完整 reviewer 回覆；同目錄 JSON 為原始 CLI stdout 與驗收收據。
- 原始 Antigravity 文字草稿留在受限本機施工目錄，SHA-256 `0ca9e2c6deb1223c16b36ca2d3c0fb9ad22928d013e6032688fd81f5f666d61a`，模型身分 `UNKNOWN`。原稿含聯絡資料欄位與 email-like 字串，且屬未整理模型輸出，因此不公開；最終候選僅保留空白聯絡欄位並禁止自行補造。
