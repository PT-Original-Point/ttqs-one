from pathlib import Path
import hashlib, json, datetime
import pypdfium2 as pdfium

BASE = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0104_I18-E11_SOURCE_PREP_20261022")
PDF = BASE / "visual" / "0104_R16" / "0104_R16_word_native.pdf"
OUT = BASE / "visual" / "0104_R16" / "pages"
OUT.mkdir(parents=True, exist_ok=True)
doc = pdfium.PdfDocument(str(PDF))
pages = []
for idx in range(len(doc)):
    page = doc[idx]
    bitmap = page.render(scale=1.35)
    image = bitmap.to_pil()
    path = OUT / f"page-{idx+1:02d}.png"
    image.save(path, format="PNG", optimize=True)
    pages.append({
        "page": idx + 1,
        "width_px": image.width,
        "height_px": image.height,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "pdf_points": [round(float(x), 2) for x in page.get_size()],
    })
    page.close()
doc.close()
receipt = {
    "receipt_id": "TTQS-0104-VISUAL-RASTER-R16",
    "observed_at_tpe": datetime.datetime.now().astimezone().isoformat(),
    "pdf_path": str(PDF),
    "pdf_sha256": hashlib.sha256(PDF.read_bytes()).hexdigest(),
    "page_count": len(pages),
    "render_scale": 1.35,
    "pages": pages,
}
receipt_path = BASE / "evidence" / "raster_receipt_0104_R16.json"
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"page_count": len(pages), "pdf_sha256": receipt["pdf_sha256"], "receipt": str(receipt_path), "page_sizes": [p["pdf_points"] for p in pages]}, ensure_ascii=False, indent=2))
