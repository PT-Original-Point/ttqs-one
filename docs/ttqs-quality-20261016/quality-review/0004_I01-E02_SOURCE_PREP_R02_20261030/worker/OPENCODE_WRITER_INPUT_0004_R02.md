# TTQS ONE bounded writer input bundle
This is an input package only. It is not a candidate document. Use only the source-bound information below.

--- BEGIN SOURCE_PACKET_0004_I01-E02_R02.md | SHA256=4535ac0b8275297ff60dabd7b4f7ada77bd8bd240b7200a6532ea32eec9aad0b ---
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

--- END SOURCE_PACKET_0004_I01-E02_R02.md ---

--- BEGIN UNIQUE_BLUEPRINT_0004_I01-E02_R02.md | SHA256=cdfaff45068df2c71bb582908c970ad67cd1a8a7ab973a8efd747cce66c4e375 ---
# 0004《目標市場調查執行與樣本紀錄》Unique Blueprint R02

狀態：`CANDIDATE_SOURCE_PREPARATION`；只供 0004 source stage。不得建置 DOCX 或將本稿標成審查 PASS。

## A. 綁定來源

- `doc_id=0004`；`requirement_id=I01-E02`；專案 157 項次 `002`；官方查核佐證表 p.1。
- 官方 PDF 原文：`目標市場需求調查。`；此官方方框是整體要求，項次 002 來自專案 157 項清單。官方 PDF、BLUEPRINT_CURRENT row、crosswalk 和 row-level SHA 請依同資料夾 `SOURCE_PACKET_0004_I01-E02_R02.md` 核對。
- 唯一交付責任：完整、可抽查的執行及樣本紀錄。正文須有一筆可追溯的 SAMPLE/SYNTHETIC worked example，所有合成事實逐筆登錄。

## B. 0004 的可辨識功能

遮掉標題和檔名後，仍須看得出這是「調查執行／樣本流向紀錄」：有時間順序的篩選、邀請、同意、回覆收件、有效性判定、排除與覆核；讀者能由唯一代碼追到匿名回覆、原始件定位、判定理由和下一步。不得只有市場調查概述或一組彙總統計。

## C. 專屬正文順序與功能

1. **首頁操作卡**：用途、使用時點、責任角色、輸入／輸出、目前 `SAMPLE/SYNTHETIC` 與 `CANDIDATE` 狀態；明示沒有真實施測證明。
2. **範圍、母體與抽樣框**：目標對象定義、納入／排除條件、抽樣框來源、涵蓋期間、去重識別碼、抽樣方法與限制。真實來源未取得時，只用虛構代碼示範並標 `SAMPLE`；不得宣稱有會員名冊或具代表性。
3. **執行計畫／流程控制**：步驟、輸入、負責角色、時間欄、控制點、輸出、例外分支；至少涵蓋資格不符、拒絕、未回覆、部分回覆、重複回覆、撤回及更正。
4. **聯絡／邀請紀錄**：每筆匿名對象代碼、資格、邀請日期／管道、送達狀態、同意狀態、期限及證據定位。示範值不得填真實姓名、電話、電子郵件、地址或追蹤識別資訊。
5. **樣本及回收紀錄**：每筆收件代碼、匿名回覆碼、日期、完整度、有效／無效狀態、排除理由、重複關聯、更正版本、覆核者及原件索引；有效列與無效列分開呈現。
6. **流向對帳**：篩選數、排除數、合資格邀請、唯一回覆、拒絕、無回覆、無效唯一回覆、有效唯一回覆、原始重複收件事件；顯示原始整數與對帳等式。
7. **流程指標**：回覆率、Blueprint 指定有效率、有效樣本產出率及資格通過率；每一列寫清分子、分母、期間、唯一計數口徑、N/A 規則及逐步算式。
8. **資料品質／隱私**：缺漏與更正歷程、拒答與撤回處理、匿名化、最小存取、保存／刪除政策來源。無已核實政策時寫 `UNKNOWN`，不得自行指定保存年限。
9. **覆核及交接**：操作者與覆核者角色分離、異常處理、回收封存及 0005 接收欄；交接有效匿名回覆碼、分母與限制，不把需求分析寫入本件。
10. **替換及附件索引**：列出真實化所需的原始名冊／抽樣框、邀請紀錄、同意、原始匿名回覆、去重／更正軌跡、覆核和保存依據；逐項對照 replacement register。

