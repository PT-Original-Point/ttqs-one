# 0120 R01A change note

- Document: 0120; official requirement: I19-E08; printed source page 8.
- Starting DOCX SHA-256: 7dfc32e23d0be9e5c5749b3e721ae47d7a472dd913d9d247ce76a70eaa8ebaf4 (R01 preserved unchanged).
- Finding: the R01 body had 15 baseline replacement entries, while satisfaction and assessment expansions were represented only by two aggregate rows. The synthetic source CSVs contain 8 satisfaction records and 14 test-score records.
- Change: preserve both aggregate rows and add 22 row-level entries to the DOCX table 26 and matching rows to `SYNTHETIC_REPLACEMENT_REGISTER_0120_R01A.csv`. The L08 nonresponse is explicitly not imputed. Every new row remains `SAMPLE/SYNTHETIC`, `PENDING_REAL_SOURCE`, and not a REAL record.
- Arithmetic: satisfaction has 7 respondents and 1 nonresponse; response means are recalculated from item values. Each of 14 test records has five 0-20 item scores and a checked total /100.
- Review state: candidate only; deterministic technical/arithmetic checks PASS; Word visual inspection PASS on all 15 pages; independent Antigravity CLI response PASS on the exact DOCX SHA with zero findings, but actual model identity and fallback state are UNKNOWN; no formal Human acceptance.
