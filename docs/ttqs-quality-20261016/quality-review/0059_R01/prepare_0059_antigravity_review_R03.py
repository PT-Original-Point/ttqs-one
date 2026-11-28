from __future__ import annotations

import hashlib
import json
from pathlib import Path

from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "docs" / "ttqs-quality-20261016" / "quality-review" / "0059_R01"
DOCX = BASE / "0059_R03.docx"
BLUEPRINT = BASE / "worker" / "opencode" / "0059_UNIQUE_BLUEPRINT_R01_DRAFT.md"
PACKET_SPEC = BASE / "inputs" / "0059_CONTENT_WRITER_PACKET_R01.md"
BLUEPRINT_SPEC = BASE / "inputs" / "0059_BLUEPRINT_WRITER_PACKET_R01.md"
PDF = BASE / "evidence" / "render_final_0263017F" / "0059_R03.pdf"
OUT_DIR = BASE / "review" / "antigravity_semantic_R03"
OUT = OUT_DIR / "review_packet_R01.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def iter_blocks(document):
    for child in document.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, document)
        elif isinstance(child, CT_Tbl):
            yield Table(child, document)


def clean_cell(text: str) -> str:
    return "<br>".join(part.strip().replace("|", "\\|") for part in text.splitlines() if part.strip())


def extract_docx(path: Path) -> tuple[str, int, int]:
    document = Document(path)
    blocks: list[str] = []
    paragraph_count = 0
    table_count = 0
    for block in iter_blocks(document):
        if isinstance(block, Paragraph):
            text = block.text.strip()
            if not text:
                continue
            paragraph_count += 1
            style = block.style.name if block.style else ""
            if style.startswith("Heading"):
                try:
                    level = int(style.rsplit(" ", 1)[-1])
                except ValueError:
                    level = 2
                blocks.append(f"{'#' * max(2, min(level + 1, 6))} {text}")
            else:
                blocks.append(text)
        elif isinstance(block, Table):
            table_count += 1
            rows = [[clean_cell(cell.text) for cell in row.cells] for row in block.rows]
            width = max((len(row) for row in rows), default=0)
            if not width:
                continue
            rows = [row + [""] * (width - len(row)) for row in rows]
            blocks.append("\n".join([
                "| " + " | ".join(rows[0]) + " |",
                "| " + " | ".join(["---"] * width) + " |",
                *["| " + " | ".join(row) + " |" for row in rows[1:]],
            ]))
    return "\n\n".join(blocks) + "\n", paragraph_count, table_count


OUT_DIR.mkdir(parents=True, exist_ok=True)
body, paragraph_count, table_count = extract_docx(DOCX)
body_bytes = body.encode("utf-8")
official_sha = "805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709"
contract_commit = "f6199a09dffe9211870c3e765c00ceb6f4a55be6"
candidate_sha = sha256(DOCX)
pdf_sha = sha256(PDF) if PDF.exists() else "NOT_FOUND"
blueprint_sha = sha256(BLUEPRINT)
packet_spec_sha = sha256(PACKET_SPEC)
blueprint_spec_sha = sha256(BLUEPRINT_SPEC)