## D. 專屬表格

- `執行階段—輸入—操作角色—操作—控制點—輸出—異常路徑`。
- `匿名接觸代碼—資格—邀請—同意—收件狀態—期限—證據定位`。
- `匿名回覆碼—原始收件—完整度—有效判定—排除理由—重複／更正關係—覆核`。
- `批次流向對帳`：每個數字同時顯示唯一值／事件值、包含與排除規則、分母。
- `官方要求—0004紀錄欄位—來源—覆核—預期輸出`。
- `樣本事實—SAMPLE ID—正文定位—真實替換原件—覆核責任`。

## E. 唯一 SAMPLE/SYNTHETIC 批次與核算口徑

本 Blueprint 使用 source packet 所列虛構批次；本地 register 對每一日期、代碼、狀態、數量、排除決定與衍生結果都有獨立 ID。批次構成：5 筆虛構接觸篩選、1 筆資格不符、4 筆合資格邀請；其中 2 筆唯一回覆（1 有效、1 不完整／無效）、1 筆拒絕、1 筆無回覆；另有 1 個重複收件副本，不增加唯一回覆數。

公式與對帳：

- `篩選數 = 不合資格 + 合資格邀請 = 1 + 4 = 5`。
- `合資格邀請 = 唯一回覆 + 拒絕 + 無回覆 = 2 + 1 + 1 = 4`。
- `唯一回覆 = 有效 + 無效 = 1 + 1 = 2`。
- `原始收件事件 = 唯一回覆 + 重複副本 = 2 + 1 = 3`。
- `回覆率 = 唯一回覆 / 合資格邀請 = 2/4 = 50.0%`。
- `有效率 = 有效唯一回覆 / 唯一回覆 = 1/2 = 50.0%`。
- `有效樣本產出率 = 有效唯一回覆 / 合資格邀請 = 1/4 = 25.0%`。
- `資格通過率 = 合資格邀請 / 篩選數 = 4/5 = 80.0%`。

重複副本先去重，再計算唯一回覆及有效率；不得把重複副本視為另一位受訪者。拒絕及無回覆不屬回收數；不完整唯一回覆屬回收但無效。比例以原始分子分母計算後四捨五入至一位小數；分母為零則 `N/A` 加原因，不回填 0%。不計算各題平均、需求排名、母體推估、顯著性、因果、開課或組織績效。

唯一有效列只引用 0003 的合成回覆碼 `SYN-0003-001`；不複製 0003 的題目、選項或回答。該 ID 必須在 Writer 開工前以本 Blueprint 登錄的 0003 register SHA 重新讀回；SHA 改變即更新 0004 的交叉引用及本 register，不能改寫 0003。

## F. 0003／0004／0005 負向近鄰拒絕

- **0003《目標市場需求調查問卷》**：題目、選項、量尺、跳答、個別答案屬 0003。0004 只存問卷版本識別及匿名回覆索引；看見問卷題目／逐題需求答案時，不複製進 0004。
- **0005《目標市場需求分析報告》**：題目層級分母、主題排序、描述統計、需求差距、解讀與決策屬 0005。0004 只提供執行數、唯一回覆數、有效性、去重／排除軌跡及有效匿名代碼；不解讀市場需求。
- **0001《中長程業務發展策略地圖》、0006《業務發展計畫與人力資源訓練規劃》**也不是本件。
- 任一段落可不改字直接移入 0003 問卷或 0005 分析報告，即表示 0004 文類辨識失敗。

## G. SAMPLE／REAL 替換與隱私規則

每個 SAMPLE 數值以 register ID 對應頁／表／欄位。升 REAL 時依序取得有權限的原始抽樣框、資格判定依據、邀請／送達紀錄、同意／拒絕／撤回、匿名原始回覆、提交時間、重複檢查、缺漏／更正與覆核記錄；逐列替換代碼、日期、狀態、分母及公式結果並保留來源定位和核對人。不能用合成值補真實缺件，也不能把 SAMPLE 與 REAL 放在同一分母混算。

