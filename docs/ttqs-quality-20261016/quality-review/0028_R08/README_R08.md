# TTQS ONE 0028 R08 候選交付

狀態：CANDIDATE_SAMPLE_SYNTHETIC；正式接受 NOT CLAIMED。doc_id 0028 對應具名需求 I05-E02。此候選在本地已有完整技術、全頁視覺與 W1 獨立語意 PASS，但仍需 GitHub 同 ref 位元組讀回；本封裝保留必要來源與收據。

## 候選與品質

DOCX SHA-256：1EB4E9D26F761B57885AF7DC304BB76324AD85C7513FC858C82AF199D5273F70（62,613 bytes）。
DOCX 確定性 QA：PASS，11 pt 正文、9.5 pt 表格。
Word 原生 PDF：21 頁；PDF SHA-256 3EC2455B1F0C5A8357987D6200F19DE1793D64AA913792AEF18CB204D9E53CB5。
全頁視覺：21/21 頁 PASS；無空白頁、裁切或重疊。聯絡頁與 PDF 保存在 render/。
W1 OpenCode v2 獨立語意審查：PASS，0 findings，固定上述候選 SHA。要求路由為 opencode/nemotron-3.5-lightning-free；實際供應模型 UNKNOWN。程序 PID 14464、session ses_e13123512ffeJ5gWsYAbKX4J3r；程序已不在 OS 清單，launcher exit code UNKNOWN，回覆及終態已回收。

最初 R08 deterministic QA 的 ID regex 將 91 筆合成 ID 誤計為 81，判為 QA_PARSER_PATTERN_DEFECT；同一候選 SHA 的修正 regex recheck PASS，原失敗收據與 superseded_by 關係一併保存。未因此修改 DOCX 或重跑語意審查。

## 來源及真實性界線

來源包、官方來源 PDF、crosswalk、專屬 Blueprint 與 Blueprint row 均隨包保存，且在 manifest 列出原始位元組 SHA-256。DOCX 內容維持 SAMPLE/SYNTHETIC；機構真實資料未提供處標記 UNKNOWN，不冒稱核准、正式數據或第三方證據。此候選不代表正式接受或 REAL 升格。