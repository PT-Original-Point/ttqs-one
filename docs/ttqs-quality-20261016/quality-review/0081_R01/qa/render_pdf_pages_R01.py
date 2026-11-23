import sys,json
from pathlib import Path
import pypdfium2 as pdfium
pdf=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
doc=pdfium.PdfDocument(str(pdf)); rows=[]
for i,page in enumerate(doc):
    img=page.render(scale=1.5).to_pil()
    path=out/f'page-{i+1:02d}.png'; img.save(path); rows.append({'page':i+1,'path':str(path),'width':img.width,'height':img.height})
print(json.dumps({'pages':len(rows),'rendered':rows},ensure_ascii=False))
