from pathlib import Path
import hashlib,json,datetime
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0141_I19-E31_SOURCE_PREP_R01_20261025')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=(root/'OPENCODE_R05_SEMANTIC_REVIEW_PACKET.md').read_text(encoding='utf-8')
start=old.find('## Source: OFFICIAL_REQUIREMENT_ROW_I19-E31.json')
end=old.find('## Source: SAMPLE_REPLACEMENT_REGISTER_0141_R05.csv')
if start<0 or end<0 or end<=start:raise SystemExit('R05 packet source boundaries missing')
source_bundle=old[start:end].strip()
review=(root/'OPENCODE_REVIEWER_ORIGINAL_0141_R05.md').read_text(encoding='utf-8')
r5receipt=(root/'OPENCODE_SEMANTIC_REVIEW_RECEIPT_0141_R05.json').read_text(encoding='utf-8')
text= (root/'DOCX_TEXT_EXTRACTION_0141_R06_CANDIDATE.txt').read_text(encoding='utf-8')
docx=root/'0141_I19-E31_R06_CANDIDATE.docx'; textsha=sha(root/'DOCX_TEXT_EXTRACTION_0141_R06_CANDIDATE.txt')
parts=[f'''# TTQS ONE Independent Semantic Review Packet — 0141 R06

Review target: doc_id 0141; official requirement I19-E31; 157-item index 155; printed checkbox serial UNKNOWN. This is a CANDIDATE only. DOCX SHA-256: `{sha(docx)}`. Exact text extracted from that DOCX SHA-256: `{textsha}`. Do not merge any verdict from another candidate SHA.

## Review instructions

You are the independent semantic reviewer, not the Builder. Review the supplied full exact-candidate text and evidence against the complete official requirement, official source excerpt, unique Blueprint R02, source packet R02, crosswalk and nearest-neighbor requirements. Recalculate key published figures against the 36-row synthetic source CSV and summary. Compare each R05 exact-SHA minor finding to the R06 text and receipts; do not inherit R05 PASS. Check genre/use, actual operational usability, frozen Q1–Q7 wording and normalization notes, Q1–Q6 denominator separate from Q7, the Q5 proposal’s unsupported qualitative complaint condition remains UNKNOWN and is not inferred from empty sample responses, exact labels, math, register locators/fact IDs, real-data and human-acceptance boundaries, potential cross-document mismatch, and whether body text still fits its declared requirement rather than a nearest neighbor.

For every finding, cite exact section/table/appendix and quote only the minimum locator. Check Word render receipt as supplied evidence; do not claim to have seen pixels yourself. A separate visual review receipt covers all 25 rendered pages and full-resolution samples; verify its exact SHA binding as metadata. Do not call tools or edit files. Return one JSON object with keys: `doc_id`, `requirement_id`, `candidate_docx_sha256`, `text_sha256`, `verdict` (`PASS`, `PARTIAL`, or `FAIL`), `major_findings`, `minor_findings`, `checks` (each has `id`, `result`, `locator`, `evidence`), `review_scope`, `not_reviewed`, `real_data_status`, `formal_acceptance_status`. Distinguish textual reviewer opinion from native receipts and from association acceptance. If any mandatory requirement lacks a usable field, procedure, evidence, calculation, hold/reject rule, mark PARTIAL/FAIL rather than relying on document length. Keep SAMPLE/SYNTHETIC distinct from REAL; no invented approval or performance claim.

## Prior R05 exact-SHA review — findings to verify, not inherited

R05 reviewed DOCX SHA `{json.loads(r5receipt)['docx_sha256']}` with verdict `{json.loads(r5receipt)['verdict']}`. Original R05 response SHA-256: `{sha(root/'OPENCODE_REVIEWER_ORIGINAL_0141_R05.md')}`.

### Original reviewer response

{review.strip()}

### R05 receipt

```json
{r5receipt.strip()}
```

## Official and source packet (unchanged from R05 packet; SHA identity preserved)

{source_bundle}
''']
for title,path in [
 ('R06 replacement register CSV','SAMPLE_REPLACEMENT_REGISTER_0141_R06.csv'),
 ('R06 source math QA receipt','R06_SOURCE_MATH_QA_RECEIPT.json'),
 ('R06 build receipt','DOCX_BUILD_RECEIPT_0141_R06_CANDIDATE.json'),
 ('R06 Word native render receipt','WORD_RENDER_RECEIPT_0141_R06_CANDIDATE.json'),
 ('R06 DOCX technical QA receipt','R06_DOCX_TECHNICAL_QA_RECEIPT.json'),
 ('R06 visual receipt','VISUAL_REVIEW_RECEIPT_0141_R06_CANDIDATE.json'),
 ('R06 targeted repair receipt','R06_TARGETED_REPAIR_RECEIPT.json'),
 ('R06 layout patch receipt','R06_LAYOUT_PATCH_RECEIPT.json')]:
 p=root/path; raw=p.read_text(encoding='utf-8-sig'); fence='```csv' if path.endswith('.csv') else '```json'; parts.append(f'\n## {title}: {path} (sha256 `{sha(p)}`)\n\n{fence}\n{raw.rstrip()}\n```\n')
parts.append(f'\n## Exact candidate text extracted from R06 DOCX (sha256 `{textsha}`)\n\nThe following text was extracted from the binary identified above. The DOCX SHA is `{sha(docx)}`.\n\n{text.rstrip()}\n')
packet='\n'.join(parts); out=root/'OPENCODE_R06_SEMANTIC_REVIEW_PACKET.md';out.write_text(packet,encoding='utf-8')
rec={'schema':'ttqs-one-0141-r06-review-packet-v1','created_at_local':datetime.datetime.now().astimezone().isoformat(timespec='seconds'),'packet_path':out.name,'packet_sha256':sha(out),'packet_bytes':out.stat().st_size,'docx_sha256':sha(docx),'text_sha256':textsha,'r05_review_sha256':sha(root/'OPENCODE_REVIEWER_ORIGINAL_0141_R05.md'),'source_bundle_sha256':hashlib.sha256(source_bundle.encode()).hexdigest(),'materials':[{'path':p,'sha256':sha(root/p)} for p in ['SAMPLE_REPLACEMENT_REGISTER_0141_R06.csv','R06_SOURCE_MATH_QA_RECEIPT.json','DOCX_BUILD_RECEIPT_0141_R06_CANDIDATE.json','WORD_RENDER_RECEIPT_0141_R06_CANDIDATE.json','R06_DOCX_TECHNICAL_QA_RECEIPT.json','VISUAL_REVIEW_RECEIPT_0141_R06_CANDIDATE.json','R06_TARGETED_REPAIR_RECEIPT.json','R06_LAYOUT_PATCH_RECEIPT.json']],'status':'READY_FOR_EXACT_SHA_INDEPENDENT_REVIEW'}
(root/'OPENCODE_R06_SEMANTIC_REVIEW_PACKET_RECEIPT.json').write_text(json.dumps(rec,ensure_ascii=True,indent=2)+'\n',encoding='utf-8');print(json.dumps(rec,ensure_ascii=True))

