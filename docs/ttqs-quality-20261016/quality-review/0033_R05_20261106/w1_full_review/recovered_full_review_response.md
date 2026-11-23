# Independent Semantic Review — 0033 I07-E01 R05

**Verdict: PASS** (with minor advisory notes, none blocking)

Scope statement: this review covers only the attached source-bound packet and extracted candidate text. I take the stated hashes (candidate a9f4e1c9…, official 805386…, Blueprint 406d…, register d114f3…) as asserted identifiers; I do **not** claim independent DOCX hashing, visual/page rendering inspection, layout or font-size verification, official acceptance, or any REAL evidence status.

## 1. Official requirement and locators
- Requirement string in the candidate (P006) is character-identical to the Blueprint's `official_requirement_text` and checkbox text: 「訓練課程計畫配合客戶及受訓者需求、職能需求的調查規劃的證明。」; page 2 cited, matching `official_evidence_table_page` = 2. The register's F0033_OFFICIAL_REQUIREMENT (第2節/表2/頁2) agrees.
- P006 adds the indicator label 指標7「訓練需求相關的職能分析及應用」— plausible but not verifiable within this packet's text scope; the requirement sentence itself is not reworded by any historical draft.

## 2. Purpose, genre, blind test
- P000–P002/P005 establish purpose (survey planning → course objective fit), reader (規劃理監事/主管/志工), use timing, and SAMPLE/SYNTHETIC status — satisfying the 30-second first-page test without evaluation-engineering jargon.
- Genre is survey-planning deliverable with directly usable instrument (表5, 18題； P023), workflow (表4/表5 area), blank REAL registers (表19/表20) — matches "可直接使用成品" genre. A reader with title/filename removed could identify the document as the survey-planning work product; it is not transplantable to 0032 or 0034 without modification.

## 3. Question mechanics and worked SAMPLE — full arithmetic recheck (all verified)
- Table 8 (重要度， 9 rows) column sums: 甲41, 乙38, 丙35, 丁39 — recalculated, correct.
- Table 9 (自評， 9 rows) column sums: 甲24, 乙25, 丙27, 丁21 — correct.
- Table 11 means/gaps: 41/9=4.56, 24/9=2.67, gap 1.89; 38/9=4.22, 25/9=2.78, gap 1.44; 35/9=3.89, 27/9=3.00, gap 0.89; 39/9=4.33, 21/9=2.33, gap 2.00 — all exact.
- Priority rule (P045/P048; F0033_PRIORITY_RULE): ≥4.00 and ≥1.20 → 丁(2.00) 1st, 甲(1.89) 2nd, 乙(1.44) 3rd; 丙 fails both, retained for risk check — internally consistent.
- Table 7 denominators: 4/3/3, 4/3/3, 4/4/3 → 12 invited, 10 returned, 9 valid; non-response = SYN-R11 (合作窗口) + SYN-R12 (預定受訓者) = 2; SYN-R10 exclusion (Q04 incomplete) pre-registered as a rule in 第6節 (P031) before use. Rates 10/12=83.3%, 9/12=75.0%, 9/10=90.0%; per-group rates correct; 9×4×2=72 scoring values all filled.
- Weights 40/30/20/10 sum 100%; weighted recalc 甲4.80, 乙4.00, 丙3.50 — exact. Modules 90+90+120+60=360 min/6 h. Register table-level citations (第7節/表7–9, 第8節/表10, 第9節/表12–13, 第10節/表14, 第13節/表18) all match the body.
- Register bookkeeping is at fact granularity: 72 raw ratings, dates, counts, scores, module content, weights, anchors, rationale, exclusion — each has a key (SYN-0033-PLAN-01 line). Table 9/Table 10 row SYN-R01 agrees with Table 21 (表18) Q04/Q05 answers.

## 4. Truth boundary
- P002/P012/P033/P088/P080 consistently mark all case data SAMPLE/SYNTHETIC; status UNKNOWN; REAL replacement area isolated (P080); recalculation-after-replacement required (P088); no future tense presented as completion; reviewer identity explicitly 待查 rather than fabricated.

## 5. Distinction from 0032 / 0034
- 表1 (TABLE 2) rows for 0032/I06-E03 and 0034/I07-E02, P005 (“不評估辦訓能力…不代替個別學員職能盤點”)， 表16 row “把自評當能力證明”， and 表22 checklist row □官方要求 satisfy the two-neighbor rejection test, including a checkable field (自評 vs 能力).

## 6. Rejection/hold criteria
- P071 enumerated rejection conditions cover empty instrument, missing denominators, market over-claim, self-as-competence, unmappable needs, unverified authority, unregistered synthetic data — matches Blueprint acceptance tests.

## Minor defects (advisory, non-blocking)
1. **Q07 off-list sample answer** — Register F0033_R01_Q07 / Table 21 (表18) / P057 chain: SYN-R01 Q07 second selection 「工作界線不清」 does not appear in the 表5 (TABLE 6) Q07 option list (不確定責任者；需求交接遺漏；說明服務範圍困難；流程不清；紀錄過多／過少；其他)； the worked answer does not mark 其他. Recommend aligning wording in R06.
2. **Rounding rule granularity** — P036 states 1-decimal rounding for the rates only; means/gaps are displayed to 2 decimals (表10) without an explicit rounding statement in P044.
3. **Required table pattern partial** — Blueprint `required_tables_or_figures` item 「欄位—定義—來源—填寫者—驗證規則」 is satisfied only in split/genre-adapted form (表19 two columns with embedded validation rules plus 表17 判定/覆核)， not as a single five-column table. Defensible under the genre-adaptation acceptance clause, but noted.
4. **Register granularity asymmetry** — the four ability constructs (甲乙丙丁 names and observable behaviors, 表11/Q04/Q05) are not fact-registered, while the analogous scale definitions are (F0033_SCALE_IMPORTANCE/SELF); they are covered only by the 表21 category row 「能力及課程需求」.

**Outcome: PASS.** All mechanism, denominator, formula, boundary, and neighborhood tests in the candidate text are internally consistent and reproducible; the four items above are polish targets for the next revision, not evidence-integrity failures.