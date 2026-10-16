# DOCX 0040 R06 — targeted register locator correction

**State:** candidate only. Technical and primary visual checks pass. A targeted independent R02 recheck of three corrected register locators is pending; no promotion or formal acceptance is granted.

- Official requirement: I08-E03 / checkbox sequence 040; unique Blueprint row SHA-256 `ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943`.
- Candidate DOCX SHA-256: `115caf94165263040b27dbea5a2c83e02f94253d361e16784da398cefd3562d7`. The R06 DOCX bytes were not changed for the register locator correction.
- R01 independent semantic review: **PARTIAL**, exact candidate SHA above, reviewed register SHA `35ffc7df10bd5af3b71d18123d69e94a90462182e2ec128e36fae678460a0e72`. Raw reply SHA-256 `21267c10f5f09230f220faae72a5e4eb62245a78c6ff34a96167a6ed4aa4e917`; normalized receipt `8f9ee7963ca856e8d240a1b0b6ff2bc430c0f27758f686b630c764f12e822708`. R01 found only three inaccurate locators: SYN-004, BL-K3, BL-K4. Its reviewed register and technical receipt are preserved under `evidence/prior/`.
- Targeted repair: all three facts now point to the p.3 assessment matrix and the K3/K4 first-column baseline/target/gap cells. Page 4 contains the separate scoring-rubric continuation. Current register SHA-256 `a75092ac268bc4d0e37bf677f2b3ea6e7cf8be808a5bed1cb52e39e1cb0eaa2d`, 40 unique facts bound to the unchanged DOCX SHA.
- Technical verification: **PASS** — nine rendered pages, all 40 page-bound facts checked against rendered-page anchors, matrix and D04 evidence fields verified, calculations recalculate to 17/5, 31/5, +14/5 and 4/5=80%. Receipt: `c38a33509eb643b76ec7e141e1d6052edbe75574c2fb8381238ed7c1397a3b0a`.
- Primary visual verification: **PASS** for all nine existing page images. PDF SHA-256 `76d1239f37b87c78388f94a7cd7282062424dbd4dffe7ba5ce8d8f773539edc7`. No DOCX rerender or rebuild occurred during this register-only repair.
- R05 findings F01/F02/F03 remain resolved in R06. All case facts remain SAMPLE/SYNTHETIC; no external original, association approval, signature, attendance, or real outcome is claimed.
- Candidate state: `CANDIDATE_NOT_PROMOTED`; formal acceptance: `NOT_GRANTED`.
