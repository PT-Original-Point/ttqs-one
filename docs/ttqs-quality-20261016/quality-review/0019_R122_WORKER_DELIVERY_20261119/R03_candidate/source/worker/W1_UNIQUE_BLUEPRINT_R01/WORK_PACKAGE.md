# Bounded W1 task package

work_id=TTQS_ONE_0019_I03_E02_UNIQUE_BLUEPRINT_W1_LONGCAT_R01_20261119
project_id=TTQS_ONE
doc_id=0019
requirement_id=I03-E02
stage=READY_UNIQUE_BLUEPRINT
role=source-bounded blueprint author; not DOCX writer and not semantic reviewer

## Exact candidate binding (context only; do not modify)
Candidate: `0019_I03-E02_R03.docx`
Candidate SHA-256: `A6DCFF55A916F8D52087B09D260CE1888252D1D4530EA37F63439045960B0CA7`
Bytes: 48,468
Current technical QA receipt reports SHA `5A204A6B3F24CD275A2B79DA86A82A4CB8E23F914040A41CA9E60FF8BCB2DF7E`, 48,321 bytes, decision FAIL. It is stale and must not be treated as QA of this candidate. Its listed false checks were calculations_reconciled and source_sha_present; both need independent bounded verification, not automatic acceptance.

## Source anchors and hashes
- Official evidence table: `OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf`, SHA-256 `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709`.
- Exact official requirement text recorded by the existing page-1 readback/review: “學員訓練及訓練機構事業發展相關的證明。” Locator: page 1, `PDF_TEXT_EXACT_PAGE_MATCH`. This quote is historical source-readback evidence supplied in the work package; do not claim you re-opened the PDF.
- Current 129-to-142 crosswalk: `CROSSWALK_129_TO_142_R01.csv`, SHA-256 `1DDFBB608BCAD25170683DDA42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679`; exact row: `I03-E02,1,0,0019,學員訓練及訓練機構事業發展相關的證明_可直接使用成品`.
- Current 157-checkbox map: `BLUEPRINT_157_CHECKBOXES_LIVE_R01.md`, SHA-256 `AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216`. A literal search for `I03-E02` and `0019` in this file returned no match. Do not invent a blueprint row from it.
- Negative neighbors: 0018 = I03-E01 training-system chart; 0020 = I03-E03 training types/KPI. Do not merge their content or requirements.

## Current candidate facts to treat as SAMPLE only
- It is an evidence-record/index genre, not a third-party original.
- It separates learner training/completion evidence from institution business-development evidence.
- All identifiers/dates/hours/outcomes are synthetic and must remain SAMPLE/SYNTHETIC with a replacement register.
- Underlying real activity sources are UNKNOWN; verification must stay N/A until originals are obtained.
- Existing manuscript contains 12/16=75.0%, 17/18=94.4%, and 16/18=88.9%; these are claims to re-compute, not trusted evidence.
- Do not fabricate names, attendance, certificates, signatures, institutional approval, outcomes, or third-party records.

## Output required
Return a compact, standalone `UNIQUE_BLUEPRINT_0019_I03-E02_R01.md` body with:
1. Requirement and source binding (separating verified bytes, historical quote, and UNKNOWN).
2. Exact purpose, reader, use moment, genre, required operational sections/fields, and evidence workflow.
3. Separate learner-training and institution-business-development evidence paths; traceability, source type, locator/version, verification, exceptions, correction trail, review and access controls.
4. SAMPLE/REAL truth boundary and complete replacement-register obligations.
5. Negative-neighbor exclusions for 0018 and 0020.
6. Acceptance checks concise enough for deterministic QA and an independent semantic reviewer.
7. Explicit residual source limitations.

Do not write generic TTQS content, do not rewrite the DOCX, do not claim the candidate passes, do not claim official source verification beyond the anchors above, and do not call tools or edit files. Mark any derived requirement as DERIVED and any unsupported fact as UNKNOWN. Return only the blueprint artifact plus a short note about any blocker.