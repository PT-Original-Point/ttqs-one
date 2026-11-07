# Structured independent review — TTQS ONE / doc_id 0110 / I18-E19 / candidate R07

## 1) Overall verdict

**PASS** — bound explicitly and only to candidate DOCX SHA-256 `9a306bf5712437ee578867b745e7d0811959decaa862ed540a82e7e8553bd3c2`. If the reviewed DOCX bytes do not hash to exactly this value, this verdict is void. `checkbox serial = UNKNOWN` (T01 R04) — correctly unresolved; `REAL status = UNKNOWN/HOLD` (T01 R07) — correctly withheld. All nine R06 blocking findings are resolved, the R07 content is complete and directly usable, and every displayed figure recomputes exactly. Residual items (Section 6) are non-blocking.

## 2) Exact candidate SHA

`9a306bf5712437ee578867b745e7d0811959decaa862ed540a82e7e8553bd3c2` (as asserted by the packet; taken as the binding identity, not independently rehashed — see exclusions).

## 3) Scope actually reviewed and explicit exclusions

**Reviewed:** the supplied extraction only — paragraphs P001–P302, tables T01–T37, the expanded 213-record fact-level synthetic replacement register, the source packet, Unique Blueprint, the prior R06 FAIL review, and the R06→R07 remediation trail. Content domains assessed: requirement/genre fit, eligibility/consent/privacy, item wording and scales, 0/blank/invalid/duplicate/denominator rules, synthetic case completeness, arithmetic, baseline vs post periods, action-plan traceability and disposition logic, HOLD/reject rules, causal and significance restraint, synthetic/real boundary, identity mapping, 0109/0111 separation, replacement-register completeness.

**Excluded / not claimed:** no files were read from disk, edited, or generated; no tools were executed; no visual or page-level layout inspection of the 26-page Word document (separate visual receipt); no byte-level hashing of the DOCX, register, source packet, blueprint, or official PDF — all SHAs are accepted as asserted by the packet and the verdict is bound to them; no access to the official PDF, crosswalk, or Git objects — the official sentence is accepted as quoted (T01 R05) and matches the packet's locked text verbatim. Anchors therefore use P###/T##-R## labels; no printed page numbers exist in the extraction. Reviewer model: `opencode/mimo-v2.6-flash-free`, as supplied natively by this session's environment configuration.

## 4) Findings table