不收或輸出真實姓名、身分證號、電話、電子郵件、地址、IP、敏感健康／財務資料。匿名代碼不得反向識別真人；重複僅用依法核准的匿名提交碼判定。保存期限、外部授權及真實抽樣代表性若無來源，一律 `UNKNOWN`。

## H. 下游接受條件（供新鮮獨立 reviewer，非本次自評）

1. 來源 PDF／Blueprint row／crosswalk 的精確 ID、文字、頁次和 SHA 一致。
2. 標題盲讀可辨識為執行與樣本紀錄；不與 0003 或 0005 混文類。
3. 一筆有效、一筆無效、拒絕、無回覆及重複副本均有可追溯欄位、理由與 SAMPLE 標示。
4. 所有篩選／邀請／回收／有效／排除總數能逐項對帳；有效率、分母零、去重規則可重算。
5. 每一個合成日期、代碼、角色、狀態、數量、比率、結果與決定都在 register 有唯一 ID 及替換原件規則。
6. 未取得 REAL 原件時不宣稱實際施測、協會核准或市場需求成果；無空白模板或待填欄代替示例。
7. 若後續建 DOCX，正文至少 10.5 pt、表格至少 9.5 pt，並由不同於 Writer 的 fresh reviewer 綁定 exact DOCX SHA；本次沒有建 DOCX，亦未作此接受。
--- END UNIQUE_BLUEPRINT_0004_I01-E02_R02.md ---

