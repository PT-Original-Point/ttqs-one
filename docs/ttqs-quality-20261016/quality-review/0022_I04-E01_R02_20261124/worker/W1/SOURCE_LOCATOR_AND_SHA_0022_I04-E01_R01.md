# 0022 / I04-E01 Writer 來源定位與 SHA 收據

- work_id：`TTQS_ONE_0022_I04-E01_WRITER_R01_20261116`
- 文件：訓練需求的定期調查與分析_分析報告
- 輸出性質：候選正文 Markdown + SAMPLE/SYNTHETIC 替換清冊 + 交叉核算；不是 DOCX、不是 CURRENT、未經獨立語意審查或正式接受。

## 唯一使用的來源

| 輸入 | 定位 | SHA-256 |
|---|---|---|
| 官方需求 PDF | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf`，第 2 頁，「計畫（Plan）」指標 4 | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` |
| 官方 PDF 頁面文字讀回 | `...\0022_I04-E01\inputs\official_source_page2_extracted.txt` | `3c295e8861ad7775a78583e9111df61ac8733a7cf40d771f942363f00572de9c` |
| 本件來源包 | `SOURCE_PACKET_0022_I04-E01_R01.md` | `c188ef3dd4316c9cd88e01476477f2c0bbda0f5a2f695bc6a8b40e759e64b18d` |
| 本件唯一 Blueprint | `UNIQUE_BLUEPRINT_0022_I04-E01_R01.md` | `d39d890ed05b922990729f65541990eaf3b0a8ca69a9aeb89040d67fa6c83f99` |

官方具名要求原文：**「訓練需求的定期調查與分析。」** 來源包記錄已以 PDF 第 2 頁文字抽取比對；未記錄頁面視覺檢查，本收據不宣稱視覺驗證。

## 映射與專屬文類

- 129-row crosswalk master SHA-256：`1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`
- `I04-E01` 唯一列 SHA-256：`96078050897b628f4bd5d1bc3471a03902295ba431a28a8fb411b9a07960b467`
- 142-row Blueprint master SHA-256：`406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`
- `0022 / I04-E01` 唯一 Blueprint row SHA-256：`9b8c1beecbcfe92344b28230649671fa2fd23f73672347e16a94d1a00534aac2`
- 唯一文類：分析／評估報告；輸出涵蓋年度調查方法、母體/普查/回覆處理、問卷、指標字典、結果/分母/計算、分群限制、需求歸類與排序、年度決策、責任/期限/門檻、追蹤 SOP、限制及 REAL 原件替換清單。
- 負向近鄰：`0021 / I03-E04` 學員訓練與職務相稱證明；`0023 / I04-E02` 訓練課程設計與規劃。均未代寫或替代。

## SAMPLE/SYNTHETIC 邊界與未知

- 所有調查期間、母體/回覆數、選項比例、能力分數、風險/急迫評分、排序、計畫時數/席次、門檻、期限及角色代碼均標為 SAMPLE/SYNTHETIC，並由替換清冊 SF-001 至 SF-112 登錄。
- 20 份回覆均視為有效分析回覆是本示例明確假設（SF-112）；不聲稱已查證真實有效卷數為 20，也不把無效卷數推定為 0。
- REAL 調查期程、母體、問卷原件、回覆資料、核定目標、會議/核准、出席與訓練成果均依來源包標 `UNKNOWN`；不得以本例替代。
- 不使用舊 0022 DOCX、peer body/table 或其他文件內容作範本；不產生/變更 DOCX、shared facts、CURRENT 或 GitHub。
