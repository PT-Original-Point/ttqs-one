# 0058 R07 failed layout attempt

- Candidate SHA-256: `C4464EDB21E2D7B118A1565C474A719BB1B97B97DDDCCD3ED3500ED6E5D14701` (derived from R06 `B7F8806A204EB6CB9C1F9FA2F84B016B6F1EAFB56FF43E5C7C02E2499CE13B07`).
- Word-export PDF SHA-256: `B62B99B0552737FB7C86B09A627976A74EE9E00F7B48F79C9AD8ACC1D8A54FCD`, 33 pages.
- Change: only `pageBreakBefore` added before the Table 10-3 caption; no content or data edits.
- Observed defect: the caption/header moved to page 31, but the R06 revision row was stranded alone on page 33. The document remained a failed visual candidate and was not accepted.
- Evidence images: `render_R07/contact-29-32.jpg` SHA-256 `DE56CF002DB780D4FDB44848E8A411B08C1685104E7D3E4844E1B98958C3A478`; `render_R07/contact-33-33.jpg` SHA-256 `0DF8044E0FB07CD9D98929DBC1D206278FB190670C6FA1DAD3F82B864319A8DE`.
- R08 addresses the measured cause by keeping the caption on a new page and reducing line spacing only within Table 10-3 data cells; R08 uses a fresh derivation from R06, not the failed R07 package.

**Result: FAIL for R07 visual layout. Preserve as historical failure evidence; do not reuse or promote.**
