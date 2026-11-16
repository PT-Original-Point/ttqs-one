# 0023 / I04-E02 來源包（R01）

- work_id：`TTQS_ONE_0023_I04-E02_SOURCE_PREP_R01_20261116`
- 範圍：只準備官方來源第 2 頁、I04-E02 對應列及 0023 專屬 Blueprint；不含正文、DOCX、合成事實或模型派工。
- PR #92 branch live ref observation：`c139d76caa033868376b2427d31f69c6166eeb46`，觀測時間 `2026-11-16T13:40:01+08:00`（即時 refs/heads 觀測；不是本機 canonical source hash，也不表示 PR 已有新提交）。
- 官方要求：**不同訓練課程的設計與規劃方向。**
- 官方來源：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf`，PDF 第 2 頁；PDF 文字抽取 exact match PASS，視覺檢查未執行。抽取器 `pypdf 6.21.4`；頁面文字見 `inputs/official_source_page2_extracted.txt`。

## 唯一映射

- Crosswalk 唯一列：`I04-E02 → 0023`，deliverable_count=`1`、split_extra_count=`0`；標題：`不同訓練課程的設計與規劃方向_制度文件`。
- 專屬文類：`策略／計畫文件｜不同訓練課程的設計與規劃方向_制度文件`；檔名：`0023__不同訓練課程的設計與規劃方向_制度文件.docx`；role=`strategy_plan`。
- 官方來源 reconciliation：指標 4、PDF p.2、`PDF_TEXT_EXACT_PAGE_MATCH`；`visually_checked_pages` 空白，因此只記錄為未視覺核驗。
- Blueprint 負向近鄰（保留原列）：
  - 0022 / I04-E01：訓練需求定期調查與分析。
  - 0024 / I04-E03：訓練提供方式及選擇指標。

## 真實資料界線

本次授權來源集合未提供可核實的 REAL 課程、核准、日期、人員、實際數字、附件或簽核原件；這些一律記為 `UNKNOWN`，不推論其在其他未授權位置不存在。沒有合格 REAL packet 時，下一階段才可走 `READY_SYNTHETIC_FACTS_AND_EXAMPLE`，並明確採 `SAMPLE/SYNTHETIC`；本次未建立合成事實、未派 Writer。

## 輸入完整性

| 輸入 | 本機 canonical SHA-256 | 位元組 |
|---|---|---:|
| 官方 PDF master | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` | 303044 |
| Crosswalk master | `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679` | 10578 |
| Blueprint master | `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e` | 1059187 |
| Reconciliation master | `ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9` | 57979 |

本機 master SHA 是來源位元組雜湊，與上方 live GitHub ref observation 分開；本次未修改 shared controls 或 GitHub。逐列 SHA/位元組與所有輸出 SHA/位元組記錄於 `SOURCE_PREP_RECEIPT_R01.json`。
