# Independent semantic review — TTQS ONE / 0102 / I18-E09 / R08c against current R02

## Exact candidate and source binding
- doc_id=0102; official requirement=I18-E09; unique Blueprint index=110; printed checkbox serial=UNKNOWN.
- Candidate revision R08c, exact DOCX SHA-256 `84c279d09484b88724dd59ae8a5155cb8d0be284133258e166269a80c26c67b4`; 97,846 bytes.
- Extracted body SHA-256 `a3943a63596b4b51c5560b43c4f28b8e9ba86276edec4fd7099ab37275f24eca`; python-docx extraction in document order: 455 paragraph XML elements, 41 tables.
- Current source packet R02 SHA-256 `54d9c05f70b4fef993bd92b656694030878a236e1a2d0c6a21af5d24d94fa1bd`; current unique Blueprint R02 SHA-256 `d6ab10107f42d6f913e1c94df45c8cd179babaa2603a8a7e628c2db78a0cce75`.
- GitHub PR #92 branch HEAD at raw-state check: `4e660df2f63afc63f85afe00afbe88ff144b0245`. The R02 files are local source controls and will be synchronized with this review evidence; do not substitute the older R01 sources from the remote tree.

## Review scope
Review this exact R08c body against the full current R02 source packet and unique Blueprint below. R08c differs from its R08 body only in cover/footer version labels per local receipts; do not import a semantic verdict from another candidate SHA. This is semantic scope only; do not claim visual review, technical QA, formal acceptance, or REAL evidence verification. Do not edit files, call tools, or use another model. Cite material findings by P/T locator. Use PASS/PARTIAL/FAIL and distinguish blockers from nonblocking notes.

## Seven explicit R02 controls
1) Evidence state is restricted to NOT_RECEIVED, RECEIVED_UNVERIFIED, VERIFIED_REAL; case disposition is separate: ELIGIBLE_FOR_HUMAN_REVIEW, HOLD, REJECTED.
2) Form A has separate response_due_date and internal_review_date; an external due date is not invented before a real request is sent.
3) Consent is recorded per purpose (internal processing, organizer verification, de-identified TTQS review, explicit public disclosure), including scope/date/withdrawal/allowed use. Public authorization identifies data, channel, and period; unknown or absent consent remains UNKNOWN/NOT_GRANTED.
4) Form F has ten yes/no/unknown checks; all ten must be YES before ELIGIBLE_FOR_HUMAN_REVIEW. Five core conditions are necessary but not sufficient.
5) Source verification is measured independently of disclosure authorization and training linkage; the formulas do not conflate source verified, eligibility, or association performance.
6) CASE-01's received URL-less screenshot is RECEIVED_UNVERIFIED with HOLD; neither sample case has a third-party original; sample verified award count is zero.
7) Full IDs SYN-0102-CASE-01/02 are used and facts shared across cases are labeled GLOBAL.


## Full current R02 source packet
# 0102 來源包 I18-E09 技能競賽獲獎證據 R02

## 文件身分與狀態

- 專案：TTQS_ONE；預定文件：`0102`；官方要求識別碼：`I18-E09`。
- 官方佐證表指標：18；本機交叉表的分層欄為「2分」；正式指標表的專案索引為 110。這些識別碼不是同一欄位。官方表格未印出 157 格流水號，故 `printed_checkbox_serial=UNKNOWN`。
- 文件名稱沿用 R04 交叉表的歷史規劃標題「指導學員參加技能競賽獲獎_完整工作稿」；名稱只是映射，不能取代正文。
- 目前狀態：`READY_SOURCE_PACKET → READY_BLUEPRINT → READY_WRITER`；尚無 0102 現行候選 DOCX。只找到歷史清冊和不相干的舊封存檔，內容禁止當範本。

## 權威來源及定位

1. 勞動力發展署《TTQS查核佐證文件資料表-訓練機構版》，R04 本機來源 PDF 第 7 頁。該頁在指標 18 的 4 分說明下列出「指導學員參加技能競賽獲獎」作為常見參考佐證之一。此為例示，不能單靠一張獎狀推定訓練造成顯著績效，也不能把例示當 4 分保證。
2. 《TTQS人才發展品質管理評核表-訓練機構版》第 4 頁，指標 18 的 2 分標準為目標客戶及學員認為訓練有達成能力提升效果；3 分和 4 分另有績效改善及顯著具體績效標準。獲獎證明需和受訓者、課程、能力及適當的目標客戶/學員回饋連起來；不能把獲獎事實直接等同全部評核條件。
3. GitHub PR #92 分支唯一 Blueprint 03 的 I18-L2 項目索引 110 指向技能競賽獲獎真實原件索取與案例欄位。該索引是專案 157 方框表內的索引，不是 doc_id，也不是已由官方紙本印出的流水號。
4. R04 `REQUIREMENT_SOURCE_RECONCILIATION.csv` 將 `I18-E09`、官方第 7 頁、doc_id 0102 和歷史標題連結；其狀態仍是 `PHASE2_BLUEPRINT_EXPANDED_PREPRODUCTION` / `THIRD_PARTY_OR_OFFICIAL_ORIGINAL_REQUIRED`。

## 精確來源版本

- GitHub PR #92 / branch `work/ttqs-one-document-quality-contract-20261016` live HEAD at source capture: `db0cd977151dd8623ca6055acdc55dd9c852aa08` (candidate branch, not formal acceptance).
- `01_HUMAN_MISSION_AND_ACCEPTANCE.md` Git blob: `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`.
- `02_GENRE_WRITING_MANUAL.md` Git blob: `4ff863d9f534b6359fc1c7c1685bd8cce02da886`.
- `03_157_CHECKBOX_BLUEPRINTS.md` Git blob: `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`.
- `04_CODEX_GOAL_24X7_EXECUTION.md` Git blob: `4ee893218791ec9460e824fc559933c276414738`.
- `05_HOURLY_NATIVE_WAKE_RESUME.md` Git blob: `35d3081c7e7fb979466c3a58a1e77b42f0d1441a`.
- `06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` Git blob: `4c7eff55748ff265b1e5a7d1122852b0d101acbd`.
- Root `AGENTS.md` Git blob: `103cc9b04e4e756cbc7a8d405faaff218beade69`.
- Official evidence table PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Official assessment form PDF SHA-256: `9d253829410a505c77d8a59fa0203b4c052aa223e2c98d1d509c7c1a57083684`.
- Local requirement/source reconciliation CSV SHA-256: `ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9`.
- Historical 142-file inventory SHA-256: `5eef25c42fd3473136149a91db21c5164c021afc73ff6602d1488511031fd7f5`.

## Existing association facts and limits

- The workspace Mission identifies 屏東縣原始點關懷協會 as the project target, but legal registration, current authority, real training activity, staff, learners, competition participation and awards are not established by the available evidence. The document must not assert these as current facts.
- No approved real competition case, learner record, organizer confirmation, award certificate, competition results list, consent, or authorization to publish was found in the current 0102 lane at source preparation.
- Any example must be visibly `SAMPLE / SYNTHETIC`. Use aliases, avoid actual names, do not fabricate an actual event organizer, award, ranking, certificate, signature, organizer response, association approval or execution record.
- A worked process example may start from a synthetic self-reported claim and correctly end `PENDING_REAL_SOURCE` / `HOLD`; it must not create a fictional third-party original or report a verified win.

## Historical material: discovery only, body reuse prohibited

- Baseline inventory row: `0102`, `I18-E09`, historical title as above, inventory SHA `bdaeb97815a495223ed631abee7a7ca189921501d48fa0f1e1995275e07b2b2c`, recorded as `VALID_DRAFT_WAITING_ORIGINAL`, with `FONT_LT_8`, `FONT_LT_9_MATERIAL`, `GOVERNANCE_CLUTTER`, `HIGH_CROSS_DOC_SIMILARITY`; readback policy explicitly states `HISTORICAL_INVENTORY_ONLY_BODY_REUSE_PROHIBITED_BY_R04`.
- The referenced baseline binary was not present at its historical path when checked. Its body is not available for reuse.
- A separate archived file named `0102_122_指標18_4分_輔導考照及學員回訓率持續提高.docx` is a different project-index/requirement neighbor. It is not I18-E09 and must not be used.

## Required document behavior

The Word must be a practical third-party evidence acquisition and verification tool, with an actual filled sample that demonstrates how to stop/hold when proof or training linkage is missing. Its process can support future handling of authentic results. Until genuine source originals are supplied, `real_awards=UNKNOWN`, `verified_awards=0 for this SAMPLE dataset only`, and `formal_acceptance=NOT_GRANTED`.

## R02 文件修訂綁定

- 本來源包僅修訂文件資料模型與驗收規則；官方需求文字及官方 PDF 來源未改。
- current unique Blueprint: `UNIQUE_BLUEPRINT_0102_I18-E09_R02.md`
- unique Blueprint SHA-256: `d6ab10107f42d6f913e1c94df45c8cd179babaa2603a8a7e628c2db78a0cce75`
- R02 修正：證據狀態與案件處置分離、同意依用途分欄、Form F 十項全是的門檻、來源查證與揭露授權指標分離、對外期限與內部檢視日分離。
- real award originals, organizer confirmations, consent, signatures, and association decisions remain unavailable; all worked records remain SAMPLE / SYNTHETIC.


## Full current unique Blueprint R02
# UNIQUE BLUEPRINT 0102 I18-E09 R02

## Identity

- `project_id`: TTQS_ONE
- `doc_id`: 0102
- `official_requirement_id`: I18-E09
- `indicator`: I18 / 指標 18「訓練系統的一般性功能—目標客戶及學員的評價」
- `project_157_index`: 110 in current `03_157_CHECKBOX_BLUEPRINTS.md`
- `printed_official_checkbox_serial`: UNKNOWN (the source page displays a checkbox, not a printed sequence number)
- `requirement_text`: 指導學員參加技能競賽獲獎。
- `genre`: third-party evidence acquisition, provenance/authenticity verification, training-linkage assessment, and case register; not a fabricated award certificate or a generic success story.
- `reader`: small training-association administrative/volunteer staff and a reviewer checking the evidence.
- `candidate_title`: 技能競賽獲獎證據取得與查核工作紀錄
- `status`: candidate/SAMPLE-SYNTHETIC; no REAL result evidenced.

## Why this file exists

Give an authorized staff member a repeatable, low-overhead way to receive a learner's award claim, obtain and authenticate a real third-party record, connect the result to a specific training activity without overstating causation, protect personal information, decide whether the item is admissible, and locate the source later. A blank checklist alone is insufficient; include a completed synthetic case showing the hold path.

## Source facts and qualification

- Official evidence table PDF p.7, SHA `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`: award coaching is one example in the indicator-18 4-point evidence list.
- Official assessment form PDF p.4, SHA `9d253829410a505c77d8a59fa0203b4c052aa223e2c98d1d509c7c1a57083684`: the 2-point standard concerns target customer/learner belief that training achieved ability improvement. Do not equate a competition award alone with this judgment or with a guaranteed score.
- Project blueprint row 110, I18-L2; local R04 crosswalk maps `I18-E09` and doc 0102, while formal printed sequence remains unknown.
- Real award originals, event results and participant records are not supplied. The sample case is synthetic and must stay explicitly separated from real evidence.

## Negative neighbors

- I18-E08 / project index 109 / docs 0100 and 0101 concern pre/post self-rating and radar analysis. Do not copy their survey/report genre or their case data. Link only when an actual shared case ID and evidence supports it; no shared real case is currently established.
- I18-L2 index 111 concerns a thank-you letter and real-source acquisition. This file must focus on competition award records, not generate a thank-you letter.
- I18-L2 index 112 concerns certificate acquisition rate and denominators. Do not claim an award count or pass rate as a credential-acquisition rate.
- I18-L4 index 122 concerns continued exam coaching and learner return rate. An archived artifact using the prefix 0102 for that different requirement is a known numeric-ID collision and is not source material.

## Document-specific outline

1. Cover and one-minute use guide: exact purpose, official mapping, who should use it, where a user finds the request form, verification form and decision register; prominent `SAMPLE / SYNTHETIC` warning.
2. Evidence boundary: what the award record can support, what it cannot prove, difference between self-report, organizer-issued source, checked original, training linkage and formal scoring.
3. Small-team roles and handoff: requester/records custodian, independent callback verifier where feasible, approver only if real delegation is confirmed; otherwise `authorization status UNKNOWN` and hold external disclosure.
4. End-to-end flow with decision branches: claim received → consent/privacy check → request minimum source → receive original or official public result → authenticity check → verify awardee/competition/date/result → link training objectives → decision → controlled filing / hold / reject → annual review. Include timeout/no-response and suspicious-source branches.
5. Form A, case intake: unique case ID, pseudonymous learner ref, course ID/date and source, competition title/date/organizer, exact claimed result, claim origin, per-purpose consent status/scope/date/withdrawal/allowed use, evidence requested, separate response_due_date and internal_review_date, evidence_state and case_disposition.
6. Form B, participant source request: complete ready-to-send draft with purpose, accepted documents/official links, permitted redaction, deadline, response channel, consent choice, no penalty/no-guarantee language. Clearly marked unissued SAMPLE template.
7. Form C, organizer verification request/script: ready-to-send text and call checklist using independently obtained official contact information; ask only to confirm competition identity, published result, category, date and listed awardee reference; record channel, date/time, handler, reply/source locator. Mark all drafts as not sent.
8. Form D, source authenticity checklist: official domain/document provenance, issuer identity, publication date, event/date/category consistency, name/alias match held privately, original-file integrity/hash, external confirmation, tamper/duplicate check, privacy/consent, evidence locator. Keep evidence_state limited to NOT_RECEIVED, RECEIVED_UNVERIFIED, VERIFIED_REAL; record ELIGIBLE_FOR_HUMAN_REVIEW, HOLD, REJECTED separately as case_disposition. No PASS without every required predicate.
9. Form E, training-linkage matrix: actual course learning objective → taught skill → practice/assessment record → competition skill/result → temporal sequence → alternative explanations → corroboration → bounded inference. Explicitly separate association, temporal order and causation.
10. Form F, case decision sheet: ten checks with answers 是／否／未知; all ten must be 是 before case_disposition=ELIGIBLE_FOR_HUMAN_REVIEW. The first five cover source/event core checks; the remaining five separately cover recipient identity, purpose-specific consent, training linkage, duplicate/tampering/conflict checks, and a locatable/preservable source. A five-condition core is necessary but not sufficient. Record source verification separately from training linkage and disclosure authority; include evidence used, missing item, owner role, response_due_date, internal_review_date, reviewer and next action. Sample approval language must be `示範判定`; no real approval.
11. Worked synthetic case: two synthetic claims, both without a received/authenticated third-party original; one can be requested but remains pending; the other lacks consent or sufficient identity match and is held. Show completed forms and an explicit zero verified-award result for the sample dataset only.
12. Computation and interpretation: `verified award cases = count(unique case_id with official source checked AND award confirmed AND identity match AND training link documented AND disclosure authority)`; sample count 0. Optional internal process KPI `evidence closure rate = verified cases / claims due for review` with sample numerator 0 and denominator 2 = 0%. State this is a synthetic workflow example, not association performance or TTQS scoring.
13. Case register and evidence/replacement register: one row per claim; sample CSV-like table with source status, verification, training link, privacy authority, decision, locator, synthetic fact IDs, real source required, owner role, deadline and state.
14. Filing, access and retention: keep identity key and source original in an authorized restricted location; public review package receives pseudonym and redacted summary only; access log, version, backup, retention trigger, safe deletion and breach response. Exact retention period is `to be set from current law/consent/association policy`; do not invent a period.
15. Exception and rejection rules; quick-use checklist and version/change record.

