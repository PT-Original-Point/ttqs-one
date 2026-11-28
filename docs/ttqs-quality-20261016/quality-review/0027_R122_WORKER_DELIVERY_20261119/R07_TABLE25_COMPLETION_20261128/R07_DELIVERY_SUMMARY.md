# 0027 / I05-E01 — R07 表25完整清冊候選

狀態：**CANDIDATE**；非正式接受，REAL 仍為 UNKNOWN/HOLD。

- 候選 DOCX SHA-256：`f070b4f00ac7e1f57c2206edc62b39612fe6de49578ba0b90f0a89288aafa248`（86,183 bytes）。
- 修補範圍：只把原側附 113 筆正式替換清冊中缺少的 11 筆補入表25；舊 102 筆逐列保留。113 筆六欄逐格與同 SHA 側附 CSV 一致；沒有變更示範事實或數值，DOCX 只改 `word/document.xml`。
- 品質：既有靜態閘 PASS；Microsoft Word 原生輸出 40 頁 PDF（SHA-256 `357abf27cf9f6b3c5981fd44a09ad93357db5bb771b9ae1b86d04543224050c5`）；Dot 對同一 SHA 作限定獨立語意／全頁視覺 PASS。詳細收據與 40 頁圖像在 `qa/`。
- Dot exact approval：`qa/DOT_EXACT_ACCEPTANCE.json`，僅授權此候選以 SAMPLE/CANDIDATE 交付；Human 正式接受未授權。
- 原遠端 R02 候選保留於既有路徑；此 R07 使用新目錄，不覆寫歷史位元組。
