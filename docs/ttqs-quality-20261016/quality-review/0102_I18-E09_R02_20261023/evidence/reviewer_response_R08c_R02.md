# Independent semantic review — R08c vs current R02

## 1) Candidate acknowledgment and verdict

- Exact candidate bound for this review: DOCX SHA-256 `84c279d09484b88724dd59ae8a5155cb8d0be284133258e166269a80c26c67b4` (97,846 bytes); extracted body SHA-256 `a3943a63596b4b51c5560b43c4f28b8e9ba86276edec4fd7099ab37275f24eca` (455 paragraph elements, 41 tables → packet lists T0001–T0041, P0001–P0455 with empty-paragraph gaps).
- Source binding: current R02 packet SHA-256 `54d9c05f70b4fef993bd92b656694030878a236e1a2d0c6a21af5d24d94fa1bd`; current unique Blueprint R02 SHA-256 `d6ab10107f42d6f913e1c94df45c8cd179babaa2603a8a7e628c2db78a0cce75`. R01/older remote sources not substituted. No verdict imported from any other candidate SHA.
- Hashes are acknowledged as bound by the packet; they were not recomputed (tool use prohibited), so byte-level identity is outside this review.
- **Verdict: `PASS` — `SEMANTIC_SCOPE_ONLY`** (no blockers; two sub-items rated PARTIAL are nonblocking, listed in §3).

## 2) Criteria table

### Seven explicit R02 controls

| # | Control | Result | Exact locators |
|---|---|---|---|
| 1 | evidence_state restricted to NOT_RECEIVED / RECEIVED_UNVERIFIED / VERIFIED_REAL; case_disposition separate (ELIGIBLE_FOR_HUMAN_REVIEW / HOLD / REJECTED) | PASS | T0007-R0023, T0007-R0024 (allowed-value sets); T0015-R0002–R0004; T0016-R0002–R0004; P0220 ("兩欄不得互相代用… HOLD 與 REJECTED 永遠不是 evidence_state"); T0024-R0006, T0024-R0007; T0040-R0002, T0040-R0003; samples T0008-R0022/R0023, T0027-R0014/R0015, T0029-R0013/R0014, T0031-R0006/R0007; checklist P0421 |
| 2 | Form A separates response_due_date and internal_review_date; no invented external due date before a real request is sent | PASS | T0007-R0021 ("實際寄出後才填…未寄出填 未設定"), T0007-R0022; T0008-R0020 ("未設定（Form B 未送出）"), T0008-R0021 (2026-10-26 / 2026-10-20); T0009-R0008; P0136; T0034-R0002/R0003 ("外部期限：未設定；內部檢視…"); P0266, P0274 ("不是外部期限"); T0006 + P0079 (targets labeled internal only) |
| 3 | Consent per purpose (internal, organizer verification, de-identified TTQS review, explicit public) with scope/date/withdrawal/allowed use; public authorization names data, channel, period; absent consent stays UNKNOWN/NOT_GRANTED | PASS | T0007-R0014–R0019 (per-purpose values GRANTED/NOT_GRANTED/UNKNOWN/WITHDRAWN; "不得以單一「已簽」代替"); T0008-R0013–R0018 (four uses UNKNOWN both cases); P0137–P0143 (options 1–4, mapping internal_use/organizer_contact/deidentified_review/public_disclosure; P0141 data scope/channel/period fields); T0009-R0009–R0011; T0034-R0002/R0003; T0017-R0014; T0040-R0014, T0040-R0015; P0370 |
| 4 | Form F ten 是／否／未知 checks; all ten 是 required for ELIGIBLE_FOR_HUMAN_REVIEW; five core conditions necessary but not sufficient | PASS | T0023-R0002–R0011 (exactly 10 rows, three answer columns); P0260 ("只能使用「是／否／未知」…十項全部為「是」"); T0024-R0002 (first five = core; items 6–10 enumerated: 身分、用途同意、訓練關聯、無重複/矛盾、來源可定位保存); P0318; P0454; filled T0025, T0026 (no all-yes → HOLD); T0032-R0007/R0008 |
| 5 | Source verification measured independently of disclosure authorization and training linkage; formulas do not conflate source verified / eligibility / association performance | PASS | P0317 (source-verified count = 4 predicates: official source checked, award confirmed, identity match, file integrity — no consent, no training link); eligibility counted separately = Form F 1–10 all 是; P0318 (explicit independence: 公開同意不足不回頭把來源查證數改成零); T0033-R0006 ("不包含訓練效果或公開授權"), T0033-R0007 (separate threshold metric); P0321–P0327 (0 is not performance/score) |
| 6 | CASE-01 URL-less screenshot = RECEIVED_UNVERIFIED + HOLD; neither sample case has a third-party original; sample verified award count zero | PASS | P0226; P0263; T0008-R0022/R0023; T0027-R0013/R0014/R0015; T0031-R0002 ("有無第三方原件 無｜無"), T0031-R0010 ("已驗證得獎 0｜0"); T0032-R0004/R0005/R0008/R0009 |
| 7 | Full IDs SYN-0102-CASE-01/02 used; shared facts marked for both cases; cross-case rows marked GLOBAL | PASS | P0344 (maintenance rule verbatim); T0034-R0002/R0003 (full IDs); T0035-R0004…R0040 (per-case rows full IDs; F-0102-005/006 shared competition/organizer = both case IDs); GLOBAL rows F-0102-001, -002, -018, -033, -034, -037, -038, -039; full IDs in templates P0127, P0145, P0164, P0187; records T0027-R0002, T0029-R0002 |

