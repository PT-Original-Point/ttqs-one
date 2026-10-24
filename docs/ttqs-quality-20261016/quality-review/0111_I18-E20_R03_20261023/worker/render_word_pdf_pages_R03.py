from pathlib import Path
import hashlib, json, datetime
import pypdfium2 as pdfium

BASE = Path(__file__).resolve().parents[1]
PDF = BASE / "visual" / "0111_R03" / "0111_R03_word_native.pdf"
OUT = BASE / "visual" / "0111_R03" / "pages"
OUT.mkdir(parents=True, exist_ok=True)
for stale in OUT.glob("page-*.png"):
    stale.unlink()
doc = pdfium.PdfDocument(str(PDF))
pages = []
for idx in range(len(doc)):
    page = doc[idx]
    image = page.render(scale=1.5).to_pil()
    path = OUT / f"page-{idx + 1:02d}.png"
    image.save(path, format="PNG", optimize=True)
    pages.append({
        "page": idx + 1,
        "width_px": image.width,
        "height_px": image.height,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "pdf_points": [round(float(v), 2) for v in page.get_size()],
    })
    page.close()
doc.close()
receipt = {
    "receipt_id": "TTQS-0111-VISUAL-RASTER-R02",
    "observed_at_tpe": datetime.datetime.now().astimezone().isoformat(),
    "doc_id": "0111",
    "requirement_id": "I18-E20",
    "official_checkbox_serial": "UNKNOWN_NOT_ASSERTED",
    "candidate_docx_sha256": "f427ed898a79393a91d6d8fadcde960a8126e90697325aa94c1b764b8b537a50",
    "pdf_path": str(PDF),
    "pdf_sha256": hashlib.sha256(PDF.read_bytes()).hexdigest(),
    "page_count": len(pages),
    "render_scale": 1.5,
    "pages": pages,
    "visual_inspection": "PENDING_HUMAN_OR_REVIEWER_DIRECT_INSPECTION",
}
path = BASE / "evidence" / "raster_receipt_0111_R03.json"
path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"page_count": len(pages), "pdf_sha256": receipt["pdf_sha256"], "page_sizes": [p["pdf_points"] for p in pages], "receipt": str(path)}, ensure_ascii=False))
