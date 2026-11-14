# DOCX 0050 R01 source map and evidence boundary

## Identity

- Project: TTQS_ONE
- Document: 0050 R01
- Unique Blueprint: I11-E02
- Official evidence checkbox: 052, official evidence table page 4
- Official wording: 「各課程單元內容均能達成訓練規劃的目標。」
- Candidate SHA-256: `d0d37c2c69b161a2cdd37ee3097306722c4a65a1afd844ae92e1dff58b43381a`
- Candidate state: `CANDIDATE_ONLY`; formal Human acceptance: `NOT_GRANTED`

## Authoritative requirement sources

| Source | Version / locator | SHA-256 | Authority and limit |
|---|---|---|---|
| Official training-evidence table | PDF, page 4; accompanying page image is in `source/official_evidence_table_page4.png` | PDF `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` | Establishes the exact requirement and checkbox location. Does not prove an association course was delivered. |
| Current Unique Blueprint | `BLUEPRINT_CURRENT.jsonl`, row `deliverable_id=0050` | file `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; row `1204cbe5799e24ded84ad7c7a4dcf2ebb6fb0270f59ed5332f1982b714a1221a` | Defines the dedicated unit-level lesson-design evidence, required tables, sample controls, rejection conditions, source boundaries, and the I11-E02 identity. |
| Writing manual | `02_GENRE_WRITING_MANUAL.md`, Indicator 11 | Current contract branch | Used to distinguish unit-level design from course-level planning and training-output review. |
| 157-checkbox contract | `03_157_CHECKBOX_BLUEPRINTS.md`, I11-E02 | Current contract branch | Defines checkbox 052 separately from 051, 053, and 054. |

## Same-case, synthetic cross-document links

The worked example is case `SYN-0033-PLAN-01`. It is a single invented planning example; it does not represent a real survey, course, class, association decision, or delivery.

- DOCX 0033 R03, I07-E01 / checkbox 033: DOCX SHA `fe5f3cfd84c761da86435a71e0fd899daa725be78628c4d2d3f2324c1fdb5f4f`; synthetic-register SHA `d114f36d9c4852cda2239bf22fcc709bdc0a40aad62418e076c6b9c2ae523247`. It is the sample demand-survey source. 0050 does not reproduce its questionnaire or claim those results as real.
- DOCX 0049 R01, I11-E01 / checkbox 051: DOCX SHA `e8212788b1f7b201ca4af4f4c5fb83ab131627dbfa815987f7cf6344edfda727`; synthetic-register SHA `c79dd292c3679b83d334f5773694d2d9089dce7c7d532197d287e3c5ad5be501`. It is the same sample course plan and source for 0050's course title, four unit goals, 12-person planning assumption, and 360 teaching minutes.
- 0050 R01 owns the four unit-level lesson designs, student exercise materials, parallel assessment forms, scoring keys, sample score interpretation, and replacement gates. It must not substitute for 0049 course-level demand-to-plan analysis or for 0051/0052 deliberation and learner feedback evidence.

## Synthetic evidence boundary

All dates, role codes, class size, lesson timings, scenarios, questions, thresholds, work products, scores, and outcomes in this candidate are `SAMPLE / SYNTHETIC`. The 99-row replacement register identifies each fact, its location, basis, responsible role to confirm, and actual source needed for replacement. No item establishes the association's current policy, staff appointment, approval, actual class, attendance, teaching, student performance, or result. The example pre/post difference is arithmetic only and is not causal evidence.

Before any real use, authorized staff must replace the synthetic course objectives, role boundaries, procedures, teaching material, assessment key and thresholds with verified current sources, and review any personal-data and accessibility controls. No official signature or third-party source is simulated.

## Exact candidate and QA references

- DOCX: `candidate/0050_R01.docx`, SHA-256 above.
- Complete synthetic replacement register: `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`, 99 unique fact IDs; SHA-256 `556f69271e796e533d4afc2c19c1ddcfbb80e8554b40c527c87e5efec29a99b3`.
- Build metadata: `evidence/build/BUILD_METADATA_R01.json`.
- Technical and visual receipt: `evidence/qa/TECHNICAL_VISUAL_QA_R01.json`.
- Word-native PDF and all 18 page images: `evidence/render_R01_d0d37c2c/`.
- Independent exact-SHA semantic review: pending in `review/packet_R01/`; it must not grant Human acceptance or promote the candidate.
