import hashlib
import json
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw

base = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0130_I19-E19_SOURCE_PREP_R01_20261024")
pdf_path = base / "qa" / "render_R01B" / "0130_I19-E19_CANDIDATE_R01B.pdf"
out = pdf_path.parent / "pages"
out.mkdir(parents=True, exist_ok=True)
pdf = pdfium.PdfDocument(str(pdf_path))
page_files = []
thumbs = []
for i in range(len(pdf)):
    page = pdf[i]
    bitmap = page.render(scale=1.5)
    image = bitmap.to_pil().convert("RGB")
    path = out / f"page-{i+1:02d}.png"
    image.save(path, optimize=True)
    page_files.append({"page": i + 1, "path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "width": image.width, "height": image.height})
    thumb = image.copy()
    thumb.thumbnail((310, 438))
    thumb = ImageOps.expand(thumb, border=1, fill="#666666")
    canvas = Image.new("RGB", (314, 466), "white")
    canvas.paste(thumb, ((314 - thumb.width) // 2, 8))
    ImageDraw.Draw(canvas).text((10, 448), f"Page {i+1}", fill="#111111")
    thumbs.append(canvas)
cols = 4
rows = (len(thumbs) + cols - 1) // cols
sheet = Image.new("RGB", (cols * 314, rows * 466), "#dddddd")
for i, thumb in enumerate(thumbs):
    sheet.paste(thumb, ((i % cols) * 314, (i // cols) * 466))
sheet_path = pdf_path.parent / "contact-sheet.png"
sheet.save(sheet_path, optimize=True)
print(json.dumps({"pdf_sha256": hashlib.sha256(pdf_path.read_bytes()).hexdigest(), "page_count": len(pdf), "pages": page_files, "contact_sheet": str(sheet_path), "contact_sheet_sha256": hashlib.sha256(sheet_path.read_bytes()).hexdigest()}, ensure_ascii=True, sort_keys=True))
