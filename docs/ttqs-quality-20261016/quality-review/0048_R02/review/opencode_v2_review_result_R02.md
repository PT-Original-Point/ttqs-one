I have everything I need. Both R01 findings are verified against the actual bytes, the SHA matches, and I recomputed all arithmetic. Here is the independent review.

---

# Independent exact-SHA semantic review — TTQS ONE DOCX 0048 R02

## Binding (independently recomputed)

| Item | Value |
|---|---|
| Artifact | `…\quality-review\0048_R02\candidate\0048_R02.docx` |
| Recomputed SHA-256 | `AD1F7AAA30E48B083452704C9493ECD710B283F24AAC9C46915E0FFCE0E6A729` |
| Reported SHA-256 | `ad1f7aaa30e48b083452704c9493ecd710b283f24aac9c46915e0ffce0e6a729` — **MATCH** |
| Bytes | 58,584 — MATCH |
| Package | 19 parts, 27 tables, 39 register rows (`SYN-048-001…039`, no gaps) |
| Method | Recomputed SHA; read `word/document.xml` + `header1/footer1` directly; recomputed every displayed figure; mapped two suspect paragraphs to rendered pages via read-only PDF text (no Word/CUA; no files modified; synthetic facts treated as synthetic) |

Verdict is bound to the exact SHA above only.

## Verdict: PARTIAL — formal acceptance NOT GRANTED

Both R01 defects are **closed**, and all semantic/authenticity/arithmetic criteria pass. One stated acceptance criterion is **not** met: the body font hard floor.

## R01 finding closure (verified against R02 bytes)

- **F1 (missing 填寫者／責任角色 column) — CORRECTED.** §02 / Table 5 header is now `欄位 | 定義／填寫內容 | 來源／附件定位 | 填寫者／責任角色 | 驗證規則` with the responsible-role column populated for all 8 rows (e.g. `案件承辦／紀錄人`, `制度權責者／紀錄人`, `紀錄人；當事人核實`, `檔案管理者`). Exactly one occurrence of the header, correctly structured. (page 2–3)
- **Distributed requirement→field→attachment trace — CORRECTED.** §01 / Table 3 is now a single explicit three-row mapping with columns `官方要求 | 本件正式紀錄欄位（§03） | 附件／原件定位與核對方式`, one row per official clause (大型採購均辦理會議通過 / 師資遴聘後亦經過會議或審查通過 / 並留有紀錄). (page 1–2)

## Criterion-by-criterion

| Criterion | Result | Locator |
|---|---|---|
| Requirement fit (procurement **and** post-selection instructor review + records) | PASS | §1 quote verbatim; §5–6 procurement; §7–8 instructor review |
| Correct genre (專屬佐證紀錄 / evidence_record) | PASS | Title; Table 1 文類／用途 |
| Direct usability (reusable forms + filled examples) | PASS | Tables 7–11 (blank) + Tables 12–21 (filled) |
| Completeness of both records | PASS | §5–6 authority/quorum/agenda/options/votes/conditions; §7–8 criteria/weights/raw scores/decision/conditions |
| Decision authority & evidence boundaries | PASS | §1 「不得自行填造規則」; Table 12 「REAL 權限 UNKNOWN」; Table 24 |
| SAMPLE/SYNTHETIC discipline | PASS | banner + §5/§7 labels + Appendix A (39 rows) + footer; no fabricated third-party original |
| Math (all recomputed) | PASS | see below |
| Cross-document separation | PASS | Table 25 (0045=I10-E01 SOP; 0047=I10-E02; 0049=I11-E01; checkbox 049 kept distinct) |
| Return / hold conditions | PASS | Table 23; §6 conditions; Table 22 |
| Title-blind purpose | PASS | §10 statement; mechanism-specific body |
| Administrator/evaluator usability | PASS | Table 2 step guide; Tables 7–11 fillable |
| Packet `required_tables_or_figures` schema | PASS | Table 5 (5 cols) + Table 3 (3-clause trace) |
| **Body font floor ≥10.5 pt** | **PARTIAL / FAIL** | see F1-R02 |

## Recomputed arithmetic (independently, all correct)

- §6 / Table 15: `120,000 − 113,000 = 7,000` ✓; `113,000 ÷ 120,000 = 0.941666… → 94.1666…% → 94.2%` (1 dp) ✓; `10 ÷ 10 = 100%` ✓
- §8 / Table 19: weights `35+25+15+15+10 = 100` ✓; X `35+20+12+12+10 = 89` ✓; Y `28+20+15+9+8 = 80` ✓
- §9: `8 ÷ 10 = 80%` ✓; case A `10/10 = 100%` ✓; case B `9/9 = 100%` ✓

No displayed result disagrees with its inputs.

## Finding (material, repairable)

**F1-R02 — PARTIAL (body font floor).** Two **non-table body paragraphs** use direct run formatting `w:sz 19` (9.5 pt), below the 10.5 pt body floor (packet acceptance test: 「正文至少10.5pt、表格至少9.5pt」):
1. page 1, front section **「30秒開始使用」** (immediately after the step table, before §01): literal run `對象定位：提供原始點協會行政人員熟悉欄位與操作的示範工具；不是協會已採用的制度或會議紀錄。`
2. page 11, end of **§10「正式使用前的替換與文件邊界」** (after the 官方要求追溯與負向鄰件 table): literal run `文件控制：R02 候選示範；本版未經協會核定或生效。真實紀錄應依正式文件管制程序編號、簽核、保存及調閱。`

Verified: these are outside all tables and not header/footer, and the run carrying the text (not merely the paragraph mark) is `w:sz 19`. All other body runs are ≥ `w:sz 21` (10.5 pt); table runs and header/footer are `w:sz 19` (allowed). This condition is **pre-existing in R01** (present at `e6bb07cc…`) — not a regression — and the R01 review's assertion that "body text ≥10.5 pt" was inaccurate.

**Repairable action:** set the text-run size of those two paragraphs to `w:sz 21` (or apply the body style at ≥10.5 pt). No content change and no other edits are needed; the DOCX SHA will then change and must be re-bound.

## Non-material observations (NOT rebuild triggers)

- **Terminology drift:** body uses 「師資遴選」 where the official requirement (P03-B10) says 「師資遴聘」 (e.g. §7 heading, Table 1, Table 4). §1 and Table 3 quote the official wording verbatim, so the requirement text is not rewritten; a parenthetical synonym note would remove drift. Non-blocking.
- **Table 3 rows 1–2 list the same §03 field set**; the two clauses are differentiated only in the attachment/original column. The required trace exists and is explicit, so the repair is satisfied; differentiation is adequate at the evidence-location level.
- `docProps/core.xml` `created = modified = 2013-12-23…` and `Normal.dotm` / Macintosh Word metadata — stale template metadata only.

## Bounded conclusion

- **Semantic verdict: PARTIAL.** Both R01 findings are verified corrected, and every requirement-fit, genre, usability, completeness, boundary, negative-neighbor, return/hold, title-blind, and arithmetic criterion passes. The sole remaining defect is the body-font-floor breach on two note paragraphs (F1-R02), a one-line style fix.
- **Formal acceptance: NOT GRANTED** — this is a `CANDIDATE_SAMPLE_ONLY` artifact; the two worked cases and all 39 register rows remain SAMPLE/SYNTHETIC, and no real meeting, vote, approval, procurement, appointment, signature, qualification, or third-party original is asserted or implied. Acceptance must be re-bound to the new SHA after the font-floor correction.
