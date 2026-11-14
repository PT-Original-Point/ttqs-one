## Verdict: **PARTIAL** — bound to DOCX SHA-256 `91d749d00b153227bb3db67a60c552c0e17fa2b5364c799dee7de6bf69117815`

I recomputed the candidate SHA and inspected its body and all 19 existing Word-rendered pages. The review used the official source, current source-map row and Unique Blueprint directly; I did not rely on Builder receipts.

**Mapping:** DOCX 0036 → I07-E04 → official checkbox 036. The official checklist p.2 says: 「有課程設計進度表、課程規劃流程圖說明、訓練規劃書等佐證資料。」 The current Unique Blueprint row SHA is `d4ac3b17720ba7411171215f28c7673b18eee6fd205879feb2b1bc875d71257f`.

| Gate | Result | Evidence |
|---|---|---|
| Requirement, genre, title-blind purpose | **PASS** | Page 1 and §§4–6, 7–12 provide an operational course-design procedure, flowchart, filled progress schedule, and training plan. The page 2 neighbor table distinguishes needs assessment, competency-method review, and multi-year program review. |
| Practical content and authority boundaries | **PASS, with exception-handling gap below** | §§2–4 define roles, inputs, decision points, and a nine-step procedure; pp. 11–13 provide usable record and assessment forms. Pages 1–2, 6–8, and 10–19 repeatedly label examples SAMPLE/SYNTHETIC and disclaim actual delivery, attendance, approval, and outcomes. |
| Case facts and calculations | **PASS** | Page 7: baselines 4/10, 5/10, 6/10, 3/10 are 40%, 50%, 60%, 30%; against 8/10 targets, gaps are 40, 30, 20, 50 percentage points. Pages 7–9 align those thresholds with the four objectives; coverage is 4/4 = 100%. Page 8 weighted options recalculate to A 3.3/5, B 4.7/5, C 3.5/5. Page 10 schedule totals 210 minutes (190 instruction/evaluation + 20 break). Pages 13–14: pre-test total 24, post-test 40, gain 16; 8/10 post-tests score at least 4/5. |
| R08→R09 semantic delta | **PASS** | R08 SHA `e2d4b3f5e906faaf3d473c7351bd79618a78dcf2c8f91a32a4e952d005ac5eae`. Only `word/document.xml` differs. After accounting for the repeated column header inserted before rubric item 8, the body text is identical. All 19 R08/R09 page PNGs are byte-identical. On R09 p.12, rubric items 1–7 appear; p.13 repeats the header and shows item 8 and the pass rule clearly. |
| Exception handling required by Blueprint | **PARTIAL — blocker** | §13, pp. 14–15, gives triggers, immediate handling, and escalation/closure paths, but no explicit escalation deadline or time limit for exceptions. The general two-working-day intake target in §4, p.4, does not set an exception escalation time. The current Blueprint calls for exception handling with escalation timing. |
| Human-facing content policy | **PARTIAL — blocker** | The p.6 “進度表怎麼維護” bullet instructs readers to update the 「替換清冊」. Page 1’s quick locator points to §15, and p.16 §15 is an official-requirement-to-body-location/evaluator-check table. These are internal register/evidence-map references in the DOCX body; the current `CURRENT_STATE.json` policy specifies `replacement_register_internal_sidecar=true` and `forbid_internal_control_metadata_in_body=true`. |

The render is legible across all 19 pages; no blank, clipped, or unreadable page was apparent. The sample scenarios, permissions, dates, course plan, and results do not claim real association approval or third-party evidence.

The candidate’s mapping, design content, arithmetic, and R08→R09 regression check pass. The missing exception escalation timing and the body’s internal register/evidence-map references prevent an overall PASS. No files were changed.
