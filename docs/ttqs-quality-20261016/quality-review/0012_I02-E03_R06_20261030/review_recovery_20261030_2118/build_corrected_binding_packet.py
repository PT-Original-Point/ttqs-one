
from pathlib import Path
from hashlib import sha256
import json
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table

base = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029")
docx_path = base / "candidate" / "0012_I02-E03_R06.docx"
source_path = base / "worker" / "luna_subagent_draft_R01_R06_scoped_repair.md"
register_path = base / "qa" / "R06_SCOPED_REPAIR_20261030" / "SYNTHETIC_REPLACEMENT_REGISTER_R06.csv"
tech_path = base / "qa" / "technical_qa_R06.json"
bp_path = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl")
official_dir = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES")
official_sha_expected = "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709"
expected_docx_sha = "f4c7a8242cb5ae0c4c038d546b2d45cac938028a521ea6ffcb5cc02334c03d13"
expected_bp_sha = "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e"
out = base / "qa" / "W1_SEMANTIC_REVIEW_R06_CORRECTED_BINDING_20261030"
if out.exists():
    raise SystemExit(f"Refusing to overwrite existing evidence folder: {out}")
for p in (docx_path, source_path, register_path, tech_path, bp_path):
    if not p.is_file():
        raise SystemExit(f"Missing required input: {p}")

def sha_bytes(b: bytes) -> str:
    return sha256(b).hexdigest()
def sha_file(p: Path) -> str:
    return sha_bytes(p.read_bytes())

docx_sha = sha_file(docx_path)
bp_sha = sha_file(bp_path)
if docx_sha != expected_docx_sha:
    raise SystemExit(f"Candidate drift: {docx_sha}")
if bp_sha != expected_bp_sha:
    raise SystemExit(f"Blueprint drift: {bp_sha}")

rows = []
for line in bp_path.read_bytes().splitlines():
    try:
        row = json.loads(line.decode("utf-8-sig"))
    except Exception:
        continue
    if row.get("deliverable_id") == "0012" and row.get("requirement_id") == "I02-E03":
        rows.append((line, row))
if len(rows) != 1:
    raise SystemExit(f"Expected one unique blueprint row, found {len(rows)}")
row_bytes, bp = rows[0]
row_sha = sha_bytes(row_bytes)

official = next((p for p in official_dir.glob("*.pdf") if sha_file(p) == official_sha_expected), None)
if official is None:
    raise SystemExit("Exact official source PDF not found")
tech = json.loads(tech_path.read_text(encoding="utf-8"))
if tech.get("artifact_sha256") != docx_sha or tech.get("technical_status") != "PASS":
    raise SystemExit("Technical receipt is not a PASS bound to the current candidate")
if tech.get("blueprint_row_sha256") != row_sha or tech.get("blueprint_file_sha256") != bp_sha:
    raise SystemExit("Blueprint binding mismatch")
if tech.get("official_requirement_pdf_sha256") != official_sha_expected:
    raise SystemExit("Technical receipt official source mismatch")
checks = tech.get("checks", {})
failed = [k for k,v in checks.items() if v is not True]
if failed:
    raise SystemExit(f"Technical receipt has failed checks: {failed}")

doc = Document(docx_path)
parts = []
for child in doc.element.body.iterchildren():
    if child.tag == qn("w:p"):
        p = Paragraph(child, doc)
        if p.text.strip():
            parts.append(p.text.strip())
    elif child.tag == qn("w:tbl"):
        table = Table(child, doc)
        lines = []
        for ri, row in enumerate(table.rows, 1):
            vals = [cell.text.replace("\n", " / ").strip() for cell in row.cells]
            lines.append(f"R{ri}: " + " | ".join(vals))
        parts.append(f"[TABLE rows={len(table.rows)} cols={len(table.columns)}]\n" + "\n".join(lines) + "[/TABLE]")
