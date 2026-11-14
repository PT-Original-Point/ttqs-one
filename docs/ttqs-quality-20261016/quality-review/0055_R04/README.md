# TTQS ONE — DOCX 0055 R04 audit package

**State:** current candidate with an independent exact-SHA semantic PASS; Human formal acceptance has not been granted. This is not a real appointment or an association-approved record.

## Identity and source

- DOCX 0055 maps to official requirement I12-E03, indicator 12c, official checkbox 058. These identifiers are distinct.
- Official source: TTQS 查核佐證文件資料表—訓練機構版, page 4, indicator 12c. Local source SHA-256: 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709.
- Unique Blueprint: inputs/UNIQUE_BLUEPRINT_0055_R02.md, SHA-256 e255a2397b47868e3c0a740320bda0bd022b9e540f7adeb7211f66d32840c45b.
- Candidate candidate/0055_R04.docx: 0c4abf37856611a8226361cedb9bf58fd7c769a4cec27574920ed5d93ff4687b (56,062 bytes).
- Synthetic replacement register evidence/SYNTHETIC_REPLACEMENT_REGISTER_0055_R04.csv: SHA-256 66f660e24cfe12bd0c1351be577a6e4602f5a5454ba4914c0b736926cf9c0af7 (52 data rows).

## What changed in R04

R04 adds only the missing sample tie-break sequence to section 7 and changes only register row FAC-0055-010. The DOCX ZIP change is confined to word/document.xml; the other 18 members remain unchanged. Scores, weighting, case facts, dates, role codes and course plan were not changed. The added rule is explicitly a proposed SAMPLE/SYNTHETIC rule and places unresolved authority or evidence on HOLD.

The OpenCode V2 CLI supplied the bounded patch script. The CLI did not execute it or create the DOCX. Codex ran the deterministic script; the provenance record preserves this distinction.

## Quality evidence

- Technical receipt: evidence/technical_qa_R04.json — PASS_TECHNICAL_SCOPE, bound to the exact candidate SHA.
- Microsoft Word COM export produced an 11-page PDF; its SHA-256 is 12e8eefed72ae97057b0257b423c92d4daf473562d0bc60f4bf5d8c8e41e0f3b. The visual receipt records inspection of all 11 page images, including the section 7 insertion. soffice.exe was unavailable; this is a Word COM render, not a LibreOffice render.
- Independent OpenCode V2 semantic reviewer verdict: PASS, bound to the exact candidate and register SHA. Full response and task are included in review/independent_semantic_R04/.
- Windows source readback in evidence/cross_document_fact_readback_R04.json verified the four Blueprint-linked source DOCX hashes and their shared SAMPLE case ID, course title and 90+90+120+60 = 360 planned minutes. The exact source DOCX blobs at the recorded live branch commit match the local source bytes.

Reviewer scope limits remain visible: the reviewer did not independently re-render the DOCX, did not run a full-corpus duplication scan, and did not open the four same-case source DOCX files. The separate Windows readback supplements only the source-fact comparison; it does not rewrite the reviewer scope or claim formal acceptance.

## Worker recovery record

- Antigravity CLI init events name gemini-3.8-flash-high; no separate provider runtime identity was emitted. No Computer Use was used. The initial invocation and three bounded repairs produced no deliverable; new Antigravity CLI dispatches are paused for that route, while OpenCode V2 and other lawful routes remain available. Attempt status, available exit codes, stderr and path-redacted stdout are under review/antigravity_attempts/. Retry02 and retry03 stdout end with one incomplete JSONL event each; this is recorded in redaction_manifest.json. Original stdout files remain local; the manifest records source and sanitized hashes.
- OpenCode V2 CLI writer request: opencode/deepseek-v4.1-flash-free; reviewer request: opencode/mimo-v2.6-flash-free. Runtime identity was not emitted in captured events. CLI-reported cost was USD 0.00; actual billing is unknown.
- Large OpenCode event transcripts with extensive local tool paths are retained locally rather than published. The exact worker task, complete extracted response, CLI exit/stderr and bounded receipts are included.

## SAMPLE / REAL boundary

The course, candidates, reviewers, scores, committee discussion, authority checks, appointment terms and dates are synthetic examples. The candidate contains no real association approval, real committee decision, credential, signed or issued appointment, or actual course delivery. Real authority and real-source records remain UNKNOWN and must be verified before operational use.