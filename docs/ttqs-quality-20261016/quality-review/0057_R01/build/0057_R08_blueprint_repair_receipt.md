# 0057 R08 Blueprint correction receipt

## Source lock
- Source candidate: `inputs/0057_UNIQUE_BLUEPRINT_R07.md`
- Corrected R07 raw-byte SHA-256: `e01d5278635a10ccdb6827bd98fa3f96af299048053c87eee89d94bf5e3364fa`
- Worker-reported normalized-text SHA-256 (R07, universal-newline digest): `6b8fc9b6198ac352439be839f09613f18804a8e063fde39df1643d74ba720b9e`
- Output: `inputs/0057_UNIQUE_BLUEPRINT_R08.md`
- Output raw-byte SHA-256 (UTF-8, no BOM, LF-only): `83371918a35f9ce62ac0780206534415202fb33421a590eb5c9b8cbad67a8453`

## Preservation
- R01–R07 were not modified; their raw-byte hashes were verified before and after.
- No DOCX was built or reviewed in this task.

## Correction applied
- 24 T9 register field labels were corrected to match their locators: `改善項 F2`, `改善項 F3`, `改善項 F4`, `改善項 F5`, or `個案操作障礙改善/提案 owner/行動/再追蹤指標`.
- Four stale rationale references were corrected for `SF-0057-228`, `229`, `230`, and `231`.
- Title, §0 summary, and closing marker were updated to R08; R07 is marked historical.
- No fact IDs, values, locators, sources, roles, statuses, findings, cohort numbers, calculations, other register rows, identity mapping, or SAMPLE/REAL boundaries were changed.

## Readback checks
1. R01–R07 raw-byte SHAs verified unchanged.
2. R08 is UTF-8 without BOM and LF-only.
3. All 237 fact IDs are unique and contiguous.
4. All register rows have 10 cells.
5. Each of the 24 corrected fields matches its locator's T9 row.
6. Each of the four rationale references is corrected.
7. R08 raw-byte SHA verified only after all writes were complete.


## Final exact-field correction

- In register row `SF-0057-229` only, the field label was corrected from `個案操作障礙改善再追蹤指標` to `個案操作障礙再追蹤指標`.
- Locator, value, rationale, all other content, and UTF-8 no-BOM LF-only encoding were preserved.
- Final R08 raw-byte SHA-256: `83371918a35f9ce62ac0780206534415202fb33421a590eb5c9b8cbad67a8453`.


## Revision-count wording correction

- In the R08 top note and Sec. 0 summary, 兩項 was corrected to 四項 to match the four numbered repair elements.
- Final R08 raw-byte SHA-256: 83371918a35f9ce62ac0780206534415202fb33421a590eb5c9b8cbad67a8453.

## Limitations
- This is a reversible source-side correction only.
- No independent semantic PASS or DOCX acceptance is claimed.
