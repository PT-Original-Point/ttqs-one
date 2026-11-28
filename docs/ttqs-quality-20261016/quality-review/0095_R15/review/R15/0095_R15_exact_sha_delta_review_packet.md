# DOCX 0095 R15 — bounded exact-SHA closure review for R14 F-01

## Identity and scope
- Candidate: DOCX 0095 / official requirement I18-E02 / official checkbox: 建立目標客戶及學員滿意度調查機制（系統及流程面）。
- Exact DOCX SHA-256: `c70521d50fbec6cdc3b53ce3dc35fa2613069e60c58625b7eb2f96a5a6fd3658`; Word-export PDF SHA-256: `b106d9c8a66b7c3eae8ecd6c58d71adb797d03e0b7982de9f414c6e744006a04` (46 pages).
- Current register CSV SHA-256: `163796fb365509ddda1d03fe2db7f795feb4f45fba30cbb138fd50857eafd1c9`; current manifest SHA-256: `b75a1df5e57343565d05e6b72f2ee1f13681c2765a2cc7ffccd4f9b53f549b21`.
- Official source page 6 SHA-256: `e0ecd2d7b1fd8c20e03b9e651083ee767ccaf3c4a6297f9cb0e7709d07620f02`; Unique Blueprint SHA-256: `9a22b3acd4bdafb15f18c15ee89088f4fb5ee334bfef9a1917fcc5740b7979c2`.
- This is a bounded delta review of R14 F-01 and R15 current locator/identity binding, not a fresh full re-review of unchanged R12-reviewed content. Candidate only; no formal association acceptance or real execution is asserted.

## Prior exact-SHA finding to resolve
R14 exact-SHA response returned PARTIAL with one blocking finding F-01. It found current register key `UNK-0095-UNK_FORMAL_EFFECTIVE_DATE` cited §9.5 row 3 at PDF p.38, while R14 §9.5 row 3 was actually on p.39. R14 DOCX SHA was `bde9a803c18137c98cf64992d75066b0722b5c3d3794eb7d6ab38667b88d0f19`; response SHA `19e93153345f208840efe71d1a91592f328d8b82ed7f519c2fe728ec1de10cd3`; receipt SHA `4e79cab0ddca3832dcbeac3baf79d52c70ba12ada00864aacb36abf0a6aa6b3d`. The R14 reviewer did not directly inspect or rehash files; Windows QA later confirmed p.39.

## Current CSV row
`UNK-0095-UNK_FORMAL_EFFECTIVE_DATE`

`document_location`: `§4.1 Tool-A blank REAL date fields; §4.2 Tool-B blank REAL date fields; §9.5 row 3；PDF pp. 11, 15, 39`

R14 current CSV SHA-256: `e1331efc3f5109bcc1502821bb132b71cce682ec08926741915b0e0c906ad5b6`.
The bounded local comparison found exactly one changed field in one row: this page locator moved p.38→p.39. No other CSV cells, keys or synthetic facts changed. The corrected location is §9.5 row 3, PDF pp.11, 15, 39.

## Direct visual evidence provided
The attached high-resolution R15 PDF page image `qa/render_0095_R15_final/page-39.png` shows §9.5, row 3, the target register key, and the text identifying that row as checked against the R15 final PDF p.39. The final Word export remains 46 pages, PDF SHA `b106d9c8a66b7c3eae8ecd6c58d71adb797d03e0b7982de9f414c6e744006a04`. Please inspect the attached page image directly if supported; otherwise mark the image-specific portion UNKNOWN.

## Current manuscript locator sections
### §1.4 page map
### 1.4 官方要求—候選結果—證據頁次—覆核追溯表

**官方來源：指標 18「訓練系統的一般性功能─目標客戶及學員的評價」；本交付件依 Unique Blueprint 指派對應 I18-E02 檢核框「建立目標客戶及學員滿意度調查機制（系統及流程面）」，不表示官方佐證表只有此一佐證項目。正式來源頁次為第 6 頁，逐字內容與 SHA-256 見 §1.2；評分級距另見 §1.3。**

