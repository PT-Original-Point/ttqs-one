# SOURCE PACKET — DOCX 0104 / I18-E11

## Identity and exact source binding

- Project: TTQS_ONE
- Document ID: `0104` (not the official checkbox serial)
- Official requirement ID: `I18-E11`
- Official checkbox serial: `112`
- Unique Blueprint row: `deliverable_id=0104`, `requirement_id=I18-E11`, filename `0104__證照獲取率_分析報告.docx`
- Document genre: `分析／評估報告｜證照獲取率_分析報告`
- Official evidence table: printed page 7; exact official phrase: `證照獲取率。`
- Page context: `目標客戶及學員認為訓練有顯著具體績效。` The illustrative list includes `指導學員參加技能競賽獲獎。／感謝函。／證照獲取率。／其他。` The list is not proof that the association achieved the result.
- Official source PDF: `docs/ttqs-quality-20261016/quality-review/0039_R09/inputs/official_source.pdf`; SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; 9 PDF pages; the matching phrase occurs on PDF page 7. Page text and official page render are attached here.
- Current PR #92 branch HEAD at preparation: `0da7b7fec054f4fa96f61e493d21234488d4398b`.
- R09 contract blob: `docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` blob `4c7eff55748ff265b1e5a7d1122852b0d101acbd`.
- Current official/quality manual blob: `docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md` blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`; checkbox 112 explicitly requires source, core demonstration, decision/result, denominators/source handling, and cross-document factual linkage.
- The exact local `BLUEPRINT_CURRENT.jsonl` row and crosswalk source row are retained under `source/`; parent-file hashes and row hashes are in `evidence/source_stage_receipt_0104_R01.json`.

## Required evidence meaning

Produce a usable **analysis report**, not a certificate, exam result, survey, thank-you letter, or generic course report. The current association's candidate counts, exam counts, certificate issuance, and performance are all `UNKNOWN` because no authenticated association data was supplied. Do not convert unknown to zero.

Keep these populations and rates distinct:

1. eligible trainees in the defined cohort;
2. exam applicants/registered examinees;
3. actual examinees;
4. people who passed;
5. people with an issued certificate whose issuance was actually verified.

Define and report separately: application rate = applicants / eligible trainees; attendance rate = actual examinees / applicants; pass rate = passed / actual examinees; verified certificate acquisition rate = people with verified certificate issuance / eligible trainees. If a separately named pass yield is shown, use passed / eligible trainees and do not relabel it as certificate acquisition. Show non-applicants, no-shows, failed, uncontactable, pending issuance, missing evidence, and unverifiable certificates separately. A zero denominator is `N/A`, never `0%`.

## Complete SAMPLE/SYNTHETIC worked example

Use at least two comparable cohorts/periods with stable synthetic IDs and a common cutoff rule. Provide row-level aggregate counts (no participant names or real certificate numbers), a field dictionary, source-lineage example, full step-by-step calculations, cohort comparison, trend interpretation, evidence-strength grade, limitations, conservative conclusion, and executable sample follow-up actions with SAMPLE roles and dates. Reconcile every total. Register every synthetic date, role, course/cohort label, count, rate, cutoff, source, provider/exam illustration, finding, and decision by fact key and document locator.

All sample decision thresholds must say `SAMPLE—待協會核定`. State that the example is not association performance and cannot support a real TTQS rating.

The REAL replacement checklist must identify consented/access-controlled eligible roster, cohort eligibility decision, official exam enrollment/attendance source, result notice, certificate issue/verification source, reconciliation and exception logs, privacy authority, period/cutoff, exact numerator/denominator, and independent verifier. No real authority, provider action, examination, candidate, pass, certificate, approval, signature, association statistic, or causal result may be invented.

## Negative-neighbor boundaries

- `0103 / I18-E10`: third-party thank-you-letter authenticity/custody workflow; not a certificate-rate analysis.
- `0105 / I18-E13`: learning-needs/survey and training-effect outcome; satisfaction or perceived effect cannot substitute for verified certificate acquisition.
- `0102 / I18-E09`: competency-gap analysis; no cross-document cohort claim is authorized absent identical cohort IDs, dates, population, denominator, and source definition.

No historical DOCX body is authorized as a writing template. Historical files are discovery evidence only. Write from the attached official source, exact crosswalk, and unique Blueprint plus the boundaries in this packet.