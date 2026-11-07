# Independent semantic review request — DOCX 0050 R01

Review target: DOCX 0050 R01, candidate-only. This is an independent semantic review, not a build check and not Human acceptance.

## Required exact target

Open and inspect this local Word file directly, recompute its SHA-256, and report whether it is exactly:

`E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0050_R01\candidate\0050_R01.docx`

Required SHA-256: `d0d37c2c69b161a2cdd37ee3097306722c4a65a1afd844ae92e1dff58b43381a`.

Do not edit, save, rebuild, or normalize the DOCX or any source. Do not rely on a Builder PASS or this request's summaries as proof. Read the candidate's actual paragraphs and every table. You may use the source files below and recalculate facts yourself.

## Requirement identity and sources to inspect

- DOCX 0050 is Unique Blueprint `I11-E02`, official checkbox `052`; it is not official line 050, not checkbox 050, and not 0049/I11-E01/051 or 0051/I11-E03/053.
- Official requirement wording: 「各課程單元內容均能達成訓練規劃的目標。」
- Official source page image: `E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0050_R01\source\official_evidence_table_page4.png`.
- Current Blueprint row: `...\inputs\UNIQUE_BLUEPRINT_0050.jsonl`.
- Source map: `...\inputs\SOURCE_MAP_R01.md`.
- Same-case course plan 0049 R01 and its register: `...\quality-review\0049_R01\candidate\0049_R01.docx` and `...\quality-review\0049_R01\evidence\SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`.
- Same-case survey 0033 R03 and its register: `...\quality-review\0033_R03\candidate\0033_R03.docx` and `...\quality-review\0033_R03\evidence\SYNTHETIC_REPLACEMENT_REGISTER_R03.csv`.
- Candidate fact register: `...\quality-review\0050_R01\evidence\SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`.
- Render evidence, for contextual page locations: `...\quality-review\0050_R01\evidence\render_R01_d0d37c2c\page-01.png` through `page-18.png`.

All `...` above are relative to `E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review` unless an absolute path is shown. Resolve them within that repository only.

## Required independent checks

1. Compute the candidate's exact SHA and confirm the review is bound to those bytes.
2. Compare the requirement text and doc ID/Blueprint/official checkbox with the official page and current Blueprint. State exact section/table/page locators.
3. Apply a title-masked test: identify the document genre and requirement from the working body alone. Decide whether this is a practical unit-level lesson-design package rather than a generic strategy plan, survey, meeting record, or course-level plan.
4. Compare the two nearest requirements: 0049/I11-E01/051 (course-level demand-to-plan) and 0051/I11-E03/053 (training-output deliberation). State concrete evidence that 0050 is distinct and not a wrong-document substitution.
5. For each of the four units, inspect whether the unit objective is observable; teaching content and instructor/learner actions teach and practise it; the time plan is executable; the work product is identifiable; the criterion is explicit; and the evidence supports the criterion. Cite unit section and table numbers.
6. Inspect actual usability: student scenario cards and answer fields; partner role-play rubric and retake; five-field handoff record; integrated exercise; separate tutor-only keys; 10-item A and B quizzes; question-to-objective alignment; and the completed synthetic score interpretation. Confirm that answer keys are not exposed in the student fields and whether keyed answers match the options.
7. Recompute arithmetic from the candidate: unit totals and segments, each quiz's item count and score denominator, thresholds, and sample pre/post calculation. Flag any difference or unsupported conclusion.
8. Verify same-case links against the actual 0033 R03 and 0049 R01 candidates/registers. Check course name, case ID, unit goals, durations, and any reused numbers. Distinguish reused sample facts from new 0050 teaching-design assumptions.
9. Verify the 99-row replacement register is fact-level, uses unique IDs, identifies locators and real replacement sources, and does not convert synthetic data into association fact. Check that no sample score, role, approval, class, staff appointment, teaching, attendance, or outcome is asserted as real.
10. Determine whether an administrator or trainer at the original-point association can use the materials directly after authorized real sources replace the synthetic inputs. Identify any missing instruction, field, control, accessibility, or rejection condition that would prevent practical use.
11. Inspect the rendered pages only for material readability problems; do not treat page count or builder output as semantic evidence.

## Response format

Return a concise but evidence-specific review with:

- `VERDICT: PASS`, `PARTIAL`, or `FAIL`.
- Exact SHA-256 inspected and whether it matches the requested SHA.
- A table of check, verdict, and page/section/table locator.
- Any material defect with its precise location and smallest necessary repair.
- Any non-material observation separately.
- Explicit statement that the artifact remains `CANDIDATE_ONLY`, no Human acceptance is granted, and no promotion is authorized.

If a source file cannot be opened or exact identity cannot be verified, say so and return PARTIAL/FAIL as appropriate. Do not invent evidence or modify files.
