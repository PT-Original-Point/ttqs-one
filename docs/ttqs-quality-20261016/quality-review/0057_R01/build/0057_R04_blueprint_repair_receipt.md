# 0057 Blueprint R04 — build receipt (bounded sidecar repair)

## Input lock

| Item | Value |
|---|---|
| Repair brief | `inputs/0057_BLUEPRINT_REPAIR_PATCH_R04.md` — SHA-256 `c665da83f3e62f54d128c6a7a2c35c3cd08df9534f2af6cf0a77ca519949ec48` (matches declared SHA; verified before writing) |
| Source candidate | `inputs/0057_UNIQUE_BLUEPRINT_R03.md` — SHA-256 `8f3b404cad787975d06444603ca647702afc7f21df1d526d3ea2daeb800effb4` (matches brief; **unchanged after this build**) |
| Defect list | `review/0057_R03_semantic_review_GLM_R01.md` (verdict `PARTIAL`; Section A = 10 bundled rows, Section B = 6 coverage/locator gaps) |
| Output | `inputs/0057_UNIQUE_BLUEPRINT_R04.md` — SHA-256 `af88b80542585e85e2d25e8b2011b8f1770b6aa049b7f8de9e067ac8a9af4552` (computed only after all writes completed) |

Preserved unchanged (byte-for-byte): R01 `da3396b969512e131154a5702781d110fb6194dc92a765b9c49d6d268eadf0d5`, R02 `3d5e778b384e53e7b51cffadaf56a67f2e381807a6b16bbf334fe0fe81667d10`, R03 `8f3b404c…eﬀb4`. **No DOCX was created or altered anywhere under `0057_R01`.** This is a reversible sidecar repair; it does **not** establish DOCX readiness, formal acceptance, or independent PASS. No association fact was invented; no official requirement text or Blueprint identity was altered.

## Repair groups applied

**G1 — §13.2 register atomicity (one value per row).** Ten flagged rows were split so each row carries one independently displayed fact. The original ID is kept for the first atomic fact; additional facts take fresh sequential IDs from the current maximum. Repeated-display locators were updated on every affected row (T7 cell + §12.1 佐證 index + §12.2 追蹤結果 cell now all carried where the same value repeats).

| Split of | Atomic facts now separate | New IDs |
|---|---|---|
| SF-0057-184 | `Q1=2 次` / `Q2=4` / `Q3=5` | 204, 205 |
| SF-0057-186 | `R1=3` / `R2=2` / `R3=3` / `R4=2` / 合計 `10/12` | 206, 207, 208, 209 |
| SF-0057-188 | 接觸紀錄筆數 `3 筆` / 觸發轉介界線筆數 `1 筆` | 210 |
| SF-0057-191 | `2025-04-15` / `2025-06-13` | 211 |
| SF-0057-192 | `C2` / `C3` | 212 |
| SF-0057-194 | 時限 `24 小時內` / `每月 2 班` | 213 |
| SF-0057-195 | 例會抽查回饋 / 界線判準卡 | 214 |
| SF-0057-198 | `時間不足` / `紀錄表欄位偏多（18 欄）` / `缺乏即時回饋` | 215, 216 |
| SF-0057-199 | 接觸紀錄抽查 `3 筆` / 觀察量尺 `10/12` | 217 |
| SF-0057-201 | 圖 3 節點 (1)–(6) 六段節點文字 | 218–222 |

**G2 — T8 locators (values unchanged).** Added the exact T8 cell locator to `SF-0057-115` (`T8 / P1 列 / 陪伴組應用率欄`), `118` (`T8 / P1 列 / 無陪伴組應用率欄`), `121` (`T8 / P2 列 / 陪伴組應用率欄`), `124` (`T8 / P2 列 / 無陪伴組應用率欄`), `127` (`T8 / P3 列 / 陪伴組應用率欄`), `130` (`T8 / P3 列 / 無陪伴組應用率欄`).

**G3 — T9 coverage + §11 date.** Registered the five F1–F5 action texts (`SF-0057-223`–`227`), the four missing F1/F2/F4/F5 re-tracking indicators (`SF-0057-228`–`231`; F3 coverage retained via `SF-0057-130`), and the `2027 上半年重檢` date (`SF-0057-232`, §11 補述).

**G4 — `SF-0057-001` locator.** Removed the ambiguous "T1 data-cell" reading. The locator now names only occurrences that actually display `2026-06-30`: the `T1` 欄定義 / 資料截點列 (type note「全數 = 2026-06-30」), §5.1 段首, §5.1 硬規則1, §5.1 硬規則2, §8.3 規則5, and the T1 註. No T1 column was added and no unregistered repeated value was introduced (smallest schema-preserving locator correction).

