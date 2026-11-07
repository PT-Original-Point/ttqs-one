Done. Only `build/patch_0055_R04.py` was created; nothing was executed and no DOCX/CSV/receipt files exist.

## Deliverable
`0055_R04/build/patch_0055_R04.py` — one deterministic, stdlib-only script (AST-parsed clean; not run).

## What it does
- **DOCX (surgical OOXML, no python-docx):** verifies the R03 SHA-256, finds the escaped ranking-verification anchor (exactly once), locates its enclosing `<w:p>`, and inserts one new `<w:p>` immediately after it, cloning the anchor paragraph's `<w:pPr>` and the run's `<w:rPr>` so formatting is preserved. Repacks the ZIP reusing the original `ZipInfo` objects (member order/dates/compression preserved).
- **CSV:** replaces only the byte-identical `FAC-0055-010` line, keeping BOM, LF endings, header/column order, exactly 52 data rows, and all other bytes untouched; `evidence_status` stays `SYNTHETIC`.
- **Receipt:** exact input/output hashes, changed members (`word/document.xml`), changed row id, `candidate_only=true`, and explicit QA-not-run/no-claim flags.

## Key safety checks (fail closed)
- Exact input hashes for both DOCX and CSV; refuses to overwrite any output; enforces writing only under the task directory.
- Anchor must occur exactly once; insertion proven by prefix/suffix byte-equality (`dst == src[:p] + new + src[p:]`), inserted text unique, exactly one paragraph added.
- Package integrity + member-order equality; asserts the changed-member set is exactly `{word/document.xml}` and every other member's content is byte-identical.
- CSV schema validated (BOM, LF-only, header, 12 columns × 52 rows, unique target row matching expected R03 content, re-parse of candidate), plus byte-diff proof that only the one line changed.

## Assumption recorded
Per your clarification: the outer `「 」` in the packet are delimiters and are **excluded**; the inner `『專業內容正確性』`/`『教學示範與引導』` marks are kept verbatim. The `FAC-0055-010` fields were composed in Traditional Chinese to match the register's house style from the packet's semantic instructions (`locator` taken verbatim).

No PASS/approval/authority/activity is claimed.