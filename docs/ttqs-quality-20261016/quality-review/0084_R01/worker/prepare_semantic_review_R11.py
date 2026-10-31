from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn


BASE = Path(__file__).resolve().parents[1]
DOCX = BASE / "candidate" / "0084_R11.docx"
SOURCE = BASE / "inputs" / "SOURCE_PACKET_0084_R01.md"
BLUEPRINT = BASE / "inputs" / "UNIQUE_BLUEPRINT_0084_R03.md"
BODY = BASE / "candidate" / "0084_R10_body.md"
UPSTREAM = BASE.parent / "0083_R01" / "candidate" / "0083_R02_body.md"
REGISTER = BASE / "evidence" / "synthetic_replacement_register_R10.csv"
TECHNICAL = BASE / "evidence" / "technical_review_R11.json"
VISUAL = BASE / "evidence" / "visual_review_R11.json"
PREVIOUS_REVIEW = BASE / "review" / "independent_semantic_review_R09.md"
REVIEW_DIR = BASE / "review"
TEXT_OUT = BASE / "evidence" / "docx_extracted_R11.md"
PACKET_OUT = REVIEW_DIR / "semantic_review_packet_R11.md"
PROMPT_OUT = REVIEW_DIR / "semantic_review_prompt_R11.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


REVIEW_DIR.mkdir(parents=True, exist_ok=True)
doc = Document(str(DOCX))
lines: list[str] = []
counts = {"paragraphs": 0, "tables": 0, "table_rows": 0}
for child in doc.element.body.iterchildren():
    if child.tag == qn("w:p"):
        text = "".join(t.text or "" for t in child.findall(".//" + qn("w:t"))).strip()
        if text:
            counts["paragraphs"] += 1
            lines.append(text)
    elif child.tag == qn("w:tbl"):
        counts["tables"] += 1
        for row in child.findall(qn("w:tr")):
            counts["table_rows"] += 1
            cells = []
            for cell in row.findall(qn("w:tc")):
                text = "".join(t.text or "" for t in cell.findall(".//" + qn("w:t"))).strip()
                cells.append(text.replace("\t", " ").replace("\n", " / "))
            lines.append("\t".join(cells))
candidate_text = "\n".join(lines).strip() + "\n"
TEXT_OUT.write_text(candidate_text, encoding="utf-8")

upstream_text = UPSTREAM.read_text(encoding="utf-8")
start = upstream_text.find("## 8. 完整合成案例 SYN-0083-B01")
end = upstream_text.find("### 8.4", start)
if start < 0 or end < 0:
    raise RuntimeError("Could not isolate 0083 case §§8.1–8.3")
upstream_excerpt = upstream_text[start:end].strip()

docx_sha = sha256(DOCX)
text_sha = sha256(TEXT_OUT)
source_text = SOURCE.read_text(encoding="utf-8")
blueprint_text = BLUEPRINT.read_text(encoding="utf-8")
register_text = REGISTER.read_text(encoding="utf-8-sig")
previous_review = PREVIOUS_REVIEW.read_text(encoding="utf-8")
technical_text = TECHNICAL.read_text(encoding="utf-8")
visual_text = VISUAL.read_text(encoding="utf-8")

prompt = f"""Review the complete attached packet as an independent exact-SHA semantic review of DOCX 0084 R11. Do not edit files, call Computer Use, or draft replacement content.

Exact target: `DOCX 0084 / I17C-E03 / official checkbox serial 090`.
Candidate DOCX SHA-256: `{docx_sha}`.
Packet SHA-256: recorded in the separate request receipt after packet generation.

Return exactly one semantic verdict: `PASS`, `PARTIAL`, or `FAIL`. Assess the actual candidate text against the included official source packet and complete Unique Blueprint R03. Cite each finding to exact section, table, Form-O field, or REG_ID and state the practical consequence.

Required checks:
1. Correct genre and requirement identity: supervisor/observer workplace behavior observation scale and feedback; distinguish document 0084 from 0082, 0083, 0090 and institutional 17d.
2. Recheck the previous R09 P1 finding against R11 exact text and Blueprint §2.3: prohibited approval-token wording in blank Form-O O-01, and agreement between §5.1 and §15.2.
3. Recheck previous R09 P2 against the current R03 Blueprint and R11 exact text: all synthetic case atoms covered by the 59-row replacement register; verify O-08 for O0-O3 and O-16/O-17/O-18 at O0/O1/O2/O3, contiguous IDs, exact row coverage and actionable real-source/authorization requirements. Do not carry forward old 46-row counts or old verdicts.
4. Recheck previous R09 P3: does §0.4 now provide a usable end-to-end observation workflow with concrete steps and HOLD/RETURN/REVERIFY gates?
5. Practical completeness: B1-B4 behavior anchors, blank Form-O, complete O0-O3 demonstration, sources/locators, N/O and disagreement handling, feedback, learner response, next steps, HOLD/RETURN/REJECT rules, and arithmetic.
6. Cross-document consistency against the included 0083 §§8.1-8.3 source excerpt: SYN-0083-B01, LRN-B01, course code, dates, counts, AID-01/AID-02, pending locator and authorization. Check that synthetic 0084 additions are not represented as 0083 evidence.
7. SAMPLE/SYNTHETIC/PROPOSED versus REAL boundary; no fabricated person, credential, signature, association execution, approval, official score, or third-party original. Keep institutional 17c 0-3 unscored and separate from the proposed individual scale.
8. Title-blind recognizability and whether a volunteer-association training administrator and evaluator can use the instructions and forms without guessing missing rules.

Review the exact candidate text included below; do not infer unseen content. The technical and visual receipts are supplementary evidence only, not semantic acceptance. The prior R09 review is historical and applied to another DOCX SHA; use its findings only as targeted questions, then independently judge R11. If the packet is incomplete, say so and return PARTIAL/UNKNOWN rather than guessing. State review scope and limitations. The candidate remains not formally accepted.
"""
PROMPT_OUT.write_text(prompt, encoding="utf-8")