header = f"""# Antigravity exact-SHA semantic review packet — DOCX 0059 R03

## Review identity and evidence binding
- Project: TTQS ONE; state: CANDIDATE / SAMPLE-SYNTHETIC; no formal acceptance is asserted.
- Candidate DOCX: `{DOCX}`
- Candidate DOCX SHA-256: `{candidate_sha}`
- This packet contains a deterministic text extraction from that exact DOCX; extracted UTF-8 text SHA-256: `{hashlib.sha256(body_bytes).hexdigest().upper()}`
- DOCX body counts: {paragraph_count} non-empty paragraphs; {table_count} tables.
- Rendered PDF SHA-256: `{pdf_sha}`; Word COM render; {len(list(PDF.parent.glob('page-*.png')))} rendered page PNG files exist in the current SHA-versioned render directory.
- Source contract revision: repository commit `{contract_commit}`; formal source and document mapping are included below.
- Unique Blueprint draft SHA-256: `{blueprint_sha}`. Blueprint-authoring packet SHA-256: `{blueprint_spec_sha}`. Content-writing packet SHA-256: `{packet_spec_sha}`.
- Official Workforce Development Agency source SHA-256: `{official_sha}`.

## Independent reviewer instructions
Review the candidate content below against the official requirement and design contract. This is an independent semantic review, not formal acceptance and not authorization to edit the DOCX. Do not use Computer Use, external tools, or infer unavailable facts. Do not trust Builder self-reports. Give PASS / PARTIAL / FAIL separately for requirement fit, genre, operational usability, completeness, SAMPLE/REAL boundary, numerical consistency, cross-document separation, and human readability. Every finding must cite a heading, table name/row, or a short exact locator from the extracted candidate. If evidence is insufficient, say UNKNOWN or PARTIAL rather than guessing. Report material omissions and concrete repair requirements. State explicitly whether the exact candidate SHA above is the reviewed SHA represented by this packet, and state limitations: the packet is a text extraction; rendered page visual inspection is a separate QA scope.

## Formal identity and official requirement
- DOCX deliverable ID: 0059.
- Requirement: I13-E03.
- Official checkbox serial: 063. It is not the DOCX ID. Checkbox 060 is a separate unnamed “Other” item and is not this document.
- Official indicator I13, training-institution evidence table pages 4–5.
- Official requirement text: “提供行動計畫、競賽、回訓、學習心得交流的平台、證照、實習或其他相關機制的建議或協助，促進訓練成果移轉的達成並展現適當資料說明。”
- Official source: Taiwan Workforce Development Agency, TTQS Evidence Reference Table, training-institution version, 9 pages. Source URL: https://ttqs.wda.gov.tw/download_files/6475978659d646f58e3eddc3b1ea51d9/TTQS%E6%9F%A5%E6%A0%B8%E4%BD%90%E8%AD%89%E6%96%87%E4%BB%B6%E8%B3%87%E6%96%99%E8%A1%A8-%E8%A8%93%E7%B7%B4%E6%A9%9F%E6%A7%8B%E7%89%88.pdf
- Adjacent documents: 0057 / I13-E01 / checkbox 061 is macro transfer review; 0058 / I13-E02 / checkbox 062 is individual action plans and team/organization performance; 0056 / I12-E04 / checkbox 059 is facility/equipment evidence. 0060 is “Other” checkbox and is not 0059.
- Correct genre: a usable operational evidence package showing the distinct mechanisms of retraining, learning-reflection exchange, certification registration/verification, and supervised simulated practice/internship pathway, with complete examples, transfer assessment and lawful real-evidence replacement controls. It must not become a generic SOP, meeting report, personal action plan, facility inspection packet, reflection essay alone, or credential list.

## Context and evidence-boundary contract
The Association is a small volunteer nonprofit and its current operations, staff, authority, learners, actual training, certificates, partners, activities and results remain UNKNOWN unless supported by authorized source records. All facts below are explicitly SAMPLE/SYNTHETIC. Do not describe synthetic outcomes as Association approvals, REAL practice or third-party verification. Do not invent real people, issuers, certificates, signatures, consent, partners, external replies, authorization, or legal conclusions. Real source originals, privacy/consent, verification, safe placement and authorization must remain HOLD/UNKNOWN until obtained.

## Required semantic checks
1. Exact mapping 0059 = I13-E03 = checkbox 063; compare against neighbors 0057/061, 0058/062, 0056/059 and distinct checkbox 060.
2. Four mechanisms separately complete and operational: (A) retraining/skill refresh; (B) learning-reflection exchange with consent and de-identification; (C) participant-reported certificates distinguished from independent issuer verification; (D) supervised simulated practice distinguished from REAL internship/placement.
3. Each example has sequence, fields, dates, counts, numerator/denominator, formula, result, decision, exception, follow-up and limitations.
4. Questionnaire: consent, full questions and choices, scale anchors, N/A and skip rules, timing after mechanisms, privacy, scoring and no causal/competence overclaim.
5. Skill rubric: five behaviorally anchored dimensions, assessor instruction, scoring threshold, safety/privacy hold, remediation and retest; retest excluded from first-test denominator.
6. Recompute survey, rubric and cross-mechanism values; assess denominator/nonresponse/N/A/deduplication rules and case/date consistency.
7. Assess realistic small-volunteer-association operation, role clarity, accessible records, rejection/hold criteria, lawful replacement map, NOT ADOPTED status, and whether an administrator/evaluator can use the document directly.
8. Assess readability and internal consistency from text; do not claim visual inspection. Visual QA is separately recorded by the production owner.

## Unique Blueprint draft (full source)
{BLUEPRINT.read_text(encoding='utf-8')}

## Content-writing packet (full source)
{PACKET_SPEC.read_text(encoding='utf-8')}

## Candidate DOCX extracted body — exact DOCX SHA above
{body}
"""
OUT.write_text(header, encoding="utf-8", newline="\n")
print(json.dumps({
    "packet": str(OUT),
    "packet_sha256": sha256(OUT),
    "docx_sha256": candidate_sha,
    "extracted_text_sha256": hashlib.sha256(body_bytes).hexdigest().upper(),
    "blueprint_sha256": blueprint_sha,
    "pdf_sha256": pdf_sha,
    "paragraphs": paragraph_count,
    "tables": table_count,
    "packet_bytes": OUT.stat().st_size,
}, ensure_ascii=False, indent=2))
