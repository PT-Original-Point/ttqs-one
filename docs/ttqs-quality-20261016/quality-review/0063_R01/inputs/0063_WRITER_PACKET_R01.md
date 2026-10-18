# 0063 Writer Packet R01

## 任務身分與界線

你是 OpenCode v2 CLI 的文件內容 Worker。請為 TTQS ONE 撰寫 DOCX 0063 的完整專屬正文草稿及 Unique Blueprint，回傳可由本機確定性排版的完整繁體中文 Markdown。你只需輸出內容，不得執行工具、讀取其他檔案、建立 DOCX、聲稱測試或核准已發生。

專案：TTQS_ONE
文件 ID：0063
正式要求：I14-E04
官方方框流水號：068
官方要求定位：勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》p.5；原文重點為「是否提供查詢功能，並具持續改善機制。」
本件正確文類：查詢服務作業程序＋完整的查詢失敗／改善合成案例，附可用的受理、處理、覆核、改善表單。
Candidate 狀態：候選示範文件，非協會已核定制度，未證明協會現有查詢服務已實際運作。
目前 GitHub 分支 HEAD：0c07049bbd0edf8c6d36e3c17ee339d82b010986

## 已核對控制來源及候選來源

- 01_HUMAN_MISSION_AND_ACCEPTANCE.md，Git blob 538bedb9d87e8465f43151933b4a5c1bfa4bbc4e：文件須完整、逐件專屬、原始點協會適切、可直接閱讀操作；嚴格區分候選、樣本、真實證據，不虛構核准、活動、簽章或法人事實。
- 02_GENRE_WRITING_MANUAL.md，Git blob 4ff863d9f534b6359fc1c7c1685bd8cce02da886：第14類文件需有自身合適文類、足以直接操作的正文、完整示範及可追溯來源。
- 03_157_CHECKBOX_BLUEPRINTS.md，Git blob 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63：第068格明確為「查詢/持續改善：查詢案例、失敗紀錄、改善」；不要把官方流水號068誤當成文件 ID 0068。
- 06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md，Git blob 263aaca84891bba8dca087875804343c3670e921：只用 OpenCode v2 CLI 當下可見的免費標示 SKU；Worker 回傳可用正文；不得以 Worker 自稱 PASS 代替品質驗收。
- DOCX 0060 R08 SHA-256 92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3
- DOCX 0061 R03 SHA-256 3d4fe20f7fb825e470ed5dfd71fcaf0f5bb8052dc7a63ef51ee08e2a11668c9c
- DOCX 0062 R04 SHA-256 460c4fca4e685bdbf93b53b9cc3eecfc0ea72ede07dab209a68ec7f34476d924

## 可沿用的跨文件事實（都是 SAMPLE，不能改寫成真實）

0060 replacement register:
- case_id SYN-0060-2026-A01。
- sample course title：社區志工接待與資源轉介界線。
- sample course date：2026-08-15；sample follow-up date：2026-09-14。
- registered 12 persons, attended 10, absent 2. Do not invent people or identities.
- source document code for sample attendance register: TT-2026-SYN60A-DO-ATT-RST-S3-006-V01.
- the derived arithmetic 12 - 10 = 2 is consistent, but 0063 must not turn it into real performance.
0061 R03:
- its single and only sample archive/index entry has file_id F-0061-2026-0001 and is linked to case SYN-0060-2026-A01 and source doc_id 0060.
- 0061 has a fixed 15-field index schema and an access/hold/authorization workflow. 0063 must not redesign its fields, claim more than the single entry, grant access, or treat a denied permission request as a search failure.
0062 R04:
- handles the complete evidence-file list and original locations. 0063 is not a substitute archive inventory.

## Unique Blueprint requirements

