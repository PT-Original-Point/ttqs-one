# DOCX 0057 — status after independent R04 deterministic audit

Snapshot: 2026-10-17 23:49:59 +08:00. Candidate Blueprint R04 exact SHA-256: `af88b80542585e85e2d25e8b2011b8f1770b6aa049b7f8de9e067ac8a9af4552`. R03 source SHA is unchanged. R04 is a Builder candidate and is not independently accepted.

Independent checks confirm 232 unique sequential `fact_id` rows, 10 cells per row, new rows 204–232 marked `SYNTHETIC`, required T8 locators present, and the formerly flagged atomic-register rows split. The apparent SF-201 bundling reported during an initial terminal read was a decoding misread; UTF-8 direct read confirms one graph node per row, so no repair is needed there.

The one confirmed blocking defect is T1 schema/example mismatch: T1 schema has `資料截點` but omits `追蹤波次`; the example has `追蹤波次` but no `資料截點`; two additional header names also differ. Exact details and minimum repair are in `review/0057_R04_independent_deterministic_audit_R01.md`.

A bounded new repair has been prepared, preserving R04:
- Patch: `inputs/0057_BLUEPRINT_REPAIR_PATCH_R05.md`
- Patch SHA-256: `11ca22101745f25fae15de5359b34605b8aebb6c617ae9661cf24b510df384be`
- Next: OpenCode v2 Writer creates R05 only; then independent exact-SHA review.

No DOCX exists yet. No association fact, approval, or formal acceptance is claimed.