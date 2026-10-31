from pathlib import Path
from hashlib import sha256
from datetime import datetime
from zoneinfo import ZoneInfo
import json
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0008_I01-E05_LUNA_TEXT_DRAFT_R03_20261030')
files={
 'candidate/0008_I01-E05_R03c.docx':'candidate/0008_I01-E05_R03c.docx',
 'candidate/0008_I01-E05_R03.md':'worker/0008_I01-E05_R03.md',
 'evidence/0008_I01-E05_R03c.pdf':'qa/render_R03c_native/0008_I01-E05_R03c.pdf',
 'evidence/DOCX_TECHNICAL_QA_R03c.json':'qa/DOCX_TECHNICAL_QA_R03c.json',
 'evidence/WORD_VISUAL_QA_R03c.json':'qa/WORD_VISUAL_QA_R03c.json',
 'evidence/WORD_NATIVE_RENDER_RECEIPT.json':'qa/render_R03c_native/WORD_NATIVE_RENDER_RECEIPT.json',
 'evidence/DETERMINISTIC_QA_R03.json':'qa/DETERMINISTIC_QA_R03.json',
 'evidence/R03_REPAIR_RECEIPT.json':'qa/R03_REPAIR_RECEIPT.json',
 'evidence/SEMANTIC_REVIEW_R02_ORIGINAL.json':'source/SEMANTIC_REVIEW_R02_ORIGINAL.json',
 'evidence/WRITER_RECEIPT_R02_ORIGINAL.json':'source/WRITER_RECEIPT_R02_ORIGINAL.json',
 'build/build_0008_r03_docx.py':'qa/build_0008_r03_docx.py',
 'build/audit_R03c.py':'qa/audit_R03c.py',
 'build/make_contact_sheets_R03c.py':'qa/make_contact_sheets_R03c.py',
 'build/make_manifest_R03c.py':'qa/make_manifest_R03c.py',
 'build/word_native_render_R03.ps1':'qa/word_native_render_R03.ps1',
}
hashes={}
for target,relative in files.items():
 p=root/relative
 if not p.is_file(): raise FileNotFoundError(p)
 hashes[target]={'sha256':sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'source_relative':relative}
manifest={
 'project_id':'TTQS_ONE','work_id':'TTQS-0008-I01-E05-R03C-DOCX-VISUAL-REPAIR',
 'observed_at_taipei':datetime.now(ZoneInfo('Asia/Taipei')).isoformat(),'github_head_before_sync':'513522d420488f062bdaa0f930e29e1d3deae850',
 'document':{'doc_id':'0008','official_requirement_id':'I01-E05','unique_blueprint_id':'I01-E05','official_checkbox':'I01-E05','state':'CANDIDATE_SAMPLE_SYNTHETIC_NOT_FORMALLY_ACCEPTED'},
 'authoritative_inputs':{'official_requirement_pdf_sha256':'805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709','unique_blueprint_file_sha256':'406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e','unique_blueprint_row_sha256':'3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d'},
 'result':{'candidate_docx_sha256':'39a41b63f2e7704d9b004923e8fbc9d9dadc54855e229646ccbf080e1e8a9487','technical_status':'PASS_WITHIN_TECHNICAL_SCOPE','visual_status':'PASS_WITHIN_VISUAL_LAYOUT_SCOPE','semantic_status':'PENDING_INDEPENDENT_EXACT_SHA_REVIEW','formal_acceptance':'NOT_GRANTED'},
 'scope_note':'R03c fixes the fact_id column wrap and raises caption text to the 10.5pt body minimum. Microsoft Word native export contains 117 pages; all 117 pages were visually checked via 30 contact sheets, with pages 20, 116, and 117 inspected at full page resolution. The 594-row SAMPLE/SYNTHETIC fact register is preserved. No real association category, policy, approval, roster, or achievement is asserted.',
 'prior_review_context':'The original R02 independent review is included and remains PARTIAL on R02. It is historical context, not an R03c semantic verdict.',
 'artifacts':hashes
}
path=root/'qa'/'GITHUB_SYNC_MANIFEST_R03c.json'
path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# 0008 / I01-E05 — R03c candidate evidence manifest','',f"Observed (Asia/Taipei): {manifest['observed_at_taipei']}",'','- **Candidate state:** CANDIDATE / SAMPLE / SYNTHETIC; not formally accepted.','- **Official mapping:** doc_id `0008`; checkbox and requirement `I01-E05`; unique Blueprint row `I01-E05`.','- **Source SHA-256:** official requirement PDF `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`; Blueprint file `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; Blueprint row `3d8181714ecc1058dcf98d653eff45149287b27521ba176701c69881f83cec2d`.','',f"- **DOCX SHA-256:** `{manifest['result']['candidate_docx_sha256']}`",'- **Technical QA:** PASS within technical scope: DOCX package integrity, 20 tables, 3 sections, body text ≥10.5 pt, table text ≥9.5 pt, 594 unique fact IDs matching the source, and native render/PDF hash linkage.','- **Visual QA:** PASS within visual layout scope: native Word render, 117/117 pages reviewed through 30 contact sheets; pages 20, 116, 117 inspected at full resolution. R03c fixed SF fact_id wrapping and lifted caption text to the 10.5 pt floor.','- **Independent semantic QA:** PENDING for exact R03c SHA. Do not treat the R02 reviewer PARTIAL as an R03c review.','- **Real evidence:** UNKNOWN / NOT ASSERTED. SAMPLE data, assumptions, and replacement register remain synthetic; association-specific policy and approval remain UNKNOWN/HOLD.','','## Included files','', '| File | SHA-256 | Bytes |','|---|---|---:|']
for target,item in hashes.items(): md.append(f"| `{target}` | `{item['sha256']}` | {item['bytes']} |")
md.extend(['','## Artifact status','', 'This package supports technical and visual layout inspection only. It is not a formal acceptance or real-world evidence package. The R02 independent review and its original writer receipt are retained as historical inputs; their verdict is not transferred to R03c.',''])
(root/'qa'/'GITHUB_SYNC_MANIFEST_R03c.md').write_text('\n'.join(md),encoding='utf-8')
print(json.dumps({'json_manifest':str(path),'markdown_manifest':str(root/'qa'/'GITHUB_SYNC_MANIFEST_R03c.md'),'json_sha256':sha256(path.read_bytes()).hexdigest(),'markdown_sha256':sha256((root/'qa'/'GITHUB_SYNC_MANIFEST_R03c.md').read_bytes()).hexdigest(),'artifact_count':len(hashes)},indent=2))



