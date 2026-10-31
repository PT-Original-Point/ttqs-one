# 0057 Blueprint R05 — build receipt (bounded T1 schema repair)

## Input lock

| Item | Value |
|---|---|
| Repair patch (brief) | `inputs/0057_BLUEPRINT_REPAIR_PATCH_R05.md` — SHA-256 `11ca22101745f25fae15de5359b34605b8aebb6c617ae9661cf24b510df384be` (matches declared SHA; verified before writing) |
| Source candidate | `inputs/0057_UNIQUE_BLUEPRINT_R04.md` — SHA-256 `af88b80542585e85e2d25e8b2011b8f1770b6aa049b7f8de9e067ac8a9af4552` (matches patch's required source SHA; re-hashed **after** the build and **unchanged**) |
| Independent audit | `review/0057_R04_independent_deterministic_audit_R01.md` — SHA-256 `de14999dbdbbe18db98a0d0f31dafd68774b8a81e4a685bcbe1550aa6509cb24` (verdict `R04 = CANDIDATE / DETERMINISTIC_AUDIT_FAIL_REPAIRABLE`) |
| Output | `inputs/0057_UNIQUE_BLUEPRINT_R05.md` — SHA-256 `efdfcfa52a4b7338ae7688e118f6b700cf1e6f4ee3ef423aa89ac3f253bc3f95` (computed only after all writes completed) |

Preserved unchanged (byte-for-byte): R01 `da3396b969512e131154a5702781d110fb6194dc92a765b9c49d6d268eadf0d5`, R02 `3d5e778b384e53e7b51cffadaf56a67f2e381807a6b16bbf334fe0fe81667d10`, R03 `8f3b404cad787975d06444603ca647702afc7f21df1d526d3ea2daeb800effb4` (matches the R03 SHA quoted in the R04 audit), R04 `af88b805…af4552`. **No DOCX was created or altered anywhere under `0057_R01`.** This is a reversible sidecar repair; it does **not** establish DOCX readiness, formal acceptance, or independent PASS.

## Scope of repair (only the four enumerated items)

1. **Remove `資料截點` from the T1 column list** (`| 資料截點 | 日期（全數 = `2026-06-30`） |` deleted). The T1 example table has no such column; the constant now lives in a table note (item 4).
2. **Add `追蹤波次`** as a column definition, carrying its existing displayed values `30/60/90/180（主波次 `T+90`）` (same value registered at `SF-0057-025`; no new synthetic value).
3. **Match the exact example labels**: `主波次 `T+90` 最晚到期` → `主波次最晚到期`; `是否列入分母` → `列入分母`.
4. **One T1 table note** added stating the shared data cutoff: `> 註：本表所有 cohort 共用單一資料截點（data cutoff）`2026-06-30`，各期追蹤成熟度均以此判定。` No column was added and no duplicate synthetic value introduced; the existing `P3-Q2` row and the two pre-existing notes are left intact.
5. **`SF-0057-001` locator** changed from the schema-row reading to the actual T1 note: `T1 表註（共同資料截點 = `2026-06-30`）`, retaining every valid §5.1 / §8.3 locator where the same value is displayed (`§5.1 段首`, `§5.1 硬規則1`, `§5.1 硬規則2`, `§8.3 規則5`, `T1 註（`P3-Q2` 未到期）`).

Net effect on the file: **+2 lines** (one blank line + one note line); schema row count unchanged at 9; all other content identical.

## Deterministic checks run (all before reporting)

A script re-read the written R05 bytes and compared them against R04:

- **Source lock**: R04 re-hashed after build = `af88b805…af4552` (unchanged); R03 still `8f3b404c…effb4`.
- **Scope / no-other-change**: `git diff --no-index --unified=0` reports **4 hunks**, all limited to T1 schema rows, the cutoff-note insertion, and the `SF-0057-001` locator. No other line changed.
- **T1 header match**: parsed 9 T1 schema field names `['period_id','完成窗起','完成窗迄','期類型','追蹤波次','主波次最晚到期','`T+90` 狀態','`T+180` 狀態','列入分母']` and the 9 T1 example header cells; ordered comparison is **EXACT_MATCH** (both raw and backtick-normalized).
- **Register integrity**: 232 `SF-0057-0NN` rows; IDs unique; contiguous 001–232; **no ID added or removed**; no duplicates.
- **Cutoff fact**: the new T1 note contains `2026-06-30`; `SF-0057-001` locator names that note and the fact label/value (`資料截點` / `2026-06-30`) is unchanged.
- **Encoding**: R05 written as UTF-8 with **no BOM** and **LF-only** line endings, matching R01–R04.

Result: **exact T1 header match = PASS; 232 IDs unchanged = PASS; R04 unchanged = PASS; no out-of-scope edits = PASS.**

## Unresolved issues / boundaries

1. This is a **bounded candidate repair**, not independent semantic PASS or formal acceptance. Exact-SHA semantic review of R05 remains deferred to a fresh reviewer context (R04's determinism audit failed only on this T1 schema defect).
2. No cohort windows, dates, maturity classifications, rates, arithmetic, narrative, T2/T3/T8/T9 content, atomic rows, or other register rows were touched.
3. Identity boundaries preserved: `0057` / `I13-E01` / checkbox `061` remain three distinct fields, clear of `062`/`063`; SAMPLE/SYNTHETIC and REAL boundaries intact; all facts remain `SYNTHETIC` or `PENDING_REAL_SOURCE`.
4. Pre-existing promotion HOLDs declared in Blueprint §16 remain open (historical 142-registry readback pending; mapping stays a crosswalk-supported candidate). No new synthetic facts, no official-requirement or Blueprint-identity changes.
5. No DOCX created, edited, or generated.

## Output

- `inputs/0057_UNIQUE_BLUEPRINT_R05.md` — SHA-256 **`efdfcfa52a4b7338ae7688e118f6b700cf1e6f4ee3ef423aa89ac3f253bc3f95`**
- This receipt: `build/0057_R05_blueprint_repair_receipt.md`
