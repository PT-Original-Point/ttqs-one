# 0142 R07 scoped repair evidence index

`doc_id=0142` / `requirement=I19-E32` / `official_157_index=156` / `revision=R07` / `state=CANDIDATE_NOT_ACCEPTED`.

## Exact bytes and source binding

- Candidate DOCX SHA-256: `50d911809834a3d607aa084ede054a8fecfb0b6fd12d0b7704a7f2158c941b9b` (51,717 bytes).
- Candidate body SHA-256: `ef47b5dd8855c50958a2ebc1a5ef3267a809e55381b7ced316ec2aec7f0c926a` (25,802 bytes).
- Current PR source ref used by W1 review: `cf566a0cb50cc2fc39f4900f330f30eb6d03911a`. Source Packet SHA-256 `e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49`; Unique Blueprint SHA-256 `4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b`.
- Build inputs: R06 DOCX `3781cb4cb2d26625fb5676181f4faa4176ca0bb80e2e3fac518245bbdc42f97e`; initial R07 `bd81634c5bebb05793bfd93f9c2255440c9e299237f3ba298f7c91ad57c68729`; R06 extracted body `cd838170a432cb31a0be7f490bb92019b9be046a5f503d3f9a8bb53ba8539150`.

## Material and QA delta

- Recovered W1 patch specification; deterministic local builder inserted the scoped verification-source column in Table 3 and updated R07 control revision/date. Other tables, paragraphs, sample arithmetic and 19-row in-document replacement register are recorded unchanged by 47 deterministic checks.
- Technical checks: `PASS_TECHNICAL_SCOPE_ONLY`, 47/47 checks true; body font floor 10.5 pt and table font floor 9.5 pt.
- Word opened and exported natively to a 14-page PDF, SHA-256 `f736404c625ec930a4da2c814e57ca2dbef87e66c66e96a4307fc3d93cec7c6e` (579,000 bytes). Fresh 120-dpi render hashes match all 14 prior page rasters; contact sheet visually reviewed, with full-page spot checks on 4, 8, 10 and 14.

## Worker collection and limits

- W1 writer task: requested `opencode/deepseek-v4.1-flash-free`; wrapper terminal exit `-1`; serving identity UNKNOWN. Worker patch spec was recovered; do not describe it as successful DOCX binary write.
- W1 Beam review: actual response PASS/no findings, exact candidate/body/current-source packet bindings; upstream model UNKNOWN; same W1 lane means no independent-owner credit.
- W2 Antigravity review: response PASS/no findings on matching candidate/body, but actual model UNKNOWN; resolver log says requested Gemini route was missing and defaulted to CCPA; its source/Blueprint differ from current PR source. Supplemental only.
- Independent semantic gate: `NOT_ESTABLISHED`. Formal acceptance: `NOT_GRANTED`. REAL data: `UNKNOWN/HOLD`.
