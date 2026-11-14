from pathlib import Path
import hashlib, json, re

root = Path(__file__).resolve().parents[1]
candidate = root / 'candidate' / '0069_R02.docx'
pdf = root / 'qa' / 'render_word_R02' / '0069_R02_word.pdf'
render_dir = pdf.parent
expected = 'b701604ab634d42d1638ea0065cbbac39bb40e631d2716a572bc5422494e53bd'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
actual = sha(candidate)
if actual != expected: raise SystemExit(f'candidate SHA mismatch: {actual}')
page_paths = sorted(render_dir.glob('page-*.png'), key=lambda p: int(re.search(r'page-(\d+)', p.name).group(1)))
contact_paths = sorted(render_dir.glob('contact-*.png'))
if len(page_paths) != 19 or len(contact_paths) != 10: raise SystemExit('unexpected render coverage')
pages = []
for p in page_paths:
    n = int(re.search(r'page-(\d+)', p.name).group(1))
    pages.append({'page': n, 'path': f'qa/render_word_R02/{p.name}', 'bytes': p.stat().st_size, 'sha256': sha(p)})
contacts = []
for i, p in enumerate(contact_paths):
    start = i * 2 + 1
    end = min(start + 1, len(page_paths))
    contacts.append({'path': f'qa/render_word_R02/{p.name}', 'pages': list(range(start, end + 1)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
receipt = {
  'schema': 'TTQS_ONE_0069_R02_VISUAL_REVIEW.v1',
  'project_id': 'TTQS_ONE', 'document_id': '0069', 'revision': 'R02',
  'requirement_id': 'I16-E01', 'official_checkbox_serial': '076',
  'candidate_docx_sha256': actual, 'candidate_docx_bytes': candidate.stat().st_size,
  'renderer': 'Microsoft Word COM read-only ExportAsFixedFormat to PDF; macros disabled; Poppler pdftoppm at 120 DPI',
  'render_pdf': {'path': 'qa/render_word_R02/0069_R02_word.pdf', 'bytes': pdf.stat().st_size, 'sha256': sha(pdf), 'page_count': 19},
  'page_images': pages,
  'contact_sheets': contacts,
  'visual_status': 'PASS_WITH_SCOPE',
  'visual_inspection_scope': 'All 19 full-size page images inspected at original PNG resolution using 10 paired side-by-side contact sheets; the final sheet contains page 19 alone.',
  'observations': [
    'No clipped text, overlap, broken table borders, missing glyphs, or unreadable content observed across the 19 rendered pages.',
    'Repeated headers, page numbers, wide control-point tables, calculations, and page transitions remain readable.',
    'Pages 16-18 contain explicitly labeled blank reusable forms as supplements; the completed SAMPLE case and its 7/7 embedded records are in section 7 and are not replaced by blank forms.',
    'SAMPLE/SYNTHETIC and REAL=UNKNOWN/HOLD boundaries remain visible; no actual association execution or approval is asserted.'
  ],
  'limitations': ['Paper-printer fidelity, accessibility tagging, and human user testing were not tested.', 'The independent semantic reviewer did not independently render the DOCX; this receipt supplies the separate visual scope.'],
  'candidate_docx_unchanged': True, 'formal_acceptance': 'NOT_GRANTED', 'real_evidence': 'UNKNOWN/HOLD',
  'checked_at_local': '2026-10-19T11:52:00+08:00'
}
receipt_path = root / 'qa' / 'visual_review_R02.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
receipt_sha = sha(receipt_path)
manifest_path = root / 'artifact_manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
manifest['visual_status'] = 'PASS_WITH_SCOPE'
manifest['visual_receipt'] = 'qa/visual_review_R02.json'
manifest['visual_receipt_sha256'] = receipt_sha
manifest['visual_pdf_sha256'] = sha(pdf)
manifest['visual_page_count'] = 19
manifest['visual_inspection_scope'] = 'All 19 original-resolution page images inspected; 19/19 coverage.'
manifest['candidate_docx_unchanged_after_visual_review'] = sha(candidate) == expected
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
readme_path = root / 'README.md'
readme = readme_path.read_text(encoding='utf-8')
old = 'Visual inspection remains pending. No rendered PDF or page images are claimed.'
new = f"Visual review is complete on the exact unchanged candidate SHA: Microsoft Word COM produced a 19-page PDF ({sha(pdf)}); all 19 page images were inspected at original resolution. The visual receipt and rendered evidence are under `qa/visual_review_R02.json` and `qa/render_word_R02/`. Result: **PASS_WITH_SCOPE**. Printer output, accessibility tagging, and human user testing were not tested."
if old not in readme: raise SystemExit('README pending-status text not found exactly once')
readme = readme.replace(old, new, 1)
readme_path.write_text(readme, encoding='utf-8')
print(json.dumps({'candidate_sha256': actual, 'visual_receipt_sha256': receipt_sha, 'pdf_sha256': sha(pdf), 'page_count': len(pages), 'contact_sheets': len(contacts), 'manifest_sha256': sha(manifest_path), 'README_updated': True}, ensure_ascii=False))
