**Independent Exact-SHA Semantic & Usability Review — DOCX 0053 R03**

---

### 1. SHA-256 Identity Verification

The candidate bytes were located and hashed locally:

- Path: `E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03\candidate\0053_R03.docx`
- Recomputed SHA-256: **`CC75583238DBA42EEDE61DE990992770F8DE75E96D1BCFE1313E57629551F8E8`**

**Result:** Byte identity **confirmed**. The recomputed hash matches the packet-asserted candidate SHA exactly (case-insensitive). Builder receipts were not used as proof.

---

### 2. Overall Verdict

| Scope | Verdict |
|-------|---------|
| **Overall (substantive, independently verifiable criteria)** | **PASS** |
| Criterion 10 — exact pt font-floor measurement (layout/image) | **PARTIAL / UNKNOWN** |

All material, textually verifiable criteria pass. The only scope not independently verifiable from the attached images is the exact font-size floor (10.5 pt body / 9.5 pt table), which cannot be measured pixel-to-point from the rendered contact sheet and page images. That sub-scope is marked PARTIAL/UNKNOWN and does **not** invalidate the substantive PASS.

---

### 3. Criterion Matrix

| # | Criterion | Verdict | Key Locators / Evidence |
|---|-----------|---------|-------------------------|
| 1 | Official I12-E01 requirement match; correct distinction among DOCX 0053, I12-E01, and 157-sequence 056 | **PASS** | Page 2 table header `官方原文｜I12-E01｜流水號 056`; Page 18 Appendix C row 1 (`056｜I12-E01 五面向檢討`, 正文定位第 2 頁) |
| 2 | Genre & usability: complete analysis/evaluation report (scope, sources, dictionary, denominators, formulas, sample data, five dimensions, decisions, actions, owners, dates, measures, REAL route) | **PASS** | Pages 1–18; required sections present on Pages 1 (purpose), 2 (scope), 3 (sources), 4–5 (method/dictionary), 6–10 (data/calc), 11 (grouping), 12 (findings), 13 (decisions), 14 (owners/dates), 18 (replacement list) |
| 3 | Recompute all displayed arithmetic; check rounding and connected statements | **PASS** | See Section 4 below; Pages 1, 9, 10, 11, 13 |
| 4 | Cross-document consistency vs exact 0052 source; 0052 text treated as **minutes**, not percentages | **PASS** | Page 3 (`35/20/35 分鐘`…`20/20/50 分鐘`, `90 分鐘`), Page 6 M1 (`360 分鐘`), Page 10 (explicit `分鐘`), Register F019–F023, F032–F033 |
| 5 | Audit 40-row register: unique IDs, fields, exact SHA binding, page/body locators, replacements, roles | **PASS** | Register SHA `65c5c4c7…909e9d`; all 40 rows (F001–F040) match body text and rendered pages; no discrepancies found |
| 6 | P0-SYN defined; P2 50% threshold only internal SAMPLE comparison, not official/association rule | **PASS** | Page 2 (`P0-SYN（本案合成計畫草稿版號） 是案例草稿`); Page 5 (`不是官方標準，也不是協會已核定規則`); Register F039–F040 |
| 7 | Sample/Real boundaries; no fabrication of REAL training, recruitment, approval, humans, materials, trainer, venue, insurance, or outcomes; UNKNOWN where evidence absent | **PASS** | Pages 1 (`目前 REAL 狀態：UNKNOWN`), 2 (`UNKNOWN`; P0-SYN not approved version), 12 (REAL evidence table all UNKNOWN), 18 (REAL replacement list); every register row marked `SAMPLE/SYNTHETIC` |
| 8 | Title-blind test: body alone identifies five-dimension course-fit analysis; negative neighbors rejected | **PASS** | Pages 1–2 body explicitly describes I12-E01 five-dimension fit analysis without relying on title/filename; Page 2 table separates 0052/I11-E04, 0054/I12-E02, 0056/I12-E04; Page 18 Appendix C maps each neighbor to its own boundary |
| 9 | Single synthetic 2026-10-03 → 2026-10-08 cycle transparently demonstrated; no false multi-year or REAL continuous-improvement claim | **PASS** | Pages 3 (`示範日期`), 9–11 (baseline vs revised), 13–14 (actions); text states `不足以稱為多年趨勢或持續成效` |
| 10 | Visual/readability scope from 18-page Word PDF; body ≥10.5 pt, table ≥9.5 pt; distinguish 8.5 pt section kickers from body | **PARTIAL / UNKNOWN** | Images 1–6 reviewed; body and tables legible, section kickers visually smaller/distinct; exact pt sizes **cannot be numerically verified** from attached images |
| 11 | Unambiguous PASS/PARTIAL/FAIL, criterion matrix, exact locators, recomputed arithmetic, register audit, exact SHA | **PASS** | This review |

