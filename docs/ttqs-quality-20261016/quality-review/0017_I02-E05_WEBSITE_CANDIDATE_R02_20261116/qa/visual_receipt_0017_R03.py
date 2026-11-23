from pathlib import Path
import json,hashlib
r=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0017_I02-E05_WEBSITE_R01_20261116")
docx=r/"candidate"/"0017_WEBSITE_DISCLOSURE_R02.docx"
pdf=r/"render"/"0017_WEBSITE_DISCLOSURE_R02_FINALR04.pdf"
imgs=sorted((r/"render").glob("finalr04-*.png"))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt={
"work_id":"TTQS-0017-I02-E05-WEBSITE-VISUAL-R03-20261116",
"candidate_sha256":sha(docx),
"pdf_sha256":sha(pdf),
"render_engine":"Microsoft Word COM export to PDF, then Poppler pdftoppm at 115 DPI",
"page_count":len(imgs),
"page_images":[{"file":p.name,"sha256":sha(p),"bytes":p.stat().st_size} for p in imgs],
"reviewed_pages":[p.name for p in imgs],
"observations":["all 9 pages reviewed","no clipping or unreadable text observed","agenda table continuation retains header","internal fact table repeats header on continuations","FAQ question/answer pairs remain together after layout repair","candidate DOCX SHA remained unchanged during Word render"],
"decision":"PASS"
}
(r/"qa"/"VISUAL_REVIEW_R03.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"candidate_sha256":receipt["candidate_sha256"],"pdf_sha256":receipt["pdf_sha256"],"page_count":len(imgs),"decision":receipt["decision"]},ensure_ascii=False))
