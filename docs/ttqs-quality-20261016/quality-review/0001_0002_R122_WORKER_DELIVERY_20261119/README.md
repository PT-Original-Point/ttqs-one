# TTQS ONE candidate delivery: 0001 / 0002

Both are CANDIDATE SAMPLE/SYNTHETIC work products, not REAL or formally accepted.

| doc_id | requirement | exact DOCX SHA-256 | technical | Word visual | independent semantic |
|---|---|---|---|---|---|
| 0001 | I01-E01 | `2C643258ADD377789F1A04F9FFE0FAEBF53CB2AEEE38EC0B7234E5BDA92BC0BB` | PASS | PASS, 12/12 | W2 PASS, exact SHA |
| 0002 | I01-E01 | `317867355DBF0759918A65C9623BA0FEBD05D7E88774E3E349C5EC18102420C7` | PASS | PASS, 15/15 | W1 PASS, exact SHA |

Semantic reviews used extracted DOCX text and did not independently re-extract official PDF page text. Visual QA was separate. Raw worker outputs, packets, OS start/terminal receipts, repair history, extracted text/PDFs, and input provenance are included. Superseded 0002 R02/R03 are under `0002/history/`.

## GitHub raw-byte readback

At immutable PR branch commit `d01e55f1a930a6fbfbcce8e813c680dfb1aff963`, GitHub base64 file readback and local SHA-256 verification confirmed both candidate DOCX files. The recorded byte counts and SHA-256 values match the exact-SHA technical, visual, and independent semantic receipts above. See `GITHUB_RAW_BYTE_READBACK_20261122.json` for per-file Git Blob SHA-1, reviewer routes, and the explicit CANDIDATE boundary. This is delivery evidence only; formal acceptance and REAL status are not claimed.
