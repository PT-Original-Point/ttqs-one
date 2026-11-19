I located and independently verified the artifact, read its OOXML package directly, and recomputed every displayed figure. No files were modified; no synthetic fact is treated as real.

## Binding

| Item | Value |
|---|---|
| Artifact | `...\quality-review\0048_R01\candidate\0048_R01.docx` |
| Recomputed SHA-256 | `e6bb07cc8f984a8d6d72a64f4498717df6a5116d98431bee75c2f1e2151d28e9` |
| Reported SHA-256 | `e6bb07cc8f984a8d6d72a64f4498717df6a5116d98431bee75c2f1e2151d28e9` — MATCH |
| Bytes | 58,156 — MATCH |
| Package | 27 tables, 39 register rows (SYN-048-001…039, no gaps), only `Title` pStyle, body text ≥10.5 pt (`w:sz 21`), table text ≥9.5 pt (`w:sz 19`); the two sub-threshold style defs (BodyText3 8 pt, Caption 9 pt) are **not used** anywhere in `document.xml` |

Verdict is bound to the exact SHA above only.

## Verdict: PARTIAL — formal acceptance NOT GRANTED

All enumerated semantic criteria pass; one packet-required **table schema** is only partly implemented (details below). No correctness, authenticity, boundary, or arithmetic failure was found.

## Criterion-by-criterion

| Criterion | Result | Locator |
|---|---|---|
| Requirement fit (procurement **and** post-selection instructor review + records) | PASS | §1 quote = official text verbatim; §5–6 procurement; §7–8 instructor review |
| Correct genre (專屬佐證紀錄 / evidence_record) | PASS | Title, Table 1 (文類／用途) |
| Direct usability (reusable forms + filled examples) | PASS | §3–§4 Tables 7–11 (blank), §5–§8 Tables 12–21 (filled) |
| Completeness of both records | PASS | §5–6 (authority, quorum, agenda, options, discussion, votes, conditions, follow-up); §7–8 (pre-set criteria, weights, raw scores, decision, conditions, follow-up) |
| Decision authority & evidence boundaries | PASS | §1 "不得自行填造規則"; Table 12 "REAL 權限 UNKNOWN"; §5/§7 disclaimers; Table 24 |
| SAMPLE/SYNTHETIC discipline | PASS | banner + §5/§7 case labels + Appendix A (39 rows) + footer |
| Math (all recomputed) | PASS | see below |
| Cross-document separation | PASS | §10 + Table 25 |
| Return / hold conditions | PASS | Table 23; §6 conditions; Table 22 |
| Title-blind purpose | PASS | §10 statement; content is mechanism-specific |
| Administrator/evaluator usability | PASS | Table 2 step guide; §3–§4 fillable |
| Packet `required_tables_or_figures` schema | **PARTIAL** | §2 / Table 5 |

## Recomputed arithmetic (independently, all correct)

- §6 / Table 15: `120,000 − 113,000 = 7,000` ✓; `113,000 ÷ 120,000 = 0.941666… → 94.1666…% → 94.2%` (1 dp) ✓; `10 ÷ 10 = 100%` ✓
- §8 / Table 19: weights `35+25+15+15+10 = 100` ✓; Candidate X `35+20+12+12+10 = 89` ✓; Candidate Y `28+20+15+9+8 = 80` ✓
- §9: `8 ÷ 10 = 80%` ✓; case A `10/10 = 100%` ✓; case B `9/9 = 100%` ✓

No displayed result disagrees with its inputs.

## Adjacency separation (confirmed, not conflated)

The candidate correctly keeps four distinct identifiers apart: **DOCX 0048** = **I10-E03** = **official checkbox 049** = **P03-B10** (Table 1; Table 25 line 390; header `TTQS ONE｜DOCX 0048｜I10-E03｜官方方框 049`). Adjacent items are kept separate and correctly labeled: **DOCX 0045 = I10-E01** (SOP), **DOCX 0047 = I10-E02** (historical review), **DOCX 0049 = I11-E01** (course plan) — Table 25. DOCX 0049 is *not* merged with official checkbox 049. Official text is quoted unaltered.

## Findings

**F1 — PARTIAL (the one repairable content gap).** §2 / Table 5 implements only three columns (`欄位 | 填寫內容 | 驗證規則／來源`), whereas the packet's `required_tables_or_figures` specifies `欄位—定義—來源—填寫者—驗證規則`. There is no explicit **填寫者／責任角色** column. The information exists elsewhere in the document (Table 8 `決議權限依據`, Table 11 `來源形成者`, Tables 16/20 `責任角色`, Table 26 `責任`), so usability is only mildly reduced — but the specified schema is not delivered as required.
*Precise repair:* in §2, add one column `填寫者／責任角色` to the field table (page 2–3 of the 16-page render), populating each of the 8 rows; no other change needed.

Secondary observation (same family, optional): the required triple table "官方要求—表單欄位—附件定位追溯表" is delivered across Tables 3 + 4 + 25 rather than as one explicit requirement→field→attachment-location table. This is an approximation, not a contradiction.

**Non-material (explicitly NOT rebuild triggers):**
- `docProps/core.xml` has `created` = `modified` = `2013-12-23T23:15:00Z`, and `docProps/app.xml` shows `Normal.dotm` / `Microsoft Macintosh Word` — stale template metadata only.
- §9's illustration uses a generic `8÷10 = 80%` while both actual cases are 100%; this is a labelled illustration, not an inconsistency.
- Terminology: body uses "師資遴選" in places where the official requirement (page 3, P03-B10) says "師資遴聘" (e.g., §7 heading, Table 1 文類／用途). §1 quotes the official wording verbatim, so the requirement text is not rewritten; a parenthetical synonym note would remove any drift. Non-blocking.

## Bounded conclusion

- **Semantic verdict: PARTIAL** (one packet-required table schema not fully implemented; single precise repair F1).
- **Formal acceptance: NOT GRANTED** — this is a CANDIDATE_SAMPLE_ONLY artifact; the two worked cases and all 39 register rows remain SAMPLE/SYNTHETIC, no real meeting, vote, approval, procurement, appointment, signature, or third-party original is asserted or implied.
- No correctness, authenticity, boundary, or arithmetic defect exists requiring a rebuild; only F1 (a content-completion edit) is warranted.
