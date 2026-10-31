# Independent exact-SHA semantic review — DOCX 0080 R05

Read-only review. No source, candidate, receipt, DOCX, PDF, or image was edited or created except this review note.

## 1. Candidate identity

- Observed SHA-256: `5a4d400b472d2b6f0cfcec23bd1cd908f468d3ba857aea19dba8b699b375055b`
- Required SHA-256: `5a4d400b472d2b6f0cfcec23bd1cd908f468d3ba857aea19dba8b699b375055b`
- Identity: **PASS** (exact match; reviewed actual DOCX bytes, including nested tables, header/footer and document.xml text, not only the Markdown body).
- Rendered PDF: `evidence/render_R05/0080_R05_word_export.pdf` (23 pages, SHA-256 `1fe0c231669fc50a42007ee188be78cc3341d9730c82fba851decda3266a8a64`).
- Visual receipt: `evidence/visual_review_R05.json` (layout_result PASS).
- Technical receipt: `evidence/technical_review_R05.json` (status PASS).

## 2. Verdict

**PASS** — semantic quality is adequate for candidate review. This is **not** formal acceptance.

## 3. Finding table

| ID | Severity | Locator (printed page / section / table / cell) | Evidence | Required remedy |
|---|---|---|---|---|
| — | None | No blocking or minor semantic defect requiring remedy was identified in the reviewed DOCX bytes, rendered 23-page PDF, nested tables, or cross-document mapping. | All required identity, official 17b alignment, mature-use content, recomputed arithmetic, cross-document mapping, sample/real boundary, wrong-document/substitution, and layout checks pass (see §4). | None required. |

Non-substantive note (not a semantic defect): `docProps/app.xml` reports stale metadata (`Pages=1`, `Words=0`, `Characters=0`); the rendered export has 23 pages. No semantic impact, consistent with prior candidate reviews.

## 4. Explicit result for every required check

### 4.1 Correct identity and genre — PASS

- p.1, §1.1–1.3, cover/header: states `DOCX 0080 / I17B-E02 / official checkbox 085 / indicator 17b` and title `課程評量與學員建議檢討紀錄`; explicitly states it is not document 0085, not checkbox 080/088, not an individual career plan, closeout progress audit, or 30-day transfer survey.
- p.1, table §1.2: `文件 SAMPLE/SYNTHETIC 候選示範（R05）`, `正式接受 NOT_GRANTED`, `真實證據 REAL=UNKNOWN/HOLD`, `官方勾選 085 PARTIAL/HOLD`, `17b 等級 不主張任何等級`.
- p.2, §1.3: `文件編號 0080 ≠ 官方勾選序號 085`, `084 是 0076 至 0079 … 複合方框；085 是本文件的官方方框；086 與 088 均屬其他要求`.
- p.21, §12: cross-document table repeats the same non-substitution statement.

### 4.2 Official 17b alignment — PASS

- p.2, §2.1: reproduces official p.6 17b grading `0 分未執行；1 分執行考試或實作評量；2 分 … 將結果與缺失彙整分析納入結案報告，作為下次課程規劃修正依據；3 分依修正決定進行課程改善且有具體成效`; states the document demonstrates the 2-point “彙整分析與改課依據” expression and preparatory fields toward 3, but does not claim any level.
- p.3–p.7, §2.2 evidence matrix (nested 6×2 cards) and §3: shows evaluation results and learner suggestions analyzed; wrong answers/skill gaps (Q01/Q17/Q18/Q19, record-accuracy subscore) become course-change proposals (§7.1–7.2).
- p.16–p.17, §8: next-cohort assessment schedule, 0–2 rubric and sample-only provisional threshold (8/10) plus HOLD conditions; explicitly states 30-day behavior transfer belongs to 0082.
- No claim of level 2/3 achieved; `REAL=UNKNOWN/HOLD` and `NOT_GRANTED` maintained throughout.

### 4.3 Mature use — PASS

- Complete synthetic review record: p.12–p.14, §6.1–6.11 (agenda/timings §6.2; role placeholders §6.3; evidence inputs §6.4; discussion §6.5; options §6.6; selected option & reasons §6.7; open questions §6.8; roles/deadlines §6.9; expected products §6.10; not-convened declaration §6.11).
- Alternatives and reasoned selection: p.10–p.12, §5.1 (three options) and §5.2 (selection reasons) and §5.3 (open questions).
- Proposed objectives/method/roles/deadlines/products: p.14–p.15, §7.1–7.4; p.16–p.18, §9 (A1–A7 with sample target dates and status `PROPOSED / SAMPLE / NOT EXECUTED`).
- Next-cohort assessment schedule/rubric/sample threshold/hold rules: p.16, §8.1–8.3.
- Usable blank form: p.18–p.19, §10.2 (27-row blank review form, stated for use only after the §6 filled example).
- Source substitution register: p.20, §11.1 (SYN-0080-001–023 ranges) backed by `inputs/SYNTHETIC_REPLACEMENT_REGISTER_0080_R01.csv` (23 rows).
- Reject/hold conditions: p.20, §11.2 (full list) and §11.3 data protection.

### 4.4 Recomputed arithmetic and source integrity — PASS

Recomputed from the actual CSVs:

