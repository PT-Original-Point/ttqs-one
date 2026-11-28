# DOCX 0049 R01 — Source map and evidence boundary

## Identity

- Project: `TTQS_ONE`
- Document: `0049`, revision `R01`
- Unique Blueprint: `I11-E01`
- Official evidence-table checkbox sequence: `051` (official PDF page 4)
- Official requirement: 「訓練課程計畫配合業主、受訓者以及職能需求等調查規劃的證明。」
- Candidate SHA-256: `e8212788b1f7b201ca4af4f4c5fb83ab131627dbfa815987f7cf6344edfda727`
- State: `CANDIDATE_ONLY`; formal acceptance `NOT_GRANTED`.

## Source authority

| Source | Exact location and SHA-256 | Use and limit |
|---|---|---|
| Official training evidence table | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\DRIVE_READBACKS\DRIVE_OFFICIAL_EVIDENCE_TABLE.pdf`, p. 4; `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` | Establishes the exact official wording and page. Page image is included under `source/`. It does not establish that the association conducted this survey or course. |
| Current Unique Blueprint | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl`, row `deliverable_id=0049`; file SHA-256 `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e` | Defines 0049 as I11-E01 / three-source demand-to-course plan, its required content, replacement register and acceptance conditions. |
| Writing manual | `docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md`, Indicator 11, lines 81–86 | Requires commissioner, learner and competency-analysis demand sources with priority; SAMPLE where actual demand evidence is absent. The separate unit-level objectives belong to 0050; training-output review belongs to 0051. |
| 157-checkbox contract | `docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md`, I11, lines 127–133 | Distinguishes official checkboxes 051/052/053. 051 requires source locations, substantive example, decision/result, and cross-document fact links. |

## Same-case source and cross-document boundary

The complete example uses case `SYN-0033-PLAN-01`, the same synthetic case as DOCX 0033 R03. It is one survey and one planned response, not two independent surveys and not an association activity.

- DOCX 0033 R03: `I07-E01`, official checkbox `033`, SHA-256 `fe5f3cfd84c761da86435a71e0fd899daa725be78628c4d2d3f2324c1fdb5f4f`.
- 0033 synthetic replacement register SHA-256: `d114f36d9c4852cda2239bf22fcc709bdc0a40aad62418e076c6b9c2ae523247`.
- 0033 supplies the same-case survey populations, anonymous raw ratings, importance/confidence calculations, option scores and four unit durations. 0049 reuses those facts to demonstrate course-plan decisions and does not recalculate the survey as a second collection.
- DOCX 0050 (`I11-E02`, checkbox `052`) owns detailed per-unit objectives and instruction/assessment alignment. No 0050 candidate is claimed as a completed matching package here.
- DOCX 0048 (`I10-E03`, checkbox `049`) is procurement/trainer meeting evidence. It is a different requirement and is expressly excluded from 0049.

## Example inputs and calculations

All facts below are `SAMPLE/SYNTHETIC`, and every one is listed in `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv` (158 unique fact IDs). Three synthetic source groups each have four invited participants: the cooperation-window proxy returned 3/3 valid; intended learners returned 3/3 valid; task-role representatives returned 4, of which 3 are valid because one lacks a complete Q04 importance matrix. Aggregate: 12 invited, 10 returned, 9 valid; return rate `10/12=83.3%`, valid/invited `9/12=75.0%`, valid/returned `9/10=90.0%`.

The cooperation-window role is only a synthetic proxy for a demand proposer. It is not a real client, commissioner, contract party, or authorization. Actual owner, trainee and competency/task sources, their authority, original instruments and dates must be replaced from real, authorized source records before any real-world use.

Across nine valid synthetic responses, importance totals are A/B/C/D = 41/38/35/39 and confidence self-rating totals are 24/25/27/21. Means and gaps are recomputed from these sums. The sample-only priority rule is importance at least 4.00/5 and gap at least 1.20; this is neither official nor association policy. Alternative weighted scores use the same-case 0033 R03 four dimensions at 40/30/20/10 percent and equal 4.80, 4.00 and 3.50 out of 5. Four planned instructional units total `90+90+120+60=360` teaching minutes; breaks and administration are excluded.

The Q04 importance raw values are in the printed `0033 R03 表8`; 0033's printed `表3` is a different causal-chain table. The 0049 R01 §2 source table cites `0033 R03 表8` directly. The option-weight comparison and unit objectives/module basis cite the printed `0033 R03 表12` and `表13`, respectively.

## Artifact and visual evidence

- Candidate DOCX: `candidate/0049_R01.docx`
- Synthetic fact-by-fact replacement register: `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`
- Build/source SHA record: `evidence/build/BUILD_METADATA_R01.json`
- Current render: `evidence/render_R01_e8212788/0049_R01.pdf` and `page-01.png` through `page-15.png` (Microsoft Word native PDF export, then bundled Poppler rasterization)
- Exact-SHA review history: R02 reviewed `955f7138951cf9f37863116540159a908c2693ce4b006c5a9bb2914f3b2de291` and returned `PARTIAL`; both minor findings were corrected here. R03 reviewed the current candidate SHA above and returned `PASS`; it found no material defect. Its two observations are register source-fact links for 25 derived aggregates (optional) and clarifying that G1's five cases are a subset of the 10-item quiz (cosmetic); neither requires changing DOCX bytes. See `review/opencode_v2_R03/opencode_v2_review_result_R03.md`.
- Official source excerpt: `source/official_evidence_table_page4.png`
- Technical and visual receipt: `evidence/qa/TECHNICAL_VISUAL_QA_R01.json`
- Independent exact-SHA review requests and original reviewer results: `review/packet_R01/`, `review/opencode_v2_R01/`, `review/packet_R02/`, `review/opencode_v2_R02/`, `review/packet_R03/`, and `review/opencode_v2_R03/`.

The sample demonstrates a complete plan and a route to replace facts with originals. It contains no real personal data and claims no real survey, approval, appointment, attendance, delivery, assessment result, or outcome.