--- BEGIN SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R02.csv | SHA256=0e0748a80d512c9e49abea3c567838239db21510408570d84f0ecfdb7e10d0c9 ---
fact_id,scope,field,synthetic_value,value_type,planned_location,source_basis,real_replacement_source,real_replacement_rule,verification_rule,status
SYN-0004-CYCLE-01,batch,cycle_id,SYN-0004-CYCLE-01,synthetic batch code,首頁／批次識別,0004 local sample plan,Actual approved survey batch record and source index,Replace the full code with the verified batch identifier; retain old sample ID in history.,Match against original authorization and batch log.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-FRAME-01,batch,frame_description,Fictional volunteer-segment contact list; no actual roster is represented.,synthetic description,抽樣框與限制,0003 blueprint sample context; fictional only,Authorized real sampling-frame source and version/hash,"Replace only with the authorized, scope-limited frame; do not copy personal data into the DOCX.","Verify scope, source owner, extract date, deduplication rule, and authorization.",SAMPLE_SYNTHETIC_ONLY
SYN-0004-DATE-OPEN,batch,open_date,2026-10-28,synthetic date,批次摘要,Aligned to 0003 sample date SYN-001; not actual fieldwork,Time-stamped approved survey schedule and original event log,Replace from original source date; do not infer from file modified time.,Date falls within authorized survey window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-DATE-CLOSE,batch,close_date,2026-10-29,synthetic date,批次摘要／未回覆判定,Fictional one-day close after sample opening,Approved schedule and close/export log,Replace from the actual close timestamp and time zone.,Confirm close is not earlier than open and responses are classified against it.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-CHANNEL-01,batch,invitation_channel,Simulated online form invitation; no link was sent.,synthetic channel,執行流程／邀請紀錄,Fictional scenario only; no external side effect,Authorized dispatch log and privacy approval,"Replace with actual channel and delivery evidence; never fabricate an email, QR, or dispatch receipt.",Match channel totals to verified send/receipt logs.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-ROLE-OPS-01,batch,operator_role_code,SYN-OPS-01,synthetic role code,執行紀錄／操作者,Fictional role; not a real person or assignment,Authorized staff/volunteer duty roster and assignment record,Replace with authorized role/person reference under access controls; omit names from public copy unless approved.,Check responsibility and separation from reviewer.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-ROLE-REV-01,batch,reviewer_role_code,SYN-REV-01,synthetic role code,覆核欄,Fictional role; not a real person or approval,Authorized reviewer assignment and dated review record,Replace only from actual assignment and review evidence; do not infer approval.,Verify reviewer distinct from operator when required.,SAMPLE_SYNTHETIC_ONLY
RULE-0004-ELIGIBILITY-01,control_rule,validity_rule,Eligible + consent recorded + within the approved window + required fields complete + one unique anonymous response.,proposed rule,有效判定說明,Operational rule proposed for the sample; confirm against approved instrument/protocol before REAL use.,Approved survey protocol and instrument version,Adopt only after authority confirms the exact required fields and eligibility criteria.,Independent checker traces each criterion to the approved protocol.,PROPOSED_RULE_NOT_REAL_POLICY
RULE-0004-DUPLICATE-01,control_rule,duplicate_rule,Same authorized anonymous submission code is one unique return; later copy is logged and excluded from unique counts.,proposed rule,重複與去重處理,No IP/address/device fingerprinting; sample-only rule.,Approved anonymized duplicate-control procedure and original submission tokens,Use only approved anonymous token; never infer identity or use IP.,Recompute unique and event counts from token-level receipt log.,PROPOSED_RULE_NOT_REAL_POLICY
RULE-0004-RETENTION-01,control_rule,retention_rule,No retention period specified in this source packet; leave REAL retention policy UNKNOWN.,unknown policy rule,資料保管／刪除,No duration is invented.,Association-approved retention and deletion policy,Insert only a verified policy citation and effective version; otherwise keep UNKNOWN.,"Verify policy owner, effective date, and scope.",UNKNOWN_REAL_SOURCE
SYN-0004-U001-ID,record,contact_code,SYN-0004-U001,synthetic anonymous code,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Authorized real sampling-frame record mapped to a non-identifying code,Replace with a scoped pseudonymous code; keep the re-identification key outside the DOCX.,Check uniqueness and ensure no direct identifier appears.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U001-SCREEN-DATE,record,screening_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Dated source-frame screening record,Replace from contemporaneous screening log; do not infer.,Compare date to batch window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U001-ELIGIBILITY,record,eligibility_decision,ELIGIBLE,synthetic decision,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Approved inclusion/exclusion evidence,Reapply approved criteria to source; record reason and checker.,Checker independently recomputes from cited criteria.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U001-INVITE-STATE,record,invitation_state,INVITED,synthetic process state,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original dispatch/attempt log,Replace from actual send/attempt receipt; no sending is claimed here.,Reconcile invited count to source log.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U001-INVITE-DATE,record,invitation_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Time-stamped invitation or contact log,Replace from actual timestamp and channel evidence.,Confirm event within approved window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U001-CONSENT,record,consent_state,CONSENT_YES,synthetic consent disposition,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Actual consent/decline/withdrawal source,Record consent only when explicit evidence exists; unknown stays UNKNOWN.,No response is never treated as consent.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U001-OUTCOME,record,response_outcome,UNIQUE_RETURN_COMPLETE_VALID,synthetic result,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original anonymous response receipt / refusal / close log,Replace from original item-level intake status and retain exclusion trail.,Reconcile with unique return and invitation flow.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U001-RETURN-DATE,record,return_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original submission timestamp and timezone,Replace from original receipt metadata; do not use file creation time.,Check within close window and link to anonymous receipt token.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U001-RESPONSE-REF,record,linked_response_code,SYN-0003-001,synthetic reference code,匿名接觸／樣本紀錄表 SYN-0004-U001,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,"0003 synthetic register SHA; for REAL, authorized anonymous raw response",Use exact current 0003 register reference or verified real anonymous token; do not copy questionnaire answers into 0004.,Check source SHA and ensure the linked record is unique.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-ID,record,contact_code,SYN-0004-U002,synthetic anonymous code,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Authorized real sampling-frame record mapped to a non-identifying code,Replace with a scoped pseudonymous code; keep the re-identification key outside the DOCX.,Check uniqueness and ensure no direct identifier appears.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-SCREEN-DATE,record,screening_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Dated source-frame screening record,Replace from contemporaneous screening log; do not infer.,Compare date to batch window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-ELIGIBILITY,record,eligibility_decision,ELIGIBLE,synthetic decision,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Approved inclusion/exclusion evidence,Reapply approved criteria to source; record reason and checker.,Checker independently recomputes from cited criteria.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-INVITE-STATE,record,invitation_state,INVITED,synthetic process state,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original dispatch/attempt log,Replace from actual send/attempt receipt; no sending is claimed here.,Reconcile invited count to source log.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-INVITE-DATE,record,invitation_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Time-stamped invitation or contact log,Replace from actual timestamp and channel evidence.,Confirm event within approved window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-CONSENT,record,consent_state,CONSENT_YES,synthetic consent disposition,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Actual consent/decline/withdrawal source,Record consent only when explicit evidence exists; unknown stays UNKNOWN.,No response is never treated as consent.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-OUTCOME,record,response_outcome,UNIQUE_RETURN_INCOMPLETE_INVALID,synthetic result,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original anonymous response receipt / refusal / close log,Replace from original item-level intake status and retain exclusion trail.,Reconcile with unique return and invitation flow.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-RETURN-DATE,record,return_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original submission timestamp and timezone,Replace from original receipt metadata; do not use file creation time.,Check within close window and link to anonymous receipt token.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-RESPONSE-REF,record,linked_response_code,NO_ANSWER_CONTENT_CARRIED,synthetic note,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,"0003 synthetic register SHA; for REAL, authorized anonymous raw response",Use exact current 0003 register reference or verified real anonymous token; do not copy questionnaire answers into 0004.,Check source SHA and ensure the linked record is unique.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U002-DISPOSITION-REASON,record,disposition_reason,REQUIRED_FIELD_MISSING,synthetic decision reason,匿名接觸／樣本紀錄表 SYN-0004-U002,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original screening / validation record and approved rule,Replace with evidence-backed reason; never guess why a person declined or failed.,Reason must match the recorded status and rule.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U003-ID,record,contact_code,SYN-0004-U003,synthetic anonymous code,匿名接觸／樣本紀錄表 SYN-0004-U003,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Authorized real sampling-frame record mapped to a non-identifying code,Replace with a scoped pseudonymous code; keep the re-identification key outside the DOCX.,Check uniqueness and ensure no direct identifier appears.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U003-SCREEN-DATE,record,screening_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U003,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Dated source-frame screening record,Replace from contemporaneous screening log; do not infer.,Compare date to batch window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U003-ELIGIBILITY,record,eligibility_decision,ELIGIBLE,synthetic decision,匿名接觸／樣本紀錄表 SYN-0004-U003,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Approved inclusion/exclusion evidence,Reapply approved criteria to source; record reason and checker.,Checker independently recomputes from cited criteria.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U003-INVITE-STATE,record,invitation_state,INVITED,synthetic process state,匿名接觸／樣本紀錄表 SYN-0004-U003,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original dispatch/attempt log,Replace from actual send/attempt receipt; no sending is claimed here.,Reconcile invited count to source log.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U003-INVITE-DATE,record,invitation_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U003,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Time-stamped invitation or contact log,Replace from actual timestamp and channel evidence.,Confirm event within approved window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U003-CONSENT,record,consent_state,DECLINED_BEFORE_SUBMISSION,synthetic consent disposition,匿名接觸／樣本紀錄表 SYN-0004-U003,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Actual consent/decline/withdrawal source,Record consent only when explicit evidence exists; unknown stays UNKNOWN.,No response is never treated as consent.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U003-OUTCOME,record,response_outcome,NO_RETURN,synthetic result,匿名接觸／樣本紀錄表 SYN-0004-U003,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original anonymous response receipt / refusal / close log,Replace from original item-level intake status and retain exclusion trail.,Reconcile with unique return and invitation flow.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U003-DISPOSITION-REASON,record,disposition_reason,EXPLICIT_REFUSAL,synthetic decision reason,匿名接觸／樣本紀錄表 SYN-0004-U003,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original screening / validation record and approved rule,Replace with evidence-backed reason; never guess why a person declined or failed.,Reason must match the recorded status and rule.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U004-ID,record,contact_code,SYN-0004-U004,synthetic anonymous code,匿名接觸／樣本紀錄表 SYN-0004-U004,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Authorized real sampling-frame record mapped to a non-identifying code,Replace with a scoped pseudonymous code; keep the re-identification key outside the DOCX.,Check uniqueness and ensure no direct identifier appears.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U004-SCREEN-DATE,record,screening_date,2026-10-29,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U004,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Dated source-frame screening record,Replace from contemporaneous screening log; do not infer.,Compare date to batch window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U004-ELIGIBILITY,record,eligibility_decision,ELIGIBLE,synthetic decision,匿名接觸／樣本紀錄表 SYN-0004-U004,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Approved inclusion/exclusion evidence,Reapply approved criteria to source; record reason and checker.,Checker independently recomputes from cited criteria.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U004-INVITE-STATE,record,invitation_state,INVITED,synthetic process state,匿名接觸／樣本紀錄表 SYN-0004-U004,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original dispatch/attempt log,Replace from actual send/attempt receipt; no sending is claimed here.,Reconcile invited count to source log.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U004-INVITE-DATE,record,invitation_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U004,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Time-stamped invitation or contact log,Replace from actual timestamp and channel evidence.,Confirm event within approved window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U004-CONSENT,record,consent_state,CONSENT_UNKNOWN_NO_RESPONSE,synthetic consent disposition,匿名接觸／樣本紀錄表 SYN-0004-U004,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Actual consent/decline/withdrawal source,Record consent only when explicit evidence exists; unknown stays UNKNOWN.,No response is never treated as consent.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U004-OUTCOME,record,response_outcome,NO_RETURN,synthetic result,匿名接觸／樣本紀錄表 SYN-0004-U004,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original anonymous response receipt / refusal / close log,Replace from original item-level intake status and retain exclusion trail.,Reconcile with unique return and invitation flow.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U004-DISPOSITION-REASON,record,disposition_reason,NO_RESPONSE_BY_CLOSE,synthetic decision reason,匿名接觸／樣本紀錄表 SYN-0004-U004,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original screening / validation record and approved rule,Replace with evidence-backed reason; never guess why a person declined or failed.,Reason must match the recorded status and rule.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U005-ID,record,contact_code,SYN-0004-U005,synthetic anonymous code,匿名接觸／樣本紀錄表 SYN-0004-U005,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Authorized real sampling-frame record mapped to a non-identifying code,Replace with a scoped pseudonymous code; keep the re-identification key outside the DOCX.,Check uniqueness and ensure no direct identifier appears.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U005-SCREEN-DATE,record,screening_date,2026-10-28,synthetic date,匿名接觸／樣本紀錄表 SYN-0004-U005,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Dated source-frame screening record,Replace from contemporaneous screening log; do not infer.,Compare date to batch window.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U005-ELIGIBILITY,record,eligibility_decision,INELIGIBLE,synthetic decision,匿名接觸／樣本紀錄表 SYN-0004-U005,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Approved inclusion/exclusion evidence,Reapply approved criteria to source; record reason and checker.,Checker independently recomputes from cited criteria.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U005-INVITE-STATE,record,invitation_state,NOT_INVITED,synthetic process state,匿名接觸／樣本紀錄表 SYN-0004-U005,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original dispatch/attempt log,Replace from actual send/attempt receipt; no sending is claimed here.,Reconcile invited count to source log.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U005-CONSENT,record,consent_state,NOT_APPLICABLE,synthetic consent disposition,匿名接觸／樣本紀錄表 SYN-0004-U005,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Actual consent/decline/withdrawal source,Record consent only when explicit evidence exists; unknown stays UNKNOWN.,No response is never treated as consent.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U005-OUTCOME,record,response_outcome,NO_RETURN,synthetic result,匿名接觸／樣本紀錄表 SYN-0004-U005,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original anonymous response receipt / refusal / close log,Replace from original item-level intake status and retain exclusion trail.,Reconcile with unique return and invitation flow.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-U005-DISPOSITION-REASON,record,disposition_reason,OUTSIDE_FICTIONAL_TARGET_SEGMENT,synthetic decision reason,匿名接觸／樣本紀錄表 SYN-0004-U005,All values below are SAMPLE/SYNTHETIC design values; no real survey is asserted.,Original screening / validation record and approved rule,Replace with evidence-backed reason; never guess why a person declined or failed.,Reason must match the recorded status and rule.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-DUP-01-ID,receipt_event,receipt_event_code,SYN-0004-DUP-01,synthetic receipt event code,重複收件紀錄,One extra fictional receipt event,Time-stamped receipt record,Replace with actual duplicate receipt event code while preserving the original receipt.,Must point to an existing unique anonymous token.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-DUP-01-DATE,receipt_event,receipt_date,2026-10-28,synthetic date,重複收件紀錄,Fictional event aligned to batch date,Original receipt timestamp and timezone,Replace from original receipt metadata.,Compare with original and close timestamps.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-DUP-01-LINK,receipt_event,duplicate_of,SYN-0003-001,synthetic link,重複收件紀錄,Same anonymous sample code; duplicate is not another person,Authorized duplicate-token comparison record,Replace with verified anonymous token relationship; do not derive identity.,Verify same token and retain both event IDs.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-DUP-01-DECISION,receipt_event,duplicate_decision,EXCLUDE_EXTRA_COPY_FROM_UNIQUE_COUNTS,synthetic decision,重複收件紀錄／對帳,Process-only decision,Approved deduplication rule and review log,Replace with evidence-backed decision; retain first/duplicate lineage.,Ensure duplicate adds one raw receipt event but zero unique respondents.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-SCREENED,aggregate,screened_contacts,5,count,批次流向對帳表,Five fictional contact codes U001-U005.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-INELIGIBLE,aggregate,ineligible_before_invite,1,count,批次流向對帳表,U005.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-ELIGIBLE_INVITES,aggregate,eligible_invitations_sent,4,count,批次流向對帳表,U001-U004; U005 was not invited.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-UNIQUE_RETURNS,aggregate,unique_returned_questionnaires,2,count,批次流向對帳表,U001 and U002; duplicate copy excluded.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-VALID_UNIQUE,aggregate,valid_unique_returns,1,count,批次流向對帳表,U001 only; linked to SYN-0003-001.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-INVALID_UNIQUE,aggregate,invalid_unique_returns,1,count,批次流向對帳表,U002 incomplete.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-REFUSALS,aggregate,explicit_refusals,1,count,批次流向對帳表,U003.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-NO_RESPONSE,aggregate,no_response_by_close,1,count,批次流向對帳表,U004.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-DUPLICATE_EXTRAS,aggregate,duplicate_extra_receipts,1,count,批次流向對帳表,One extra receipt linked to SYN-0003-001.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-COUNT-RAW_RECEIPT_EVENTS,aggregate,raw_receipt_events,3,count,批次流向對帳表,Two unique returns plus one duplicate copy.,"Verified original frame/export, intake log, refusal/close records, and duplicate ledger",Recount from verified row-level evidence; never overwrite with historical or synthetic totals.,Arithmetic and row-level IDs must reconcile.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-FLOW-SCREEN,derived,screening_flow,5 = 1 + 4,count identity,對帳／交接表,5 screened = 1 ineligible + 4 eligible invitations.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-FLOW-INVITE,derived,invitation_flow,4 = 2 + 1 + 1,count identity,對帳／交接表,4 invitations = 2 unique returns + 1 refusal + 1 no response.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-FLOW-VALID,derived,validity_flow,2 = 1 + 1,count identity,對帳／交接表,2 unique returns = 1 valid + 1 incomplete/invalid.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-FLOW-RECEIPT,derived,receipt_event_flow,3 = 2 + 1,count identity,對帳／交接表,3 raw receipt events = 2 unique returns + 1 duplicate extra.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-RATE-RESPONSE,derived,response_rate,2 / 4 = 50.0%,derived ratio,對帳／交接表,Unique returns / eligible invitations; duplicate extras excluded.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-RATE-EFFECTIVE,derived,effective_rate,1 / 2 = 50.0%,derived ratio,對帳／交接表,Valid unique returns / unique returned questionnaires; official Blueprint口徑.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-RATE-YIELD,derived,valid_yield,1 / 4 = 25.0%,derived ratio,對帳／交接表,Valid unique returns / eligible invitations.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-RATE-ELIGIBLE,derived,eligibility_pass_rate,4 / 5 = 80.0%,derived ratio,對帳／交接表,Eligible invitations / screened contacts.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-HANDOFF-N,derived,valid_sample_count_to_0005,1,count,對帳／交接表,Only valid unique sample; SAMPLE only.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-HANDOFF-ID,derived,valid_sample_id_to_0005,SYN-0003-001,synthetic code,對帳／交接表,Reference only; 0005 owns any item-level analysis.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
SYN-0004-LIMIT-N,derived,analysis_limit,n=1 synthetic response; no population inference,derived limitation,對帳／交接表,One synthetic valid response cannot support market inference.,Recompute only after source facts are replaced with verified real evidence,"Recalculate from current row-level evidence, retain formula and denominator, round percentage to one decimal.",Independent arithmetic recomputation; denominator zero => N/A with reason.,SAMPLE_SYNTHETIC_ONLY
UNK-0004-REAL-EXECUTION,real_input_status,actual_survey_occurrence,UNKNOWN,unknown; not a SAMPLE value,REAL replacement gate,No authoritative original included in this source packet.,Actual dated execution records and original returns,"Do not infer from a draft, schedule, or synthetic example.",Remain UNKNOWN until cited original is verified.,UNKNOWN_REAL_SOURCE
UNK-0004-REAL-FRAME,real_input_status,actual_sampling_frame,UNKNOWN,unknown; not a SAMPLE value,REAL replacement gate,No authoritative original included in this source packet.,Authorized sampling-frame original and eligibility criteria,"Verify owner, authorization, scope, date, and hash before use.",Remain UNKNOWN until cited original is verified.,UNKNOWN_REAL_SOURCE
UNK-0004-REAL-CONSENT,real_input_status,actual_consent_and_withdrawal,UNKNOWN,unknown; not a SAMPLE value,REAL replacement gate,No authoritative original included in this source packet.,Original consent/withdrawal evidence,No consent is inferred from response or silence.,Remain UNKNOWN until cited original is verified.,UNKNOWN_REAL_SOURCE
UNK-0004-REAL-ROLES,real_input_status,actual_operator_and_reviewer,UNKNOWN,unknown; not a SAMPLE value,REAL replacement gate,No authoritative original included in this source packet.,Authorized duty roster and assignment/review record,Use permitted role references; no invented names or approvals.,Remain UNKNOWN until cited original is verified.,UNKNOWN_REAL_SOURCE
UNK-0004-REAL-RETENTION,real_input_status,approved_retention_period,UNKNOWN,unknown; not a SAMPLE value,REAL replacement gate,No authoritative original included in this source packet.,Association-approved effective retention/deletion policy,Keep UNKNOWN until source is supplied; never invent a period.,Remain UNKNOWN until cited original is verified.,UNKNOWN_REAL_SOURCE
XREF-0003-SYN-001,shared_reference,source_sample_date,2026-10-28,shared SAMPLE reference,0004 valid sample row / cross-document source note,0003 source/SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv SHA-256 646a5dff8a540d53033d1cf161a6d4839bbf9928d0ae4fece6b6a256764604e1; existing fact_id SYN-001. Not independently accepted.,"Actual dated anonymous response source, if formally obtained","At 0004 Writer start, re-read exact 0003 register and confirm SYN-001; if it changes, update only this reference and derived 0004 dates.",The sample date must agree with the source register and the event timestamp; never infer from file timestamps.,SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE
XREF-0003-SYN-002,shared_reference,source_response_code,SYN-0003-001,shared SAMPLE reference code,0004 valid sample row / handoff-to-0005 ID,0003 source/SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv SHA-256 646a5dff8a540d53033d1cf161a6d4839bbf9928d0ae4fece6b6a256764604e1; existing fact_id SYN-002. Does not copy the questionnaire answers.,Actual authorized anonymous response token and verified 0003 register,"At 0004 Writer start, re-read exact 0003 register and confirm SYN-002; do not edit or replace 0003. For REAL, replace with an authorized anonymous code only.","Confirm exact source hash, unique token, sample-only status, and no direct identifier.",SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE

--- END SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R02.csv ---
