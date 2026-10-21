# DOCX 0106 / I18-E14 / project item 115 — source-ready work lane

**Current state: source package verified and synced; manuscript generation pending. No DOCX candidate exists yet.** Project item 115 is a sequence index, not a printed official checkbox serial. Formal acceptance is not granted.

## Source binding

- 142-series crosswalk: `I18-E14` → document `0106`.
- Official PDF: page 7; SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Project 157 index: `I18-L3`, item 115, financial effect with before/after calculation and limitations.
- SOURCE_PACKET raw SHA-256: `6e39bdeff9c8f0955aca5c382346bdd4d897cb7c1a9d22a4a2e438632b333238`.
- UNIQUE_BLUEPRINT raw SHA-256: `dad70f1d1772ed20636d50956e3464aa9ac6918df242f7f11cb5a12f0b63a97d`.
- All association finance and respondent facts remain `UNKNOWN`; only the fixed synthetic worked case may be used.

## OpenCode writer dispatch

Requested model: `opencode/mimo-v2.6-flash-free`; actual provider billing and serving-model identity remain `UNKNOWN` until returned metadata supports a conclusion. No paid model, fallback, Computer Use, or file edits were authorized.

- Attempt 1 used the `plan` agent, whose native system rule prohibited implementation. The session returned zero tokens and no manuscript.
- Attempt 2 switched the same session to `build`, but no continuation user message was recorded; zero tokens and no manuscript. Only that owned CLI client was stopped; the existing OpenCode service was preserved.
- Attempt 3 is the only current writer process: PID `15384`, OpenCode session `ses_e9f9a27baffeOVEvJCqeg08qPn`, agent `build`. At last readback the session contained the full prompt, but no assistant response or token usage. This is pending, not a successful writer result.

Original CLI stdout/stderr, native session exports and correction receipts are under `writer/`. Do not dispatch another writer for 0106 while PID 15384 remains active.

## Acceptance gates

No Word file is created until a complete writer manuscript is recovered and its sample calculations are recomputed. A DOCX candidate then requires the project's technical, visual and independent exact-SHA review gates. `SAMPLE/SYNTHETIC` can never be upgraded to association results without authorized source evidence.
