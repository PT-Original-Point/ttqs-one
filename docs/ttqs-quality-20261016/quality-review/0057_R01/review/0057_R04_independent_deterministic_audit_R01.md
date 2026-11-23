# DOCX 0057 Blueprint R04 — independent deterministic audit

Snapshot: 2026-10-17 23:49:36 +08:00. Candidate SHA-256: `af88b80542585e85e2d25e8b2011b8f1770b6aa049b7f8de9e067ac8a9af4552`. Source R03 SHA-256: `8f3b404cad787975d06444603ca647702afc7f21df1d526d3ea2daeb800effb4` (unchanged).

## Verified checks

- 232 register rows, IDs 001–232 unique and contiguous; all rows have 10 cells.
- New IDs 204–232 are marked `SYNTHETIC`.
- The previously reviewed R03 arithmetic/date sections were retained; R04’s own build receipt records its deterministic recomputations.
- Required T8 repeated-value locators exist for IDs 115, 118, 121, 124, 127 and 130.
- The former atomicity findings are separated, including the six Figure 3 node values; UTF-8 readback confirms `SF-0057-201` is only node (1) and IDs 218–222 are nodes (2)–(6). An earlier terminal-decoding interpretation that this row still bundled all six nodes was false and is corrected here.
- R04 remains a Blueprint candidate only. No DOCX was created or accepted.

## Blocking defect found independently

T1’s two-column field/type schema does not describe the adjacent T1 example table consistently. The schema lists `資料截點` but omits `追蹤波次`; the example table includes `追蹤波次` but has no `資料截點` column. It also labels `主波次 T+90 最晚到期` vs `主波次最晚到期`, and `是否列入分母` vs `列入分母`. This is a real Writer ambiguity. It is not resolved by the valid `SF-0057-001` locator to the schema note.

**Minimum repair before semantic review:** make T1 schema names match the example table exactly; add `追蹤波次` to the schema; move the constant `2026-06-30` from a purported data-column definition into one explicit T1 table note (or add a registered column, if chosen); use the example’s exact `主波次最晚到期` and `列入分母` labels; update `SF-0057-001` locator to the actual T1 note. Preserve all cohort dates, values, calculations and R04 history; use a new R05 file and do not create/edit a DOCX.

## Status

`R04 = CANDIDATE / DETERMINISTIC_AUDIT_FAIL_REPAIRABLE`. Do not claim independent semantic PASS. R04 Writer self-reported 100 checks, but the independent schema comparison above failed. Exact-SHA semantic review is deferred until this defect is repaired.

Worker evidence: `opencode_v2_blueprint_repair_R04_stdout.jsonl`, stderr/exit files and `opencode_v2_blueprint_repair_R04_session_export.json`.