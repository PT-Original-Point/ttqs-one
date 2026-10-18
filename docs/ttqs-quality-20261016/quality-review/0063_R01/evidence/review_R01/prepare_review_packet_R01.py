from pathlib import Path
import csv, hashlib, json
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parents[2]
DOCX=ROOT/'candidate/0063_R01.docx'
BLUEPRINT=ROOT/'inputs/0063_UNIQUE_BLUEPRINT_R01.md'
MANUSCRIPT=ROOT/'inputs/0063_MANUSCRIPT_R01.md'
REGISTER=ROOT/'sidecar/0063_R01_SYNTHETIC_REPLACEMENT_REGISTER.csv'
BUILD=ROOT/'evidence/build_receipt_R01.json'
OUT=ROOT/'evidence/review_R01/0063_R01_SEMANTIC_REVIEW_PACKET.md'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def extract_docx(path):
    d=Document(path); out=[]
    body=d._element.body
    for el in body.iterchildren():
        if el.tag==qn('w:p'):
            p=Paragraph(el,d)
            if p.text.strip(): out.append(p.text)
        elif el.tag==qn('w:tbl'):
            t=Table(el,d)
            out.append('[TABLE]')
            for row in t.rows:
                vals=[cell.text.replace('\n',' / ').strip() for cell in row.cells]
                out.append(' | '.join(vals))
            out.append('[/TABLE]')
    return '\n'.join(out)

docx_sha=sha(DOCX); bp_sha=sha(BLUEPRINT); ms_sha=sha(MANUSCRIPT); reg_sha=sha(REGISTER)
build=json.loads(BUILD.read_text(encoding='utf-8'))
text=extract_docx(DOCX)
mission='''Relevant acceptance constraints from the current TTQS ONE Human Mission (Git blob 538bedb9d87e8465f43151933b4a5c1bfa4bbc4e):
- Every artifact must match the official named requirement and correct genre, with document-specific operational content, usable forms/processes, and clear sample/real separation.
- Do not claim association approval, real operations, signatures, or third-party evidence without a source. Keep unknown facts UNKNOWN.
- Avoid overlap with neighboring documents and keep exact official checkbox serial distinct from DOCX ID.
- Verify arithmetic, dates, cross-document links, human readability, and replacement evidence requirements.
- Technical or builder self-checks do not constitute independent semantic acceptance; the review must bind to the exact candidate content hash.
'''
review_instructions='''## Independent review task
You are a semantic reviewer independent of the OpenCode writer and deterministic builder. Review the complete DOCX body extraction below against the official source, current mission constraints, the complete document-specific Unique Blueprint, and replacement register. The DOCX SHA and extraction hash are supplied by the local runner; do not claim you recalculated the DOCX bytes or saw the page images. Do not edit, rebuild, or infer real execution.

Return a concise but evidence-rich Markdown report with:
1. Overall `PASS`, `PARTIAL`, or `FAIL` for semantic content only.
2. A verdict for each: official-purpose and three-code mapping; correct document genre; operational maturity/usability for a small volunteer association; complete forms/tables/workflow/decision and hold/reject criteria; sample-vs-real and authority boundary; cross-document facts and no extra 0061 index entry; arithmetic/date consistency; title-blind identification and negative-neighbor separation from 0060/0061/0062/0064; evidence replacement readiness.
3. For every PARTIAL/FAIL, give section/table row and exact excerpt or a concise locator, why it fails, and minimum correction. Do not turn unknown into pass.
4. State separately that visual page review was not in your input and is outside this semantic verdict.
5. State whether any hard rejection condition exists.

Check especially: 8 baseline and 8 retest tasks; baseline 5/8, 1/8, 2/8; retest 6/8, 8/8 within one clarification; +12.5 percentage points; zero result 0/8; no speed claims; permission denial is not search failure; 0061 remains one sample index entry; all actors and dates are synthetic/proposed; 2026-11-25 follow-up interval has an explicit valid anchor.
'''
packet='\n'.join([
'# TTQS ONE 0063 R01 — exact-candidate semantic review packet',
'',
'## Candidate identity and source hashes',
'- Project: TTQS_ONE',
'- DOCX ID: 0063',
'- Requirement: I14-E04',
'- Official checkbox sequence: 068 (not DOCX ID 0068)',
'- Official source: Taiwan Workforce Development Agency, TTQS Training Institution Evidence Checklist, p.5; the single relevant text is “是否提供查詢功能，並具持續改善機制。”',
'- Candidate status: SAMPLE/SYNTHETIC demonstration draft; not an association-approved or deployed procedure.',
'- DOCX SHA-256: `'+docx_sha+'`',
'- Extracted body text SHA-256: `'+hashlib.sha256(text.encode()).hexdigest()+'`',
'- Unique Blueprint SHA-256: `'+bp_sha+'`',
'- Manuscript SHA-256: `'+ms_sha+'`',
'- Replacement register SHA-256: `'+reg_sha+'`',
'- Build receipt candidate SHA-256: `'+build.get('candidate_sha256','UNKNOWN')+'`',
'',mission,review_instructions,
'## Cross-document facts and fixed boundary',
'- DOCX 0060 / I14-E01 / official box 065; exact candidate R08 SHA-256 `92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3`.',
'- DOCX 0061 / I14-E02 / official box 066; exact candidate R03 SHA-256 `3d4fe20f7fb825e470ed5dfd71fcaf0f5bb8052dc7a63ef51ee08e2a11668c9c`; exactly one sample index row, `F-0061-2026-0001`, source doc 0060 and case `SYN-0060-2026-A01`.',
'- DOCX 0062 / I14-E03 / official box 067; governs evidence-file list and original locations.',
'- DOCX 0064 / I14-E05 / official box 069; systemization and retrieval speed/performance. 0063 must not report speed or response-time claims.',
'- Existing 0060 synthetic source facts: case `SYN-0060-2026-A01`; course “社區志工接待與資源轉介界線”; date 2026-08-15; registered 12, attended 10, absent 2; source code `TT-2026-SYN60A-DO-ATT-RST-S3-006-V01`. These are inherited SAMPLE facts, not 0063-generated real records.',
'',
'## Complete Unique Blueprint',BLUEPRINT.read_text(encoding='utf-8').strip(),
'',
'## Synthetic replacement register',REGISTER.read_text(encoding='utf-8-sig').strip(),
'',
'## Exact DOCX body text extracted locally from the SHA above',text,
])
OUT.write_text(packet,encoding='utf-8')
print(json.dumps({'packet_path':str(OUT.relative_to(ROOT)),'packet_sha256':sha(OUT),'docx_sha256_before':docx_sha,'docx_sha256_after':sha(DOCX),'text_chars':len(text),'packet_chars':len(packet),'blueprint_sha256':bp_sha,'manuscript_sha256':ms_sha,'register_sha256':reg_sha},ensure_ascii=False))
