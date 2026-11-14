# TTQS ONE targeted copy patch task

WORK_ID=TTQS-I18E08-DOC0100-R10-OPENCODE-WRITER-20261022-01
DOC_ID=0100
REQUIREMENT=I18-E08 (project internal index 109; official printed serial remains UNKNOWN)
ROLE=TARGETED_COPY_PATCH_PROPOSAL
BASE_DOCX_SHA256=debd41e7ca1b18b88cad37db118c5b3474df411b3e2d1c87a8351d456245e0b2

Return a concise JSON proposal containing exact Traditional Chinese replacement text for only the specific passages needed to resolve the four findings in the attached independent review of the exact base SHA. Do not rewrite the manuscript or change the eight-person synthetic data. Do not create/edit files, call tools, or propose a Word export. Do not claim review acceptance or real association actions. If facts are insufficient, return a precise blocker instead of inventing.

Authoritative boundaries:
- DOCX 0100 is a learner-facing five-dimension pre/post self-assessment form under official I18-E08; it is not the separate 0101 perceived-growth radar report, a skills rubric, a satisfaction form, or an official pass/fail instrument.
- Official form page is p.7; internal index 109 is not the official checkbox number.
- Keep all eight paired synthetic cases A01–A08 and all 80 original score cells unchanged: pre total 75; post total 117; net +42; n=8; mean paired change +5.25. These are SAMPLE/SYNTHETIC only, not association data, participant identities, measured effectiveness, or approval.
- The current exact-SHA semantic review was PASS_SEMANTIC_ONLY with four explicit findings. The current Word front matter has a stale engineering label R09a and says no independent review; any replacement must stay candidate-only and must not say formally accepted. Prefer neutral reader-facing version wording without engineering revision IDs.
- Preserve the no-imputation rule and never infer a person from handwriting, response style, birthday, or identifying data. Never use birthdays or other PII to generate codes.
- The CSV header was directly checked and has no leading spaces. Do not edit or recommend changing CSV headers.

Required finding handling:
1. Pairing: identical four-digit codes alone do not prove that the same human answered both forms. Use a privacy-preserving operational process that records no names or identity key, prevents/flags duplicate codes within each phase, and explains exactly when a pre/post pair may enter 0101. Any collision, mismatch, wrong version, or unresolved ambiguity must be HOLD, then REJECT/exclude if unresolved. Do not use handwriting/style comparison or identity checks. State plainly that even a valid anonymous code pair is a protocol-linked pair, not independent identity verification.
2. Privacy QC: operational checklists must explicitly prevent or isolate employer, commissioning organization, service-recipient/client, and other direct or indirect organization-identifying details in free text. Give usable handling steps that preserve privacy and do not publish real originals.
3. Front matter: remove engineering labels such as R09/R09a/R10 from the human-facing form. Replace the inaccurate “no independent review” status with neutral truthful wording: SAMPLE candidate, no real learner responses, not formally submitted/accepted; review evidence belongs to a separate receipt and the document itself does not claim approval.
4. Data-quality terms: use the clear phrase “四位數字” consistently; never suggest birthday. Distinguish (a) blank/missing response, (b) out-of-range value outside 0–4/unclear mark, (c) multiple selections. For each define first-step HOLD/correction only while the respondent is available and can confirm their own response without identity logging; otherwise REJECT the affected form/item and exclude it. Never impute or have staff guess a score.

Return JSON schema:
{
  "work_id": "TTQS-I18E08-DOC0100-R10-OPENCODE-WRITER-20261022-01",
  "doc_id": "0100",
  "base_docx_sha256": "...",
  "patches": [
    {"finding_id":"F1", "destination":"exact section/table", "replacement_text":"...", "rationale":"..."},
    {"finding_id":"F2", ...},
    {"finding_id":"F3", ...},
    {"finding_id":"F4", ...}
  ],
  "blocked": []
}
No prose outside JSON.
