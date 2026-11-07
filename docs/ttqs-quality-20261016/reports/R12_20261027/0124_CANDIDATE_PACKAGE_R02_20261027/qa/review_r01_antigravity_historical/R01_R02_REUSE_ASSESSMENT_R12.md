# DOCX 0124 R01 Antigravity review reuse assessment (R12)

- Project: TTQS ONE; requirement: I19-E12; current candidate: R02.
- PR #92 branch readback: `work/ttqs-one-document-quality-contract-20261016` at `e130ab75a75e73574ed1a6a7914db4dd00c0e670` (PR head matched branch).
- Current candidate R02: SHA-256 `5ea20da675395954e5587859ddc3ca4b483abaeff90509a86c66950581afec07`; GitHub blob SHA-1 `319283191b9d51568b7a148a3611c8c0f780235e`.

## Recovered W2 work

A prior Antigravity CLI invocation is present locally and is now preserved in this sidecar package. `work_id=TTQS-0124-I19-E12-R01-ANTIGRAVITY-R12-EXACT-SHA-SEMANTIC-REVIEW` reviewed the R01 candidate SHA `0a6567c2779d9ad8014ab6d1c892779a98892351a38ceda0dea9fa8b24ff2988`. The CLI process exited 0 after 54.495 seconds and returned a text-only PASS. The wrapper requested `gemini-3.8-flash-high` and the CLI model catalog listed it, but the service response did not identify the inference model; actual model and fallback remain UNKNOWN. Usage recorded by the CLI session was 22,138 input + 6,412 output + 4,028 thinking = 28,550 tokens. No tool calls were observed. The candidate was not mutated.

## Why R01 PASS does not apply to R02

The R01 and R02 source packet SHA-256 is the same (`83a03deb7cbef3f07ef8b7ce0b2b25e1744baa6bc2e96b29e3259453558ccfee`), as is the Unique Blueprint SHA-256 (`d0d8b0990d96fb7dab5d02a34d9f507b6434e57778646c920c488f01c1ab0f42`). The candidate body is not identical: a deterministic WordprocessingML text extraction with whitespace normalization produced SHA-256 `d151e6021144db96dc2b975583dc307a39ce087528eedc60474eed5205cb5947` for R01 (12,294 characters) and `39c96a171eff281fbd02fbf3c85d5e03503146cdf600a3fb58d47a160978210d` for R02 (12,590 characters).

The existing R01-to-R02 table diff receipt (SHA-256 `0a27d9970240e1c4cbc1251464048f75fe65c169ec85b690e132a46d6279c86f`) records substantive changes: Table 3 adds separate dispositions for an offer/expected start and the CLAIM_ONLY, HOLD, HIRE_ONLY, FEEDBACK_ONLY, and NOT_ELIGIBLE states; Table 6 changes E3-E5 response choices and instructions, distinguishing NOT APPLICABLE, DECLINED, and UNKNOWN. These affect interpretation and case classification, so the R01 semantic PASS cannot be carried to R02 by metadata or layout equivalence.

## Current quality boundary and route status

R02 retains its existing technical PASS receipt (`38c151ee435d9f730f4754d1d1e8942b6d084d131d494dc3784e8abb9ca76ba8`) and 14-page visual PASS receipt (`e1648f48f04513c84fb131bf0199d51090f5524a5f057f37a2e9c7f24c1735f6`), each bound to R02 SHA `5ea20da675395954e5587859ddc3ca4b483abaeff90509a86c66950581afec07`. R02 independent semantic status remains NOT_GRANTED; formal acceptance is NOT_GRANTED and REAL evidence is UNKNOWN_NOT_SUPPLIED. No DOCX bytes were changed in this reconciliation.

The user-provided OpenCode daily report (attachment SHA-256 `ff3ca9886e3a345d78be358b2883296b7e5454408d23bc940fee239ba826c900`) reports global Free inference Operational at its 08:17 snapshot but explicitly says it did not perform account-level inference tests. That does not override the local account's actual provider 429 receipts. No OpenCode inference was attempted in this reconciliation.

**Next lawful action:** keep 0124 R02 in CANDIDATE / semantic NOT_GRANTED. Retry review only after a genuinely usable authorized reviewer route is evidenced; do not repeat the R01 prompt or treat the unknown serving model as a verified Gemini result. Continue independent READY documents outside this review lane.