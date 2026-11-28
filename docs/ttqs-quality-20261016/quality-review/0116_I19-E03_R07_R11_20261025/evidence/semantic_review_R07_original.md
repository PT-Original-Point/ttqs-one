# Independent Semantic Review — 0116 / I19-E03 / Blueprint 127 / candidate R07

**Verdict: PASS (semantic only)** — bound to DOCX SHA-256 `82898de03bdd759030cb334a1cb972cdb06a0d160cc47a1a9110c0bbb4edb80c` and extraction SHA-256 `cdad739b42e07e752910756fb9fdaa66681fbdbc4b95eceda778620c86199e98`. PASS covers content semantics only. It is **not** formal acceptance of any TTQS score, association performance, or layout. **Visual scope: NONE.**

## SHA binding (consistency only; byte-level hash UNKNOWN)

| Item | Value | Binding status |
|---|---|---|
| DOCX SHA-256 (review scope) | `82898de0…edb80c` | Three-way consistent: review request ↔ extraction header `DOCX_SHA256` ↔ R07 QA receipt `docx_sha256`. Not recomputed (no tools) → request/header/receipt consistency verified; **byte-level hash UNKNOWN** |
| Extraction inspected | `cdad739b…99e98` | Material header ↔ QA receipt `extraction_sha256` agree |
| Dataset inspected | `76c80580…06adf` | Material header ↔ receipt ↔ Form A「名冊來源」agree (file intentionally still named R06 — unchanged fixed source) |
| Source packet | `3430b1a9…08c9d` | Request, extraction header, packet header, receipt all agree; 64 hex |
| Replacement register | `6d3071d7…d4650` | Material header only (not carried in receipt) — consistent, unattested elsewhere |

**Method:** no tools used; no files read or modified; no DOCX byte inspection; no Word visual inspection; no SHA independently verified. Only the attached packet was examined; the QA receipt was read as a scoped attestation, not proof.

---

## Prior R06 ADVISORY-1/2/3 — repair verification (recheck item 5)

| ID | R06 state | R07 state | Locator | Result |
|---|---|---|---|---|
| ADVISORY-1 | demo rows 01/02/06 其他因素 = `NOT_RECORDED` (dataset = `UNKNOWN`) | all eight demo rows now show `UNKNOWN` | §6 demo table, rows SYN-0116-01/02/06, column 其他因素; matches dataset `other_factors_status=UNKNOWN` ×8 | **FIXED** — strict row-fidelity restored |
| ADVISORY-2 | routing row SELF_REPORT_ONLY = 4筆 without distinguishing the job-seeking respondents | now「4筆（01、02、03、06；**另2筆為求職中**）」; §6 prose also states「自陳目前受僱者為01、02、03、06；求職中為04、05」 | §8 證據路由 table, SELF_REPORT_ONLY row; §6 逐項準確摘要 | **FIXED** — 4 self-reported employed rows are explicitly distinguished from the 2 job-seeking self-reports |
| ADVISORY-3 | ambiguous serial clause lacking subject/object | now「索引127**僅是內部位置，絕不可寫成或宣稱為官方紙本印刷序號；該官方印刷序號為 UNKNOWN_NOT_ASSERTED**」 | header; reinforced by §8 retire trigger「把索引127寫成紙本印刷序號」and `OFFICIAL_PRINTED_CHECKBOX_SERIAL=UNKNOWN_NOT_ASSERTED` | **FIXED** — index 127 explicitly cannot be called the official printed serial |

No residual defect from R06 remains; no new MAJOR or MINOR defect was found in R07.

---

## Criterion-by-criterion results (the seven rechecks)

**1) Official purpose fit and document type — PASS.** Attached official p.7 reads verbatim: 指標19「訓練系統的市場功能─目標市場及顧客的價值創造」, 1分常見參考佐證 including「口頭說明學員訓後就業狀況，但未有具體紀錄及評量」. Candidate §1 positions itself as the tool that converts that oral information into dated, denominator-defined, evidence-graded records,「不自行評分」「不得宣稱達到2至4分成果」— correct, since attached p.8 shows 2–4分 require completed survey/analysis results, pass rates, salary records, etc., none of which exist here. §1 also enforces「不得以滿意度資料替代就業證據」per the I19 guidance. Document type/title「學員訓後就業狀況追蹤調查表」matches the crosswalk row `I19-E03,1,0,0116,學員訓後就業狀況追蹤調查表`. Receipt `no_formal_acceptance_claim: true`; no self-scored claim anywhere.

**2) Title-blind identification and negative neighbors 0115/0117 — PASS.** Title removed, the content is unmistakably a post-training employment follow-up survey + response-logging/evidence-classification worksheet (Q01–Q12, frozen cohort denominator, response-status accounting, evidence routing) — not a satisfaction survey (Q08「主觀歸因，非因果證據；不得加總成訓練效果分數」), not a salary survey (no salary field; the historical 0116_138 salary-survey proposition is absent), not employer-satisfaction (learner-side only), not a certificate original (Form C is index-only), not certification tracking (no pass-rate denominator). Negative requirements: §9 跨文件界線 + §8 retire thresholds — 0115/I19-E02 = knowledge sharing, 0117/I19-E04 = certification tracking, no shared denominators or spliced numerators, fact_id separation, 0100/0101 excluded as fact sources, cross-reference only after verified same cohort/period/source index. Matches source packet exactly.