## Required tables and usable content

- Case intake table with fillable fields, allowed values and worked sample row.
- Evidence authenticity matrix with at least 8 checks and disposition for pass/fail/unknown.
- Training-linkage matrix with skill, course objective, evidence source and inference limit.
- Decision table mapping missing original, failed issuer confirmation, identity mismatch, no award, duplicate, no consent, missing training link, and confirmed authentic record to HOLD/REJECT/eligible-for-human-review.
- Replacement register with one fact per row, `fact_id`, `case_id`, `doc_id`, location, synthetic value, replacement source required, responsible role, state.
- Two fully populated sample case records; neither may assert an authentic award.
- Request text to the learner and organizer, marked `SAMPLE TEMPLATE - NOT SENT`.

## Sample case fixed boundary and arithmetic

Use `case_id=SYN-0102-CASE-01` and `SYN-0102-CASE-02`. All names/events/claims/dates are invented for workflow demonstration. For both cases, no third-party original has been received, independently checked, or approved for disclosure. Hence `source_verified_count=0` and `eligible_for_human_review_count=0`; the sample source-verification rate is `0/2=0%`. Do not call this a closure rate or association performance. The calculation only demonstrates a control metric. It is not a real association outcome, award result, or TTQS score. Do not manufacture an award certificate, winner list, organizer reply, signature or real institution name.

## Required rejection / hold conditions

HOLD if source is not received; issuer/channel cannot be independently checked; consent/authority is incomplete; identity or event details conflict; training-to-competition relationship lacks traceable support; third-party reply is pending; original integrity unknown; publication scope not authorized. REJECT the evidence item only when reliable checks show it is false, unrelated, duplicate or not an award; retain reason and reviewer. Never convert a missing source into a zero award result for the association.

## Document acceptance criteria

- Reader can operate the end-to-end workflow without further model interpretation.
- Distinct genre is unmistakable when title is hidden: evidence acquisition + authenticity + training linkage.
- Templates, completed synthetic examples, decision thresholds, formulas and exceptions are all usable.
- 2-point vs 4-point source context is accurately qualified.
- No real association event, winner, certificate, authorization, signature or approval is fabricated.
- No reuse of historical 0102 body or unrelated 0102_122 file.
- Real evidence remains UNKNOWN until a protected authorized source is supplied; formal acceptance remains NOT_GRANTED.

## R02 semantic-repair controls (優先於本文件較早的 R01 欄位草案)

- `evidence_state` 僅使用 `NOT_RECEIVED`、`RECEIVED_UNVERIFIED`、`VERIFIED_REAL`；`case_disposition` 獨立使用 `ELIGIBLE_FOR_HUMAN_REVIEW`、`HOLD`、`REJECTED`。狀態不混填。
- Form A 必須分開 `response_due_date` 與 `internal_review_date`；對外期限只在實際送出後設定。
- 同意可複選且按用途分開：內部處理、向主辦查證、去識別化 TTQS 審查、明確公開。公開授權必須列明資料、管道及期間；同意未取得時每一用途均為 `UNKNOWN` 或 `NOT_GRANTED`。
- Form F 回答只可用「是／否／未知」，十項全部為「是」才可送人類複核；五項核心條件不是充分條件。
- 來源查證數不以公開揭露權限決定。來源真實、獎項與身分可核時計來源已驗證；訓練關聯、用途同意和十項決策門檻另行評估。
- CASE-01 的無網址截圖已收到但未經第三方查核，故 `evidence_state=RECEIVED_UNVERIFIED`、`case_disposition=HOLD`；兩個 SAMPLE 案仍沒有第三方原件，`verified_awards=0` 僅描述這組合成資料。
- 使用完整案號 `SYN-0102-CASE-01`、`SYN-0102-CASE-02`；共用事實標示兩案，跨案列標 `GLOBAL`。


## Full exact-R08c body
P0001: 技能競賽獲獎證據取得與查核工作紀錄
P0002: SAMPLE / SYNTHETIC 示範文件
P0003: 非原始點協會真實得獎、核准、競賽或第三方原件
P0004: 本文件中的姓名、競賽、主辦單位、日期、獎項、聯絡紀錄、簽署與判定，全部是流程演練用的合成資料。文件沒有取得任何第三方原件，沒有確認任何真實得獎事實，也沒有任何協會核准或正式評核結果。閱讀時請把每一個 SYN- 編號視為「示範用」，不可當成業務紀錄。

[TABLE T0001]
T0001-R0001: 項目 | 內容
T0001-R0002: 文件編號 | 0102（內部文件編號，不是官方列印流水號）
T0001-R0003: 對應要求 | I18-E09；TTQS 指標 18「訓練系統的一般性功能—目標客戶及學員的評價」
T0001-R0004: 專案索引 | 110（專案 157 方框表索引；不是文件編號，也不是官方流水號）
T0001-R0005: 官方依據 | 《TTQS 查核佐證文件資料表－訓練機構版》第 7 頁；《TTQS 人才發展品質管理評核表－訓練機構版》第 4 頁
T0001-R0006: 版本 | R08c
T0001-R0007: 文件性質 | 第三方證據取得、來源真偽查核、訓練關聯分析與案例登錄工具
T0001-R0008: 主要使用者 | 小型訓練協會行政志工、資料保管人、獨立查證人、覆核人
T0001-R0009: 資料狀態 | real_awards=UNKNOWN；verified_awards=0（僅限本示範資料集）；formal_acceptance=NOT_GRANTED
P0006: 文件用途
P0007: 這份文件不是獎狀範本，也不是得獎故事。它是一套可以重複使用的工作方法，讓一位沒有法務或資訊背景的行政志工，在收到學員「我參加過比賽、得了獎」的說法時，知道如何：
P0008: 1. 先收件、編案號，不急著對外宣布。
P0009: 2. 檢查個資與同意範圍，只收必要資料。
P0010: 3. 用學員提供的線索，向競賽主辦單位索取可核對的來源。
P0011: 4. 用獨立取得的官方聯絡管道查證，不只用學員給的截圖。
P0012: 5. 核對競賽、日期、組別、獎項與得獎者身分。
P0013: 6. 把競賽技能與課程目標、訓練紀錄連起來，但不過度推論因果。
P0014: 7. 做出有限度的判定：可送人類複核、暫緩（HOLD）或拒收（REJECTED）。
P0015: 8. 把來源、位置、版本、權限與替換需求記錄下來，讓下一個人找得到。
P0016: 對應要求與正確用法
P0017: 官方佐證資料表第 7 頁在指標 18 的 4 分說明下，把「指導學員參加技能競賽獲獎」列為常見參考佐證之一。這是例示，不是保證；不能因為有一張獎狀，就推定訓練造成顯著績效，也不能把這個例示當成 4 分門檻。
P0018: 評核表第 4 頁的 2 分標準，重點是目標客戶及學員認為訓練有達成能力提升效果；3 分、4 分還涉及績效改善與顯著具體績效。獲獎證明必須和受訓者、課程、能力及適當的目標客戶／學員回饋連起來，不能把「獲獎」直接等同全部評核條件。
P0019: 因此，本文件處理的是「證據是否真實、是否屬於這個人、是否和這段訓練有關、是否可以揭露」，不是替協會打分數。單一獎項不保證 2 分，也不保證 4 分。
P0020: 使用者與責任邊界
P0021: 本文件假設使用者是小型協會的行政志工或兼職工作人員，可能同時負責收件、建檔與聯繫。為避免一人作業失去把關，文件把「收件」、「查證」、「判定」與「核准」分開；如果人力不足，至少要做到「查證者不是唯一獲益者」與「對外揭露前有人覆核」。
P0022: 正確的停止條件
P0023: 遇到下列任一情況，應停止往「已得獎」或「可對外使用」推進，並在表單上留下停止原因：
P0024: 沒有收到任何來源，或只有學員口述：停在 NOT_RECEIVED，不得寫成得獎。
P0025: 收到截圖或影本，但無法確認發行者、賽事或官方公告：停在 RECEIVED_UNVERIFIED。
P0026: 同意不足、同意撤回、或對外揭露範圍不明：停止對外查證與公開，判 HOLD。
P0027: 得獎者姓名、隊名、競賽日期、組別或獎項任一項不一致：停止，判 HOLD。
P0028: 查證管道只來自學員提供的截圖，沒有獨立來源：停止，先換管道。
P0029: 訓練目標與競賽技能之間沒有可追溯紀錄：不得寫因果，判 HOLD 或只能列為背景資料。
P0030: 無法確認協會現行授權人與職務：對外揭露與正式核准停止，記「待依章程及授權名冊確認」。
P0031: 發現疑似偽造、重複或移花接木：停止流通、保留原檔、交人類判斷；只有可靠查核才能 REJECTED，不得自行公開指控。
P0032: 缺少證據時，不得把它轉成「協會沒有得獎」或「協會零績效」。UNKNOWN 就是 UNKNOWN。
P0033: 一分鐘上手
P0034: 1. 今天收到說法：建立案號，填 Form A，先不承諾任何結果。
P0035: 2. 三天內檢查同意：沒有同意，就不向第三方查；同意不足，先補。
P0036: 3. 只索取最少資料：用 Form B 向學員要獎狀、官方結果頁或主辦聯絡窗口。
P0037: 4. 自己找官方管道：用主辦單位官方網站、政府登記或活動公告頁取得電話與網址，不要只用學員給的連結。
P0038: 5. 逐項查核：用 Form D 核對發行者、賽事、日期、組別、獎項、得獎者與檔案完整性。
P0039: 6. 再做訓練關聯：用 Form E 對照課程目標、練習／評量紀錄、競賽技能與時間序。
P0040: 7. 開 Form F 判定：只有來源真實、身分一致、獎項確定、訓練關聯有證據、揭露權限具備，才可列「可送人類複核」。
P0041: 8. 登錄與歸檔：更新案例登錄表與替換清冊；每年覆核一次。
P0042: 表單索引

[TABLE T0002]
T0002-R0001: 表單 | 名稱 | 主要產出 | 建議負責角色
T0002-R0002: Form A | 案例收件表 | 案號、主張、同意狀態、目前證據狀態 | 收件／記錄保管人
T0002-R0003: Form B | 向學員索取資料稿 | 未送出樣板、同意選項、期限 | 承辦人
T0002-R0004: Form C | 向主辦單位查證稿與電話腳本 | 查證管道、通話紀錄、回覆定位 | 獨立查證人
T0002-R0005: Form D | 來源真偽清單 | 各項查核結果與來源狀態 | 獨立查證人
T0002-R0006: Form E | 訓練關聯矩陣 | 技能、課程目標、佐證、推論上限 | 承辦人＋講師
T0002-R0007: Form F | 案例決定表 | 可送人類複核／HOLD／REJECTED | 承辦人擬稿、覆核人確認
T0002-R0008: 附件一 | 案例登錄表 | 每案一行，追蹤期限與狀態 | 記錄保管人
T0002-R0009: 附件二 | 索引／替換清冊 | 每個合成事實的替換來源 | 記錄保管人
P0044: 1. 證據邊界：一張獎狀能說什麼、不能說什麼
P0045: 1.1 五個不同層次，不要混在一起

[TABLE T0003]
T0003-R0001: 層次 | 內容 | 可以支持 | 不能證明
T0003-R0002: 1. 學員自述 | 學員說自己參加某競賽、得到某獎 | 有一項待查主張 | 競賽存在、獎項真實、身分正確
T0003-R0003: 2. 學員提供的截圖／影本 | 學員轉貼的公告、獎狀照片 | 有具體查證線索 | 發行者真偽、是否變造、是否為同一競賽
T0003-R0004: 3. 主辦單位來源 | 官方網站結果頁、主辦函文、正式公告 | 競賽與結果有官方說法 | 得獎者就是本會學員、訓練有貢獻
T0003-R0005: 4. 已查核原件 | 與官方來源互相對照、身分與賽事細節一致 | 來源真實、獎項確定、身分可對應 | 獎項由本會課程造成、評核會給幾分
T0003-R0006: 5. 訓練關聯 | 課程目標、教學、練習、評量與競賽技能有紀錄可連 | 技能重疊、時間序合理、有關聯證據 | 嚴格因果、必然獲獎、自動符合評分標準
P0047: 1.2 三種常見的過度推論
P0048: 把「有獎狀」寫成「訓練績效顯著」：獎狀只證明某次競賽的結果，不證明學習前後的能力變化，也不證明目標客戶的評價。
P0049: 把「同一個人」寫成「同一門課的功勞」：學員可能課前已有基礎、另外參加其他培訓、或競賽難度較低。沒有訓練紀錄與時間序，只能說「有關聯」，不能說「因為這門課所以得獎」。
P0050: 把「協會沒有人提供」寫成「協會沒有得獎」：目前狀態是資料未取得，不是績效為零。UNKNOWN 不能被改寫成 0。
P0051: 1.3 與 2 分、4 分的關係
P0052: 2 分談的是目標客戶及學員認為訓練有達成能力提升效果；這需要回饋或評價資料，不是單靠獎項。
P0053: 3 分、4 分涉及績效改善與顯著具體績效；獲獎可以是佐證之一，但仍要能說明「誰受訓、受什麼訓、學到什麼、表現在哪裡、如何確認」。
P0054: 本文件只協助把「獲獎證據」與「訓練關聯」整理到可被查核的程度，不做評分，也不宣稱會得幾分。
P0055: 1.4 證據等級不是自動加分
P0056: 即使拿到官方結果頁，也要看它是否列出可對應的得獎者、是否為同一屆／同一組別、是否為正式獎項。若官方頁面基於個資只列隊名或部分姓名，必須另外取得主辦單位確認，或由學員提供可對照的證明；不能只看「看起來很像」就通過。
P0057: 2. 小型團隊的角色與交接
P0058: 2.1 最低限度的人員配置

