# 0105 / I18-E13 來源包 R01

## 文件身分與範圍

- 專案：TTQS_ONE；文件 ID：`0105`；R04 142 文件 crosswalk 對應官方要求識別碼 `I18-E13`。
- R04 crosswalk row maps `0105` to `問卷調查及課後行動計畫評估表等顯示目標客戶及_可直接使用成品`；官方序列原始文件對照為 page 7、I18-L3 project index 114。
- Index 114 is a project blueprint index. It is not a printed official checkbox ordinal. No printed serial is claimed here.
- Document genre: ready-to-use survey instrument plus post-training action-plan and follow-up evaluation forms, with a worked synthetic data example and transparent descriptive calculation.
- Official evidence table PDF page 7 states under the 3-point common evidence examples: `問卷調查及課後行動計畫評估表等顯示目標客戶及學員認為訓練有績效改善的效果。` It is an example of supporting evidence, not proof of association achievement or a guaranteed score.

## Source of truth and exact source identifiers

- Live GitHub PR #92 / branch `work/ttqs-one-document-quality-contract-20261016` at source capture: commit `95d7c2e856f70cfb883d186aee1c87d1c2720370`.
- Current 06 contract blob: `4c7eff55748ff265b1e5a7d1122852b0d101acbd`; R09 and the project authorization are applied from this live contract.
- Current `01_HUMAN_MISSION_AND_ACCEPTANCE.md` blob: `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`.
- Current `02_GENRE_WRITING_MANUAL.md` blob: `4ff863d9f534b6359fc1c7c1685bd8cce02da886`.
- Current `03_157_CHECKBOX_BLUEPRINTS.md` blob: `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` (project index 114: performance-improvement survey and action-plan follow-up; index 113 is a distinct `Other` row and is not being used as the authority for this named document).
- R04 129-to-142 crosswalk source blob: `1ac4a8419088d947947031b758e29c35a3606514`; seed-142 source blob: `f20ac9ae37700eb03a93b8da4407e7bf4788b602`.
- Crosswalk row excerpt and seed-142 row excerpt are included beside this packet.
- Official evidence-table PDF: `quality-review/0039_R09/inputs/official_source.pdf`, SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; page 7 excerpt SHA-256 `78a60101bc37d688670a27d0f115f78abde6385391947459cbbb51343b5ad9eb`; corresponding page image SHA-256 `cd6abab433007af144da97f54c946b3be85d90977b5140c74fec3a428ab7f180`.

## Target association facts and limits

- The project target is 屏東縣原始點關懷協會. Current legal status, actual courses, staff, target customers, learners, survey responses, action-plan execution, and organizational performance are not established by this source packet.
- No real survey data, course roster, respondent consent, follow-up records, approval, or objective performance evidence is included. The deliverable must not report association performance as REAL.
- Use fully completed, visibly `SAMPLE / SYNTHETIC` material so the forms can be understood. Never invent a real respondent, course date, signature, decision, external approval, association result, or verified organizational outcome.

## Neighbor boundaries

- `0104 / I18-E11` is a certificate-acquisition-rate analysis; this document is about perceived performance improvement and post-course action-plan follow-up. A learner satisfaction result cannot count as an issued certificate.
- `0106 / I18-E14` is a financial performance-improvement explanation; do not turn synthetic survey responses into financial statements or objective financial outcomes.
- `0110 / I18-E19` addresses stronger 4-point organizational-performance improvement/significant-effect evidence; this document's 3-point common-evidence example does not prove that higher standard.
- `0095 / I18-E02` is a system/process satisfaction survey mechanism; the present deliverable must include a specific performance-improvement instrument and post-course action-plan evaluation, not merely a generic satisfaction SOP.
- No cross-document cohort join is authorized without the same source-backed cohort ID, dates, population, denominator, consent and matching evidence definitions.

## Required claim boundary

Distinguish, field by field: (1) a respondent's perception, (2) a planned action, (3) a self-reported follow-up, (4) an objective source-verified indicator, and (5) a causal conclusion. The sample may demonstrate an apparent descriptive change, but it must label every such value `SAMPLE / SYNTHETIC`; no causal attribution is permitted without a suitable design and corroborating sources. If source evidence is absent, mark `UNKNOWN`, `NOT_RECEIVED`, or `HOLD`, not REAL or PASS.