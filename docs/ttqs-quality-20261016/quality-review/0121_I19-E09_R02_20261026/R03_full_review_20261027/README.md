# DOCX 0121 / I19-E09 — R03 exact-SHA QA package

## Status

- Candidate state: `CANDIDATE`; formal acceptance: `NOT_GRANTED`; REAL association evidence: `NOT_PROVIDED`.
- R03 DOCX SHA-256: `ba067fdb2b90f99b9b354a6edc9d176d5af9527febdaaa71e6c550125f22b539` (72,632 bytes). This exact candidate was not changed during review.
- Latest independent semantic result: reviewer response `PASS`; recorded scope is `PASS_FULL_BODY_TEXT_ONLY_WITH_PROVIDER_IDENTITY_UNKNOWN`. Requested model was `gemini-3.8-flash-high`; actual serving model/provider identity remains `UNKNOWN`.
- Technical and Word visual QA: PASS for the exact R03 candidate. Word-native PDF SHA-256 `fa3fd36e716372d47ae36a3eaf4a5f28ec5c395d9800e6764bf69325abed0f70`, 23 pages. Changed pages 1 and 18 were inspected; 21 unchanged pages were pixel-identical to R02. Body/table minimum fonts are 10.5/9.5 pt.
- No REAL outcomes, participant identities, signatures, association approvals or third-party credentials are asserted. Sample reflections and values remain SAMPLE/SYNTHETIC.

## Official mapping and source anchors

- Internal doc_id: `0121`; official requirement: `I19-E09`; printed checkbox serial: `UNKNOWN`.
- Source packet SHA-256: `fbeb11b96648fff29a49a0fca74bf0cc3b3d1d29934f07dfaa3cf7e410a557fd`.
- Unique Blueprint SHA-256: `99320fdc9078615ad04087c43bcbd22c5bbf751a22127c51e048e909726a5fca`.
- Official mapping evidence SHA-256: `fc9e9704748e58847c14c707078acf66ed07f024e2b83c67201b2372ead8208d`; source/Blueprint row SHA-256: `e5956462565186757b6a20f53cff22e9e53cd5abca1e2b69e6942a24c91f5b08`.
- Existing source files are preserved at `docs/ttqs-quality-20261016/quality-review/0121_I19-E09_R03_20261027/source/`; this package references those exact source hashes and does not duplicate the official source.

## R03 content delta and review

R03 is a minimal continuation of the R02 candidate: it updates the candidate revision/date label at P002 and replaces the synthetic reflection at P163 to address the exact R02 reviewer finding. No other body bytes were changed. The existing replacement register row continues to label P07 as SAMPLE; this is not a real interview quotation.

The R03 full-body reviewer checked exact mapping, title-blind genre, 0120/0122 negative-neighbor separation, 10 Likert items plus 2 open questions, skills rubric, cohort arithmetic, sample boundary and HOLD/REJECT controls. The raw response has no findings that block its text-only scope. It does not inspect Word binary or layout; layout evidence is the separate native Word QA above. Earlier R02 partial and R03 delta-review receipts remain preserved as history; this R03 full-body review is bound only to the R03 SHA.

## Reproduction receipts

The `review/ANTIGRAVITY_R12_FULL_SEMANTIC_R03_20261027/` directory includes the original request, raw stdout/stderr, extracted response, dispatch start/terminal, input manifest and CLI model catalogue. R12 reports exit 0, 52,786 tokens, no tool indicators, and no candidate mutation. Model/provider identity and cost remain UNKNOWN. No Computer Use was used.


