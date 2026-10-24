# 0102 / I18-E09 — R08c against current R02

**State:** CANDIDATE. Semantic review is PASS / SEMANTIC_SCOPE_ONLY; formal acceptance is not granted and real evidence is not verified.

## Binding and byte identity

- Project document ID: 0102; official requirement: I18-E09; project registry index: 110; printed official checkbox serial: UNKNOWN.
- Current source packet R02 SHA-256: 54d9c05f70b4fef993bd92b656694030878a236e1a2d0c6a21af5d24d94fa1bd.
- Current Unique Blueprint R02 SHA-256: d6ab10107f42d6f913e1c94df45c8cd179babaa2603a8a7e628c2db78a0cce75.
- Candidate R08c SHA-256: 84c279d09484b88724dd59ae8a5155cb8d0be284133258e166269a80c26c67b4. The candidate was unchanged before and after the exact-SHA semantic review.
- Review input SHA-256: c40ac9356215e151e16a4049aa438a309ea777e10e93449b9b7c44515b00e19b.
- Do not transfer PASS from R14 or R35: their reviews bind to older R01/other source hashes.

## Evidence scopes

- Semantic: independent OpenCode CLI review returned PASS / SEMANTIC_SCOPE_ONLY, zero blockers, against the exact R08c SHA and the current R02 packet and Blueprint. The original response, JSONL stdout, sanitized native-session metadata and dispatch receipt are included. The session selected opencode/mimo-v2.6-flash-free; native app reported cost 0. Provider backend identity, provider fallback and actual billing remain UNKNOWN.
- Nonblocking reviewer notes: (1) cover/footer say R08c while the version-history row still says R08; (2) Form F has generic deadline labels and no explicit evidence-used field, although related dates and evidence appear elsewhere. These are disclosed, not converted into PASS on missing subscopes.
- Technical: existing Word/OOXML receipts bind to the R08 lineage and current R02 source hashes. R08c changes only word/document.xml and word/footer1.xml for candidate-label correction; other package members are reported byte-identical to R08a. Technical receipt reports 41 tables, 396 rows with row-splitting prevention, and font minima 10.5 pt body / 9.5 pt table.
- Word and visual: Microsoft Word 16.0 exported the exact R08c to a 57-page PDF (SHA-256 c73b667abd9213cf6f1e93fb8a9343bba6f9a94cf30fc7884c68a23286bfc6a0). The existing visual receipt reports all 57 pages inspected on five R08a contact sheets; the R08c-only page 1 and page 57 deltas were rerendered and inspected. This run directly inspected R08c pages 1 and 57 and contact sheet pages 1–12.
- Content boundary: two illustrative synthetic cases; zero third-party originals, zero verified awards, zero human-review-eligible cases. This is not association performance and does not authorize external disclosure. Formal acceptance remains NOT_GRANTED; real evidence remains NOT_VERIFIED.

## Current R02 controls confirmed by the exact-SHA reviewer

The reviewer checked the separated evidence state/disposition tokens; response deadline vs internal review date; purpose-specific consent; all-ten Form F decision gate; independent source-verification and disclosure measures; CASE-01 URL-less screenshot → RECEIVED_UNVERIFIED + HOLD; and full case IDs/shared GLOBAL fact rows. It also checked genre, neighboring requirements, sample arithmetic, rejection/hold conditions and title-hidden use.

## Work and dispatch record

- Work ID: TTQS-0102-I18E09-R08c-CURRENT-R02-SEMANTIC-REVIEW-R01.
- Windows PID 72584, OpenCode CLI 2.0.32, exit 0, 255.88 seconds, hidden window, MainWindowHandle=0.
- Native session: ses_e9811dea9ffeHf6zEZUn38gl5P; app-reported input 38,013, output 5,486, reasoning 14,584, cache-read 4,864, cost 0.
- provider_backend_identity=UNKNOWN; provider_side_fallback=UNKNOWN; actual_billing=UNKNOWN.

## Package source

Prepared for readback against PR #92 branch head 4e660df2f63afc63f85afe00afbe88ff144b0245. This package does not change DOCX bytes, declare formal acceptance, or substitute for human review.