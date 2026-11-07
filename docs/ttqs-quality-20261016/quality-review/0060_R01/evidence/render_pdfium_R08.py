from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageDraw, ImageOps

BASE = Path(__file__).resolve().parents[1]
DOCX = BASE / "candidate/0060_R08.docx"
PDF = BASE / "evidence/render_R08/0060_R08_Word_export.pdf"
OUT = BASE / "evidence/render_R08"
EXPECTED = "92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def main() -> None:
    before = digest(DOCX)
    if before != EXPECTED:
        raise SystemExit(f"Candidate SHA mismatch: {before}")
    OUT.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(PDF)
    pages = []
    manifest_pages = []
    for index in range(len(pdf)):
        page = pdf[index]
        image = page.render(scale=1.7).to_pil().convert("RGB")
        path = OUT / f"page-{index + 1:02d}.png"
        image.save(path, optimize=True)
        text = page.get_textpage().get_text_range()
        manifest_pages.append({
            "page": index + 1,
            "path": str(path),
            "sha256": digest(path),
            "bytes": path.stat().st_size,
            "width": image.width,
            "height": image.height,
            "extracted_chars": len(text.strip()),
            "blank": len(text.strip()) == 0,
        })
        pages.append((index + 1, image.copy()))
    contacts = []
    thumb_width, gap = 920, 24
    for start in range(0, len(pages), 4):
        thumbs = []
        for number, image in pages[start:start + 4]:
            height = round(image.height * thumb_width / image.width)
            thumb = ImageOps.expand(image.resize((thumb_width, height), Image.Resampling.LANCZOS), border=2, fill="#687385")
            canvas = Image.new("RGB", (thumb.width, thumb.height + 34), "white")
            canvas.paste(thumb, (0, 34))
            ImageDraw.Draw(canvas).text((12, 9), f"Page {number:02d}", fill="#172033")
            thumbs.append(canvas)
        width = max(image.width for image in thumbs)
        height = max(image.height for image in thumbs)
        sheet = Image.new("RGB", (width * 2 + gap * 3, height * 2 + gap * 3), "#e7ebf0")
        for index, image in enumerate(thumbs):
            sheet.paste(image, (gap + (index % 2) * (width + gap), gap + (index // 2) * (height + gap)))
        path = OUT / f"contact-{start + 1:02d}-{start + len(thumbs):02d}.png"
        sheet.save(path, optimize=True)
        contacts.append({"path": str(path), "sha256": digest(path), "bytes": path.stat().st_size})
    after = digest(DOCX)
    manifest = {
        "candidate_sha256": before,
        "candidate_unchanged": before == after,
        "pdf_sha256": digest(PDF),
        "pdf_bytes": PDF.stat().st_size,
        "page_count": len(pages),
        "rendered_png_count": sum(not page["blank"] for page in manifest_pages),
        "pages": manifest_pages,
        "contact_sheets": contacts,
        "renderer": "Microsoft Word COM PDF export + bundled PDFium rasterization",
        "rendered_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    (OUT / "render_manifest_R08.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_sha256": before, "pdf_sha256": manifest["pdf_sha256"], "page_count": len(pages), "nonblank_pages": manifest["rendered_png_count"], "manifest": str(OUT / "render_manifest_R08.json")}, ensure_ascii=False))


if __name__ == "__main__":
    main()

