# 0098 R08→R10 bounded independent semantic delta review

Task: review only the documented R08→R10 change in the exact final DOCX. This is not a full rereview and not formal acceptance. Preserve prior R08 independent semantic PASS only within its recorded scope; do not extend it beyond unchanged content.

Binding:
- DOCX ID 0098; requirement I18-E06 (satisfaction survey system/process).
- R10 candidate SHA-256: 6310a71f6fb540b22572f823e7becb7a8198c12dc068eebff2794599e5a88152.
- R10 DOCX path: candidate/0098_R10.docx.
- R10 manuscript SHA-256: 07b741bbc7246a05863b9c07e019564cc2b7d8f36e9662cc02c64f45151d7d74.
- SAMPLE replacement register SHA-256: 923d20a99dc75f5f03436723a051d3f28d7b9a6f98858994411a19ceead8397e; 192 unique rows. Only FACT-0098-003 changed from R09; R08 prior evidence recorded 192 rows.
- R08 candidate SHA-256: a5d4bb14c884ff2d19db7bb6a86f999de0604d9ac6bacd9eb26f0b5db2c9cdba.
- R08 prior independent exact-SHA semantic review: PASS, OpenCode v2; review scope body text/register; expressly did not verify layout, official printed serial, or REAL originals. Response SHA-256 bd82f9eba803f7cc4e33e5ad4f7f6450fec812ff6002f50e2140c038cc5d3adf.

R10 change is one user-facing §8.2.1 body paragraph. R10 text:
“示範資料替換清冊：在同一交付套件的「evidence」資料夾開啟「SYNTHETIC_REPLACEMENT_REGISTER.csv」。清冊有 192 筆示範事實，每筆都有唯一代碼；只用來逐筆核對日後取得的真實來源。”
The adjacent instructions say confirm Word is R10 and the paired register is R10 with 192 rows/no duplicate codes; pause if absent/mismatched; replace SAMPLE only against lawful, verified REAL source and retain UNKNOWN/HOLD otherwise.

R09 defect being corrected: user-facing prose embedded an engineering register SHA; the earlier R08 lineage also had a nonportable internal evidence path. R10 points to the same-delivery-package evidence folder and filename, and moves exact hashes to sidecar receipts. No other substantive content is intended to change from the previously reviewed body. R10 Word was rendered with Microsoft Word; 29-page PDF and overview of all pages were inspected, plus full-size pages 2,14,28,29; no clipping/overlap observed. Full-size inspection was sampled, not every page at original scale.

Review only these questions:
1. Does the R10 direction let a human user locate the paired register in a normal delivery package without requiring knowledge of local Windows/Git paths?
2. Does it keep version/count mismatch as a HOLD and preserve SAMPLE/REAL boundaries without implying the association has real records?
3. Does removing the hash/path from the user-facing body introduce any material semantic regression in this changed section, given the stated unchanged remainder and prior R08 review?
4. Identify any concrete defect with exact locator, or return PARTIAL if this packet cannot support a sound judgment.
Do not claim you opened or independently hashed the DOCX. The exact SHA is supplied as binding by local technical evidence; state this limitation. Do not infer formal acceptance or REAL evidence.

Return concise JSON: verdict PASS/PARTIAL/FAIL; exact candidate SHA; scope; findings with locator and rationale; explicit limitations; whether any new repair is required. No tools or file operations.
