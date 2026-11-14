# 0006 / I01-E03 — R17 候選與品質證據

狀態：CANDIDATE；不是協會正式核准，也不是 REAL 成果。

- 候選：`candidate/0006_I01-E03_R17.docx`
- 候選 SHA-256：`7d40b9e4ddc85a1fbbc246212db3cdab5196b136fc63016540eac6fec6e53aef`
- 官方需求：I01-E03「業務發展計畫（包括人力資源的發展與訓練規劃內容、主題或方向）。」
- 唯一 Blueprint：`source/BLUEPRINT_CURRENT_ROW_0006.jsonl`；完整工作包與來源雜湊見 `source/SOURCE_PACKET.json`。
- 官方 PDF：`source/official_TTQS_evidence_table.pdf`。
- 合成替換清冊：`inputs/SYNTHETIC_REPLACEMENT_REGISTER_0006_R17.csv`，含 177 筆 SAMPLE/SYNTHETIC 事實。

## 本次版本差異與驗收

R17 僅修正七個合成事實的位置索引，並將兩處版本標記由 R16 改為 R17；沒有改動正文、策略、數字或計算。建置收據見 `qa/BUILD_RECEIPT_R17_REGISTER_POINTER_REPAIR.json`。

- 技術：PASS；21 張表、177 筆合成事實、公式重算與字級門檻通過。見 `qa/TECHNICAL_QA_R17_STATIC.json`。
- Word 視覺：PASS；Word 16.0 輸出 47 頁 PDF。11 張 R17 變動頁直接目視，36 頁頁面影像與 R16 位元相同。PDF 及 11 張直接檢視頁均附於 `qa/`。
- 語意：PASS_DELTA_SCOPE；R17 僅就七個索引及兩處版本標記做 exact-SHA 差異審查；其他語意範圍承接 R16 的審查收據。這不是 R17 全文重新審查，也不是正式接受。
- REAL／核准：未主張；真實資料仍須由協會提供與核實。

R17 產物由本機確定性索引修復及 Codex QA 組成；這次 R17 不是 W1 或 W2 成功撰稿的成果。`ARTIFACT_MANIFEST.json` 列出本資料夾每個檔案的 SHA-256。

## 原始位元組保護
本資料夾的 .gitattributes 停用文字換行轉換，避免 JSON／CSV／Markdown 收據在 Git 傳輸時被改寫；遠端 readback 逐檔比對原始 SHA-256。