| # | Finding | Severity | Anchors | Basis | Disposition |
|---|---|---|---|---|---|
| 1 | R06 blocker 1 (ineligible learner L06 counted) resolved: respondent-level HOLD/INVALID, raw row preserved, excluded from valid returns and every item N; response rate corrected to 7/8 | Positive | P265, P273–P276; T30 R02; T31 R07; T35 R05, R07 notes; register `learners.L06.*`, `learners.L06.validity_status`, `case.valid_returns.learners=7` | Blueprint F; R06 blocking 1 | Resolved |
| 2 | R06 blocker 2 (client observation window = baseline) resolved: C02 now requires separate full-date baseline (D−30～D0) and post-training (D0+1～D0+30) windows; C03–C07 anchor to baseline using post observation; action plan no longer labels the client window as baseline | Positive | P110–P114; T05 R05–R06; T33 R02–R07; T22 R03 | Blueprint C/E2; R06 blocking 2 | Resolved |
| 3 | R06 blocker 3 (C10 code key mismatch) resolved: options a–e, x, n defined on the form with n mutually exclusive; sample values a, b, x, c, n, x all valid | Positive | P172–P178; P271; T34 R02–R07 | R06 blocking 3 | Resolved |
| 4 | R06 blocker 4 (C08 undefined referent) resolved: C08 now names the 工作人員填寫區「指定的服務／工作實務名稱」, which the settings table defines | Positive | P161–P165; T05 R03; T33 R02–R07 (C08 values) | R06 blocking 4 | Resolved |
| 5 | R06 blocker 5 (no client tracking) resolved: mandatory anonymous return code + fill date on form; per-respondent fill dates in register | Positive | P103; T05 R08; register `clients.C01–C06.fill_date` | R06 blocking 5 | Resolved |
| 6 | R06 blocker 6 (invalid/duplicate/blank undefined) resolved: explicit definitions — invalid = multiple marks / out-of-range / contradictory / unreadable; duplicate = same anonymous code or approved non-identifying marker, no name crosswalk, no cross-code inference; blanks not imputed; partial scored per item | Positive | P045, P210; P288 | Blueprint E/G; R06 blocking 6 | Resolved |
| 7 | R06 blocker 7 (broken action-plan linkage) resolved: B-3 cites actual items (L02, L07–L09; C03–C07), B-1 concrete outcome, B-2 defined scope, B-4 operational indicator separated with formula and fixed denominator; `SYN-Q-01` gone | Positive | T20 R02–R05; T21 R02–R05 | R06 blocking 7 | Resolved |
| 8 | R06 blocker 8 (30-day vs 60-day ambiguity) resolved: D0+30 explicitly interim, D0+60 final decision point; REVISE at interim correctly justified (87.5%<90.0%); CLOSE prohibited pending D0+60; H-4 barrier now links to F-2 with matching audit-trail entry | Positive | P213, P280, P282; T23 R02–R03; T24 R03; T26 R02–R05; T27 R02; T28 R03; T29 R06–R10 | R06 blocking 8 | Resolved |
| 9 | R06 blocker 9 (unsupported employment fact) resolved: "不以受僱或支薪身分為前提" replaces the factual assertion; 原始點協會 labeled intended user, not verified fact; learner form keeps blank association name | Positive | P074, P077; P002, P021; T05 R02; T01 R07–R08 | Blueprint H; R06 blocking 9 | Resolved |
| 10 | R06 material 10 (stop-instruction conflict) substantially resolved: whole-form stop only for C01＝否/不確定; per-item 0 for unobserved items with explicit no-abandonment rule; C06 demonstrates partial-zero retention. Residual: P080's "沒有可以比較的依據" wording remains broader than P196 | Minor residual | P080 vs P196; T33 R07 | R06 material 10 | Substantively resolved; see 6.1 |
| 11 | R06 material 11 (C02 period/frequency mismatch) resolved: full calendar dates required for both windows; sample frequencies all map to offered codes F1–F3; HOLD rule enforceable | Positive | P110–P114; T33 R02–R07 | R06 material 11 | Resolved |
| 12 | R06 material 12 (traceability overstates learner link) substantially resolved: T07 explicitly labels L02 "自我效能感知（非組織績效）", L02 body text carries the same disclaimer, operational indicator listed separately in T37 R05. Residual: the T37 R05 row itself still lists L02 without an inline proxy label | Minor residual | T37 R05–R06; T07 R03; P052 | R06 non-blocking 12 | Substantively resolved; see 6.2 |
| 13 | R06 blocker-class 13 (version clarity) resolved in body: P002 distinguishes 表單版次 R03 from 建置候選 R07 with reason | Positive | P002; T01 R02–R04 | R06 finding 13 | Resolved |
| 14 | R06 finding 14 (register unverifiable) resolved: register supplied expanded; 213 records / 213 unique field paths independently reconciled (see §5); all respondent answers, counts, rates, periods, target, roles, disposition, D0 enumerated | Positive | Full register; T31–T34; T30; T36; T29 | Blueprint F/I; R06 finding 14 | Resolved (minor note 6.3) |
| 15 | Requirement fit, genre, identity binding: dual-respondent instrument + action plan; official sentence verbatim; doc_id/requirement mapped; serial UNKNOWN; no statistical-significance or causal conversion of 「顯著」; SAMPLE/REAL boundary intact throughout | Positive | T01 R02–R08; P009, P085, P212, P219, P223, P255, P280, P282, P292; T37 R06 | Official text; Blueprint A/B/G | PASS |
| 16 | Adjacent-document separation: no 0109 social-platform-frequency content, no 0111 special-performance/social-impact register, no shared fictional actors/metrics visible in the extraction | Positive | P001–P302 (absence verified); T01–T37 | Blueprint B/H | PASS (bounded to supplied extraction) |
| 17 | Human-facing body clean: no engineering paths, commits, hashes, or control metadata in questionnaire/plan bodies | Positive | P001–P302 | Blueprint I | PASS |

## 5) Independently recomputed figures

All values recomputed from the raw answer rows (T31–T34), excluding respondent L06 (HOLD/INVALID):

**Learner returns:** 8 delivered eligible invitations; 7 valid; 1 ineligible (L06); duplicates 0. Rate = 7 ÷ 8 = **87.5%** (T30 R02 ✓).

| Item | Valid 1–5 values (excl. L06) | N | Sum | Mean | Favorable (4–5) |
|---|---|---|---|---|---|
| L01 | 4,4,5,3,4,5,4 | 7 | 29 | 4.143 | 6/7 = 85.7% ✓ |
| L02 | 3,4,4,3,5,3,4 | 7 | 26 | 3.714 | 4/7 = 57.1% ✓ |
| L03 | 4,4,4,3,5,3,4 | 7 | 27 | 3.857 | 5/7 = 71.4% ✓ |
| L04 (frequency) | 3,3,2,3,1,4,2 | 7 eligible | — | not scored | distribution 1=1, 2=2, 3=3, 4=1 ✓; 0/invalid = 1 (L06) ✓ |
| L05 | 4,3,4,3,4,2 (0=1: L08) | 6 | 20 | 3.333 | 3/6 = 50.0% ✓ |
| L06 (item) | 4,4,3,4,4,5,4 | 7 | 28 | 4.000 | 6/7 = 85.7% ✓ |
| L07 | 4,4,3,4,4,5 (0=1: L08) | 6 | 24 | 4.000 | 5/6 = 83.3% ✓ |
| L08 | 3,4,3,4,4,2 (0=1: L08) | 6 | 20 | 3.333 | 3/6 = 50.0% ✓ |
| L09 | 4,3,4,3,3,4 (0=1: L08) | 6 | 21 | 3.500 | 3/6 = 50.0% ✓ |

