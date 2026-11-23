# TTQS ONE 0040 R06 candidate delivery

- Project: `TTQS_ONE`; requirement `I08-E03`, official checkbox `040`; document ID `0040`.
- Candidate SHA-256: `b2635adfc72f0328509b582f1d9af5f37a6eca8a37c5a54cbf77a31deb63dde6` (51,379 bytes).
- Technical QA: PASS, including OOXML integrity, unchanged body text from R05, table grid alignment, register and arithmetic provenance, body/table font floors (10.5/9.5 pt), and no unconverted LaTeX markers.
- Visual QA: 8 pages; pages 1–7 are pixel-identical to the previously inspected R05 renders; page 8 was rendered and inspected in the R06 run. Word PDF and page PNGs are included.
- Independent semantic QA: W2 Antigravity CLI PASS on this exact SHA, zero blocking findings. Two LOW notes are preserved as nonblocking. Requested model was `gemini-3.8-flash-high`; provider-served model remains UNKNOWN.
- The document and all examples remain SAMPLE/SYNTHETIC. This is a candidate-quality result, not formal acceptance or REAL evidence.
- Raw GitHub byte readback: PASS for the candidate at immutable PR branch commit `ef16ff5ce1b70cc2580026e6b89d07589cd30b8e` (51,379 bytes; SHA-256 and Git Blob SHA-1 match). The later receipt commit preserves the same candidate blob; no formal acceptance is implied.

See `artifact_manifest.json` for the file hashes and sizes.