# OpenCode v2 writer task — DOCX 0067 R01

Project TTQS_ONE. Return exactly one complete, polished Traditional Chinese body Markdown artifact for `0067_R01_body.md`; do not return a plan, review report, code, source digest, or extra files. The caller will save the raw response and deterministically build the DOCX.

## Authority and bindings

- Exact target: DOCX 0067, I15-E03, official checkbox 073, official evidence-table page 5, document title 「訓練執行評估指標分析及相關統計分析_分析報告」.
- Read the complete appended Unique Blueprint, official source excerpt, dataset, replacement register and cross-document facts below. They are the only fact source for the body. No web search or invented facts.
- The old parked body/candidate is forbidden as a writing template. The prior failures list is a rejection checklist only.
- Every displayed person/count/date/course/budget/target is SAMPLE/SYNTHETIC. Do not claim association approval, execution, signature, real survey, actual participants, actual expenditure, policy or performance. No personal names.

## Deliverable requirements

Write a genuinely usable multi-cohort statistical analysis report, not an empty form or generic how-to. It must include a front-page 30-second guide; official requirement and genre fit; scope and limits; named metrics with numerator/denominator/period/unit/source; a complete filled table for all three cohorts and linked input fact IDs; denominator-flow reconciliations; individual and weighted aggregate formulas/calculations; trend and group differences; sample-threshold comparison; transparent small-sample and data-quality limitations; actionable SAMPLE recommendations marked NOT APPROVED; real-source replacement checklist; explicit HOLD/REJECT conditions; and the complete 49-row synthetic replacement register as an appendix.

Use the supplied numbers exactly. Recalculate them independently. Distinguish `valid assessment`, `pass`, `no valid assessment`, `survey valid`, `positive (4 or 5)` and `registered/attended/completed`. Do not count missing assessment as fail. Keep denominator definitions consistent with DOCX 0066 R01 where values are reused. Show the weighted 24/30=80.0% pass rate separately from the unweighted mean of class rates 79.6%; show the TWD 370 net underspend without hiding C3's 4.0% overrun. Label all sample benchmarks as unapproved demonstration thresholds.

Include a direct distinction from 0066 single-class closure and 0068 improvement follow-up. The title-blind body must still clearly be a cross-class/period KPI analysis report. Use plain Taiwan Traditional Chinese; no internal paths, hashes, CLI/model names, JSON keys, queue terms, source-control metadata or engineering jargon in the body. No blank fill-in table may stand in for the complete sample case.

Aim for 7,000–9,000 Chinese characters including the appendix; use clear headings and readable tables. Return raw Markdown only, no code fence or preamble. If an input contradiction prevents correct writing, return `BLOCKED:` followed by exact conflicting fact IDs; do not silently fix the data.

---

# Official requirement and source context

# DOCX 0067｜正式需求來源對照

- 專案：TTQS ONE；狀態：CANDIDATE／SAMPLE SYNTHETIC，尚未獲協會正式接受。
- doc_id：0067；requirement_id：I15-E03；官方方框流水號：073。
- 官方《TTQS 查核佐證文件資料表—訓練機構版》PDF SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；PDF 實體第 5 頁，印刷頁 5。
- 官方條目原文：**「訓練執行評估指標分析及相關統計分析。」**
- 官方指標脈絡：指標 15「評估報告及定期性綜合分析」，佐證清單包含訓練執行評估指標分析及相關統計分析。
- 當前 157 方框 Blueprint 來源：`docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md` blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`；第 181 行之方框 073：**執行 KPI 統計：分母/分組/期間/來源/差距**。該行要求特定來源定位、核心正文/示範、決策或結果及跨文件連結。
- 142 交付 Crosswalk R01（歷史來源，非當前 Human 正式接受）：來源 SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`；I15-E03 對應一份 deliverable 0067，名稱為「訓練執行評估指標分析及相關統計分析_分析報告」。該對應已於 2026-10-19 以當前官方 PDF 與 157 Blueprint row 073 重核。
- 文類：跨班／跨期間執行 KPI 統計分析報告；與單班完整結案報告、課後改善追蹤分開。

## 官方 PDF 第 5 頁節錄