[TABLE T0004]
T0004-R0001: 角色 | 主要工作 | 不可以做 | 人力不足時
T0004-R0002: 收件／記錄保管人 | 建立案號、收件、保管同意書與原件、更新登錄表 | 不得單獨決定對外公開 | 可由承辦人兼任，但公開前要有人覆核
T0004-R0003: 承辦人 | 填表、向學員索取、整理訓練關聯、擬判定 | 不得把未查核資料寫成事實 | 可兼任收件，但查證要換人
T0004-R0004: 獨立查證人 | 用獨立管道向主辦單位查證、填 Form D | 不得只採用學員提供的截圖 | 若真的只有一人，記錄「未能獨立查證」，判定降為 HOLD
T0004-R0005: 覆核人 | 檢查缺件、矛盾、推論過頭 | 不得代替主辦單位回答 | 由理事長、秘書長或指定幹部擔任；資格未確認前只能列「待確認」
T0004-R0006: 核准人 | 核准對外揭露或正式使用 | 不得在授權不明時自稱核准 | 記「待依章程及授權名冊確認」，先 HOLD 對外揭露
P0060: 2.2 利益衝突
P0061: 學員本人、學員親屬、直接教練，不宜同時擔任該案的唯一查證人與唯一核准人。若人力真的不足，至少把「查證紀錄」與「核准紀錄」分開簽註，並在 Form F 寫明「未能完全獨立」。這不是形式主義，而是避免把「希望他得獎」變成「看起來就得獎」。
P0062: 2.3 授權狀態怎麼寫
P0063: 當協會現行授權人、職務或任期無法確認時，不要猜人名，也不要寫「理事長已同意」。固定寫：
P0064: 待依章程及授權名冊確認。
P0065: 在這個狀態下，可以做內部整理、可以向學員索取資料（若同意範圍允許），但不得對外公開、不得具名背書、不得回覆主辦單位以外的人「本會已確認」。等授權名冊與會議紀錄確認後，再補上角色與日期。
P0066: 2.4 交接包
P0067: 每次交接只需三樣東西：
P0068: 1. 案例登錄表（目前狀態、下一步、期限）。
P0069: 2. 該案的 Form A～F（含尚未補齊的欄位）。
P0070: 3. 受限資料夾的位置與存取紀錄。
P0071: 不要用通訊軟體對話當唯一紀錄；重要結論要回寫表單，否則下一個人只會看到片段。
P0072: 3. 端到端流程與分支
P0073: 3.1 流程總覽
P0074: 收到主張
  ↓
建立案號（Form A）
  ↓
同意／個資檢核 ──不足──→ 停止對外，補同意或 HOLD
  ↓
最少化索取（Form B）
  ↓
取得來源？ ──沒有──→ NOT_RECEIVED／逾期 HOLD
  ↓ 有
來源真偽查核（Form D）
  ↓
競賽／日期／組別／獎項／身分核對 ──不一致──→ HOLD（必要時人類判斷）
  ↓
訓練關聯（Form E）
  ↓
案例判定（Form F）
  ↓
可送人類複核／HOLD／REJECTED
  ↓
歸檔、登錄、年度覆核
P0075: 3.2 十個步驟與產出

[TABLE T0005]
T0005-R0001: 步驟 | 做什麼 | 產出 | 停止點
T0005-R0002: 1 | 收件：口頭、訊息、紙本都算，同日給案號 | Form A 前半 | 不承諾「一定會認定」
T0005-R0003: 2 | 同意與個資：確認目的、範圍、撤回方式 | 同意狀態欄 | 無同意→停止對外
T0005-R0004: 3 | 最少化：只收案號、別名、競賽名稱、結果、聯絡方式 | 索取清單 | 不收集身分證號、完整地址
T0005-R0005: 4 | 向學員索取：Form B | 未送出草稿、期限 | 期限到未回→提醒→HOLD
T0005-R0006: 5 | 向主辦查證：Form C，使用獨立管道 | 通話／書面紀錄 | 管道不能獨立確認→HOLD
T0005-R0007: 6 | 真偽查核：Form D | 逐項結果 | 任何關鍵項未知→不得 VERIFIED_REAL
T0005-R0008: 7 | 身分與賽事核對 | 對照紀錄 | 姓名／隊名／日期／組別不符→HOLD
T0005-R0009: 8 | 訓練關聯：Form E | 技能與紀錄對照 | 無紀錄→不得寫因果
T0005-R0010: 9 | 判定：Form F | 可送人類複核／HOLD／REJECTED | 缺證不得轉通過
T0005-R0011: 10 | 歸檔與覆核 | 登錄表、替換清冊、存取紀錄 | 每年或狀態變更時重看
P0077: 3.3 期限建議（內部管理用）

[TABLE T0006]
T0006-R0001: 節點 | 建議期限 | 說明
T0006-R0002: 收件到建案 | 當日建立暫編案號；必要欄位最遲 3 個工作天內補齊 | 先有案號避免資料散落；後續補件不延後收件登錄
T0006-R0003: 同意檢核 | 收件後 3 個工作天 | 沒有同意就不對外
T0006-R0004: 向學員索取 | 7 個日曆天 | 在 Form B 寫明截止日
T0006-R0005: 第一次提醒 | 截止日後 7 天 | 只提醒一次，避免騷擾
T0006-R0006: 第二次提醒 | 截止日後 21 天 | 說明可能轉 HOLD
T0006-R0007: 轉 HOLD | 截止日後 30 天 | 保留重啟機制
T0006-R0008: 向主辦查證 | 取得管道後 10 個工作天 | 電話後補書面
T0006-R0009: 年度覆核 | 每年一次或資料變更時 | 不自動延長同意
P0079: 這些是低維護的內部目標，不是法律期限；實際仍依協會政策與適用法規。
P0080: 3.4 分支處理
P0081: 分支 A：逾期未回
P0082: 1. 截止日後第 7 天：用原管道提醒一次，附上案號與缺件清單。
P0083: 2. 第 21 天：第二次提醒，說明「若未回覆，案件將暫緩，未來可補件重啟」。
P0084: 3. 第 30 天：改為 HOLD，在登錄表寫「學員未回覆」，不要寫「未獲獎」。
P0085: 4. 日後學員補件：沿用原案號，新增版本，不重新編案。
P0086: 分支 B：資料不一致
P0087: 以官方來源為準，把學員說法與官方說法並列，不直接刪掉學員版本。
P0088: 日期差一天、組別名稱寫法不同，先記「待釐清」，不要自行認定是同一件事。
P0089: 得獎者姓名不同、隊名不同、競賽屆次不同：直接 HOLD，不可用「應該是暱稱」帶過。
P0090: 若官方公告更正，保留舊版與更正版，記錄取得日期。
P0091: 分支 C：疑似重複
P0092: 先查案例登錄表是否已有同一競賽、同一得獎者、同一獎項。
P0093: 比對檔案完整性值、檔名、公告日期、截圖內容。
P0094: 若只是同一事實的不同副本：合併為一案，註明副本來源，不重複計算。
P0095: 若看起來是不同人重複使用同一張獎狀：HOLD，交人類判斷；不要公開指控。
P0096: 分支 D：疑似偽造或變造
P0097: 立刻停止在群組、網站或公文裡流通。
P0098: 保留原始檔案與開啟紀錄，不要只留截圖。
P0099: 檢查字體、日期、印章、公告編號、網址、後設資料是否矛盾。
P0100: 不自行下結論「一定是假的」；記「疑似」，判 HOLD，必要時依協會政策處理。
P0101: 只有當可靠查核顯示「賽事不存在」、「官方否認該獎項」、「得獎者確定不是本人」或「同一文件已被證明變造」，才可 REJECTED，並保留理由與覆核人。
P0102: 分支 E：主辦單位不願回覆
P0103: 電話不願回答：改書面，附上所需確認的具體欄位，不要求提供其他得獎者個資。
P0104: 書面仍未回：記「查證未完成」，HOLD。
P0105: 主辦單位表示「不便確認個人資料」：可改問「是否可確認公告連結與獎項名稱」，或請學員自行向主辦申請證明。
P0106: 不得把「主辦不回應」推定為真或假。
P0107: 分支 F：學員撤回同意
P0108: 停止一切對外查證與揭露。
P0109: 依同意書與協會政策處理已保存資料；若無保存依據，採最小化刪除。
P0110: 在登錄表記「撤回」，不要保留可識別的公開版本。
P0111: 若已進入人類複核，通知覆核人停止。
P0112: 4. Form A：案例收件表
P0113: SAMPLE／SYNTHETIC 表格。 以下欄位可直接複製到文書軟體；「允許值」是為了避免同一個狀態出現多種寫法。
P0114: 4.1 欄位定義

[TABLE T0007]
T0007-R0001: 欄位 | 說明 | 允許值／格式 | 必填
T0007-R0002: case_id | 案號 | SYN-0102-CASE-01 或未來真實案 REAL-YYYY-序號 | 是
T0007-R0003: learner_ref | 學員代號，不用真名 | P-SYN-01 之類 | 是
T0007-R0004: claim_date | 收到主張日期 | YYYY-MM-DD | 是
T0007-R0005: claim_channel | 從哪裡聽到 | 口頭／訊息／紙本／轉介 | 是
T0007-R0006: course_id | 學員指稱的課程 | 內部課程編號 | 是
T0007-R0007: course_dates | 課程期間 | YYYY-MM-DD～YYYY-MM-DD | 是
T0007-R0008: competition_name | 競賽名稱 | 全文，含屆次（若有） | 是
T0007-R0009: competition_date | 競賽日期 | YYYY-MM-DD | 是
T0007-R0010: organizer | 主辦單位 | 全名；不確定寫「待確認」 | 是
T0007-R0011: category | 組別／職類 | 全文 | 是
T0007-R0012: claimed_result | 學員主張的獎項 | 冠軍／亞軍／季軍／佳作／入圍／其他 | 是
T0007-R0013: claim_origin | 主張依據 | 自述／截圖／獎狀影本／他人轉述 | 是
T0007-R0014: consent_status | 同意記錄狀態 | UNKNOWN／REQUESTED／PARTIAL／GRANTED／REFUSED／WITHDRAWN | 是
T0007-R0015: consent_scope_status | 各用途的個別同意狀態 | 內部使用、主辦查證、去識別化審查、公開使用各填 GRANTED／NOT_GRANTED／UNKNOWN／WITHDRAWN；不得以單一「已簽」代替 | 是
T0007-R0016: consent_scope | 同意範圍 | 多選：內部處理／向主辦查證／去識別化 TTQS 審查／明確公開；未勾選即無授權 | 是
T0007-R0017: consent_date | 同意日期 | YYYY-MM-DD；未取得填 UNKNOWN | 是
T0007-R0018: withdrawal_date | 撤回日期 | YYYY-MM-DD；未撤回填 無，未知填 UNKNOWN | 是
T0007-R0019: allowed_use | 本次允許用途 | 只寫已明確勾選的用途；公開須記載資料範圍、管道及期間 | 是
T0007-R0020: evidence_requested | 已索取項目 | 獎狀、官方結果頁、主辦聯絡窗口 | 是
T0007-R0021: response_due_date | 對外回覆期限 | 實際寄出後才填 YYYY-MM-DD；未寄出填 未設定 | 是
T0007-R0022: internal_review_date | 內部檢視日 | YYYY-MM-DD；與對外期限分開 | 是
T0007-R0023: evidence_state | 證據狀態 | NOT_RECEIVED／RECEIVED_UNVERIFIED／VERIFIED_REAL；只描述來源收件與查核 | 是
T0007-R0024: case_disposition | 案件處置 | ELIGIBLE_FOR_HUMAN_REVIEW／HOLD／REJECTED；與證據狀態分開 | 是
T0007-R0025: owner_role | 目前承辦角色 | 職稱或角色，不寫個人電話 | 是
T0007-R0026: next_action | 下一步 | 一句話，含日期 | 是
T0007-R0027: notes | 備註 | 只寫必要事實，不寫八卦 | 否
P0116: 4.2 已填 SAMPLE：兩案收件列

