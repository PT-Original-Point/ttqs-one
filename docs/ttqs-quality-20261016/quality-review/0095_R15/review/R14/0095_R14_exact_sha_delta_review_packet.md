# DOCX 0095 R14 — bounded exact-SHA semantic and locator review

## Review identity and scope

- Internal document ID: `0095`; official requirement: `I18-E02`; official checkbox: `建立目標客戶及學員滿意度調查機制（系統及流程面）。`
- Current candidate DOCX SHA-256: `bde9a803c18137c98cf64992d75066b0722b5c3d3794eb7d6ab38667b88d0f19`. Same-edition Word PDF SHA-256: `6220a5641d6963badad457da99a05cb13e5c76d92088136e504da5bddb4a4918` (46 pages).
- Current register CSV SHA-256: `e1331efc3f5109bcc1502821bb132b71cce682ec08926741915b0e0c906ad5b6`; manifest SHA-256: `40bea6a4bec6d133a4a8ee80afb875e01f926075e6083817c69f897493680fc4`; 211 rows, 13 columns, 211 unique keys.
- Official source page 6 SHA-256: `e0ecd2d7b1fd8c20e03b9e651083ee767ccaf3c4a6297f9cb0e7709d07620f02`.
- Unique Blueprint SHA-256: `9a22b3acd4bdafb15f18c15ee89088f4fb5ee334bfef9a1917fcc5740b7979c2`.
- State is `CANDIDATE_ONLY`; this is not formal TTQS acceptance and asserts no REAL association survey, approval, signature, or execution.
- Review is limited to the R12→R13→R14 locator/version-boundary delta and closure of four R12 nonblocking observations. Do not re-review all unchanged survey content as though it changed; flag any material defect actually detected.

## Prior exact-SHA semantic evidence and limitations

R12 reviewer response SHA-256 `354ae95e47eea2d268001f2d11fec62384f38c607486aeb946425f75e519db6e` reviewed DOCX SHA-256 `f9f0ff551d5b670f868ea4614317646ea3d7ac738dd68b5879df5059ddcd56c6` and returned `PASS`, zero blocking, four nonblocking observations. Requested route was OpenCode v2.0.32 `opencode/mimo-v2.6-flash-free`; upstream provider identity was `UNKNOWN`. That reviewer explicitly did not open or rehash source files or inspect rendered pages.

R13 DOCX SHA-256 `173c8de96f45c470839e0fbfd42a0663dabc806f48163ab8e423a66122061c87` was not independently reviewed. Its final Word PDF showed pagination flow from p.22 onward different from R12, so it was superseded; no R13 semantic PASS is claimed. R14 retains the R13 register fact values and corrects the exact page maps against its own 46-page Word PDF.

## The four R12 observations and evidence for this review

1. `OB-R12-01` was a packet omission: the current manuscript explicitly distinguishes 0095/I18-E02 from 0094/I18-E01 and 0096/I18-E03 in §9.1–§9.4. The full source text is reproduced below.
2. `OB-R12-02`: the sensitivity check is part of §7.2 and appears on PDF p.33; the R14 visual receipt includes p.33 in its high-resolution scope. The §1.4 map now places §7.2 on pp.31–34.
3. `OB-R12-03`: §1.4 now maps the case-opening metadata to p.23; §7.2 / §7.3 transition and figure spans are mapped to actual R14 pages. Check the map against the supplied current PDF-bound visual/locator evidence.
4. `OB-R12-04`: the R14 current register is explicitly revision-labeled and has a distinct versioned filename/hash; R08/R11/R12/R13 registers are identified as historical.

## R14 §1.4 page map (full current table)

### 1.4 官方要求—候選結果—證據頁次—覆核追溯表

**官方來源：指標 18「訓練系統的一般性功能─目標客戶及學員的評價」；本交付件依 Unique Blueprint 指派對應 I18-E02 檢核框「建立目標客戶及學員滿意度調查機制（系統及流程面）」，不表示官方佐證表只有此一佐證項目。正式來源頁次為第 6 頁，逐字內容與 SHA-256 見 §1.2；評分級距另見 §1.3。**

