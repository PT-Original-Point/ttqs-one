# 0069 R02 — Semantic Repair Delta (SAMPLE-vs-REAL gate reconciliation)

- doc_id=0069
- requirement_id=I16-E01
- official_checkbox_serial=076
- revision output=R02 (copy-based, bounded correction of R01)
- source of truth read in full: `sources/UNIQUE_BLUEPRINT_R01.md`, `sources/SOURCE_FACTS_R01.md`, `candidate/0069_R01_body.md`
- output so far: `candidate/0069_R02_body.md` (body only). No DOCX built; R01 bytes preserved.
- Scope: content/claims reconciliation only. This delta does not assert visual QA, semantic PASS, formal acceptance, or build completion.

---

## (a) Exact sections changed

| # | Location in R02 body | Change |
|---|---|---|
| 1 | Header SAMPLE banner (bullet added) | Adds explicit statement that the §7 SAMPLE case is a complete embedded synthetic record set (7/7), its 8/8 critical pass applies only to the synthetic example, and is unrelated to real-association evidence status. |
| 2 | Identity map — `revision` | R01 → R02 (bounded correction note). |
| 3 | §1 use card, step 5 ("放行前") | Reworked: sample shows 7/7 complete synthetic records with internal locators; REAL release separately requires traceable originals, source/privacy check and association approval (HOLD). |
| 4 | §3.1 process map (note added below the diagram) | States this SAMPLE case passes 8/8 critical controls and has 7/7 records; the generic "missing file/source → hold" rule is a REAL-case rule and does not fail the synthetic sample. |
| 5 | §5 control matrix — C1 row | Decision de-coupled from a source-verification hold; now "SAMPLE 通過；出席預警已記錄，續行". |
| 6 | §5 control matrix — C3 row | Criterion, evidence locator, observation, result and decision reworked to the embedded synthetic record set (presence/completeness/internal consistency/locator traceability) = SAMPLE pass; REAL originals separate. |
| 7 | §5 key-control tally | 7 pass + C3 hold → 8/8 SAMPLE pass; REAL C3 requires original check. |
| 8 | §5 intro note | Adds that the sample's critical result is 8/8 SAMPLE pass. |
| 9 | §7.1 case summary — post-course records row | "index columns filled; REAL originals absent" → "7/7 synthetic records complete with internal locators (SAMPLE)". |
| 10 | §7.5 post-course records (table rewritten) | Seven synthetic records each given an existing SAMPLE record ID plus an exact internal locator (section/table/row); tally restated as 7/7 SAMPLE, applies to synthetic case only. |
| 11 | §7.6 deviation form | Added explicit contingency remainder row: 15-min block used 8 min, 7 min remaining. |
| 12 | §8 calculation table — control-point record-row rate | Removed "C3 ... still HOLD"; now notes C3 synthetic record complete. |
| 13 | §8 calculation table — critical-control status | 7÷8 = 87.5% → 8÷8 = 100.0% (SAMPLE). |
| 14 | §8 calculation table — post-course record rate | Relabeled "post-course required-record completion (SAMPLE)", 7÷7 = 100.0%. |
| 15 | §8.1 gate explanation | Replaces "C3 source unverified, overall HOLD" with SAMPLE pass + internal-demonstration hand-off; REAL remains UNKNOWN/HOLD. |
| 16 | §8.2 gate explanation | Same SAMPLE/REAL separation for the no-stop reasoning. |
| 17 | §8.3 "no averaging" statement | 7 pass/C3 hold → 8/8 SAMPLE pass; final disposition changed from "whole package HOLD / cannot hand off" to internal demonstration hand-off, explicitly non-real. |
| 18 | §9 disposition register | Result/status/closure/limits reworked to 7/7 + 8/8 SAMPLE pass and internal demonstration hand-off; added "real evidence status = UNKNOWN/HOLD". |
| 19 | §10.2 hold checklist status note | Clarifies HOLD applies to REAL cases; the synthetic sample's 7/7 + 8/8 does not release any real association package. |
| 20 | §12.2 replacement register (note added) | Notes the seven synthetic records are embedded at §7.5; the register is the REAL-replacement crosswalk; SAMPLE pass ≠ REAL ready. |
| 21 | Concluding boundary bullets | Added bullets for the synthetic 7/7 + 8/8 (synthetic-only, internal demonstration hand-off) and the separate REAL UNKNOWN/HOLD with pre-conditions for real release. |

Unchanged (deliberately): §2 scope/authority/vocabulary, §3.2 cross-document hand-off table, §4 responsibility matrix, §6 trigger/decision table (illustrative thresholds), §7.2–7.4 timing and pre-course detail, §10.1 replacement guide, §11 blank forms, §12.1 fact-check matrix, identity values other than revision.

---

## (b) The prior contradiction (in R01)