[TABLE T0008]
T0008-R0001: 欄位 | SYN-0102-CASE-01 | SYN-0102-CASE-02
T0008-R0002: learner_ref | P-SYN-01 | P-SYN-02
T0008-R0003: claim_date | 2026-10-05 | 2026-09-30
T0008-R0004: claim_channel | 電話＋訊息 | 訊息轉貼
T0008-R0005: course_id | SYN-COURSE-01 | SYN-COURSE-02
T0008-R0006: course_dates | 2026-03-02～2026-04-10 | 2026-01-05～2026-02-15
T0008-R0007: competition_name | 示範盃技能競賽（合成名稱） | 示範盃技能競賽（合成名稱）
T0008-R0008: competition_date | 2026-08-22 | 2026-08-22
T0008-R0009: organizer | （合成）示範技能發展協會 | （合成）示範技能發展協會
T0008-R0010: category | 照顧服務類／個人組 | 照顧服務類／團體組
T0008-R0011: claimed_result | 佳作 | 冠軍
T0008-R0012: claim_origin | 學員自述＋一張無網址截圖 | 他人轉貼截圖，無原始連結
T0008-R0013: consent_status | UNKNOWN（本合成情境未取得簽署） | UNKNOWN（示範文字不構成授權）
T0008-R0014: consent_scope_status | 四種用途均 UNKNOWN；未取得授權 | 四種用途均 UNKNOWN；未取得授權
T0008-R0015: consent_scope | 未勾選任何已確認範圍 | 未確認任何已確認範圍
T0008-R0016: consent_date | UNKNOWN | UNKNOWN
T0008-R0017: withdrawal_date | UNKNOWN | UNKNOWN
T0008-R0018: allowed_use | 無；不得查證或揭露 | 無；不得查證或揭露
T0008-R0019: evidence_requested | 獎狀影本、官方結果頁、主辦窗口 | 官方結果頁、獎狀、可對照的隊員名單
T0008-R0020: response_due_date | 未設定（Form B 未送出） | 未設定（Form B 未送出）
T0008-R0021: internal_review_date | 2026-10-26（合成內部檢視日） | 2026-10-20（合成內部檢視日）
T0008-R0022: evidence_state | RECEIVED_UNVERIFIED（學員提供無網址截圖） | RECEIVED_UNVERIFIED（轉貼截圖）
T0008-R0023: case_disposition | HOLD | HOLD
T0008-R0024: owner_role | 行政志工 A | 行政志工 B
T0008-R0025: next_action | 先取得明確同意並核實聯繫授權；合成內部檢視日 2026-10-26 再檢視是否可送出 | 合成內部檢視日 2026-10-20 檢視同意與身分缺件；補件前維持 HOLD
T0008-R0026: notes | 無第三方原件；不得寫成已得獎 | 截圖與另一貼文相似，尚未查證，不得指控
P0118: 提醒： 上表的「已填」只是格式示範。SYN- 開頭的案號、人名、日期、競賽與主辦單位都不是真實資料；表內日期、截圖情節、角色、同意狀態及流程均為虛構演練，不代表實際收件、簽署、搜尋、聯繫或追蹤。
P0119: 4.3 填寫要點
P0120: 先寫「學員主張」四個字，再寫內容。不要一開始就寫「獲獎案」。
P0121: claimed_result 只填學員說的，不填你希望的分數或名次。
P0122: 同意狀態不確定時填 UNKNOWN，不要空白；空白會被下一個人誤認為已同意。
P0123: next_action 一定要有日期與動詞，例如「2026-10-26 前電話確認」，不要寫「再處理」。
P0124: 5. Form B：向學員索取資料稿
P0125: SAMPLE TEMPLATE—NOT SENT  以下文字是可直接修改的樣板。本文件沒有實際寄出，也沒有模擬任何學員回覆。使用前請確認同意狀態、稱謂、協會名稱與回覆管道。
P0126: 5.1 書面索取稿（電子郵件／訊息均可）
P0127: 主旨：技能競賽結果佐證資料請託（案號：SYN-0102-CASE-01）
P0128: 您好，P-SYN-01：
P0129: 我們正在整理您提到「2026-08-22 示範盃技能競賽（合成名稱）佳作」的資料。為了確認競賽與結果，並避免誤用您的個人資料，想請您協助提供下列其中一項或多項：
P0130: 1. 主辦單位提供的獎狀影本或掃描檔（可遮住身分證號、地址、電話）。
P0131: 2. 主辦單位官方網站公告的結果頁連結，或公告截圖（請盡量包含網址與公告日期）。
P0132: 3. 主辦單位的官方聯絡窗口（單位名稱、官方電話或官方網站聯絡頁）。
P0133: 4. 您所屬組別、隊名或參賽名稱，以及可對照的參賽證明。
P0134: 您可以自行遮罩的資料： 身分證號、住址、電話、生日、簽名、其他參賽者姓名。我們不需要這些資料，也不會要求您提供。
P0135: 回覆方式： 請回覆本訊息，或將檔案交給本會行政窗口。若您不方便提供某一項，請直接說明，我們會記錄「未提供」，不會因此認定您沒有得獎。
P0136: 回覆期限： 本稿未送出。取得必要同意並由授權人實際寄出後，才從寄出日起算 7 個日曆天並填入實際日期；未寄出前不得填外部期限。
P0137: 同意選項（可複選）： 可複選第 1～4 項；第 5 項「不同意」不可與其他項目同時勾選。請只選擇您理解並同意的用途。
P0138: ☐ 1. 同意本會為本案作必要的內部整理與查核；不含對外聯繫或公開。
P0139: ☐ 2. 同意本會以最低必要資料向競賽主辦單位查證；聯絡方式與未遮罩資料不公開。
P0140: ☐ 3. 同意去識別化後供本會內部訓練成果審查及 TTQS 佐證檢視；不含公開發布。
P0141: ☐ 4. 明確同意公開下列資料（須逐項填寫資料、管道及期間）：資料範圍＿＿＿＿；公開管道＿＿＿＿；有效期間＿＿＿＿。
P0142: ☐ 5. 不同意；請停止尚未進行的查證，並依適用政策處理已保存資料。
P0143: Form B → Form A 對照： 每一勾選用途分別填入 consent_scope_status；1 對應 internal_use=GRANTED，2 對應 organizer_contact=GRANTED，3 對應 deidentified_review=GRANTED，4 對應 public_disclosure=GRANTED 並記資料範圍、管道及期間。未勾選用途填 NOT_GRANTED；表單尚未取得或內容不清楚填 UNKNOWN；撤回後填 WITHDRAWN 並記 withdrawal_date。只要任一授權條件不清楚，該用途維持 HOLD。單獨勾選「內部」不代表同意聯繫主辦或公開；不得從「可以拿去用」等含糊文字推定授權。
P0144: 不會因為您未提供而影響任何權益。 但若缺少可核對來源，我們可能無法完成查證，屆時會記錄為「暫緩」，不會寫成「未得獎」。本會也不保證查核結果、不保證任何評分、補助或後續機會。
P0145: 如有疑問，請與本會行政窗口聯繫，並告知案號 SYN-0102-CASE-01。
P0146: 謝謝您的協助。
P0147: （本稿為 SAMPLE TEMPLATE—NOT SENT，未實際寄出。）
P0148: 5.2 已填 SAMPLE 摘要（CASE-01）

[TABLE T0009]
T0009-R0001: 欄位 | 內容 | 說明
T0009-R0002: 收件人 | P-SYN-01（別名） | 不使用真實姓名
T0009-R0003: 案號 | SYN-0102-CASE-01 | 全程沿用
T0009-R0004: 競賽 | 示範盃技能競賽（合成名稱） | 學員自述
T0009-R0005: 日期 | 2026-08-22 | 待官方確認
T0009-R0006: 主張獎項 | 佳作 | 僅為主張
T0009-R0007: 已索取 | 獎狀影本、官方結果頁、主辦窗口 | 最少化
T0009-R0008: 回覆期限 | 未設定 | 未寄出前無外部期限；實際寄出後 7 個日曆天填入
T0009-R0009: 同意記錄狀態 | UNKNOWN | 未取得簽署；各用途均未授權
T0009-R0010: 同意範圍 | 未確認 | 不得推定任何用途
T0009-R0011: 公開 | NOT_GRANTED | 不得放入公開版
T0009-R0012: 目前證據狀態 | RECEIVED_UNVERIFIED | 已有無網址截圖線索，沒有第三方原件
T0009-R0013: 案件處置 | HOLD | 等待合法授權與可核來源
T0009-R0014: 寄送狀態 | 未送出 | 本文件不模擬實際寄送
P0150: 5.3 追蹤與提醒

[TABLE T0010]
T0010-R0001: 時點 | 動作 | 文字重點
T0010-R0002: 截止前 2 天 | 一次簡短提醒 | 「不確定您是否收到，若有困難可告訴我們」
T0010-R0003: 截止後 7 天 | 第一次提醒 | 重附缺件清單與案號
T0010-R0004: 截止後 21 天 | 第二次提醒 | 說明可能轉為暫緩，未來可補件
T0010-R0005: 截止後 30 天 | 轉 HOLD | 記錄「學員未回覆」，不寫「未獲獎」
P0152: 提醒稿同樣標 SAMPLE TEMPLATE—NOT SENT，不得假裝已寄出。
P0153: 5.4 不要寫的句子

[TABLE T0011]
T0011-R0001: 不要寫 | 建議改寫
T0011-R0002: 「請證明您真的得獎。」 | 「請提供可核對的官方來源或獎狀，我們會依程序確認。」
T0011-R0003: 「沒回覆就代表您沒得獎。」 | 「未回覆會先暫緩，未來仍可補件。」
T0011-R0004: 「一定要正本。」 | 「正本、影本或官方公告連結均可，視可核對程度處理。」
T0011-R0005: 「這是為了幫您加分。」 | 「這是為了確認資料正確，不保證任何評分結果。」
T0011-R0006: 「我們已經確認過了。」 | 「我們已完成初步檢視，尚待官方來源確認。」
P0155: 6. Form C：向主辦單位查證稿與電話腳本
P0156: SAMPLE TEMPLATE—NOT SENT  本節所有文字都是未送出樣板。文件沒有聯繫任何主辦單位，也沒有任何回覆。實際使用前，請先確認：同意範圍允許向主辦查證、協會對外聯繫角色已確認、查證管道是獨立取得的官方管道。
P0157: 6.1 查證前三分鐘
P0158: 1. 不要只用學員給的連結。 從主辦單位官方網站、政府機關登記資料、活動公告頁或正式公文，找到電話與網址。
P0159: 2. 把管道來源記下來。 哪個網站、哪一頁、什麼時候看到、誰找到的。
P0160: 3. 確認你要問什麼。 只問競賽存在、公告結果、組別、日期、獎項與得獎者是否可對照；不要問其他得獎者個資。
P0161: 4. 確認你可以說什麼。 不要自稱「協會已核准」；只說「本會正在進行內部資料確認」。
P0162: 5. 準備案號。 所有對話都以案號開頭，避免把不同案件混在一起。
P0163: 6.2 書面查證稿
P0164: 主旨：技能競賽公告結果查詢（案號：SYN-0102-CASE-01）
P0165: 您好：
P0166: 本會為辦理訓練成果資料確認，想請貴單位協助確認下列公開資訊。本函僅供本會內部查核，不會公開貴單位回覆內容，也不會要求提供其他參賽者個人資料。
P0167: 競賽名稱：示範盃技能競賽（合成名稱）
P0168: 競賽日期：2026-08-22
P0169: 組別／職類：照顧服務類／個人組
P0170: 本會學員參賽名稱：P-SYN-01（真實姓名只存於受限身分對照表，依已確認同意範圍核對）
P0171: 學員主張獎項：佳作
P0172: 想請貴單位確認：
P0173: 1. 貴單位是否於上述日期舉辦或公告該競賽？
P0174: 2. 該競賽是否設有上述組別？
P0175: 3. 公告結果是否列有「佳作」獎項？
P0176: 4. 公告所列得獎者，是否可與本函所附學員姓名或參賽名稱對照？
P0177: 5. 若方便，請提供公告頁連結、公告日期或公文文號，供本會記錄來源。
P0178: 若貴單位不便確認個人資料，也可以只確認「競賽存在、組別存在、獎項名稱與公告連結」，本會會據此記錄可查核的範圍。
P0179: 回覆方式：請回覆本函，或來電本會行政窗口。若需要正式函文或附件格式，請告知，我們會依貴單位流程補件。
P0180: SAMPLE TEMPLATE—NOT SENT（本文件未實際寄出。）
P0181: 6.3 電話腳本
P0182: 撥打前
P0183: 確認號碼來自官方網站或正式公告，不是學員轉貼的私人號碼。
P0184: 在紙上寫好：案號、競賽名稱、日期、組別、要問的五个問題。
P0185: 不要在公共場所大聲說出學員姓名；需要時只說「本會學員」。
P0186: 開場
P0187: 您好，我是○○協會（合成示例）的行政志工，姓○。耽誤您兩分鐘，我們正在確認一件訓練成果資料，案號是 SYN-0102-CASE-01。想請教貴單位 2026-08-22 示範盃技能競賽的公告結果，方便嗎？
P0188: 若對方問為什麼要問
P0189: 我們不會公開貴單位的回覆，也不會要求其他參賽者資料。只想確認競賽名稱、日期、組別、獎項與公告連結，避免我們把資料寫錯。
P0190: 核心問題（依序問，對方不答就跳過）
P0191: 1. 「請問貴單位是否在 2026-08-22 舉辦或公告這個競賽？」
P0192: 2. 「公告的組別有沒有『照顧服務類／個人組』？」
P0193: 3. 「公告結果有沒有列出『佳作』？」
P0194: 4. 「如果方便，公告上的得獎者姓名或隊名，能不能讓我們對照？我們可以提供學員姓名，只供核對。」
P0195: 5. 「請問公告頁的網址、公告日期或公文文號是什麼？我會記下來。」
P0196: 若對方要求身分或正式函文
P0197: 可以，我可以提供案號與本會聯絡方式。若需要正式函文，請告訴我收件窗口與格式，我們會補。學員的完整個資我不會在電話中提供，必要時以加密對照表另送。
P0198: 若對方表示不便確認個人
P0199: 沒關係，能不能只告訴我可公開的公告頁或公告編號？這樣我們會記錄「官方公告存在，個人對照未完成」，不會寫成已確認。
P0200: 收尾
P0201: 謝謝您。我確認一下我記到的內容：……（複述）。如果方便，請給我一個稱呼或單位窗口，我後續以書面補件。若我記錯，請糾正我。
P0202: 通話後
P0203: 當天完成紀錄，不靠記憶。
P0204: 把「對方說的」與「我推論的」分開寫。
P0205: 若主辦只提供口頭確認，記「口頭確認，待書面」，並維持 RECEIVED_UNVERIFIED 或 HOLD；即使有通話紀錄，口頭確認也不得單獨升為 VERIFIED_REAL，仍須取得可定位的書面或官方公告來源。
P0206: 6.4 查證紀錄表

[TABLE T0012]
T0012-R0001: 欄位 | 填法 | CASE-01 示範值
T0012-R0002: 案號 | 固定格式 | SYN-0102-CASE-01
T0012-R0003: 管道來源 | 官方網站／政府登記／公告頁／正式公文 | 尚未搜尋或定位（合成情境）
T0012-R0004: 管道取得方式 | 誰、何時、如何找到 | 未執行；取得同意及授權後才由指定角色依官方來源搜尋
T0012-R0005: 網址或頁面名稱 | 可重找的位置 | 未知；目前無網址或頁面名稱
T0012-R0006: 聯繫日期時間 | YYYY-MM-DD HH:MM | 未聯繫
T0012-R0007: 聯繫方式 | 電話／書面／表單 | 書面草稿已完成，未送出
T0012-R0008: 對方單位／角色 | 只記角色，不記私人手機 | 待聯繫
T0012-R0009: 主要問題 | 五項核心問題 | 競賽、日期、組別、獎項、公告連結
T0012-R0010: 回覆摘要 | 只寫對方實際說的 | 無（不得預填）
T0012-R0011: 回覆定位 | 公告編號／網址／公文號 | 無
T0012-R0012: 後續 | 下一步與日期 | 先確認明確同意及授權角色；之後才可決定是否送出；2026-10-26 為合成內部檢視日
T0012-R0013: 紀錄人 | 角色 | 獨立查證人（示例）
P0208: 注意： 上表沒有「已聯絡」或「已回覆」的示範值。為避免把演練誤認為真實互動，本文件不虛構任何主辦單位回覆、電話內容、公告編號或承辦人姓名。
P0209: 6.5 管道可信度判斷