查核（Review）—15. 評估報告及定期性綜合分析。
常見參考佐證資料：訓練執行評估指標分析及相關統計分析。

來源 PDF 已在本 PR 分支 `quality-review/0064_R06/official_source.pdf` 存檔；本工作不複製或修改原 PDF。


# Unique Blueprint

# UNIQUE BLUEPRINT｜DOCX 0067 R01

## A. 身分與文類

- project_id: TTQS_ONE
- doc_id: **0067**
- requirement_id: **I15-E03**
- official_checkbox_serial: **073**
- 官方要求：「訓練執行評估指標分析及相關統計分析。」
- 專屬文類：**跨班／跨期間訓練執行 KPI 統計分析報告**。它必須能比較分組、期間、分母、來源和差距，不能換標題後充作單班結案報告、課程設計會議或改善追蹤單。
- 主要讀者：訓練承辦人、資料覆核者、主管及評核閱讀者。
- 使用時點：一個分析期的資料收集與覆核完成後；本範例只演示 2026/08–10 三個合成班次，不宣稱協會實際採行此週期。
- 證據狀態：全篇 SAMPLE／SYNTHETIC。沒有真實協會紀錄、核准目標、實際班次、簽章或正式決議；REAL 一律 UNKNOWN／HOLD。

## B. 官方要求邊界與相鄰錯件排除

1. 0066（I15-E02／方框 072）是單班完整結案報告；0067 只做跨班／跨期統計，引用 0066 的一個合成班次不得把單班當成年度績效。
2. 0068（I15-E04／方框 074）是改善追蹤；0067 可指出統計差距與提出「待核定」建議，不能冒充後續改善紀錄或有效性驗證。
3. 0065（I15-E01／方框 071）為單項訓練執行評估紀錄；0067 不複製其單件正文。
4. 正文遮住標題後，仍須由班次分組、期間趨勢、分母橋接及 KPI 差異辨認為統計分析報告。

## C. 讀者可直接操作的核心問題

- 這一期納入幾個班次？每班名冊、到課、完成、有效評量、問卷及費用的原始來源在哪裡？
- 分母代表誰、哪一期間、什麼排除條件？缺一欄時如何標 N/A／HOLD？
- 哪些指標達到「本次示範門檻」、哪些落差需要補查？加權總率和班級平均為何不同？
- 使用者如何把真實名冊、簽到、測驗、問卷、核定預算與憑證替換進來，並重新計算？

## D. 必備章節（不得用空表或未來式代替）

1. 首頁 30 秒導讀：文件用途、doc_id/I15-E03/073、誰用／何時用、數據在何處、SAMPLE/REAL 界線。
2. 本次合成分析範圍、期間、單位與不可推論事項。
3. 指標字典：報名、到課、完成（至少 5 小時的合成門檻）、有效評量、達標、問卷有效、正向（4/5 分）、計畫預算、合成支出。
4. 資料收集與納入程序：班次建立→原始資料取件→去識別→逐筆校驗→覆核→彙整→分析；角色只能寫「待協會依實際授權指定」的通用功能，不捏造現職人員。
5. 完整的三班合成原始資料表，附各輸入 fact_id。
6. 分母流向橋接：登錄→到課/缺席→完成/未完成；到課→有效/無效或缺評量；問卷發出→有效/排除；所有恆等式要相等。
7. KPI 定義、各班率、跨班加權率、班級率的簡單平均、期間趨勢、示範門檻和差距。
8. 評量成績差異與費用差異的計算示例；避免由小樣本推因果。
9. 合成結果解讀：差距、限制、優先核對項目與 SAMPLE 建議，不寫成協會已決議。
10. 偏誤、缺漏、重複及 N/A 處理；明確列出拒收/HOLD 條件。
11. 真實資料替換作業清單：原件、欄位、責任角色（由協會指定）、覆核方式及缺件狀態。
12. 完整 49 筆 SAMPLE/SYNTHETIC 替換清冊附錄，逐筆對應 fact_id、正文位置、原件替換路徑及狀態。
13. 與 0066、0068 的文件責任界線與證據索引。

## E. 公式及逐步計算（百分比四捨五入至 1 位；金額保留元、單位新臺幣）