---

### 4. Recomputed Arithmetic

| Item | Candidate Claim | Independent Recomputation | Match? |
|------|----------------|---------------------------|--------|
| Baseline conformance | 11/15 = 73.3% | 11 ÷ 15 × 100 = 73.333…% → 73.3% | Yes |
| Revised conformance | 14/15 = 93.3% | 14 ÷ 15 × 100 = 93.333…% → 93.3% | Yes |
| Difference | +3/15 = +20.0 pp | (14/15 − 11/15) × 100 = +20.000… pp | Yes |
| 學員 baseline | 2/3 = 66.7% | 66.666…% → 66.7% | Yes |
| 教材 baseline | 1/3 = 33.3% | 33.333…% → 33.3% | Yes |
| 師資 baseline | 3/3 = 100.0% | 100.0% | Yes |
| 教學方法 baseline | 2/3 = 66.7% | 66.666…% → 66.7% | Yes |
| 訓練設施 baseline | 3/3 = 100.0% | 100.0% | Yes |
| G1 baseline time | 35+20+35 = 90 分鐘 | 90 min | Yes |
| G1 baseline practice share | 35/90 = 38.9% | 38.888…% → 38.9% | Yes |
| G1 proposal time | 20+20+50 = 90 分鐘 | 90 min | Yes |
| G1 proposal practice share | 50/90 = 55.6% | 55.555…% → 55.6% | Yes |
| G1 delta | +15 min, +16.7 pp | +15 min; 55.6% − 38.9% = 16.666… pp → 16.7 pp | Yes |
| Total course time | 90+90+120+60 = 360 分鐘 | 360 min (breaks/admin excluded) | Yes |
| Readability baseline | 4/6 correct | 4/6 = 66.666…% (derived; **not printed** in body) | Confirmed absent from body |
| Readability revised | 5/6 = 83.3% | 83.333…% → 83.3% | Yes |

All arithmetic in the candidate is correct. The 0052 source segments (35/20/35 and 20/20/50) are correctly interpreted as **minutes**, not percentages; the erroneous R01 percentage interpretation (81/9) is not repeated.

---

### 5. 40-Row Register Audit

- Register SHA-256: `65c5c4c7c8b5393481102a5e8f961640701c264454fdd53233a0dc0692909e9d` — matches packet.
- All 40 rows (SYN-0053-F001 through F040) were independently checked against:
  - `fact_id` uniqueness: all unique.
  - `candidate_sha256`: all rows bind to `cc755832…1f8e8`.
  - `body_locator` / `rendered_page`: every locator resolves to the rendered text provided (e.g., F019 page 3, F030 page 9, F034 page 14, F039 page 2).
  - `real_replacement_source` and `replacement_responsible_role`: populated for every row; no empty replacement fields.
  - `status`: all `SAMPLE/SYNTHETIC` — `待 REAL 替換`; no row claims REAL status.
- **No discrepancies found.** Register is consistent with the DOCX body.

---

### 6. Cross-Document 0052 Minutes Audit

The exact 0052 R01 source (SHA `406d1ef2…d455`) records:
- Table 20, row 2: `35/20/35` → `20/20/50` (說明/示範/引導練習), `增加 15 分鐘演練`, `不加總時數`.
- Table 22, row 2: `20 分重點說明+20 分示範+50 分引導演練`.

