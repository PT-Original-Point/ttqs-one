from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
root=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0075_R01\evidence\render_word_R01')
files=sorted(root.glob('page-*.png'))
font=ImageFont.load_default()
cell_w,cell_h=580,820
for start in range(0,len(files),4):
    group=files[start:start+4]
    sheet=Image.new('RGB',(cell_w*2,cell_h*2),(236,239,243))
    d=ImageDraw.Draw(sheet)
    for j,p in enumerate(group):
        im=Image.open(p).convert('RGB')
        im.thumbnail((cell_w-20,cell_h-38),Image.Resampling.LANCZOS)
        x=(j%2)*cell_w+(cell_w-im.width)//2
        y=(j//2)*cell_h+28+(cell_h-28-im.height)//2
        sheet.paste(im,(x,y))
        d.text(((j%2)*cell_w+10,(j//2)*cell_h+7),p.stem,fill=(120,0,0),font=font)
    out=root/f'contact_{start+1:02d}-{start+len(group):02d}.png'
    sheet.save(out)
    print(out)
