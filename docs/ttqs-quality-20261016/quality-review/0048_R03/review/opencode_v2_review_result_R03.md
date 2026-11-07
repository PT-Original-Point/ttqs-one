All independent checks are complete. Here is the bound verdict.

---

# Independent exact-SHA review — TTQS ONE DOCX 0048 R03

## Verdict: **PASS**

Formal association acceptance: **NOT GRANTED** (candidate is `CANDIDATE_SAMPLE_ONLY`).

## Binding (independently recomputed)

| Item | Value |
|---|---|
| Artifact | `…\quality-review\0048_R03\candidate\0048_R03.docx` |
| SHA-256 **before** review | `d029d291425447f20d59cb54b9a30190cd8ac0621041d2233b4a1bb8d081cc39` |
| SHA-256 **after** review | `d029d291425447f20d59cb54b9a30190cd8ac0621041d2233b4a1bb8d081cc39` — **unchanged** |
| Bytes | 58,586 — MATCH |
| Official source PDF | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` — found locally (`E:\TTQS\_official_TTQS_checklist.pdf`, 303,044 bytes), **hash MATCH**, page 3 read directly |
| Method | Recomputed SHA twice; parsed `word/document.xml` + `styles.xml` + `header/footer` directly (no Word/COM); read all 16 rendered pages; diffed R02→R03; recomputed every figure. No candidate/evidence file was edited, rebuilt, or saved. |

The verdict is bound to the exact SHA above only.

## Criterion-by-criterion

| # | Criterion | Result | Page / section / table evidence |
|---|---|---|---|
| 1 | Exact official requirement | PASS | Official PDF p3 item 10 (P03-B10) reads verbatim 「大型採購均辦理會議通過、師資遴聘後亦經過會議或審查通過並留有紀錄。」 Candidate p2 §01 + p2 Table 3 rows quote it **identically, unaltered**. |
| 2 | Official identity not conflated | PASS | p1 Table 1 `DOCX 0048｜I10-E03｜官方方框 049（P03-B10）`; p11 Table 25 keeps 0045/I10-E01, 0047/I10-E02, 0049/I11-E01 distinct; header `DOCX 0048｜I10-E03｜官方方框 049`. DOCX 0049 ≠ checkbox 049. |
| 3 | Correct genre (evidence_record) | PASS | p1 Table 1 文類／用途 =「可直接操作的專屬佐證紀錄」; p2 「紀錄不是原件的替代品」; no substitution of originals. |
| 4 | Procurement meeting record completeness | PASS | p6 §05 Case A (Table 12 authority/scope/budget; Table 13 attendance+rules); p7 §06 (Table 14 agenda/evidence/discussion/options; Table 15 math; decision text with conditions 「在條件完成前不得下單、簽約或付款」); p8 Table 16 responsible roles + deadlines. |
| 5 | Post-selection instructor review completeness | PASS | p8 §07 Case B (Table 17 pre-set criteria/weights, attendance/validity); p9 §08 (Table 18 review dimensions, Table 19 raw+weighted scores, Table 20 decision/reason/conditions/follow-up). |
| 6 | Roles, authority, agenda, evidence, discussion, decisions, conditions, responsibility & deadlines | PASS | Tables 8–11 (blank fill-in), 12–21 (filled); each decision carries 理由/條件/禁止事項/責任期限. |
| 7 | Decision authority & evidence boundaries | PASS | p2 「不得自行填造規則」; p6 「REAL 權限 UNKNOWN」; p11 Table 24 minimum REAL sources; p10 Table 22 `停止標示「通過」`. |
| 8 | Distinct case IDs | PASS | Case A `SYN-I10E03-A-001` (p6), Case B `SYN-I10E03-B-001` (p8) — distinct, correctly cross-referenced. |
| 9 | Exact register linkage | PASS | 39 IDs `SYN-048-001…039` present in candidate, **no gaps**; each §5–§8 synthetic fact traces to Appendix A (p12–16 Table 26) with value/locator/replacement/responsible/status. |
| 10 | Real/SAMPLE boundary | PASS | Banner + footer on every page; per-case labels p6/p8; Appendix A disclaimer; no real meeting/vote/approval/appointment/signature/qualification/third-party original asserted or implied. |
| 11 | Body font floor ≥10.5 pt | PASS | Independently parsed: minimum body run = 10.5 pt; **0** body runs below floor (distribution 10.5/12/14/16/23 pt). |
| 12 | Table font floor ≥9.5 pt | PASS | All 542 table runs = 9.5 pt; **0** below floor. Header/footer = 9.5 pt (permitted; not body/table). |
| 13 | R02 repairs verified | PASS | (a) §02/p3 Table 5 now has explicit `填寫者／責任角色` column, 8 rows populated. (b) §01/p2 Table 3 = single 3-row `官方要求｜本件正式紀錄欄位（§03）｜附件／原件定位與核對方式` trace. |
| 14 | R02 font defect repaired (this R03) | PASS | p1 note「對象定位…」and p11 note「文件控制…」changed `w:sz 19 → 21` (9.5→10.5 pt), verified in bytes and render. |
| 15 | Return / hold / rejection conditions | PASS | p10 Table 23 (4 退件/暫停 conditions); p10 Table 22; p7 §06 hold conditions. |
| 16 | Title-blind identification | PASS | p11 statement: body identifies as「會議通過／審查通過紀錄」via participants/agenda/evidence/decision-conditions/votes/attachment index; not transferable to a peer requirement. |
| 17 | Human usability | PASS | p1 Table 2 4-step guide + 30-second start; Tables 7–11 directly fillable; whole doc readable at 16 pages. |
| 18 | All 16 rendered pages incl. p1 & p11 notes | PASS | Visual inspection of all pages via contact sheets: no blank page, clipping, overlap, orphan row, or unreadable table; pagination stable at 16. |

## Arithmetic recomputation (independent, all correct)

- p7 Table 15: `120,000 − 113,000 = 7,000` ✓ · `113,000 ÷ 120,000 = 0.941666… ×100% = 94.1666…% → 94.2%` (1 dp) ✓ · `10 ÷ 10 ×100% = 100%` ✓
- p9 Table 19: weights `35+25+15+15+10 = 100` ✓ · X `(5/5×35)+(4/5×25)+(4/5×15)+(4/5×15)+(5/5×10) = 35+20+12+12+10 = 89` ✓ · Y `28+20+15+9+8 = 80` ✓
- p10 §09: `8÷10×100% = 80%` (labelled illustration) ✓ · Case A `10/10 = 100%` ✓ · Case B `9/9 = 100%` ✓

No displayed result disagrees with its inputs.

## R02→R03 delta audit (confirms repair scope)

Only `word/document.xml` changed. Diff shows: two body notes `w:sz 19 → 21`, plus three version-string relabels (`R02`→`R03` in Table 1 版本/生效, the p11 control note, and Appendix B 修訂紀錄). No substantive content change. This matches the claimed repair exactly.

## Scope limitations

- Read-only; no Word COM/CUA invoked. Layout was judged from the supplied R03 render (PDF + 16 PNGs) and the 4 contact sheets, not re-rendered.
- The official requirement text and page/box (p3, P03-B10) were verified directly against the hash-matched official PDF. The **checkbox sequence `049`** and the 142-ID crosswalk were taken from the authoritative source map / Unique Blueprint row (row SHA `8b258f91…` recomputed as MATCH); they were not independently re-derived from the PDF.
- All names, roles, attendance, votes, thresholds, scores, approvals, qualifications, dates and case records are **SYNTHETIC**.

## Genuine defects requiring repair

**None.** Two non-material observations (not rebuild triggers): terminology drift 「師資遴選」 in §07 heading/Table 1 vs 「師資遴聘」 in the official text — the official PDF itself uses both forms, and §01/p2 Table 3 quote the requirement verbatim, so the requirement is not rewritten; and Table 3 rows 1–2 share the §03 field set, differentiated at the attachment/original column (as accepted in R02).

**Conclusion:** Both R02 findings are verified repaired on these exact bytes, all semantic/authenticity/arithmetic/font criteria pass, and the only prior blocking defect (body font floor) is independently confirmed fixed. Formal acceptance remains **NOT GRANTED** — this is a `CANDIDATE_SAMPLE_ONLY` artifact and no institutional approval is asserted or implied.