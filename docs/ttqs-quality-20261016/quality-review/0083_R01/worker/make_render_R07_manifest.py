from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader


BASE = Path(__file__).resolve().parents[1]
DOCX = BASE / "candidate" / "0083_R07.docx"
RENDER = BASE / "evidence" / "render_R07_final"
PDF = RENDER / "0083_R07.pdf"
MANIFEST = RENDER / "visual_input_manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


reader = PdfReader(str(PDF))
pages = sorted(RENDER.glob("page-*.png"))
if not reader.pages or len(reader.pages) != len(pages):
    raise RuntimeError(f"PDF page/PNG count mismatch; got {len(reader.pages)} PDF pages and {len(pages)} PNGs")

font = ImageFont.load_default()
sheets = []
for batch, offset in enumerate(range(0, len(pages), 16), start=1):
    batch_pages = pages[offset:offset + 16]
    thumb_w, thumb_h = 300, 424
    gap, label_h = 14, 24
    sheet = Image.new("RGB", (4 * thumb_w + 5 * gap, 4 * (thumb_h + label_h) + 5 * gap), "white")
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(batch_pages):
        col, row = index % 4, index // 4
        x, y = gap + col * (thumb_w + gap), gap + row * (thumb_h + label_h + gap)
        with Image.open(path) as source:
            thumb = source.convert("RGB")
            thumb.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            sheet.paste(thumb, (x + (thumb_w - thumb.width) // 2, y))
        page_num = int(path.stem.split("-")[-1])
        draw.text((x, y + thumb_h + 3), f"Page {page_num:02d}", fill="#17365D", font=font)
    out = RENDER / f"contact_sheet_{batch:02d}.png"
    sheet.save(out, optimize=True)
    sheets.append({"file": out.name, "sha256": sha256(out), "pages": [int(p.stem.split("-")[-1]) for p in batch_pages]})

page_evidence = []
for number, (pdf_page, png) in enumerate(zip(reader.pages, pages), start=1):
    page_evidence.append({
        "page": number,
        "png": png.name,
        "png_sha256": sha256(png),
        "png_bytes": png.stat().st_size,
        "pdf_text_characters": len(pdf_page.extract_text() or ""),
    })

manifest = {
    "schema": "TTQS_ONE_0083_VISUAL_INPUT_MANIFEST.v1",
    "revision": "R07",
    "candidate_docx": str(DOCX.relative_to(BASE)),
    "candidate_docx_sha256": sha256(DOCX),
    "pdf": PDF.name,
    "pdf_sha256": sha256(PDF),
    "pdf_pages": len(reader.pages),
    "render_engine": "Microsoft Word COM export; Poppler rasterization at 100 dpi",
    "visual_coverage": f"all pages 1-{len(reader.pages)} represented in full-page contact sheets; targeted full-resolution inspection pending",
    "pages": page_evidence,
    "contact_sheets": sheets,
}
MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "docx_sha256": manifest["candidate_docx_sha256"],
    "pdf_sha256": manifest["pdf_sha256"],
    "page_count": manifest["pdf_pages"],
    "manifest_sha256": sha256(MANIFEST),
    "contact_sheets": sheets,
    "last_pages_text_chars": [p["pdf_text_characters"] for p in page_evidence[-5:]],
}, ensure_ascii=False, indent=2))

