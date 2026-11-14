# DOCX 0055 R04 bounded content repair

Project: TTQS_ONE
Document: 0055
Official requirement: I12-E03
Official evidence-table location: page 4, indicator 12c
157-item sequence: 058
Current predecessor: 0055 R03, exact SHA-256 747218b1ac4deb1e4ffc49b788eabd095e04f0cae894e4491bd2822e93898f71
Current register: SYNTHETIC_REPLACEMENT_REGISTER_0055_R03.csv, exact SHA-256 a0f0dcfb67ce6097f54f2c662cc261886441b95c3f5b12ab7e8b700223c85c23
Unique Blueprint: UNIQUE_BLUEPRINT_0055_R02.md, exact SHA-256 e255a2397b47868e3c0a740320bda0bd022b9e540f7adeb7211f66d32840c45b
Source map: SOURCE_MAP_R02.md, exact SHA-256 4dc7807d921848e3b47f5d1d28eb06e99124fdb32ef0c26286fc6ca4348b37c4

## Verified gap

The Unique Blueprint requires this deterministic tie-break rule:
higher subject-accuracy weighted points, then teaching-demonstration weighted points, then a documented second demonstration.
The full R02 semantic reviewer marked the omission nonblocking because the three SAMPLE totals are distinct, but the rule is still absent from the operational document. R03 repairs only the section 9 voting denominator; it did not change section 7. This task closes the real Blueprint content gap. It is not a metadata refresh.

## Writer change scope

Create a new R04 candidate from the supplied R03 DOCX. Preserve R03 unchanged. Edit only the section 7 ranking/check area and the matching existing register row FAC-0055-010. Do not change scores, weights, thresholds, case facts, roles, dates, sections, or layout settings. Do not add a new register row; keep the 52-row register schema and update the existing selection-rule row.

Add a short, readable paragraph immediately after the section 7 ranking verification. It must:
1. Mark the rule as SAMPLE/SYNTHETIC and as a proposed demonstration rule, not an adopted association policy.
2. Resolve a tie in order: subject-accuracy weighted points; teaching-demonstration weighted points; a second demonstration with the same prompt, preparation time, duration, and rubric, with observations and scores retained.
3. State that if a tie remains or the approved authority/rule cannot be verified, hold the decision pending the procedure authorized by real governing documents.
4. State the current three SAMPLE totals do not tie and this fallback was not triggered.

Update FAC-0055-010 so its locator and synthetic value cover the added section 7 rule, and its real-source, verifier, and HOLD fields continue to require an actually authorized selection policy. Preserve 52 rows, all required columns, and all unrelated register bytes/values.

## Technical constraints

- Prefer a surgical OOXML edit. Do not round-trip the DOCX through python-docx; the previous round-trip created an extra blank page. R03 was patched from its exact predecessor bytes.
- Output only to this R04 workspace. Do not overwrite R03 or any other document.
- Deliver candidate/0055_R04.docx, evidence/SYNTHETIC_REPLACEMENT_REGISTER_0055_R04.csv, a reproducible bounded patch script, and a concise change receipt with exact input and output SHA-256 values.
- Preserve strict SAMPLE/REAL boundaries. No real committee authority, candidate, credential, approval, appointment, signature, or course delivery may be invented.
- Do not claim technical, visual, or semantic PASS. A separate QA/reviewer will inspect the exact R04 SHA after build.

## Exact proposed insertion and register delta

Append this as a separate paragraph after the existing section 7 ranking verification:

「同分處理（SAMPLE / SYNTHETIC，提案規則）：若加權總分相同，先比較『專業內容正確性』加權點數，再比較『教學示範與引導』加權點數；仍同分時，安排相同題目、準備時間、時長及量尺的第二次試教，記錄評審觀察與分數。若仍同分，或無法核實具權限者與已核定的後續規則，立即 HOLD，依真實章程與授權處理，不另創規則。本例三組加權總分互異，未觸發此程序。此提案須由具權限者核定後始得正式採用。」

Update only FAC-0055-010 in the register:
- locator: 第 4 節量尺表「權重」欄；第 7 節排序核對與同分處理。
- synthetic value: retain weights 25/25/20/20/10 and add the same tie-break order and HOLD condition, marked as an unapproved synthetic proposal.
- rationale: demonstration of a predeclared, recalculable selection and tie procedure; not an adopted association policy.
- real source: governing authority and officially approved selection method, plus second-demonstration score sheets if used.
- verifier: the authorized person/body only after authority is verified.
- status remains SYNTHETIC.
- HOLD: no formal use until authority and tie rule are approved; if triggered but evidence or authority is missing, HOLD.
Preserve exactly 52 rows and all required columns. Preserve all other CSV rows and fields byte-for-byte.
