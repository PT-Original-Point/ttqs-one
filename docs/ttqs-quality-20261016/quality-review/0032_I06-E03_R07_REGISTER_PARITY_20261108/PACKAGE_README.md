# TTQS ONE 0032 R07 register parity repair

- Candidate DOCX SHA-256: e1d6311e9828f464aba7b9bc47c20fa8b5392951dba96cf9a71d77be73fb691f (unchanged).
- Source register SHA-256: 31f0d02d35e6b244fde51e793bd05d498a64b5c9522ea13040d2e09a2e1a985e.
- Derived register SHA-256: f423a9057185688695dcdeb96a50e7adde338d044a3b622db46130e22a8b2a32.
- R01 is a scoped partial repair: exact candidate cell-1 text applied to SYN-032-147, 149, 150, 151, and 153. SYN-032-148 was already exact and remains unchanged.
- SYN-032-152 is retained and excluded from a global parity PASS. Its register value combines role text and frequency/escalation content from separate candidate cells; a cell-1-only replacement would discard content. Resolve the cross-cell mapping in a later bounded change.
- W1 OpenCode and W2 Antigravity returned raw, hash-bound work receipts. The corrected W2 review is PASS_SCOPED; it supersedes the earlier overbroad review and accepts only the five corrections plus unchanged 148.
- No DOCX bytes were changed. No visual review was rerun. Candidate remains CANDIDATE; formal acceptance is not granted. No REAL source or association authorization is asserted.
