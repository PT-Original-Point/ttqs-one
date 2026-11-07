from pathlib import Path
from PIL import Image,ImageDraw
root=Path(r"E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0086_R01/evidence/render_R01_final2")
files=sorted((root/"pages").glob("page-*.png"),key=lambda p:int(p.stem.split("-")[-1]))
thumb_w=760; label_h=34; pad=18; gap=22
for start in range(0,len(files),4):
 subset=files[start:start+4]; tiles=[]
 for fp in subset:
  im=Image.open(fp).convert("RGB"); h=round(im.height*thumb_w/im.width); im=im.resize((thumb_w,h),Image.Resampling.LANCZOS); tile=Image.new("RGB",(thumb_w,h+label_h),"white"); ImageDraw.Draw(tile).text((12,8),f"PAGE {int(fp.stem.split('-')[-1])}",fill="#174a75"); tile.paste(im,(0,label_h)); tiles.append(tile)
 th=max(t.height for t in tiles); sheet=Image.new("RGB",(pad*2+2*thumb_w+gap,pad*2+2*th+gap),"#d9dee5")
 for i,t in enumerate(tiles):sheet.paste(t,(pad+(i%2)*(thumb_w+gap),pad+(i//2)*(th+gap)))
 sheet.save(root/f"contact_{start//4+1:02d}.png")
print("FINAL_PAGES="+str(len(files)))
print("CONTACTS="+str(len(list(root.glob('contact_*.png')))))