R01 made the fictional worked example fail on the real association's evidence status:

- §5 C3: result "暫緩（來源未驗證）", decision "HOLD，不得放行", driven by "REAL 原件 0 份、來源未驗證".
- §5 tally: "本案關鍵狀態為 7 通過、C3 暫緩，不可稱 8/8 全通過".
- §7.1/§7.5: records shown as "索引列已填；REAL 原件未附", closing with "C3 不通過放行條件並維持 HOLD".
- §8: "關鍵管制點狀態 … 7 ÷ 8 … 87.5%（C3 暫緩；不得放行）"; §8.1 "C3 來源未驗證，總體放行仍為 HOLD"; §8.3 final decision "整包 HOLD，不得移交為已驗證證據".
- §9: status "暫緩（HOLD）至來源查核完成".

This conflated the synthetic case with the real association's evidence status. It contradicted `UNIQUE_BLUEPRINT_R01.md` §7–§8, which require the SAMPLE case to be a completed, internally consistent process: 7/7 post-course records and all eight critical SAMPLE controls passing, with real association activity separately UNKNOWN/HOLD.

---

## (c) Corrected SAMPLE-vs-REAL gate distinction

SAMPLE gate (fictional case `SYN-0069-CASE-01`, this document only):
- C3 criterion is now presence, completeness, internal consistency and locator traceability of the seven synthetic records embedded in §7.5, each tied to an exact internal locator (section/table/row) plus its existing SAMPLE record ID (`SAMPLE-PLAN-0069-V1`, `SAMPLE-CONSENT-0069`, `SAMPLE-ATTEND-0069`, `SAMPLE-TIMELOG-0069`, `SAMPLE-SAFETY-0069`, `SAMPLE-ASSESSREC-0069`, `SAMPLE-DEVIATION-0069-01`).
- C3 = SAMPLE PASS; critical controls = 8/8 SAMPLE PASS.
- The 7/7 result is stated as applying only to the synthetic case.
- Disposition is an internal demonstration / review hand-off only. No claim of association activity, authorization, records, adoption, signature, approval or real evidence.
- No external files are implied to be attached.

REAL gate (actual association), kept separate and unchanged in principle:
- Actual association evidence and adoption remain UNKNOWN/HOLD.
- If real use is proposed, authorized REAL originals, source verification, privacy handling and actual association approval are required before any real release.
- The absence of REAL originals does not make the synthetic sample fail; the synthetic pass does not release a real association package.

---

## (d) Recalculated results (recomputed from stated numerators/denominators)

| Metric | Formula | N / D | Result | Note |
|---|---|---|---|---|
| Pre-course completion | completed ÷ total | 10 / 10 | 100.0% | SAMPLE |
| Control-point record-row completion | rows with observation/result/decision ÷ rows | 12 / 12 | 100.0% | record completeness, not pass status |
| Critical-control status | passed critical ÷ critical total | 8 / 8 | 100.0% | SAMPLE; C3 passes on embedded set |
| Attendance | attended ÷ enrolled | 10 / 12 | 83.3% | triggers illustrative <85% warning (no auto-cancel) |
| During-course check completion | completed ÷ total | 6 / 6 | 100.0% | SAMPLE |
| On-time rate | on-time ÷ timed checks | 5 / 6 | 83.3% | T4 late |
| Late deviation | actual − planned | 11:08 − 11:00 | 8 min | >5 → warning; ≤10 → stop not met |
| Contingency block | 15 − 8 | 15 / 8 used | 7 min remaining | instructional time not reduced |
| Assessment hand-off | delivered/returned ÷ attendees | 9 / 10 | 90.0% | hand-off rate, NOT pass rate |
| Post-course required records | complete ÷ required | 7 / 7 | 100.0% | SAMPLE only |

Noncritical controls D1, D2, D4, C2 are retained and kept distinct from the critical set; no averaging across critical/noncritical. Warning decisions preserved: attendance 10/12 = 83.3% triggers the document's explicitly illustrative <85% warning; T4 is 8 minutes (>5 warning, ≤10 stop) with 7 minutes of the 15-minute contingency remaining; no safety event is claimed.

---

## (e) Remaining limitations

- This is a content/claims reconciliation of the body markdown only; no DOCX was built and no rendered/visual verification was performed.
- The synthetic case still rests entirely on invented, clearly tagged SAMPLE/SYNTHETIC data; it demonstrates internal consistency, not real-world evidence.
- Real association evidence, adoption, authorization and approval remain UNKNOWN/HOLD; nothing here supplies or verifies them.
- Thresholds (5 min, 10 min, 85%, 7/7, 8/8) remain local illustrative values, not official TTQS or approved association standards.
- Case independence from 0033/0065/0066/0068 is restated but not independently verified here.
- This delta does not constitute semantic PASS, formal acceptance, or any independent review conclusion.
