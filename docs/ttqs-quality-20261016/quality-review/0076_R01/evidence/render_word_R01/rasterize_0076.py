from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw
src = Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01\evidence\render_word_R01\0076_R01_word_render.pdf')
out = src.parent / 'pages'
out.mkdir(parents=True, exist_ok=True)
doc = pdfium.PdfDocument(src)
files=[]
for i in range(len(doc)):
    page=doc[i]
    bitmap=page.render(scale=1.8)
    im=bitmap.to_pil().convert('RGB')
    p=out / f'page-{i+1:02d}.png'
    im.save(p, optimize=True)
    files.append(p)
thumb_w, thumb_h = 720, 1018
for start in range(0,len(files),4):
    subset=files[start:start+4]
    sheet=Image.new('RGB',(thumb_w*2, (thumb_h+38)*2),'#d9dde3')
    draw=ImageDraw.Draw(sheet)
    for j,p in enumerate(subset):
        im=Image.open(p).convert('RGB')
        im.thumbnail((thumb_w,thumb_h),Image.Resampling.LANCZOS)
        x=(j%2)*thumb_w+(thumb_w-im.width)//2
        y=(j//2)*(thumb_h+38)+38
        sheet.paste(im,(x,y))
        draw.text(((j%2)*thumb_w+12,(j//2)*(thumb_h+38)+10),f'PAGE {start+j+1}',fill='#111827')
    sheet.save(out.parent / f'contact-{start//4+1:02d}.jpg',quality=92,optimize=True)
print('pages',len(files))
print('page_dimensions',Image.open(files[0]).size)
for p in files: print(p.name,p.stat().st_size)