### Blueprint R02 acceptance checks

| Check | Result | Exact locators |
|---|---|---|
| Identity: doc 0102 / I18-E09 / index 110 / printed serial UNKNOWN / title / SAMPLE-SYNTHETIC status | PASS (printed-serial note below) | T0001-R0002–R0006 (version R08c), T0001-R0007/R0008; P0001, P0002; T0001-R0002 & R0004 state 0102/110 are not official serials (see note N5) |
| Genre = third-party acquisition + authenticity + training linkage + register (not certificate/success story) | PASS | T0001-R0007; P0007; §4–§9 (P0112–P0260); T0014 (14 checks); T0018; T0034; T0035 |
| Operable end-to-end without further interpretation | PASS | P0033–P0041; P0073–P0075 flow; T0005 (10 steps + stop points); T0040 (17 thresholds); P0419–P0432 |
| Required outline items 1–15 present | PASS | Cover/guide P0001–P0041; boundary §1 (T0003); roles §2 (T0004); flow §3 (branches A–F P0081–P0111 incl. timeout P0081, suspicious source P0096); Form A §4; Form B §5; Form C §6 (independent channel P0158, call checklist P0182–P0205); Form D §7; Form E §8; Form F §9; worked cases §10; computation §11; registers §12; filing/retention §13 (P0384–P0385 no invented period); exceptions/checklist/version §14–15 |
| Required tables (intake, ≥8-check authenticity, linkage matrix, decision mapping, replacement register, two filled cases, unsent request texts) | PASS | T0007/T0008; T0014 (14 checks) + T0015/T0016; T0018–T0020; T0040 (covers missing original, issuer failure, identity mismatch, no award, duplicate, no consent, missing linkage, authentic record); T0035 (fact_id/case_id/doc_id/location/value/source/role/state); T0008 + T0025/T0026 + T0027/T0029; P0125/P0147, P0156/P0180 |
| Sample boundary & arithmetic: 2 claims, 0 third-party originals, 0 verified, 0 eligible, 0/2=0%, not closure/performance | PASS | T0032-R0002–R0009; P0317–P0318; P0450; T0033 (process KPIs, P0330 disclaimer); T0031-R0010 |
| Rejection/hold conditions incl. integrity-unknown, reply-pending, unauthorized publication; missing source never becomes zero | PASS | T0040-R0002–R0018; P0101, P0408–P0410; P0032, P0050, P0325, P0413; T0024-R0004 |
| 2-point vs 4-point qualification accurate | PASS | P0017, P0018, P0019, P0051–P0054; T0021-R0006 |
| No fabricated real event/winner/certificate/authorization/signature/approval; `示範判定` used | PASS | P0002–P0004, P0118, P0156, P0208, P0277; P0263, P0271 ("示範判定"); P0063–P0065 (authorization UNKNOWN fixed text); T0012-R0010 ("不得預填"); T0037-R0003; P0308–P0314 |
| No historical 0102 body reuse / no 0102_122 artifact use | PASS (semantic; see note N8) | No exam-coaching, return-rate, or 122-prefix content anywhere; identity fixed at 0102+I18-E09+110 (T0001-R0002–R0004); no survey/109, thank-you/111, acquisition-rate/112 material |
| Real evidence UNKNOWN; formal acceptance NOT_GRANTED | PASS | T0001-R0009; P0450; T0035-R0002/R0003/R0019 (`AWAITING_REAL_SOURCE`); P0385 |
| **R08c revision-label traceability** (cover/footer labels only vs R08) | **PARTIAL (nonblocking)** | T0001-R0006 = "R08c", but version log T0041-R0002 latest row = "R08 | 2026-10-23"; no R08c row. Footer label not present in the text extraction (out of extraction scope) |
| **Form F field completeness** (evidence used, response_due_date + internal_review_date as labeled fields) | **PARTIAL (nonblocking)** | Form F fields P0252–P0257 use generic "期限：" and have no explicit "使用證據" field; substance is carried by T0025/T0026 說明 columns, P0263–P0267, P0271–P0275 (internal review date stated, external due left unset). Full date split present in Form A/register: T0007-R0021/R0022, T0034 |

