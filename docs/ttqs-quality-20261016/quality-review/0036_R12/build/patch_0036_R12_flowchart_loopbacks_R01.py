from pathlib import Path
from zipfile import ZipFile
from PIL import Image,ImageDraw,ImageFont
from hashlib import sha256
import shutil
base=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016')
r11=base/'0036_R11';r12=base/'0036_R12'
src=r11/'candidate'/'0036__課程設計進度與訓練規劃_R11.docx'
out=r12/'candidate'/'0036__課程設計進度與訓練規劃_R12.docx'
original=r12/'build'/'0036_course_design_flow_R11_original.png'
flow=r12/'build'/'0036_course_design_flow_R12.png'
assert sha256(src.read_bytes()).hexdigest()=='1e08913a7e330fcbd52f50645138f97b8c951022ef69bc5bd1ee3d2971c9a7c7'
assert sha256(original.read_bytes()).hexdigest()=='220219b638b6e240f43aeefc3b4a2d847606f67a34f58cf267dff044a0176e63'
im=Image.open(original).convert('RGB');assert im.size==(1600,1650)
d=ImageDraw.Draw(im);font=Path(r'C:\Windows\Fonts\msjh.ttc');assert font.is_file()
left_font=ImageFont.truetype(str(font),24,index=0);right_font=ImageFont.truetype(str(font),22,index=0);teal=(20,132,136)
d.line([(30,418),(14,418),(14,270),(340,270)],fill=teal,width=7,joint='curve')
d.polygon([(340,270),(317,255),(317,285)],fill=teal)
d.line([(1520,879),(1583,879),(1583,720),(1260,720)],fill=teal,width=7,joint='curve')
d.polygon([(1260,720),(1284,704),(1284,736)],fill=teal)
im.save(flow,format='PNG',optimize=True)
with ZipFile(src) as zin,ZipFile(out,'w') as zout:
 for info in zin.infolist():zout.writestr(info,flow.read_bytes() if info.filename=='word/media/image1.png' else zin.read(info.filename))
with ZipFile(src) as a,ZipFile(out) as b:
 assert set(a.namelist())==set(b.namelist()) and b.testzip() is None
 changed=[n for n in a.namelist() if sha256(a.read(n)).digest()!=sha256(b.read(n)).digest()]
 assert changed==['word/media/image1.png'],changed
shutil.copyfile(r11/'sources'/'SYNTHETIC_REPLACEMENT_REGISTER_0036_R11.csv',r12/'sources'/'SYNTHETIC_REPLACEMENT_REGISTER_0036_R12.csv')
print('SOURCE_DOCX_SHA256='+sha256(src.read_bytes()).hexdigest())
print('CANDIDATE_DOCX_SHA256='+sha256(out.read_bytes()).hexdigest())
print('CANDIDATE_BYTES='+str(out.stat().st_size))
print('FLOW_R11_SHA256='+sha256(original.read_bytes()).hexdigest())
print('FLOW_R12_SHA256='+sha256(flow.read_bytes()).hexdigest())
print('CHANGED_PACKAGE_PARTS='+','.join(changed))
