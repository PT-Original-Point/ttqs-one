# SOURCE PACKET — 0134 / I19-E23 / R01

## Current source identity

- PR #92 head and branch commit observed: d9650e0df31b17f296994af5a65ec56930f40463.
- Internal doc_id: 0134. Current 142 crosswalk requirement: I19-E23. Printed official checkbox serial: UNKNOWN; do not infer it from either identifier.
- 157 project blueprint index 147: “會員/會費：實際帳冊與敏感資料隔離.” Any separate project-code field is UNKNOWN unless the active official map supplies it.
- Official requirement exact text, source PDF page 8: “會員人數及會費收入均逐年增加。” The PDF extraction breaks the last word across a line; whitespace-normalized extraction matches the sentence.
- Required genre: analysis/evaluation report specifically covering annual membership count and fee income, with real-ledger evidence separation.
- Negative neighbors: 0133 / I19-E22 is training classes and attendee person-times; 0135 / I19-E25 is target-market/customer-value outcomes. Neither may be folded into this report.

## Source-of-truth files

- source/official_source.pdf is an exact copy of the current branch PDF blob; page 8 extraction and page-only PDF are provided for quick verification.
- source/official_129_to_142_crosswalk.csv is the exact current crosswalk input. The 3-row neighbor excerpt is separately provided.
- source/UNIQUE_BLUEPRINT_0134_142_R04.json is the exact current 142 unique Blueprint row; the Markdown copy exposes every field without adopting a historical manuscript.
- source/PROJECT_157_BLUEPRINT_INDEX146_148_EXCERPT.md contains official project index 147 and adjacent rows.
- source/blueprint_seed_142.csv is the current 142 Blueprint seed input.

## Required next document conten

The report must distinguish member headcount from fee income; define the unit, period, opening/closing balance or annual recognition rule, membership-status inclusion/exclusion, income ledger basis, refunds/waivers/arrears, and comparable periods. It must provide a complete SAMPLE/SYNTHETIC multi-year dataset, independently recalculable sums and year-on-year rates, explicit zero/missing denominator handling, separate evidence strength for the two indicators, a member/fee reconciliation workflow, privacy and financial-record access controls, findings, limitations, recommendations, accountable role placeholders, follow-up measures, and a per-fact replacement register. No synthesized amount or headcount may be described as association performance.

## Prior artifact handling

Historical 0134 DOCX variants exist in archived repository folders. The current quality-review tree had no 0134 package at this source-prep stage. Historical body reuse is explicitly prohibited by the current unique Blueprint; old files are discovery-only and no semantic/layout PASS is inherited.

## Current stage state

SOURCE_PACKET_READY; UNIQUE_BLUEPRINT_CAPTURED; MANUSCRIPT_NOT_YET_BUILT; DOCX_NOT_YET_BUILT; independent review NOT_RUN. Next stage: construct a new 0134-specific complete SAMPLE/SYNTHETIC report from this packet and the unique Blueprint, then use the local Word builder and exact-SHA QA.