## 3) Blockers, nonblocking issues, sample boundary, neighbors, title-hidden genre

**Blockers: none.** All seven controls and all seven Blueprint acceptance criteria are satisfied semantically.

**Nonblocking issues**
- **N1** P0205 pairs an evidence_state value with a disposition value in one construction ("維持 RECEIVED_UNVERIFIED 或 HOLD"), which reads as interchangeability; P0220, T0024-R0006 and P0421 elsewhere enforce strict separation, so this is loose phrasing, not a control breach.
- **N2** Short forms "CASE-01/CASE-02" appear in headings and column labels — P0148, P0221, P0225, P0278, P0292, T0012-R0001 header, T0031-R0001 headers, T0037-R0002/R0004. Every identity-bearing record uses the full ID (T0027-R0002, T0029-R0002, T0034, T0035), and P0344 mandates full IDs; shorthand is not used as a case_id value.
- **N3** Disposition tokens carry qualifiers: "HOLD（公開用途）" T0024-R0005, "HOLD（對外）" T0040-R0015, "HOLD／合併" T0040-R0011, "REJECTED（該項）" T0040-R0008 / P0263 context. Base values are from the permitted set; qualifiers scope them.
- **N4** T0025-R0003 answer cell reads "否（尚未搜尋）" — token is 否 with an inline annotation; no "部分" answer appears in T0023/T0025/T0026, consistent with P0260.
- **N5** The identity table never states `printed_checkbox_serial=UNKNOWN` verbatim; it only asserts 0102 and 110 are not official serials (T0001-R0002, T0001-R0004). Conclusion is implied, not recorded as a field.
- **N6** T0008-R0011 claim_origin value "學員自述＋一張無網址截圖" combines enumerated values (自述／截圖／獎狀影本／他人轉述, T0007-R0013); same cell pattern at T0008-R0012. Cosmetic.
- **N7** Replacement-register status vocabulary reuses the token `VERIFIED_REAL` (P0354) for "replaced with a real source", overlapping the evidence_state token (T0015-R0004); the register defines its own state list at P0351–P0355, so the overlap is defined, not ambiguous in use.
- **N8** Non-reuse of the historical 0102 body and of `0102_122…` is verified only semantically (no such content, no numeric-ID collision, no exam/return-rate genre); byte-level non-reuse cannot be confirmed without tools.
- **N9** Form A has no explicit "course source" field (Blueprint: "course ID/date and source"); course_id/course_dates exist (T0007-R0006/R0007) and course provenance is recoverable via the replacement register (T0035-R0005, F-0102-004/020/026: 課程名冊、課表、簽到).
- **N10** T0040 "期限" column values (30/21/14/7 天) are internal handling targets; external response due dates remain unset (T0008-R0020, T0009-R0008), so control 2 is unaffected.
- **N11 (informational)** Formula reconciliation: Blueprint §12's literal "verified award cases" formula includes training link + disclosure authority, which R02 repair control 5 forbids conflating ("R02 修正…來源查證與揭露授權指標分離", and the R02 controls state priority over earlier R01 field drafts). The body implements the separated form (P0317 four predicates + separate eligibility count) and states the independence rule at P0318. Arithmetic is unchanged: 0.

