# Independent Exact-SHA Review — DOCX 0053 R01 (I12-E01 / official sequence 056)

Shorthand: **R#** = rendered PDF page #, **T#** = body table # as numbered in the structured extraction, row named where present. No visual inspection was performed; all verification below is from packet text only.

---

## 1. Reviewed SHA and identity limitation

**REVIEWED_SHA256:** `14a7b825d24059f2c339f95eabfa613d4cad43dea9534fa80fcffa8a2489f4f8`

Limitation: this is the *asserted packet-extracted* identity. The packet is text-only; I could not hash the DOCX bytes (68,109-byte claim unrecomputed), the PDF export (`0c30f9…`), the blueprint row (`57a8b5…`), the crosswalk (`1ddfbb…`), or the register (`a98e0e…`). All SHA values are treated as recorded identity claims, not independently recomputed.

## 2. Overall verdict: **PARTIAL**

All material text-verifiable acceptance tests recompute and are supported; the unresolved material gap is the visual/typographic acceptance test (font minima 10.5pt/9.5pt, layout fit, official page-4 image) which cannot be proven from this packet, plus three inaccurate register locators and minor completeness gaps (fixable, small scope). These are insufficient grounds for PASS; none rises to FAIL.

## 3. Criterion matrix

| Test | Verdict | Evidence |
|---|---|---|
| Official sequence 056 (not DOCX 0053) correctly distinguished | PASS | R2 T4 rows 3–4; T6 row 3; R18 T29 row 2 |
| I12-E01 official text quoted unaltered, page-4 source located | PASS | T3 (R2); T6 row 2 (R3) |
| Genre = analysis/evaluation report (data, denominators, formulas, step calc, limits, decisions) | PASS | T11 (R5); T17–18 (R10); T20–21 (R12); T22–23 (R13) |
| Administrator can decide and track | PASS | T10 gate (R4); T23 actions+success checks (R13); T24 owners/deadlines/indicators (R14); return criteria R14 bullets; R15–17 worksheets/form |
| Five dimensions each separately evaluated | PASS | L1–L3, M1–M3 (T12, R6); T1–T3, P1–P3, F1–F3 (T13, R7–8) — each has criterion, evidence, baseline→recheck status |
| Population/denominators and N/A rules defined | PASS | T11 (R5); 公式 R4 (§03); p15 note "沒有證據不可填 N/A" |
| Formulas recomputable; rounding stated | PASS | T17, T18, R10 G1 paragraph; T11 row 6 "列到小數一位；中間計算保留精確分數" |
| Before/after results with same denominator | PASS | T19 (R11); T18 row 5 "同一 15 項分母" |
| Conclusions bounded to SAMPLE; no performance claim | PASS | T22 (R13); T2 row 3 (R1) |
| Limitations and UNKNOWN handling | PASS | T8 (R3); T21 (R12); R11 比較邊界 |
| Owner/deadline/follow-up + return criteria | PASS | T24 (R14; A-04 未完成, A-05/A-06 dates UNKNOWN by design); R14 return bullets |
| Title-blind recognizability | PASS | R1–R2: 15-item five-facet mechanism, official quote, dimension set; not transplantable to 055/057/058/059 work |
| SAMPLE/SYNTHETIC vs REAL boundaries | PASS | R1 T1; per-section disclaimers T12/T13; T21 all UNKNOWN; T24 A-05/A-06 |
| Continuous improvement ("近年") longitudinal depth | PASS* | Single synthesized cycle 2026-10-03→10-08; the doc itself declares "不足以稱為多年趨勢" (R11) and leaves REAL tracking unestablished (T24 A-06). Limitation honestly stated, not hidden. |
| Peer-DOCX non-copy test (0052/0054 bodies) | PARTIAL | 0052 body absent (SHA+size only); 0054 not even in packet — non-copy check possible only on 0053's side |
| Font minima / layout / 30-second first page (front 30s read) | PARTIAL | Text shows the first-page summary exists (T1–T2, R1); pt sizes, rendering fit, and page-4 image (`0e00b4…`) unverifiable |
| Register audit (38 rows) | PASS with defects | See §7 |

## 4. Findings

