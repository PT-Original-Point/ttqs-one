# Antigravity CLI route incident — 0044 R01

- **Route:** Antigravity CLI 1.4.0; executable SHA-256 `f5466e6aaf9f1345cae476fecb9aebb9e82c2ca8dfd43136fa9747fcf075e062`.
- **Requested model/effort:** `gemini-3.8-flash-high` / `high`; runtime model identity was not returned.
- **Review target:** DOCX 0044 / I09-E04 / checkbox 045; exact candidate SHA `76bde5df4209abc6f102a15a02c5e51a5816ef3df309aaed0a0ab44ea9075644`.
- **Outcome:** four headless permission denials, three scoped repairs, zero reviewer response, no semantic verdict. Route status is `PAUSED_NEW_DISPATCH` under the Human three-error/three-repair rule.
- **Safety and file integrity:** no Computer Use, no `--dangerously-skip-permissions`, candidate SHA unchanged across all four attempts; temporary scoped read rules were removed by restoring the original settings bytes.

| Attempt | Denied action | Scoped correction before attempt | Exit | Response | stdout SHA-256 | stderr SHA-256 |
|---:|---|---|---:|---:|---|---|
| 1 | command | Initial attempt; no prior repair. | 0 | 0 chars | `f26f08be166b19eb9b1417cf3750c612957a6cb9bfa3277bac97c9e0878c3719` | `6f9b232ca1f3b43aa72e2ba63698c09b0796b612d5a17cf05efee31e6c79b713` |
| 2 | read_file | Repair 1: revised the prompt to forbid RunCommand/shell and require native read-only file/image inspection, otherwise PARTIAL/UNKNOWN. | 0 | 0 chars | `df2db049e7ce88604b913c618a9bd5245159ada55e8491dca71ab0bfc82191d1` | `2f70f945243833d446f0501960769e51d4aabe7f6b4f4f502a24883d197ccc06` |
| 3 | read_file | Repair 2: temporarily added a recursive read_file allow rule scoped to the retry packet absolute Windows directory. | 0 | 0 chars | `8d3a62bdcfc63de4d09f767e786068f72ceffa6cc0c37af603b2cba34ceace03` | `2f70f945243833d446f0501960769e51d4aabe7f6b4f4f502a24883d197ccc06` |
| 4 | read_file | Repair 3: temporarily added five normalized forward-slash read_file rules scoped to the candidate, inputs, evidence, prompt, and packet manifest. | 0 | 0 chars | `67597210d63c2b025dc6da52d0d302f87f70a78478a75af12db7a6789d68fab1` | `2f70f945243833d446f0501960769e51d4aabe7f6b4f4f502a24883d197ccc06` |

Each `attempt_NN/` directory preserves the raw stdout/stderr, execution receipt, exact prompt and packet manifest. `packet_reconstruction_check.json` verifies every immutable packet input against the public parent candidate/source/evidence files. All checks passed. The CLI transport-level `SUCCESS` with exit 0 is not a review result: the model response was empty and `denied_actions` records the blocked tool.

The candidate remains `CANDIDATE / NOT_PROMOTED`; independent semantic review is pending. Keep the DOCX bytes fixed. Continue other lawful READY documents; resume this review only after the read-only CLI path has been reliably corrected.
