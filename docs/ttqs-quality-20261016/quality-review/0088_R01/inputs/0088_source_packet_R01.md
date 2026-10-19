# 0088 來源核對包 R01

**狀態：候選來源包，供新稿撰寫與後續獨立驗收**  
**核對日：2026-10-20（台灣時間）**  
**專案：TTQS_ONE**  
**文件編號：0088**  
**需求編號：I17D-E02**  
**文件名稱：就業及考照追蹤紀錄**

## 1. 本件唯一官方要求

官方《TTQS 查核佐證文件資料表－訓練機構版》第 6 頁，在「17d 成果評估」的方框中列有：

> 就業及考照追蹤紀錄。

來源 PDF 的 SHA-256 為 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。本機正式來源副本與 `quality-review/0064_R06/official_source.pdf` 的原始位元組 SHA 相同。第 6 頁 PNG 由該 PDF 第 6 頁直接轉出並已目視核對；畫面同列相鄰要求「訓後調查表。」及「品質不良率下降統計表。」。

這三個方框不可互換：0087/I17D-E01 是訓後調查表；本件 0088/I17D-E02 是個別學員就業與考照追蹤紀錄；0089/I17D-E03 是品質不良率下降統計表。

## 2. 文件身分與來源對照

| 欄位 | 核對值 | 證據與限制 |
|---|---|---|
| 專案 | TTQS_ONE | 本專案現行候選分支 |
| 儲存庫／分支 | `PT-Original-Point/ttqs-one` / `work/ttqs-one-document-quality-contract-20261016` | PR #92 現行 head `2ec98c24876dd96c4df0cc14767bfe3df08092fd`，本機 fetch 後一致 |
| 文件編號 | `0088` | R04 142-ID crosswalk 與來源 reconciliation |
| Unique requirement | `I17D-E02` | R04 需求來源核對表 |
| 官方 checkbox 文字 | `就業及考照追蹤紀錄。` | 官方來源 PDF 第 6 頁；逐字保留 |
| 官方頁次 | 第 6 頁 | PDF 第 6 頁已直接目視核對 |
| 官方 157 項流水號 | `UNKNOWN / 尚未由具流水號欄位的權威登錄核實` | 現行 142-ID crosswalk、來源 reconciliation 與舊 Blueprint 列均未提供可信流水號；不可依檔名或相鄰文件推算 |
| 文件用途 | 就業及考照追蹤紀錄 | 對應官方方框；使用者需要逐案追蹤、判斷證據狀態、安排後續處理 |
| 正式／真實狀態 | `CANDIDATE / SAMPLE-SYNTHETIC ONLY` | 尚無可供本包核實的協會真實個案原件；不得標成協會實績 |

## 3. 核對來源及雜湊

| 來源 | SHA-256 | 使用方式 |
|---|---|---|
| 官方查核佐證表 PDF | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` | 只用來辨認第 6 頁原文及鄰項 |
| R04 `REQUIREMENT_SOURCE_RECONCILIATION.csv` | `ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9` | I17D-E02 列確認 page 6、原文及 deliverable ID 0088；此為 R04 runtime source map |
| R04 `TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv` | `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679` | I17D-E02 對應一份交付文件 0088 |
| R04 `BLUEPRINT_CURRENT.jsonl`（歷史需求拆解列） | `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e` | 只作需求拆解及歷史狀態核對；正文不得沿用 |
| R04 `BASELINE_142_DOCX_INVENTORY_READBACK.csv` | `5eef25c42fd3473136149a91db21c5164c021afc73ff6602d1488511031fd7f5` | 確認舊 0088 位元組及歷史缺陷，不作新稿模板 |
| PR #92 現行 Mission | blob `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` | SAMPLE/REAL、禁止偽造、候選狀態及品質驗收規則 |
| PR #92 現行寫作手冊 | blob `4ff863d9f534b6359fc1c7c1685bd8cce02da886` | 依文件文類設計專屬完整內容及操作要求 |
| PR #92 現行 157 checkbox 契約 | blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` | 要求精確綁定 doc_id、requirement、checkbox 及 Unique Blueprint |

`BASELINE_142_DOCX_INVENTORY_READBACK.csv` 的舊 0088 文件 SHA-256 為 `fb0d15f7039e6256bc6a9c737f414fccba51139b68be8748fb3c066321709c35`；baseline 記錄其狀態為 `VALID_DRAFT_WAITING_ORIGINAL`、來源為 `OFFICIAL_REQUIREMENT_ONLY_NO_REQUIREMENT_SPECIFIC_HISTORICAL_SOURCE_LOCATED`、可讀性為 `FAIL_REPAIR`、正文最小字級不足且有治理雜訊，並明確規定 `HISTORICAL_INVENTORY_ONLY_BODY_REUSE_PROHIBITED_BY_R04`。本次新稿不複製該正文、表格或段落。

## 4. 真實證據界線

本次沒有收到協會真實學員名冊、訓練紀錄、追蹤同意、就業證明、考照成績或證書原件。因此新候選只可提供完整 `SAMPLE / SYNTHETIC` 操作案例及可直接替換的空白表單。不得宣稱原始點協會已辦訓、已追蹤、已取得就業成果、已通過考照或已核准任何程序。

姓名、日期、案件數、分母、聯絡狀態、結果、角色代碼、抽查值及所有計算均須登錄逐事實替換清冊。任何需要第三方證明的案例都只能展示取得及驗證步驟；不得製作、仿造或引用不存在的證書、雇主證明、簽名或正式核准。

## 5. 開工前狀態

- PR #92 live head 與本機 branch head：`2ec98c24876dd96c4df0cc14767bfe3df08092fd`。
- PR #92 遠端目前沒有 `quality-review/0088_R01` 候選包。
- 0088 舊 DOCX 是歷史輸入，正文禁止重用。
- Windows 觀察到的 `opencode-cli.exe` 僅為 `serve --service`；未見 0088 Writer 命令。未見 Antigravity 執行程序。
- 本件可以依官方原文、doc_id、requirement ID 與已核對需求拆解建立 SAMPLE 候選；numeric checkbox serial 保持 UNKNOWN，待找到有權威來源的流水號欄位再補入控制收據，不得猜測。
- 0088 R01 的 Builder、獨立 reviewer、技術檢查與視覺檢查結果均尚未發生；建立來源包不等於 DOCX 通過或正式接受。
