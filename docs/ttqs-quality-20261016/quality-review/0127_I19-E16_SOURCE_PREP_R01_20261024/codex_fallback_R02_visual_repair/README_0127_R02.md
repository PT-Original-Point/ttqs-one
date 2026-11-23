# DOCX 0127 R02 candidate evidence

- Requirement: I19-E16; Unique Blueprint: UBP-0127-I19-E16.
- Candidate DOCX SHA-256: `abba46bcdd0919c4511df025cd90d65cd302fe3f9f59c86d0fa8b7efe2015285`.
- State: candidate only; formal acceptance not granted; REAL evidence remains UNKNOWN/HOLD.
- Technical pre-render gate: PASS for DOCX ZIP integrity, body/table font floors, structure, and the recorded CSV calculations.
- R02 embedded PNG assets were visually inspected directly. This is asset-only evidence, not full DOCX layout QA.
- Native Word export did not complete. Attempt 1 timed out; its initial ownership note was corrected, and only the exact renderer-owned Word instance was stopped. Attempt 2 opened the file but stalled at `ExportAsFixedFormat` and returned no PDF/page images. Prior Word instances were preserved.
- OpenCode v2.1.4 exact-SHA semantic review was dispatched once with requested model `opencode/glm-5.3-flash-free`. The provider returned HTTP 429 `Free usage limit reached` before review content; actual serving model is UNKNOWN, no fallback or alternate model retry was used, and there is no semantic verdict.
- R01 remains preserved as historical baseline. Its page 3 chart panels overlap and page 8 contains only a trailing disclosure line. R02 builder separates the chart panels, raises text to the required font floors, and moves the disclosure before source inventory; these are candidate repairs pending Word render verification.
- All example data remain SAMPLE/SYNTHETIC. No association approval, REAL performance, signature, or formal acceptance is asserted.

## Exact source pins

- SOURCE_PACKET SHA-256: `058663e200fd0207196c08a02e4d159c6e3eaa7f167094cd7b409b4050b18675`
- UNIQUE_BLUEPRINT SHA-256: `9a249a2e398407469bd82c9bf5d7a6188c9e3d28be79172bd4cc33b213c700ff`
- Market sample CSV SHA-256: `9d188e1c8c4b2a488cac2a989a029358dfae8c022ac30a9298518126d137fa36`
- Customer sample CSV SHA-256: `ca7d92fc02a98ae32e0d306c0a42ff2fd9d6cd58a25b53cb34e89203325b15b6`