**3) Operational completeness — PASS.** Q01–Q12 all present, distinct, with full option sets and per-item skip/missing rules (Q05 direction+month incl. non-employment transition; Q07 skip ≠ disqualification + de-identification; Q10 refusal ≠ whole-questionnaire refusal; Q12 registration-only, no promises). Forms A, A2, B, B1, C, D1–D3 are all fillable tables — 14 `[TABLE]` blocks map one-to-one, in order, to the receipt's `table_shapes` (12×3, 9×3, 10×2, 8×2, 13×3, 12×3, 5×4, 6×4, 5×4, 9×8, 10×2, 10×3, 6×3, 9×4) — 14/14 corroborated. Joins explicit: cohort_id + 匿名追蹤碼 (+ evidence_id for C) across A/A2/B/B1/C and the dataset's case_id/cohort_id; no dangling「另列於下表」. Denominator: frozen cohort, mutually exclusive statuses, DECLINED/WITHDRAWN never in numerator and never removed from denominator, UNKNOWN ≠ unemployment (§2, §7, §8, D2). Statuses/codes complete with the 9-row code dictionary (incl. NOT_RECORDED→UNKNOWN, SAMPLE flags). Evidence routes and HOLD/REJECT complete: 9 routing states matching Blueprint §7; 12/12 retire thresholds matching Blueprint §8; §3 four pre-contact checks, one-follow-up-contact cap, no self-extension, proxy-fill prohibition.

**4) Arithmetic and synthetic row facts — PASS** (recomputation below). All eight rows match the fixed dataset on every substantive field; all counts, formulas, and the 90-day date recompute exactly.

**5) R06 repairs — PASS.** Verified in the table above.

**6) SAMPLE/REAL and consent/third-party boundaries — PASS.** `SAMPLE_SYNTHETIC_ONLY` / `data_origin` / `consent_status=SAMPLE_ONLY_NOT_REAL_CONSENT` on all eight rows (dataset + §6 header prose + code dictionary). §1 four hard lines (real performance UNKNOWN/HOLD; no identifiable PII; self-report vs third-party split with no-document →「無佐證文件輸入」; no causal inference). §5 A carries `SAMPLE_ONLY_NOT_REAL_CONSENT｜無真實授權 → HOLD_NO_CONTACT_AUTHORITY`; §5 C note「沒有文件輸入；不得標 VERIFIED」; §8 routing VERIFIED 0 / REQUEST_EVIDENCE 0 / REJECTED 0, whole-case HOLD_NO_CONTACT_AUTHORITY + HOLD_PRIVACY_POLICY; §9/§10 keep real figures at UNKNOWN. No fabricated roster, consent, contact, delivery, employment proof, verifier, signature, approval, or score. Q02/Q10 rules correctly separate item-level NA_REFUSED and optional-evidence refusal from whole-questionnaire DECLINED.

**7) Replacement register mapping and usability — PASS.** §10 items 1–8 map 1:1 to register rows (COHORT-01, 01..08, RESP-06, EMP-04, VER-00, DATE-90, SKILL, CONSENT) with equivalent minimum acceptance conditions (authorized roster + inclusion/exclusion + frozen denominator; protected pseudonymous IDs; dated actual returns + delivery/contact log incl. refusal/withdrawal; evidence with source index/scope/date/verifier/controlled storage; actual completion date + approved interval; consent/authority basis to replace illustrative flags). Includes recompute-and-reissue-receipts and originals-not-in-public-PR rules. A承辦人 can execute freeze → authorize → contact → log → classify → compute → decide from the document alone; an auditor can recompute every figure (code dictionary + all formulas in §7).

---

## Arithmetic recomputation (independent)

