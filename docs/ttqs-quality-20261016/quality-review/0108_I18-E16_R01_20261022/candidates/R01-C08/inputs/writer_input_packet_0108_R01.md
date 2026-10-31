# TTQS ONE bounded writer input packet

# Writer brief

WORK_ID=TTQS-0108-I18-E16-SYNTHETIC-MANUSCRIPT-WRITER-R01-20261022-01
DOC_ID=0108
OFFICIAL_REQUIREMENT=I18-E16｜提高薪資紀錄
PROJECT_BLUEPRINT_INDEX=117 (internal index, not official checkbox serial)
ROLE=TEXT_ONLY_WRITER
REQUESTED_MODEL=opencode/deepseek-v4.1-flash-free
SOURCE_HEAD=75d8f79679e3b3df2a88555e78637404674ff018
SOURCE_PACKET_SHA256=f11df2f92edb7c63bc7dbddefe8461188dfdf90c4be9e0c0c4ae284f15457d5f
UNIQUE_BLUEPRINT_SHA256=41713064e2744c12831cb56098cc3ceb5661279048eb16123583f6c26d2f64ab
OFFICIAL_PDF_SHA256=805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709
SAMPLE_CASE_ID=SYN-COHORT-0108-A

Write a complete, mature Traditional-Chinese manuscript for an evaluator-facing TTQS evidence record, following the two attached files as binding. Output only the full manuscript in Markdown; no preface, tool calls, code, or assertion of QA/acceptance.

Include: cover/status and exact doc/requirement identity; one-minute use; scope and non-causality warning; period and pay-component definitions; an 8-row fully populated synthetic record table; individual source-index and comparability state; formulas/calculations; reconciliation and second-person review workflow; detailed filled examples including an increase and HOLD case; a usable blank operating form clearly marked as a template; sample-to-real replacement register with evidence, authority/consent, masking, custodian, verifier, completion, and HOLD; decision states/rejection criteria; limitations, source traceability, and version/change log. Make it operational for a small volunteer association.

Use exactly the fixed SYN-P01 through SYN-P08 data and arithmetic in the Blueprint. Retain: matched n=6; base sum 205,500 and mean 34,250; follow-up sum 212,500 and mean 35,416.67; net +7,000; mean difference +1,166.67; aggregate change 3.406% (display 3.4%); increases 4/6=66.7%; average among four increases +1,875. P07 is an employment transition; P08 has a missing baseline; neither enters the matched denominator or may be called zero/no raise. Mark everything SAMPLE/SYNTHETIC; do not describe the association, real trainees, actual employers, or real wage evidence.

Never fabricate payroll/tax/insurance records, employer confirmations, consent, signatures, approvals, real wages, or training-caused effects. Missing/noncomparable inputs are UNKNOWN/HOLD; distinguish evidence state from case disposition; never convert UNKNOWN into zero. Do not import 0100/0101 ability scores, 0102 awards, or 0107 certification facts. Do not claim shared REAL cases. Use only clearly synthetic explanatory detail.

Do not edit project files, call tools, use external services, or create third-party documents. Return the entire manuscript in one response, not an outline.

Use the attached source packet and Unique Blueprint as binding.

--- SOURCE PACKET ---

# 0108｜I18-E16「提高薪資紀錄」來源包 R01

## 身分與來源錨定

- TTQS ONE 文件 ID：**0108**；官方要求：**I18-E16**；文類：`evidence_record`；官方佐證表第 7 頁。
- 157 項專案藍圖內部索引：**117**；不是官方印刷流水號。官方序號維持 `UNKNOWN`，除非從正式原表直接讀得。
- 本次 GitHub PR #92 候選分支 HEAD：`3dad3490872be0169cfbe9bb1b6564434694a8a6`。
- 官方 mapping `quality-review/0036_R13/inputs/mapping/checkbox_mapping_compact.json` Git blob：`ee3fc17e4e0e89a5b5d404c6f0ca7bd92a1a4f9b`；映射 0108 → I18-E16、第 7 頁、`0108__提高薪資紀錄_可直接使用成品.docx`。
- 157 Blueprint registry `03_157_CHECKBOX_BLUEPRINTS.md` Git blob：`8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`；第 117 項明確要求「提高薪資紀錄：外部薪資證據合規取得」。

