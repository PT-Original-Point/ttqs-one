from __future__ import annotations
import csv, hashlib, json, re, zipfile
from datetime import datetime, timezone
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / 'candidate' / '0045_R01.docx'
PDF = ROOT / 'evidence' / 'render_R01_final' / '0045_R01.pdf'
REGISTER = ROOT / 'evidence' / 'SYNTHETIC_REPLACEMENT_REGISTER_R01.csv'
EXPECTED_DOCX_SHA = 'c40f401fade386d831b5ba170f9cb17a24313de84474cd957a92ecf8d75a7049'
SECTION_PAGES = {
    '1': '1', '2': '2-3', '3': '2-3', '4': '3-4', '5': '4-5', '6': '5-6',
    '7': '6-7', '8': '7', '9': '8', '10.1': '8', '10.2': '9',
    '10.3': '9-10', '10.4': '11', '10.5': '11', '11': '11-12',
    '12': '12', '13': '12'
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

candidate_sha = sha256(DOCX)
if candidate_sha != EXPECTED_DOCX_SHA:
    raise SystemExit(f'Candidate bytes changed: {candidate_sha}')
with zipfile.ZipFile(DOCX) as zf:
    bad_member = zf.testzip()
    if bad_member:
        raise SystemExit(f'DOCX ZIP integrity failed: {bad_member}')

with REGISTER.open('r', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = list(reader.fieldnames or [])
if 'printed_pages' not in fields:
    fields.append('printed_pages')
for row in rows:
    sections = re.findall(r'§\s*(\d+(?:\.\d+)?)', row['document_location'])
    if not sections:
        raise SystemExit(f'No section locator: {row["fact_id"]}')
    locators = []
    for section in dict.fromkeys(sections):
        if section not in SECTION_PAGES:
            raise SystemExit(f'No page map for §{section}: {row["fact_id"]}')
        locators.append(f'§{section} p.{SECTION_PAGES[section]}')
    row['printed_pages'] = '; '.join(locators)
with REGISTER.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)

reader = PdfReader(str(PDF))
pages = len(reader.pages)
if pages != 12:
    raise SystemExit(f'Expected 12 render pages; got {pages}')
page_pngs = sorted((ROOT / 'evidence' / 'render_R01_final').glob('page-*.png'))
if len(page_pngs) != 12:
    raise SystemExit(f'Expected 12 page images; got {len(page_pngs)}')

now = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
pdf_sha = sha256(PDF)
register_rows = len(rows)
visual_review = {
    'deliverable_id': '0045',
    'requirement_id': 'I10-E01',
    'official_checkbox_sequence': '047',
    'candidate_revision': 'R01',
    'candidate_docx_sha256': candidate_sha,
    'render_pdf_sha256': pdf_sha,
    'render_method': 'Microsoft Word COM opened read-only and exported PDF; Poppler pdftoppm rendered PNG at 150 dpi',
    'page_count': pages,
    'page_images': [p.name for p in page_pngs],
    'pages_visually_inspected': list(range(1, 13)),
    'visual_layout_result': 'PASS_VISUAL_LAYOUT',
    'inspection_notes': [
        'Pages 1-8 were inspected at original raster resolution; title hierarchy, body and tables are legible with no clipping.',
        'Page 1 title underline defect was removed before this frozen SHA; title and metadata remain clear.',
        'Page 5 scoring formula is legible and consistent with the 2-reviewer arithmetic shown on later pages.',
        'Page 9 raw-score table begins at page bottom and continues with its repeated header on page 10; no data row is clipped.',
        'Pages 10-11 preserve the scoring calculations and contract/delivery chronology without clipped cells.',
        'Page 11 ends with section 11 heading and its introductory paragraph; the checklist table starts intact on page 12, with no stranded table header.',
        'Page 12 checklist, related-document crosswalk, and revision record are readable; no clipped text or orphaned table header.'
    ],
    'review_scope': 'Visual layout only; not semantic acceptance or institutional approval.',
    'reviewed_at_utc': now
}
(ROOT / 'evidence' / 'visual_layout_review_R01.json').write_text(
    json.dumps(visual_review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

build_path = ROOT / 'evidence' / 'build_receipt_R01.json'
build = json.loads(build_path.read_text(encoding='utf-8'))
build.update({
    'docx_sha256': candidate_sha,
    'docx_bytes': DOCX.stat().st_size,
    'synthetic_register_rows': register_rows,
    'printed_page_locators': 'Recorded per synthetic fact as section plus printed page or page range',
    'render_pdf_sha256': pdf_sha,
    'render_page_count': pages,
    'render_method': visual_review['render_method'],
    'visual_layout_review': 'PASS_VISUAL_LAYOUT',
    'visual_review_receipt': 'evidence/visual_layout_review_R01.json',
    'independent_semantic_review': 'PENDING_NO_VALID_INDEPENDENT_ROUTE',
    'promotion': 'NOT_PROMOTED',
    'generated_utc': now
})
build_path.write_text(json.dumps(build, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

qa_path = ROOT / 'evidence' / 'technical_static_QA_R01.json'
qa = json.loads(qa_path.read_text(encoding='utf-8'))
qa.update({
    'docx_sha256': candidate_sha,
    'docx_zip_integrity': 'PASS',
    'synthetic_register_rows': register_rows,
    'register_printed_page_locators': 'PASS',
    'render_pdf_sha256': pdf_sha,
    'render_page_count': pages,
    'render_image_count': len(page_pngs),
    'visual_layout_review': 'PASS_VISUAL_LAYOUT',
    'visual_review_receipt': 'evidence/visual_layout_review_R01.json',
    'semantic_acceptance': 'PENDING_INDEPENDENT_REVIEW',
    'promotion': 'NOT_PROMOTED',
    'qa_updated_utc': now
})
qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

progress_path = ROOT / 'PROGRESS.json'
progress = json.loads(progress_path.read_text(encoding='utf-8'))
progress.update({
    'state': 'CANDIDATE_BUILT_RENDERED_VISUAL_PASS_PENDING_INDEPENDENT_SEMANTIC_REVIEW',
    'candidate_sha256': candidate_sha,
    'synthetic_register_rows': register_rows,
    'render_pdf_sha256': pdf_sha,
    'render_page_count': pages,
    'visual_layout_review': 'PASS_VISUAL_LAYOUT',
    'independent_semantic_review': 'PENDING_NO_VALID_INDEPENDENT_ROUTE',
    'promotion': 'NOT_PROMOTED',
    'last_material_update_utc': now,
    'next_actions': [
        'Persist this frozen candidate and its evidence to the existing GitHub branch and read back exact remote SHA',
        'Obtain valid independent exact-SHA semantic review when an authorized reviewer route is available',
        'Do not rebuild unless a specific semantic or layout defect is located'
    ]
})
progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({
    'candidate_sha256': candidate_sha,
    'candidate_bytes': DOCX.stat().st_size,
    'register_rows': register_rows,
    'render_pdf_sha256': pdf_sha,
    'page_count': pages,
    'page_images': len(page_pngs),
    'visual_layout_review': 'PASS_VISUAL_LAYOUT',
    'semantic_review': 'PENDING_NO_VALID_INDEPENDENT_ROUTE',
    'generated_utc': now
}, ensure_ascii=False, indent=2))
