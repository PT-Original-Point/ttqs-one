# TTQS ONE candidate delivery: 0001 / 0002

Both are CANDIDATE SAMPLE/SYNTHETIC work products, not REAL or formally accepted.

| doc_id | requirement | exact DOCX SHA-256 | technical | Word visual | independent semantic |
|---|---|---|---|---|---|
| 0001 | I01-E01 | `2C643258ADD377789F1A04F9FFE0FAEBF53CB2AEEE38EC0B7234E5BDA92BC0BB` | PASS | PASS, 12/12 | W2 PASS, exact SHA |
| 0002 | I01-E01 | `6C11620746C46C637222DA31BBACD7243CB6DD0C46E25296CDCD7FE08B556BCD` | PASS_STATIC | PASS, 19/19; Dot exact-SHA | Dot PASS, candidate ready for integration |

Semantic reviews used extracted DOCX text and did not independently re-extract official PDF page text. Visual QA was separate. Raw worker outputs, packets, OS start/terminal receipts, repair history, extracted text/PDFs, and input provenance are included. Superseded 0002 R02/R03 are under `0002/history/`.

## 0002 R07D exact candidate

Current candidate: `0002/candidate/0002_I01-E01_R07D.docx` (SHA-256 `6c11620746c46c637222da31bbacd7243cb6dd0c46e25296cdcd7fe08b556bcd`). The 18-row SAMPLE register, PASS_STATIC receipt, Dot exact acceptance, native Word receipt, event log, and 19-page PDF are recorded under `0002/qa/` and in the file hash manifest. R04 remains unchanged at its historical path; R02/R03 remain under `0002/history/`. Candidate only; REAL and Human formal acceptance are not granted.

## Historical GitHub raw-byte readback


At immutable PR branch commit `d01e55f1a930a6fbfbcce8e813c680dfb1aff963`, GitHub base64 file readback and local SHA-256 verification confirmed 0001 R01 and 0002 R04. This is historical evidence for those exact revisions and does not qualify R07D. The recorded byte counts and SHA-256 values match the exact-SHA technical, visual, and independent semantic receipts above. See `GITHUB_RAW_BYTE_READBACK_20261122.json` for per-file Git Blob SHA-1, reviewer routes, and the explicit CANDIDATE boundary. This is delivery evidence only; formal acceptance and REAL status are not claimed.
