# DOCX 0104｜I18-E11｜R16

- 狀態：`CANDIDATE`；尚未正式接受、簽核或送審。
- 官方方框：112；官方要求：證照獲取率（crosswalk 與來源摘錄收於 `source/`）。
- DOCX SHA-256：`9a074b207e7a57f1448cf96868f3cc3f30a72834a021f9b04392909ea3183d7b`。
- OpenCode bounded patch writer：DeepSeek V4.1 Flash Free（原生 session 欄位）；回覆為 JSON 修補方案，並非 DOCX。Windows 本機腳本將修補整合進 R16 手稿並建置 Word。原生服務端實際模型／計費來源未能獨立證實；本機 session cost 欄位為 0。
- 技術 QA：`PASS`，候選 SHA 相同；ZIP/XML/Word 可開啟、124 筆合成替換列、分母/比例/交叉表一致性與字級等檢查通過。
- Word 匯出及視覺：36 頁，所有頁面已直接目視；`PASS_WITH_NONBLOCKING_WHITESPACE_OBSERVATIONS`。第 7、13、25、36 頁有非阻擋留白觀察，未記錄裁切或重疊。
- 獨立語意：OpenCode MiMo V2.6 Flash Free 原生 session 回覆 `PASS`，0 blocking、3 nonblocking。範圍為 `TEXT_ONLY`：reviewer 依 R16 packet 回覆，沒有直接開啟 DOCX、重算其二進位 SHA、看頁面或做真人可用性測試。reviewer 在回覆中明確表示 SHA 是 packet 綁定值，並未自行重算；本機另對 DOCX 實際計算上述 SHA。詳見原始輸入、原始回覆及原生 session receipt。
- 非阻擋語意事項：T-13／T-16 的 D-1…D-3 標籤重複；T-17 引用未印出的 T-03 表號但仍附第 3 節定位；T-7 的兩個 N/A 儲存格標示格式不一致。審查認定不影響數字、分母或結論。
- 真實證據界線：正文、個案、組別、日期及門檻均為 `SAMPLE/SYNTHETIC`；沒有實際協會成績、證照、核准或第三方原件。
- `technical_qa_receipt_..._initial_expected_121.json` 是中間檢查器仍預期 121 列的歷史結果；最終 124 列檢查器收據才是 R16 技術判定。保留此檔以呈現檢核修正過程。
- `visual/0104_R16/` 收錄 Word 匯出的 PDF 及全部 36 頁 PNG；`evidence/artifact_manifest_R16.json` 綁定本包檔案 SHA-256。

- Writer patch-plan lineage：原生回覆有 19 項 bounded patch；`writer_patch_plan_lineage_R16.json` 檢查 19 項內容對最終手稿的涵蓋並列出差異。以原生 patch 順序重放不會逐字還原最終手稿；部分最終文字增補/調整沒有獨立 application receipt，因此 Writer→最終手稿的施工來源追溯為 `PARTIAL_PROVENANCE`。這不改變已固定的 DOCX SHA 與 TEXT_ONLY reviewer verdict。