| # | Severity | Location | Observed | Why it matters | Minimum correction |
|---|---|---|---|---|---|
| 1 | Minor | Register F017 (body_locator "第 1、3 頁") | Exact course name 「志工服務紀錄、交接與工作界線實務」 does not appear on rendered page 1 (R1 text lacks it; closest partial mention is T12 row 2 on R6) | Register locators must be verifiable | Change to "第 3 頁（第 6 頁部分表述）" |
| 2 | Minor | Register F018 ("第 3、6 頁"; rendered_page 3) | “12 個規劃名額” appears only in T12 L2 row (R6); R3 contains no headcount | Same — locator drift breaks traceability | Correct to R6 only |
| 3 | Minor | Register F030 | Records "4/6 正確=66.7%", but body displays baseline only as 4/6 (T16, R9); the explicit 66.7% appears only for the M-dimension rate (T17/T19), not the QA rate | Register should not add a displayed form that body text omits | Either add "=66.7%" next to the 4/6 in body §07 summary, or record value as "4/6" with 66.7% marked derived |
| 4 | Minor | R7 T13 P2 row; R9 T14 P2 row | The 50% practice-minimum (“本示範設定的 50% 最低值”) is used as a judgment rule but never defined in T11 dictionary | A governing criterion should be registered and defined | Add a data-dictionary row + one register row for the 50% minimum |
| 5 | Minor | R2 §01 last paragraph | Symbol “P0-SYN” used without in-document definition | Undefined notation for a reader/assessor | Define inline: "P0-SYN（本案例之合成計畫草稿版號）" |
| 6 | Minor | T24 A-03 (R14) | “20/20/50 重算 90 分鐘” could be misread as three segments totaling 90 | Contradicts T15's correct caution | Reword: "90 分鐘內 18/18/45，餘 9 分鐘…" |
| 7 | Minor | T29 row 8 (R18) | 持續改善 locator “第 8-14 頁” includes R8, which holds no continuous-improvement content | Register accuracy | Tighten to "第 9–14 頁；第 17 頁" |
| 8 | Minor (completeness) | Register overall | Unregistered synthetic specifics: P0-SYN token; T3's "六個合成作答樣例"; G1 “五情境至少答對四題" threshold; the 50% minimum (see #4) | Every synthetic fact claims one-register-row coverage | Add rows F039+ or fold into existing facts |
| 9 | Informational (operator note) | Packet itself | Official page-4 excerpt shows indicators 11/12/13 with 12a–12e but no visible "056" numbering; sequence 056 rests on the packet's 157-grid/genre-manual claim | Mapping of sequence numbers is not independently verifiable from this packet | Operator should retain the 157-grid source where 056 is actually printed |
| 10 | Informational | T5 row 5 (R2) | "0056 / I12-E04" mapping asserted; packet crosswalk only confirms I12-E01→0053 | Cross-map of 0052/0054/0056 unverified | Verify against full crosswalk before reuse |

No Critical or High findings. Nothing in the body fabricates approvals, participants, courses, results, or third-party documents.

## 5. Recalculated arithmetic (independent)

Baseline counts from T12/T13 rows: 評分中「部分符合」= L2, M2, M3, P2 (4); 「符合」= 11. → 11/15.
- 11÷15 = 0.73333… → 73.3% ✓ (T2, T17, T18)
- Recheck: only M3 remains 部分符合 → 14/15 = 0.93333… → 93.3% ✓
- Per dimension: 學員 2/3→66.7% | 教材 1/3→33.3% ✓ | 師資 3/3 ✓ | 方法 2/3→66.7% ✓ | 設施 3/3 ✓; recheck 3/3, 2/3 (66.7%), 3/3, 3/3, 3/3 ✓ (T17, T19)
- Δ = 14−11 = 3 items ✓; Δpp = (14/15−11/15)×100 = 3/15×100 = **20.0 pp exactly** ✓; per-dimension pp (33.3, 33.3, 0, 33.3, 0) average to 20.0 — consistent ✓
- M3 QA: T16 rows 1,1,1,1,0,0 = 4/6 baseline ✓; 1,1,1,1,1,0 = 5/6 recheck ✓; 5/6 = 83.333→83.3% ✓; 4/6 = 66.666→66.7% (derived, see Finding 3)
- G1 baseline 35/20/35 of 90 min: 31.5+18+31.5 = 81 ✓; Proposal 20/20/50: 18+18+45 = 81 ✓; both leave 9 min unassigned, explicitly flagged (T15, R9; R10 paragraph) ✓; P2's 45 min = 50% of 90 ✓ — and the 35% baseline correctly falls below the declared 50% minimum
- Total duration 90+90+120+60 = 360 ✓ (T6 row content, R3; T12 M1 row, R6)
- Decision logic on R4: 93.3% ≥ 90% threshold, yet unresolved M3 blocks REAL publication — coherent ✓