All match T35 R02–R10 and P276–P277 exactly.

**Client/partner returns:** 6 invitations; 6 valid; rate = 6 ÷ 6 = **100.0%** ✓ (T30 R03).

| Item | Valid values (C01–C05; C06=0 all items) | N | Sum | Mean | Favorable |
|---|---|---|---|---|---|
| C03 | 4,4,3,5,4 | 5 | 20 | 4.000 | 4/5 = 80.0% ✓ |
| C04 | 4,3,4,4,5 | 5 | 20 | 4.000 | 4/5 = 80.0% ✓ |
| C05 | 3,4,4,3,4 | 5 | 18 | 3.600 | 3/5 = 60.0% ✓ |
| C06 | 3,4,3,4,4 | 5 | 18 | 3.600 | 3/5 = 60.0% ✓ |
| C07 | 4,3,4,4,4 | 5 | 19 | 3.800 | 4/5 = 80.0% ✓ |

Matches T35 R11–R15 and P278 exactly. C06 correctly retained as a valid form with per-item 0 exclusion under P196.

**Operational check (fixed denominator 8, SYN-LIST-01):** baseline 6 ÷ 8 = 75.0%; interim D0+30 7 ÷ 8 = 87.5%; change = 87.5 − 75.0 = **+12.5 pp** ✓ (T08, T29, T36). Target gap: baseline 75.0 − 90.0 = **−15.0 pp**; interim 87.5 − 90.0 = **−2.5 pp** ✓. With n = 8, 7/8 = 87.5% < 90.0% and 8/8 = 100.0% is the first attainable value meeting the ≥90.0% threshold ✓ (P213, P280, T29 R06, register `case.target_attainability_fixed_denominator`). Interim disposition REVISE is arithmetically forced; D0+60 final result correctly pending with no CLOSE ✓.

**Period arithmetic:** D0 = 2026-01-30; D−30 = 2025-12-31 ✓; D0+1～D0+30 = 2026-01-31～2026-03-01 ✓; fill dates 2026-03-02 fall one day after the post window closes ✓.

**Register reconciliation:** learner item cells 8 × 13 = 104; client item cells 6 × 13 = 78; client fill dates 6; `learners.L06.validity_status` 1; case-level period/scenario/count/target/role/privacy/disposition fields 16; case rate/count/D0/attainability fields 8. Total = **213 records, 213 unique field paths** — matches the asserted register size exactly, with no duplicate paths and no demo value found in T31–T34/T30/T36 that lacks a register entry.

## 6) Exact remaining defects (all non-blocking; none prevents PASS)

1. **P080 residual wording:** the client stop instruction ("沒有可以比較的依據，請停止填寫") remains broader than the corrected P196 rule (whole-form stop only for C01＝否/不確定; per-item 0 otherwise). Mitigated by P196's explicit rule and the C06 demonstration, but tightening P080 to reference C01 would remove residual ambiguity for a first-time administrator.
2. **T37 R05 inline labeling:** the traceability row "訓練對組織績效改善及提升" still lists L02 without an inline "self-efficacy proxy" qualifier in that row. The qualifier exists at T07 R03 and P052, so the mapping is not misleading overall, but the row is weaker than the rest.
3. **Register coverage of narrative demo cells:** a small set of synthetic strings (e.g., `SYN-LIST-01`, `SYN-EVID-BIN-01`, F-1/F-2 action texts, H-4 barrier text, audit-trail rows, B-/C-field demonstration texts) are covered by the document's replacement instructions (P299–P300) rather than individual register rows. All arithmetic- and truth-critical values are enumerated; this is a completeness edge, not a defect in the verifiable set.
4. **Cosmetic:** L04's options remain displayed in descending 4→1 order while other items ascend; harmless but inconsistent.
5. **Inherent limits (not defects):** register SHA `684f04…d3de`, source-packet/blueprint/official-PDF SHAs, and the candidate DOCX SHA were not independently rehashed; the verdict is bound to the asserted candidate SHA. No visual/layout review was performed (26-page Word receipt separate). No printed page anchors exist in the extraction.

**Final: PASS**, bound to SHA-256 `9a306bf5712437ee578867b745e7d0811959decaa862ed540a82e7e8553bd3c2`, content-only, candidate status unchanged (acceptance remains with the authorized reviewer; REAL status remains UNKNOWN/HOLD).