| KPI | 定義／分母 | 全體原始值 | 預期值 |
|---|---|---:|---:|
| 到課率 | 到課／登錄 | 32／37 | 86.5% |
| 完成率（登錄口徑） | 達至少 5 小時完成／登錄 | 30／37 | 81.1% |
| 到課者完成率 | 完成／到課 | 30／32 | 93.8% |
| 評量覆蓋率 | 有效評量／到課 | 30／32 | 93.8% |
| 評量達標率 | 達標／有效評量 | 24／30 | 80.0% |
| 問卷有效回收率 | 有效問卷／發出問卷 | 30／32 | 93.8% |
| 問卷正向率 | 4/5 分正向數／有效問卷 | 26／30 | 86.7% |
| 預算使用率 | 合成支出／合成計畫 | 24,630／25,000 | 98.5% |

逐班資料：C1＝12 登錄、10 到課、10 完成、9 有效評量/8 達標、10 發出/9 有效問卷/8 正向、計畫 8,000／支出 7,650（引用 0066 R01 SAMPLE）；C2＝15/13/12/12/10/13/12/10、10,000/9,700；C3＝10/9/8/9/6/9/9/8、7,000/7,280。C2/C3 全為本工作新增合成案例。

- 跨班達標率（加權）= (8+10+6)/(9+12+9)=24/30=80.0%。
- 班級達標率平均=(8/9+10/12+6/9)/3=79.6296…%=79.6%。兩者差約 0.4 個百分點，不能互換。
- 班級支出差額：C1 7,650−8,000=−350；C2 9,700−10,000=−300；C3 7,280−7,000=+280；合計 −370。
- 整體使用率=24,630/25,000=98.52%≈98.5%，但 C3 單班 7,280/7,000=104.0%；整體未超支不能遮蔽單班超支。
- 分母為 0 → N/A 並寫原因；缺原始來源、計算不平或欄位衝突 → HOLD，不得補猜。

## F. 固定合成數據與逐事實替換清冊

本 Blueprint 的唯一數據來源是 `SYNTHETIC_DATASET_R01.csv`；49 個輸入／目標事實的識別碼都在 `SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`。文件不得新增未登錄姓名、日期、數字、授權、正式決議或外部來源。派生 KPI 可計算，但須列公式、分子、分母並回連輸入 fact_id。

## G. 本次示範門檻（不是協會已核定標準）

到課率 ≥85%；登錄口徑完成率 ≥80%；評量覆蓋率 ≥95%；評量達標率 ≥80%；問卷有效回收率 ≥90%；問卷正向率 ≥85%；合成預算使用率 ≤100%。門檻均標示「示範用、未核定」，只為練習差距判讀；不能寫成協會政策或官方門檻。

## H. 驗收／拒收／HOLD

- 任一分子大於分母、登錄不等於到課＋缺席、有效評量超過到課、問卷有效超過發出 → REJECT，先對帳。
- 成績「未達標」不能吞併「沒有有效評量」；兩者分列。
- 門檻、問卷量尺或期間在班次間不同且不可換算 → 不合併，標 N/A/HOLD 並分組呈現。
- 只有彙總百分比、沒有來源欄位/樣本數/分母/期間 → REJECT。
- 任何 SAMPLE 資料被當成 REAL、將建議寫成正式決議、或把 0066 單班當成年績效 → REJECT。
- 缺真實原件時，文件仍可作完整 SAMPLE 示範，但 REAL/正式成效為 UNKNOWN/HOLD；不偽造簽章、出席、核准或憑證。

## I. 替換為 REAL 的最低來源清單

逐班取得合法可核實的正式課程與日期、名冊/報名、簽到或時數、完成門檻、原始評量與量規、問卷原始回覆、經核定預算、支出明細及合法憑證；確認資料權限與去識別。未取得不得把演示數字改名為實績。


# Cross-document facts

# Cross-document facts｜0067 R01

