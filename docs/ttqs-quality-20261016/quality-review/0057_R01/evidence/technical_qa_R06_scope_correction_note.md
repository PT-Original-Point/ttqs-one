# 0057 R06 QA scope correction

The first technical-check draft is preserved as `technical_qa_R06_iteration01_scope_correction.json`. It contained two incorrect assertions.

1. It required internal DOCX ID `0057` and unique requirement ID `I13-E01` in the evaluator-facing body. The R09 Unique Blueprint explicitly forbids those IDs in the body. The corrected check verifies the exact official requirement quotation plus natural `I13`/checkbox `061` context in the DOCX, and verifies the three-way mapping in the external Blueprint and receipt.
2. It required every replacement-register status to be `SYNTHETIC`. The actual 237-row register has 215 `SYNTHETIC` and 22 `PENDING_REAL_SOURCE` entries. All examples remain synthetic; the 22 rows are explicitly pending authorized real-source replacement.

The corrected receipt applies those source-backed criteria. No DOCX bytes changed; R06 remains SHA-256 `3D4CA6C5D1BD0262A5CE47A1339021C4F7563D9E9F1D06C82676D9BB002DD472`.
