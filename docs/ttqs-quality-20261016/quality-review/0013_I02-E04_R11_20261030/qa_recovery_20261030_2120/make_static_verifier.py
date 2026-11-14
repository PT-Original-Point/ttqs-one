
from pathlib import Path
base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029")
qa=base/"qa"
src=qa/"verify_0013_R11_technical.py"
dst=qa/"verify_0013_R11_technical_static.py"
if dst.exists(): raise SystemExit(f"Refusing to overwrite {dst}")
lines=src.read_text(encoding="utf-8-sig").splitlines()
out=[]
for line in lines:
    s=line.strip()
    if s=="from pypdf import PdfReader":
        continue
    if s.startswith("visual = json.loads(VISUAL"):
        continue
    if s.startswith("pdf_pages = len(PdfReader"):
        continue
    if s.startswith('"native_word_render_receipt_exact_sha_and_25_pages":'):
        continue
    if s.startswith('"visual_receipt_does_not_claim_semantic_or_formal_pass":'):
        continue
    if s.startswith('"native_word_pdf_sha256":'):
        out.append('    "native_word_pdf_sha256": None,')
        continue
    if s.startswith('"native_word_pdf_pages":'):
        out.append('    "native_word_pdf_pages": None,')
        continue
    if s.startswith('"visual_status": visual.get'):
        out.append('    "visual_status": render_status.get("visual_verdict"),')
        continue
    if s.startswith('"semantic_status": "PENDING_INDEPENDENT'):
        out.append('    "semantic_review_sha256": sha_file(BASE / "qa" / "semantic_review_R11.json"),')
        out.append('    "semantic_status": semantic.get("verdict"),')
        continue
    out.append(line)
    if s=='build = json.loads(BUILD.read_text(encoding="utf-8"))':
        out.extend([
            'semantic = json.loads((BASE / "qa" / "semantic_review_R11.json").read_text(encoding="utf-8"))',
            'render_status = json.loads((BASE / "qa" / "render_R11_instrumented" / "R11_RENDER_STATUS.json").read_text(encoding="utf-8"))',
            'assert semantic.get("candidate_sha256") == sha_file(DOCX)',
            'assert semantic.get("verdict") == "PASS_SCOPED_SAMPLE_SEMANTIC"',
            'assert render_status.get("candidate_sha256") == sha_file(DOCX)',
            'assert render_status.get("state") == "WORD_EXPORT_TIMEOUT_NO_PDF"'
        ])
if any("visual = json.loads(VISUAL" in x or "pdf_pages =" in x for x in out):
    raise SystemExit("Visual-only dependency remained")
dst.write_text("\n".join(out)+"\n",encoding="utf-8")
print(dst)

