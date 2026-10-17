# DOCX 0057 — Blueprint R04 bounded repair brief

## Authority and input lock

Repair only the current Blueprint sidecar, not a DOCX. Source candidate: `inputs/0057_UNIQUE_BLUEPRINT_R03.md`, SHA-256 `8f3b404cad787975d06444603ca647702afc7f21df1d526d3ea2daeb800effb4`. Preserve R01–R03 byte-for-byte. Write a new `inputs/0057_UNIQUE_BLUEPRINT_R04.md`. This is a reversible sidecar repair; it does not establish DOCX readiness or formal acceptance.

Use the independent OpenCode GLM R03 exact-SHA review receipt `review/0057_R03_semantic_review_GLM_R01.md` as the defect list. Preserve the synthetic case, arithmetic, dates, narrative, decision logic, proposal status, and sample/real boundaries. Do not invent association facts. Do not create or edit any DOCX. Do not alter official requirements or Blueprint identity.

## Required bounded repairs

1. **Atomic value register (§13.2):** retain unique IDs and exact locators; make each row contain one independently displayed synthetic fact. For existing rows `SF-0057-184`, `186`, `188`, `191`, `192`, `194`, `195`, `198`, `199`, and `201`, keep the original ID for the first atomic fact and allocate fresh sequential IDs beginning after the current maximum for additional facts. Update every affected repeated display locator. Specifically separate Q1/Q2/Q3 answers; R1/R2/R3/R4 scores and the total; record count and referral-boundary flag; each date; each competency; time-limit and monthly frequency; each support mechanism; each barrier including the 18-field count; each evidence set; and each of the six flowchart node texts. One row must never bundle different questionnaire answers, rubric item scores, dates, evidence sets, barrier facts, competencies, supports, or node texts.
2. **T8 locators:** add the exact T8 cell locators to `SF-0057-115`, `118`, `121`, `124`, `127`, and `130`, where the same values are repeated from T5. Do not change the values.
3. **T9 coverage:** add one registered fact per each of the five distinct F1–F5 action texts in T9; add four missing fact rows for the F1/F2/F4/F5 re-tracking indicators (retain the existing F3 coverage); and register the `2027 上半年重檢` date in §11. Give every row a unique ID and exact one-value locator.
4. **SF-0057-001 locator:** resolve the reviewer’s nonexistent T1 data-cell locator. Point only to exact displayed occurrences that actually contain `2026-06-30`, or add a real T1 column only if it can be done without creating unregistered repeated values. Prefer the smallest schema-preserving locator correction.
5. **Schema/table consistency:** reconcile the §13.1 T3 field schema with the actual T3 example table. Every listed field must be present in the table or removed from the schema with a clear reason; use one canonical column name for each data field. Reconcile T8 schema/example column names too. Do not change computed data values.

## Invariants to recheck before reporting

- R04 SHA is computed only after all writes complete.
- Old R03 SHA remains unchanged.
- `fact_id` uniqueness, one-value-per-row, exact locators, and full displayed synthetic fact coverage.
- T2/T4/T5/T6 calculations, cohort nesting, all decision inputs and T+90/T+180 arithmetic remain unchanged and still correct.
- All newly added synthetic facts are explicitly `SYNTHETIC`; all actual association records/decisions remain `UNKNOWN/PENDING_REAL_SOURCE`.
- 0057 = I13-E01 = official checkbox 061 remains clear and distinct from 062/063.
- Output a concise patch receipt listing old/new SHA, each repair group, newly allocated IDs, deterministic checks run and any unresolved issue. Do not claim independent PASS.

If the source candidate SHA differs, stop without writing and report the observed SHA. Do not enumerate unrelated deliverables.