| 官方指標 18／I18-E02 覆核面向 | 候選結果 | 文件證據定位（章節 → PDF頁次，逐項對應） | 覆核方式及證據界線 | 候選狀態 |
| :--- | :--- | :--- | :--- | :--- |
| **指標18／I18-E02：調查機制系統面** | 提出兩類對象的量表、資料字典、計算口徑、存取及版本控制建議。 | §2.1–§2.4 → PDF pp.5–6<br>§3.1–§3.2 → PDF pp.6–9<br>§4.1 → pp.10–13；§4.2 → pp.13–17；§4.3 → pp.17–19<br>§5.1 → pp.20–22；§5.2 → p.22 | 核對工具、欄位、分母及公式；均為候選設計，不證明已採用。 | PROPOSED |
| **指標18／I18-E02：端到端作業流程面** | 展開需求界定、對象篩選、告知、發放、回收、檢核、分群分析、審閱及追蹤。 | §2.1–§2.4 → PDF pp.5–6<br>§3.1 → p.6；§3.2 → pp.7–9<br>§8.1–§8.5 → pp.35–38 | 核對流程輸入、控制點、輸出及暫緩／退回條件；實際執行 UNKNOWN。 | PROPOSED |
| **指標18／I18-E02：目標客戶與學員分軌評價** | 提供 Tool-A、Tool-B、完整 SAMPLE／SYNTHETIC 明細及分群計算。 | §4.1 → pp.10–13；§4.2 → pp.13–17；§4.3 → pp.17–19<br>§6 opening / case metadata → PDF p.23<br>§6.1–§6.4 → pp.24–30<br>§7.1 → p.31；§7.2 → pp.31–34（附圖 A → pp.33–34） | 分別檢查兩種問卷、分母、均分與正向率；不得合併取代分群結果。 | SYNTHETIC |
| **指標18／I18-E02：結果判讀與持續改善** | 說明限制、證據強度、候選改善建議、責任欄位及後續核驗方式。 | §6.3.3 → PDF p.28；§6.4 → pp.29–30；§6.4.1 → p.30<br>§7.3–§7.4 → PDF p.34<br>§8 → PDF pp.35–38<br>§9.5 → PDF pp.39–42<br>§10 → PDF pp.42–46 | 核對合成值、限制與替換清冊；無真實核定、實施或效果證據。 | PROPOSED／SYNTHETIC |

頁次錨點說明：本表頁次以最終 R14 Word 匯出逐項核對；章節錨點為主要定位，PDF exact SHA 與視覺檢查範圍記於外部 QA 收據。若正文或版面再變更，必須重新核頁，不得沿用舊版頁碼。


## R14 §9.1–§9.4 neighbor distinction (full current text)

## 9. 相鄰文件與工作物差異

本節對照 I18-E02 與相鄰文件的官方文字及工作物差異，供確認本候選報告的專屬用途；不表示本件已獲 TTQS 評核通過。

### 9.1 四項相鄰文件之文類與職責對照表

| DOCX ID | 要求代碼 | 官方參考佐證文字 | 本報告與其界線 |
| :--- | :--- | :--- | :--- |
| 0093 | I17D-E07（內部索引；官方原頁未於本件核驗） | 未核驗的額外近鄰，不作本件官方需求引據。 | 僅作分件提醒；0095 不代替或複製其他文件內容。 |
| 0094 | I18-E01 | 口述目標客戶及學員認為訓練有其功能，僅有滿意度調查，但未有具體紀錄及評量。 | 口述紀錄與評量工具不同於本件系統及流程分析報告。 |
| 0095 | I18-E02 | 建立目標客戶及學員滿意度調查機制（系統及流程面）。 | 本件專屬於滿意度調查機制設計、流程、工具及分析口徑。 |
| 0096 | I18-E03 | 感謝函。 | 感謝函為另一獨立文件；其出具者及原件狀態須依實際來源核實，0095 不代製或取代。 |