## 官方佐證原文與限制

- 官方 PDF：`quality-review/0036_R13/inputs/official/TTQS_evidence_table_training_institution_source.pdf`；Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0`；SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。
- 官方 PDF 第 7 頁列有「提高薪資紀錄。」；對應文字抽取檔 `official_full_text.txt` 第 649 行，Git blob `687044213a0a349fc5167f8627657674708ba74d`。同頁第 648、650 行分別為 I18-E15「高證照通過率之證明資料」與 I18-E17「社群網站知識討論區，人員使用網站頻率」，不得把它們混入本件。
- 共用第 7 頁原頁渲染圖位於 `quality-review/0107_I18-E15_R01_20261022/inputs/official/page7_render_0107_source.png`，SHA-256 `b4b229b154ae401cff6305f8dd413d967ac7a347165d112c355fa15689a358a1`。它是同一官方表第 7 頁的共用來源圖，不是 0108 成品或協會證據。
- 此勾選只列為參考佐證，不自帶薪資增加門檻、因果證明或評核分數保證。薪資變動只能由可比對的正式來源證明；參訓前後的時間關聯本身不能證明訓練造成加薪。

## 文件邊界與安全

- 0108 要呈現一個班別／觀察期間內可追溯、可覆核的薪資變動紀錄；不是薪資調查、勞動市場行情報告、協會員工名冊、薪資單仿件或加薪證明書。
- 目前沒有原始點協會或學員的真實薪資、雇主、薪資單、扣繳、投保或同意紀錄提供給本案。正文只能使用專屬合成資料，所有人名、單位、期間、金額及文件代碼均須 `SAMPLE/SYNTHETIC`；真實結果維持 `UNKNOWN`，正式接受 `NOT_GRANTED`。
- 真實薪資文件含高度個資。不得將真實薪資單、身分證號、帳號、雇主識別、簽名、章戳或可反查資料上傳公開 PR；僅在有權限的正式來源保管，公開版使用遮罩索引及替換清冊。

## 下一施工階段

`READY_SOURCE_PACKET / READY_UNIQUE_BLUEPRINT` 已成立；0108 尚無既有候選 DOCX 或 Writer。本文包與專屬 Blueprint 通過來源和算術驗收後，才可派一個受限純文字 Writer。Writer 路由須先具備可用、無費用、無模型回退且可留原生回覆收據的條件；目前 OpenCode free-tier CLI 有 403，Antigravity 模型身分／fallback 仍 UNKNOWN，因此本來源階段不等於 Writer 已派或文件已完成。

--- UNIQUE BLUEPRINT ---

# UNIQUE BLUEPRINT｜0108 / I18-E16｜R01

## 1. 唯一用途與文件類型

文類：**薪資變動佐證紀錄（evidence record）**。目的是讓協會行政人員或評核者可以按同一班別、同一人、同一雇用關係及可比期間，追溯參訓前後薪資資料、重算變動並辨認缺件。它不是薪資調查報告、勞動市場比較、雇主證明、正式薪資單或訓練成效因果研究。把標題遮住，正文仍須可由「基準期／追蹤期薪資、同一雇用關係、來源索引、個案狀態與重算」辨認為薪資變動證據紀錄。

首頁和每個合成資料表均標 `SAMPLE / SYNTHETIC — NOT 原始點協會 REAL 薪資資料`。不得仿製第三方薪資單、扣繳憑單、投保資料、雇主函、章戳、簽名或可掃描碼。

## 2. 一頁操作摘要

1. 取得可合法處理的正式名冊、完訓資料、薪資基準期與追蹤期原始紀錄、雇用關係確認和資料使用依據。
2. 先用內部受控代碼配對同一人；不把姓名、身分證、帳戶或雇主全名放進公開版。
3. 固定比較口徑：基準期 2026-01-01 至 2026-03-31；課程期 2026-04-01 至 2026-04-30；追蹤期 2026-07-01 至 2026-09-30。正式使用時必須換成真實核准觀察窗並記錄理由。
4. 只有薪資組成可比、雇用關係可確認、兩期來源可回查的個案納入「可比較薪資紀錄」分母。
5. 第二人重算薪資基準、追蹤、差額與期間；缺一期間、口徑不同或個資授權不明即 `HOLD`。
6. 以描述性語句報告結果；不可把參訓後薪資上升寫成訓練造成加薪。

## 3. 固定合成示範案例

- 案例代碼：`SYN-COHORT-0108-A`。案例、課程、班別、日期、人員與金額全為虛構合成資料，不代表協會實際提供課程、僱用關係或薪資結果。
- 課程期間：2026-04-01 至 2026-04-30。示範基準期：2026-01-01 至 2026-03-31；示範追蹤期：2026-07-01 至 2026-09-30。金額為每月固定本薪的三個月平均，幣別示範為新臺幣；加班費、一次性獎金及非固定給付另列，不併入固定本薪。
- 固定人員集合：SYN-P01 至 SYN-P08。不得另造第二組資料。

## 4. 8 人個案明細（唯一固定 SAMPLE）

| SAMPLE ID | 基準期月均固定本薪 | 追蹤期月均固定本薪 | 差額 | 雇用/可比狀態 | 納入匹配比較 | 示範來源代碼 |
|---|---:|---:|---:|---|---|---|
| SYN-P01 | 32,000 | 34,000 | +2,000 | 同一雇主、組成可比 | 是 | SYN-P01-B / SYN-P01-F |
| SYN-P02 | 28,500 | 30,000 | +1,500 | 同一雇主、組成可比 | 是 | SYN-P02-B / SYN-P02-F |
| SYN-P03 | 42,000 | 41,500 | -500 | 同一雇主、組成可比 | 是 | SYN-P03-B / SYN-P03-F |
| SYN-P04 | 35,000 | 35,000 | 0 | 同一雇主、組成可比 | 是 | SYN-P04-B / SYN-P04-F |
| SYN-P05 | 30,000 | 32,000 | +2,000 | 同一雇主、組成可比 | 是 | SYN-P05-B / SYN-P05-F |
| SYN-P06 | 38,000 | 40,000 | +2,000 | 同一雇主、組成可比 | 是 | SYN-P06-B / SYN-P06-F |
| SYN-P07 | 無薪資基準資料 | 29,500 | 不可計算 | 合成示範為追蹤期開始受僱；屬就業轉換，不是加薪 | 否 | SYN-P07-T |
| SYN-P08 | 缺件 | 33,000 | UNKNOWN | 基準原件未提供；必須 HOLD | 否 | SYN-P08-H |

`SYN-Pxx-B/F/T/H` 僅是本合成案例的欄位代碼，不是文件、薪資單、雇主或第三方原件。若 Writer 描述任何合成原件，必須標 `DEMONSTRATION ONLY — NO REAL THIRD-PARTY DOCUMENT`。

## 5. 可重算指標與結論口徑

### 5.1 算術

- 可比較個案：6 人；人員集合 = {SYN-P01…SYN-P06}。
- 基準期合計 = 32,000 + 28,500 + 42,000 + 35,000 + 30,000 + 38,000 = **205,500**；平均 = 205,500 / 6 = **34,250**。
- 追蹤期合計 = 34,000 + 30,000 + 41,500 + 35,000 + 32,000 + 40,000 = **212,500**；平均 = 212,500 / 6 = **35,416.67**。
- 同一組匹配個案總差額 = 212,500 - 205,500 = **+7,000**；平均月均本薪差額 = 7,000 / 6 = **+1,166.67**。
- 匹配個案總額相對變化 = 7,000 / 205,500 × 100 = **3.406%（顯示 3.4%）**。這是合成匹配樣本的描述性比較，不是協會績效或因果效應。
- 薪資增加個案 = {SYN-P01, SYN-P02, SYN-P05, SYN-P06}，4 / 6 = **66.7%**。一人減少（P03）、一人不變（P04）。分母只含有完整可比來源的六筆合成個案。
- 增加者平均差額 = (2,000 + 1,500 + 2,000 + 2,000) / 4 = **1,875**。
- P07 是就業轉換；P08 基準缺件。兩者不得算成「沒有加薪」或混入 4/6 分母。

### 5.2 結論文字限制

可寫：「在此 SYNTHETIC 示範的 6 筆可比較紀錄中，4 筆追蹤期固定本薪較基準期高；此描述只呈現兩期紀錄差異，無法單獨判定差異由訓練造成。」不得寫「課程使薪資增加 66.7%」「學員普遍加薪」或將示範比例外推至全體、協會或真實市場。

## 6. 必須完整生成的正文和表單

1. 首頁、資料狀態、版本、文件 ID、官方要求代碼與用途。
2. 適用範圍、證據鏈與不作因果推論說明。
3. 期間/薪資組成定義卡：本薪、固定津貼、變動津貼、加班費、獎金、稅前/稅後分界、月均計算、雇用變更處理。
4. 八人個案表，逐筆標記來源、可比較性、狀態、分子/分母資格。
5. 可重算總表，顯示 ID 集合、基準/追蹤合計、平均、差額、比例及四捨五入。
6. 證據追溯與覆核表：正式名冊、完訓、個人同意/法源、基準薪資、追蹤薪資、同一雇用關係、遮罩版索引、原件保管位置、初核/複核角色；不得填真人姓名或偽造原件。
7. `SAMPLE → REAL` 替換清冊，逐項列替換來源、權限/同意、遮罩、保管位置、核對責任、完成條件及缺件狀態。
8. 個案狀態和決策紀錄：`VERIFIED_COMPARABLE`、`INCREASE`、`NO_CHANGE`、`DECREASE`、`EMPLOYMENT_TRANSITION`、`HOLD`、`EXCLUDE_WITH_REASON`。
9. 事實限制與下一步：薪資基準期選擇理由、追蹤覆蓋率、期間外變動、雇用關係變更、資料缺失與選擇偏差。

## 7. REAL 替換、個資保護與拒收門檻

- `HOLD`：基準期/追蹤期任一原件缺失；薪資組成不可比；同一人配對不可靠；期間未核定；僱用關係變更未解釋；個資處理法源/同意未核實；來源不能回查；第二人重算不一致。
- `EXCLUDE_WITH_REASON`：非本班、未完訓、非薪資收入、期間外、非固定給付誤入或重複資料。保留原因與變更軌跡。
- `REJECTED_RECORD`：確認來源錯置、文件遭竄改或明確無效後拒收並留理由。來源尚未確認只可 HOLD，不能先指控偽造。
- REAL 欄位未有真實來源前一律 `UNKNOWN`；沒有證據不等於 0。公開 GitHub 只保存合成資料與遮罩索引，不保存薪資單影本或可識別學員/雇主資料。

## 8. 負向近鄰與跨文件事實

- 0100/0101（I18-E08）是能力自評/雷達變化；不能把能力分數直接當薪資證據。
- 0102（I18-E09）是競賽獲獎；獎項不是薪資變化。
- 0107（I18-E15）是證照考試結果；證照通過不等同加薪。
- 0108（I18-E16）使用獨立的 `SYN-COHORT-0108-A`，不宣稱與 0100/0101/0102/0107 或原始點協會共用同一真實案例。0109（I18-E17）網站使用頻率也不能代替薪資資料。
- 只有找到合法共用的 REAL 原始來源時才可跨文件引用相同 source ID；不得複製案例數字來製造證據鏈。

## 9. Writer 和驗收 Gate

Writer 只回完整繁中正文 Markdown（表格及重算均完整），不呼叫工具、不讀寫檔、不製作第三方原件、不宣稱獨立 QA 通過。正文必須保留八人資料與所有算術，明示 SAMPLE/SYNTHETIC 和 REAL UNKNOWN。

技術 QA 應核對 8 筆、6 筆匹配分母、4 筆增加、總額 205,500 / 212,500、差額 +7,000、平均差額 +1,166.67、3.4%、增加者均差 +1,875、P07/P08 排除理由、表格/OOXML、替換清冊及無個資。獨立 reviewer 綁定最終 DOCX exact SHA。Word 原生全頁目視完成前維持 `CANDIDATE / VISUAL_PENDING`；獨立語意 PASS 也不等於正式接受。