# TTQS ONE — 0139 / I19-E29 / R09 candidate evidence

**State:** CANDIDATE. This package binds DOCX 0139 to official requirement I19-E29 and Unique Blueprint internal index 153. The printed official checkbox serial remains UNKNOWN; the internal index is not substituted for it.

**Current candidate:** `candidate/0139_R09.docx`, SHA-256 `1deaf540425e38b4ad0017e6cf6a90057dc372cf5af69bbe27346c7ac834df5e` (116,371 bytes).

R09 changes one ACT-03 evidence-description paragraph in the R08 parent: an unsupported L-2 rating of synthetic evidence was removed. The change does not alter the data, formulae, or 34-row synthetic replacement register. `R09_TECHNICAL_DELTA_QA.json` binds the exact candidate SHA and confirms the OOXML delta. Word rendered 23 pages. Page 13 was directly inspected; the other 22 pages were pixel-identical to the previously inspected R08 baseline.

The independent OpenCode v2 review used the confirmed route `opencode/glm-5.3-flash-free`, at reported cost USD 0. Its PASS is limited to the single R09 text delta against the supplied §9.2 and SAMPLE/HOLD context. It is not a second full-document review. The prior full-body R08 review is retained in `history/R08_parent_NOT_CURRENT/`, and the R09-to-R08 byte comparison documents the single changed paragraph.

All examples remain SAMPLE/SYNTHETIC. REAL evidence is UNKNOWN/HOLD. Formal acceptance is NOT_GRANTED. No association approval, real outcome, signature, or third-party evidence is asserted. The historical R08 DOCX is explicitly NOT CURRENT.

`PUBLIC_PACKAGE_MANIFEST.json` contains SHA-256 and byte length for every payload file except the manifest itself. `.gitattributes` disables text conversion within this package so the published evidence bytes remain exact.