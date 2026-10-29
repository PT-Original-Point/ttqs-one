from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import re

root = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0008_I01-E05_LUNA_TEXT_DRAFT_R03_20261030\qa\render_R03c_native")
source = root / "png"
out = root / "contact"
out.mkdir(parents=True, exist_ok=True)
files = sorted(source.glob("page-*.png"), key=lambda p: int(re.search(r"(\d+)$", p.stem).group(1)))
box_w, box_h = 760, 1050
pad, label_h = 22, 34
try:
    font = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 18)
except OSError:
    font = ImageFont.load_default()
for start in range(0, len(files), 4):
    batch = files[start:start+4]
    sheet = Image.new("RGB", (2*box_w+3*pad, 2*(box_h+label_h)+3*pad), "white")
    draw = ImageDraw.Draw(sheet)
    for offset, path in enumerate(batch):
        page_no = int(re.search(r"(\d+)$", path.stem).group(1))
        im = Image.open(path).convert("RGB")
        im.thumbnail((box_w, box_h), Image.Resampling.LANCZOS)
        col, row = offset % 2, offset // 2
        x = pad + col*(box_w+pad) + (box_w-im.width)//2
        y = pad + row*(box_h+label_h+pad) + label_h + (box_h-im.height)//2
        draw.text((pad+col*(box_w+pad), pad+row*(box_h+label_h+pad)), f"PAGE {page_no}", fill="#17365D", font=font)
        sheet.paste(im, (x, y))
        draw.rectangle((pad+col*(box_w+pad), pad+row*(box_h+label_h+pad)+label_h, pad+col*(box_w+pad)+box_w, pad+row*(box_h+label_h+pad)+label_h+box_h), outline="#D9D9D9", width=2)
    sheet.save(out / f"sheet-{start//4+1:03d}.jpg", quality=88)
print(f"pages={len(files)} sheets={len(list(out.glob('sheet-*.jpg')))} path={out}")

