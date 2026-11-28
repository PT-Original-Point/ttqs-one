from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "evidence" / "render_R04" / "0062_R04.pdf"
OUT = ROOT / "evidence" / "render_R04" / "pages"
CONTACT = ROOT / "evidence" / "render_R04" / "contact_sheets"
DPI = 150
THUMB_WIDTH = 420


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    CONTACT.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(str(PDF))
    pages = []
    manifest = {
        "pdf_path": str(PDF),
        "pdf_sha256": file_hash(PDF),
        "dpi": DPI,
        "page_count": len(pdf),
        "pages": [],
        "contact_sheets": [],
    }
    for n in range(len(pdf)):
        page = pdf[n]
        width_pt, height_pt = page.get_size()
        bitmap = page.render(scale=DPI / 72)
        pil = bitmap.to_pil().convert("RGB")
        image_path = OUT / f"page-{n+1:02d}.png"
        pil.save(image_path, optimize=True)
        pages.append(pil.copy())
        manifest["pages"].append({
            "page": n + 1,
            "width_pt": round(width_pt, 2),
            "height_pt": round(height_pt, 2),
            "orientation": "landscape" if width_pt > height_pt else "portrait",
            "png": str(image_path),
            "png_sha256": file_hash(image_path),
            "pixel_size": list(pil.size),
        })

    font_path = Path(r"C:\Windows\Fonts\arial.ttf")
    font = ImageFont.truetype(str(font_path), 22) if font_path.exists() else ImageFont.load_default()
    cell_w = THUMB_WIDTH + 24
    cell_h = 620
    for batch_start in range(0, len(pages), 9):
        batch = pages[batch_start : batch_start + 9]
        rows = math.ceil(len(batch) / 3)
        sheet = Image.new("RGB", (cell_w * 3, cell_h * rows), "#D8E0E7")
        draw = ImageDraw.Draw(sheet)
        for local, page_img in enumerate(batch):
            idx = batch_start + local
            scale = THUMB_WIDTH / page_img.width
            thumb = page_img.resize((THUMB_WIDTH, int(page_img.height * scale)), Image.Resampling.LANCZOS)
            col = local % 3
            row = local // 3
            x = col * cell_w + 12
            y = row * cell_h + 36
            sheet.paste(thumb, (x, y))
            draw.text((x, 8 + row * cell_h), f"PAGE {idx+1:02d}", fill="#173D59", font=font)
        sheet_path = CONTACT / f"contact-{batch_start+1:02d}-{batch_start+len(batch):02d}.jpg"
        sheet.save(sheet_path, quality=90)
        manifest["contact_sheets"].append(str(sheet_path))

    manifest_path = ROOT / "evidence" / "visual_render_manifest_R04.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "page_count": len(pages),
        "pdf_sha256": manifest["pdf_sha256"],
        "manifest": str(manifest_path),
        "contact_sheets": manifest["contact_sheets"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
