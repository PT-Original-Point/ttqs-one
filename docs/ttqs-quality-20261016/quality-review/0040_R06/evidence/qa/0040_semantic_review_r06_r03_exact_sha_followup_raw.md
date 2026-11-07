## R03 bounded exact-SHA follow-up — **PASS**

Freshly read from disk:

- **DOCX:** `115caf94165263040b27dbea5a2c83e02f94253d361e16784da398cefd3562d7` — matches expected.
- **Register:** `a75092ac268bc4d0e37bf677f2b3ea6e7cf8be808a5bed1cb52e39e1cb0eaa2d` — matches expected.

The corrected register locators agree with the existing page images:

- **0040-SYN-004:** Printed p.3 matrix; all four K1–K4 baseline/target/gap rows are on that page.
- **0040-SYN-BL-K3:** Printed p.3, K3「同意與隱私界線」row, first column; baseline 1.2, target 2, gap 0.8.
- **0040-SYN-BL-K4:** Printed p.3, K4「收尾與交接」row, first column; baseline 0.6, target 2, gap 1.4.
- **Printed p.4** is the rubric continuation with K3/K4 descriptors; it does not contain those baseline values.

Checked all 40 register rows against the existing R01 page map: 40 unique IDs, all populated and bound to the DOCX SHA; no other material locator defect found in this bounded check.

The prior R02 response remains preserved as returned. Its DOCX hash had a transposition typo; this R03 follow-up binds to the freshly verified hash above. No files were changed or rerendered. This is a locator/hash follow-up, not a full semantic re-review or promotion decision.
