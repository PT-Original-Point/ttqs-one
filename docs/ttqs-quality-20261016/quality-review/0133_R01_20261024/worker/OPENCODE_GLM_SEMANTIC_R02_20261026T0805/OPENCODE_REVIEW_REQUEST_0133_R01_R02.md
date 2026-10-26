# OpenCode v2 independent semantic review request — TTQS ONE 0133 R01

## Review contract
You are an independent, read-only semantic reviewer. Review ONLY the supplied candidate text and source materials. Do not use tools, browser, Computer Use, external services, or modify/create/delete any file. Do not claim to have viewed the DOCX binary, images, rendered pages, Windows, GitHub, or performed a real-world human usability test. The DOCX was extracted locally from the exact candidate below; your review scope is TEXT_ONLY. Do not infer actual association performance, real records, approvals, signatures, or official acceptance from SAMPLE data.

Return a concise but evidence-dense Markdown review with verdict `PASS`, `PARTIAL`, or `FAIL`; exact candidate SHA-256; work/doc/requirement/blueprint identities; review scope and limits; findings with section/table/row locators and short evidence descriptions; and a final list of blocking defects or `none`. Do not repeat or invent SHA values. If the supplied extracted text is incomplete or you cannot bind it to the candidate SHA, use `PARTIAL` and explain why.

## Exact identity and input binding
- Project/work: TTQS_ONE / TTQS_ONE_0133_I19-E22_R01
- DOCX: 0133_I19-E22_CANDIDATE_R01.docx
- Official requirement: I19-E22; official evidence table page 8; exact wording in supplied source is “每年訓練班次、人次均持續成長。”
- Project 157 index: 146. This is an internal project index, NOT an official printed checkbox serial. Official printed serial remains UNKNOWN unless the supplied official source prints it.
- Unique Blueprint SHA-256: edb8d241b1604790b36daf1622b907a9985ec7901c6d1e0a79f440be5fcb42fd
- Source packet SHA-256: 097dcc766a8c2b0f320cb51e084e46681e85deef23a9476b94890726654b2863
- DOCX SHA-256: 25116afb8206e0828c8b3a4a763845a9c3e672a4cb49969a64a2a3737d87256b
- DOCX extracted-text SHA-256: 314c24da92f364dddd4609956b602b4b19dd89bb48562392b752bd79b65bbd5d
- Other source input SHA-256 values: unique 142 Blueprint JSON ceab756c5f176bb29a63622a8150d30dcb6bda303da7e6f9426bad55d9dc4b84; official page-8 source text cd5a1002c56577c35ed836eebd7e983f6fbabec1992111dd3909a3b0faa718fb; neighbor crosswalk abbfe9202cb846e92d425d7e8464e6f8b8af78989c98ecdf9e1457a3ed6db2a1; 157 excerpt 811fb839a813266290a518938922524aa43894ae65c5be5277e2a3c96f016108.

## Required review checks
1. Correct genre and direct fit to the official requirement: an annual record and trend analysis of training class sessions AND trainee person-times, checking every adjacent year rather than only first/last.
2. Correct distinction from negative neighbors: 0132/I19-E21 product defect improvement and 0134/I19-E23 member-count/fee-income change. Reject accidental reuse, mixing, or title-only substitution.
3. Operational completeness for a small volunteer association: yearly scope; source trail from plan/class closure/attendance; definitions; roles; deduplication; practical steps; complete filled sample; reusable forms; exceptions; hold/reject criteria; correction trace; evidence retention and replacement register.
4. Recalculate the SAMPLE values and displayed growth from the supplied text. Expected examples in the Blueprint include 2023 6 classes/72 person-times, 2024 8/104, 2025 10/141; 24 completed classes plus 1 cancelled excluded; adjacent growth rates 33.3%/44.4% and 25.0%/35.6%; do not let endpoint growth replace year-by-year judgment. Check denominators, units, rounding, zero/missing rules, totals and conclusion.
5. Check whether “person-times” definition is coherent, avoids counting same attendee repeatedly within a class, and separates sign-up count/unique persons/class-days.
6. Check every case fact is clearly SAMPLE/SYNTHETIC, any REAL evidence is explicitly UNKNOWN/HOLD, and the document avoids fabricated association decisions, approvals, signed originals or actual performance claims.
7. Title-blind test: based on body alone, is the purpose identifiable as annual training class/person-time trend evidence? Does the body explain what evidence proves the claim and what cannot yet be concluded?
8. Check internal traceability and exact official identity. Never turn index 146 into a printed official checkbox serial.
9. Scope limits: semantic text-only review. Do not assess typography, layout, charts/images, page rendering, DOCX opening, or formal acceptance; those have separate technical/visual evidence.

## AUTHORITATIVE SOURCE PACKET
# 0133 來源包 I19-E22 R01

狀態：SOURCE_PREP_COMPLETE；候選資料僅供可逆建置；REAL 成果及正式接受均 UNKNOWN。

## 核實身分
- project_id：TTQS ONE
- doc_id：0133（內部 142 序列文件編號）
- 142 crosswalk requirement_id：I19-E22
- 157 Blueprint index：146；官方指標 I19-L3；官方參考佐證資料表 PDF 第 8 頁
- 官方原文：「每年訓練班次、人次均持續成長。」
- 文件文類：年度班次與參訓人次登錄表及多年度趨勢分析
- 官方印刷方框流水號：UNKNOWN；不可用 doc_id、內部 ID 或 157 index 代替。

## 來源版本
來源讀取基準：GitHub PR #92 分支 `work/ttqs-one-document-quality-contract-20261016`，HEAD `69434ddef4012e4ac1e94d2dfed638f67f926f19`。以下 blob 與 SHA 由該 HEAD 直接讀取。