[TABLE T0013]
T0013-R0001: 管道 | 可用程度 | 原因
T0013-R0002: 主辦單位官方網站公告頁 | 高 | 可定位、可重查
T0013-R0003: 政府機關登記或正式公文 | 高 | 發行者可確認
T0013-R0004: 主辦單位官方社群帳號 | 中 | 需確認帳號真偽與是否為正式公告
T0013-R0005: 學員提供的截圖 | 低 | 無從確認來源與是否變造
T0013-R0006: 學員轉貼的他人貼文 | 低 | 可能重複、過期或移花接木
T0013-R0007: 私人通訊軟體對話 | 低 | 難以定位、難以確認對方身分
P0211: 低可信度管道不是完全不能用，而是只能當線索，不能單獨成為 VERIFIED_REAL 的依據。
P0212: 7. Form D：來源真偽清單
P0213: 7.1 十四項查核

[TABLE T0014]
T0014-R0001: # | 查核項目 | 怎麼查 | 符合條件 | 不符或未知的處置
T0014-R0002: 1 | 管道是否獨立取得 | 從官方網站、政府登記或正式公告找，不只用學員連結 | 有獨立來源與取得紀錄 | 未知→先補管道，不得升為已驗證
T0014-R0003: 2 | 網域與聯絡資訊 | 比對官方網域、地址、電話 | 與主辦單位公開資訊一致 | 不一致→HOLD，查是否仿冒
T0014-R0004: 3 | 發行者身分 | 文件抬頭、署名、印章、承辦單位 | 可確認是競賽主辦或其授權單位 | 未知→HOLD
T0014-R0005: 4 | 公告或文件日期 | 公告頁日期、公文發文日、獎狀日期 | 與競賽時間合理相符 | 日期矛盾→HOLD
T0014-R0006: 5 | 競賽名稱與屆次 | 與官方公告逐字比對 | 名稱、屆次一致 | 名稱相似但屆次不同→HOLD
T0014-R0007: 6 | 競賽日期與地點 | 公告、獎狀、學員說法三方比對 | 日期一致；地點不矛盾 | 差一天先釐清；差很多→HOLD
T0014-R0008: 7 | 組別／職類 | 公告與獎狀比對 | 組別名稱可對應 | 不同組別→HOLD，必要時 REJECTED
T0014-R0009: 8 | 獎項名稱與名次 | 公告、獎狀比對 | 獎項確定，非「入圍」誤寫「佳作」 | 獎項不存在→REJECTED
T0014-R0010: 9 | 得獎者姓名或隊名 | 以受限身分對照表核對，不公開個資 | 姓名／隊名可對應，或主辦確認 | 對不上→HOLD；確定不同人→REJECTED
T0014-R0011: 10 | 內容一致性 | 檢查日期、規則、格式、用語有無矛盾 | 無明顯矛盾 | 有矛盾→HOLD，查是否變造
T0014-R0012: 11 | 檔案完整性 | 保留原檔、檢查後設資料、版本 | 原檔可開、無異常修改痕跡 | 只有截圖→RECEIVED_UNVERIFIED
T0014-R0013: 12 | 重複或轉載 | 查登錄表、比對檔案與公告 | 非重複使用他人文件 | 疑似重複→HOLD，交人類判斷
T0014-R0014: 13 | 同意與公開範圍 | 對照同意書 | 查證與揭露範圍清楚 | 不足→HOLD 對外揭露
T0014-R0015: 14 | 保存與可定位 | 檔名、資料夾、來源連結、取得日期 | 下一個人找得到 | 找不到→先補紀錄，不得結案
P0215: 7.2 證據狀態與案件處置
P0216: 證據狀態 evidence_state

[TABLE T0015]
T0015-R0001: 狀態 | 定義 | 必要條件 | 不可做的事
T0015-R0002: NOT_RECEIVED | 尚未收到任何可保存的來源材料；只有口述主張 | 無檔案、截圖或可定位來源 | 不得推定得獎或未得獎
T0015-R0003: RECEIVED_UNVERIFIED | 已收到檔案、截圖或來源線索，但尚未完成獨立查核 | 來源或關鍵事實未確認 | 不得宣稱已確認或公開
T0015-R0004: VERIFIED_REAL | 可定位的第三方正式來源及關鍵事實已完成查核 | 發行者、競賽、日期、組別、獎項、身分及完整性均可核 | 不代表訓練有功勞，也不代表可以公開
P0218: 案件處置 case_disposition

[TABLE T0016]
T0016-R0001: 處置 | 定義 | 使用條件 | 下一步
T0016-R0002: ELIGIBLE_FOR_HUMAN_REVIEW | 資料可送人類複核；不是核准或評分 | Form F 十項檢查全部為「是」，且沒有未解阻擋 | 由覆核人確認後送人類複核
T0016-R0003: HOLD | 暫緩，等待補件、授權或釐清 | 任一必要條件為「否」或「未知」，且沒有可靠反證 | 記缺項、責任角色、內部檢視日及下一步
T0016-R0004: REJECTED | 拒收該證據項目 | 有可靠查核證明來源虛假、無關、重複或非該獎項 | 記理由與覆核者；不延伸為對人的判斷
P0220: 兩欄不得互相代用。例如，收到一張無網址截圖時，evidence_state=RECEIVED_UNVERIFIED；若同意或來源未完成查核，case_disposition=HOLD。HOLD 與 REJECTED 永遠不是 evidence_state。
P0221: 7.3 已填 SAMPLE：CASE-02 的截圖查核
P0222: 此為合成案例。CASE-02 只收到一張轉貼截圖，沒有官方連結、沒有獎狀原檔、沒有同意書。以下結果用來說明「收到但未驗證」與「HOLD」的差別。

[TABLE T0017]
T0017-R0001: # | 查核項目 | 結果 | 說明
T0017-R0002: 1 | 管道獨立取得 | 未知 | 只有轉貼截圖，無原始網址
T0017-R0003: 2 | 網域與聯絡資訊 | 未知 | 截圖未顯示可辨識網域
T0017-R0004: 3 | 發行者身分 | 未知 | 無法確認帳號或公告單位
T0017-R0005: 4 | 公告日期 | 未知 | 截圖沒有公告日期
T0017-R0006: 5 | 競賽名稱與屆次 | 未知 | 截圖可見字樣但無官方來源，名稱及屆次均未核實
T0017-R0007: 6 | 競賽日期 | 未知 | 截圖自述 2026-08-22，無官方對照
T0017-R0008: 7 | 組別 | 未知 | 截圖顯示團體組，無法確認
T0017-R0009: 8 | 獎項 | 未知 | 截圖顯示冠軍，無法確認
T0017-R0010: 9 | 得獎者身分 | 不符／未知 | 截圖列「示範隊」，學員表示是暱稱，無對照證明
T0017-R0011: 10 | 內容一致性 | 未知 | 排版與轉載痕跡無法判斷
T0017-R0012: 11 | 檔案完整性 | 未知 | 無原檔、無後設資料
T0017-R0013: 12 | 重複或轉載 | 未知 | 與另一貼文相似，尚未查證，不得指控
T0017-R0014: 13 | 同意與公開範圍 | 不符 | 未簽署，僅口頭說「可以拿去用」
T0017-R0015: 14 | 保存與可定位 | 不符 | 無網址、無原始檔
P0224: 綜合： RECEIVED_UNVERIFIED，案件狀態 HOLD。原因不是「證明造假」，而是「無法確認＋同意不足＋身分對不上」。在沒有可靠反證前，不能用 REJECTED。
P0225: 7.4 CASE-01 的查核狀態
P0226: CASE-01 已收到學員提供的一張無網址截圖，但沒有第三方原件、官方結果或主辦回覆。evidence_state=RECEIVED_UNVERIFIED，案件處置為 HOLD。可先將截圖線索記入 Form D，將未確認欄位標為「未知」；第三方正式來源到件後再完成來源查核。不得把截圖當成獎項已驗證，也不得把「沒有第三方原件」寫成「沒有收到任何來源」。
P0227: 8. Form E：訓練關聯矩陣
P0228: 8.1 填寫原則
P0229: 1. 左邊寫課程實際發生的事，不是課程簡介裡的好聽話。
P0230: 2. 中間寫可追溯的紀錄：出席、練習、評量、作品、講師觀察。
P0231: 3. 右邊寫競賽實際要求，不要用「應該差不多」帶過。
P0232: 4. 時間序要清楚：課程在前、競賽在後，才有基本關聯條件；但時間在前不等於因果。
P0233: 5. 最後一欄一定寫「可推論到哪裡」，避免把關聯寫成保證。
P0234: 8.2 矩陣欄位

[TABLE T0018]
T0018-R0001: 欄位 | 說明
T0018-R0002: 課程目標 | 課程文件上的具體能力描述
T0018-R0003: 教授與練習 | 實際教了什麼、練了什麼、練多久
T0018-R0004: 評量紀錄 | 分數、作品、通過標準、講師觀察
T0018-R0005: 競賽技能 | 競賽規則或職類要求的技能
T0018-R0006: 時間序 | 課程結束到競賽之間隔
T0018-R0007: 替代解釋 | 課前經驗、其他培訓、競賽難度、團隊因素
T0018-R0008: 其他佐證 | 學員回饋、講師紀錄、作品
T0018-R0009: 可推論上限 | 只能說關聯、不能說因果的具體寫法
P0236: 8.3 已填 SAMPLE：CASE-01

[TABLE T0019]
T0019-R0001: 課程目標 | 教授與練習 | 評量紀錄 | 競賽技能 | 時間序 | 替代解釋 | 其他佐證 | 可推論上限
T0019-R0002: 能依標準流程完成基本照顧操作 | 翻身、移位、清潔、安全注意事項；第 2～3 週反覆演練 | 第 3 週技能演練 78/100（合成）；講師記錄「流程完整、速度待加強」 | 未取得競賽規則；主張只提及照顧服務類，實際競賽技能未知（待補） | 課程 2026-04-10 結束，競賽 2026-08-22，間隔約 4 個月 | 學員課前已有照顧經驗；可能參加其他單位培訓；競賽難度與當日題目未知 | 講師紀錄、學員自述、課程出席紀錄 | 只能說「課程技能與競賽職類有重疊，且課程在前」；不能說「本課程造成佳作」
P0238: 8.4 已填 SAMPLE：CASE-02

[TABLE T0020]
T0020-R0001: 課程目標 | 教授與練習 | 評量紀錄 | 競賽技能 | 時間序 | 替代解釋 | 其他佐證 | 可推論上限
T0020-R0002: 增進進階溝通與異常處理 | 情境演練、同儕回饋 | 出席 14/18（合成）；無正式評量分數 | 團體組競賽，細項未知 | 課程 2026-02-15 結束，競賽 2026-08-22，間隔約 6 個月 | 團隊其他成員貢獻不明；課外練習未知；競賽規則未取得 | 僅有學員自述 | 資料不足，不能建立可追溯關聯；不得寫「課程訓練出冠軍」
P0240: 8.5 可說與不可說

[TABLE T0021]
T0021-R0001: 可說 | 不可說
T0021-R0002: 「課程目標與競賽職類有部分技能重疊。」 | 「因為上了這門課，所以得獎。」
T0021-R0003: 「課程結束後約四個月參加競賽。」 | 「訓練直接造成獲獎。」
T0021-R0004: 「學員在課程評量中完成基本流程。」 | 「課程績效顯著提升。」
T0021-R0005: 「目前缺少講師紀錄與競賽規則，關聯待補。」 | 「沒有紀錄也能看出關聯。」
T0021-R0006: 「這是關聯證據，不是因果證明。」 | 「有獎狀就代表訓練有效。」
P0242: 8.6 關聯強度怎麼記

[TABLE T0022]
T0022-R0001: 強度 | 條件 | 用法
T0022-R0002: 無 | 沒有課程紀錄或技能對不上 | 不列入訓練關聯
T0022-R0003: 弱 | 只有學員自述，技能名稱相似 | 只能當背景，不能支持結論
T0022-R0004: 中 | 有課程目標、出席或練習紀錄，技能可對應，時間合理 | 可寫「有關聯證據」，仍需揭露限制
T0022-R0005: 較強 | 上述＋講師觀察＋評量紀錄＋競賽規則可對照＋替代解釋已檢查 | 可作為 Form F 的較強訓練關聯證據；仍須來源、身分、獎項、完整性、用途同意及 Form F 其餘檢查全部通過
P0244: 本文件不設「強到可以自動通過」的等級；最終仍由人類看完整脈絡。
P0245: 9. Form F：案例決定表
P0246: 9.1 決定表

[TABLE T0023]
T0023-R0001: 檢查項 | 是 | 否 | 未知 | 備註
T0023-R0002: 1. 已收到可辨識來源？ | ☐ | ☐ | ☐ | 只有口述不算
T0023-R0003: 2. 來源管道可獨立取得？ | ☐ | ☐ | ☐ | 不只用學員截圖
T0023-R0004: 3. 發行者與競賽主辦可確認？ | ☐ | ☐ | ☐ | 官方網站／公文
T0023-R0005: 4. 競賽名稱、日期、組別一致？ | ☐ | ☐ | ☐ | 逐項比對
T0023-R0006: 5. 獎項確定？ | ☐ | ☐ | ☐ | 不是「入圍」誤寫
T0023-R0007: 6. 得獎者身分可對應？ | ☐ | ☐ | ☐ | 以受限身分對照表
T0023-R0008: 7. 同意與揭露權限具備？ | ☐ | ☐ | ☐ | 含對外範圍
T0023-R0009: 8. 訓練關聯有可追溯證據？ | ☐ | ☐ | ☐ | Form E
T0023-R0010: 9. 無重複、變造或明顯矛盾？ | ☐ | ☐ | ☐ | 有疑慮即 HOLD
T0023-R0011: 10. 來源可定位、可保存？ | ☐ | ☐ | ☐ | 檔名、連結、日期
P0248: 判定：
P0249: ☐ 可送人類複核（不是核准，也不是評分）
P0250: ☐ HOLD（暫緩，補件或等人類判斷）
P0251: ☐ REJECTED（只拒收該證據項目）
P0252: 理由（必填，三行內）：
P0253: 缺少項目：
P0254: 責任角色：
P0255: 期限：
P0256: 覆核人：
P0257: 下一步：
P0258: 9.2 判定門檻

