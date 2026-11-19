# 0010 / I02-E01 R04b exact-SHA independent semantic review

Requested route: OpenCode v2 CLI `opencode/deepseek-v4.1-flash-free` when its recorded provider cooldown has expired. Review only the attached text packet; no tools, browsing, file edits, or claims of unperformed local checks. Return one JSON object matching the schema below.

Exact Word candidate SHA-256: `9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe`.
Source Markdown SHA-256: `b16f1c4e9f674b6b6a1258a09192a87f40d4e92430810091fe2eadfe228aba47`.
Word text extraction SHA-256: `41212d79d37d23144c4305141f4e3b13e048a0e0dd02e51e64d01edd5ab30e74`.
SAMPLE/SYNTHETIC register SHA-256: `6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc`.
Official requirement: `對學員訓練成果有評核標準的訂定及說明。` (printed p.1, indicator 2).
Unique Blueprint file SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; row SHA-256: `3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d`.

Review the complete R04b body, extracted Word text and all 157 register rows. Verify R03 semantic findings and R04 changes remain repaired; question/LO allocation, 0–4 rubric, case and retest math, thresholds, atomic fact locators, case/retest provenance, title-blind genre and rejection of negative neighbors 0009/I01-E06 and 0011/I02-E02; practical use by a small volunteer association; consistency between Markdown, extracted Word text, register and exact candidate SHA; and SAMPLE/REAL boundary. Identify precise section/table/field locators for every finding. Do not promote unresolved Blueprint outward-policy/public-disclosure scope beyond PARTIAL/UNKNOWN. No actual learner, roster, authorizer, assessment or association approval evidence was supplied. Do not call synthetic material REAL, adopted, effective or formally accepted.

Technical/visual receipts are supplied for context but do not substitute for this independent semantic review. Do not perform layout review unless a concrete text-layout issue appears in the extracted content; the Word render is separately bound to the exact DOCX SHA.

JSON schema:
{
  "receipt_type":"independent_exact_sha_semantic_review",
  "review_id":"0010-I02-E01-R04b",
  "reviewed_at_utc":"ISO-8601",
  "candidate_sha256":"9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
  "source_markdown_sha256":"b16f1c4e9f674b6b6a1258a09192a87f40d4e92430810091fe2eadfe228aba47",
  "extracted_text_sha256":"41212d79d37d23144c4305141f4e3b13e048a0e0dd02e51e64d01edd5ab30e74",
  "register_sha256":"6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc",
  "verdict":"PASS|PARTIAL|FAIL",
  "scope":"...",
  "checks":[{"id":"...","result":"PASS|PARTIAL|FAIL","locator":"...","reason":"..."}],
  "findings":[{"id":"...","severity":"critical|major|moderate|minor","locator":"...","evidence":"...","required_repair":"..."}],
  "limitations":["..."],
  "does_not_claim":["REAL evidence","formal acceptance","unresolved Blueprint scope"]
}
