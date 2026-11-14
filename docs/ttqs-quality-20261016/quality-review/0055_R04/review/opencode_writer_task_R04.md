# OpenCode V2 bounded writer task — TTQS ONE 0055 R04

Use the current OpenCode V2 CLI free model session. Do not use Computer Use, browser/UI automation, Antigravity, external-provider keys, or any other agent. Stay inside this task directory.

Read only the existing `inputs/REVISION_PACKET_R04.md`, `inputs/patch_0055_R03_reference.py`, `inputs/0055_R03.docx` as binary ZIP/OOXML when needed, and `inputs/SYNTHETIC_REPLACEMENT_REGISTER_0055_R03.csv`. Confirm the exact input hashes named in the packet before designing the patch. Do not inspect paths outside this task folder.

Deliver exactly one reproducible script: `build/patch_0055_R04.py`. Do not execute it, do not create/edit a DOCX or CSV, and do not create/update reports. The script must use only Python standard library, be deterministic, fail closed on hash/anchor/schema mismatch, refuse overwrites, write only under this task directory, patch the DOCX ZIP package surgically without python-docx, and alter only `word/document.xml`. Preserve every other ZIP member byte-for-byte. Insert exactly the proposed SAMPLE/SYNTHETIC tie-break paragraph immediately after the exact ranking-verification paragraph. Preserve paragraph formatting by cloning compatible paragraph properties. Update only CSV row `FAC-0055-010`, preserving UTF-8/BOM, line endings, header, column order, exactly 52 data rows, and all other rows/fields byte-for-byte; status remains SYNTHETIC. Output paths when run must be `candidate/0055_R04.docx`, `evidence/SYNTHETIC_REPLACEMENT_REGISTER_0055_R04.csv`, and `evidence/patch_receipt_R04.json` with exact hashes, changed package members/row ID, `candidate_only=true`, and all QA-not-run flags explicitly true. No PASS, approval, real authority, or actual activity claims.

Exact DOCX source SHA-256: `747218B1AC4DEB1E4FFC49B788EABD095E04F0CAE894E4491BD2822E93898F71`.
Exact CSV source SHA-256: `A0F0DCFB67CE6097F54F2C662CC261886441B95C3F5B12AB7E8B700223C85C23`.
Exact ranking paragraph anchor:
`排序核對：C-03 87.6 > C-01 82.6 > C-02 81.0。各候選的專業內容正確性、教學示範與引導、成人志工適配與可近性，以及個資、角色與安全界線均達示例門檻；若真實原件或權限有任何一項無法核驗，該候選立即 HOLD，不因排序高而例外。`
Exact insertion text and only FAC-0055-010 field changes are in `inputs/REVISION_PACKET_R04.md`; follow them exactly. Keep R03 unchanged. Write the script once, then return a short summary naming its path and key safety checks. Do not create other files.