**Sample boundary and case arithmetic**
- CASE-01 (SYN-0102-CASE-01): URL-less learner screenshot only, no third-party original (T0027-R0013) → `evidence_state=RECEIVED_UNVERIFIED`, `case_disposition=HOLD` (T0008-R0022/R0023, P0226, P0263); consent four purposes UNKNOWN (T0008-R0014); external due 未設定, internal review 2026-10-26 (T0008-R0020/R0021, P0266); Form F: 是×1, 否×3, 未知×6 (T0025).
- CASE-02 (SYN-0102-CASE-02): reposted screenshot, no official link/original (T0029-R0012) → RECEIVED_UNVERIFIED + HOLD (T0008-R0022/R0023, P0271); consent UNKNOWN, identity unmatched (T0026); internal review 2026-10-20, external due 未設定.
- Arithmetic: claims 2; screenshot leads 2; third-party originals 0; source-verified 0; Form F all-yes 0; eligible for human review 0; **verified awards 0; source verification 0/2 = 0%** (T0032-R0002–R0009; T0031-R0010). Other KPIs 0/2 except intake 2/2=100%, all labeled internal process metrics (T0033, P0330).
- Boundary held: 0 is not association performance, award rate, score, or "no award" (P0321–P0327, P0450); no closure-rate label (T0032-R0009 "不是結案率"); no certificate/winner list/organizer reply/signature manufactured (P0277, T0012-R0010, T0037-R0003).

**Neighbor requirement comparison**
- **I18-E08 / index 109 / docs 0100–0101** (pre/post self-rating, radar analysis): no survey instrument, no self-rating scale, no radar/report content; no shared real case ID asserted; Form E is record-based linkage only (T0018–T0022). Compliant.
- **Index 111** (thank-you letter, real-source acquisition): no letter-generation content anywhere; scope stays on award evidence acquisition/verification (T0001-R0007). Compliant.
- **Index 112** (certificate acquisition rate / denominators): body's rates use claim/case denominators explicitly labeled process KPIs, never a credential-acquisition or pass rate; P0323 disclaims denominator meaning. Compliant.
- **Index 122 / archived `0102_122…`** (exam coaching, return rate): no 考照/回訓率 content; doc identity pinned to 0102 + I18-E09 + index 110 (T0001-R0002–R0004); the archived artifact is not referenced. Numeric-ID collision avoided. Compliant.

**Title-hidden genre check**
With P0001 hidden, content is unmistakably third-party evidence acquisition + authenticity verification + training-linkage + case register: ready-to-send learner/organizer request drafts marked `SAMPLE TEMPLATE—NOT SENT` (P0125, P0147, P0156, P0180), independent-channel sourcing (P0158–P0159, T0013), a 14-point authenticity checklist with three-state evidence model (T0014, T0015, T0016), a linkage matrix with inference ceilings (T0018–T0022), a ten-check decision gate (T0023, T0024), and registers (T0034, T0035). It is not a certificate, success story, survey report, exam-coaching record, or thank-you letter. **PASS.**

## 4) State model identity

`STATE_MODEL_IDENTITY = UNKNOWN` — no native OpenCode session metadata is available within this response, and no fallback, tool use, or prose inference is authorized.

## 5) Declarations

`VISUAL_SCOPE=NOT_REVIEWED`
`TECHNICAL_SCOPE=NOT_REVIEWED_BY_REVIEWER`
`FORMAL_ACCEPTANCE=NOT_GRANTED`
`REAL_EVIDENCE=NOT_VERIFIED`