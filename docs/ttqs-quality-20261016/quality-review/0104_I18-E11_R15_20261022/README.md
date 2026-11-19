# DOCX 0104 / I18-E11 / official checkbox 112 — R16 candidate

State: CANDIDATE; not formally accepted. SAMPLE/SYNTHETIC data only. No association decision, signature, credential, or real outcome is asserted.

- Current R16 DOCX: candidate/R16/0104__證照獲取率_分析報告_R16.docx
- Exact SHA-256: 9a074b207e7a57f1448cf96868f3cc3f30a72834a021f9b04392909ea3183d7b (87,368 bytes)
- Mapping: DOCX 0104 → I18-E11 → checkbox 112 → official source page 7.
- Source packet SHA-256: a3c88e83117a33de657d075d53454eca4e743ec9de22d58a090c9cfd82e3a45a
- Unique Blueprint SHA-256: 65bfb2bbe8339ae00d542aac922aa1a09f678cd4a527a8475dd1b6aa4d485d94
- Crosswalk SHA-256: 922294941ce3f33eb83deef49f2aa0600cf44d42c9a79738e59394e61b12a220
- Synthetic replacement register: 124 fact rows; SHA-256 48e5aa975af18df8da95843ef165649853b7f48e226d3a70b8221111ef29c03e.

## Worker and quality evidence

The OpenCode v2 writer used selected model deepseek-v4.1-flash-free in native session ses_ea00e6c9bffeRq91HBDZl6RZBb; its recovered R16 manuscript is preserved with the dispatch/session receipt. The separate reviewer used selected model mimo-v2.6-flash-free, native session ses_ea002ffe1ffefP6DIiuFo8fPbr, and returned PASS_TEXT_ONLY, zero blocking findings, and three nonblocking observations on the same R16 SHA. The reviewer did not recompute the candidate hash, inspect page images, or perform real-person usability testing. Actual serving model/fallback and vendor billing remain UNKNOWN.

OpenCode CLI exit 1 and its raw provider invalid-output event are preserved. A later text event was returned in the same CLI invocation; the native session ended succeeded. This is not rewritten as a CLI exit-zero success.

Native Microsoft Word exported render/R16/0104_R16_word_native.pdf; 36 A4 pages were rasterized and directly inspected. The visual receipt covers all 36 page hashes and records nonblocking whitespace on pages 7, 13, 25 and 36. Technical QA passes on the same DOCX SHA and checks arithmetic/register; visual review is separate from text-only semantic review.

The initial technical run was retained as a failed validator expectation (121 rows). The register contains 124 rows; after correcting that expected row count, the rerun passed without changing DOCX bytes. R15 remains historical at candidate/0104__證照獲取率_分析報告_R15.docx; its file and receipts are preserved.

See evidence/R16/, review/R16/, and SHA256SUMS.json. This package does not represent formal acceptance.
