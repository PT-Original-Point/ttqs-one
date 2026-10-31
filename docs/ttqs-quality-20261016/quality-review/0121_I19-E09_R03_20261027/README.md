# DOCX 0121 / I19-E09 — R03 exact-SHA QA package

## Current status after R12 provider-identity correction

- Candidate state: `CANDIDATE`; formal acceptance: `NOT_GRANTED`; REAL association evidence: `NOT_PROVIDED`.
- R03 DOCX SHA-256: `ba067fdb2b90f99b9b354a6edc9d176d5af9527febdaaa71e6c550125f22b539` (72,632 bytes). No DOCX bytes changed during the correction.
- Technical QA: `PASS` on the exact R03 SHA. Word visual QA: `PASS_WITH_DELTA_SCOPE`, native Word PDF SHA-256 `fa3fd36e716372d47ae36a3eaf4a5f28ec5c395d9800e6764bf69325abed0f70`, 23 pages; changed pages 1 and 18 were directly inspected and the 21 unchanged pages were pixel-identical to R02. Body/table minimum fonts are 10.5/9.5 pt.
- Semantic acceptance: `NOT_GRANTED_PROVIDER_IDENTITY_UNKNOWN`. Antigravity's full-body response self-reported PASS and requested `gemini-3.8-flash-high`, but the native terminal records the actual serving model/provider as `UNKNOWN`; therefore it is not accepted as a verified Gemini review. The separate OpenCode GLM attempt was rejected before a model response by provider `free-limit` HTTP 429, so it produced no verdict.
- The original Antigravity response and dispatch evidence are retained under `evidence/R12_PROVIDER_IDENTITY_CORRECTION_20261027/ANTIGRAVITY_ORIGINAL/`. The OpenCode 429 receipts remain in `evidence/R12_OPENCODE_FREE_LIMIT_20261027/`.
- No REAL outcomes, participant identities, signatures, association approvals or third-party credentials are asserted. Sample reflections and values remain `SAMPLE/SYNTHETIC`.

## Official mapping and source anchors

- Internal doc_id: `0121`; official requirement: `I19-E09`; printed checkbox serial: `UNKNOWN`.
- Source packet SHA-256: `fbeb11b96648fff29a49a0fca74bf0cc3b3d1d29934f07dfaa3cf7e410a557fd`.
- Unique Blueprint SHA-256: `99320fdc9078615ad04087c43bcbd22c5bbf751a22127c51e048e909726a5fca`.
- Official mapping evidence SHA-256: `fc9e9704748e58847c14c707078acf66ed07f024e2b83c67201b2372ead8208d`; source/Blueprint row SHA-256: `e5956462565186757b6a20f53cff22e9e53cd5abca1e2b69e6942a24c91f5b08`.
- Existing source files are preserved at `source/`; this package references those exact source hashes and does not duplicate the official source.

## R03 content delta and review evidence

R03 is a minimal continuation of R02: it updates the candidate revision/date label at P002 and replaces the synthetic reflection at P163 to address the exact R02 reviewer finding. No other body bytes changed. The existing replacement-register row labels P07 as SAMPLE; it is not a real interview quotation.

The Antigravity response addresses the full extracted body and reports no substantive blockers, but its actual serving model remains UNKNOWN, so its PASS is retained only as an unqualified worker report. It did not inspect Word binary or layout; the separate native Word QA above covers the stated visual scope. The R12 correction receipt explains why the response is not an accepted semantic review. The earlier OpenCode attempt requested GLM-5.3 Flash Free but received HTTP 429 before a model response.

## Remaining gate

A qualified independent semantic review bound to exact DOCX SHA `ba067fdb2b90f99b9b354a6edc9d176d5af9527febdaaa71e6c550125f22b539` is still required. No DOCX rebuild is required unless that review identifies a concrete content defect.