# DOCX 0057 Blueprint R08 bounded correction brief

## Immutable inputs and worker-incident evidence

- Source candidate: `inputs/0057_UNIQUE_BLUEPRINT_R07.md`; exact raw-byte SHA-256: `e01d5278635a10ccdb6827bd98fa3f96af299048053c87eee89d94bf5e3364fa`.
- R07 raw bytes are UTF-8 without BOM, 132,137 bytes, 1,049 CRLF line endings. The earlier Builder-reported `6b8fc9b6198ac352439be839f09613f18804a8e063fde39df1643d74ba720b9e` is the universal-newline text digest, not the file's raw-byte digest. Preserve that original report/log and explicitly record the correction in the R08 receipt; do not alter R07.
- Preserve R01–R07 byte-for-byte. Create only `inputs/0057_UNIQUE_BLUEPRINT_R08.md` and `build/0057_R08_blueprint_repair_receipt.md`.
- Output encoding must be UTF-8 without BOM and LF-only, consistent with R01–R06. Hash the saved output with `hashlib.sha256(Path(...).read_bytes())`; do not hash re-encoded universal-newline text.
- Do not alter any DOCX or conduct a review in this task. This is a reversible correction to sidecar labels and exact-byte provenance.

## Required correction: 24 T9 register field/reason mismatches

R07 corrected the T9 row locators but left old finding labels in 24 register fields/reasons. Preserve every fact ID, locator, value, source, role, status, and decision. Correct only the field description and where necessary the locator rationale:

| IDs | Correct current T9 mapping | Required field label |
|---|---|---|
| SF-0057-165, 166, 175, 223, 228 | F3: supplement non-self-report corroboration | `改善項 F3` followed by the existing field type |
| SF-0057-167, 168, 176, 224 | F5: reduce accompanied/unaccompanied application gap | `改善項 F5` followed by the existing field type |
| SF-0057-169, 170, 177, 225, 229 | Case A operational barrier, explicitly not an §10.1 finding | `個案操作障礙改善` followed by the existing field type; do not label F4 |
| SF-0057-171, 172, 178, 226, 230 | F4: improve T+90 follow-up coverage | `改善項 F4` followed by the existing field type |
| SF-0057-173, 174, 179, 227, 231 | F2: improve actual post-training application | `改善項 F2` followed by the existing field type |

For SF-0057-228, replace its stale rationale reference to `T9 / F2` with `T9 / 補足非自述佐證列` and retain the fact that the non-self-report share is below 50%. For SF-0057-229, replace stale `T9 / F4` with `T9 / 降低個案表單負擔列`; for SF-0057-230 replace stale `T9 / F5` with `T9 / 提高追蹤涵蓋列`; for SF-0057-231 replace stale `T9 / F1` with `T9 / 提升訓後實際應用列`. The locators of these rows are already corrected and must remain unchanged.

Use exact field labels:
- F2 rows: `改善項 F2 期限`, `改善項 F2 目標值`, `改善項 F2 提案 owner`, `改善項 F2 行動`, `改善項 F2 再追蹤指標`.
- F3 rows: corresponding `改善項 F3 ...` labels.
- F4 rows: corresponding `改善項 F4 ...` labels.
- F5 rows: corresponding `改善項 F5 ...` labels.
- Case A rows: `個案操作障礙改善期限`, `個案操作障礙改善目標值`, `個案操作障礙提案 owner`, `個案操作障礙改善行動`, `個案操作障礙再追蹤指標`.

## Revision and readback

- Title/current revision → R08; add an R08 bounded-repair note stating only the 24 register field/reason corrections and byte-level hash correction; retain R07 as historical; update §0 current/historical summary and closing marker to R08.
- Do not rewrite R01–R07 historical notes or change analytical findings F1–F5, T9 display values/actions/dates/targets, the 237 register IDs, cohort numbers, calculations, other rows, identity mapping, or SAMPLE/REAL boundaries.
- Verify R07 raw-byte SHA before and after; confirm R01–R07 remain unchanged; verify R08 has no BOM/CRLF and is LF-only; parse all 237 IDs for uniqueness/contiguity and all rows for 10 cells; verify each of the 24 fields matches its locator's row and each of the four rationale references is corrected; re-check exact raw-byte SHA only after all writes are complete.
- Receipt must state the worker-reported normalized-text SHA and corrected R07 raw-byte SHA separately, plus exact R08 raw-byte SHA. Do not claim independent semantic PASS or DOCX acceptance.