- 0076 assessment CSV (SHA-256 `348106b5…c96ad5d`): n = 16; pre total 870, mean 54.375; post total 1265, mean 79.0625; gain +24.6875; post ≥ 80 = 9/16; practical total 253, mean 15.8125/20; subscores communication 66/16 = 4.125/5, privacy 65/16 = 4.0625/5, record accuracy 57/16 = 3.5625/5, handoff 65/16 = 4.0625/5; record accuracy ≤ 3 = 8/16; practical PASS 11, HOLD 5. All match the document (p.3–p.4, §2.2 cards; p.7, §3.1 table; p.7, §3.3 table; p.22, Appendix B).
- 0076 item-analysis CSV (SHA-256 `215dad15…792a9bd`): Q01/Q17/Q18/Q19 = 11/16 (0.6875); Q02/Q03 = 12/16 (0.75); all 20 item counts match the technical receipt; sum of item correct counts = 253, matching the practical total numerically (document notes the coincidence and warns against conflating scales).
- 0077 reflection CSV (SHA-256 `3bdce0a1…6bc6e985`, the corrected hash): themes NEEDS_CLARIFICATION 5, PRIVACY_CONSENT 3, RECORD_ACCURACY 4, CLOSED_LOOP_HANDOFF 3, ROLE_BOUNDARY 1; total 16; percentages 31.25/18.75/25.00/18.75/6.25 summing to 100.00. All match (p.9, §4.1 table; p.23, Appendix B).
- Practical subscores reconcile to the practical total (253) with no mismatch.
- Source hashes cited in p.22, Appendix A all match recomputed values: official checklist `805386b7…`, 157-box blueprint `ad03323d…`, UNIQUE_BLUEPRINT_0080_R03 `a13ba084…`, SOURCE_PACKET_0080_R03 `1a4f761e…`, SYNTHETIC_REVIEW_DATA `3f1f1582…`, SYNTHETIC_REPLACEMENT_REGISTER `4a063307…`, 0076 assessment `348106b5…`, 0076 item analysis `215dad15…`, 0077 reflection `3bdce0a1…` (corrected), 0079 R07 `0361cf65…`.

### 4.5 Cross-document mapping — PASS

- p.21, §12 table: 0076/0077/0078/0079 = I17B-E01 / checkbox 084; 0080 = I17B-E02 / checkbox 085; 0081 = I17B-E03 / checkbox 086; 0082 = I17C-E01 / checkbox 088. No serial/file-number substitution found (`085` never written as `DOCX 0085`; `0080` never written as checkbox 080/088 except in explicit negations).
- 0079 R07 exact SHA `0361cf65557733cb3e1af93d5e59197aa96d307622a840800d008d8c580c66a7` verified independently and cited at p.9, §4.3 and p.22, Appendix A.
- No disclosure of individual 0079 card contents: p.9, §4.3 states the group record must not reveal any individual card content, quote or score, and may use only non-identifying aggregate restriction language; p.22, Appendix A repeats `不得抄錄個別內容`.

### 4.6 Sample/real boundary — PASS

- All meeting, role, date, decision, score, threshold, plan and result content is labeled `SAMPLE/SYNTHETIC`, `PROPOSED`, `NOT_EXECUTED`; the synthetic meeting is declared not convened (p.12, §6.11; p.1, cover).
- No real participants, consent, meeting, approval, execution, improvement, credentials, signatures or outcomes are fabricated; roles are function placeholders only (p.12, §6.3; p.15, §7.3).
- `REAL=UNKNOWN/HOLD` and `formal_acceptance=NOT_GRANTED` are stated on the cover (p.1), §1.2 table, §6.1, §11, and final line (p.23).
- No claim that the association has executed, approved, improved, or reached any 17b level.

### 4.7 Wrong-document / substitution test — PASS

- With the title hidden, the body still clearly serves checkbox 085: it is a course-evaluation and learner-suggestion review record built on 0076 assessment/item analysis and 0077 reflection themes, producing low-item/skill-gap analysis, three-option comparison, a synthetic review record, course-change proposals, next-cohort assessment design, and hold/reject rules.
- It is distinguishable from 084 (composite of four distinct products 0076–0079), 086 (0081 closeout/action-plan verification; explicitly disclaimed at p.16, §8.4 and p.21, §12) and 088 (0082 30-day behavior transfer; explicitly disclaimed at p.16, §8.4 and p.21, §12).

### 4.8 Rendered 23-page layout — PASS

- All 23 pages are covered: R04 full-document contact sheet plus direct inspection of changed pages 1, 22 and 23 at original raster resolution; pages 2–21 are byte-identical to the reviewed R04 renders.
- p.22, Appendix A locator table keeps the final 0079 R07 source row on the same page; no single-row continuation remains at p.23.
- Appendix A 8.2-pt table text is readable at 115 DPI; all source locations and SHA-256 values are distinguishable.
- p.23 starts with the complete Appendix B calculation table and Appendix C; no clipping, overlap, trailing blank page, or broken border observed.
- `visual_review_R05.json`: page_count 23, layout_result PASS, semantic_review PENDING (now completed by this review).

## 5. Formal acceptance

`formal_acceptance=NOT_GRANTED`. The document is a candidate/sample artifact only; no real evidence, meeting, consent, approval, execution, improvement, credential, signature, or outcome is claimed. Checkbox 085 remains `PARTIAL/HOLD` pending real source paths. No official acceptance is declared.