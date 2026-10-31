# 0011 / I02-E02 — R11 candidate and quality evidence

- State: CANDIDATE / SAMPLE-SYNTHETIC. This is not formal association acceptance and does not claim REAL operating evidence.
- Official requirement: 「與訓練政策有關之訓練產品與市場定位。」
- Official checkbox serial: UNKNOWN (not inferred from doc_id).
- Unique Blueprint file SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`.
- Unique Blueprint raw-line SHA-256: `115b34f20b7f8106f5aa45d06da39ecae99a85a75f5276b79970911b428b32ec`.
- Canonical Blueprint-row SHA-256: `6243ec2921c7af4be7ed1d3538003f3cb2d4474d427a394a7146cbf8f0806dd5`.
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Requirement crosswalk SHA-256: `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679` (I02-E02 maps only to 0011).

## Candidate

`candidate/0011_I02-E02_R11.docx` SHA-256: `cce86967e17b6ff2a5af5bec7e37e0d6f850b069ad3845a8d04ebb1065b37f3d` (76,343 bytes). R11 changes only the front-page version label from an erroneous R09 to R11; the R10 candidate remains preserved locally.

## Same-SHA quality gates

- Technical: PASS, 27 tables / 260 table rows including headers / no empty cells / body ≥10.5 pt / tables ≥9.5 pt / 83 unique synthetic fact IDs / formula recalculation exact. Receipt: `qa/TECHNICAL_QA_R11.json`.
- Word-native visual: PASS, 28 pages. Page 1 directly inspected; pages 2–28 match the inspected R10 page images byte-for-byte. R11 PDF SHA-256: `9da52fb317c01db9385a11c18ec94fe5be2579d41c0d4536eb73fa84a059cf29`.
- Independent semantic/usability: PASS on the full extracted text and all 27 tables against the official requirement, unique Blueprint row, and negative-neighbor rows 0010 / I02-E01 and 0012 / I02-E03. Four LOW, nonblocking advisories are retained in the full response and adjudication. Requested route: `opencode/glm-5.3-flash-free`; actual serving model identity: UNKNOWN.
- Exact-SHA adjudication: `qa/INDEPENDENT_SEMANTIC_ADJUDICATION_R11.json`; raw OpenCode stdout, full review input, original response, and native dispatch terminal are retained in this package.

## Limitations and acceptance boundary

Four LOW advisories remain: (1) field dictionary roles are distributed across Form A rather than a single five-column table; (2) two Form B Fact-ID citations could be more exact; (3) one rubric crosswalk could be stated more explicitly; (4) parent-item attribution is not independently bound by the review packet. These were classified nonblocking by the reviewer and are listed verbatim in the response. The reviewer’s actual serving model identity is UNKNOWN. REAL association policies, survey records, approvals, delivery and outcomes remain UNKNOWN/HOLD. Formal acceptance is NOT_GRANTED.
