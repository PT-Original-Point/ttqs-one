from pathlib import Path
from hashlib import sha256
import json
import pypdfium2 as pdfium

root = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0007_I01-E04_R12_STATUS_CLAIM_REPAIR_20261031")
render = root / "render" / "word_native_r12"
pdf_path = render / "0007_I01-E04_R12_WORD_RENDER.pdf"
pdf_sha = sha256(pdf_path.read_bytes()).hexdigest()
doc = pdfium.PdfDocument(pdf_path)
pages = []
for i in range(len(doc)):
    page = doc[i]
    bitmap = page.render(scale=2.0)
    out = render / f"page-{i+1:02}.png"
    bitmap.to_pil().save(out, format="PNG", optimize=True)
    pages.append({"page": i + 1, "file": out.name, "sha256": sha256(out.read_bytes()).hexdigest(), "bytes": out.stat().st_size})
receipt = {
    "project_id": "TTQS_ONE",
    "doc_id": "0007",
    "requirement_id": "I01-E04",
    "revision": "R12",
    "pdf_sha256": pdf_sha,
    "page_count": len(pages),
    "rasterizer": "pypdfium2, 2.0x scale",
    "pages": pages,
    "status": "RASTERIZED_PENDING_VISUAL_INSPECTION"
}
(render / "PAGE_IMAGE_MANIFEST_R12.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"page_count": len(pages), "pdf_sha256": pdf_sha, "images": len(pages)}, ensure_ascii=False))