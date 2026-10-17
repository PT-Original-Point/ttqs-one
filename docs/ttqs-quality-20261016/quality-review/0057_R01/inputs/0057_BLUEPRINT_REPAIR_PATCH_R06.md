# DOCX 0057 — Blueprint R06 bounded precision and provenance repair

## Input lock

- Source candidate: `0057_UNIQUE_BLUEPRINT_R05.md`
- Required source SHA-256: `efdfcfa52a4b7338ae7688e118f6b700cf1e6f4ee3ef423aa89ac3f253bc3f95`
- Independent exact-SHA semantic review: `../review/0057_R05_semantic_review_GLM_R01.md` (PASS, with two non-blocking precision/version findings)
- Preserve R01–R05 byte-for-byte. Create only `0057_UNIQUE_BLUEPRINT_R06.md` and its concise build receipt. Do not create or alter any DOCX.
- If the R05 source hash does not match, stop without writing and report the observed hash.

## Required bounded changes

1. **Current revision labels:** Set the document title revision to R06, add a concise current `R06 修訂性質（bounded repair）` note describing only the changes in this patch, update §0's revision summary so R06 is current and R05/R04 are historical, and change the closing marker to `Blueprint R06 結束`. Preserve prior R04/R05 history and accurate labels such as `R04 欄名一致化` and `本 R04 已逐值原子化`; do not rewrite history.
2. **Record R05 history:** Add a concise `R05 修訂性質（歷史）` note describing the already completed T1 schema/example alignment, the single shared `2026-06-30` cutoff note, and the `SF-0057-001` locator correction. Do not change any T1 content or fact.
3. **Clarify the date rationale without changing dates:** In §12.2 and the `SF-0057-191` rationale, replace `訓練後 30 天內首次應用` with `訓練後 1 個月內首次應用`. Preserve `T0=2025-03-15`, first application `2025-04-15`, all other dates, calculations, conclusions, and register values. The wording should describe the one-calendar-month interval, not assert an elapsed-day count.

## Strict preservation

- No new synthetic facts, IDs, tables, calculations, dates, claims, or association decisions.
- Keep 0057 / I13-E01 / official checkbox 061 distinct; keep 062/063 boundaries and SAMPLE/SYNTHETIC vs REAL declarations unchanged.
- Do not modify substantive analysis, any other register row, cohort/rate/date math, or R04/R05 history beyond the exact revision/provenance notes requested above.

## Required build receipt and checks

- Re-hash R05 before and after writing; verify R01–R05 are unchanged.
- Report R06 exact SHA-256, the exact changed sections/lines, and a no-other-change diff audit against R05.
- Verify title, current revision note, §0 summary, and closing marker identify R06; R05 T1 repair is explicitly recorded as historical.
- Verify both date-rationale locations use the new one-month wording, while the two displayed dates remain exactly `2025-03-15` and `2025-04-15` and all register IDs remain unique/contiguous 001–232.
- State clearly that this is a bounded Blueprint candidate repair, not DOCX production, formal acceptance, or association approval.
