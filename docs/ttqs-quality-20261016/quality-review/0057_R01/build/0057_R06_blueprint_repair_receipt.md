# 0057 Blueprint R06 — build receipt (bounded precision / provenance repair)

## Input lock

| Item | Value |
|---|---|
| Repair patch (brief) | `inputs/0057_BLUEPRINT_REPAIR_PATCH_R06.md` — SHA-256 `cbe2fb44982c4000bd0de11cdcb4b3bd04c5ca1d609922488d389f68cb33ae1c` (verified before writing) |
| Source candidate | `inputs/0057_UNIQUE_BLUEPRINT_R05.md` — SHA-256 `efdfcfa52a4b7338ae7688e118f6b700cf1e6f4ee3ef423aa89ac3f253bc3f95` (matches the patch's required source SHA; re-hashed **before and after** the build; **unchanged**) |
| Independent exact-SHA review | `review/0057_R05_semantic_review_GLM_R01.md` — SHA-256 `000428320a5df39d6bfb4d4fc8dfcfbb6580a4f5efe4f90967b13766f7994185` (verdict `PASS`, two non-blocking precision/version findings) |
| Output | `inputs/0057_UNIQUE_BLUEPRINT_R06.md` — SHA-256 `f724c2c46b44667988bab125bd30297728cf8e743a6d5ef6109fd5e452cccab6` (computed only after all writes completed) |

Preserved unchanged (byte-for-byte): R01 `da3396b969512e131154a5702781d110fb6194dc92a765b9c49d6d268eadf0d5`, R02 `3d5e778b384e53e7b51cffadaf56a67f2e381807a6b16bbf334fe0fe81667d10`, R03 `8f3b404cad787975d06444603ca647702afc7f21df1d526d3ea2daeb800effb4`, R04 `af88b80542585e85e2d25e8b2011b8f1770b6aa049b7f8de9e067ac8a9af4552`, R05 `efdfcfa52a4b7338ae7688e118f6b700cf1e6f4ee3ef423aa89ac3f253bc3f95`. **No DOCX was created or altered anywhere under `0057_R01`.** This is a reversible sidecar repair; it does **not** establish DOCX readiness, formal acceptance, or independent PASS.

## Scope of repair (only the two bounded items, plus the label/§0/closing-marker provenance edits they require)

1. **Current revision labels → R06.** Title set to `（R06）`; added a concise current `R06 修訂性質（bounded repair）` note describing only this patch; added the historical `R05 修訂性質（歷史）` note; demoted the `R04` top note heading to `（歷史）` (body text unchanged); updated §0's summary so **R06 is current** and **R05/R04 are historical**; closing marker changed to `（Blueprint R06 結束）`.
2. **Record R05 history.** New `R05 修訂性質（歷史）` note records the already-completed R05 repairs: the `T1` schema/example header alignment, the single shared `2026-06-30` cutoff table note, and the `SF-0057-001` locator correction. No T1 content or fact changed.
3. **Date-rationale wording (values preserved).** In §12.2 (`期限（deadline）`) and in the `SF-0057-191` 設值理由, replaced the day-count wording with `訓練後 1 個月內首次應用`. `T0=2025-03-15`, first application `2025-04-15`, all other dates, calculations, conclusions and register values are unchanged; the wording now describes the one-calendar-month interval and does not assert an elapsed-day count.

## Diff audit against R05 (no other change)

`difflib.SequenceMatcher` over decoded UTF-8 lines reports **exactly 6 changed regions** and every other line identical:

| # | R05 line(s) | R06 line(s) | Nature |
|---|---|---|---|
| 1 | 1 | 1 | title `（R04）` → `（R06）` |
| 2 | 5 | 5–14 | 1 removed + 9 added: insert `R06` note (3 lines) + blank `>` + `R05` historical note (4 lines) + blank `>`; demote `R04` heading line to `（歷史）` |
| 3 | 24 | 33 | §0 revision summary updated (R06 current; R05/R04 historical) |
| 4 | 636 | 645 | §12.2 date rationale `30 天內` → `1 個月內` |
| 5 | 862 | 871 | `SF-0057-191` rationale `30 天內` → `1 個月內` |
| 6 | 1024 | 1033 | closing marker `Blueprint R04 結束` → `Blueprint R06 結束` |

Net line delta: **+9** (R05 1028 LF → R06 1037 LF). No other line differs.

## Deterministic checks run (all before reporting)

- **Source lock**: R05 re-hashed before and after = `efdfcfa5…3f95` (unchanged); R01–R04 re-hashed and unchanged.
- **No-other-change**: 6 change regions only (table above); all other lines byte-identical.
- **Label/provenance**: title `（R06）` ×1; closing `（Blueprint R06 結束）` ×1; stale `Blueprint R04 結束` ×0; `R06 修訂性質（bounded repair）` ×2 (note heading + §0 reference); `R05 修訂性質（歷史）` ×1; `R04 修訂性質（歷史）` ×1; old `R04 修訂性質（bounded repair）` ×0.
- **History preserved**: `R04 欄名一致化` ×2 (unchanged); the register doctrine line `本 R04 已**逐值原子化**` unchanged (byte-equal between R05 and R06).
- **Date wording**: old `訓練後 30 天內首次應用` ×0 and `訓練後 30 天內` ×0 in R06; new `訓練後 1 個月內首次應用` ×3 (R06 note / §0 / `SF-0057-191`) and `訓練後 1 個月內` ×4 (adds §12.2). The only remaining unrelated `30 天內` is §8.1 Q1 (`過去 30 天內`, untouched).
- **Dates preserved**: `2025-03-15` ×4 and `2025-04-15` ×3 (each +1 only from the new provenance note's own mention); all other date tokens unchanged.
- **Register integrity**: 232 `SF-0057-0NN` rows; IDs unique; contiguous 001–232; **no ID added or removed**; no duplicates. IDs remain `SF-0057-001`…`SF-0057-232`.
- **T1 untouched**: the whole §7 `T1` block (schema + example + notes) is byte-identical between R05 and R06.
- **Encoding**: R06 written as UTF-8 with **no BOM** and **LF-only** line endings, matching R01–R05.

Result: **6 intended regions only = PASS; old wording removed from both rationale locations = PASS; R01–R05 unchanged = PASS; 232 contiguous IDs = PASS; T1 identical = PASS.**

## Boundaries (not independent acceptance)

1. This is a **bounded Blueprint candidate repair**, not DOCX production, not formal acceptance, and not association approval. A passing build receipt is **not** independent semantic acceptance; a fresh exact-SHA reviewer context is required for R06.
2. No new synthetic facts, IDs, tables, calculations, dates, claims, or association decisions were introduced.
3. Identity boundaries preserved: `0057` / `I13-E01` / official checkbox `061` remain three distinct fields, clear of `062`/`063`; cohort windows, maturity, rates, decision logic and SAMPLE/SYNTHETIC-vs-REAL declarations unchanged.
4. Pre-existing promotion HOLDs (historical 142-registry readback pending → mapping stays a crosswalk-supported candidate; all facts `SYNTHETIC`/`PENDING_REAL_SOURCE`) remain open and unchanged.
5. No DOCX created, edited, or generated; no shared control-plane file written.

## Output

- `inputs/0057_UNIQUE_BLUEPRINT_R06.md` — SHA-256 **`f724c2c46b44667988bab125bd30297728cf8e743a6d5ef6109fd5e452cccab6`**
- This receipt: `build/0057_R06_blueprint_repair_receipt.md`