- Upstream candidate: DOCX 0066 R01 / I15-E02 / official checkbox 072; exact candidate SHA-256 `c9ec333f27c967eb5bbd28c49f3c54d218783cd659feec936ba9c0c566d1f8d6`.
- Shared SAMPLE case: `SYN-0060-2026-A01`, course 「社區志工接待與資源轉介界線」, sample date 2026-08-15. 0066 R01 data: registered 12, attended 10, completed 10 (sample threshold 5 hours), valid assessment 9, passed 8, questionnaires issued 10/valid 9/positive 8 (positive = 4 or 5), planned budget TWD 8,000, sample spend TWD 7,650.
- These values are copied only as the same SAMPLE cohort to keep cross-document facts aligned. DOCX 0066 itself labels its records synthetic and does not establish real Association execution.
- C2 and C3 are new independent SAMPLE/SYNTHETIC cohorts created only for this analysis. No names or real learner records.
- 0067’s responsibility is across-cohort denominator, period, grouping, rate, variance and data-quality analysis. It must not rewrite 0066 or claim this three-cohort sample is annual/real performance.
- 0068/I15-E04/074 is a different improvement-follow-up requirement. 0067 may provide sample recommendations only; it cannot claim follow-up execution or effectiveness.
- Input fact registry: 49 rows, fact IDs `SYN-0067-R01-F001` through `...F049`. Derived rates are not invented facts; every output has a formula and trace back to the inputs.


# Fixed dataset CSV

```csv
cohort_id,case_id,course_name,course_date,registrants,attendees,completers,completion_threshold_hours,valid_assessments,passes,survey_issued,survey_valid,positive_responses,planned_budget_twd,actual_spend_twd,source_class,input_fact_id_range,evidence_state
C1,SYN-0060-2026-A01,社區志工接待與資源轉介界線,2026-08-15,12,10,10,5,9,8,10,9,8,8000,7650,CROSS_DOCUMENT_SAMPLE_0066_R01,F001-F014,SAMPLE_SYNTHETIC
C2,SYN-0067-2026-B01,志工危機辨識與轉介實務（示範班）,2026-09-12,15,13,12,5,12,10,13,12,10,10000,9700,NEW_SYNTHETIC_FOR_0067,F015-F028,SAMPLE_SYNTHETIC
C3,SYN-0067-2026-C01,社區關懷訪視安全與紀錄（示範班）,2026-10-10,10,9,8,5,9,6,9,9,8,7000,7280,NEW_SYNTHETIC_FOR_0067,F029-F042,SAMPLE_SYNTHETIC
```

# Complete 49-row replacement register CSV