以上區分只依正式要求文字及 Blueprint 的文件分工，不推定鄰近文件的真實內容、出具者或執行情況。

### 9.2 與 0093 I17D-E07 雇主調查表的差異

內部來源對照索引將 DOCX 0093／I17D-E07 列為相鄰工作物；本件未附其官方來源頁，故此處只作未核驗的額外分件提醒，不把該項文字當作正式需求證據。0095 則依 §1.2 所列 I18-E02 檢核框，提供候選系統設計與合成分析，兩者內容不互相替代。

### 9.3 與 0094 I18-E01 口述訪談紀錄的差異

I18-E01 對應的官方文字為口述目標客戶及學員認為訓練有其功能，但只有滿意度調查且缺少具體紀錄及評量。0095 則對應 I18-E02 的系統與流程機制。兩項各自成件；本報告不將訪談原話、訪談人或真實口述資料冒充為本件調查結果。

### 9.4 與 0096 I18-E03 感謝函的差異

I18-E03 的參考佐證文字為「感謝函」。其實際出具者、內容與原件狀態須由合法來源核實。0095 是候選機制分析報告，不得冒充、代製或填補 0096 的真實原件。


## R14 §9.5 REAL-source path/index (full current text)

### 9.5 升格真實（REAL）所需外部佐證路徑與索引清單

本索引逐項對應 Unique Blueprint `real_data_required` 之升格類別（正式日期；真實人名／角色；核准／簽章；真實班次／課程；實際數字／比例；真實附件與檔案位置），並就本件之實際需求細分為 8 個可核對項目。每列均載明所需真實來源、可對應之事實粒度清冊鍵，以及本次取得狀態；目前清冊鍵以 `qa/0095_R14_synthetic_replacement_register.csv` 為準；R08、R11、R12、R13 CSV／manifest 均保留為歷史原件，不作為本版頁碼依據（R07 版清冊 `qa/0095_R07_synthetic_replacement_register.csv` 為歷史標的，維持不變）。

