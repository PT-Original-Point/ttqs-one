# DOCX 0085｜I17C-E04｜官方方框 091｜來源包 R02

狀態：`SOURCE PACKET / BLUEPRINT INPUT`。本檔是 `UNIQUE_BLUEPRINT_0085_R02.md` 的施工輸入，不是協會政策、不是正式表單、不是已執行的社群討論紀錄、不是正式接受佐證。所有示範值一律 `SAMPLE / SYNTHETIC`；真實資料 `REAL=UNKNOWN/HOLD`；正式接受 `FORMAL_ACCEPTANCE=NOT_GRANTED`；執行狀態 `NOT_EXECUTED`。

## 1. 身分鎖（機器可讀）

```yaml
DOCX_NO: "0085"
ITEM_REQ: "I17C-E04"
CHECKBOX_NO: "091"
SERIES: "I17c 行為評估（多獨立作品，不合併）"
GENRE_PRIMARY: "知識管理社群：討論主題、互動與學習應用分析"
UPSTREAM_PAGE: "官方《TTQS 查核佐證文件資料表—訓練機構版》印刷第 6 頁 17c 行為評估"
NEIGHBOR_PREV: "0084 / I17C-E03 / 090"
NEIGHBOR_NEXT: "0086 / I17C-E05 / 092"
SERIES_SIBLINGS: "0082 / I17C-E01 / 088; 0083 / I17C-E02 / 089"
STATUS: "SOURCE PACKET / NOT_EXECUTED"
REAL: "UNKNOWN/HOLD"
FORMAL_ACCEPTANCE: "NOT_GRANTED"
```

- 文類：知識管理社群的**討論主題選擇、互動（含相異意見）記錄、共享／整編知識產出、實務應用與後續追蹤**之紀錄與分析工具。
- **編號混淆禁制**：DOCX `0085` 不等於官方方框 `085`（方框 085 為 I17b「課程評量及建議檢討」，依 0079 R02 修正對應 DOCX 0080），也不等於方框 `091` 所暗示的「文件 0091」；亦不得與相鄰的文件編號 `0084`（方框 090）、`0086`（方框 092）互換。文件號與方框號是兩套序列，不得互相替代。
- 對應出處：`UNIQUE_BLUEPRINT_0079_R02.md` 末段「R02 對照修正」明載「DOCX 0085 與 0086 實際對應 I17C-E04 與 I17C-E05」（本次已重讀原文核對，見 S6）。

## 2. 正式來源與位元組識別（本機逐一重算）

