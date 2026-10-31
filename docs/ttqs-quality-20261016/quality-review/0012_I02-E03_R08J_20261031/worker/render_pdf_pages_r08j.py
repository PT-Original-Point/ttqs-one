from pathlib import Path
import json, hashlib
import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw
pdf=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\qa\R08J_SCOPED_LABEL_CLARIFICATION_20261031\render\0012_I02-E03_R08J_WORD.pdf')
out=pdf.parent/'pages'
out.mkdir(exist_ok=True)
doc=pdfium.PdfDocument(str(pdf))
texts=[]; entries=[]
for i,page in enumerate(doc):
    txt=page.get_textpage().get_text_range()
    texts.append(txt)
    im=page.render(scale=120/72).to_pil()
    p=out/f'page-{i+1:02d}.png'; im.save(p)
    entries.append({'page':i+1,'width':im.width,'height':im.height,'png':str(p),'png_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'text_excerpt':txt[:500]})
for i,txt in enumerate(texts,1):
    if '5,800' in txt or '示例折抵後' in txt or 'SYN-029' in txt:
        print('TARGET_PAGE',i,repr(txt[:2400]))
# Contact sheets of 7 pages each, retaining readable thumbnail scale.
for group in range(4):
    batch=entries[group*7:(group+1)*7]
    tiles=[]
    for e in batch:
        im=Image.open(e['png']).convert('RGB')
        im.thumbnail((650,900))
        canvas=Image.new('RGB',(670,940),'white')
        canvas.paste(im,((670-im.width)//2,25))
        ImageDraw.Draw(canvas).text((12,5),f"Page {e['page']}",fill='black')
        tiles.append(canvas)
    sheet=Image.new('RGB',(1340,3760),'#777777')
    for j,im in enumerate(tiles): sheet.paste(im,((j%2)*670,(j//2)*940))
    sheet.save(pdf.parent/f'contact-{group+1:02d}.jpg',quality=88)
manifest={'pdf_path':str(pdf),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(entries),'dpi':120,'page_images':entries}
(pdf.parent/'PAGE_RENDER_MANIFEST_R08J.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PAGE_COUNT',len(entries))
print('PDF_SHA256',manifest['pdf_sha256'])
print('MANIFEST_SHA256',hashlib.sha256((pdf.parent/'PAGE_RENDER_MANIFEST_R08J.json').read_bytes()).hexdigest())
