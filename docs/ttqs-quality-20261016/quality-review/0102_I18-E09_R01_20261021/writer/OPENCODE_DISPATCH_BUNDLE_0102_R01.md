## PART 1 — Writer assignment

# OpenCode v2 Writer 任務包 0102 I18-E09 R01

## 工作範圍

只撰寫一份完整、實際可用的繁體中文文件正文，供 Microsoft Word 排版：`0102` / `I18-E09` / 專案索引 `110`。文件類型是「技能競賽獲獎證據取得、來源真偽查核、訓練關聯分析與案例登錄工具」。請輸出完整 Markdown 正文；不得建立、修改或搜尋其他檔案。不要讀取整個 E:\TTQS，也不要使用檔案工具、Computer Use、瀏覽器或其他模型服務。

## 隔離來源與 SHA

- 唯一來源包：`source/SOURCE_PACKET_0102_I18-E09_R01.md`，SHA-256 `1c71d7095d32c31dacf450b0069e0c4ab3d7d2b9f296e38827cfff9976a7f767`。
- 唯一 Blueprint：`source/UNIQUE_BLUEPRINT_0102_I18-E09_R01.md`，SHA-256 `6ddf1fb585eb24144dfc544034d74e9fb9e02c742521083150f4087357e8bc8a`。
- 請把這兩個來源視為完整界線，不要自行補造真實協會、競賽、得獎、第三方原件、姓名、簽名、核准或聯絡回覆。
- 官方原始來源定位：佐證資料表 p.7；評核表 p.4。獲獎只是一項佐證例示；不得宣稱單一獎項保證 2 分或 4 分。

## 交付要求

1. 以讀者能立刻操作為準，建議正文 8,000–12,000 個中文字。不要縮成提綱或泛用說明。輸出完整文件，不要先解釋你準備如何寫。
2. 首頁明確標示 `SAMPLE / SYNTHETIC 示範文件`、`非原始點協會真實得獎、核准、競賽或第三方原件`，列文件用途、對應要求、使用者及正確的停止條件。把工程 SHA 和 CLI 資訊留在文件外，不得寫入 Word 正文。
3. 依專屬 Blueprint 完成端到端流程：學員主張收件 → 個資/同意及最少化 → 向競賽主辦單位索取 → 以獨立取得的官方聯絡管道查證 → 核對活動/日期/組別/獎項/匿名身分 → 記錄原件來源及保管 → 比對課程目標、訓練紀錄與技能 → 做有限度結論 → HOLD/REJECT/待人類核准。要有逾期未回、資料不一致、疑似重複/偽造等分支。
4. 提供可直接使用的表格及完整已填 SAMPLE：收件表、向學員索取稿、主辦方查證稿/電話腳本、來源真偽清單、訓練關聯矩陣、案例決定表、索引/替換清冊。空表之外，另有完整 SAMPLE 案例。所有發送稿均標 `SAMPLE TEMPLATE—NOT SENT`。
5. 使用兩個固定合成案例：`SYN-0102-CASE-01`、`SYN-0102-CASE-02`。兩案都沒有已收/已認證的第三方原件；案例一是待索取，案例二因同意/身分不足而 HOLD。不得寫成已得獎或已查證。示範內部工作量計算：兩筆合成待審主張、已驗證 0，流程結案率 `0/2=0%`；必須標明這不是協會實績、不是獲獎率、不是評核分數，也不能把 0 解讀為協會沒有得獎。
6. 必須區分 `NOT_RECEIVED`、`RECEIVED_UNVERIFIED`、`VERIFIED_REAL`、`HOLD`、`REJECTED`；只有官方原件/可核的官方結果、身分一致、獎項確定、訓練關聯有證據且揭露權限具備時，才可列「可送人類複核」。缺證不得轉為通過或協會零績效。
7. 逐一提供拒收/暫緩門檻、責任角色、記錄位置欄位、期限、後續動作。無法確認協會現行授權人/職務時用「待依章程及授權名冊確認」，不要造現任人名或委員會。
8. 文風自然、面向小型協會行政志工，步驟明確、低維護成本。所有 SAMPLE 事實在正文中有顯著標示，並使它們能被替換清冊追溯。不能把 0100/0101 自評/雷達文件內容改標題複製過來；目前沒有任何共用 REAL case_id。
9. 最後只輸出正文 Markdown，禁止回傳檔案建立聲稱、工具自評 PASS、模型身分宣稱或外部原件已取得等說法。
---
## PART 2 — Source packet

# 0102 來源包 I18-E09 技能競賽獲獎證據

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

- GitHub PR #92 / branch `work/ttqs-one-document-quality-contract-20261016` live HEAD at source capture: `4012f92d6d0c9d051388bcefefc9c0123421596a` (candidate branch, not formal acceptance).
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
---
## PART 3 — Unique Blueprint

# UNIQUE BLUEPRINT 0102 I18-E09 R01

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
5. Form A, case intake: unique case ID, pseudonymous learner ref, course ID/date and source, competition title/date/organizer, exact claimed result, claim origin, consent scope/date, evidence requested, due date, current evidence state.
6. Form B, participant source request: complete ready-to-send draft with purpose, accepted documents/official links, permitted redaction, deadline, response channel, consent choice, no penalty/no-guarantee language. Clearly marked unissued SAMPLE template.
7. Form C, organizer verification request/script: ready-to-send text and call checklist using independently obtained official contact information; ask only to confirm competition identity, published result, category, date and listed awardee reference; record channel, date/time, handler, reply/source locator. Mark all drafts as not sent.
8. Form D, source authenticity checklist: official domain/document provenance, issuer identity, publication date, event/date/category consistency, name/alias match held privately, original-file integrity/hash, external confirmation, tamper/duplicate check, privacy/consent, evidence locator. Status options: NOT_RECEIVED, RECEIVED_UNVERIFIED, VERIFIED_REAL, HOLD, REJECTED; no PASS without every required predicate.
9. Form E, training-linkage matrix: actual course learning objective → taught skill → practice/assessment record → competition skill/result → temporal sequence → alternative explanations → corroboration → bounded inference. Explicitly separate association, temporal order and causation.
10. Form F, case decision sheet: eligible source? authentic? correct person? award? linked training? consent/authority? disposition and reason; evidence used, missing item, owner role, due date, reviewer and next action. Sample approval language must be `示範判定`; no real approval.
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

Use `case_id=SYN-0102-CASE-01` and `SYN-0102-CASE-02`. All names/events/claims/dates are invented for workflow demonstration. For both cases, no third-party original has been received, independently checked, or approved for disclosure. Hence `verified_award_count=0`; with two synthetic claims due for review, `closure_rate=0/2=0%`. The calculation only demonstrates a control metric. It is not a real association outcome, award result, or TTQS score. Do not manufacture an award certificate, winner list, organizer reply, signature or real institution name.

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
---