| # | 來源 | 位置 | Git blob | SHA-256 | 本件使用範圍 | 重算狀態 |
|---|---|---|---|---|---|---|
| S1 | Human Mission | `quality-review/0077_R01/inputs/upstream_snapshots/01_HUMAN_MISSION_AND_ACCEPTANCE.md` | `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` | `07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8` | 志工／社群性質組織的適切性、不得假造人員／執行／批准、完整可用示範、SAMPLE/REAL 界線 | `MATCH` |
| S2 | 文類寫作手冊 | `quality-review/0077_R01/inputs/upstream_snapshots/02_GENRE_WRITING_MANUAL.md` | `4ff863d9f534b6359fc1c7c1685bd8cce02da886` | `7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa` | 17c 五項成品分工（含知識社群討論記錄與分析）、行為量尺需前後比較與觀測來源、不得偽稱外部評核 | `MATCH` |
| S3 | 157 方框藍圖 | `quality-review/0077_R01/inputs/upstream_snapshots/03_157_CHECKBOX_BLUEPRINTS.md` | `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` | `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216` | section `I17c` **row 091** 標題與四要素（特定來源定位、核心正文/示範、決策或結果、跨文件事實連結；不得以空白欄位交差） | `MATCH` |
| S4 | 官方佐證資料表 PDF | `quality-review/0077_R01/inputs/upstream_snapshots/official_evidence_table_source.pdf` | `9c7621decdad585b743bf2b3d949ee5518b7bee0` | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` | 印刷第 6 頁 17c 行為評估之機構級評分說明與參考佐證清單 | `MATCH` |
| S5 | 同頁可讀影像 | `quality-review/0078_R01/evidence/official_evidence_table_page6-6.png` | `7cce2401a3230cb86875df79396538d0adea41d5` | `b7bd4c09b7d7e22993a1577647e10a421fb240222b46b531ba3f01ee047fa1d1` | 目視核對 PDF 印刷第 6 頁（本次已開啟檢視） | `MATCH` |
| S6 | 0079 藍圖（身分修正） | `quality-review/0079_R01/inputs/UNIQUE_BLUEPRINT_0079_R02.md` | `32143214c740bb41fb40a6b6a330089902840229` | `02ae81cb147d82f3a940be9e1747b483264aa0f9dcb15ffbd19e8a1611faa7b6` | **僅使用**其鄰件身分修正：DOCX 0085/0086 = I17C-E04/E05；其餘內容不引用 | `MATCH` |
| S7 | 0082 藍圖 | `quality-review/0082_R01/inputs/UNIQUE_BLUEPRINT_0082_R02.md` | `3679bfa41ef88ca1792234049f49f0127a923ed5` | `451acd1e197b916f2d14c03bd2651653892a4a7955119291e9628bdc5e27e602` | 0082=I17C-E01/088 之文類與邊界；N/O 與 0 之分離原則、自陳與因果界線 | `MATCH` |
| S8 | 0083 藍圖 | `quality-review/0083_R01/inputs/UNIQUE_BLUEPRINT_0083_R03.md` | `85e362aea519c3899a5145588e0aeb462897cc9e` | `21f76376621c5dd22d002a62202f41ea7335bbf872a965b0bbf8fb86955d0178` | 0083=I17C-E02/089 之文類與邊界；決策表、清冊 schema 與不變錨點 | `MATCH` |
| S9 | 0083 候選正文 | `quality-review/0083_R01/candidate/0083_R07_body.md` | `67aa18f5aee06a905e895f397653214c49ffccb8` | `4f150eb598cea245971f606deb8238a24d191517fb8b06b88545fa45414b9dd0` | 合成案例 `SYN-0083-B01` 不變錨點、17c 五作品表中「知識社群＝另件」的既有表述 | `MATCH` |
| S10 | 0084 來源包 | `quality-review/0084_R01/inputs/SOURCE_PACKET_0084_R01.md` | `40fa6f848342ae72a432b352f56f354d739d449d` | `6c2e928a889f0e01fe6aeca2ed0ed5b6a0dca6b3a12f591ba493a969dd4d3f1d` | 相鄰件 0084=I17C-E03/090 之身分、17c 機構級 0–3 界線 | `MATCH` |
| S11 | 0084 藍圖 | `quality-review/0084_R01/inputs/UNIQUE_BLUEPRINT_0084_R03.md` | `2bead32209a52adb9377b487fc373d5bbda135d0` | `49ac3786cdac0547bdab636663a280b5ef015e2b956ee2fefb157d674b66ed7e` | 0084 之邊界、角色碼、59 列清冊規格；「知識社群＝SEPARATE」 | `MATCH` |
| S12 | 0084 抽取正文 | `quality-review/0084_R01/evidence/docx_extracted_R11.md` | `4e86521b7188daf36eb75ebf392855b7eb413ab4` | `329dadf269064ddaecfcb0a731bb1d720a6eda6b56445a5ee3d8b558887ae848` | 已建置 0084 之 17c 五作品表、數學與狀態不變錨點（僅供一致性核對，非本件正文範本、非 REAL 證據） | `MATCH` |

路徑前綴一律為 `docs/ttqs-quality-20261016/`。重算方式：PowerShell `Get-FileHash -Algorithm SHA256` 與 `git hash-object`，於本機逐一執行；上表 12 項雜湊與 blob 與派發指示所列值**完全一致**。

## 3. 來源衝突檢查

1. **12/12 MATCH**：未發現 SHA-256 或 Git blob 不符，故本件不觸發來源層 `HOLD`。
2. **身分映射**：S6 原文已重讀，確認 DOCX 0085 = I17C-E04、DOCX 0086 = I17C-E05，與派發指示一致。方框 091 屬 section `I17c`（S3 line 225），標題「知識管理社群：討論主題、互動與學習應用分析」。
3. **次要映射來源缺件（HOLD，不推測）**：S7 §2.1 引用之需求清冊 `送審資料/05_填表建議_方法示範不等於實績/142份文件逐項檢查與填表建議.csv`（稱第 17、18 列）在本 checkout 中**不存在**（已以全庫 `*142*` 與 `送審資料` 目錄搜尋確認）。該 CSV 的逐列內容本次**未取得**，故凡依賴該 CSV 的細節一律標 `HOLD`，不臆測；本件身分映射改以 S6 為依據。
4. **分支與 HEAD**：派發時分支 `work/ttqs-one-document-quality-contract-20261016`；本機驗證 `git rev-parse HEAD` = `717f08733d4cda7d84af21db346e44f41f7854fb`（僅為觀測值）。分支會推進，**任何提案內容都不得寫死此 HEAD**。
5. **S9/S12 內容層**：S9 全文未提及 0085／I17C-E04／091；S12 全文亦未提及 0085／091，僅有「知識社群討論分析＝17c 其他獨立作品、各自獨立、不合併、SEPARATE」。此為**一致**（相鄰件把本件當獨立作品），不構成衝突。

## 4. 官方內容（可直接使用）

1. S3 section `I17c` **row 091**：「知識管理社群：討論主題、互動與學習應用分析」。四要素要求：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外**不得只交空白欄位**。
2. S4／S5（印刷第 6 頁，17c 行為評估）參考佐證清單逐字包含：「學員訓後動態調查表。」「參訓學員的學習成果實施行動計畫表追蹤紀錄。」「派訓單位主管對參訓學員的學習成效評估表。」「**知識管理社群討論。**」「神秘客實地稽核（外部稽核）課後機制等。」「其他：」。
3. 同頁 17c 之**機構級**評分說明：0 分未執行；1 分協助客戶執行課後行動計畫評估；2 分有機制並能展現辦理或追蹤客戶執行之相關紀錄；3 分相關紀錄能展現具體成效。**這是機構層評核語言**：不得填入社群成員或個人欄位，不得宣稱本會已得任何分數或等級；本件只提供文件層內容之對照（`UNSCORED`）。
4. S2 對 17c 的分工敘述：知識社群討論記錄與分析是 17c 的**獨立成品之一**，與結訓動態問卷、行動計畫追蹤、派訓主管量規、神秘客／外部稽核並列，不得互相代填。

## 5. 17c／17d 與相鄰文件界線

| 文件 | 要求／方框 | 文類 | 與本件關係 |
|---|---|---|---|
| 0082 | I17C-E01／088 | 學員訓後動態（行為轉移）問卷 | 同系列、**不同成品**；僅系列層連結，題項、資料、分母一律不共用 |
| 0083 | I17C-E02／089 | 學員行動計畫追蹤紀錄 | 同系列、**不同成品**；案例 `SYN-0083-B01` 與本件**無事實連結** |
| 0084 | I17C-E03／090 | 派訓主管職場觀察量規與回饋 | 同系列、**不同成品**；本件不得出現主管觀察級別或回饋對話 |
| **0085（本件）** | **I17C-E04／091** | **知識管理社群討論主題、互動與學習應用分析** | 本件 |
| 0086 | I17C-E05／092 | 神秘客實地稽核（外部稽核）方法與邊界 | 同系列、**不同成品**；本件不得出現外部稽核方法或第三方稽核原件宣稱 |
| 17d | 成果評估 | 就業／考照／品質／營運成果 | 另件；本件不得宣稱組織成果或訓練因果 |

## 6. 可引用的合成錨點（僅 SAMPLE；多數為**明確非連結**）

- 本件**不沿用** `SYN-0083-B01`／`SYN-0084-B01`／`LRN-B01`／`SYN-COURSE-0083-B`，也**不沿用** `SYN-0073-2026-A01`／`BTR-nn`。本件另立完全獨立合成案例 `SYN-0085-C01`（社群群體碼 `KM-G01`、參與者碼 `KM-P1`～`KM-P9`），並在正文寫明非連結。
- **可引用（僅作爲不變錨點的「不得矛盾」清單）**：0083 結訓日 `2026-03-06`、T1/T2/T3 `2026-04-03`／`2026-05-01`／`2026-05-29`、累計 83.3%、狀態 `PARTIAL`、`AID-01` 提供日 `2026-04-13`、`AID-02` 仍 `REQUESTED`；0084 O0–O3 `2026-03-05`／`2026-04-13`／`2026-05-01`／`2026-05-29`、級別 1/1/1/N-O 等。本件**不得改寫、不得引用為本件證據、不得換算**。
- 本件案例日期區間設為 `2026-06-15`～`2026-08-03`，晚於上述錨點，**不宣稱與其同一事件、同一課程或同一人**。
- 任何第三方原件（平台紀錄、成員名冊、會議簽到、外部回函）一律 `UNKNOWN/PENDING_REAL_SOURCE`，不偽造。

## 7. Blueprint / Writer 必須交付

1. `UNIQUE_BLUEPRINT_0085_R02.md`：身分鎖、來源矩陣與衝突檢查、文類目的與排除項、W1–W7 工作流、逐節大綱與逐欄位字典、空白可列印表單、完整合成案例（含相異意見與未決問題）、數學與口徑規則、決策與退件條件、隱私與記錄更正控制、跨文件一致性與負面測試、逐原子替換清冊與完整度測試、驗收矩陣。
2. 必須同時有**空白可列印表單**與**已完整填寫的合成示例**；只有空白表單即不合格。
3. 官方機構級 0–3 只能作 `UNSCORED` 對照，不得成為任何個人／社群評分欄。
4. 所有門檻、期限、角色、流程與示例結果標 `PROPOSED SAMPLE ONLY`；無效數據一律 `UNKNOWN/HOLD`，不得寫學習成效或因果。
5. **本來源包產製階段的歷史範圍**：當時不建置 DOCX、不修改其他檔案、不 commit／push／publish、不執行 Word／Computer Use、不呼叫其他模型。此限制隨來源包階段結案而解除；後續 DOCX Writer 依 `UNIQUE_BLUEPRINT_0085_R02.md` 與獨立 Writer 任務施工，不得把本句解讀為禁止建置 DOCX。

## 8. 狀態詞彙（沿用系列慣例）

`SAMPLE/SYNTHETIC`｜`PROPOSED SAMPLE ONLY`｜`NOT_EXECUTED`｜`HOLD`｜`RETURN`｜`REJECT`｜`REVERIFY`｜`NO_OPPORTUNITY`｜`REAL=UNKNOWN/HOLD`｜`FORMAL_ACCEPTANCE=NOT_GRANTED`｜`PENDING`（未定期限或未定位原件）。
