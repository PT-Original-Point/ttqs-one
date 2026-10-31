from pathlib import Path
import hashlib, json, math
import pypdfium2 as pdfium
from PIL import Image, ImageDraw, ImageFont
HERE=Path(__file__).resolve().parent
pdf_path=HERE/'0058_R06.pdf'
out=HERE/'pages'; out.mkdir(exist_ok=True)
doc=pdfium.PdfDocument(str(pdf_path))
page_records=[]
for i in range(len(doc)):
    page=doc[i]
    image=page.render(scale=1.6).to_pil().convert('RGB')
    path=out/f'page-{i+1:02}.png'
    image.save(path,optimize=True)
    page_records.append({'page':i+1,'width':image.width,'height':image.height,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest().upper()})
font=ImageFont.load_default()
for start in range(0,len(page_records),4):
    entries=page_records[start:start+4]
    thumbs=[]
    for rec in entries:
        im=Image.open(out/f"page-{rec['page']:02}.png").convert('RGB')
        target_w=570; target_h=round(im.height*target_w/im.width)
        im=im.resize((target_w,target_h),Image.Resampling.LANCZOS)
        tile=Image.new('RGB',(target_w+24,target_h+54),'white')
        tile.paste(im,(12,38))
        d=ImageDraw.Draw(tile); d.text((12,12),f"Page {rec['page']}",font=font,fill='black')
        thumbs.append(tile)
    cols=2; rows=math.ceil(len(thumbs)/cols); cell_w=max(t.width for t in thumbs);cell_h=max(t.height for t in thumbs)
    sheet=Image.new('RGB',(cols*cell_w+36,rows*cell_h+36),(226,228,232))
    for k,im in enumerate(thumbs): sheet.paste(im,(18+(k%2)*cell_w,18+(k//2)*cell_h))
    first=entries[0]['page']; last=entries[-1]['page']
    cp=HERE/f'contact-{first:02}-{last:02}.jpg'
    sheet.save(cp,quality=90,optimize=True)
manifest={'source_docx_sha256':'F6B5EB7A005F50352FF8A12335AED42AD13802A6CF40FC49CBDFFD005F2C72D0','pdf':{'path':pdf_path.name,'bytes':pdf_path.stat().st_size,'sha256':hashlib.sha256(pdf_path.read_bytes()).hexdigest().upper(),'page_count':len(doc)},'renderer':'Microsoft Word COM export; pypdfium2 raster scale 1.6','page_images':page_records,'contact_sheets':[{'path':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest().upper()} for p in sorted(HERE.glob('contact-*.jpg'))]}
(HERE/'render_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'page_count':len(doc),'pdf_sha256':manifest['pdf']['sha256'],'pages':len(page_records),'contact_sheets':len(manifest['contact_sheets']),'manifest_sha256':hashlib.sha256((HERE/'render_manifest.json').read_bytes()).hexdigest().upper()},indent=2))