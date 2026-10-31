# Independent exact-SHA review — DOCX 0049 R01 repair

Review this candidate as an independent, read-only reviewer. Do not edit, rebuild, or save any artifact.

## Exact candidate under review

- DOCX: `candidate/0049_R01.docx`
- Required SHA-256: `955f7138951cf9f37863116540159a908c2693ce4b006c5a9bb2914f3b2de291`
- Size: 61,772 bytes
- Mapping: DOCX 0049 = Unique Blueprint `I11-E01` = official checkbox sequence `051` (not 049).
- Official requirement: `訓練課程計畫配合業主、受訓者以及職能需求等調查規劃的證明。`

If the on-disk SHA differs, stop and report FAIL without reviewing another version.

## Sources and review evidence

Read the candidate itself, `SOURCE_MAP_R01.md`, `evidence/build/BUILD_METADATA_R01.json`, `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`, and the current `evidence/qa/TECHNICAL_VISUAL_QA_R01.json`.

Verify against the actual official source image `source/official_evidence_table_page4.png`, the unique Blueprint row for 0049 in `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl`, the applicable writing manual and checkbox blueprint in `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES`, and these exact cross-document source artifacts:

- DOCX 0033 R03: SHA-256 `fe5f3cfd84c761da86435a71e0fd899daa725be78628c4d2d3f2324c1fdb5f4f`.
- Its replacement register: SHA-256 `d114f36d9c4852cda2239bf22fcc709bdc0a40aad62418e076c6b9c2ae523247`.
- Same synthetic case ID: `SYN-0033-PLAN-01`; these two documents represent one sample survey and its downstream course plan, not two surveys.
- Render to inspect: `evidence/render_R01_955f7138/0049_R01.pdf` and every one of its 15 `page-*.png` images. These are exported from Microsoft Word on this Windows host. Do not inspect older render directories as substitutes.

## Required independent checks

1. Exact official wording, document genre, and scope for 051; distinguish 0049/I11-E01/051 from 0033/I07-E01/033, 0048/I10-E03/049, and 0050/I11-E02/052.
2. The content must remain a real, usable three-source-demand-to-course-plan document, not a survey-only report, unit lesson plan, procurement/minutes record, or generic template. Check the body with title/front cover mentally masked.
3. Recompute/check the linked data and formulas from 0033, including the three-source denominators, importance/self-rating means and gaps, option weights/scores, and 90+90+120+60=360 minutes.
4. Verify the prior concrete defects are actually corrected in the DOCX and register: 0033 printed Table 12 is the option-weight comparison; printed Table 13 carries the course objectives/module basis; the p.1 quick guide points to §4.1 for option comparison; the shared sample planned cohort is 12, with a 14-seat sample room estimate for 12 learners plus two teaching staff. Search for any stale contradictory wording.
5. Verify the 158-row register has unique fact IDs and covers every synthetic figure. Confirm SAMPLE/SYNTHETIC is never presented as association activity, approval, authorization, actual attendance, course delivery, result, or third-party evidence.
6. Determine whether the document is practically usable by association administrators and evaluators: actionable course design, objectives, content/method, schedule, staffing/resources/environment, assessment timing/scales/thresholds, failure/retraining/reopen conditions, replacement gates, and clear allocation to 0048/0050.
7. Inspect all 15 final rendered pages at readable scale. Check clipping, overlap, table/page splits and repeated headers, orphan headings/headers, body/table font floors, and whether section 10.1 begins with its four gate rows together. Pay special attention to any new regression after the corrections.

## Required response

Return one concise, complete report under 2,500 words; do not leave the last sentence unfinished. Start with exact on-disk SHA and verdict `PASS`, `PARTIAL`, or `FAIL`. Give a result for each of the seven checks above. For every defect, provide page/section/table-row locator, why it matters, and whether DOCX bytes need repair. If there are no material defects, state so explicitly. The result is an independent candidate review only; it does not grant formal Human acceptance or promotion.
