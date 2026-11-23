# 0004《目標市場調查執行與樣本紀錄》來源封包 R02

狀態：`SOURCE_PREPARATION_CANDIDATE`。本封包供 0004 後續 Writer 使用；不是 DOCX、不是建置收據、不是獨立審查或正式接受。

## 1. 文件身分與範圍

- `doc_id=0004`；`requirement_id=I01-E02`；專案 157 項次 `002`。
- 現行檔名列：`0004__目標市場調查執行與樣本紀錄.docx`。
- 現行文類：`執行與樣本紀錄｜目標市場調查執行與樣本紀錄`。
- 本件職責：記錄一個調查批次如何界定接觸對象、實際（本示例為合成）邀請、同意、回收、有效性判定、排除／重複處理、覆核及交接；不承擔問卷題目設計或需求分析。
- 執行範圍限本 source-preparation stage。不得建立或修改 DOCX、0003、0005、共享 dashboard、GitHub、CURRENT 或其他目錄。

## 2. 「官方方框」與項次 002 的編號邊界

官方《TTQS查核佐證文件資料表－訓練機構版》第 1 頁，在計畫（Plan）／「訓練機構未來經營方向及目標之訂定」的常見參考佐證中，列有單一文字 `目標市場需求調查。`。官方 PDF 頁面未把這一項印成「002」；`002` 是專案 157 項清單 `03_157_CHECKBOX_BLUEPRINTS.md` 的項次。該項次要求實際問卷、完整樣本資料和分析報告，再由目前 142 deliverable crosswalk 拆為三件：0003 問卷、0004 執行與樣本紀錄、0005 需求分析報告。不可把專案項次 002 說成官方 PDF 的方框流水號。

## 3. 本機權威來源與精確雜湊

以下 SHA-256 為本次直接讀取本機位元組後重算；原始來源均只讀。

|來源|本機位置／定位|大小|SHA-256|用途|
|---|---|---:|---|---|
|官方查核佐證表|`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\INPUTS\R04\06_OFFICIAL_SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf`，p.1|303,044 bytes|`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`|官方文字及頁次|
|R04/SOURCES 官方副本|`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf`|303,044 bytes|`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`|與 R04 PDF 位元組相同|
|Drive readback 官方副本|`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\DRIVE_READBACKS\DRIVE_OFFICIAL_EVIDENCE_TABLE.pdf`|303,044 bytes|`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`|與 R04 PDF 位元組相同|
|目前 BLUEPRINT_CURRENT|`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl`|1,059,187 bytes|`406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`|本件目前唯一指定 row 的控制來源|
|0004 BLUEPRINT_CURRENT row|同上，`deliverable_id=0004`／`requirement_id=I01-E02`|7,215 bytes（raw JSON，不含行尾）|Canonical JSON SHA-256 `84989534340738464502b2629f05d90dadd944603dd5adde3ac5544ba24b39c5`；raw row SHA-256 `8d725484b7d1fa03c93ebf4a2cbcceb7a4c2757b22a26119afd8a7aaf9f7fb62`|逐欄位要求；原始 row 另存於 `source/BLUEPRINT_CURRENT_ROW_0004.jsonl`|
|129-to-142 crosswalk|`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv`，I01-E02 row|10,578 bytes|`1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`|核實分件 0003／0004／0005|
|來源對照表|`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\REQUIREMENT_SOURCE_RECONCILIATION.csv`，I01-E02 row 3|57,979 bytes|`ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9`|記錄官方 p.1 與 `PDF_TEXT_EXACT_PAGE_MATCH`|
|157 項次文件（專案規格，不是官方 PDF）|`E:\TTQS\_tmp_r12_readback_0122_20261026\docs\ttqs-quality-20261016\03_157_CHECKBOX_BLUEPRINTS.md`，line 11|37,247 bytes（Windows CRLF）|本機 SHA-256 `7732c40f25d0803f18836725d1634ebe72a156925444f3ea9915b6168cc1a70a`；CRLF 正規化後 Git blob SHA-1 `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`|確認項次 002 文句及其候選規格身分|

官方 PDF 三個本機副本 SHA 完全相同。`source/official_evidence_table_p1.png` 是由上列 R04 PDF 第 1 頁產生的只讀視覺定位副本；PDF 頁面與其來源 SHA 才是權威。渲染器曾回報缺少 Symbol／ArialUnicode 顯示字型；影像中文字仍可讀，文字精確比對以官方 PDF 和來源對照表為準。

## 4. 來源讀回與本件就緒判定

目前 BLUEPRINT_CURRENT 的 0004 row 指向 `I01-E02`、上述檔名及「執行與樣本紀錄」文類；官方要求文字是 `目標市場需求調查。`，官方來源頁為 1，row 的本機讀回狀態為 `PDF_TEXT_EXACT_PAGE_MATCH`。同一份 crosswalk row 明列 `0003 | 0004 | 0005` 及三個不同標題。其 Blueprint row 要求包含執行流程、樣本逐筆紀錄、邀請／回收／有效／排除流向、缺失／重複／更正處理、資料保管／覆核／交接，以及 `有效率=有效數/回收數` 的分母規則。