DOCX 0053 R03 correctly treats these as **minutes**:
- Page 3: `35/20/35 分鐘` → `20/20/50 分鐘`, `兩組各合計 90 分鐘`.
- Page 6: M1 `計畫總教學時間 360 分鐘`.
- Page 10: `基線 35+20+35=90 分鐘`; `方案 A 20+20+50=90 分鐘`; `練習增加 15 分鐘`.
- Register F032–F033 confirm minutes and derived percentages (38.9% → 55.6%, +16.7 pp).

**0052 feedback-based planning is not conflated with 0053 fit analysis.** Page 2 explicitly bounds 0052 as SAMPLE input only.

---

### 7. Negative-Neighbor / Title-Blind Test

**Title-blind:** With title, filename, and sequence number masked, the body on Pages 1–2 independently identifies the document as the I12-E01 five-dimension course-fit analysis (Page 2 header `官方原文｜I12-E01｜流水號 056`; Page 1 `五面向` repeated throughout). It cannot be repurposed without modification for another requirement.

**Negative neighbors:**
| Neighbor | Requirement | 0053 Boundary |
|----------|-------------|---------------|
| 0052 / I11-E04 | 依學員及結訓學員意見規劃或修訂課程 | Page 2: only SAMPLE course-plan input; no重贴 questionnaire, no claim of REAL feedback or course delivery. Page 18 Appendix C: `只把其 SAMPLE 課程計畫當分析輸入`. |
| 0054 / I12-E02 | 依遴選標準和流程選擇學員，教材推薦/審查 | Page 2: does not replace REAL individual selection, committee resolution, appointment letters, or material-approval originals. |
| 0056 / I12-E04 | 設備安檢或場地投保證明 | Page 2: does not produce, forge, or replace any third-party facility-inspection or insurance originals. Page 18 Appendix C: requires REAL field-survey/equipment-maintenance originals. |

All three neighbors are cleanly separated; no copied or conflated work.

---

### 8. Sample/Real Boundary Audit

- Every date, person, count, amount, ratio, score, result, meeting, and decision in the body is marked `SAMPLE/SYNTHETIC`.
- `REAL` status is explicitly `UNKNOWN` on Pages 1, 2, 12, 14, and 18.
- No actual association training, recruitment, approval, human participation, materials, trainer, venue, insurance, or outcome is fabricated.
- Register F038 states `不得 REAL 開課`; Page 13 states `不得宣稱 REAL 課程已可開辦或已獲核准`.
- Page 18 Appendix C lists the REAL materials required before升格 (approved course plan, class roster, material versions, trainer credentials, venue/equipment originals, etc.).

---

### 9. Material Defects & Minimum Targeted Fixes

**No material defects found.** All substantive criteria pass independently.

Observation (non-material, no fix required for PASS):
- Page 3 refers to G1–G4 as `90 分`, `120 分`, `60 分` using `分` rather than `分鐘` in the case-scope sentence. Context on the same page (`合計 360 教學分鐘`) and Pages 6/10 (`分鐘`) disambiguates this as minutes. No fix required; if the builder wishes to remove any residual ambiguity, a minimum targeted edit would be to add `分鐘` after each unit figure on Page 3.

---

### 10. Visual / Layout Scope Statement

Attached images reviewed:
- Image 1: 18-page contact sheet.
- Images 2–6: rendered Pages 2, 5, 8, 10, 18.
- Image 7: official source PDF Page 4.

Body text and tables are legible; section kicker labels (e.g., `01 需求定位`) are visually distinct and smaller than body text, consistent with the 8.5 pt kicker allowance. **Exact point sizes cannot be measured from images**; therefore the Blueprint font floor (body ≥10.5 pt, table ≥9.5 pt) is marked **PARTIAL / UNKNOWN** for this review only. No layout anomaly was observed in the inspected pages.

---

### 11. Exact SHA Reviewed

**`cc75583238dba42eede61de990992770f8de75e96d1bcfe1313e57629551f8e8`** — recomputed from local DOCX bytes and confirmed identical to the packet assertion.

---

**This is an independent candidate review only. It is not official association acceptance, REAL evidence, or promotion.**