| Check | Recomputation | Candidate claim | Result |
|---|---|---|---|
| Response rate | 6 ÷ 8 = **75.0%** | 75.0% (§7.1, D1) | ✅ |
| Respondent self-employed/employed ratio | currently 受僱 = 01,02,03,06 = 4; 自營 now = 0; 4 ÷ 6 = **66.7%** | 66.7% (§7.2, D1) | ✅ |
| Sample evidence-input rate | 0 of 4 employment self-reports have documents (all NONE_PROVIDED) = **0%** | 0/4 = 0% (§7.3, D1) | ✅ |
| Self-rating mean | (2+1+2+0+0+1) ÷ 6 = 6 ÷ 6 = **1.0** | 1.0 (§7.5) | ✅ |
| Baseline distribution | JOB_SEEKING 3 (01,02,07); EMPLOYED 2 (03,05); SELF_EMPLOYED 1 (04); STUDYING 2 (06,08) | 受僱2／自營1／求職中3／在學2 | ✅ |
| Status reconciliation | 6 + 2 + 0 + 0 = **8**; mutually exclusive | same (§7.8, D2) | ✅ |
| 90-day date | 2026-06-30 + 90 d → July 31 (d31) → Aug 31 (d62) → **2026-09-28 (d90)** | 2026-09-28 (A, dataset) | ✅ |
| Row-by-row vs dataset | all 8 rows: response status/date, baseline→current, start month, skill use, rating, other_factors, evidence class/index, consent, origin | — | **8/8 on all fields**, incl. other_factors=UNKNOWN ×8 (ADVISORY-1 closed) |
| Routing counts | employment self-reports: SELF_REPORT_ONLY 4 (01,02,03,06), VERIFIED 0, REQUEST 0; UNKNOWN 2 (07,08); DECLINED 0; whole-case HOLD ×2 | same | ✅ (now disambiguated vs 04/05 — ADVISORY-2 closed) |
| Item inventories | Q01–Q12 = 12 distinct; §8 thresholds = 12/12 Blueprint §8; routing states = 9/9 Blueprint §7; register = 8/8 | same | ✅ |
| §6 summary prose vs dataset | 6 responses (01–06), 2 no-response (07,08), employed 01/02/03/06, job-seeking 04/05, baseline 2/1/3/2, all evidence NONE_PROVIDED, Q09 all UNKNOWN | same | ✅ |

No arithmetic, denominator, date, count, status-code, or row-fidelity error found.

---

## Defects and advisories

**No MAJOR, no MINOR, no outstanding defect.** One non-blocking observation:

| ID | Severity | Locator | Note |
|---|---|---|---|
| OBS-1 | OBSERVATION | §4 Q12 vs §5 B/B1 field lists | Q12 (後續支持需求) is by its own rule registration-only (「僅登記需求」) and has no arithmetic, denominator, or evidence-grade impact; the Blueprint's own Form B spec captures this via「後續處置」, and an answer can be logged in B「缺答／拒答／撤回處置」. Optional future nicety: add an explicit Q12 row to B1. Not a defect against the Blueprint or source packet; no repair required for this verdict. |

Because no defect remains, **no minimum repair is required**.

---

## SAMPLE / REAL determination

**SAMPLE_SYNTHETIC_ONLY throughout; real performance = UNKNOWN / HOLD.** No association decision, consent, contact attempt, delivery proof, employment outcome, third-party document, verifier result, signature, approval, or score is asserted as real. All approver/reviewer/owner fields blank + HOLD; all four employment self-reports capped at SELF_REPORT_ONLY / NONE_PROVIDED; VERIFIED/REQUEST_EVIDENCE/REJECTED = 0; causality, improvement, and 2–4分 claims forbidden; real figures barred from publication before denominator review; index 127 asserted as internal-only with the official printed serial UNKNOWN_NOT_ASSERTED.

## Visual scope and uncertainties

- **Visual scope: NONE.** I did not inspect the DOCX bytes, the Word-native PDF, or any page raster and claim no layout knowledge. The QA receipt's fonts (≥10.5/9.5 pt), 3 sections (incl. one landscape), page/render facts are attestations only, checked here solely for internal consistency (14 table shapes, 8 synthetic rows, 6/2/0/0 counts all agree with the extracted content).
- All SHA-256 values were checked for length and cross-document consistency, never recomputed → **byte-level verification UNKNOWN**.
- Extraction completeness: tables corroborated 14/14 shapes in order; the 92-paragraph count is unverified.
- 157 Blueprint row 127, crosswalk CSV row, full genre manual/mission doc, and PR #92 blobs remain attested-only; the official p.7/p.8 scoring text is directly verified from the attached excerpts.
- The R06 review was used only as defect context; every criterion and every prior finding was re-tested independently against the R07 evidence above.

**Final rationale:** All three R06 advisories are verifiably repaired in R07 (demo 其他因素 cells now match the fixed dataset as UNKNOWN on rows 01/02/06; the 4 self-reported employed rows are explicitly distinguished from the 2 job-seeking self-reports in §8 and §6; index 127 is now explicitly barred from being called the official printed serial, which is UNKNOWN_NOT_ASSERTED). Every mapping, denominator, formula, status code, join, register item, and SAMPLE/REAL fence re-recomputes and reconciles exactly against the fixed dataset and the official pages 7–8 text; the document remains a title-blind-appropriate employment follow-up tool that claims no score and holds all real performance at UNKNOWN, with layout outside this semantic scope — **PASS**, bound to DOCX SHA-256 `82898de03bdd759030cb334a1cb972cdb06a0d160cc47a1a9110c0bbb4edb80c` and extraction SHA-256 `cdad739b42e07e752910756fb9fdaa66681fbdbc4b95eceda778620c86199e98`. This statement asserts no formal acceptance.
