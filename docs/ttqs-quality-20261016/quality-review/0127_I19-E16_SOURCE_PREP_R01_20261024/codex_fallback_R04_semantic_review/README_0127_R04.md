# 0127 / I19-E16 — R04 candidate and delegated review record

## State

`CANDIDATE_NOT_FORMALLY_ACCEPTED`. This package does not establish REAL evidence, association approval, or formal acceptance.

## Exact artifact pins

- Candidate DOCX SHA-256: `d374fa890072edfbad55542b56fb43df22aeac6db51e3f9d2164ab2f0f82ae03` (121,740 bytes)
- Paired synthetic replacement CSV SHA-256: `d5eb3b91ecc83d4e76b831804f85d0e5f81b24e5f66d8a7853aaebc475803b88` (16,321 bytes)
- Extracted body SHA-256: `00b009b1b9c2a24758372f44e3d70824bc4cba8dd4a2214d0ec213e18d69c632`
- Official source packet SHA-256: `058663e200fd0207196c08a02e4d159c6e3eaa7f167094cd7b409b4050b18675`
- Unique Blueprint SHA-256: `9a249a2e398407469bd82c9bf5d7a6188c9e3d28be79172bd4cc33b213c700ff`

## Delegated work

- **W1 OpenCode v2** (`opencode/iceman-free` requested): native session export recovered the response, but exact validation rejected it because its body-text SHA-256 differed from the candidate extraction by one character. W1 is not counted as semantic PASS. The recovered response and rejection receipt are preserved under `worker_review/W1_OPENCODE_ICEMAN_R01_20261115/`.
- **W2 Antigravity CLI 1.5.9** (`gemini-3.8-flash-high` requested): attempt 6 reached the model, exited 0 after 64.789 seconds, and returned a full-body semantic/usability review. All eight checks were PASS, findings were empty, and the response, raw stdout, validator, manifest, and candidate hashes bind exactly. Recorded usage: 29,966 input + 6,183 output + 5,548 thinking = 36,149 tokens. Tool calls: 0.
- The Antigravity **requested model** is recorded as `gemini-3.8-flash-high`; the **actual serving model remains UNKNOWN**. No claim of provider-side model identity is made.
- W2 scope is text semantic/usability review only. It did not perform visual QA, verify REAL evidence, or grant formal acceptance. Its packet SHA-256 and stdin payload SHA-256 are preserved in the manifest/dispatch receipts; the exact W2 stdin payload bytes were not separately archived.

## Other quality evidence

- The visual receipt and rendered evidence cover 18 pages; spot-check pages 7, 8, 12, and 18 are recorded in the receipt. Body/table font floors are 10.5/9.5 pt.
- The static QA and content extraction receipts are included as source records. This README does not elevate their scope or state.
- All example values remain SAMPLE/SYNTHETIC and are paired with the replacement register. No third-party original or real-world performance is asserted.

## Source lineage

The source and Blueprint hashes match the exact source pins already recorded in the adjacent R02 source-preparation package. Historical R02 candidate/review files remain untouched.
