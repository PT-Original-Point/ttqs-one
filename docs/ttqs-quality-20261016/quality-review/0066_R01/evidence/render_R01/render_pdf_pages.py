from pathlib import Path
import pypdfium2 as pdfium, json
pdf=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0066_R01\evidence\render_R01\0066_R01_word_export.pdf')
out=pdf.parent; doc=pdfium.PdfDocument(str(pdf)); pages=[]
for i,page in enumerate(doc):
    pil=page.render(scale=1.8).to_pil(); p=out/f'page-{i+1:02d}.png'; pil.save(p); pages.append({'page':i+1,'path':str(p),'width':pil.width,'height':pil.height,'bytes':p.stat().st_size})
print(json.dumps({'page_count':len(pages),'pages':pages},ensure_ascii=False))