| 官方指標 18／I18-E02 覆核面向 | 候選結果 | 文件證據定位（章節 → PDF頁次，逐項對應） | 覆核方式及證據界線 | 候選狀態 |
| :--- | :--- | :--- | :--- | :--- |
| **指標18／I18-E02：調查機制系統面** | 提出兩類對象的量表、資料字典、計算口徑、存取及版本控制建議。 | §2.1–§2.4 → PDF pp.5–6<br>§3.1–§3.2 → PDF pp.6–9<br>§4.1 → pp.10–13；§4.2 → pp.13–17；§4.3 → pp.17–19<br>§5.1 → pp.20–22；§5.2 → p.22 | 核對工具、欄位、分母及公式；均為候選設計，不證明已採用。 | PROPOSED |
| **指標18／I18-E02：端到端作業流程面** | 展開需求界定、對象篩選、告知、發放、回收、檢核、分群分析、審閱及追蹤。 | §2.1–§2.4 → PDF pp.5–6<br>§3.1 → p.6；§3.2 → pp.7–9<br>§8.1–§8.5 → pp.35–38 | 核對流程輸入、控制點、輸出及暫緩／退回條件；實際執行 UNKNOWN。 | PROPOSED |
| **指標18／I18-E02：目標客戶與學員分軌評價** | 提供 Tool-A、Tool-B、完整 SAMPLE／SYNTHETIC 明細及分群計算。 | §4.1 → pp.10–13；§4.2 → pp.13–17；§4.3 → pp.17–19<br>§6 opening / case metadata → PDF p.23<br>§6.1–§6.4 → pp.24–30<br>§7.1 → p.31；§7.2 → pp.31–34（附圖 A → pp.33–34） | 分別檢查兩種問卷、分母、均分與正向率；不得合併取代分群結果。 | SYNTHETIC |
| **指標18／I18-E02：結果判讀與持續改善** | 說明限制、證據強度、候選改善建議、責任欄位及後續核驗方式。 | §6.3.3 → PDF p.28；§6.4 → pp.29–30；§6.4.1 → p.30<br>§7.3–§7.4 → PDF p.34<br>§8 → PDF pp.35–38<br>§9.5 → PDF pp.39–42<br>§10 → PDF pp.42–46 | 核對合成值、限制與替換清冊；無真實核定、實施或效果證據。 | PROPOSED／SYNTHETIC |

頁次錨點說明：本表頁次以最終 R15 Word 匯出逐項核對；章節錨點為主要定位，PDF exact SHA 與視覺檢查範圍記於外部 QA 收據。若正文或版面再變更，必須重新核頁，不得沿用舊版頁碼。


### §9.5 current real-source index
### 9.5 升格真實（REAL）所需外部佐證路徑與索引清單

本索引逐項對應 Unique Blueprint `real_data_required` 之升格類別（正式日期；真實人名／角色；核准／簽章；真實班次／課程；實際數字／比例；真實附件與檔案位置），並就本件之實際需求細分為 8 個可核對項目。每列均載明所需真實來源、可對應之事實粒度清冊鍵，以及本次取得狀態；目前清冊鍵以 `qa/0095_R15_synthetic_replacement_register.csv` 為準；R08、R11、R12、R13、R14 CSV／manifest 均保留為歷史原件，不作為本版頁碼依據（R07 版清冊 `qa/0095_R07_synthetic_replacement_register.csv` 為歷史標的，維持不變）。

| # | 升格核實項目（對應 Blueprint real_data_required 類別） | 需要的真實來源 | 對應清冊鍵 | 本次狀態 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 真實作者與覆核者姓名／角色（真實人名／角色） | 協會編製者與正式覆核者之具名紀錄、職稱及授權依據 | UNK-0095-UNK_AUTHOR_REVIEWER_IDENTITY（R07 新增）；PROP-0095-ROLE-CRD、PROP-0095-ROLE-COL、PROP-0095-ROLE-ANL、PROP-0095-ROLE-DEC 僅為候選職能標籤，非人名 | 未提供；UNKNOWN |
| 2 | 核准／簽章原件（核准／簽章） | 有權核准者之核定文件、簽章或會議決議原件及其生效依據 | UNK-0095-UNK_APPROVAL_SIGNATURE（R07 新增）；UNK-0095-UNK_REAL_SYSTEM | 未提供；UNKNOWN |
| 3 | 正式／生效日期（正式日期） | 制度或工具之核定發布日、生效日，以及真實問卷之施測與回收日期 | UNK-0095-UNK_FORMAL_EFFECTIVE_DATE（R07 新增；本版 REAL 日期欄位留白，Tool-A／Tool-B REAL 空白日期欄位見 R15 PDF pp.11、15；本索引第 3 列在 R15 最終 PDF p.39 核對）；SYN-0095-COURSE_DATE、SYN-0095-FOLLOWUP_DATE 為合成日期 | 未提供；UNKNOWN |
| 4 | 真實班次／課程／期別（真實班次／課程） | 經核實之課程計畫、辦訓名冊、期別／班次識別與時數 | UNK-0095-UNK_REAL_COURSE_COHORT（R07 新增）；SYN-0095-CASE_ID、SYN-0095-COURSE_NAME、SYN-0095-COURSE_HOURS 為合成值 | 未提供；UNKNOWN |
| 5 | 實際合格／邀請／回收／有效份數與原始問卷（實際數字／比例） | 可核對之對象清冊、發放／送達紀錄、回收清冊、有效性判定紀錄與原始問卷（如存在且有權使用） | SYN-0095-LEARNER_INVITED、SYN-0095-LEARNER_RETURNED、SYN-0095-LEARNER_VALID、SYN-0095-CUSTOMER_INVITED、SYN-0095-CUSTOMER_RETURNED、SYN-0095-CUSTOMER_VALID、UNK-0095-UNK_NONRESPONSE_REASON、UNK-0095-UNK_INVALID_ID、UNK-0095-UNK_INVALID_OTHER_SCORES、UNK-0095-UNK_REAL_RESPONSES | 未提供；UNKNOWN |
| 6 | 實際計算與分析（實際數字／比例） | 與原始回答可追溯連結之資料表、公式、計算過程與分析覆核記錄 | L-01–L-05 與 C-01–C-05 各題 SUM／MEAN／POSN／POSRATE，共 40 個題項鍵；另有 5 個分軌分母／回收衍生鍵（SYN-0095-LEARNER_RETURN_RATE、LEARNER_VALID_RATE、CUSTOMER_RETURN_RATE、CUSTOMER_VALID_RATE、CUSTOMER_VALID_RETURN_SHARE）及 8 個訓後追蹤計算鍵。全清冊共 53 個 DERIVED_SYNTHETIC_METRIC 鍵，完整鍵名與值以 R15 CSV／manifest 為準；UNK-0095-UNK_REAL_RESPONSES | 未提供；UNKNOWN |
| 7 | 實際改善決定、責任、期限與後續追蹤 | 有權者之決定原件、責任指派、期限核定及後續可比資料 | UNK-0095-UNK_IMPROVEMENT_ORIGINALS（R07 新增）；UNK-0095-UNK_REAL_RESPONSES；§8.5 之責任／負責人／期限／狀態欄位現為空白 | 未提供；UNKNOWN |
| 8 | 真實附件與經授權之儲存／存取路徑（真實附件與檔案位置） | 由正式資料管理者核實之檔案位置、存取權限、調閱紀錄與保存規則 | UNK-0095-UNK_ATTACHMENT_STORAGE_LOCATION（R07 新增） | 未提供；UNKNOWN |

