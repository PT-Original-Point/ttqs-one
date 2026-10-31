# 0113 / I18-E22｜來源準備狀態 R01

- 階段：`SOURCE_PREP_R01`；本次 deterministic technical QA：`PASS_SOURCE_PREP_TECHNICAL`。
- 官方來源：PDF p.7，指標 18 的 4 分參考例「會員人數逐年增加。」；官方印刷 checkbox 序號未由本來源證實，維持 `UNKNOWN_NOT_ASSERTED`。
- 唯一 Blueprint 綁定 0113／I18-E22；157 清單 position 123 僅為專案索引，不冒充 doc_id 或官方序號。
- SAMPLE 案例 `SYN-0113-CASE-01`：2022–2025 期末數 42、46、51、57；逐期對帳式 42+8−4=46、46+9−4=51、51+10−4=57；同比 +9.5%、+10.9%、+11.8%；總變動 +15／+35.7%。
- 真實名冊／會員定義／授權來源均未提供；清冊保持 `SYNTHETIC_ONLY; REAL UNKNOWN/HOLD`。
- 本收據只驗證來源綁定、合成資料算式、唯一事實 ID、替換清冊及必要 HOLD/REJECT 區隔；不代表 DOCX 已建置、Word 可用、語意／視覺驗收或正式接受。

## SHA-256

- `source/SOURCE_PACKET_0113_I18-E22_R01.md`：`5596e508240bc7995fb69181433756da11e9a0af02923620fc5490f49ea4a99b`（2517 bytes）
- `source/UNIQUE_BLUEPRINT_0113_I18-E22_R01.md`：`15871b0ace40420c33b4a883c3f0f6dd2f2afa685fa47a1b36d3f66ca514c334`（5733 bytes）
- `source/SYNTHETIC_DATASET_0113_R01.csv`：`6fe0928cc6100eae0ed6245f6866668e230276d51c8451a0a6197d90a3990d1f`（659 bytes）
- `evidence/SYNTHETIC_REPLACEMENT_REGISTER_0113_R01.csv`：`d25abbc9de8e941f3e7a35b7e6da197e7c49c4dc51dd51157a83e1c2ecbe03fd`（2336 bytes）
- `evidence/source_manifest_0113_R01.json`：`150c713310ed1c148d0ce28c0a943c95d84b9de39a003bc2c245c1a7f8f26352`（3134 bytes）
- `source/official_source_training_institution.pdf`：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`（303044 bytes）
- `source/official_source_page7.png`：`0479eecd5ea3c2092ae19e0d4ad7c8f44aa20e525d36938f4957e727e3edbaab`（400415 bytes）
- `source/official_source_text_extraction.txt`：`47f4f8aafd086906f52a5653ad8a0429656ddd2f0ec6cce9aaadab2b110623db`（20802 bytes）
- `evidence/technical_qa_source_blueprint_R01.json`：`86c4475467949efe5dadc2ea6ef4fec70164a372a5b1dd9133a7c9acb72b76c5`
