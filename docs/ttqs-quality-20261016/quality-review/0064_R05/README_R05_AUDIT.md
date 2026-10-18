# 0064 R05 audit bundle

- Project: TTQS_ONE
- Document ID: 0064
- Official requirement: I14-E05
- Official checkbox serial: 069
- Candidate: R05; status remains `CANDIDATE`, with formal acceptance and promotion not granted.
- DOCX SHA-256: `54888e13f954478051a49839d8b67ff845992c72811e41e09d90045e512c69e1`
- Unique Blueprint R02 SHA-256: `0f521debdaeeef17f2c47d11cccbb193e2a4b0f8370bf4dd56da86d512c0f3d8`
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`
- Render PDF SHA-256: `2d7e5c84d72b62b96b04cc45e7613154c2e959669e66cd8e27611b6f2ffe12c2` (28 pages; 28 page images included)

## Model recommendation and actual routes

The supplied OpenCode V2 daily report (source SHA-256 `2854ed92ff7d013b6bf74baf6de56d1916632e420d13900651d72dc6ae13e308`) recommended DeepSeek V4.1 Flash Free as the first isolated writer test and Beam Free as an elevated-priority reviewer. R01 manuscript work used `opencode/deepseek-v4.1-flash-free`; the exact-SHA R05 semantic review used `opencode/beam-free`. The corresponding invocation and response evidence is included under `model_routes/` and `review/`.

The local CLI was `opencode v2.0.29`, while the report stated `v2.0.32` as its latest confirmed release; version alignment is therefore `NOT_ALIGNED`. The report's recommendation to test free routes was followed, but this does not establish provider-side billing: billing remains `UNKNOWN`. OpenCode's canonical reviewer session reported cost `0`; that is only the session-reported field, not a provider invoice. The canonical session used 334,114 input, 11,617 output and 8,418 reasoning tokens, plus 8,746,240 cache-read tokens.

## Content, build, and quality result

R05 is based on Unique Blueprint R02 and the official I14-E05 source. It contains 12 synthetic task cards, timing and retrieval measures, arithmetic, a 12-row sample-to-real replacement register, SOP/hold criteria and explicit SAMPLE/REAL boundaries. The register CSV is included. A-0062-08 is explicitly held: no version, filename, path or content is disclosed; only the approved HOLD response is allowed.

R04 had a visible pagination defect: T07/T12 labels were separated from their task cards. R05 applied a targeted keep-with-next repair for those headings. Technical checks pass on the exact R05 SHA. The original visual-render receipt was still pending and had partial direct coverage. A supplemental direct inspection now covers all 28 page images and found one material layout defect: the §13.3 table header is stranded at the bottom of page 19, with data starting on page 20. R05 therefore remains a historical candidate with layout repair required; it is not visually accepted or promoted. The exact DOCX bytes are preserved. A targeted keep-with-next repair is recorded in the R06 package; the full R05 review history remains unchanged.

OpenCode Beam Free returned `PASS` for semantic review of the exact R05 SHA only. The reviewer did not personally inspect page images, compared only official PDF page 5, checked targeted cross-document facts rather than exhaustively rereading neighboring documents, and did not independently read `REQUIREMENT_SOURCE_RECONCILIATION.csv`; the review relies on the separate visual receipt for layout. Two informational observations remain: the T08 heading lacks a `keepNext` XML marker but no visible split results, and the 28-page length exceeds a non-binding 12–16 page recommendation. Neither was judged a blocking defect; no rebuild was made for those metadata-only observations.

The reviewer response, review packet/prompt, canonical raw session export, model-route record, and duplicate-session disclosure are included. A redundant Beam invocation was accidentally started while the canonical server-side session continued after its CLI client detached. It is preserved as duplicate evidence and excluded from the review count. Shell incompatibilities (POSIX `head`, a nested PowerShell `$_` filter, and Bash heredoc) caused failed client commands; the canonical session recovered using temporary Python scripts. No Antigravity or Computer Use was used.

## Evidence boundary

Technical, visual, and semantic checks are bound to the DOCX SHA above. This bundle documents a candidate-quality result only. It does not claim formal acceptance, association approval, real-world execution, real evidence, or promotion. Synthetic examples must be replaced and independently verified before any real use.

`MANIFEST_R05.json` hashes every other file in this bundle; it excludes itself to avoid a self-referential digest.