頁次錨點（R15 最終匯出核對）：索引表位於 PDF pp.39–42；第 3 列在 p.39，第 7–8 列在 p.41。正文或版面變動後須重新核頁，不沿用舊版頁次。

不得以本報告虛構路徑、組織名稱、人員或簽章替代上述原件；亦不得以上表任一列之 UNKNOWN 狀態推論該項目不存在或本會未曾辦理。必要來源未提供時，維持 UNKNOWN，不升格 REAL。本索引僅列示升格路徑與所需來源，不對原始點協會評分，亦不宣稱任何項目已取得。

R08 歷史版本補充說明（定位與完整性界線；不代表 R15 頁次）：
(1) 定位：UNK-0095-UNK_FORMAL_EFFECTIVE_DATE 之 document_location 已由「§4.2 Tool-B real response-date and return-date fields；PDF pp. 10–11, 32」更正為實際存在於本版表單之 REAL 空白日期欄位（§4.1 Tool-A「實際填答日期」；§4.2 Tool-B「邀請發送日期」「送達日期」「實際填答日期」「回收日期」），並以 §9.5 第 3 列對應之。該欄位皆為空白，本版未填入任何真實日期，不得聲稱已有既存日期值。
(2) 頁碼錨點：此段僅記錄歷史 R08 CSV 的定位基礎，不代表對 R10、R11、R12、R13 或 R14 的檢查；R15 current register 的頁碼定位以 R15 最終 Word 匯出 PDF 核對。
(3) 完整性：R08 清冊共 211 筆資料列、13 欄與唯一 register_key。R06 原有 208 鍵，移除 3 個不再使用的合併／合併正向率鍵後保留 205 鍵，再新增 6 個 UNKNOWN 升格索引鍵，因此 208 − 3 + 6 = 211；205 = 208 − 3。R06、R07 歷史 CSV 與 manifest 均維持原件，不回溯改寫；本版實際位元組與鍵集合以隨附 manifest 為準。


## Official source distinction
The exact official page-6 I18-E02 text is: “建立目標客戶及學員滿意度調查機制（系統及流程面）。” It is the system/process mechanism-design deliverable. I18-E01 is oral records; I18-E03 is a thank-you letter. The candidate explicitly leaves association approval, signatures, real dates, real survey responses, and actual execution UNKNOWN; all example data remain SAMPLE/SYNTHETIC.

## Required bounded reviewer output
Return exactly a verdict `PASS`, `PARTIAL`, or `FAIL`, with blocking count, bound to DOCX SHA `c70521d50fbec6cdc3b53ce3dc35fa2613069e60c58625b7eb2f96a5a6fd3658`. State whether R14 F-01 is `CLOSED`, `PARTIAL`, or `OPEN`. Verify: (1) the current CSV row points to §9.5 row 3 at p.39; (2) the actual page 39 and manuscript map agree; (3) the DOCX binds the R15 CSV SHA; (4) only this register locator changed versus R14; (5) no REAL fact, approval, signature or execution is inferred. Cite exact key and page. Do not claim formal acceptance, directly rehash files, or review any file that was not actually provided/read. Provider identity must remain UNKNOWN unless attested by the native response.