| 來源 | 路徑 | Git blob | SHA-256 |
|---|---|---|---|
| 官方佐證資料表 PDF | `docs/ttqs-quality-20261016/quality-review/0031_R06/inputs/official_source.pdf` | `9c7621decdad585b743bf2b3d949ee5518b7bee0` | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` |
| 157 唯一 Blueprint | `docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md` | `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` | `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216` |
| 142 crosswalk | `docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/official_129_to_142_crosswalk.csv` | `1ac4a8419088d947947031b758e29c35a3606514` | `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679` |
| 142 Blueprint seed | `docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/blueprint_seed_142.csv` | `f20ac9ae37700eb03a93b8da4407e7bf4788b602` | `280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0` |
| 詳細 142 Blueprint | `docs/ttqs-quality-20261016/quality-review/0040_R04/inputs/BLUEPRINT_CURRENT.jsonl` | `cab446ede479001334289d18062e6b8bb2340dc3` | `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e` |
| 逐指標寫作手冊 | `docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md` | `4ff863d9f534b6359fc1c7c1685bd8cce02da886` | `7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa` |
| Human Mission | `docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md` | `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` | `07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8` |

## 官方資料位置與辨識

官方 PDF 第 8 頁常見 3 分參考佐證列載：「每年訓練班次、人次均持續成長。」同頁相鄰項包括學員訓後創業案例、證照/就業、個人產品不良件數下降及會員人數/會費逐年增加。0133 只處理班次及人次，不把鄰項資料挪入本件。官方資料表說明為常見參考例，並非原始點協會已發生成果、已核准事實或評核分數。

142 crosswalk 當前列：`I19-E22, 1, 0, 0133, 年度訓練班次與參訓人次趨勢表`。157 index146 對應 I19-L3 的「年度班次/人次：完整多期數據」。

## 真實資料界線

本次沒有取得原始點協會年度課程清冊、實際辦理紀錄、結班資料、參訓名冊/簽到、核准統計口徑、簽核或外部佐證。案例日期、課程、班次、參訓人次、來源鍵、角色、彙總及成長率均為 SAMPLE/SYNTHETIC。`REAL_EVIDENCE=UNKNOWN`；不得宣稱協會班次或人次實際成長，不得寫成已核准或評核已接受。

專屬內容及驗收見 `UNIQUE_BLUEPRINT_0133_I19-E22_R01.md`。歷史 0133 DOCX 僅為存在性/錯件風險線索；不得複製或作正文模板。


## UNIQUE BLUEPRINT
# UNIQUE BLUEPRINT｜0133｜I19-E22｜R01

## 1. 文件身分及官方來源
- 專案：TTQS ONE
- 文件編號：0133（內部 142 序列 doc_id）
- 內部要求：I19-E22（142 文件 crosswalk；不是官方方框流水號）
- 專案 157 Blueprint：index 146，I19-L3，官方佐證資料表第 8 頁
- 官方參考佐證原文：**「每年訓練班次、人次均持續成長。」**
- 文件名稱：年度訓練班次與參訓人次趨勢表
- 官方印刷方框序號：UNKNOWN；不可拿 0133、I19-E22 或 index 146 充當。
- 文類：年度資料登錄表＋多年度趨勢分析；須可供訓練行政人員逐班登錄、覆核來源及重算趨勢，也可供評核委員追到原始班次和簽到資料。

## 2. 專屬用途與錯件防護
本件只呈現逐年實際辦理班次數與參訓人次的年度序列，明確比較每一相鄰年度的變化。官方句子同時要求班次與人次持續成長；不能只比較三年首尾、不能以班次增加代替人次增加、也不能把報名人數、課程日數或唯一學員數誤稱參訓人次。

負向近鄰：0132／I19-E21 是產品不良單位及前後檢驗趨勢，分子分母是產品與受檢產品；0134／I19-E23 是會員人數與會費收入年度變化。0133 不得挪用鄰項數據或正文。移除標題後，正文仍須因逐班 run_id、班次狀態、匿名學員班次關聯、年度雙序列與相鄰年度成長檢查而可辨認為本件。

## 3. 統計口徑與資料控制

### 3.1 年度與班次
- 年度採曆年 1 月 1 日至 12 月 31 日，按課程實際辦理日歸屬年度；跨年系列採最後一個具實質教學活動年度，並列跨年日期及理由。年度規則一經採用，不得為追求成長而改變。
- 一個班次是具唯一班次 ID、特定課程與同一 cohort，實際發生至少一次教學活動且有課程結案／出席來源的辦理單位。同一 cohort 多日課程只計一班；同課程另開不同 cohort 才另計一班。
- 僅排定但取消、延期未實際開課、零出席或只有宣傳／報名資料者不計已辦班次，須另列排除清冊及狀態。

### 3.2 參訓人次
- 本表操作定義：每個「班次 ID × 去識別學員 ID」若該學員至少出席該班一次，計 1 參訓人次。同一人同一班的多個上課日只計 1 人次；同一人參加兩個不同班次計 2 人次。
- 參訓人次不是報名數、座位數、課程日出席加總，也不是跨年唯一自然人數。取消報名、全程未到者不計；名冊與簽到資料不一致時先 HOLD 並查明。
- 此計數規則是 SAMPLE 示範的可重算定義，不代表協會已採正式政策。換成 REAL 前須引用實際核准或持續一致使用的計數政策；沒有政策時明示方法並由權責角色確認，否則不得作正式績效結論。

### 3.3 相鄰年度判讀
- 班次成長率 = (本年已辦班次 − 前年已辦班次) ÷ 前年已辦班次 × 100%。
- 參訓人次成長率 = (本年參訓人次 − 前年參訓人次) ÷ 前年參訓人次 × 100%。
- 年度淨增量亦須分開列出。分母為 0 或前年度缺漏時，成長率列 N/A，不能除以零或判為持續成長。
- 要支持「所列期間每年均持續成長」，每一相鄰年度的班次增量及參訓人次增量都須大於 0，且口徑與來源可比。只看首尾成長不足以支持「每年」。任一年任一指標未增加，應如實標為「該相鄰年度未同時成長」。
- 百分率用未四捨五入值計算，顯示至小數 1 位；班次、人次保留整數。

## 4. 完整合成案例規格
案例 ID：`SYN-0133-CASE-01`；年度 2023–2025；全部日期、課程、班次、角色、來源及數字都是 SAMPLE/SYNTHETIC，並非原始點協會紀錄。案例安排 2023 年 6 班／72 人次、2024 年 8 班／104 人次、2025 年 10 班／141 人次；兩項指標在每一相鄰年度都增加。2025 另設 1 班排定後取消的合成例外，明確排除於已辦班次與參訓人次。

| 年度 | 班次 ID | 日期 | SAMPLE 課程名稱 | 狀態 | 參訓人次 | 合成來源鍵 |
|---|---|---|---|---|---:|---|
|2023|SYN-23-01|2023-02-11|志工服務紀錄與個資保護|已辦|12|SYN-PLAN/ATT/CLOSE-23-01|
|2023|SYN-23-02|2023-04-15|活動安全與風險辨識|已辦|12|SYN-PLAN/ATT/CLOSE-23-02|
|2023|SYN-23-03|2023-06-10|社區服務溝通|已辦|12|SYN-PLAN/ATT/CLOSE-23-03|
|2023|SYN-23-04|2023-08-12|專案成果紀錄與追蹤|已辦|12|SYN-PLAN/ATT/CLOSE-23-04|
|2023|SYN-23-05|2023-10-14|志工團隊協作|已辦|12|SYN-PLAN/ATT/CLOSE-23-05|
|2023|SYN-23-06|2023-12-09|基礎行政與檔案管理|已辦|12|SYN-PLAN/ATT/CLOSE-23-06|
|2024|SYN-24-01|2024-02-17|志工服務紀錄與個資保護|已辦|13|SYN-PLAN/ATT/CLOSE-24-01|
|2024|SYN-24-02|2024-03-23|活動安全與風險辨識|已辦|13|SYN-PLAN/ATT/CLOSE-24-02|
|2024|SYN-24-03|2024-05-18|社區服務溝通|已辦|13|SYN-PLAN/ATT/CLOSE-24-03|
|2024|SYN-24-04|2024-06-22|專案成果紀錄與追蹤|已辦|13|SYN-PLAN/ATT/CLOSE-24-04|
|2024|SYN-24-05|2024-08-17|志工團隊協作|已辦|13|SYN-PLAN/ATT/CLOSE-24-05|
|2024|SYN-24-06|2024-09-21|基礎行政與檔案管理|已辦|13|SYN-PLAN/ATT/CLOSE-24-06|
|2024|SYN-24-07|2024-11-16|社區活動風險與通報|已辦|13|SYN-PLAN/ATT/CLOSE-24-07|
|2024|SYN-24-08|2024-12-14|志工排班與服務交接|已辦|13|SYN-PLAN/ATT/CLOSE-24-08|
|2025|SYN-25-01|2025-01-18|志工服務紀錄與個資保護|已辦|12|SYN-PLAN/ATT/CLOSE-25-01|
|2025|SYN-25-02|2025-02-22|活動安全與風險辨識|已辦|13|SYN-PLAN/ATT/CLOSE-25-02|
|2025|SYN-25-03|2025-04-12|社區服務溝通|已辦|14|SYN-PLAN/ATT/CLOSE-25-03|
|2025|SYN-25-04|2025-05-17|專案成果紀錄與追蹤|已辦|14|SYN-PLAN/ATT/CLOSE-25-04|
|2025|SYN-25-05|2025-06-21|志工團隊協作|已辦|14|SYN-PLAN/ATT/CLOSE-25-05|
|2025|SYN-25-06|2025-07-19|基礎行政與檔案管理|已辦|14|SYN-PLAN/ATT/CLOSE-25-06|
|2025|SYN-25-07|2025-08-23|社區活動風險與通報|已辦|15|SYN-PLAN/ATT/CLOSE-25-07|
|2025|SYN-25-08|2025-09-20|志工排班與服務交接|已辦|15|SYN-PLAN/ATT/CLOSE-25-08|
|2025|SYN-25-09|2025-10-18|志工團隊協作實務|已辦|15|SYN-PLAN/ATT/CLOSE-25-09|
|2025|SYN-25-10|2025-12-06|專案成果紀錄與追蹤實務|已辦|15|SYN-PLAN/ATT/CLOSE-25-10|
|2025|SYN-25-X01|2025-11-22|志工排班與服務交接（合成取消例）|取消|0|SYN-PLAN-25-X01|

合計：2023 6 班、72 人次；2024 8 班、104 人次；2025 10 班、141 人次；三年 24 個已辦班次，合成取消班 1 班排除。三年共 317 人次。

| 比較 | 班次計算 | 班次成長 | 人次計算 | 人次成長 | 判讀 |
|---|---|---:|---|---:|---|
|2024 對 2023|(8−6)÷6×100|33.3%|(104−72)÷72×100|44.4%|兩項均增加|
|2025 對 2024|(10−8)÷8×100|25.0%|(141−104)÷104×100|35.6%|兩項均增加|
|2025 對 2023（補充）|(10−6)÷6×100|66.7%|(141−72)÷72×100|95.8%|首尾增加但不可代替逐年判讀|

## 5. 正文結構和使用方式
1. 首頁30秒摘要：官方命題、用途、讀者、使用時點、輸出、資料狀態、三年樣例摘要、使用者下一步。
2. 官方來源與身分；分開顯示官方原文、doc_id、內部 ID、157 index、官方印刷序號 UNKNOWN。
3. 資料口徑、跨年班次規則、取消班次處理、唯一學員與人次差異。
4. 訓練計畫→已辦班次/結案清冊→匿名學員名冊與簽到→年度彙整→第二人複核的來源鏈及每欄定位。
5. 24筆合成已辦班次明細與1筆取消例外、年度彙總及逐年公式。
6. 可實際照做的 SOP：鎖定清冊、判斷狀態、班次去重、班次×學員去重、彙總、重算、第二人覆核、更正留痕、鎖版。
7. 欄位字典：欄位/定義/來源/記錄角色/核對方法/輸出用途。
8. 例外判定表：取消、延期、零出席、跨年、缺名冊、同班多日重複計算、重複 ID、漏結案、政策改變。
9. 趨勢分析：班次與人次分別作相鄰年度判斷，不歸因、不推論唯一學員數；不創設官方百分比門檻。
10. 可複製年度登錄表和至少一個全填妥示範；REAL 原件替換區明示目前未取得證據。
11. 逐事實 SAMPLE 替換簿：精確定位每筆日期、班次 ID、課名、狀態、人次、來源 ID、年度彙總、成長率、角色與更正；記錄需要替換的 REAL 原件類型/授權位置。
12. HOLD/REJECT/READY、0132/0134負向近鄰、附件來源與版本。

## 6. 日常判定

READY 僅代表資料足以形成正式年度分析：逐班來源、實際辦理狀態、統一期間與參訓名冊/簽到可追溯；口徑固定；至少兩個相鄰年度完整；第二人可重算。

HOLD：名冊簽到不合；班次狀態、跨年歸屬或口徑不明；只有報名數或彙總；取消/延期不明；來源缺漏；年度不完整；重複可能未排除；前後政策變更未能分層。可補件但不得作對外結論。

REJECT：課程日數當班次；日簽到加總冒充人次；報名數冒充參訓人次；取消班計入已辦；只呈現首尾掩蓋年度下降；算式不一致；移除 SAMPLE 標示卻無 REAL 原件。

官方沒有指定成長率最低門檻或統計顯著性要求，不得杜撰。

## 7. 禁止事項及驗收

所有案例/數據/日期/課程/角色/來源鍵必須標示 SAMPLE/SYNTHETIC。不存在 REAL 原件時不得稱作原始點協會實績、已核准事實、正式政策或評核接受；正式印刷方框流水號 UNKNOWN。不得複製歷史 0133 正文。

驗收：官方原文與定位正確；文件/內部 ID 不混；24 已辦+1取消的年度合計吻合；每一相鄰年度兩指標皆可獨立重算；取消班未算；人次定義可去重；資料鏈可用；有完整合成逐班數據和可複製實務表；替換簿逐筆定位；標題盲測通過；0132、0134 明確排除；Word 正文>=10.5pt、表格>=9.5pt、全頁視覺驗收；獨立 exact-SHA 語意審查未由 Builder 自報代替。


## UNIQUE 142 BLUEPRINT RECORD
{
  "deliverable_id": "0133",
  "requirement_id": "I19-E22",
  "final_filename": "0133__年度訓練班次與參訓人次趨勢表.docx",
  "document_genre": "專屬佐證紀錄｜年度訓練班次與參訓人次趨勢表",
  "document_purpose": "本件專屬焦點：年度訓練班次與參訓人次趨勢表；需直接回應的官方佐證要求為：每年訓練班次、人次均持續成長。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。",
  "primary_user_or_reader": "供執行人員、主管與評核閱讀者追溯要求、事實、證據位置及覆核狀態。",
  "evidence_role": "保存此項要求專屬的原始紀錄或證據索引；不代替第三方原件。 本文件只擁有 I19-E22 的直接紀錄／分析口徑；不得吞併其他要求的事實。",
  "source_of_truth": "官方查核佐證表精確原文『每年訓練班次、人次均持續成長。』，表內頁次 8，讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH；REQ_157_MAP 對應 I19-E22；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。",
  "required_sections": "紀錄目的、責任及適用界線；官方要求拆解與證明路徑；來源、形成時點及納入規則；欄位定義及證據位置；完整合成紀錄示例；核對、計算與一致性判定；例外、缺證及更正軌跡；真實原件與合成示例的區別；覆核、保管及調閱規則；相關要求及文件交叉引用；真實資料替換清單；附件索引與版本",
  "required_tables_or_figures": "欄位—定義—來源—填寫者—驗證規則；完整合成填寫列及欄位解說；問題／例外—修正—覆核及追蹤；官方要求—表單欄位—附件定位追溯表",
  "required_fields_or_questions": "合成資料識別碼；日期欄位及合成標示；責任角色代碼；來源／附件位置欄位；判定、理由、覆核及後續行動",
  "required_calculations_or_analysis": "若此表單有數量、金額、期間或比例，明列定義、分子分母與逐步算例；若沒有，明示不適用並提供至少一個欄位驗證／完整度判斷示例。",
  "required_cross_references": "同要求分件 無；相鄰要求 I19-E21, I19-E23；共用原始來源時只引用核實結果，不複製別份文件正文。",
  "real_data_required": "升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。",
  "third_party_evidence_required": "若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。",
  "prohibited_fabrication": "不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。",
  "title_blind_test": "遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『年度訓練班次與參訓人次趨勢表』並證明『每年訓練班次、人次均持續成長。』；若可無修改移作其他要求即失敗。",
  "negative_choice_neighbors": "0132《個人產品不良件數與訓後改善分析表》（I19-E21）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0134《會員人數及會費收入逐年變化分析報告》（I19-E23）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。",
  "acceptance_tests": "移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『年度訓練班次與參訓人次趨勢表』，且能指出直接回應『每年訓練班次、人次均持續成長。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。",
  "document_role": "evidence_record",
  "official_requirement_text": "每年訓練班次、人次均持續成長。",
  "official_checkbox_text": "每年訓練班次、人次均持續成長。",
  "official_evidence_table_page": "8",
  "official_source_readback_status": "PDF_TEXT_EXACT_PAGE_MATCH",
  "official_visually_checked_pages": "",
  "requirement_deliverable_siblings": "0133",
  "docx_body_template_policy": "FROM_SOURCE_ONLY; old body is discovery evidence only and prohibited as rebuild template; Wave005 R3 0031-0040 quality-height references only; Wave001-004 tainted; old Wave005 invalid; Wave006 prohibited.",
  "synthetic_population_rule": "缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。",
  "historical_blueprint_source": "bad8b1fe91596a067c04e3ed29deadd48c28a243dfa26e9aa845b87f45d45988",
  "historical_body_use": "PROHIBITED",
  "source_map_notes": "129 exact official requirement rows + reconciled 142-ID crosswalk; official source PDF and exact Drive readback evidence are recorded in runtime SOURCE/CONTROL maps."
}


## OFFICIAL PAGE 8 SOURCE TEXT
                 內涵說明（以下為         常見參考佐證資料
項目    評核指標項目     例，但不以此為       （並註明資料來源及頁碼）
                     限）
                3分 目標市場及顧客     具體紀錄及評量。
                價值均有一定程度提     感謝函。
                升的效果。         其他：
                4分 目標市場及顧客  2 分之常見參考佐證資料：
                價值均有顯著具體的     有具體紀錄可辨識目標市場及顧
                提升績效。          客價值均有部份提升效果。
                              相關證據顯示有初步訓練成果，
                               且有部份佐證資料。
                              提出學員滿意度、考試測驗或心
                               得報告（學習技能面）。
                              提出課後追蹤調查與分析結果、
                               證照通過情形（學習技能面）。
                              部份會員透過訓練後，事業成就
                               上突破原有格局。
                              企業主雇用結訓後學員，肯定機
                               構訓練的成效。
                              部份學員能運用所學於職務中。
                              進行訓後薪資調查，部份訓後學
                               員微幅調薪。
                              其他：
                            3 分之常見參考佐證資料：
                              有量化之效益可呈現目標市場及
                               顧客價值均有一定程度提升的效
                               果。
                              相關證據顯示個人訓練後之績效
                               改善成果。
                              提出市場競爭力、營業額、工作
                               流程、成本控制或客訴率等營運
                               表現（財務面）。
                              學員訓後創業案例。
                              學員證照通過、就業率高。
                              個人產品不良件數有下降趨勢。
                              每年訓練班次、人次均持續成
                               長。
                              會員人數及會費收入均逐年增
                               加。
                              其他：
                            4 分之常見參考佐證資料：
                              經營績效中之數據呈現目標市場
                               及顧客價值均有顯著具體的提升
                               績效。
                              提出參與社會公益活動、獲頒公
                               民營單位獎項、結合學校單位產


                       8


## INTERNAL NEIGHBOR CROSSWALK
﻿requirement_id,deliverable_count,split_extra_count,deliverable_ids,document_titles
I19-E20,1,0,0131,學員證照通過與就業追蹤統計表
I19-E21,1,0,0132,個人產品不良件數與訓後改善分析表
I19-E22,1,0,0133,年度訓練班次與參訓人次趨勢表
I19-E23,1,0,0134,會員人數及會費收入逐年變化分析報告
I19-E25,1,0,0135,目標市場與顧客價值具體提升成效分析報告


## PROJECT 157 INDEX CONTEXT
144｜**考照/就業率：分母與可追溯數據**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

145｜**產品不良件數：前後比較與其他影響**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

146｜**年度班次/人次：完整多期數據**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

147｜**會員/會費：實際帳冊與敏感資料隔離**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

148｜**其他：** 未有獨特補充證據前不生成文件；狀態 BLOCKED_UNTIL_UNIQUE_OTHER_NAMED。

## I19-L4（官方 p8-9）

149｜**市場價值顯著績效：可驗證的長期數據及限制**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

150｜**公益/表揚/產學/研發社會影響：原件與來源**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

151｜**正面媒體報導：真實報導來源與截頁索引**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

152｜**個人升薪/獎勵/升遷證明：取得同意與原件**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

153｜**高考照/就業率：追蹤分母與時期**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

154｜**資訊系統普及率：定義/期間/數據**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

155｜**顧客滿意度上升：多期同量尺統計**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

156｜**三年營業額增長：真實財報合法核實**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

157｜**其他：** 未有獨特補充證據前不生成文件；狀態 BLOCKED_UNTIL_UNIQUE_OTHER_NAMED。

## 統計核對

總 checkbox：157；具名：129；其他：28。如與官方 PDF／現有權威 Registry 發生差異，必須逐格標 locator 修正，不得猜測。


## FULL TEXT EXTRACTED FROM THE CANDIDATE DOCX
年度訓練班次與參訓人次趨勢表
文件編號 0133　｜　內部 crosswalk I19-E22　｜　157 Blueprint index 146
SAMPLE / SYNTHETIC 示範版　｜　REAL 原件與機構實績：目前 UNKNOWN
30 秒摘要
本表用來逐年登錄實際辦理的訓練班次與參訓人次，讓訓練行政人員可以從年度課程清冊、班次結案及出席來源逐筆核對，並由第二位覆核者重算每一相鄰年度的兩項變化。適用時點是年度結束後完成班次結案及出席資料彙整時；主要輸出是逐班明細、年度班次與人次總數、年增量及成長率。
本示範依官方第 8 頁常見參考佐證「每年訓練班次、人次均持續成長。」設計。案例以 2023 至 2025 年為 SAMPLE / SYNTHETIC，分別列出 6/72、8/104、10/141 班次／人次。示範資料中，2024 對 2023 班次增加 33.3%、人次增加 44.4%；2025 對 2024 班次增加 25.0%、人次增加 35.6%。這些數字只驗證本表可用及可重算，不是原始點協會的實績、政策、核准或評核結果。
使用者下一步：把 SAMPLE 區逐筆替換成已授權的 REAL 年度計畫、實際開課／結班記錄和去識別簽到來源；依同一計數口徑重算。資料未齊時先標 HOLD，不得對外宣稱指標成立。
1. 官方要求與本件責任
官方參考佐證原文：「每年訓練班次、人次均持續成長。」 來源為《TTQS 查核佐證文件資料表－訓練機構版》PDF 第 8 頁的 3 分常見參考佐證資料。該資料表說明這是常見參考例，並不代表原始點協會已辦理、已核准、已有成長或已取得評核分數。

[TABLE 1]
R1: 身分欄位 | 本件核實值 | 用途及限制
R2: 文件編號 | 0133 | 142 序列內部 doc_id；不是官方方框流水號
R3: 內部要求 | I19-E22 | 142 序列 crosswalk 的識別碼；不是官方印刷序號
R4: 157 Blueprint | index 146，I19-L3 | 專案具名佐證要求的位置；官方印刷方框序號仍為 UNKNOWN
R5: 官方來源 | PDF 第 8 頁 | 常見參考佐證，不是協會個案原件
R6: 本件文類 | 年度班次與參訓人次登錄表及趨勢分析 | 同時呈現逐班來源、兩項年度總數及每年變化
R7: 本版狀態 | SAMPLE / SYNTHETIC | 目前沒有可核驗協會年度課程及出席原件；REAL_EVIDENCE=UNKNOWN
[/TABLE 1]

本件只處理年度訓練班次數及參訓人次。0132／I19-E21 處理產品不良件數與產品檢驗分母；0134／I19-E23 處理會員人數及會費收入。不得把產品品質、會員數、會費、證照或就業數據放進本件，也不得讓本表取代相鄰文件。
2. 統計口徑
2.1 年度
示範採曆年，即 1 月 1 日至 12 月 31 日。REAL 使用時須依協會實際採用且可核實的年度規則；規則固定後不得為製造成長而改變。以實際教學活動日期歸屬年度。同一班次如跨年，依實際結案規則指定一個年度，並列開課日、結訓日、歸屬理由及覆核人；不得將同一班拆成兩年各算一班。
2.2 已辦訓練班次
一個班次須有唯一班次 ID、明確課程與同一學員 cohort，且至少實際發生一次教學活動並能追到班次結案或等效出席資料。同一 cohort 的多日課程算一班；同一課程另外開班、另有獨立 cohort 和班次資料，才另算一班。排定後取消、延期而未開課、零出席、只有招生或課程計畫，均不列入已辦班次；須保留在排除清冊，說明取消、延期或未成班原因。
2.3 參訓人次
本示範採可逐筆核對的操作定義：同一「班次 ID × 去識別學員 ID」只要在該班至少出席一次，計 1 參訓人次。同一學員參加同班多日不重複計數；同一學員參加不同班次，各班各計 1 人次。全程未到者、取消報名者不計。參訓人次不是報名人數、核定名額、課程日簽到次數，也不是跨年度唯一自然人數。
這是為示範而明訂的計數方法，不能被誤寫成協會既有政策或官方另訂門檻。轉為 REAL 前，須依權責單位實際採用的統計規則；若沒有可證明的一致規則，先記錄待確認的方法與決策責任，不作正式績效結論。
2.4 年增率與「持續」判讀

[TABLE 2]
R1: 指標 | 年度淨增量 | 年增率 | 分母規則
R2: 已辦班次 | 本年班次數 − 前年班次數 | 淨增量 ÷ 前年班次數 × 100% | 前年為 0 或缺漏時列 N/A，不除以零
R3: 參訓人次 | 本年參訓人次 − 前年參訓人次 | 淨增量 ÷ 前年參訓人次 × 100% | 前年為 0 或缺漏時列 N/A，不除以零
[/TABLE 2]

要說明一段期間「每年」兩項都持續成長，每一相鄰年度的班次與人次淨增量都必須各自大於 0，並且資料口徑、期間及來源可比。只比較首尾總數，可能掩蓋中間年度下降，不能替代逐年比較。若任一年度其中一項不增或下降，須直接列出該年度，不可刪年或用另一指標抵銷。百分率以未四捨五入數值計算，表內顯示至小數 1 位；班次、人次使用整數。官方沒有規定最低成長率或統計顯著性門檻，本表不創設此類標準。
3. 來源鏈、責任與欄位字典
實務上每個年度建立一份受控班次母清冊，依序對照核定或實際課程計畫、開課及結班記錄、去識別學員名冊、逐次簽到／出席資料、年度統計表。對公開送審或跨部門共享的版本，只記受權限控管的原件位置與必要索引，不把未授權個資放進公開候選文件。

[TABLE 3]
R1: 欄位 | 定義 | REAL 來源及位置 | 登錄角色 | 核對規則
R2: 年度 | 實際辦理歸屬年度 | 課程日期、班次結案記錄 | SYN-ROLE-REG（合成角色代碼） | 同班只歸屬一年；跨年另附理由
R3: 班次 ID | 同一課程 cohort 的唯一識別碼 | 訓練班次母清冊 | SYN-ROLE-REG | 年度內不得重複；取消班仍保留 ID
R4: 課程名稱 | 可與課程計畫及結班資料對應的名稱 | 課程計畫／班次通知 | SYN-ROLE-REG | 不以文件標題代替實際課程名
R5: 實際辦理日期 | 有教學活動的日期或起訖日 | 課程紀錄、簽到資料 | SYN-ROLE-REG | 取消、延期要標出實際狀態
R6: 班次狀態 | 已辦、取消、延期、零出席、待核 | 結班資料及出席資料 | SYN-ROLE-REG | 只有符合定義的已辦班次進入年度班次數
R7: 參訓人次 | 本班至少出席一次的不同去識別學員 ID 數 | 去識別名冊及簽到資料 | SYN-ROLE-REG | 同一學員同一班去重；不得逐日相加
R8: 計數口徑／版次 | 本年度採用的參訓人次定義 | 統計作業規則或核准紀錄 | SYN-ROLE-REV（合成覆核角色） | 年度間一致；如改變，須分層或說明不可比
R9: 原件索引 | 權限控管資料位置、檔名／頁／列 | 機構受控檔案位置 | SYN-ROLE-REG | 公開版不可暴露敏感個資或秘密
R10: 覆核狀態及日期 | 第二人重算、核對和更正情況 | 覆核紀錄 | SYN-ROLE-REV | 不可把合成角色或示範日期寫成真人簽核
[/TABLE 3]

4. 每年執行 SOP

[TABLE 4]
R1: 步驟 | 執行動作 | 判斷與控制點 | 輸出
R2: 1. 鎖定年度範圍 | 列出本年度所有計畫班次，包含取消及延期 | 不以招生清單直接當成已辦班次 | 年度班次母清冊及原件索引
R3: 2. 核實辦理狀態 | 對照實際教學日期、結班或出席記錄 | 無實際教學、零出席、取消班不列入已辦數 | 狀態欄及排除原因
R4: 3. 統一班次 ID | 確認同 cohort 多日仍為同一班，不同 cohort 有不同 ID | 發現重複 ID 或班次拆分錯誤先 HOLD | 唯一班次清單
R5: 4. 建立參訓關聯 | 將簽到資料轉為「班次 × 去識別學員」關聯 | 每位學員在同班只留一筆；跨班可分別計次 | 去重後參訓人次
R6: 5. 逐班彙總 | 逐班記錄狀態、人次、來源和缺漏 | 人次不可大於可追溯有效的班次名冊數；未知先 HOLD | 逐班登錄表
R7: 6. 年度計算 | 加總已辦班次及人次，分別計算年增量與年增率 | 遇前年缺值或零分母列 N/A，不製造百分率 | 年度趨勢表及逐步算式
R8: 7. 第二人覆核 | 由非登錄者抽回母清冊及出席來源重算全數彙總 | 差異未解、來源缺頁或權限不明不得鎖版 | 覆核紀錄、差異清單
R9: 8. 更正及鎖版 | 更正時保留前值、新值、原因、來源、日期和覆核 | 不覆寫或刪除錯誤歷史；留修訂軌跡 | 定稿版本、附件索引
[/TABLE 4]

5. SAMPLE / SYNTHETIC 逐班完整示範
以下 24 筆已辦班次和 1 筆取消班均為合成記錄。課程名稱是為協會教育訓練情境設計的示例，不表示原始點協會曾開課。SYN-PLAN、SYN-ATT、SYN-CLOSE 均為虛構來源鍵，沒有對應真實原件。

[TABLE 5]
R1: 年度 | 班次 ID | 日期 | 合成課程名稱 | 狀態 | 參訓人次 | 合成來源鍵
R2: 2023 | SYN-23-01 | 2023-02-11 | 志工服務紀錄與個資保護 | 已辦 | 12 | SYN-PLAN/ATT/CLOSE-23-01
R3: 2023 | SYN-23-02 | 2023-04-15 | 活動安全與風險辨識 | 已辦 | 12 | SYN-PLAN/ATT/CLOSE-23-02
R4: 2023 | SYN-23-03 | 2023-06-10 | 社區服務溝通 | 已辦 | 12 | SYN-PLAN/ATT/CLOSE-23-03
R5: 2023 | SYN-23-04 | 2023-08-12 | 專案成果紀錄與追蹤 | 已辦 | 12 | SYN-PLAN/ATT/CLOSE-23-04
R6: 2023 | SYN-23-05 | 2023-10-14 | 志工團隊協作 | 已辦 | 12 | SYN-PLAN/ATT/CLOSE-23-05
R7: 2023 | SYN-23-06 | 2023-12-09 | 基礎行政與檔案管理 | 已辦 | 12 | SYN-PLAN/ATT/CLOSE-23-06
R8: 2024 | SYN-24-01 | 2024-02-17 | 志工服務紀錄與個資保護 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-24-01
R9: 2024 | SYN-24-02 | 2024-03-23 | 活動安全與風險辨識 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-24-02
R10: 2024 | SYN-24-03 | 2024-05-18 | 社區服務溝通 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-24-03
R11: 2024 | SYN-24-04 | 2024-06-22 | 專案成果紀錄與追蹤 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-24-04
R12: 2024 | SYN-24-05 | 2024-08-17 | 志工團隊協作 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-24-05
R13: 2024 | SYN-24-06 | 2024-09-21 | 基礎行政與檔案管理 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-24-06
R14: 2024 | SYN-24-07 | 2024-11-16 | 社區活動風險與通報 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-24-07
R15: 2024 | SYN-24-08 | 2024-12-14 | 志工排班與服務交接 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-24-08
R16: 2025 | SYN-25-01 | 2025-01-18 | 志工服務紀錄與個資保護 | 已辦 | 12 | SYN-PLAN/ATT/CLOSE-25-01
R17: 2025 | SYN-25-02 | 2025-02-22 | 活動安全與風險辨識 | 已辦 | 13 | SYN-PLAN/ATT/CLOSE-25-02
R18: 2025 | SYN-25-03 | 2025-04-12 | 社區服務溝通 | 已辦 | 14 | SYN-PLAN/ATT/CLOSE-25-03
R19: 2025 | SYN-25-04 | 2025-05-17 | 專案成果紀錄與追蹤 | 已辦 | 14 | SYN-PLAN/ATT/CLOSE-25-04
R20: 2025 | SYN-25-05 | 2025-06-21 | 志工團隊協作 | 已辦 | 14 | SYN-PLAN/ATT/CLOSE-25-05
R21: 2025 | SYN-25-06 | 2025-07-19 | 基礎行政與檔案管理 | 已辦 | 14 | SYN-PLAN/ATT/CLOSE-25-06
R22: 2025 | SYN-25-07 | 2025-08-23 | 社區活動風險與通報 | 已辦 | 15 | SYN-PLAN/ATT/CLOSE-25-07
R23: 2025 | SYN-25-08 | 2025-09-20 | 志工排班與服務交接 | 已辦 | 15 | SYN-PLAN/ATT/CLOSE-25-08
R24: 2025 | SYN-25-09 | 2025-10-18 | 志工團隊協作實務 | 已辦 | 15 | SYN-PLAN/ATT/CLOSE-25-09
R25: 2025 | SYN-25-10 | 2025-12-06 | 專案成果紀錄與追蹤實務 | 已辦 | 15 | SYN-PLAN/ATT/CLOSE-25-10
R26: 2025 | SYN-25-X01 | 2025-11-22 | 志工排班與服務交接（取消例） | 取消 | 0 | SYN-PLAN-25-X01
[/TABLE 5]

核對：2023 年 6 班、72 人次；2024 年 8 班、104 人次；2025 年 10 班、141 人次。2025 年另有 1 班排定後取消，列入例外紀錄而不計班次或人次。三年已辦班次總計 24；參訓人次共 317。這些值全為 SYNTHETIC。
6. 年度趨勢及可重算計算
已辦班次年度序列

[TABLE 6]
R1: 年度 | 已辦班次 | 前年班次 | 淨增量 | 年增率 | 可比性判讀
R2: 2023 | 6 | N/A | N/A | N/A | 示範基期
R3: 2024 | 8 | 6 | +2 | 33.3% | 較前年增加
R4: 2025 | 10 | 8 | +2 | 25.0% | 較前年增加
[/TABLE 6]

參訓人次年度序列

[TABLE 7]
R1: 年度 | 參訓人次 | 前年人次 | 淨增量 | 年增率 | 可比性判讀
R2: 2023 | 72 | N/A | N/A | N/A | 示範基期
R3: 2024 | 104 | 72 | +32 | 44.4% | 較前年增加
R4: 2025 | 141 | 104 | +37 | 35.6% | 較前年增加
[/TABLE 7]

逐年年增率算式核對

[TABLE 8]
R1: 比較與指標 | 代入算式及結果
R2: 2024 對 2023 班次 | (8−6)÷6×100%=33.3%
R3: 2025 對 2024 班次 | (10−8)÷8×100%=25.0%
R4: 2024 對 2023 參訓人次 | (104−72)÷72×100%=44.4%
R5: 2025 對 2024 參訓人次 | (141−104)÷104×100%=35.6%
[/TABLE 8]

逐年結論：在這組合成資料中，2024 相較 2023 的班次與人次均增加；2025 相較 2024 亦均增加。因此，示範計算符合「每個相鄰年度的兩項數值都有增加」這項表格檢查。這只是 SAMPLE 驗算，不是協會實績或官方評定。
補充首尾計算：2025 對 2023 班次增幅=(10−6)÷6×100=66.7%；參訓人次增幅=(141−72)÷72×100=95.8%。首尾結果必須與逐年變化並列，不可用來遮蔽中間年度下降。班次年增率兩次分別為 33.3%、25.0%；人次年增率分別為 44.4%、35.6%。數值先以原始整數計算，最後才四捨五入至小數一位。
趨勢圖讀法
班次樣例序列為 6 → 8 → 10；參訓人次樣例序列為 72 → 104 → 141。兩序列使用不同單位，不能共用未標示單位的單一縱軸。逐年向上只描述這組 SAMPLE 數字；沒有真實課程清冊及出席證據前，不得據此說明協會成長或原因。
7. 為什麼數量口徑不能混用

[TABLE 9]
R1: 常見混淆 | 錯誤結果 | 正確處理
R2: 把同一班三日課程記成三班 | 班次被放大 | 同 cohort、同班次 ID 多日只計 1 班
R3: 把每一日簽到人數相加 | 人次被放大 | 依班次 ID × 去識別學員 ID 去重；每班每人最多 1 人次
R4: 把報名數當參訓人次 | 缺席者仍被算入 | 以至少一次可核實出席作為本示範定義；REAL 須依一致政策
R5: 把取消班次當已辦 | 班次與人次不實增加 | 取消、延期未開課及零出席另列，不進年度已辦數
R6: 只比較 2023 與 2025 | 可能掩蓋中間年度下降 | 逐列檢查每個相鄰年度、兩個指標各自變化
R7: 把不同統計口徑拼接 | 表面趨勢不可比 | 口徑變更時重算可比期間、分層或標 HOLD，不混列
[/TABLE 9]

全合成去重示例（不併入前述年度總計）：SYN-LEARNER-014 在 SYN-CLASS-A 的兩個上課日均簽到，仍只計該班 1 人次；若又參加不同的 SYN-CLASS-B，第二班再計 1 人次。這是「人次」而非兩個不同自然人。範例學員代碼及班次代碼都是合成，不代表真人或已發生課程。
8. 例外、差異更正及覆核

[TABLE 10]
R1: 例外 ID | 合成錯誤或情境 | HOLD / REJECT 判斷 | 更正操作及留痕
R2: SYN-EX-01 | 20筆日簽到誤當人次，去重為11 | REJECT 20 作為人次；先 HOLD 等來源核對 | 以「班次×去識別學員」重算 11；保存舊值20、新值11、來源鍵、原因與第二人覆核
R3: SYN-EX-02 | 排定的 SYN-25-X01 後來取消 | 不得計已辦班次或參訓人次 | 母清冊保留取消狀態、日期和來源位置；年度彙總排除
R4: SYN-EX-03 | 結班表有12人、簽到證據只能核實10人 | HOLD，不採較高數字 | 查缺漏或更正結班表；未能對齊前年度人次標未知，不自行填補
R5: SYN-EX-04 | 2024以報名數計人次，2025改用實際出席 | HOLD，不直接比較 | 找回兩年原始資料按同一規則重算；若不可重算，說明不可比並停止持續成長結論
[/TABLE 10]

更正記錄範例鍵 SYN-0133-CORR-01：因合成示範把同班兩日簽到筆數誤當人次，登錄角色 SYN-ROLE-REG 將示範值20更正為11個去重學員班次關聯；第二覆核角色 SYN-ROLE-REV 對照合成名冊重算。這個更正只演示留痕方式，沒有真人、協會原件或實際簽核。
正式作業的更正紀錄須含：原版本、修正版本、受影響年度/班次、原因、支持原件及位置、登錄角色、覆核角色、日期、彙總重算差額、是否更正已發布版本。不得無痕覆寫。
9. 可複製的年度登錄表
以下欄位供實際行政作業使用，尚未填入任何 REAL 資料。正式填寫時，每一筆都要連到有權限的原件位置；若原件不存在或未獲使用授權，寫 UNKNOWN/HOLD，不得把空白解讀為已完成。
班次與參訓登錄

[TABLE 11]
R1: 年度 | 班次 ID | 課程名稱 | 開課/結訓日期 | 狀態 | 參訓人次 | 計畫/結班來源位置
R2: 待補 | 未填 | 未填 | 未填 | 未核實 | 未核實 | 未取得
[/TABLE 11]


[TABLE 12]
R1: 班次 ID | 統計口徑版次 | 名冊/簽到來源位置 | 登錄角色 | 覆核角色 | 差異/更正索引 | 來源完整度
R2: 待補 | 未確認 | 未取得 | 未取得 | 未取得 | 未取得 | UNKNOWN
[/TABLE 12]

年度班次彙總

[TABLE 13]
R1: 年度 | 已辦班次 | 前年班次 | 淨增量 | 年增率 | 來源完整度 | 複核結論
R2: 待補 | 未取得 | 未取得 | N/A | N/A | UNKNOWN | HOLD
[/TABLE 13]

年度參訓人次彙總

[TABLE 14]
R1: 年度 | 參訓人次 | 前年人次 | 淨增量 | 年增率 | 口徑一致 | 複核結論
R2: 待補 | 未取得 | 未取得 | N/A | N/A | UNKNOWN | HOLD
[/TABLE 14]

REAL 原件替換區目前未填且未取得資料，這不代表已完成。取得 REAL 來源後，先逐班登錄，再分別彙總班次與人次；不得直接將 SYNTHETIC 數值換標籤。
10. SAMPLE / SYNTHETIC 逐事實替換簿
下表是候選資料的替換清冊；同一班次鍵下的課程、日期、狀態、人次及合成來源鍵均屬 SYNTHETIC。換成 REAL 時須把每列指向受權限保護的真實訓練計畫、班次辦理/結班資料及去識別出席名冊/簽到；對外公開前再檢查個資及第三方授權。

[TABLE 15]
R1: 合成鍵 | 文件位置 | 合成事實組 | 換成 REAL 必要來源
R2: SYN-23-01 | §5/p4; §10/p9 | 年度、ID、日期、課名、已辦、12人次、PLAN/ATT/CLOSE鍵 | 課程計畫、實際日期/結班、去識別名冊與簽到
R3: SYN-23-02 | §5/p4; §10/p9 | 同欄位組、12人次 | 同上，對應唯一班次
R4: SYN-23-03 | §5/p4; §10/p9 | 同欄位組、12人次 | 同上，對應唯一班次
R5: SYN-23-04 | §5/p4; §10/p9 | 同欄位組、12人次 | 同上，對應唯一班次
R6: SYN-23-05 | §5/p4; §10/p9 | 同欄位組、12人次 | 同上，對應唯一班次
R7: SYN-23-06 | §5/p4; §10/p9 | 同欄位組、12人次 | 同上，對應唯一班次
R8: SYN-24-01 | §5/p4; §10/p9 | 年度、ID、日期、課名、已辦、13人次、PLAN/ATT/CLOSE鍵 | 課程計畫、實際日期/結班、去識別名冊與簽到
R9: SYN-24-02 | §5/p4; §10/p9 | 同欄位組、13人次 | 同上，對應唯一班次
R10: SYN-24-03 | §5/p4; §10/p9 | 同欄位組、13人次 | 同上，對應唯一班次
R11: SYN-24-04 | §5/p4; §10/p9 | 同欄位組、13人次 | 同上，對應唯一班次
R12: SYN-24-05 | §5/p4; §10/p9 | 同欄位組、13人次 | 同上，對應唯一班次
R13: SYN-24-06 | §5/p5; §10/p9 | 同欄位組、13人次 | 同上，對應唯一班次
R14: SYN-24-07 | §5/p5; §10/p9 | 同欄位組、13人次 | 同上，對應唯一班次
R15: SYN-24-08 | §5/p5; §10/p10 | 同欄位組、13人次 | 同上，對應唯一班次
R16: SYN-25-01 | §5/p5; §10/p10 | 年度、ID、日期、課名、已辦、12人次、PLAN/ATT/CLOSE鍵 | 課程計畫、實際日期/結班、去識別名冊與簽到
R17: SYN-25-02 | §5/p5; §10/p10 | 同欄位組、13人次 | 同上，對應唯一班次
R18: SYN-25-03 | §5/p5; §10/p10 | 同欄位組、14人次 | 同上，對應唯一班次
R19: SYN-25-04 | §5/p5; §10/p10 | 同欄位組、14人次 | 同上，對應唯一班次
R20: SYN-25-05 | §5/p5; §10/p10 | 同欄位組、14人次 | 同上，對應唯一班次
R21: SYN-25-06 | §5/p5; §10/p10 | 同欄位組、14人次 | 同上，對應唯一班次
R22: SYN-25-07 | §5/p5; §10/p10 | 同欄位組、15人次 | 同上，對應唯一班次
R23: SYN-25-08 | §5/p5; §10/p10 | 同欄位組、15人次 | 同上，對應唯一班次
R24: SYN-25-09 | §5/p5; §10/p10 | 同欄位組、15人次 | 同上，對應唯一班次
R25: SYN-25-10 | §5/p5; §10/p10 | 同欄位組、15人次 | 同上，對應唯一班次
R26: SYN-25-X01 | §5/p5; §8/p8; §10/p10 | 取消日期/班次/課名/0人次及排除判斷 | 計畫版本、取消通知或系統狀態、確認無實際教學及出席
R27: SYN-DERIVED-01 | §6/p6; §10/p10 | 6/72、8/104、10/141與24班/317人次 | 從核實後逐班 REAL 明細重新加總，不得直接換數
R28: SYN-RATE-01 | §6/p6; §10/p10 | 33.3%、44.4%、25.0%、35.6%、首尾66.7%及95.8% | 由 REAL 未四捨五入總數重算並記錄公式
R29: SYN-ROLE-01 | §3/p3; §8/p8; §10/p10 | 登錄角色、覆核角色、示例更正責任 | 由實際授權職務或角色代碼及真實覆核記錄替換；不得補造簽名
R30: SYN-EX-01 | §8/p8; §10/p10 | 20筆日簽到誤當人次，去重為11 | REAL需原始簽到及去識別學員×班次清單；示例不併年度數
[/TABLE 15]

11. HOLD、REJECT 及對外使用門檻

[TABLE 16]
R1: 狀態 | 條件 | 可做的事 | 禁止的結論
R2: READY | 班次、日期、狀態、名冊、簽到和計數方法均有可核原件；期間可比；第二人可重算 | 形成有證據的年度比較 | 不得把數值提高成官方評分或因果結論
R3: HOLD | 只有報名或彙總；缺年度或來源；名冊與簽到不一致；班次狀態/跨年歸屬不明；政策改變未重算；重複可能未排除 | 補資料、去識別、重算及記錄差異 | 不得對外稱每年兩項持續成長
R4: REJECT | 把課程日數當班次、逐日簽到當人次、取消班計入、以首尾掩蓋年度下降、公式錯誤或 SAMPLE 被冒充 REAL | 保留錯誤記錄並按更正程序重做該列 | 不得使用該值進年度結論
[/TABLE 16]

目前原始點協會 REAL 資料、統計政策、覆核簽核及正式接受皆為 UNKNOWN；本候選只通過示範資料的內容及算式檢查。沒有官方成長率最低門檻，不能另造「合格百分比」。
12. 負向鄰項與來源索引

[TABLE 17]
R1: 文件 | 專屬問題 | 本件如何排除錯件
R2: 0132／I19-E21 | 個人產品不良件數及訓後改善 | 不含產品、缺陷、受檢單位或不良率分子分母
R3: 0134／I19-E23 | 會員人數及會費收入年度變化 | 不含會員名冊、會費帳冊或收入數字
R4: 0133／I19-E22 | 每年訓練班次、人次均持續成長 | 逐班狀態、班次去重、班次×學員去重、雙年度序列及相鄰年度計算
[/TABLE 17]


[TABLE 18]
R1: 來源 | 定位 | 本件使用方式
R2: TTQS 查核佐證文件資料表－訓練機構版 | PDF p.8 | 官方原句及常見參考佐證定位
R3: 157 CHECKBOX BLUEPRINTS | index146，I19-L3 | 專案具名需求：年度班次/人次完整多期數據
R4: 142 crosswalk | I19-E22 → 0133 | 內部 ID 對應；不等於官方流水號
R5: 142 詳細 Blueprint | deliverable_id 0133 | 文件文類、可用性、替換簿及鄰項驗收細節
[/TABLE 18]

