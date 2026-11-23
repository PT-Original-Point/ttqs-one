# TTQS ONE｜0030 I06-E01 R05 交付摘要

- **候選狀態：** CANDIDATE；不是 REAL 或正式接受。
- **官方要求：** I06-E01「工作經驗的相關受訓證明。」（官方佐證表第 2 頁）。
- **實際材料增量：** W1 OpenCode 免費路線回傳 2 段補充，合計 517 個 Han 字；R05 正文 5,319 個 Han 字，落在官方工作包設定的 5,000–7,000 範圍。舊 R04 的 4,802 字低於下限，不列為完成版本。
- **候選 DOCX SHA-256：** `e2531031233f137e4d222aca2da753c735a81314b77a2ab432cf176c89b11a27`
- **正文 SHA-256：** `1cfe4f99a0f985b2bfa1f1cd8eccb7d789b959e21395122d247ed65434261448`
- **确定性 QA：** R05 exact-SHA PASS；Word 可讀、12 表、合成鍵 SYN-0030-001～015 齊全，與 R04 基底未變的表格已核對。
- **獨立語意審查：** W1 OpenCode v2 fresh plan context，要求模型 `opencode/iceman-free`，實際服務模型 UNKNOWN；exit 0，PASS、無 findings。審查綁定上述候選及正文 SHA；限制是未直接語意閱讀 DOCX 二進位，也未做視覺審查。
- **全頁視覺：** Word COM 唯讀輸出 PDF 12 頁，再以 Poppler 144 dpi 產生 12 張 raster。逐頁檢查 PASS；無裁切、重疊或空白頁。第 12 頁替換清冊尾端兩列未重複欄標題，前頁已有標題，列內容完整可讀，記為低影響觀察。
- **來源：** 官方 PDF SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；來源頁、Blueprint、合成事實各以 sidecar 記錄。Blueprint row canonical JSON SHA 與 packet manifest 相符；crosswalk row manifest hash 的序列化基礎仍 UNKNOWN，未與抽取檔案 SHA 混用。
- **REAL 限制：** 真實任職／職務說明及其他第三方原件未提供；R05 明確保留 SAMPLE/SYNTHETIC、UNKNOWN 與不得升格標示。
- **GitHub 原始位元組讀回：** PASS。2026-11-19T16:18:01.357+08:00 從 origin/work/ttqs-one-document-quality-contract-20261016 的 HEAD 77a625364bdd12949e948cdc0e021094f1a89c30 直接讀回 docs/ttqs-quality-20261016/quality-review/0030_I06-E01_R05_20261117/candidate/0030_I06-E01_R05.docx；檔案 SHA-256 e2531031233f137e4d222aca2da753c735a81314b77a2ab432cf176c89b11a27、53,843 bytes。確定性、12 頁全頁視覺及 W1 獨立語意收據均綁定同一候選 SHA；本件仍為 CANDIDATE，未宣稱正式接受。詳見 delivery/GITHUB_RAW_READBACK_R05.json。
