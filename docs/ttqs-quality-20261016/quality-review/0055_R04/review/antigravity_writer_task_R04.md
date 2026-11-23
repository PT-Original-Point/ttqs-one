# Antigravity writer task — 0055 R04

Use only the Antigravity CLI session's filesystem tools. Do not use Computer Use, browser/UI control, external messaging, shell tools, or other agents. The selected model must be exactly `gemini-3.8-flash-high`.

Keep every file operation inside this `0055_R04` task directory. Do not inspect or request access to any path outside it. The provided inputs and task packet contain the required context; proceed without any other files.

Important: `inputs/0055_R03.docx` is a binary input. Do not call a text-view tool on it or on a guessed `document.xml` path. Its SHA is provided above; the generated script must open it as a ZIP and inspect OOXML at runtime. The exact unique ranking-verification paragraph text in that document is:

`排序核對：C-03 87.6 > C-01 82.6 > C-02 81.0。各候選的專業內容正確性、教學示範與引導、成人志工適配與可近性，以及個資、角色與安全界線均達示例門檻；若真實原件或權限有任何一項無法核驗，該候選立即 HOLD，不因排序高而例外。`

Use the exact existing filenames in `inputs/`. The copied reference script is named `patch_0055_R03_reference.py`. Do not probe non-existent files or outputs. Read only text inputs that actually exist; use the packet and the exact anchor above, then write the required new script once with `write_to_file` and finish. Do not attempt to access the previously denied external contract or any other file outside this R04 folder.

## Scope

Read `inputs/REVISION_PACKET_R04.md` and the listed source/evidence files. Build only a reproducible Python standard-library patch script at `build/patch_0055_R04.py`. Do not execute it, do not create or edit a DOCX, do not edit the source candidate, and do not create or edit any report.

The exact source inputs are:

- `inputs/0055_R03.docx` — expected SHA-256 `747218B1AC4DEB1E4FFC49B788EABD095E04F0CAE894E4491BD2822E93898F71`
- `inputs/SYNTHETIC_REPLACEMENT_REGISTER_0055_R03.csv` — expected SHA-256 `A0F0DCFB67CE6097F54F2C662CC261886441B95C3F5B12AB7E8B700223C85C23`
- `inputs/UNIQUE_BLUEPRINT_0055_R02.md`
- `inputs/REVISION_PACKET_R04.md`

Use the exact proposed paragraph and the exact FAC-0055-010 field changes in the revision packet. This is a narrow substantive Blueprint repair: explicit tie resolution and HOLD conditions. Preserve SAMPLE/SYNTHETIC boundaries and the 52-row register.

## Script requirements

1. Be deterministic, bounded, idempotence-protected, and use only Python standard library. Refuse to overwrite any existing R04 candidate or evidence output.
2. Verify both expected input SHA-256 values before work. Read only the two copied inputs above; write only beneath this R04 directory.
3. Patch the DOCX as a ZIP package without `python-docx`. Preserve every ZIP member other than the intended `word/document.xml` member. Insert exactly one new paragraph immediately after the existing section 7 ranking verification paragraph identified from its actual text/OOXML; do not infer a different location merely from a heading or table. If the anchor is missing or ambiguous, fail closed without writing outputs.
4. Preserve the existing document structure and formatting. Keep the insertion a separate paragraph using a compatible neighboring paragraph style. The new paragraph must be the exact proposed Chinese text in the packet. Check the generated XML parses, the paragraph appears once, and all original text remains.
5. Update only row `FAC-0055-010` in the copied CSV. Keep the header, column order, exactly 52 data rows, and all other rows/fields byte-for-byte unchanged. Preserve the file's UTF-8/BOM and line-ending convention. If a required column/row is missing, duplicated, or malformed, fail closed. Keep status `SYNTHETIC`.
6. Write `candidate/0055_R04.docx`, `evidence/SYNTHETIC_REPLACEMENT_REGISTER_0055_R04.csv`, and a concise `evidence/patch_receipt_R04.json` containing exact input/output hashes, changed ZIP members, changed register row ID, and explicit `candidate_only=true`, `technical_qa_not_run=true`, `visual_qa_not_run=true`, `semantic_review_not_run=true`.
7. The script itself must not claim or imply PASS, approval, formal use, real committee authority, real appointments, or actual teaching activity.

Before finishing, inspect your script for output-scope violations and summarize its path and exact behavior. Do not run it.
