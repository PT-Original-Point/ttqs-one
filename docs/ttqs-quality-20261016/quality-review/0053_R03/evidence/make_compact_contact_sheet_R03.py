from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03\evidence\render_final_R03')
thumb_w=270; thumb_h=382; cell_w=290; cell_h=410; cols=4; rows=5
sheet=Image.new('RGB',(cols*cell_w,rows*cell_h),(238,242,245)); draw=ImageDraw.Draw(sheet)
for n in range(1,19):
 im=Image.open(root/f'page-{n:02d}.png').convert('RGB')
 im.thumbnail((thumb_w,thumb_h),Image.Resampling.LANCZOS)
 x=((n-1)%cols)*cell_w+(cell_w-im.width)//2; y=((n-1)//cols)*cell_h+22
 sheet.paste(im,(x,y)); draw.text((((n-1)%cols)*cell_w+8,((n-1)//cols)*cell_h+4),f'PAGE {n:02d}',fill=(25,55,75))
file=root.parent/'visual_contact_sheet_R03_compact.jpg'
sheet.save(file,quality=88,optimize=True)
print(file); print('pixels',sheet.size,'bytes',file.stat().st_size)
