# 0141 / I19-E31 — R07-C1.1 candidate evidence

Observed: 2026-10-25 10:39 Asia/Taipei. Repository: `PT-Original-Point/ttqs-one`, PR #92, branch `work/ttqs-one-document-quality-contract-20261016`; source branch head before this evidence commit: `da239f68e27fc2920f09d1ca359703b5cc4fe811`.

## Candidate and source binding

- Document ID: `0141`; official requirement ID: `I19-E31` (kept distinct).
- Candidate DOCX: `0141_I19-E31_R07_C1_1_CANDIDATE.docx`, SHA-256 `8e0252ac4ba18edbd364e29c7f143744e801b062b3c2cd8d69f5c4a83aee7c2c`, 165,128 bytes.
- Source packet SHA-256: `43c0e1bda5dfeb12c1ba8fc8805b876641f5184e4bf95eb4ef6c3182cf8ee964`.
- Unique Blueprint SHA-256: `e19761674045b2defa7090ba1d8f1224943a89e54811180c20b9ea362de59cda`.
- Synthetic response CSV SHA-256: `723259199dd51973fc6473ec000234cc853fa1511be05864fdfd7b08bb452862`; all 36 responses are SAMPLE/SYNTHETIC. Register contains 44 replacement rows.
- The exact predecessor used by the delta receipt is included as `0141_I19-E31_R07_C1_LAYOUTFIX2_CANDIDATE.docx`, SHA-256 `0922f737c19598b4448b60f25a6c39391bb444a1dde2536f8eef4e83cf44673a`. A different file named `...R07_C1_CANDIDATE.docx` has SHA `c9fb...` and is not the predecessor referenced by this delta.

## Verification state

- Deterministic source/math QA: PASS; 36-row dataset and displayed aggregates recomputed; build receipt is bound to candidate SHA above.
- Independent reviewer: PASS only for `SEMANTIC_VERSION_DELTA_ONLY` on the exact candidate SHA above; six scoped findings resolved. The reviewer’s actual provider/model identity is UNKNOWN (runtime claim is not attested); provider billing is also unverified.
- This scoped delta review does not re-review the full body, questionnaire, data, formulas, official mapping, or layout. The predecessor full semantic review was PARTIAL on its own SHA; that result is not upgraded or spliced into a full-document PASS.
- The predecessor packet receipt records prior raw SHA `23bfc238cc0b0b55665b71a39aab563f6aef7bad3bca31605268adaa6da2495e`, but the delta packet cites available raw response SHA `045e7f75e6bc8c405a4754abfc2305c4bc998d710a899827b07978a3d95b8e81`. The included raw response binds to predecessor DOCX SHA `0922f737...` and reports `PARTIAL`; the `23bfc...` raw bytes were not found in the current local R07 folder. Preserve this receipt linkage discrepancy as OPEN.
- Microsoft Word render and page-image visual review: PENDING. At the observation point, free RAM was about 1,020 MB and aggregate CPU load was 100%; many longstanding hidden Word automation processes were present. No process was terminated and no new Word render was started under that pressure.
- Candidate only. Formal acceptance NOT_GRANTED. Real association data UNKNOWN/HOLD. Official score NOT_ASSIGNED.

## Files in this evidence package

This directory includes the candidate DOCX, manuscript, replacement register, extracted text, source packet, unique Blueprint, synthetic source CSV, build/math/delta/patch receipts, exact-SHA reviewer packet and raw response, plus the exact predecessor DOCX and prior review materials required to understand the scoped result. The receipts retain their original scope and SHA bindings.