[TABLE T0024]
T0024-R0001: Form F 條件 | 案件處置 | 操作規則
T0024-R0002: Form F 十項檢查全部為「是」 | ELIGIBLE_FOR_HUMAN_REVIEW | 前五項為來源與賽事核心條件；其餘五項（得獎者身分、用途同意、訓練關聯、無重複或矛盾、來源可定位保存）也須全數通過。此狀態仍不是核准或評分
T0024-R0003: 任一項為「否」或「未知」，且沒有可靠反證 | HOLD | 記錄缺項、責任角色、內部檢視日及下一步；不得送出為已完成
T0024-R0004: 官方或其他可靠來源證明不是該獎項、不是本人、重複冒用或變造 | REJECTED | 只拒收該證據項目，保留查核依據及覆核人
T0024-R0005: 來源真實，但公開用途沒有明確同意 | HOLD（公開用途） | 來源狀態仍可為 VERIFIED_REAL；不得公開。只在另有明確內部用途授權時才能作該範圍內的內部處理
T0024-R0006: 已收到截圖但沒有可獨立確認的官方來源 | RECEIVED_UNVERIFIED ＋ HOLD | 證據狀態與案件處置分欄記錄，不得把截圖當成官方來源
T0024-R0007: 尚未收到任何材料，只有口述 | NOT_RECEIVED ＋ HOLD | 不得寫成「未得獎」
P0260: Form F 的答案只能使用「是／否／未知」；不得用「部分」代替。只有十項全部為「是」才可送人類複核。
P0261: 9.3 已填 SAMPLE：CASE-01

[TABLE T0025]
T0025-R0001: 檢查項 | 結果 | 說明
T0025-R0002: 1. 已收到可辨識來源 | 是 | 已收到學員提供的無網址截圖；只證明收到線索，不是官方來源
T0025-R0003: 2. 管道可獨立取得 | 否（尚未搜尋） | 沒有已核實管道；取得同意與授權後才搜尋
T0025-R0004: 3. 發行者可確認 | 未知 | 尚無官方文件
T0025-R0005: 4. 賽事細節一致 | 未知 | 待官方比對
T0025-R0006: 5. 獎項確定 | 未知 | 「佳作」僅為主張
T0025-R0007: 6. 身分可對應 | 未知 | 尚無官方名單
T0025-R0008: 7. 同意與權限 | 否 | 沒有簽署或明確同意；各用途均未授權
T0025-R0009: 8. 訓練關聯 | 未知 | 有課程紀錄，但競賽技能與講師完整觀察未核實
T0025-R0010: 9. 無重複或變造 | 未知 | 尚未取得原檔
T0025-R0011: 10. 可定位保存 | 否 | 沒有第三方來源、官方連結或已執行查證紀錄
P0263: 示範判定： HOLD（第三方來源待查）。目前已收到學員提供的無網址截圖，故證據狀態為 RECEIVED_UNVERIFIED；不得寫成已得獎、已查證或可公開。
P0264: 缺少項目： 官方結果頁或主辦確認、獎狀影本、得獎者身分對照、競賽規則。
P0265: 責任角色： 承辦人整理；獨立查證人聯繫；覆核人確認。
P0266: 內部檢視： 2026-10-26 為合成內部覆核日，不是外部期限；未取得同意與聯繫授權前不得追蹤或對外聯繫。
P0267: 下一步： 先取得明確同意並核實對外聯繫角色；只有在兩項均完成後，授權人才能決定是否送出 Form C。收到來源後才填 Form D。
P0268: 本判定是流程示範，不構成協會核准、不構成得獎認定、不構成評分。
P0269: 9.4 已填 SAMPLE：CASE-02

[TABLE T0026]
T0026-R0001: 檢查項 | 結果 | 說明
T0026-R0002: 1. 已收到可辨識來源 | 是 | 已收到轉貼截圖；只證明收到線索，不是官方來源
T0026-R0003: 2. 管道可獨立取得 | 否 | 無原始網址
T0026-R0004: 3. 發行者可確認 | 否 | 無法確認
T0026-R0005: 4. 賽事細節一致 | 未知 | 日期、組別均無官方對照
T0026-R0006: 5. 獎項確定 | 未知 | 截圖稱冠軍
T0026-R0007: 6. 身分可對應 | 否 | 隊名與學員資料對不上
T0026-R0008: 7. 同意與權限 | 否 | 未簽署；口頭範圍不明
T0026-R0009: 8. 訓練關聯 | 否 | 無正式評量與競賽規則
T0026-R0010: 9. 無重複或變造 | 未知 | 與另一貼文相似，未查證
T0026-R0011: 10. 可定位保存 | 否 | 無網址、無原檔
P0271: 示範判定： HOLD（同意不足＋身分不足）。證據狀態 RECEIVED_UNVERIFIED；不得寫成已得獎、已查證、已拒絕或造假。
P0272: 缺少項目： 同意書、官方公告、獎狀、隊名對照、競賽規則。
P0273: 責任角色： 承辦人補同意；獨立查證人找官方來源；覆核人檢查身分。
P0274: 內部檢視： 2026-10-20 為合成內部覆核日，不是外部期限；同意及身分缺件未補前維持 HOLD。
P0275: 下一步： 以 Form B 重新說明同意範圍；若學員不願提供，停止對外查證並依政策處理資料。
P0276: 10. 完整合成案例
P0277: 界線聲明： 以下兩案都是虛構的流程演練。為避免把演練誤認為真實紀錄，本文件不虛構任何送出、回覆、簽章、核准或得獎證明。所有對外文字都是未送出樣板；所有日期、名稱、分數、對話與判定都是合成資料。
P0278: 10.1 CASE-01：已收截圖、第三方來源待查
P0279: 基本資料

[TABLE T0027]
T0027-R0001: 項目 | 內容
T0027-R0002: 案號 | SYN-0102-CASE-01
T0027-R0003: 學員代號 | P-SYN-01
T0027-R0004: 課程 | SYN-COURSE-01「基礎照顧服務技能班（合成課程）」
T0027-R0005: 課程期間 | 2026-03-02～2026-04-10，36 小時
T0027-R0006: 競賽 | 示範盃技能競賽（合成名稱）
T0027-R0007: 競賽日期 | 2026-08-22
T0027-R0008: 主辦 | （合成）示範技能發展協會
T0027-R0009: 組別 | 照顧服務類／個人組
T0027-R0010: 主張獎項 | 佳作
T0027-R0011: 主張來源 | 2026-10-05 電話自述＋一張無網址截圖
T0027-R0012: 同意 | 未取得簽署或明確授權；不得對外查證或公開
T0027-R0013: 目前證據 | 僅有學員提供的無網址截圖（線索）；無第三方原件、官方公告或主辦回覆
T0027-R0014: 證據狀態 | RECEIVED_UNVERIFIED
T0027-R0015: 案件處置 | HOLD（待合法授權與真實來源）
P0281: 處理經過（全部為合成演練）
P0282: 1. 2026-10-05：學員來電，說自己參加競賽得到佳作，並傳來一張沒有網址的截圖。承辦人當日建立案號，沒有承諾「會列入成果」。
P0283: 2. 2026-10-06：合成流程原擬進行同意說明，但示範狀態設定為尚未取得簽署或明確授權；沒有實際同意書、簽名或對話紀錄。
P0284: 3. 2026-10-07：承辦人完成 Form B 草稿，列出可接受文件與遮罩方式；完成 Form C 草稿，指定五項查證問題。兩份都未送出。
P0285: 4. 2026-10-07：合成流程預定在取得同意及授權後搜尋主辦單位官方管道；本示範未實際搜尋、定位網址、撥打或寄出。
P0286: 5. 2026-10-20：合成內部檢視日（非資料截止日、非外部期限）；尚未授權聯繫，證據狀態維持 RECEIVED_UNVERIFIED，案件處置維持 HOLD。
P0287: 6. 2026-10-26：合成內部再檢視日；只有取得明確同意與聯繫授權後，才決定是否寄送及設定真正期限。
P0288: 目前判定
P0289: HOLD。不是「已得獎」，也不是「未得獎」。尚無可核對來源，且沒有明確同意或授權角色。下一步先確認同意及授權；完成前，索取稿和查證稿都不得送出。
P0290: 若補件，怎麼變

[TABLE T0028]
T0028-R0001: 新資料 | 可能變化 | 仍不能做
T0028-R0002: 收到官方結果頁，列有可對照姓名與佳作 | RECEIVED_UNVERIFIED→查核→可能 VERIFIED_REAL | 不能說課程造成獲獎
T0028-R0003: 主辦書面確認競賽與獎項，但名單只列隊名 | 可在身分及其他關鍵事實核實後將來源設為 VERIFIED_REAL；案件處置仍須另判 | 不能公開未同意的姓名
T0028-R0004: 只有學員自製獎狀圖 | 維持 HOLD | 不能升為已驗證
T0028-R0005: 主辦確認無此獎項 | REJECTED（該項） | 不能延伸成協會零績效
P0292: 10.2 CASE-02：同意與身分不足，維持 HOLD
P0293: 基本資料

[TABLE T0029]
T0029-R0001: 項目 | 內容
T0029-R0002: 案號 | SYN-0102-CASE-02
T0029-R0003: 學員代號 | P-SYN-02
T0029-R0004: 課程 | SYN-COURSE-02「照顧服務進階班（合成課程）」
T0029-R0005: 課程期間 | 2026-01-05～2026-02-15
T0029-R0006: 競賽 | 示範盃技能競賽（合成名稱）
T0029-R0007: 競賽日期 | 2026-08-22
T0029-R0008: 組別 | 照顧服務類／團體組
T0029-R0009: 主張獎項 | 冠軍
T0029-R0010: 主張來源 | 2026-09-30 他人轉貼截圖，無原始連結
T0029-R0011: 同意 | 未取得簽署或可用授權；情境文字不是實際對話或同意紀錄
T0029-R0012: 目前證據 | 一張轉貼截圖；無官方公告、無獎狀、無名單對照
T0029-R0013: 證據狀態 | RECEIVED_UNVERIFIED
T0029-R0014: 案件狀態 | HOLD（同意不足＋身分不足）
P0295: 處理經過（全部為合成演練）
P0296: 1. 2026-09-30：承辦人收到轉貼截圖，內容顯示「示範隊」獲得團體組冠軍。沒有網址、沒有公告日期。
P0297: 2. 2026-10-01：承辦人建立案號，向學員確認是否為本人。學員說「示範隊」是暱稱，但沒有提供隊員名單或參賽證明。
P0298: 3. 2026-10-02：合成情境以含糊的「可以拿去用」作為待判斷文字；這不是實際對話或同意紀錄，不能視為授權，也不代表發生過聯繫。
P0299: 4. 2026-10-05：承辦人比對截圖與另一則貼文，發現排版相似，但無法確認是否同一來源；記「疑似重複，未查證」，沒有公開指控。
P0300: 5. 2026-10-12：第二次追問同意與隊名對照，未取得回覆。
P0301: 6. 2026-10-20：維持 HOLD。不是 REJECTED，因為沒有可靠證據證明造假；也不是 VERIFIED_REAL，因為關鍵事實都無法確認。
P0302: 目前判定
P0303: HOLD。阻擋事項有兩項：同意不足、身分無法對應。第三步才是查真偽；在同意與身分未補前，不向主辦查個人資料，也不公開截圖。
P0304: 若補件，怎麼變

[TABLE T0030]
T0030-R0001: 新資料 | 可能變化 | 仍不能做
T0030-R0002: 簽署同意＋隊名與學員可對照 | 可進入查核，仍為 RECEIVED_UNVERIFIED | 不能直接寫冠軍
T0030-R0003: 官方公告列出隊名與獎項 | 可能 VERIFIED_REAL | 不能說課程造成冠軍
T0030-R0004: 官方公告顯示不同隊伍 | REJECTED（該項） | 不能公開指責
T0030-R0005: 學員撤回同意 | 停止處理，依政策刪除 | 不能保留公開版本
P0306: 10.3 兩案比較

[TABLE T0031]
T0031-R0001: 項目 | CASE-01 | CASE-02
T0031-R0002: 有無第三方原件 | 無 | 無
T0031-R0003: 有無學員截圖 | 有，無網址 | 有，轉貼
T0031-R0004: 同意 | 未取得簽署 | 未取得簽署或明確授權
T0031-R0005: 身分對照 | 待官方名單 | 隊名對不上
T0031-R0006: 證據狀態 | RECEIVED_UNVERIFIED | RECEIVED_UNVERIFIED
T0031-R0007: 案件狀態 | HOLD | HOLD
T0031-R0008: 主要阻擋 | 來源未到 | 同意＋身分
T0031-R0009: 下一步 | 先確認同意與聯繫授權，再決定是否送出 | 補同意與隊名；補件前不對外查證
T0031-R0010: 已驗證得獎 | 0 | 0
P0308: 10.4 這個示範沒有證明什麼
P0309: 沒有證明任何真實競賽存在。
P0310: 沒有證明任何學員得獎。
P0311: 沒有證明協會有或沒有得獎。
P0312: 沒有證明課程有效或無效。
P0313: 沒有證明評核會給幾分。
P0314: 沒有協會核准、沒有主辦回覆、沒有簽章。
P0315: 11. 計算與解讀
P0316: 11.1 來源查證與人類複核資格分開計算
P0317: 來源已驗證案件數 = count(unique case_id where all are true)
  (1) 可定位的官方原件或官方結果已取得並查核
  (2) 競賽及獎項事實獲確認
  (3) 得獎者身分一致
  (4) 來源檔案完整性已檢查

可送人類複核案件數 = count(unique case_id where Form F 第 1～10 項全部為「是」)
P0318: 來源是否已驗證，不以是否取得公開揭露權限決定。若官方來源、獎項及身分已查證，但公開同意不足，來源仍可計入「來源已驗證」；公開用途另列 HOLD，不可公開。訓練關聯及用途同意影響案件能否送人類複核，不能回頭把來源查證數改成零。五項核心條件是必要門檻，但只有 Form F 十項全數為「是」才可列 ELIGIBLE_FOR_HUMAN_REVIEW。
P0319: 11.2 本示範資料集

