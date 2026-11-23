# Independent semantic review — TTQS ONE DOCX 0040 R06

**Overall verdict: PARTIAL**, bound to DOCX SHA-256 `115caf94165263040b27dbea5a2c83e02f94253d361e16784da398cefd3562d7`.

The document’s substantive content passes the reviewed semantic gates. The review remains PARTIAL because three replacement-register locators point to the wrong printed page/table content. Those locator errors are in the sidecar register, not the DOCX body.

## Exact artifacts and review route

- Candidate: [0040_R06.docx](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R06/candidate/0040_R06.docx>) — SHA-256 `115caf94165263040b27dbea5a2c83e02f94253d361e16784da398cefd3562d7`
- Register: [SYNTHETIC_REPLACEMENT_REGISTER_R06.csv](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R06/evidence/SYNTHETIC_REPLACEMENT_REGISTER_R06.csv>) — SHA-256 `35ffc7df10bd5af3b71d18123d69e94a90462182e2ec128e36fae678460a0e72`
- Existing Word-export PDF: SHA-256 `76d1239f37b87c78388f94a7cd7282062424dbd4dffe7ba5ce8d8f773539edc7`, 9 pages
- Official source PDF: SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`
- Source map: SHA-256 `405b987797d1558ecac182cea8e1adfbd1aead7754c880db32db43c235d5024e`
- Unique Blueprint row: SHA-256 `ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943`
- Companion 0039 R09 candidate directly checked for shared-case consistency: SHA-256 `3e7ed5f173dc4604803f477289f1d6190e95a5c58d3a229420eaee67037080f5`

The source map and Blueprint identify **DOCX 0040 → I08-E03 → official checkbox sequence 040**. The official PDF p.3 states: 「課程規劃會議紀錄展現訓練課程設計流程，擬定訓練評估方法並作為訓練成效評估的依據，且有佐證資料可查。」 The 0040 source-map row names the assessment-method and effectiveness-indicator matrix. The companion 0039 is the meeting-record example; the two documents share a synthetic case and are not mistaken for the same deliverable.

The package’s `CURRENT_STATE_reviewer_route.json` specifies `WIN10_CODEX_LOCAL_NATIVE_CONTROL_REVIEW`, prefers `CROSS_REVIEW_BY_OTHER_ACTIVE_AGENT`, and disallows OpenCode. I performed a read-only Codex review without invoking Builder. The local branch/head verified as `work/ttqs-one-document-quality-contract-20261016` / `66b54520057896a701b0c1f919d0213ad721fb7a`; the worktree was clean. The package mapping JSON has a container `revision` field of R03, but its 0040 mapping, official source, and exact Blueprint row agree with each other and with the R06 candidate metadata.

## Findings

| Gate | Result | Evidence and locator |
|---|---|---|
| Official requirement and genre | **PASS** | Official source p.3, source-map row `doc_id=0040`, and unique Blueprint row agree on I08-E03/040. DOCX pp.1–2 frames this as an assessment matrix/tool and says meeting decisions are documented in the companion meeting example. It does not present itself as the meeting minutes. |
| Title-blind purpose and adjacent-item distinction | **PASS** | With the title hidden, p.1’s user, use timing, steps, outputs, quoted requirement, and K1–K4 assessment content identify an assessment-method matrix. Page 2’s 「文件／資料｜本件如何引用｜不得推論」 table separates the meeting example, a separate needs-survey example, system-improvement records, and a course-plan document. Page 9’s 「區分相鄰工作文件」 guide repeats the functional distinctions. The body contains no internal Blueprint IDs, requirement IDs, hashes, or evaluator line-map; `SAMPLE-0039-01` is the human-facing synthetic case identifier. |
| Practical operation and evidence-location fields | **PASS** | Page 1 gives intended users, use timing, five operating steps, and outputs. On p.3, the K1–K4 matrix’s 「證據欄位、定位及責任」 column gives each row a synthetic index and tells the user to enter a controlled file ID, attachment/page, version, de-identified code, observation fact, score, date, and evaluator role. Page 6, 「原始評量證據定位」 in the D04 example, repeats the synthetic pointer, says no external original is attached, and instructs formal users to enter controlled file ID, attachment/page, and version; missing evidence is marked 「未提供／待補」, and the tool’s own page number cannot substitute for the original-record location. This resolves R05 finding F01. |
| SAMPLE/REAL, authority, and third-party boundaries | **PASS** | Page 1 marks the case, roles, scores, and calculations SAMPLE/SYNTHETIC and says they are not the association’s actual survey, course, or outcomes. Page 7 states there are no actual attendance, learner scores, approval, course-execution, or outcome originals and that the document does not create third-party originals or real signatures. Page 8, 「正式效力」 and 「替換示範資料」, says the tool is not approved/adopted and prohibits fabricated signatures, approvals, third-party documents, or participant records. |
| Shared case and date consistency | **PASS** | Page 1 identifies `SAMPLE-0039-01` and the sample date 2026-06-12. The directly checked 0039 R09 companion uses the same case/date and matching K1–K4 baselines and five paired score records. Page 2 says the separate needs-survey example is a different synthetic case and must not be merged. Page 7’s D04 deadline, 2026-06-19, is explicitly a sample target date and an unexecuted follow-up action—not the optional 30-day follow-up. |
| Arithmetic and thresholds | **PASS** | Page 3’s K1–K4 baseline means are 1.0, 0.6, 1.2, 0.6 against target 2, giving gaps 1.0, 1.4, 0.8, 1.4. Pages 3–4 define a 0/1/2 rubric, total 0–8, complete four ratings, total ≥6, and K3 ≥1; missing ratings are not filled with zero. Page 5’s five pretest totals are 2, 3, 4, 3, 5 (sum 17; mean 17/5=3.4); posttest totals are 6, 7, 6, 5, 7 (sum 31; mean 31/5=6.2); paired changes are +4,+4,+2,+2,+2 (sum 14; mean +2.8). D01, D02, D03, D05 pass; D04’s 5/8 does not. Thus 4/5=80%. Construct means also recalculate to pre 1.0/0.6/1.2/0.6 and post 2.0/1.6/1.6/1.0. Page 2’s 4/4=100% is correctly limited to design coverage, not learning or causal effect. |
| R05 finding F02: authorization rule vs D04 status | **PASS — resolved** | In the R06 register, `0040-SYN-009` points only to p.1, step 4, “30日追蹤另行核准,” and explicitly says it does not assert follow-up was or was not performed. D04’s unexecuted status is separately registered as `0040-SYN-CALC-009` (p.6 D04 follow-up row and p.7 tracking table) and `0040-SYN-037` (p.7 deadline/status cell). The two facts are no longer combined. |
| R05 finding F03: version metadata | **PASS — resolved** | DOCX core properties read as title 「訓練評估方法與成效指標對照表（示範工具）」, sample/user-facing subject, comments identifying R06, and `revision=6`. |
| Replacement-register integrity and locators | **PARTIAL — blocker** | The register has 40 rows and 40 unique fact IDs; every field is populated and every row is bound to the exact candidate SHA. `0040-REF-001`, `0040-SYN-006`, `0040-SYN-009`, and `0040-SYN-CALC-005` were directly checked and their values/locators match the body. However, **three other rows mislocate K3/K4 baseline values** (details below). |
| Readability and layout | **PASS, with minor pagination note** | I directly inspected all nine existing page PNGs and the PDF; no blank page, clipping, overlap, or unreadable content. The p.3 matrix is dense but legible; p.4 is a short continuation with substantial whitespace. At the bottom of p.6, the next table’s header appears without a data row; p.7 repeats the header and shows the rows, so the orphan header is awkward but does not hide content or prevent use. Pages 8–9 repeat the operating-guide header and remain readable. |

## Blocking register locator defects

The DOCX itself shows all four K1–K4 baseline/gap rows in the p.3 matrix headed 「差距與目標｜直接評量／工具｜時點與門檻｜證據欄位、定位及責任」. Printed p.4 is the continuation of the separate scoring rubric; its K3/K4 rows do not contain the baseline means or gaps.

- `0040-SYN-004` says K1–K2 are on p.3 and K3–K4 on p.4. All four target rows are on p.3; the p.4 K3/K4 rows are rubric descriptors.
- `0040-SYN-BL-K3` locates baseline 1.2 and gap 0.8 on p.4. They are in the p.3 matrix, K3 row, first column.
- `0040-SYN-BL-K4` locates baseline 0.6 and gap 1.4 on p.4. They are in the p.3 matrix, K4 row, first column.

These prevent a full PASS because the register is intended to trace synthetic facts to the printed evidence. The three locators should point to the p.3 matrix rows; no DOCX content repair is indicated by this review.

## R05 regression summary and limitations

All three R05 findings are resolved in R06: F01’s evidence ID/location prompts are present on p.3 and p.6; F02’s 30-day authorization rule and D04 unexecuted status are separately registered at p.1 and pp.6–7; F03’s core properties now identify R06/revision 6.

I read the prior R05 raw review (SHA `4c0cb2d6ba44a232d1aa5eb6707820893d56b9a78fd3da0f8a15e12c981e03df`) and receipt (SHA `62d970b0a2910094319ae3a3359d33add1ce7664696637106a5bd4b91158aaa2`) as regression references. I also read the R06 technical/visual receipts (SHAs `0b54517a969c4bda28538fd68b73af8e7701fe4e2fc60aea72f1907b801fe0e7` and `56cd1b98c7049f9fdac924fc428bfee987983d07881e7d35802def7ec5915184`) for artifact bindings; they were not treated as semantic proof. The visual judgment above comes from my direct inspection of all nine existing page images. I did not edit, rebuild, or rerender any file.

The local candidate SHA and branch/head were verified in this review; I did not independently re-fetch the remote GitHub blob during this turn. The review establishes a candidate-level result only and cannot prove the author’s personal identity separation from the package metadata.

**Candidate status: CANDIDATE / NOT_PROMOTED. Formal or Human acceptance is not granted. No review receipt was written.**