核對結果：`READY_SOURCE_PACKET`。官方需求、現行 row、分件順序和本件文類一致；沒有來源證據顯示 0004 應改成問卷或需求分析報告。這只表示來源包可供獨立讀回，不是 `READY_WRITER`、DOCX 品質 PASS 或正式接受。未提供可驗證的真實施測原始件；真實調查是否發生仍為 `UNKNOWN`，本包只規劃完整 SAMPLE/SYNTHETIC 示範。

## 5. 0003 的唯讀跨件資料界線

僅為保持示例鏈一致，讀取 0003 source-prep 的來源 packet、unique blueprint、register 與 manifest；未修改 0003，也未以 0003 DOCX 正文作模板。

- 0003 replacement register SHA-256：`646a5dff8a540d53033d1cf161a6d4839bbf9928d0ae4fece6b6a256764604e1`；該 register 以 `SYN-001` 記錄樣本日期 `2026-10-28`，以 `SYN-002` 記錄匿名合成回覆碼 `SYN-0003-001`。
- 0003 的 source packet SHA-256：`c41d67261de8806bcabd20d8354b8163ae3409cb5d64fff05b0c8448052164ca`；unique blueprint SHA-256：`2733e5f8aec6951f9e475a2d12d854e8f6950d3fb6eef85b29c8dfbb12ae0dbf`。
- 0003 R17 candidate evidence manifest SHA-256：`f1f7fd578b3b12cfe6c533b171655e92f098f965d7d6ce0fd7bf98f514d1b981`。其記錄的狀態是當時快照，不代表現況接受；任何 R08 技術或模型自評也不代表獨立接受。0004 只引用回覆碼與日期，question item/scale/答案留在 0003；0004 Writer 開工前必須再讀 0003 register 並比對上述 SHA，若變更，僅更新 0004 的引用與本 register，不改 0003。
- 0003 current R17 candidate DOCX SHA-256：`206dce1d471ea5cdda2a6af15d65cc0c59c7909e55d8fe4475e0ad0b05507281`；independent semantic review receipt SHA-256：`ce6e86c338e0c24d6bd9ff9f97f74e4e94f85ae3c398c9445cbea0e167ba383d`；原始回覆 SHA-256：`1810ed0c6c8d45a59b84a8a30935e83c4c4bbe1b059d42ff3090d209959d6f16`。候選語意審查 PASS 不等於 REAL 施測或 Human 正式接受；該 DOCX 狀態仍為 CANDIDATE。

## 6. 0004 與相鄰文件的硬邊界

- **0003 問卷**：擁有題目文字、選項、量尺、跳答與完整單筆示範答卷。0004 只記錄問卷的執行與樣本流向；不重印 Q1–Q13 或再創一套量尺。
- **0004 本件**：擁有抽樣框／資格、執行步驟、邀請與同意、回收／有效判斷、缺漏／拒答／重複／撤回、紀錄追溯與資料交接。只計算流程品質率，不分析需求主題。
- **0005 需求分析報告**：擁有逐題有效分母、需求排序／彙整、差距解讀、限制與後續決策。0004 不出平均分數、需求排名、代表性／因果／開課結論。
- 不以舊 0004/0005 Word、歷史統計或失敗正文作為本件正文模板；只依官方來源與現行 0004 row 建立專屬表格。

## 7. SAMPLE/SYNTHETIC 算例摘要（完整逐事實清冊見 CSV）

示例限定為虛構批次：篩選 5 個虛構接觸代碼，其中 1 個不符合假設資格，4 個送出合成邀請；4 個邀請結果為 2 份唯一回覆、1 次明確拒絕、1 次截至截止日無回覆。唯一回覆中 1 份有效（只連結 0003 的 `SYN-0003-001`），1 份不完整／無效；另有 1 筆重複收件事件，僅作去重紀錄，不算新增人或唯一回覆。所有日期、代碼、角色、狀態、數字、判定及衍生率均在 register plan 逐列登錄。

- 篩選流向：`5 = 1 不合資格 + 4 合資格並邀請`。
- 邀請流向：`4 = 2 唯一回覆 + 1 拒絕 + 1 無回覆`。
- 唯一回覆：`2 = 1 有效 + 1 不完整／無效`。
- 收件事件：`3 = 2 唯一回覆 + 1 重複副本`。
- 回覆率：唯一回覆／合資格邀請=`2/4=50.0%`。
- 有效率（Blueprint 指定口徑）：有效唯一回覆／唯一回覆=`1/2=50.0%`。
- 有效樣本產出率（額外流程指標）：有效唯一回覆／合資格邀請=`1/4=25.0%`。
- 資格通過率（額外流程指標）：合資格邀請／已篩選接觸=`4/5=80.0%`。
- 百分比以未四捨五入的原始比值計算後取小數一位。分母為 0 時寫 `N/A` 並註明原因，不得填 0% 或補造分母。重複副本不進唯一回覆、有率計算或 0005 樣本數。

這些數字只示範流程可重算性，絕非協會實際接觸、回收、樣本數或需求成果。真實紀錄、角色、日期、抽樣框、同意、退件和政策一律 `UNKNOWN`，需取得原始紀錄後逐項替換。沒有真實原件時保留 SAMPLE 標記，不能把此例寫成 REAL。
