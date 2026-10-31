# Independent exact-SHA review request — DOCX 0049 R01

Review the current candidate as an independent, read-only reviewer. Do not edit, rebuild, save, or reformat any candidate or source file. If the on-disk candidate SHA differs from the required SHA below, stop and report the mismatch without reviewing another version.

## Exact candidate

- Path: `docs/ttqs-quality-20261016/quality-review/0049_R01/candidate/0049_R01.docx`
- Required SHA-256: `e8212788b1f7b201ca4af4f4c5fb83ab131627dbfa815987f7cf6344edfda727`
- Size: 61,773 bytes
- Identity: DOCX 0049 = Unique Blueprint `I11-E01` = official evidence-table checkbox `051`, official source page 4.
- Official requirement: 「訓練課程計畫配合業主、受訓者以及職能需求等調查規劃的證明。」
- Candidate state remains `CANDIDATE_ONLY`; formal acceptance is `NOT_GRANTED`.

## Primary sources to inspect directly

Read the full candidate, `SOURCE_MAP_R01.md`, `evidence/build/BUILD_METADATA_R01.json`, `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`, and `evidence/qa/TECHNICAL_VISUAL_QA_R01.json`. Independently verify the official source image at `source/official_evidence_table_page4.png`, the current Unique Blueprint row for 0049 in `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl`, the Indicator 11 writing manual and I11 checkbox specifications in `docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md` and `03_157_CHECKBOX_BLUEPRINTS.md`, and the complete DOCX 0033 R03 plus its replacement register.

Recompute the source hashes before relying on cross-document facts:

- DOCX 0033 R03: `fe5f3cfd84c761da86435a71e0fd899daa725be78628c4d2d3f2324c1fdb5f4f`.
- DOCX 0033 synthetic register: `d114f36d9c4852cda2239bf22fcc709bdc0a40aad62418e076c6b9c2ae523247`.
- Shared example case: `SYN-0033-PLAN-01`. This is one synthetic survey feeding one synthetic plan, not two surveys or an association activity.

Visually inspect the Word-native final render `evidence/render_R01_e8212788/0049_R01.pdf` and every `page-01.png` through `page-15.png`. Do not substitute an older render folder or review-history DOCX.

## Required checks

1. Verify exact official wording, correct genre/scope for checkbox 051, and the distinction from 0033 / I07-E01 / 033, 0048 / I10-E03 / 049, and 0050 / I11-E02 / 052.
2. With the cover/title masked, decide whether the body is a mature, practical three-source demand-to-course plan rather than a survey report, unit-level lesson plan, meeting record, or generic template.
3. Recompute denominators, importance and confidence means, gaps/ranking, weighted option scores, and 90+90+120+60=360 teaching minutes against 0033 R03.
4. Verify prior repairs remain correct: printed 0033 table 12 is the option comparison; table 13 is the objectives/module basis; the quick guide points to §4.1; cohort is 12 and sample room estimate 14; the §10.1 gate rows stay together. Search for stale contradictory text.
5. Confirm the register contains 158 unique fact IDs with complete replacement provenance, and that SAMPLE/SYNTHETIC facts are never represented as real association survey, authorization, decision, approval, attendance, delivery, assessment result, or third-party evidence.
6. Verify practical use by association administrators and evaluators: source and authority checks, decisions and alternatives, objectives, content/method/schedule/staff/resources/environment, assessment timing/scales/thresholds, failure/retraining/reopen conditions, and replacement gates.
7. Independently inspect all 15 page images for clipping, overlap, table splits/repeated headers, orphan headings, readability, and body/table font floors. Report page-specific findings.
8. Recheck the two minor R02 findings against the current exact candidate and packet: (a) §2 owner/client demand row should identify Q04 raw values as `0033 R03 表8`, while not misidentifying 0033's printed table 3; (b) SOURCE_MAP candidate SHA and render path/page count should match this exact candidate and 15-page render.

## Response requirements

Return one complete report under 2,500 words. Begin with the verified on-disk SHA and exactly one verdict: `PASS`, `PARTIAL`, or `FAIL`. Give a result for each of the eight checks. For each defect, state exact page/section/table-row locator, why it matters, whether DOCX bytes need repair, and the smallest adequate fix. Explicitly state whether any material defect remains. This is an independent exact-SHA candidate review only; do not grant Human acceptance, production status, or promotion. Do not edit or save any artifact.