| # | 升格核實項目（對應 Blueprint real_data_required 類別） | 需要的真實來源 | 對應清冊鍵 | 本次狀態 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 真實作者與覆核者姓名／角色（真實人名／角色） | 協會編製者與正式覆核者之具名紀錄、職稱及授權依據 | UNK-0095-UNK_AUTHOR_REVIEWER_IDENTITY（R07 新增）；PROP-0095-ROLE-CRD、PROP-0095-ROLE-COL、PROP-0095-ROLE-ANL、PROP-0095-ROLE-DEC 僅為候選職能標籤，非人名 | 未提供；UNKNOWN |
| 2 | 核准／簽章原件（核准／簽章） | 有權核准者之核定文件、簽章或會議決議原件及其生效依據 | UNK-0095-UNK_APPROVAL_SIGNATURE（R07 新增）；UNK-0095-UNK_REAL_SYSTEM | 未提供；UNKNOWN |
| 3 | 正式／生效日期（正式日期） | 制度或工具之核定發布日、生效日，以及真實問卷之施測與回收日期 | UNK-0095-UNK_FORMAL_EFFECTIVE_DATE（R07 新增；本版 REAL 日期欄位留白，Tool-A／Tool-B REAL 空白日期欄位見 R14 PDF pp.11、15；本索引第 3 列在 R14 最終 PDF p.39 核對）；SYN-0095-COURSE_DATE、SYN-0095-FOLLOWUP_DATE 為合成日期 | 未提供；UNKNOWN |
| 4 | 真實班次／課程／期別（真實班次／課程） | 經核實之課程計畫、辦訓名冊、期別／班次識別與時數 | UNK-0095-UNK_REAL_COURSE_COHORT（R07 新增）；SYN-0095-CASE_ID、SYN-0095-COURSE_NAME、SYN-0095-COURSE_HOURS 為合成值 | 未提供；UNKNOWN |
| 5 | 實際合格／邀請／回收／有效份數與原始問卷（實際數字／比例） | 可核對之對象清冊、發放／送達紀錄、回收清冊、有效性判定紀錄與原始問卷（如存在且有權使用） | SYN-0095-LEARNER_INVITED、SYN-0095-LEARNER_RETURNED、SYN-0095-LEARNER_VALID、SYN-0095-CUSTOMER_INVITED、SYN-0095-CUSTOMER_RETURNED、SYN-0095-CUSTOMER_VALID、UNK-0095-UNK_NONRESPONSE_REASON、UNK-0095-UNK_INVALID_ID、UNK-0095-UNK_INVALID_OTHER_SCORES、UNK-0095-UNK_REAL_RESPONSES | 未提供；UNKNOWN |
| 6 | 實際計算與分析（實際數字／比例） | 與原始回答可追溯連結之資料表、公式、計算過程與分析覆核記錄 | L-01–L-05 與 C-01–C-05 各題 SUM／MEAN／POSN／POSRATE，共 40 個題項鍵；另有 5 個分軌分母／回收衍生鍵（SYN-0095-LEARNER_RETURN_RATE、LEARNER_VALID_RATE、CUSTOMER_RETURN_RATE、CUSTOMER_VALID_RATE、CUSTOMER_VALID_RETURN_SHARE）及 8 個訓後追蹤計算鍵。全清冊共 53 個 DERIVED_SYNTHETIC_METRIC 鍵，完整鍵名與值以 R14 CSV／manifest 為準；UNK-0095-UNK_REAL_RESPONSES | 未提供；UNKNOWN |
| 7 | 實際改善決定、責任、期限與後續追蹤 | 有權者之決定原件、責任指派、期限核定及後續可比資料 | UNK-0095-UNK_IMPROVEMENT_ORIGINALS（R07 新增）；UNK-0095-UNK_REAL_RESPONSES；§8.5 之責任／負責人／期限／狀態欄位現為空白 | 未提供；UNKNOWN |
| 8 | 真實附件與經授權之儲存／存取路徑（真實附件與檔案位置） | 由正式資料管理者核實之檔案位置、存取權限、調閱紀錄與保存規則 | UNK-0095-UNK_ATTACHMENT_STORAGE_LOCATION（R07 新增） | 未提供；UNKNOWN |

頁次錨點（R14 最終匯出核對）：索引表位於 PDF pp.39–42；第 3 列在 p.39，第 7–8 列在 p.41。正文或版面變動後須重新核頁，不沿用舊版頁次。

不得以本報告虛構路徑、組織名稱、人員或簽章替代上述原件；亦不得以上表任一列之 UNKNOWN 狀態推論該項目不存在或本會未曾辦理。必要來源未提供時，維持 UNKNOWN，不升格 REAL。本索引僅列示升格路徑與所需來源，不對原始點協會評分，亦不宣稱任何項目已取得。

R08 歷史版本補充說明（定位與完整性界線；不代表 R14 頁次）：
(1) 定位：UNK-0095-UNK_FORMAL_EFFECTIVE_DATE 之 document_location 已由「§4.2 Tool-B real response-date and return-date fields；PDF pp. 10–11, 32」更正為實際存在於本版表單之 REAL 空白日期欄位（§4.1 Tool-A「實際填答日期」；§4.2 Tool-B「邀請發送日期」「送達日期」「實際填答日期」「回收日期」），並以 §9.5 第 3 列對應之。該欄位皆為空白，本版未填入任何真實日期，不得聲稱已有既存日期值。
(2) 頁碼錨點：此段僅記錄歷史 R08 CSV 的定位基礎，不代表對 R10、R11、R12 或 R13 的檢查；R14 current register 的頁碼定位以 R14 最終 Word 匯出 PDF 核對。
(3) 完整性：R08 清冊共 211 筆資料列、13 欄與唯一 register_key。R06 原有 208 鍵，移除 3 個不再使用的合併／合併正向率鍵後保留 205 鍵，再新增 6 個 UNKNOWN 升格索引鍵，因此 208 − 3 + 6 = 211；205 = 208 − 3。R06、R07 歷史 CSV 與 manifest 均維持原件，不回溯改寫；本版實際位元組與鍵集合以隨附 manifest 為準。


