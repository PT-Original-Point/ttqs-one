# OpenCode v2 Writer task — 0104 / I18-E11 / R01

Use only the supplied source packet, exact unique Blueprint row, exact crosswalk row, and official page-7 extract/render. Return one complete Traditional-Chinese evaluator-facing analysis report as Markdown. Do not create/edit files, run tools, browse, use Computer Use, copy any historical DOCX body, or return only an outline.

The complete report must include:
- Title-blind identification as `證照獲取率_分析報告`; first-page-equivalent plain-language summary of purpose, reader, use time, population, cutoff, outputs, and SAMPLE/REAL state.
- Scope, source hierarchy, cohort inclusion/exclusion, field definitions, privacy/reconciliation controls, complete current-real-state UNKNOWN panel.
- Separate eligible trainees, applicants/registrants, actual examinees, passed, and issued-and-verified certificate holders. Define and calculate application rate, attendance rate, pass rate, verified certificate acquisition rate, and optional pass yield only under distinct labels. Include zero-denominator N/A, unknown/missing, non-applicant, no-show, failed, late/pending issuance, and unverified evidence handling.
- At least two fully populated comparable SAMPLE/SYNTHETIC cohorts with stable IDs and common cutoff, all counts, stepwise arithmetic, comparison, trend interpretation, evidence-strength grading, limits, and conservative decisions. Reconcile every count and rate. No names or genuine certificate IDs.
- A source-field dictionary, row-level aggregate evidence, calculation table, cohort comparison, management decision/follow-up owner/deadline, official requirement trace table, exception/hold/rejection matrix, and fact-level synthetic replacement register. Each invented date, role, cohort, course, count, rate, source, exam/provider illustration, decision, and result has a fact key and exact section/table locator.
- Thresholds marked `SAMPLE—待協會核定`; not association policy.
- Hold gates: denominator cannot be reconstructed; cohort eligibility disputed; duplicate identity; source/version mismatch; exam/result mismatch; no verified certificate issuance; privacy/consent issue; stale cutoff; zero denominator; or unmatched records. Gate only the affected metric and never hide the exception.
- Negative-neighbor rejection for 0103/I18-E10 and 0105/I18-E13. Do not link 0102/I18-E09 absent identical cohort/date/denominator/source evidence.
- A practical operating procedure, replacement-source checklist, retention/privacy controls, evidence locator, conclusion, release criteria, and limitations.
- Never infer skill, job performance, training causality, satisfaction, official recognition, or association performance from the synthetic example. Do not fabricate any third-party document or association decision.

Return the complete body only, then a compact worker note with CLI-reported model/session metadata if present. Requested route is OpenCode v2 free `opencode/deepseek-v4.1-flash-free`; do not switch/fallback to another model.