body_text = "\n\n".join(parts)
register_text = register_path.read_text(encoding="utf-8-sig")
fields = [
    "document_genre","document_purpose","primary_user_or_reader","evidence_role","source_of_truth",
    "required_sections","required_tables_or_figures","required_fields_or_questions","required_calculations_or_analysis",
    "required_cross_references","real_data_required","third_party_evidence_required","prohibited_fabrication",
    "title_blind_test","negative_choice_neighbors","acceptance_tests","document_role","official_requirement_text",
    "official_checkbox_text","official_evidence_table_page","official_source_readback_status","synthetic_population_rule"
]
selected_bp = {k: bp.get(k) for k in fields}
inputs = {
    "work_id":"TTQS-0012-W1-SEMANTIC-R06-GLM-20261030-02",
    "project_id":"TTQS_ONE","document_id":"0012","requirement_id":"I02-E03",
    "candidate_sha256":docx_sha,"candidate_bytes":docx_path.stat().st_size,
    "official_pdf_sha256":official_sha_expected,"blueprint_file_sha256":bp_sha,"blueprint_row_sha256":row_sha,
    "worker_source_sha256":sha_file(source_path),"synthetic_register_sha256":sha_file(register_path),
    "technical_receipt_sha256":sha_file(tech_path),"technical_status":tech["technical_status"],
    "technical_check_count":len(checks),"visual_status":"PENDING; no exact-candidate visual PASS receipt",
    "semantic_status":"PENDING; this packet requests one independent exact-SHA semantic review",
    "formal_acceptance":"UNKNOWN_NOT_ACCEPTED"
}
out.mkdir(parents=True)
(out / "candidate_text_extracted.txt").write_text(body_text, encoding="utf-8")
(out / "blueprint_row.json").write_text(json.dumps(bp, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(out / "synthetic_register.csv").write_text(register_text, encoding="utf-8")
(out / "technical_receipt.json").write_text(json.dumps(tech, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(out / "review_input_manifest.json").write_text(json.dumps(inputs, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
packet = f"""# 0012 / I02-E03 / R06 - Corrected-binding independent semantic review

## Review task

Work ID: {inputs['work_id']}
Review only the exact local candidate identified below. Do not edit or rebuild it. Do not claim visual QA, REAL evidence, association approval, or formal acceptance.

Candidate DOCX SHA-256: {docx_sha}
Candidate bytes: {docx_path.stat().st_size}
Official requirement: {bp['official_requirement_text']}
Official checkbox text: {bp['official_checkbox_text']}
Official table page: {bp['official_evidence_table_page']}

## Evidence binding

- Candidate: {docx_path} | SHA-256 {docx_sha}
- Official source PDF: {official} | SHA-256 {official_sha_expected}
- Current unique Blueprint file: {bp_path} | SHA-256 {bp_sha}
- Unique Blueprint row for 0012 / I02-E03 | SHA-256 {row_sha}
- Worker source draft: {source_path} | SHA-256 {inputs['worker_source_sha256']}
- R06 synthetic replacement register: {register_path} | SHA-256 {inputs['synthetic_register_sha256']}
- Existing deterministic technical receipt: {tech_path} | SHA-256 {inputs['technical_receipt_sha256']}; PASS, {len(checks)} checks. Technical evidence only.
- Visual QA: pending; do not infer a visual PASS from prior candidate versions.
- Formal association acceptance: UNKNOWN / NOT ACCEPTED.

## Blueprint-specific scope

{json.dumps(selected_bp, ensure_ascii=False, indent=2)}

## Required independent review

Read the complete candidate text below. Verify candidate identity against this manifest and exact SHA. Return PASS, PARTIAL, or FAIL, with exact section/table/row locators for every material finding. Cover:
1. Official requirement, document ID, I02-E03 and unique Blueprint alignment.
2. Correct evidence-record genre and routine association usability.
3. Complete, coherent synthetic example, replacement-register alignment, calculations and denominators where applicable, and clear SAMPLE/SYNTHETIC versus REAL boundary.
4. Title-blind identification and negative-neighbor distinction from I02-E02 / 0011 and I02-E04 / 0013.
5. Missing, contradictory, unsupported or placeholder content; exact hold/return criteria and source locations.
6. Whether it directly answers the official requirement without fabricating subsidy rules, approvals, third-party originals, signatures, association decisions or performance.

Do not review visual layout in this task. Do not treat the technical receipt as semantic evidence. Do not rely on or reproduce previous review output.

## Prior packet quarantine

A previous dispatch packet was changed after its dispatch record and contains an embedded review of baseline candidate SHA a90340289d360a7705fad8137db3a33b648a126ca67b1454d66c0b9288f9d9b5; it is not evidence about this R06 candidate. The previous packet and response are excluded. This new packet is generated from current local inputs and binds to the exact hashes above.

## Candidate text extracted from the exact-hash DOCX

{body_text}

## Current R06 synthetic replacement register

{register_text}
"""
packet_path = out / "REVIEW_PACKET_R06_CORRECTED.md"
packet_path.write_text(packet, encoding="utf-8")
manifest = json.loads((out / "review_input_manifest.json").read_text(encoding="utf-8"))
manifest["review_packet_sha256"] = sha_file(packet_path)
manifest["review_packet_bytes"] = packet_path.stat().st_size
manifest["candidate_extracted_text_sha256"] = sha_file(out / "candidate_text_extracted.txt")
(out / "review_input_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({
    "packet_path":str(packet_path),"packet_sha256":sha_file(packet_path),"packet_bytes":packet_path.stat().st_size,
    "candidate_sha256":docx_sha,"blueprint_file_sha256":bp_sha,"blueprint_row_sha256":row_sha,
    "source_sha256":inputs["worker_source_sha256"],"register_sha256":inputs["synthetic_register_sha256"],
    "technical_receipt_sha256":inputs["technical_receipt_sha256"],"body_chars":len(body_text),
    "register_rows":max(0,len(register_text.splitlines())-1),"technical_checks":len(checks),"failed_checks":failed
},ensure_ascii=False,indent=2))