[TABLE T0032]
T0032-R0001: 項目 | 數值 | 說明
T0032-R0002: 合成待審主張 | 2 | CASE-01、CASE-02
T0032-R0003: 已收學員／轉貼截圖線索 | 2 | 均非第三方原件
T0032-R0004: 已收第三方原件 | 0 | 兩案都沒有
T0032-R0005: 來源已驗證案件 | 0 | 無可查核官方來源
T0032-R0006: 身分及獎項均已確認 | 0 | 均未確認
T0032-R0007: Form F 十項全是 | 0 | 兩案均有未知或否
T0032-R0008: 可送人類複核案件 | 0 | 全十項門檻未達
T0032-R0009: 來源查證完成率 | 0/2=0% | 來源已驗證案件÷待查證主張數；不是結案率
P0321: 11.3 這個 0 不是什麼
P0322: 不是協會實績。 這是兩個虛構案件的流程演練。
P0323: 不是獲獎率。 分母不是所有參賽者，也不是所有課程學員。
P0324: 不是評核分數。 本文件不打分數，也不預測 2 分或 4 分。
P0325: 不是「協會沒有得獎」。 沒有資料不等於沒有事實；UNKNOWN 不能寫成 0。
P0326: 不是「學員說謊」。 缺件只表示查核未完成。
P0327: 不是「訓練無效」。 沒有關聯證據只表示目前不能寫因果。
P0328: 11.4 可選的流程指標

[TABLE T0033]
T0033-R0001: 指標 | 算法 | 本示範 | 用途
T0033-R0002: 主張收件率 | 已建案數÷收到主張數 | 2/2=100% | 確認沒有漏案
T0033-R0003: 有效同意取得率 | 至少一項明確且符合本次用途的有效同意案件÷合成建案數 | 0/2=0% | 兩個合成案均未取得可用授權
T0033-R0004: 查證管道定位率 | 已核實定位獨立管道÷合成建案數 | 0/2=0% | 兩案都沒有實際搜尋或定位
T0033-R0005: 第三方來源取得率 | 已取得官方來源÷已建案 | 0/2=0% | 顯示真正瓶頸
T0033-R0006: 來源查證率 | 來源已驗證案件÷待查證主張數 | 0/2=0% | 不包含訓練效果或公開授權
T0033-R0007: 全條件可送人類複核率 | Form F 十項全是案件÷已建案數 | 0/2=0% | 決策門檻，不是得獎率
T0033-R0008: 平均停留天數 | 各案停留天數平均 | 依實際紀錄 | 找出逾期
P0330: 這些都是內部流程指標，不是協會對外績效，也不是 TTQS 評分。
P0331: 11.5 什麼時候可以更新數字
P0332: 只有在以下事件發生時才更新，且要保留舊版：
P0333: 收到新來源。
P0334: 完成一次獨立查證。
P0335: 身分或賽事細節被更正。
P0336: 同意範圍變更或撤回。
P0337: 判定改變。
P0338: 年度覆核。
P0339: 不要因為「快要報名截止」或「長官想看成果」而提前把 HOLD 改成已驗證。
P0340: 12. 案例登錄表與索引／替換清冊
P0341: 12.1 案例登錄表

[TABLE T0034]
T0034-R0001: case_id | 學員代號 | 競賽 | 主張獎項 | evidence_state | case_disposition | 同意範圍狀態 | 來源定位 | 下一步 | response_due_date／internal_review_date | 負責角色
T0034-R0002: SYN-0102-CASE-01 | P-SYN-01 | 示範盃（合成） | 佳作 | RECEIVED_UNVERIFIED | HOLD | 四種用途均 UNKNOWN | 學員提供無網址截圖；無官方來源 | 先取得符合用途的明確同意，再決定是否索取來源 | 外部期限：未設定；內部檢視：2026-10-26 | 合成角色 A
T0034-R0003: SYN-0102-CASE-02 | P-SYN-02 | 示範盃（合成） | 冠軍 | RECEIVED_UNVERIFIED | HOLD | 四種用途均 UNKNOWN | 僅有轉貼截圖，無官方網址 | 補合法同意與隊名對照；補件前不聯繫主辦 | 外部期限：未設定；內部檢視：2026-10-20 | 合成角色 B
P0343: 維護規則
P0344: 一案一行，不把兩案寫在同一行；替換清冊使用 SYN-0102-CASE-01、SYN-0102-CASE-02 完整案號，共用競賽／主辦資料標兩案，跨案控制列標 GLOBAL。
P0345: evidence_state 只用三個來源狀態，case_disposition 只用三個處置值；「處理中」不是狀態，放在下一步。
P0346: 期限一到就更新，不讓表格變成裝飾。
P0347: 每月花 15 分鐘看一次逾期與 HOLD 案件。
P0348: 12.2 索引／替換清冊
P0349: 一個合成事實一行。未來取得真實資料時，逐行替換，不要整份文件改寫。doc_id 固定為 0102。

[TABLE T0035]
T0035-R0001: fact_id | case_id | doc_id | 文件位置 | 合成值 | 替換來源需求 | 負責角色 | 狀態
T0035-R0002: F-0102-001 | GLOBAL | 0102 | 封面 | 協會現況不主張 | 登記資料、章程、現行名冊 | 理事會／秘書 | AWAITING_REAL_SOURCE
T0035-R0003: F-0102-002 | GLOBAL | 0102 | 2.3 | 授權人「待依章程及授權名冊確認」 | 授權名冊、會議紀錄 | 理事會 | AWAITING_REAL_SOURCE
T0035-R0004: F-0102-003 | SYN-0102-CASE-01 | 0102 | Form A | P-SYN-01 | 學員同意與身分對照 | 記錄保管人 | SYNTHETIC_PLACEHOLDER
T0035-R0005: F-0102-004 | SYN-0102-CASE-01 | 0102 | Form A | SYN-COURSE-01 | 課程編號、課表、時數 | 訓練承辦 | SYNTHETIC_PLACEHOLDER
T0035-R0006: F-0102-005 | SYN-0102-CASE-01／SYN-0102-CASE-02 | 0102 | Form A | 示範盃技能競賽（合成） | 官方競賽名稱與屆次 | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0007: F-0102-006 | SYN-0102-CASE-01／SYN-0102-CASE-02 | 0102 | Form A | （合成）示範技能發展協會 | 主辦單位正式名稱 | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0008: F-0102-007 | SYN-0102-CASE-01 | 0102 | Form A | 2026-08-22 | 合成競賽日期；非公告日期 | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0009: F-0102-008 | SYN-0102-CASE-01 | 0102 | Form A | 佳作 | 官方獎項名稱 | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0010: F-0102-009 | SYN-0102-CASE-01 | 0102 | Form C | 尚未搜尋、未定位任何頁面 | 實際官方網址與取得日（僅在授權後） | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0011: F-0102-010 | SYN-0102-CASE-01 | 0102 | Form E | 技能演練 78/100 | 原始評量紀錄 | 講師／訓練承辦 | SYNTHETIC_PLACEHOLDER
T0035-R0012: F-0102-011 | SYN-0102-CASE-01 | 0102 | Form E | 講師記錄「流程完整」 | 講師原始觀察紀錄 | 講師 | SYNTHETIC_PLACEHOLDER
T0035-R0013: F-0102-012 | SYN-0102-CASE-02 | 0102 | Form A | P-SYN-02 | 學員同意與身分對照 | 記錄保管人 | SYNTHETIC_PLACEHOLDER
T0035-R0014: F-0102-013 | SYN-0102-CASE-02 | 0102 | Form A | SYN-COURSE-02 | 課程編號、課表、時數 | 訓練承辦 | SYNTHETIC_PLACEHOLDER
T0035-R0015: F-0102-014 | SYN-0102-CASE-02 | 0102 | Form A | 冠軍 | 官方獎項與名單 | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0016: F-0102-015 | SYN-0102-CASE-02 | 0102 | Form A | 「示範隊」 | 正式隊名與隊員對照 | 學員／主辦 | SYNTHETIC_PLACEHOLDER
T0035-R0017: F-0102-016 | SYN-0102-CASE-02 | 0102 | Form D | 截圖與另一貼文相似 | 原始連結與出處 | 獨立查證人 | AWAITING_REAL_SOURCE
T0035-R0018: F-0102-017 | SYN-0102-CASE-02 | 0102 | Form E | 出席 14/18 | 出席紀錄 | 訓練承辦 | SYNTHETIC_PLACEHOLDER
T0035-R0019: F-0102-018 | GLOBAL | 0102 | 13 | 保留期限「另定」 | 法規、同意書、協會政策 | 記錄保管人 | AWAITING_REAL_SOURCE
T0035-R0020: F-0102-019 | SYN-0102-CASE-01 | 0102 | Form A／10.1 | 2026-10-05；電話自述及無網址截圖情節 | 真實收件日期、通道與原始來源（如有） | 記錄保管人 | SYNTHETIC_PLACEHOLDER
T0035-R0021: F-0102-020 | SYN-0102-CASE-01 | 0102 | Form A／Form E／10.1 | 2026-03-02～2026-04-10；36 小時 | 課程名冊、課表及簽到紀錄 | 訓練承辦 | SYNTHETIC_PLACEHOLDER
T0035-R0022: F-0102-021 | SYN-0102-CASE-01 | 0102 | Form A／10.1 | 個人組；合成競賽日期 2026-08-22；主張佳作 | 官方競賽規則、結果頁與原件 | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0023: F-0102-022 | SYN-0102-CASE-01 | 0102 | Form A／10.1 | 未取得簽署或明確同意；未發送任何文字 | 真實同意文件及實際寄送紀錄（若發生） | 記錄保管人 | SYNTHETIC_PLACEHOLDER
T0035-R0024: F-0102-023 | SYN-0102-CASE-01 | 0102 | 10.1／12.1 | 2026-10-20、2026-10-26 合成內部檢視日 | 實際內部檢視紀錄；不可當外部期限 | 承辦角色 | SYNTHETIC_PLACEHOLDER
T0035-R0025: F-0102-024 | SYN-0102-CASE-01 | 0102 | 4／10.1 | P-SYN-01、合成角色 A | 真實身分與在職角色（有權限時） | 記錄保管人 | SYNTHETIC_PLACEHOLDER
T0035-R0026: F-0102-025 | SYN-0102-CASE-02 | 0102 | Form A／10.2 | 2026-09-30；他人轉貼截圖情節 | 真實收件來源及原始連結（如有） | 記錄保管人 | SYNTHETIC_PLACEHOLDER
T0035-R0027: F-0102-026 | SYN-0102-CASE-02 | 0102 | Form A／10.2 | 2026-01-05～2026-02-15；課程日期 | 課程名冊、課表及簽到紀錄 | 訓練承辦 | SYNTHETIC_PLACEHOLDER
T0035-R0028: F-0102-027 | SYN-0102-CASE-02 | 0102 | Form A／10.2 | 團體組；合成競賽日期 2026-08-22；主張冠軍 | 官方競賽規則、結果頁、隊員名單 | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0029: F-0102-028 | SYN-0102-CASE-02 | 0102 | 10.2 | 未取得簽署或明確授權；含糊措辭僅屬合成情節 | 真實同意文件；不得以口頭含糊語句替代 | 記錄保管人 | SYNTHETIC_PLACEHOLDER
T0035-R0030: F-0102-029 | SYN-0102-CASE-02 | 0102 | 10.2／12.1 | 2026-09-30 至 2026-10-20 合成時間線 | 真實收件、聯繫、處理及覆核紀錄 | 承辦角色 | SYNTHETIC_PLACEHOLDER
T0035-R0031: F-0102-030 | SYN-0102-CASE-02 | 0102 | Form A／10.2 | P-SYN-02、示範隊、合成角色 B | 真實身分、正式隊名及在職角色 | 記錄保管人 | SYNTHETIC_PLACEHOLDER
T0035-R0032: F-0102-031 | SYN-0102-CASE-01 | 0102 | Form E／11 | 78/100；講師觀察「流程完整、速度待加強」 | 原始評量表、評量規準及講師紀錄 | 講師／訓練承辦 | SYNTHETIC_PLACEHOLDER
T0035-R0033: F-0102-032 | SYN-0102-CASE-02 | 0102 | Form E／11 | 出席 14/18；無正式評量分數 | 簽到紀錄與實作評量表 | 訓練承辦 | SYNTHETIC_PLACEHOLDER
T0035-R0034: F-0102-033 | GLOBAL | 0102 | 11.4 | 主張收件 2/2；有效同意 0/2；管道定位 0/2；官方來源 0/2；來源查證 0/2；Form F 十項全是 0/2 | 依真實完整母體重算並保存明細 | 品質管理者 | SYNTHETIC_PLACEHOLDER
T0035-R0035: F-0102-034 | GLOBAL | 0102 | 4、6、13 | 行政志工、承辦人、覆核人、查證人等合成角色 | 以實際職務授權與利益衝突覆核替換 | 協會授權人 | SYNTHETIC_PLACEHOLDER
T0035-R0036: F-0102-035 | SYN-0102-CASE-01 | 0102 | Form E／10.1 | 個人組照顧服務類技能描述及課程技能對照 | 官方競賽規則、真實課程目標與評量規準 | 訓練承辦／講師 | SYNTHETIC_PLACEHOLDER
T0035-R0037: F-0102-036 | SYN-0102-CASE-02 | 0102 | Form D／10.2 | 截圖版面相似、可能重複的情節 | 原始檔、來源連結及可核對的比對紀錄 | 獨立查證人 | SYNTHETIC_PLACEHOLDER
T0035-R0038: F-0102-037 | GLOBAL | 0102 | Form B／Form C | 所有未送出信件、電話話術與追蹤文字 | 實際核准文字、授權角色及真實寄送／聯繫記錄 | 授權聯繫人 | SYNTHETIC_PLACEHOLDER
T0035-R0039: F-0102-038 | GLOBAL | 0102 | Form D／Form F | NOT_RECEIVED、RECEIVED_UNVERIFIED、HOLD 等示範狀態 | 逐項對應真實來源與覆核記錄後重判 | 覆核人 | SYNTHETIC_PLACEHOLDER
T0035-R0040: F-0102-039 | GLOBAL | 0102 | 11.4 | 示範分子分母與 0/2 驗證率 | 依真實母體及逐案來源重算並保留明細 | 品質管理者 | SYNTHETIC_PLACEHOLDER
P0351: 狀態用語
P0352: SYNTHETIC_PLACEHOLDER：目前是合成值，不可當事實。
P0353: AWAITING_REAL_SOURCE：等待真實來源或政策確認。
P0354: VERIFIED_REAL：已用真實來源替換並查核。
P0355: RETIRED：已失效或不再使用，保留紀錄。
P0356: 12.3 替換流程
P0357: 1. 找到真實來源，先影印或保存原檔。
P0358: 2. 在替換清冊找到對應 fact_id。
P0359: 3. 填「替換來源需求」與「負責角色」，不要直接覆蓋舊值。
P0360: 4. 建立新版本，保留舊版與替換日期。
P0361: 5. 重新跑一次 Form D 與 Form F；不要假設換了名字就自動通過。
P0362: 6. 更新案例登錄表與年度覆核紀錄。
P0363: 13. 歸檔、存取與保存
P0364: 13.1 兩個資料夾就好

