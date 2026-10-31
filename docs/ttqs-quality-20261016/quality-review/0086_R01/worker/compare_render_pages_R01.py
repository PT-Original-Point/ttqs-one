from pathlib import Path
from PIL import Image,ImageDraw
import hashlib
root=Path(r"E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0086_R01/evidence")
old=root/"render_R01_final2/pages"; new=root/"render_R01_final3/pages"
def files(d):return sorted(d.glob("page-*.png"),key=lambda p:int(p.stem.split("-")[-1]))
a=files(old); b=files(new)
print("OLD_PAGES",len(a),"NEW_PAGES",len(b))
changed=[]
for i in range(max(len(a),len(b))):
 if i>=len(a) or i>=len(b):changed.append(i+1);continue
 if hashlib.sha256(a[i].read_bytes()).digest()!=hashlib.sha256(b[i].read_bytes()).digest():changed.append(i+1)
print("PIXEL_INPUT_CHANGED_PAGES",changed)
thumb_w=760;label_h=34;pad=18;gap=22
for start in range(0,len(b),4):
 subset=b[start:start+4];tiles=[]
 for fp in subset:
  im=Image.open(fp).convert("RGB");h=round(im.height*thumb_w/im.width);im=im.resize((thumb_w,h),Image.Resampling.LANCZOS);tile=Image.new("RGB",(thumb_w,h+label_h),"white");ImageDraw.Draw(tile).text((12,8),f"PAGE {int(fp.stem.split('-')[-1])}",fill="#174a75");tile.paste(im,(0,label_h));tiles.append(tile)
 th=max(t.height for t in tiles);sheet=Image.new("RGB",(pad*2+2*thumb_w+gap,pad*2+2*th+gap),"#d9dee5")
 for i,t in enumerate(tiles):sheet.paste(t,(pad+(i%2)*(thumb_w+gap),pad+(i//2)*(th+gap)))
 sheet.save(root/f"render_R01_final3/contact_{start//4+1:02d}.png")