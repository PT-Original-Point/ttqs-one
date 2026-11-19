# Semantic/Usability Review — Candidate SHA-256 `6f846e1737ff0d9b8baf40f459071f9258d51c267935d95222a89e7a05804a63`

**VERDICT: PASS** — semantic/usability scope only.  
**Blocking findings: None.**

## Evidence

1. **Identity and genre — PASS.** §1 Table 1 rows 1–10; §2; §2.1 Table 2 rows 1–5; §2.2 Table 3 rows O-01–O-05. The document is an I18-E17 community knowledge discussion-board usage-frequency analysis report, mapped to doc_id 0109. It correctly distinguishes I18-E16/0108, I18-E15/0107, I18-E13/0105, I18-E08/0100–0101, and I18-E19. The verified I18-E08→0100/0101 crosswalk mapping appears in Table 2 row 4, Table 3 row O-05, Table 12 row 3, and Table 14 row O-05.

2. **Definitions and method — PASS.** §4.1 gives two 13-week Monday–Sunday windows in Asia/Taipei, each 91 days. §4.2 fixes the 8-person synthetic roster and 104 person-week denominator, retaining zero-activity members. §4.3 defines meaningful interaction, exclusions (login, browsing, likes, notifications, bots, tests, duplicates), active week, active member, deduplication, and boundary cases. Table 7 row 3 defines the sample sustained-use rule (≥6 active weeks/13). §5.1 gives formulas, numerators, denominators, and rounding.

3. **Replacement register — PASS.** Table 13 row 14 explicitly confirms the sustained-use result `0/8 = 0.0% → 5/8 = 62.5%, difference +62.5 percentage points`. Rows 12–20 cover active-member rate, active-person-week rate, sustained rate, interaction totals, per-member and per-person-week averages, distribution/median, and Figure 1. The table includes source, legal-basis, masking/custody, independent-recheck, and status columns. P01–P08 rows 3–10 match Table 6; “同上” references remain traceable to row 3.

4. **Prior R11 findings — all closed.**
   - Sustained-rate row: Table 13 row 14.
   - Per-row legal-basis field: Table 13 header and every row.
   - HOLD/REJECT boundaries: Table 5 rows 6–10; Table 14 X-05, X-06, X-07, R-04.
   - Undefined G6: removed; Table 10 T-06 now cites G4/G5.
   - Internal “Blueprint” jargon: absent; §3.1 design B cites §4.4 instead.
   - I18-E08 neighbor mapping: verified in Table 2 row 4 and O-05.
   - Code traceability: §4.4 maps P01–P08 to SYN-0109-P01–P08.
   - Conditional retention: §3.3 item 5 keeps retention/deletion UNKNOWN and unexecuted.
   - Official 3-point reference: Table 3 O-01, §6.1, and Table 15 treat it only as an example, not an earned score.

5. **SAMPLE/REAL boundary — PASS.** §1 Table 1 rows 6 and 10; §2; §4.2–§4.4; Table 13; Table 15 rows 4–7. No real platform, roster, approval, execution, third-party evidence, official score, or association decision is fabricated. REAL remains UNKNOWN/HOLD and formal acceptance remains NOT_GRANTED.

6. **Usability and HOLD/REJECT — PASS.** §3.2 G0–G5 gates; §3.3 review/publication steps; §7 Table 10 T-01–T-06; §8 Table 11 filled sample worksheet; §3.4 Table 5 and §9.2 Table 14 decision rules. The process is low-maintenance and usable for a small volunteer association.

## Math and cross-document checks

- `5/8 = 62.5%`; `7/8 = 87.5%`; difference `+25.0 pp`.
- `13/104 = 12.5%`; `47/104 = 45.2%`; difference `+32.7 pp`; active-week difference `47 − 13 = 34`.
- `0/8 = 0.0%`; `5/8 = 62.5%`; difference `+62.5 pp`.
- `18/5 = 3.60`; `67/7 = 9.57`; difference `+5.97`.
- `18/13 = 1.3846…`; `67/47 = 1.4255…`; unrounded difference `+0.0409…`, displayed `+0.04`; the `1.43 − 1.38 = 0.05` display artifact is correctly explained in §5.5.
- `18 → 67 = +49`; `67/18 = 3.72×`.
- Median active weeks: `4, 5, 6, 7, 8, 8, 9` → `7` (n=7).
- Distribution: baseline `3/5/0`; demonstration `1/2/5`.
- Per-person deltas reconcile to `+34` active weeks and `+49` interactions.
- Dates: `2026-03-30` to `2026-06-28` and `2026-06-29` to `2026-09-27` are each 91 inclusive days, Monday–Sunday.
- Cross-document identifiers are consistent: I18-E17 ↔ 0109; 157 index 118 is internal; official serial UNKNOWN; case ID SYN-0109-CASE-01.

## Nonblocking notes

- Table 1 row 7 and Table 12 O-01 omit the “3 分” wording found in Table 3 O-01; the exact official quote and example status are still present.
- The legal-basis column is present but repeats a generic “由本會有權者依 G2 確認…” clause for every row; item-specific legal bases remain appropriately UNKNOWN.
- Terminology varies slightly between “活躍人週” and “活躍成員週率.”
- Table 14 S-01 does not restate the 13-week duration; §4.1 and §4.4 supply it.
- O-05 is not labeled in Table 2 or Table 11, though the mapping is present and O-05 appears in Tables 3, 12, and 14.
- Table 11 is a filled summary worksheet rather than a blank event-level collection template; §4.3 and §5.4 provide the event definitions and note the absence of a per-event sample log.
- Figure 1 has a caption/description, but the actual chart rendering was not inspected.

## Scope

This was a TEXT_ONLY review of the extracted candidate text. I did not inspect DOCX binary/OOXML, Microsoft Word layout, actual Figure 1 pixels, or any visual rendering. **Visual review is outside my scope.** No tools were used and no files were edited.