**SAMPLE/REAL verdict:** Every result, date, role, course, material version, venue, and judgment in the candidate is SAMPLE/SYNTHETIC and is labeled as such where asserted (T1, T8, T21, T24, register F001–F038 all `SYNTHETIC—待 REAL 替換`). No sample approval course, participants, results, or third-party evidence is presented as real. The boundary discipline is correct.

## 6. Negative-neighbor determination

- **vs 0052 / I11-E04:** **PASS — distinct work product, one-sidedly verified.** 0053 neither re-posts feedback questionnaires nor claims a feedback-driven planning process; it consumes 0052's synthetic plan strictly as the object under review (T5 row 2, R2; T6 row 6, R3). Rejectable differences: 15-item compliance table, rates, grouped deltas, action register — none of these is 0052's deliverable. Limit: 0052's full body is not in this packet (SHA/size only); the reverse non-copy check cannot be executed here.
- **vs 0054 / I12-E02:** **PASS — distinct work product, one-sidedly verified.** 0053 contains no individual-selection records, committee resolutions, or approval originals and explicitly cedes them (T5 row 4; R6 note "個別名單與正式錄取決定屬 0054 的 REAL 原件"). L2 operates on rule operability, not an actual admission list. Limit: 0054 is absent from the packet; only 0053's side is testable.

## 7. Register coverage verdict

38/38 rows audited. All fact IDs unique (F001–F038); all 10 required columns populated; all rows carry the exact candidate SHA `14a7b8…f4f8`; type = SAMPLE/SYNTHETIC and status = 待 REAL 替換 for every row; responsible role and REAL replacement source present in every row.

Problematic rows (specific, not a vague score):
- **F017** — body locator includes R1; course name absent from R1 (actual: R3; partial on R6).
- **F018** — body locator "第 3、6 頁"; no headcount on R3 (actual: R6 T12 L2).
- **F030** — value adds a percentage the body does not display for the QA baseline (see Finding 3).
- **Completeness gaps (no row exists):** "P0-SYN" token; T3's six calibration samples (distinct from the six readability figures in F029); G1 "五情境、至少答對四題" threshold; 50% practice minimum.

Verdict: **coverage adequate (all principal synthetic facts keyed), register itself PASS after the two locator corrections and one value rewording**; the unregistered items above should be added before REAL upgrade.

## 8. Checks I could not perform from this packet

1. **Hash recomputation** — candidate DOCX, PDF export, blueprint row/file, crosswalk, register (text-only review).
2. **Visual inspection** — no page images: font-size minima (正文≥10.5pt, 表格≥9.5pt), table fit/overflow, header/footer rendering, color/contrast, and the official page-4 image (`0e00b4…`) remain unverified. First-page readability is supported by text order and presence of T1/T2 only.
3. **Body-extraction fidelity** — whether the structured extract reflects all DOCX content (hidden text, formatting, merged-cell semantics) cannot be proven.
4. **Peer non-copy check against 0052/0054 full texts** — 0052 present only as SHA+size; 0054 absent entirely.
5. **Blueprint line 53 / crosswalk row 53 existence** — only excerpts are in the packet; file-level SHA claims unrecomputed.
6. **Official "056" enumeration and DOCX 0056(I12-E04) mapping** — the page-4 excerpt does not itself print sequence numbers; supporting lists are packet claims.
7. **Byte count 68,109 and page count 18** — accepted as operator-recorded, unrecomputable here.
8. The operator's separately recorded 18-page visual pass is excluded from consideration as non-independent evidence.

---

**Recommendation: PARTIAL.** Retain the document; fix the three register rows (F017, F018, F030), add the four missing synthetic-fact rows, tighten the two wording/locator items (T24 A-03, T29 row 8), and complete an independent visual/typographic pass before recording any PASS. This is a review recommendation only, not formal association acceptance.