```csv
fact_id,cohort_id,field,value,unit,locator,source_to_replace,why_synthetic,status
SYN-0067-R01-F001,C1,case_id,SYN-0060-2026-A01,合成班次代碼,0066 R01 DOCX 首頁案例編號,0066 R01 candidate SAMPLE; replace with authorized real source: 真實班次/課程主檔及授權編碼,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F002,C1,course_name,社區志工接待與資源轉介界線,文字,0066 R01 DOCX 首頁課名,0066 R01 candidate SAMPLE; replace with authorized real source: 正式課程計畫,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F003,C1,course_date,2026-08-15,YYYY-MM-DD,0066 R01 DOCX 首頁演練日期,0066 R01 candidate SAMPLE; replace with authorized real source: 正式開課紀錄/簽到原件,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F004,C1,registrants,12,人,0066 R01 摘要表：報名／到課／缺席,0066 R01 candidate SAMPLE; replace with authorized real source: 合法名冊/報名原始檔,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F005,C1,attendees,10,人,同上,0066 R01 candidate SAMPLE; replace with authorized real source: 簽到/出缺勤原件,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F006,C1,completers,10,人,0066 R01 完成數表及 5 小時合成門檻,0066 R01 candidate SAMPLE; replace with authorized real source: 出席時數與完成規則原件,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F007,C1,completion_threshold_hours,5,小時,0066 R01 完成數表/門檻註記,0066 R01 candidate SAMPLE; replace with authorized real source: 核定課程規則/出席時數,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F008,C1,valid_assessments,9,份/人,0066 R01 評量橋接：有效 9,0066 R01 candidate SAMPLE; replace with authorized real source: 原始評量及有效性規則,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F009,C1,passes,8,人,0066 R01 評量橋接：達標 8,0066 R01 candidate SAMPLE; replace with authorized real source: 核定量規與原始評分,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F010,C1,survey_issued,10,份,0066 R01 問卷摘要：發出 10,0066 R01 candidate SAMPLE; replace with authorized real source: 發放紀錄,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F011,C1,survey_valid,9,份,0066 R01 問卷摘要：有效 9,0066 R01 candidate SAMPLE; replace with authorized real source: 匿名原始問卷及排除規則,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F012,C1,positive_responses,8,份,0066 R01 問卷正向：4/5 分 8,0066 R01 candidate SAMPLE; replace with authorized real source: 問卷原始答卷與量尺,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F013,C1,planned_budget_twd,8000,TWD,"0066 R01 財務合計：合成計畫 8,000",0066 R01 candidate SAMPLE; replace with authorized real source: 核定預算原件,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F014,C1,actual_spend_twd,7650,TWD,"0066 R01 財務合計：合成支出 7,650",0066 R01 candidate SAMPLE; replace with authorized real source: 帳務明細與合法憑證,從 0066 R01 的 SAMPLE/SYNTHETIC 單班案例引用作為 C1；來源本身不是 REAL，不得當作協會已辦訓紀錄。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F015,C2,case_id,SYN-0067-2026-B01,合成班次代碼,0067_R01 合成資料 C2 欄位 case_id,No real record provided; obtain authorized original: 真實班次/課程主檔及授權編碼,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F016,C2,course_name,志工危機辨識與轉介實務（示範班）,文字,0067_R01 合成資料 C2 欄位 course_name,No real record provided; obtain authorized original: 正式課程計畫,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F017,C2,course_date,2026-09-12,YYYY-MM-DD,0067_R01 合成資料 C2 欄位 course_date,No real record provided; obtain authorized original: 正式開課紀錄/簽到原件,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F018,C2,registrants,15,人,0067_R01 合成資料 C2 欄位 registrants,No real record provided; obtain authorized original: 合法名冊/報名原始檔,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F019,C2,attendees,13,人,0067_R01 合成資料 C2 欄位 attendees,No real record provided; obtain authorized original: 簽到/出缺勤原件,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F020,C2,completers,12,人,0067_R01 合成資料 C2 欄位 completers,No real record provided; obtain authorized original: 出席時數與完成規則原件,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F021,C2,completion_threshold_hours,5,小時,0067_R01 合成資料 C2 欄位 completion_threshold_hours,No real record provided; obtain authorized original: 核定課程規則/出席時數,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F022,C2,valid_assessments,12,份/人,0067_R01 合成資料 C2 欄位 valid_assessments,No real record provided; obtain authorized original: 原始評量及有效性規則,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F023,C2,passes,10,人,0067_R01 合成資料 C2 欄位 passes,No real record provided; obtain authorized original: 核定量規與原始評分,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F024,C2,survey_issued,13,份,0067_R01 合成資料 C2 欄位 survey_issued,No real record provided; obtain authorized original: 發放紀錄,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F025,C2,survey_valid,12,份,0067_R01 合成資料 C2 欄位 survey_valid,No real record provided; obtain authorized original: 匿名原始問卷及排除規則,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F026,C2,positive_responses,10,份,0067_R01 合成資料 C2 欄位 positive_responses,No real record provided; obtain authorized original: 問卷原始答卷與量尺,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F027,C2,planned_budget_twd,10000,TWD,0067_R01 合成資料 C2 欄位 planned_budget_twd,No real record provided; obtain authorized original: 核定預算原件,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F028,C2,actual_spend_twd,9700,TWD,0067_R01 合成資料 C2 欄位 actual_spend_twd,No real record provided; obtain authorized original: 帳務明細與合法憑證,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F029,C3,case_id,SYN-0067-2026-C01,合成班次代碼,0067_R01 合成資料 C3 欄位 case_id,No real record provided; obtain authorized original: 真實班次/課程主檔及授權編碼,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F030,C3,course_name,社區關懷訪視安全與紀錄（示範班）,文字,0067_R01 合成資料 C3 欄位 course_name,No real record provided; obtain authorized original: 正式課程計畫,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F031,C3,course_date,2026-10-10,YYYY-MM-DD,0067_R01 合成資料 C3 欄位 course_date,No real record provided; obtain authorized original: 正式開課紀錄/簽到原件,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F032,C3,registrants,10,人,0067_R01 合成資料 C3 欄位 registrants,No real record provided; obtain authorized original: 合法名冊/報名原始檔,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F033,C3,attendees,9,人,0067_R01 合成資料 C3 欄位 attendees,No real record provided; obtain authorized original: 簽到/出缺勤原件,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F034,C3,completers,8,人,0067_R01 合成資料 C3 欄位 completers,No real record provided; obtain authorized original: 出席時數與完成規則原件,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F035,C3,completion_threshold_hours,5,小時,0067_R01 合成資料 C3 欄位 completion_threshold_hours,No real record provided; obtain authorized original: 核定課程規則/出席時數,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F036,C3,valid_assessments,9,份/人,0067_R01 合成資料 C3 欄位 valid_assessments,No real record provided; obtain authorized original: 原始評量及有效性規則,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F037,C3,passes,6,人,0067_R01 合成資料 C3 欄位 passes,No real record provided; obtain authorized original: 核定量規與原始評分,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F038,C3,survey_issued,9,份,0067_R01 合成資料 C3 欄位 survey_issued,No real record provided; obtain authorized original: 發放紀錄,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F039,C3,survey_valid,9,份,0067_R01 合成資料 C3 欄位 survey_valid,No real record provided; obtain authorized original: 匿名原始問卷及排除規則,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F040,C3,positive_responses,8,份,0067_R01 合成資料 C3 欄位 positive_responses,No real record provided; obtain authorized original: 問卷原始答卷與量尺,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F041,C3,planned_budget_twd,7000,TWD,0067_R01 合成資料 C3 欄位 planned_budget_twd,No real record provided; obtain authorized original: 核定預算原件,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F042,C3,actual_spend_twd,7280,TWD,0067_R01 合成資料 C3 欄位 actual_spend_twd,No real record provided; obtain authorized original: 帳務明細與合法憑證,為說明跨班統計而明確建立的合成示例值，非協會實際班次、帳務或成效。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F043,ALL,attendance_rate_target,85,%,0067_R01 示範差距判讀門檻表,Replace only if the Association supplies an authorized approved KPI threshold; otherwise leave explicitly as a sample benchmark.,示範分析用假設，沒有協會核准或官方效力。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F044,ALL,completion_rate_registered_target,80,%,0067_R01 示範差距判讀門檻表,Replace only if the Association supplies an authorized approved KPI threshold; otherwise leave explicitly as a sample benchmark.,示範分析用假設，沒有協會核准或官方效力。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F045,ALL,assessment_coverage_target,95,%,0067_R01 示範差距判讀門檻表,Replace only if the Association supplies an authorized approved KPI threshold; otherwise leave explicitly as a sample benchmark.,示範分析用假設，沒有協會核准或官方效力。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F046,ALL,assessment_pass_rate_target,80,%,0067_R01 示範差距判讀門檻表,Replace only if the Association supplies an authorized approved KPI threshold; otherwise leave explicitly as a sample benchmark.,示範分析用假設，沒有協會核准或官方效力。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F047,ALL,survey_response_rate_target,90,%,0067_R01 示範差距判讀門檻表,Replace only if the Association supplies an authorized approved KPI threshold; otherwise leave explicitly as a sample benchmark.,示範分析用假設，沒有協會核准或官方效力。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F048,ALL,positive_response_rate_target,85,%,0067_R01 示範差距判讀門檻表,Replace only if the Association supplies an authorized approved KPI threshold; otherwise leave explicitly as a sample benchmark.,示範分析用假設，沒有協會核准或官方效力。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
SYN-0067-R01-F049,ALL,budget_utilization_ceiling,100,%,0067_R01 示範差距判讀門檻表,Replace only if the Association supplies an authorized approved KPI threshold; otherwise leave explicitly as a sample benchmark.,示範分析用假設，沒有協會核准或官方效力。,SAMPLE_SYNTHETIC_UNVERIFIED_REAL
```
