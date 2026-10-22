# TTQS ONE candidate: 0100 / I18-E08

- State: CANDIDATE; formal acceptance NOT GRANTED.
- Internal 157-item index: 109. Printed official checkbox number: UNKNOWN. Do not conflate either with DOCX ID 0100.
- Unique Blueprint: `source/UNIQUE_BLUEPRINT_0100_I18-E08_R08.md` (local SHA-256 `16095B5BBE2F70C8BDD26408195134F561F7AE5BD62830FD6351E3D1709DA38C`).
- Source packet: `source/SOURCE_PACKET_I18-E08_0100_0101_R08.md` (local SHA-256 `55A4BB4503E807480E58A19DE2E505EB07985624FF4130A05370B064DBFB8B9A`).
- Candidate DOCX SHA-256: `1563f89a1b83119c5f7c57a21cbf6b89cc0c213231c5d12f90fc4d58fa06039e` (58,798 bytes).
- Word-native PDF SHA-256: `c27271ef7fa7d973ddbb34c653ea19a0b4098a1a167e1731da97649523a66ac4` (16 pages).
- Technical QA: pass; OOXML ZIP integrity, 17 tables, full 8×5×2 synthetic fixture (80 score cells), totals 75→117, net +42, mean delta +5.25.
- Visual QA: pass, all 16 pages inspected individually. One non-blocking whitespace observation on page 13.
- Independent semantic review: `PASS_SEMANTIC_EXACT_SHA`, bound to this exact DOCX SHA. Reviewer inspected the full extracted candidate text plus official requirement, source packet and Blueprint; visual pages and 0101-side agreement were outside that semantic review scope. Three recorded observations are non-blocking; no mandatory semantic repair.
- Synthetic/real boundary: all sample measurements are synthetic; no association approval, real learner record, formal acceptance, or external result is claimed.
- Adjacent DOCX 0101 is a separate I18-E08 artifact. Current local SHA-256 `56f433e095f32378f2fd8241c1a27948d2bfe6748da003af5623d265885edb68`; its prior GitHub R09 candidate is tracked separately and was read from the current branch during this run (remote Git blob SHA-1 `94624ae436571dba496f42dec10996baa4109a63`). It is not rebuilt or replaced by 0100 R10.

## Worker provenance

- OpenCode v2 Writer selected/requested the free `deepseek-v4.1-flash-free` route, returned four copy patches, and exited 0. Exact provider-serving model remains UNKNOWN. The patches were adopted after Codex content arbitration; this worker did not directly edit the DOCX.
- Antigravity was asked for `gemini-3.8-flash-high`; the native runtime log says the ID was absent from local config and it defaulted to CCPA. The returned text was NOT ADOPTED; Gemini use is not verified. Token counts are copied from the CLI response; provider billing remains UNKNOWN.
- The first OpenCode semantic-review launch exposed a console because Codex omitted `-WindowStyle Hidden`; this was a launch error, not a scheduler requirement. The stalled process was stopped; the same review session was resumed in hidden mode with redirected logs and returned the semantic verdict. See the incident receipt.

This package preserves candidate and formal acceptance as separate states. No protected originals or real personal records are included.