**G5 — schema/table consistency (computed values unchanged).** `T3`: the field schema now uses one canonical column set identical to the T3 example table (`period_id` / `能力項` / `滿分` / `總分門檻` / `該期達標率`); `評量題數` was removed with a stated reason (total-score design, no per-item item counts — listing it would fabricate item statistics), and `各項滿分`→`滿分`, `達門檻標準`→`總分門檻`. `T8`: a `欄 | 型別` schema table was added whose column names are identical to the T8 example table, plus a note that T5 rate values are repeated displays logged under the same `fact_id`.

## New IDs allocated (29 total)

`SF-0057-204` … `SF-0057-232` (contiguous, no gaps, no duplicates; next free = `SF-0057-233`). Grouped: 204–222 (atomicity), 223–232 (T9 coverage + §11 date). Every new fact row is marked `SYNTHETIC`; actual association records/decisions remain `UNKNOWN / PENDING_REAL_SOURCE`.

## Deterministic checks run (all before reporting)

A script re-read the written R04 bytes and ran **100 checks, 0 failures**:
- **Register integrity**: 232 `fact_id` rows; IDs unique and contiguous 1–232; every row has exactly 10 cells.
- **T2 arithmetic**: six rates × P1/P2/P3 recomputed from their own numerator/denominator cells (all match); merged row = column-wise sums of P1+P2+P3; `P3-Q2` left `—` with `A=14` informational only; nesting `G≤E≤D≤C≤A` and `F≤B≤A` per cohort.
- **T4**: `Tier-A + Tier-B + Tier-C = E` and `G = Tier-A + Tier-B` per cohort; `G/E` recomputed; Tier-A record-count column kept separate from persons.
- **T5**: group 涵蓋/應用 sums equal the period `D`/`E`; every group rate recomputed; merged `33+41=74`, `26+22=48`; P3 gap `75.0 − 50.0 = 25.0` pp.
- **T6**: `失聯 + 拒訪 = C − D` per cohort and per merged row.
- **Schema reconciliation**: T3 has no `評量題數` row; T3 schema names equal T3 example header; T8 schema names equal T8 example header.
- **Atomicity spot-check**: value cells of the split rows (184/186/188/191/192/194/195/198/199/200/201/204) contain no `；`/`、` bundling.
- **Date invariants**: P1/P2/P3 `T+90`, `P2`/`P3` `T+180`, `P3-Q2` earliest/latest `T+90` and latest `T+180`, and case `T+30/+60/+90/+180` all re-derived by calendar arithmetic and matched.
- **Boundary invariants confirmed intact**: `0057` = `I13-E01` = official checkbox `061` remain three distinct fields clear of `062`/`063`; decisions still bound to mature `P3` only; merged rates still labelled descriptive/non-decision.

## Interpretation notes, additions beyond the enumerated minimum, and residual issues

1. **Brief wording "§13.1 T3 field schema"** was read as the T3 field-schema table in §7 (the reviewer's own Section B row is "§13.1／§7 T3 欄不一致"); §13.1 itself is the register-row schema and was left intact.
2. **`SF-0057-200` normalized** (no new ID): it bundled the T+90 record count + referral flag + the main-wave decision, the same defect class as `SF-0057-188`. Its 合成值 is now the decision only; the count/flag remain covered by `SF-0057-188`/`210` (which now also carry the §12.2 追蹤結果 T+90 locator). Content-preserving, no data change.
3. **Two extra repeated-display locators added** so T9 問題欄 displays that repeat a registered value are locatored: `SF-0057-160` gains `T9 / F3 列 / 問題欄` (`≥15 百分點`), `SF-0057-215` gains `T9 / F4 列 / 問題欄` (`18 欄`). No new IDs.
4. **Residual (not flagged by the reviewer, left untouched to stay bounded):** T9 `F1 問題欄` ("應用率未隨達標率同步上升") is narrative-only with no numeric synthetic value, consistent with §10.1 finding narratives not carrying their own rows; `SF-0057-193` (示範任務) and `SF-0057-197` (成功準則) each carry one compound descriptive/rule sentence rather than a category in the brief's bundle list; the T1 field schema lists `資料截點` while the T1 example table instead shows `追蹤波次` (pre-existing T1 naming difference, outside the brief's T3/T8 scope — `SF-0057-001` now points explicitly at the schema definition row). None of these were raised by the R03 reviewer.
5. **No unresolved blocker.** The only open items remain the pre-existing promotion HOLDs already declared in the Blueprint (§16.1: historical 142-registry readback not performed → mapping stays a crosswalk-supported candidate; all facts still `SYNTHETIC`/`PENDING_REAL_SOURCE`). No independent PASS is claimed; a fresh independent exact-SHA review is required.