[TABLE T0036]
T0036-R0001: 資料夾 | 放什麼 | 誰可以看
T0036-R0002: 受限區 | 同意書、真實姓名對照、獎狀原檔、通訊紀錄、未遮罩截圖 | 記錄保管人、覆核人；必要時承辦人
T0036-R0003: 審閱區 | 去識別化摘要、Form A～F 的公開版、案例登錄表 | 參與審查者；不含個資
P0366: 不要把所有東西都放在共用雲端硬碟的「公開」資料夾。檔案名稱不要放真實姓名，例如：
P0367: 下列檔名僅示範命名規則；檔案並未建立，也不代表已取得同意或第三方來源。
P0368: SAMPLE_SYN-0102-CASE-01_FormD_TEMPLATE.pdf
SAMPLE_SYN-0102-CASE-01_consent_request_TEMPLATE.pdf
P0369: 13.2 受限身分對照表
P0370: 對照表只存於受限區；至少包含 learner_ref、真實姓名、聯絡方式、consent_status、consent_scope、withdrawal_date、allowed_use、同意日期及備註。每一用途分開記錄，不得用「已簽署」這類單一狀態推定所有用途均獲授權。
P0371: 優先使用協會已核准且具存取控制的儲存方式。若只能使用檔案，採用具密碼保護的檔案格式；檔案與密碼分開傳遞，密碼以電話或另一個已核實的管道提供，不放在同一封郵件或同一個共用資料夾。無法確認檔案保護或存取權限時，不放入真實身分資料，先保留於適當受限的正式來源並標 UNKNOWN。
P0372: 不放在公開版，不貼在群組，不夾在一般公文附件。只有執行已授權核對的人員才開啟，並記存取紀錄。
P0373: 同意撤回時立即記 withdrawal_date、停用相關用途；依適用法律、同意內容與協會政策決定刪除或去識別化，不推定可繼續使用。
P0374: 13.3 保管紀錄

[TABLE T0037]
T0037-R0001: 示範日期（非實際收件） | 檔案／來源樣例 | 假設來源 | 預定存放位置 | 樣例版本 | 樣例限制 | 合成角色
T0037-R0002: 2026-10-05 | CASE-01 截圖情境 | 合成學員訊息情節 | 受限區（若真實取得且有依據） | SAMPLE | 無原檔；非實際收件 | 合成角色 A
T0037-R0003: 2026-10-06 | CASE-01 同意狀態 | 無簽署；尚待確認 | 不建立同意書 | SAMPLE | 不存在已簽署文件 | 記錄保管人角色
T0037-R0004: 2026-09-30 | CASE-02 轉貼截圖情境 | 合成轉貼情節 | 受限區（若真實取得且有依據） | SAMPLE | 無網址；非實際收件 | 合成角色 B
P0376: 上表是合成情境示例，沒有真實文件、收件或存取事件。正式使用時，應刪除示範行，只登錄實際收到日期、來源與保管位置。
P0377: 13.4 存取紀錄

[TABLE T0038]
T0038-R0001: 日期時間（實際使用時填） | 角色（實際填） | 實際查看內容 | 實際目的 | 是否複製
T0038-R0002: 待實際操作時填寫 | 填實際角色 | 填實際查看內容 | 填實際目的 | 是／否
P0379: 以上是空白欄位樣板，沒有實際存取紀錄。正式使用時，每次查看都要能回答「誰在什麼時候看了什麼、為什麼」。
P0380: 13.5 公開版怎麼遮

[TABLE T0039]
T0039-R0001: 要遮 | 怎麼處理
T0039-R0002: 真實姓名 | 用 P-SYN-01 代號
T0039-R0003: 身分證號、生日、地址 | 完全移除
T0039-R0004: 電話、電子郵件 | 移除或只留角色
T0039-R0005: 簽名、印章 | 遮罩或另存受限區
T0039-R0006: 其他參賽者姓名 | 遮罩或移除
T0039-R0007: 獎狀編號 | 若可反向查個資，遮罩
T0039-R0008: 主辦承辦人姓名 | 只寫「活動組人員」
P0382: 公開版可以保留：競賽名稱、日期、組別、獎項、課程名稱、技能對照、去識別化的訓練紀錄。保留的目的是讓讀者理解證據，不是讓讀者追人。
P0383: 13.6 保存期限
P0384: 本文件不自行發明年限。保存期限記：
P0385: 待依現行法規、同意書範圍及協會政策確認。
P0386: 在確認前，採最小保存：
P0387: 只留完成查核所需資料。
P0388: 同意撤回或目的消失時，啟動檢視。
P0389: 每年覆核一次，決定續存、去識別化或刪除。
P0390: 刪除前確認沒有法定保存義務或爭議處理需求。
P0391: 13.7 備份與版本
P0392: 至少一份備份，放在另一個受限位置。
P0393: 每次更新檔名加版本與日期，例如 v02_20261020。
P0394: 不要把舊版刪掉，直到新版本確認可讀。
P0395: 年度覆核時抽樣開啟檔案，確認沒有損壞。
P0396: 13.8 外洩或誤傳
P0397: 建議內部目標（不是法律期限）：
P0398: 1. 發現後立即停止分享，移除公開連結。
P0399: 2. 24 小時內通知記錄保管人與覆核人。
P0400: 3. 保留事件紀錄：什麼資料、多少人看到、如何發生。
P0401: 4. 72 小時內完成初步影響評估與補救。
P0402: 5. 依協會政策與適用法規決定是否通知當事人。
P0403: 6. 事後修改流程，不只寫檢討。
P0404: 14. 例外與拒收規則
P0405: 14.1 逐項門檻

[TABLE T0040]
T0040-R0001: 情境 | 暫緩或拒收門檻 | 判定 | 責任角色 | 記錄位置欄位 | 期限 | 後續動作
T0040-R0002: 尚未收到任何材料 | 只有口述，沒有檔案、截圖或可定位來源 | evidence_state=NOT_RECEIVED；case_disposition=HOLD | 承辦人 | Form A evidence_state、case_disposition、next_action | 30 天 | 提醒、補件、轉長期 HOLD
T0040-R0003: 只收到無網址截圖 | 截圖已收到，但沒有可獨立查核的官方來源 | evidence_state=RECEIVED_UNVERIFIED；case_disposition=HOLD | 承辦人 | Form A evidence_state、case_disposition、來源定位 | 30 天 | 索取原件或官方來源；不得稱為已驗證
T0040-R0004: 主辦不回應 | 已用獨立管道聯繫但無回覆 | HOLD | 獨立查證人 | Form C 回覆摘要、日期 | 30 天 | 改書面、請學員自行申請
T0040-R0005: 發行者無法確認 | 無官方網域、無署名、無公文號 | HOLD | 獨立查證人 | Form D #2、#3 | 14 天 | 找官方管道，不採私人連結
T0040-R0006: 賽事名稱或屆次不符 | 名稱相似但屆次不同 | HOLD | 查證人＋覆核人 | Form D #5 | 14 天 | 請主辦釐清；確定不同賽事則拒收
T0040-R0007: 日期或組別不符 | 官方與主張差很多 | HOLD | 查證人 | Form D #6、#7 | 14 天 | 比對公告；必要時請學員說明
T0040-R0008: 獎項不存在 | 官方公告無此獎項 | REJECTED（該項） | 覆核人 | Form D #8、Form F 理由 | 完成查核後 7 天 | 保留官方說法；通知學員禮貌說明
T0040-R0009: 身分確定不是本人 | 官方名單與學員確定不同 | REJECTED（該項） | 覆核人 | Form D #9 | 7 天 | 不公開指控；依政策處理
T0040-R0010: 身分只是對不上 | 可能是暱稱、隊名或資料缺漏 | HOLD | 承辦人 | Form A notes、Form D #9 | 30 天 | 補隊名、參賽證明、主辦對照
T0040-R0011: 疑似重複 | 同一文件出現在多案 | HOLD／合併 | 記錄保管人 | 登錄表、Form D #12 | 14 天 | 合併案號；不重複計算
T0040-R0012: 疑似變造 | 字體、日期、印章矛盾 | HOLD | 覆核人 | Form D #10、#11 | 立即 | 停止流通、保留原檔、人類判斷
T0040-R0013: 確定變造 | 有可靠反證 | REJECTED | 覆核人＋核准人（若已授權） | Form F 理由、保管紀錄 | 7 天 | 依政策處理；不公開細節
T0040-R0014: 沒有同意 | 未簽署或只口頭 | HOLD | 記錄保管人 | Form A consent_status | 14 天 | 補同意；不補則停止對外
T0040-R0015: 同意不含公開 | 只同意內部查核 | HOLD（對外） | 覆核人 | Form A consent_scope | 立即 | 公開版不得使用；可做內部摘要
T0040-R0016: 訓練關聯不足 | 無課程紀錄或技能對不上 | HOLD | 承辦人＋講師 | Form E「可推論上限」 | 30 天 | 補紀錄；不足則只列背景
T0040-R0017: 來源真實但缺訓練關聯 | 官方已確認，但無課程證據 | HOLD | 覆核人 | Form F #8 | 30 天 | 不得寫成績效；可保留來源
T0040-R0018: 全部條件成立 | Form F 十項檢查全部為「是」 | ELIGIBLE_FOR_HUMAN_REVIEW | 承辦人擬稿、覆核人確認 | Form F 全部欄位 | 7 天 | 交人類複核，不是自動核准
P0407: 14.2 拒收的三個原則
P0408: 1. 只拒收證據項目，不拒收人。 寫「該項證據不成立」，不要寫「這個學員不誠實」。
P0409: 2. 沒有反證就不拒收。 缺件、對不上、待回覆，都是 HOLD，不是 REJECTED。
P0410: 3. 拒收要留理由與覆核人。 沒有理由的拒收，下一個人無法判斷是否合理。
P0411: 14.3 不能做的事
P0412: 不能把 HOLD 當成 REJECTED，也不能把 HOLD 當成通過。
P0413: 不能把「沒有回覆」寫成「沒有得獎」。
P0414: 不能把「有獎狀」寫成「訓練績效顯著」。
P0415: 不能把「主辦口頭說有」直接寫成「已驗證」；即使有通話紀錄，仍須取得可定位的書面或官方公告來源，並完成 Form D 關鍵欄位查核。
P0416: 不能把其他獎項、其他年度、其他組別的證書移花接木。
P0417: 不能在未確認授權時，以協會名義對外發布。
P0418: 15. 快速檢查、維護與版本
P0419: 15.1 送件前十二項
P0420: ☐ 案號唯一，沒有和別的案混用。
P0421: ☐ evidence_state 與 case_disposition 分欄填寫，沒有把 HOLD／REJECTED 填入證據狀態。
P0422: ☐ 學員代號與真實姓名分開存放。
P0423: ☐ 同意狀態已填，不是空白。
P0424: ☐ 已取得獨立官方管道，不只靠學員截圖。
P0425: ☐ Form D 的關鍵項沒有「未知」卻被寫成「已驗證」。
P0426: ☐ 競賽名稱、日期、組別、獎項逐項對過。
P0427: ☐ 得獎者身分有對照，不是「看起來像」。
P0428: ☐ Form E 有寫「可推論上限」，沒有寫因果。
P0429: ☐ Form F 的判定與理由一致。
P0430: ☐ 缺少的項目、責任角色、期限都有寫。
P0431: ☐ 公開版已去識別化。
P0432: ☐ 登錄表與替換清冊已更新。
P0433: 15.2 每月十五分鐘維護
P0434: 1. 看登錄表有沒有逾期。
P0435: 2. 看 HOLD 案件有沒有新資料。
P0436: 3. 看同意有沒有撤回。
P0437: 4. 看公開版是否還含個資。
P0438: 5. 看替換清冊有沒有「合成值」被誤用。
P0439: 6. 把本月新學到的問題寫進版本紀錄。
P0440: 15.3 年度覆核
P0441: 抽樣 2～3 案，重跑 Form D 的關鍵項。
P0442: 確認官方連結還有效。
P0443: 確認同意範圍沒有過期或變更。
P0444: 確認保存期限與政策仍適用。
P0445: 確認沒有把 UNKNOWN 寫成 0。
P0446: 更新版本與替換清冊。
P0447: 15.4 版本紀錄

[TABLE T0041]
T0041-R0001: 版本 | 日期 | 修改內容 | 修改角色 | 備註
T0041-R0002: R08 | 2026-10-23 | 承接 R07 的語意修正；將 0/2 合成示範界線併入最後提醒，移除孤立末頁 | 文件維護角色 | SAMPLE / SYNTHETIC；未新增真實得獎資料
P0449: 15.5 最後提醒
P0450: 這份文件最重要的不是表格，而是停下來的地方。本文件所示 0/2=0% 僅為兩個合成案件的流程示範，不能當成協會實績、獲獎率或評核分數；真實資料未取得合法來源前維持 UNKNOWN。
P0451: 沒有來源，停在 NOT_RECEIVED。
P0452: 有來源但沒查核，停在 RECEIVED_UNVERIFIED。
P0453: 有查核但缺同意、身分、訓練關聯或權限，停在 HOLD。
P0454: 五項核心條件是必要門檻；只有 Form F 十項檢查全部為「是」，才列 ELIGIBLE_FOR_HUMAN_REVIEW。
P0455: 只有可靠反證，才用 REJECTED。


## Required output
1) exact candidate SHA acknowledgment; verdict `PASS`, `PARTIAL`, or `FAIL` and `SEMANTIC_SCOPE_ONLY`.
2) criteria table covering all seven controls and the full Blueprint acceptance checks, with exact locators.
3) blockers and nonblocking issues; sample-boundary and case arithmetic; neighbor requirement comparison; title-hidden genre check.
4) State model identity only from native OpenCode session metadata, otherwise UNKNOWN. No fallback is authorized; do not infer from prose.
5) Declarations: `VISUAL_SCOPE=NOT_REVIEWED`, `TECHNICAL_SCOPE=NOT_REVIEWED_BY_REVIEWER`, `FORMAL_ACCEPTANCE=NOT_GRANTED`, `REAL_EVIDENCE=NOT_VERIFIED`.
