# DOCX 0057 — Blueprint R05 minimal T1 schema repair

## Input lock

- Source: `0057_UNIQUE_BLUEPRINT_R04.md`
- Required source SHA-256: `af88b80542585e85e2d25e8b2011b8f1770b6aa049b7f8de9e067ac8a9af4552`
- Independent local audit: `../review/0057_R04_independent_deterministic_audit_R01.md`
- Preserve R01–R04 byte-for-byte. Write a new `0057_UNIQUE_BLUEPRINT_R05.md` and a concise build receipt. Do not edit or create a DOCX.

## Only required repair

Align the T1 two-column field/type schema with the T1 example table. The schema fields, in order, must correspond exactly to the example table header names:

`period_id` / `完成窗起` / `完成窗迄` / `期類型` / `追蹤波次` / `主波次最晚到期` / `T+90 狀態` / `T+180 狀態` / `列入分母`

Specifically:

1. Remove `資料截點` from the list of table columns; the table does not have that column.
2. Add `追蹤波次` as a column definition with its existing displayed values `30/60/90/180`.
3. Match the exact example labels `主波次最晚到期` and `列入分母`.
4. Add one concise T1 table note stating the shared data cutoff is `2026-06-30`. Keep the value as the existing synthetic fact; do not add a new column or duplicate new synthetic values.
5. Update `SF-0057-001` to locate the actual T1 note (not a schema row), retaining all valid §5.1/§8.3 locators where the same value is displayed.

Do not change any cohort windows, dates, maturity classifications, rates, arithmetic, narrative or other register rows. Do not alter the already repaired atomic rows or T2/T3/T8/T9 content. Keep `0057` / `I13-E01` / checkbox `061` distinct, and preserve SAMPLE/SYNTHETIC and REAL boundaries.

## Verify and report

- Confirm the source SHA before any write and hash R04 again afterward; R04 must remain unchanged.
- Parse the T1 schema field names and T1 example header and report `EXACT_MATCH` only if their ordered names are identical.
- Confirm the T1 note displays `2026-06-30` and `SF-0057-001` points to that note.
- Confirm register IDs remain unique/contiguous 001–232, no ID was added or removed, and all other R04 content is unchanged apart from the T1 schema/note and SF-001 locator.
- Output the R05 exact SHA, build receipt, scope, checks and unresolved issues. This is a bounded candidate repair, not independent PASS or formal acceptance.
- If the input SHA differs, stop without writing and report the observed SHA.