# 0012 / I02-E03 — R08J candidate package

- Candidate SHA-256: `1b2ad16bb36d9ba867fd517067d0e2c61529b1bfe390e045e01cd05fca7795e6`
- State: `CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED`
- Requirement: I02-E03, “補助參與機構公開招生課程或進階課程優惠辦法之規定。”
- Unique Blueprint mapping: `source/official_blueprint_mapping.json`
- Parent candidate R08I SHA-256: `9524e1875d72f51b19e564702711eef1a000379695827918a0de1a154434fa97`
- Independent review of the parent SHA was PARTIAL. The located defect was that NTD 5,800, the remaining sample budget, had an ambiguous label next to NTD 4,800, the applicant's remaining unpaid eligible tuition.
- R08J changes only the §9 calculation label/formula explanation and the matching SYN-029 register row. Amounts and arithmetic remain unchanged.
- Technical QA: PASS for this exact SHA; 68-row Markdown/CSV register match, 17 DOCX tables / 221 rows, payment fields, math, and font floors were checked.
- Word native visual QA: PASS for this exact SHA. Microsoft Word COM exported the PDF without changing the DOCX; 28 pages were rasterized. The full set was reviewed in contact sheets, with full-size checks of pages 14 and 22.
- Independent semantic review of R08J: PENDING at package creation; do not treat parent review as R08J acceptance.
- Formal association approval and real-case evidence: NOT PROVIDED / UNKNOWN. This candidate remains SAMPLE/SYNTHETIC and is not an effective policy.
- Source GitHub head read before staging: `6cb393e01d11ebac9d5afbe71446e5753a3d9e57`.
