# 0121 / I19-E09 — R03 candidate evidence

State: CANDIDATE. Formal association acceptance is NOT GRANTED; REAL evidence is NOT PROVIDED. The candidate and every sample record remain SAMPLE/SYNTHETIC.

## Exact mapping and source

- Internal document ID: 0121; official requirement: I19-E09. The printed official checkbox serial remains UNKNOWN.
- Source Packet SHA-256: fbeb11b96648fff29a49a0fca74bf0cc3b3d1d29934f07dfaa3cf7e410a557fd.
- Unique Blueprint SHA-256: 99320fdc9078615ad04087c43bcbd22c5bbf751a22127c51e048e909726a5fca.
- Official mapping evidence SHA-256: fc9e9704748e58847c14c707078acf66ed07f024e2b83c67201b2372ead8208d.

## R03 candidate and QA

- DOCX: `candidate/0121_I19-E09_R03.docx`, SHA-256 `ba067fdb2b90f99b9b354a6edc9d176d5af9527febdaaa71e6c550125f22b539` (72,632 bytes).
- Deterministic body-extract file SHA-256: `4ea875c255a3d1f852788a258725150729787f83dad96efa997dd491a8f01552`.
- R02 full-body independent review was PARTIAL at P162–P163; the worker's overall R02 PASS was not adopted because its chronology finding contradicted the sample dates and distribution. R03 repaired that one issue.
- Exact R03 delta review: PASS on the exact R03 DOCX/body hashes. It covers P002 revision/date and P163 text; the unchanged content inherits the R02 full-body scope.
- Technical/visual receipt: 27/27 checks, 23-page Word-native PDF SHA-256 `fa3fd36e716372d47ae36a3eaf4a5f28ec5c395d9800e6764bf69325abed0f70`; pages 1 and 18 changed and inspected, other 21 pages pixel-identical to R02. Body minimum 10.5 pt, table minimum 9.5 pt.
- Replacement register is extracted from exact DOCX table index 15 (zero-based), 22 rows; extraction receipt is included.

## R12 full-body semantic review (2026-10-27)

- Independent W2 Antigravity CLI review completed on the unchanged R03 candidate: SHA-256 `ba067fdb2b90f99b9b354a6edc9d176d5af9527febdaaa71e6c550125f22b539`; ordered body SHA-256 `4ea875c255a3d1f852788a258725150729787f83dad96efa997dd491a8f01552`. The reviewer returned PASS with 0 reported substantive blockers across requirement/provenance, genre/title-blind identity, negative neighbors, usable instruments, calculations, SAMPLE/REAL truth boundary, anti-fabrication and operational CAPA.
- Scope is text-only. The reviewer explicitly leaves Word-native typography and visual page layout UNKNOWN. The separate exact-SHA native QA remains 27/27 on a 23-page Word export; pages 1 and 18 inspected, 21 pages pixel-identical to prior reviewed pages; body/table floors 10.5/9.5 pt.
- Requested model: `gemini-3.8-flash-high`; model catalog listed it, but actual serving identity is UNKNOWN. Do not attribute this result to a verified Gemini serving model or claim provider fallback status. CLI-reported usage: 28,821 input + 23,965 output (thinking 17,128 is included in output), 52,786 total.
- Exact request SHA-256 `d5935a49c75152ff3e68451e9e78271f4ec4d746645bab49f89086a621576b1d`; raw stdout SHA-256 `93770fa08a7e4714c6b6e65d38c699f81bd4b26169a33e5f05741c951b5cdb10`; normalized reviewer response SHA-256 `9f68f37a3427aee265f54f3f895fa832cca6580a3f6fdc0de07916f47865ed4d`. Raw inputs, stdout/stderr, terminal and adjudication are under `worker/W2_R03_full_body_R12/`. Candidate remains CANDIDATE; REAL evidence NOT PROVIDED; formal association acceptance NOT GRANTED; no DOCX bytes changed.

## Worker and limitation record

- W2 Antigravity CLI requested `gemini-3.8-flash-high`; CLI selection reported that model. Provider serving identity remains UNKNOWN. The exact R03 response is PASS, 18,607 reported tokens, no external tool action. A protocol event named `finish` is documented separately and is not counted as an OS/file/browser/Computer-Use action.
- W1 OpenCode free review route returned HTTP 429 with `retryAfterMs=62226000`; no identical-input retry was attempted before its release window.
- Earlier R02 W2 attempt had exit 0 but an auto-denied command permission and an empty response; its 35,297 reported tokens are not credited as a useful review. The raw failure evidence is preserved.

No REAL interview, signature, consent, association approval or formal acceptance is asserted.
