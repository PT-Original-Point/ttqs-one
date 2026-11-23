from pathlib import Path
import hashlib
pkg=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022')
md=pkg/'writer/opencode_writer_manuscript_0104_R15_patched.md'
review=pkg/'review/R15/opencode_review_final_R15.md'
source=(pkg/'source/SOURCE_PACKET_0104_I18-E11_R01.md').read_text(encoding='utf-8-sig')
blue=(pkg/'source/UNIQUE_BLUEPRINT_0104_I18-E11_R01.jsonl').read_text(encoding='utf-8-sig')
text='''# Bounded Writer Task — DOCX 0104 / I18-E11 / R15 → R16

work_id: TTQS-0104-I18-E11-R16-BOUNDED-REPAIR-20261022
project: TTQS_ONE
input_candidate_sha256: 9bbb96da74ba9da845ab0e063421d04f035e79496209a02de1f04b0c98ec7eb8
input_manuscript_sha256: '''+hashlib.sha256(md.read_bytes()).hexdigest()+'''
independent_review_sha256: '''+hashlib.sha256(review.read_bytes()).hexdigest()+'''
source_packet_sha256: '''+hashlib.sha256((pkg/'source/SOURCE_PACKET_0104_I18-E11_R01.md').read_bytes()).hexdigest()+'''
unique_blueprint_sha256: '''+hashlib.sha256((pkg/'source/UNIQUE_BLUEPRINT_0104_I18-E11_R01.jsonl').read_bytes()).hexdigest()+'''

## Assignment

Return a minimal, directly applicable patch plan for the current R15 Markdown source appended below. Do not rewrite the report. Do not edit files, call tools, or build a DOCX. Return one JSON object only, no code fences, following the output schema below. Use exact source text/anchors and exact replacements; each replacement must match once. For the T-13 table, replace its complete data block and add its sort rule. For fact-register changes, provide exact Markdown rows and insertion anchors. Do not leave any finding unaddressed or broaden the change beyond these ten reviewed findings.

## Evidence identity and governing boundaries

DOCX 0104 is the analysis report for official requirement I18-E11, checkbox 112, official page 7, exact phrase 「證照獲取率。」. Its genre is certificate-acquisition-rate analysis, not a certificate, exam result, survey, thank-you letter, or generic course report. The unique Blueprint is included below and is authoritative for this document's scope. All R15 demonstration values, thresholds, roles, sources, dates, cohorts, decisions, and outcomes are SAMPLE/SYNTHETIC. REAL association data and acceptance remain UNKNOWN. Do not invent real results, participants, third-party originals, approval, signature, or causal claims. Do not change any numerator, denominator, rate, threshold, date, cohort, sample status, or substantive conclusion. Do not make any claim about I18-E12; its source is absent and the reviewer explicitly marked the comparison UNKNOWN. Keep the current replacement register facts stable and auditable.

## Exact-SHA independent review result

Verdict PARTIAL, zero blocking defects; all five prior blockers were verified fixed and arithmetic was independently recomputed correct. Text-only review did not inspect visual layout. The ten residual findings are:

- RF-1: §12 T-13 duplicate priority labels 1,1,2,3,3; table order is not descending shortfall; no tie rule; F-GP-02 says row 2 but its actual rank label is 1. Sort the three below-threshold deficits by descending shortfall magnitude: verified certificate acquisition −12.50 pp, application −5.00 pp, issuance verification −3.64 pp. Show the two above-threshold margins separately/after deficits, with smaller positive margin first, and use unique row/rank locators. State the sorting/tie rule. Update all F-GP locator text to match final table row numbers.
- RF-2: §11.1 A-7 and §11.2 B-7 are distinct multiplication-chain calculations but only duplicate F-RA-05/F-RB-05 currently carry the resulting rates. Add unique SAMPLE keys F-CHAIN-A and F-CHAIN-B, with precise locators, expressions/results, replacement basis and responsible role.
- RF-3: §23 sample retention recommendation 「示例建議 3 年」 lacks a fact key. Add F-RET-01 with SAMPLE value, §23 locator, replacement source/authority and responsible role.
- RF-4: T-12 A/B judgment cells are not all traceable. For each five fixed indicators, annotate both cohort judgment cells with the relevant existing cohort rate fact key plus the relevant F-RT-01…05 sample-threshold key. The optional pass-output row must be marked reference-only/no threshold and cite F-RA-06/F-RB-06. Keep the current judgment values unchanged.
- RF-5: §15 FN-2 evidence 「T-12」 is wrong for the 8 non-applicants; cite T-10/P8 (and §11.1/A-1 for the sample rate if useful).
- RF-6: §17 T-17 R-1 evidence position incorrectly includes T-11; use §2.1 for the exact official text and §11.1/A-5, §11.2/B-5, T-10/P5 for worked proof. Do not use the cohort/date table as evidence of the requirement.
- RF-7: §26 modification rule currently lists only T-10, T-14 and T-19. Expand to all dependent destinations for changed source/count/rate/cutoff/decision values, including where applicable §11.1–§11.3, T-12, T-13, §13 narrative, T-14, T-15/T-16, T-18/T-19, §19 replacement register, and §24 navigation; instruct re-compute rather than manually copy rates.
- RF-8: §25.1 item 4 「3 件」 is not scoped. Clarify it means A期 2件待簽發 + 1件查證未通過; B期 separately has 2件（1待簽發+1查證未通過）. Keep all numbers intact and align any matching conclusion text.
- RF-9: SRC-C1 label conflicts: §10 calls it an unformed-cohort control record (not a learner list or registration list), while F-SR-07 says registration statistics. Standardize source type to the former; describe 0 only as a SAMPLE synthetic control count, not an association or registration-system record. Update all occurrences consistently.
- RF-10: opening 「5 個比率（另加簽發查證完成率）」 is ambiguous because pass-output yield is optional. Name the five fixed ratios explicitly (application P2/P1, attendance P3/P2, pass P4/P3, verified certificate acquisition P5/P1, issuance-verification completion P5/P4); list pass-output yield P4/P1 separately as optional and not part of those five.

## Required output JSON schema

{
  "work_id": "TTQS-0104-I18-E11-R16-BOUNDED-REPAIR-20261022",
  "input_candidate_sha256": "...",
  "patches": [
    {"finding":"RF-1", "target":"...", "find_exactly":"...", "replace_with":"...", "expected_matches":1},
    {"finding":"RF-2", "target":"...", "insert_after_exactly":"...", "insert_rows":["| F-CHAIN-A | ... | S |"], "expected_matches":1}
  ],
  "checks": {"changed_math":false,"changed_real_claims":false,"introduced_i18_e12_claim":false,"addressed_findings":["RF-1",..."RF-10"]},
  "notes": "..."
}

For T-12 judgment cells, exact table row replacements may be returned as complete Markdown rows. For the three new fact-register entries, provide valid seven-column rows matching the existing §19.4 replacement register schema and insert them at a precise anchor. Keep fixes minimal; no editorial rewrite outside these anchors. Do not output the entire manuscript.

## Current unique Blueprint row

'''+blue+'''

## Official source packet

'''+source+'''

## Current exact manuscript source (R15)

<<<BEGIN_R15_MANUSCRIPT>>>
'''+md.read_text(encoding='utf-8-sig')+'''
<<<END_R15_MANUSCRIPT>>>
'''
out=pkg/'writer/TASK_PACKET_0104_R16_BOUNDED_REPAIR.md'
out.write_text(text,encoding='utf-8')
print('task_packet_bytes',out.stat().st_size,'sha256',hashlib.sha256(out.read_bytes()).hexdigest(),'manuscript_bytes',md.stat().st_size)