with zipfile.ZipFile(DOCX) as archive:
    bad_member = archive.testzip()
if bad_member:
    raise RuntimeError(f"DOCX ZIP corruption: {bad_member}")

packet = f"""# Exact-SHA independent semantic review packet — DOCX 0084 R11

Target identity: `0084 / I17C-E03 / official checkbox 090`.
Candidate DOCX SHA-256: `{docx_sha}`.
Extracted final Word text SHA-256: `{text_sha}`.
Candidate state: `CANDIDATE / NOT_EXECUTED`; `REAL=UNKNOWN/HOLD`; `FORMAL_ACCEPTANCE=NOT_GRANTED`.
Extracted DOCX structure: {counts['paragraphs']} nonempty paragraphs, {counts['tables']} tables, {counts['table_rows']} table rows. ZIP test: PASS.
Source packet SHA-256: `{sha256(SOURCE)}`.
Unique Blueprint R03 SHA-256: `{sha256(BLUEPRINT)}`.
R10 source body SHA-256: `{sha256(BODY)}`.
0083 R02 body SHA-256: `{sha256(UPSTREAM)}`.
Replacement register CSV SHA-256: `{sha256(REGISTER)}`.
Technical receipt SHA-256: `{sha256(TECHNICAL)}`.
Visual receipt SHA-256: `{sha256(VISUAL)}`.

## Review instructions

{prompt}

## Official source packet

{source_text}

## Complete Unique Blueprint R03

{blueprint_text}

## Cross-document source: 0083 §§8.1–8.3

{upstream_excerpt}

## Current 59-row synthetic replacement register

```csv
{register_text.rstrip()}
```

## Previous R09 independent review (historical, different SHA)

Historical target SHA was `1a0fdd4b7001f4ccf3462b9e7db19f3fabd7b20c2d457805bd8b53df84fadf37`. Its PARTIAL verdict does not apply to R11. Findings P1/P2/P3 are included solely as targeted regressions to recheck.

{previous_review}

## Current deterministic technical receipt

```json
{technical_text.rstrip()}
```

## Current visual receipt

```json
{visual_text.rstrip()}
```

## Candidate text extracted from the exact R11 DOCX above

{candidate_text}
"""
PACKET_OUT.write_text(packet, encoding="utf-8")

receipt = {
    "schema": "TTQS_ONE_0084_SEMANTIC_REVIEW_REQUEST.v1",
    "revision": "R11",
    "route": "OpenCode CLI v2",
    "candidate_docx": str(DOCX.relative_to(BASE)),
    "candidate_docx_sha256": docx_sha,
    "candidate_text_sha256": text_sha,
    "packet": str(PACKET_OUT.relative_to(BASE)),
    "packet_sha256": sha256(PACKET_OUT),
    "prompt": str(PROMPT_OUT.relative_to(BASE)),
    "prompt_sha256": sha256(PROMPT_OUT),
    "source_packet_sha256": sha256(SOURCE),
    "blueprint_r03_sha256": sha256(BLUEPRINT),
    "register_csv_sha256": sha256(REGISTER),
    "technical_receipt_sha256": sha256(TECHNICAL),
    "visual_receipt_sha256": sha256(VISUAL),
    "previous_review_sha256_historical": sha256(PREVIOUS_REVIEW),
    "cross_document_0083_body_sha256": sha256(UPSTREAM),
    "candidate_zip_test": "PASS",
    "candidate_text_extraction_counts": counts,
    "dispatch_policy": "One bounded independent semantic review; no retries if the free route returns a service/account error.",
    "status": "PACKET_READY_NOT_YET_DISPATCHED",
}
request_path = REVIEW_DIR / "opencode_semantic_R11_request.json"
request_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
