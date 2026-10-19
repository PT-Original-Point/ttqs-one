from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(r"E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0085_R01")
PDF = ROOT / "evidence" / "render_R06" / "0085_R06_word_render.pdf"
OUT = ROOT / "evidence" / "render_R06"
OUT.mkdir(parents=True, exist_ok=True)

pdf = pdfium.PdfDocument(str(PDF))
pages = []
for i in range(len(pdf)):
    page = pdf[i]
    bitmap = page.render(scale=1.55)
    image = bitmap.to_pil().convert("RGB")
    path = OUT / f"page-{i+1:03d}.png"
    image.save(path, optimize=True)
    pages.append((path, image))

contact_paths = []
for start in range(0, len(pages), 12):
    batch = pages[start : start + 12]
    thumb_w, thumb_h, pad, label_h = 340, 460, 18, 28
    canvas = Image.new("RGB", (4 * thumb_w + 5 * pad, 3 * (thumb_h + label_h) + 4 * pad), "#e8edf2")
    draw = ImageDraw.Draw(canvas)
    for j, (path, image) in enumerate(batch):
        col, row = j % 4, j // 4
        x = pad + col * (thumb_w + pad)
        y = pad + row * (thumb_h + label_h + pad)
        thumb = ImageOps.contain(image, (thumb_w, thumb_h), Image.Resampling.LANCZOS)
        canvas.paste(thumb, (x + (thumb_w - thumb.width) // 2, y))
        draw.text((x + 4, y + thumb_h + 4), path.stem, fill="#203040")
    cpath = OUT / f"contact-{start+1:03d}-{start+len(batch):03d}.jpg"
    canvas.save(cpath, quality=88, optimize=True)
    contact_paths.append(cpath)

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = {
    "project_id": "TTQS_ONE",
    "doc_id": "0085",
    "candidate": "R06",
    "pdf_path": str(PDF),
    "pdf_sha256": sha(PDF),
    "render_engine": "Microsoft Word PDF export, rasterized by pypdfium2",
    "page_count": len(pages),
    "png_scale": 1.55,
    "pages": [{"path": str(p), "sha256": sha(p), "width": im.width, "height": im.height} for p, im in pages],
    "contact_sheets": [{"path": str(p), "sha256": sha(p)} for p in contact_paths],
    "rendered_at_utc": datetime.now(timezone.utc).isoformat(),
}
manifest_path = OUT / "render_manifest_R06.json"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"page_count": len(pages), "pdf_sha256": manifest["pdf_sha256"], "contacts": [str(p) for p in contact_paths], "manifest": str(manifest_path)}, ensure_ascii=False, indent=2))
