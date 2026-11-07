# 0057 R03 precise patch task

Scope: modify only the already existing `inputs/0057_UNIQUE_BLUEPRINT_R03.md`, baseline SHA-256 `3d5e778b384e53e7b51cffadaf56a67f2e381807a6b16bbf334fe0fe81667d10`. Preserve `0057_UNIQUE_BLUEPRINT_R02.md` byte-for-byte at that SHA. No DOCX. Do not inspect or edit unrelated files. Avoid full-file reads; use targeted grep/read spans for the sections below and targeted edits.

## Fix four proven defects

### 1. T+90 endpoint rules
Align §§5.2–5.6, T2/T4/T6/T7/T10, §§8.1–8.3, charts/findings/decisions/checklists:
- Call T+90 the primary outcome endpoint.
- D counts a person with a T+90 questionnaire response OR qualifying non-self evidence dated by T+90.
- E counts one person with application by the T+90 endpoint: the defined T+90 self-report threshold OR qualifying Tier-A/B evidence dated by T+90.
- G is E with Tier-A/B non-self evidence dated by T+90.
- Tier-B observation at T+60 or T+90 qualifies; a T+60 questionnaire response alone does not. T+30/T+60/T+180 questionnaire responses remain descriptive and never determine D/E/G. State this distinction plainly.
- Count each person once; preserve aggregates only if consistent; otherwise recompute every affected table/rate/chart/finding/decision/register item. T7/T12 T+60 observation may support application by T+90.

### 2. Q2 maturity boundary
Keep cutoff `2026-06-30`, P3-Q2 window `2026-04-01–2026-06-30`, and synthetic `A=14` only if you add the explicit sample assumption: those 14 completions fall within `2026-04-02–2026-06-30` (zero completed on 4/1), so earliest T+90 is `2026-07-01`; all 14 are not yet due and excluded from every rate. Update T1/T2/§5.1/§8.3/§10/§13/§15–19 references and register. Do not assert all Q2 records are not due without this fact.

### 3. T9 status
Add the status field to every row in the populated T9 table and fill all five rows `預擬／未核定`, consistent with §11 and proposed owners.

### 4. Atomic synthetic replacement register
In §13.2 replace broad grouped multi-cohort rows with exact row/cell locators and one unique fact identifier per displayed value. Individually enumerate every P1/P2/P3 A–G count and six rates; every T4/T5/T6 cohort value; every T1 date/status; Q2 A/date-range assumption; T3/T10 score thresholds/outcomes; each chart value; each decision threshold/outcome; T7/T12 dates/scores/observations; every T9 date/target. For repeated facts, include all exact locators or separate rows. No broad locator such as “T2 欄 A”. Keep engineering IDs only in sidecar Blueprint, never in future Human Word body.

## Version labels and verification
Update title, R01→R02 change-summary references and terminal marker so this file is clearly R03 and lists the four R03 fixes. Do not change R02. Verify all rate math, date arithmetic, `G⊆E⊆D⊆C⊆A`, `F⊆B⊆A`, T4 exclusivity, T5/T6 sums and P3-only decision thresholds. Return accurate byte count, line count, exact SHA, touched sections and unresolved gaps. No self-claim of independent PASS.