Begin the response with exactly this top-level marker: UNIQUE_BLUEPRINT.
Create a concrete mapping with:
1. identity mapping doc_id 0063 → I14-E04 → official box 068, official page 5 wording.
2. genre rationale and specific reader/users (small volunteer association training administration and evaluator), in plain Traditional Chinese.
3. negative-neighbor boundary against 0060/I14-E01/065, 0061/I14-E02/066, 0062/I14-E03/067, 0064/I14-E05/069. In particular: 0061 query/access logs are not 0063's continuous-improvement case; 0064 owns speed/performance measurement. Do not mix document ID and checkbox serial.
4. section-by-section architecture specifying what complete usable content appears in each section.
5. one internally consistent, fully synthetic improvement case and a fact inventory.
6. every formula, numerator, denominator, denominator rules, rounding and interpretation.
7. sample replacement-register row plan, including exact real source needed to replace each synthetic fact and role/function to verify (no real person's name).
8. use and disuse conditions; explicit HOLD/REJECT/stop branches.
9. final acceptance checklist tied to the required content and the final DOCX SHA will be recorded outside the human-facing body.

## Scenario and mandatory complete data

Create one clearly named and fully labeled sample case: SYN-0063-QI-2026-01. It is a 0063 query-service quality-improvement tabletop exercise, distinct from source case SYN-0060-2026-A01. Every fact, date, role assignment, result, metric, target and decision in the scenario is SAMPLE/SYNTHETIC. Do not say original point association actually adopted, approved, deployed, performed or signed this process. Functional roles only; real organization role assignments are UNKNOWN.

The test fixture has two synthetic search cards for the exercise only. It does not add another record to 0061; 0061 still has exactly its single sample file_id F-0061-2026-0001. Keep the fixture visibly separate from any actual archive:
- Card A is the source package 0060, case SYN-0060-2026-A01; it carries the course title and date listed above, attendance metrics 12/10/2 and sample source code TT-2026-SYN60A-DO-ATT-RST-S3-006-V01.
- Card B is the single 0061 index entry F-0061-2026-0001 referring to Card A/case SYN-0060-2026-A01. It is a synthetic test fixture label for this exercise, not a second 0061 index item.
- No personal names, student IDs, contact details, actual association folders or credentials.

Baseline 8 query tasks on 2026-10-26, same set repeated on 2026-10-28:
1. exact case_id SYN-0060-2026-A01 → unique hit, first response success.
2. exact file_id F-0061-2026-0001 → unique hit, first response success.
3. exact course title → unique hit, first response success.
4. course date 2026-08-15 → unique hit, first response success.
5. user phrase 報到表 → baseline zero result because synonym alias absent; one failure.
6. phrase 課程人數 → the case contains three different measures (registered 12, attended 10, absent 2), so the service must clarify which measure; do not guess. Baseline not resolved at first response, one clarification required.
7. request 課程資料全部 → too broad and lacks exact record/field/purpose; must ask for a narrower request and verify permission; baseline not resolved at first response, one clarification required.
8. ask 課程日期與到課人數 → unique values 2026-08-15 and 10, first response success.

Baseline first-response resolvable = 5/8 = 62.5%. One zero-result case = 1/8 = 12.5%. Two clarification-required cases (metric ambiguity and overbroad scope) = 2/8 = 25.0%. Use fixed denominator 8 and explain one query task equals one observation. Do not classify access denial as search failure.

Synthetic corrective actions on 2026-10-27:
- Add a controlled alias mapping 報到表 → 出缺席簽到紀錄名冊 / source code TT-2026-SYN60A-DO-ATT-RST-S3-006-V01; preserve original official record title/code and do not rename source evidence.
- Add a three-choice clarification prompt for ambiguous “人數”: 報名人數12 / 到課人數10 / 缺席人數2; cite the sample source and do not silently choose a metric.
- Add a minimal-scope clarification for broad requests, requiring request purpose, exact record/field and a separate permission decision. Search hit alone never authorizes disclosure.
Retest the same 8 tasks on 2026-10-28:
- First response successes: tasks 1-5 and 8 = 6/8 = 75.0%.
- Tasks 6 and 7 become resolved after one clarification each; total resolved within one clarification = 8/8 = 100.0%.
- First-response improvement = 75.0% - 62.5% = +12.5 percentage points.
- zero-result rate after alias correction = 0/8 = 0%.
- All figures are synthetic. Do not report elapsed seconds, response-time benchmark or speed; I14-E05/0064 handles systematization and retrieval speed.
Synthetic follow-up review date 2026-11-25, still only a proposed sample date, not a real review.

##正文交付要求

After the Blueprint, begin the second top-level marker exactly: HUMAN_FACING_MANUSCRIPT.
Write a mature and complete Traditional Chinese document of about 8,000–12,000 Chinese characters if feasible. Use the title:
「查詢服務與持續改善作業指引暨合成演練」

The reader should understand in the first page: what the document is; who should use it; when to use it; how to process a request; what gets held or rejected; what evidence to keep. Use humane language for a small volunteer organization and avoid enterprise jargon.

Include all of the following:
- clear document control and candidate status, use limitations, no false association approval;
- concise purpose and scope; when this document applies; explicit out-of-scope list;
- a stepwise operating flow from receiving a query, identity/purpose/scope check, search using approved source/index, result and permission decision, response, record, complaint/failed-query review, correction, retest and follow-up;
- functional role matrix with duties and separation of duties; real role appointments marked UNKNOWN / pending association confirmation;
- decision table with at least: unique match, no-result, ambiguous result, overbroad request, incomplete source/locator, permission hold/denial, privacy risk, and repeated/systemic failure. Give action, record, closure/stop criterion for each;
- response language examples for success, clarification, no-result, permission hold/denial, correction notice. Do not disclose sensitive data in the example;
- a complete intake form (blank reusable version) and one filled synthetic intake;
- a complete baseline 8-row query matrix with query, intended target/answer, first outcome, reason and corrective action; concise tables may be split for readability;
- full failure log for three distinct issues (missing alias, ambiguous metric, overbroad request) with impact, containment, root cause, correction, owner function, due date, evidence and retest status;
- correction plan, decision/closure and 30-day follow-up plan;
- same-8 retest table with first-response vs one-clarification classifications;
- reproducible calculations for every KPI, including explicit formulas and numerator/denominator;
- a reusable blank ongoing query/service improvement record plus completed sample;
- a replacement/evidence checklist explaining exactly which actual records are needed before any SAMPLE can be replaced with REAL;
- rejection/HOLD conditions and a final usage checklist.

Mark every scenario table, filled form, date, count, decision, target, functional assignment and result clearly as SAMPLE/SYNTHETIC; include a short label on every table/callout containing synthetic values. Blank reusable forms may be labeled TEMPLATE/未填，不得偽裝為已完成證據. Keep document engineering hashes/CLI metadata out of the human-facing body.

Use compact, readable tables (prefer <=5 columns; split wide tables). Writing should be specific, operational and internally consistent. Do not invent facts beyond this packet. Never turn synthetic facts into REAL claims. Return full content, not a summary.

End with exactly two sections:
1. 「Unique Blueprint」
2. 「Manuscript」
with all content under those sections.

