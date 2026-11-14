# DOCX 0051 R01 — register-only correction receipt

- DOCX exact SHA remains `6f575ebb41c6c26b4d6b36262fb4d9a5abdae53cbdc1ff4e75acda46d5f0b495` (56,098 bytes).
- OpenCode v2 semantic review returned PASS for that exact DOCX and the preceding replacement-register SHA `cddc262b205850d9bbdc9297c316d901783b56b66d03d05e3e7af33889d94266`.
- The reviewer identified F024–F027 as having imprecise locators because the primary §6表12 anchor was omitted.
- A later change touched only those four `document_location` cells in the CSV, adding `§6表12`; current register SHA is `57da26117ebaf3a517af4fe040d54661ca1021faa1202d19d651b3a51866f707`. No sample values or DOCX bytes changed.
- `verify_register_locator_correction_0051.py` checked all 227 sequential unique IDs, required nonblank fields, SAMPLE-only statuses, the four corrected locators, and the candidate’s table-12 caption/objective-code references. Result: PASS; see `REGISTER_LOCATOR_QA_R01.json`.
- This deterministic receipt does not claim a second independent semantic review of the corrected companion register.