## Targeted current register locators

- `SYN-0095-LEARNER_RETURN_RATE` → `§6.3.1 learner return rate；PDF p. 27`
- `UNK-0095-UNK_FORMAL_EFFECTIVE_DATE` → `§4.1 Tool-A blank REAL date fields; §4.2 Tool-B blank REAL date fields; §9.5 row 3；PDF pp. 11, 15, 38`
- `UNK-0095-UNK_REAL_RESPONSES` → `§6.1–§6.4 synthetic response examples; §9.5 rows 5–6；PDF pp. 24–30, 39`
- `UNK-0095-UNK_IMPROVEMENT_ORIGINALS` → `§8.5 tracking table responsibility/person/deadline/status fields, PDF pp. 37–38；§9.5 row 7, PDF p. 41`
- `UNK-0095-UNK_ATTACHMENT_STORAGE_LOCATION` → `§8.3, PDF p. 35；§9.5 row 8, PDF p. 41；§10.1 attachment index, PDF pp. 42–43`

Independent Windows QA on exact R14 SHA:
- DOCX integrity: ZIP CRC clean; 383 paragraphs, 29 tables, 19 sections.
- Explicit font floor: body 10.5 pt across 515 explicit-size runs; table 9.5 pt across 1001 explicit-size runs.
- Register: 211 rows with PDF references; 258 expanded references; 0 out of bounds and 0 to empty pages. Sampled locator anchors are checked against PDF extracted text; full semantic locator scope remains bounded.
- Arithmetic recomputed from the displayed raw DOCX tables: learner N=14 item sums `[57,56,55,56,58]`, means `[4.0714,4.0000,3.9286,4.0000,4.1429]`, positive rates `[78.6,78.6,71.4,78.6,85.7]%`; customer N=5 sums `[21,20,20,21,21]`, means `[4.2,4.0,4.0,4.2,4.2]`, positive rates all `80.0%`. L-03 sensitivity excluding SYN-L14 recomputes to 52/13=4.00, 10/13=76.9%, rate gap 8.8pp, mean gap 0.14; synthetic only.
- Visual QA: all 46 pages checked in contact sheets; high-resolution direct inspection on 4, 5, 8, 9, 10, 19, 20, 21, 22, 23, 24, 31, 32, 33, 34, 39, 40, 41, 42, 43, 44, 45, 46. Nonblocking layout notes: p.5 continues only the last §1.4 row, p.9 the last two §3.2 SOP rows, p.20 a short section-4 continuation, and p.46 the closing candidate-boundary panel; all are readable with no clipping/overlap. Review whether any is a blocking presentation defect.

## Required reviewer output

Return a concise verdict exactly `PASS`, `PARTIAL`, or `FAIL`, with blocking count. Bind it to DOCX SHA `bde9a803c18137c98cf64992d75066b0722b5c3d3794eb7d6ab38667b88d0f19`. For each R12 observation, mark `CLOSED`, `PARTIAL`, or `OPEN` and cite the actual §/PDF page or register key. Check that: (a) official requirement and I18-E02 genre remain correct; (b) neighboring I18-E01/I18-E03 work is distinguished without fabricating neighboring originals; (c) R14 §1.4 and §9.5 anchors match the 46-page R14 PDF; (d) current vs historical register identity is unambiguous; (e) SAMPLE/SYNTHETIC versus REAL/UNKNOWN remains clear; and (f) the listed whitespace notes are nonblocking or identify a precise repair. Do not claim to have rehashed DOCX/PDF, independently run arithmetic, or inspected images beyond the evidence stated here. Do not claim formal acceptance.
