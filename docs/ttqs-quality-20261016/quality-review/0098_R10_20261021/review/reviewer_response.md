```json
{
  "verdict": "PASS",
  "candidate_sha256": "6310a71f6fb540b22572f823e7becb7a8198c12dc068eebff2794599e5a88152",
  "requirement": "I18-E06 (satisfaction survey system/process)",
  "scope": "Bounded R08→R10 semantic delta only: the single changed user-facing paragraph in §8.2.1 of 0098_R10.docx, read against the packet-quoted R10 text and the stated unchanged adjacent pre-flight instructions. Not a full rereview, not layout verification, not register re-verification, not formal acceptance.",
  "findings": [
    {
      "id": "F1",
      "question": 1,
      "locator": "0098_R10.docx §8.2.1, sole changed paragraph, sentence 1: 「示範資料替換清冊：在同一交付套件的「evidence」資料夾開啟「SYNTHETIC_REPLACEMENT_REGISTER.csv」。」",
      "severity": "none",
      "rationale": "The pointer is package-relative (\"同一交付套件的「evidence」資料夾\") plus a bare filename, with no drive letter, user profile, repository path, or Git/Windows-specific construct. A human opening a normal delivery package can follow it without local-path knowledge. This directly corrects the R08-lineage nonportable internal path."
    },
    {
      "id": "F2",
      "question": 2,
      "locator": "0098_R10.docx §8.2.1 changed paragraph, sentences 2–3, read together with the unchanged adjacent pre-flight instructions (R10-document/R10-register identity, 192 rows, no duplicate codes, pause on absence/mismatch, SAMPLE replaced only from lawful verified REAL source, otherwise UNKNOWN/HOLD).",
      "severity": "none",
      "rationale": "Mismatch remains a stop condition rather than an auto-proceed: identity/count/code checks precede use, and any absence or mismatch triggers pause. The SAMPLE/REAL boundary is explicit — 「示範事實」 are labeled demonstration facts and are 「只用來逐筆核對日後取得的真實來源」, which instructs later comparison against REAL source rather than asserting that real records exist or that any association is established. No wording in the changed paragraph upgrades SAMPLE into REAL evidence."
    },
    {
      "id": "F3",
      "question": 3,
      "locator": "0098_R10.docx §8.2.1 changed paragraph versus R08/R09 body text for the same passage.",
      "severity": "none",
      "rationale": "Removing the embedded register SHA from user-facing prose is an editorial relocation, not a semantic loss: per the packet the exact hash is retained in sidecar receipts, and the user-facing obligation (open this file, it has 192 demonstrably-coded entries, use only for later REAL cross-check) is preserved verbatim in substance. No instruction, boundary, or hold condition is dropped from the user-facing layer. Given the stated unchanged remainder and the R08 PASS within its recorded body-text/register scope, this delta introduces no material semantic regression in the changed section."
    },
    {
      "id": "F4",
      "question": 4,
      "locator": "0098_R10.docx §8.2.1 changed paragraph, clause 「每筆都有唯一代碼」.",
      "severity": "observation (non-blocking, not a text defect)",
      "rationale": "This is a claim about the register's contents. The packet binds the register SHA-256 and records 192 unique rows, and the adjacent pre-flight requires a no-duplicate-code check, but the packet does not explicitly report that code uniqueness itself was confirmed on the bound R10 register. Confirm at pre-flight against the bound register; this does not invalidate the paragraph's locatability, hold behavior, or SAMPLE/REAL framing, so it does not change the verdict."
    }
  ],
  "new_repair_required": false,
  "limitations": [
    "I did not open, render, inspect, or independently hash 0098_R10.docx or any register file; no tools or file operations were used. The R10 candidate SHA-256 and manuscript SHA-256 are accepted solely as binding values supplied by local technical evidence, not as my own measurement.",
    "Layout, pagination, clipping/overlap, and official printed serial were outside this delta review. The packet's Word/PDF inspection was sampled at full size (pages 2, 14, 28, 29 of 29), not every page at original scale.",
    "The adjacent §8.2.1 pre-flight instructions are available to me only as the packet's paraphrase, not verbatim; F2 therefore relies on that characterization, including the precise HOLD wording.",
    "Physical packaging is unverified: the paragraph's correctness assumes SYNTHETIC_REPLACEMENT_REGISTER.csv is actually shipped in the same delivery package's evidence folder. A SHA binding alone does not establish file placement.",
    "The R08 independent semantic PASS (OpenCode v2, response SHA-256 bd82f9eb…) is preserved only within its recorded scope — body text/register, excluding layout, official printed serial, and REAL originals — and is not extended to changed content or to files outside that scope.",
    "This is a bounded semantic delta judgment only; it is not formal acceptance, not a REAL-evidence finding, and not authorization to treat SAMPLE content as verified REAL data."
  ]
}
```
