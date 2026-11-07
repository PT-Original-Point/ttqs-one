from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw, ImageFont
import hashlib, csv, json, re

root = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016")
pkg = root / "docs/ttqs-quality-20261016/quality-review/0053_R01"
review = pkg / "review/opencode_v2_review_R01"
review.mkdir(parents=True, exist_ok=True)
candidate = pkg / "candidate/0053_R01.docx"
pdf = pkg / "evidence/render_final_14a7b825/0053_R01_Word_export.pdf"
register = pkg / "SYNTHETIC_REPLACEMENT_REGISTER_0053_R01.csv"
source_map = pkg / "inputs/SOURCE_MAP_0053_R01.md"
blueprint = pkg / "inputs/UNIQUE_BLUEPRINT_0053.json"
official_text = pkg / "inputs/official_evidence_table_page4.txt"
contract = root / "docs/ttqs-quality-20261016"
sha = hashlib.sha256(candidate.read_bytes()).hexdigest()

def docx_blocks(path):
    d = Document(str(path))
    out = []
    for child in d.element.body.iterchildren():
        if child.tag.endswith('}p'):
            p = Paragraph(child, d)
            t = p.text.strip()
            if t:
                out.append(f"[PARAGRAPH | style={p.style.name}] {t}")
        elif child.tag.endswith('}tbl'):
            table = Table(child, d)
            out.append(f"[TABLE {len([x for x in out if x.startswith('[TABLE ')])+1}]")
            for ri, row in enumerate(table.rows, 1):
                cells = []
                for cell in row.cells:
                    text = " / ".join(p.text.strip() for p in cell.paragraphs if p.text.strip())
                    cells.append(text.replace("\n", " | "))
                out.append(f"  row {ri}: " + " || ".join(cells))
            out.append("[/TABLE]")
    return "\n".join(out)

candidate_content = docx_blocks(candidate)
(pkg / "review/candidate_body_text_R01.txt").write_text(candidate_content, encoding="utf-8")

blueprint_obj = json.loads(blueprint.read_text(encoding="utf-8"))
manual = (contract / "02_GENRE_WRITING_MANUAL.md").read_text(encoding="utf-8")
manual_match = re.search(r"## 指標 12｜依目標執行.*?(?=\n## 指標 13｜)", manual, flags=re.S)
manual_excerpt = manual_match.group(0) if manual_match else "[Manual section not found]"
checkbox_doc = (contract / "03_157_CHECKBOX_BLUEPRINTS.md").read_text(encoding="utf-8")
checkbox_lines = checkbox_doc.splitlines()
checkbox_excerpt = "\n".join(checkbox_lines[136:145])
source_map_text = source_map.read_text(encoding="utf-8")
reg_rows = list(csv.DictReader(register.open(encoding="utf-8-sig", newline="")))

# Exact rendered page text permits page-targeted semantic references; it is kept separate from the structured DOCX text.
reader = PdfReader(str(pdf))
page_text = []
for n, page in enumerate(reader.pages, 1):
    page_text.append(f"\n### Rendered page {n}\n" + (page.extract_text() or "[No extractable text]"))

# Contact sheet for a separate visual pass. It is diagnostic only; the full-size page renders remain preserved.
render_dir = pkg / "evidence/render_final_14a7b825"
paths = [render_dir / f"page-{n:02d}.png" for n in range(1, len(reader.pages)+1)]
thumb_w, cols, margin, label_h = 340, 3, 18, 30
thumbs = []
for n, path in enumerate(paths, 1):
    im = Image.open(path).convert("RGB")
    h = round(im.height * thumb_w / im.width)
    im = im.resize((thumb_w, h), Image.Resampling.LANCZOS)
    card = Image.new("RGB", (thumb_w, h+label_h), "white")
    card.paste(im, (0, label_h))
    draw = ImageDraw.Draw(card)
    draw.text((10, 7), f"PAGE {n:02d}", fill="#10243A")
    thumbs.append(card)
rows = (len(thumbs)+cols-1)//cols
cell_h = max(im.height for im in thumbs)
sheet = Image.new("RGB", (cols*thumb_w+(cols+1)*margin, rows*cell_h+(rows+1)*margin), "#DCE5EF")
for i, im in enumerate(thumbs):
    x = margin + (i % cols)*(thumb_w+margin)
    y = margin + (i // cols)*(cell_h+margin)
    sheet.paste(im, (x,y))
contact = review / "page_contact_sheet_R01.png"
sheet.save(contact, optimize=True)

review_packet = f"""# Independent Exact-SHA Review Packet — DOCX 0053 R01

## Review identity
- Candidate: `0053_R01.docx`
- Exact SHA-256: `{sha}`
- Candidate bytes: {candidate.stat().st_size}
- Mapped DOCX ID: `0053`
- Official Unique Blueprint: `I12-E01`
- Official checkbox sequence: `056` (not the DOCX ID)
- Candidate genre claim: `{blueprint_obj.get('document_genre')}`
- Render source: Microsoft Word export, {len(reader.pages)} pages, PDF SHA-256: `{hashlib.sha256(pdf.read_bytes()).hexdigest()}`
- Synthetic register: {len(reg_rows)} rows, SHA-256: `{hashlib.sha256(register.read_bytes()).hexdigest()}`

## Official requirement source
Official evidence table, page 4, source PDF SHA-256 `{blueprint_obj.get('official_pdf_sha256')}`:

{official_text.read_text(encoding='utf-8')}

## Current genre manual, Indicator 12
{manual_excerpt}

## Official checkbox writing instruction, sequence 056
{checkbox_excerpt}

## Unique Blueprint 0053 / I12-E01
```json
{json.dumps(blueprint_obj, ensure_ascii=False, indent=2)}
```

## Source map and fact boundaries
{source_map_text}

## Synthetic replacement register — all rows
```csv
{register.read_text(encoding='utf-8-sig')}
```

## Candidate DOCX body in document order
The following is extracted from the exact DOCX bytes above. Paragraphs and table rows are preserved as structured text; table row/section identifiers should be used for precise findings.

{candidate_content}

## Page-specific rendered text extraction
The following is extracted independently from the Microsoft Word PDF export to help locate findings by physical page. It does not replace visual inspection.

{''.join(page_text)}
"""
packet_path = review / "independent_review_packet_R01.md"
packet_path.write_text(review_packet, encoding="utf-8")
manifest = {
    "candidate_path": str(candidate), "candidate_sha256": sha,
    "candidate_bytes": candidate.stat().st_size,
    "official_requirement_id": "I12-E01", "official_checkbox_sequence": "056",
    "blueprint_sha256": hashlib.sha256(blueprint.read_bytes()).hexdigest(),
    "register_sha256": hashlib.sha256(register.read_bytes()).hexdigest(),
    "register_rows": len(reg_rows), "render_pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
    "render_pages": len(reader.pages),
    "packet_sha256": hashlib.sha256(packet_path.read_bytes()).hexdigest(),
    "contact_sheet": str(contact), "contact_sheet_sha256": hashlib.sha256(contact.read_bytes()).hexdigest(),
    "prepared_utc": __import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat()
}
(review / "review_packet_manifest_R01.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(manifest, ensure_ascii=False, indent=2))
