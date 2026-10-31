import os,re,sys,hashlib,json
from PIL import Image,ImageDraw,ImageFont
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE=r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0133_I19-E22_SOURCE_PREP_R01_20261024'
BODY=os.path.join(BASE,'candidate','0133_I19-E22_BODY_R01.md')
OUT=os.path.join(BASE,'candidate','0133_I19-E22_CANDIDATE_R01.docx')
CHART=os.path.join(BASE,'render','trend_0133_SAMPLE_R01.png')
FONT=r'C:\Windows\Fonts\msjh.ttc'
PAGE_W=8.27; MARGIN=0.72; CONTENT_W=PAGE_W-2*MARGIN

def sha(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def set_font(run,name='Microsoft JhengHei',size=10.5,bold=None,color=None,italic=None):
 run.font.name=name
 run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),name)
 run.font.size=Pt(size)
 if bold is not None: run.bold=bold
 if italic is not None: run.italic=italic
 if color is not None: run.font.color.rgb=RGBColor(*color)

def add_rich(p,text,size=10.5,color=None):
 # Basic Markdown emphasis; literal facts and punctuation are preserved.
 pat=re.compile(r'(\*\*.*?\*\*|`.*?`)')
 for part in pat.split(text):
  if not part: continue
  if part.startswith('**') and part.endswith('**'):
   r=p.add_run(part[2:-2]);set_font(r,size=size,bold=True,color=color)
  elif part.startswith('`') and part.endswith('`'):
   r=p.add_run(part[1:-1]);set_font(r,name='Consolas',size=max(10.5,size),color=(76,82,89))
  else:
   r=p.add_run(part);set_font(r,size=size,color=color)

def shade(cell,fill):
 tcPr=cell._tc.get_or_add_tcPr(); shd=tcPr.find(qn('w:shd'))
 if shd is None: shd=OxmlElement('w:shd');tcPr.append(shd)
 shd.set(qn('w:fill'),fill)

def set_cell_margins(cell,top=70,start=75,bottom=70,end=75):
 tc=cell._tc;tcPr=tc.get_or_add_tcPr(); mar=tcPr.first_child_found_in('w:tcMar')
 if mar is None: mar=OxmlElement('w:tcMar');tcPr.append(mar)
 for m,v in [('top',top),('start',start),('bottom',bottom),('end',end)]:
  node=mar.find(qn('w:'+m))
  if node is None: node=OxmlElement('w:'+m);mar.append(node)
  node.set(qn('w:w'),str(v));node.set(qn('w:type'),'dxa')

def set_cell_border(cell,color='A8B6C4',sz='5'):
 tc=cell._tc;tcPr=tc.get_or_add_tcPr();borders=tcPr.first_child_found_in('w:tcBorders')
 if borders is None: borders=OxmlElement('w:tcBorders');tcPr.append(borders)
 for edge in ('top','left','bottom','right','insideH','insideV'):
  tag='w:'+edge;el=borders.find(qn(tag))
  if el is None: el=OxmlElement(tag);borders.append(el)
  el.set(qn('w:val'),'single');el.set(qn('w:sz'),sz);el.set(qn('w:space'),'0');el.set(qn('w:color'),color)

def parse_row(line):
 return [x.strip() for x in line.strip().strip('|').split('|')]

def width_profile(header,n):
 h=' '.join(header)
 if n==7 and ('班次 ID' in h or '班次ID' in h): return [0.45,0.82,0.88,1.55,0.55,0.52,2.0]
 if n==9: return [0.55,0.65,0.65,0.62,0.82,0.65,0.65,0.62,0.82]
 if n==7 and ('已辦班次' in h or '參訓人次' in h): return [0.68,0.9,0.86,0.78,0.82,0.92,1.55]
 if n==6: return [0.85,0.95,1.4,0.85,0.85,1.65]
 if n==5: return [0.9,1.55,1.7,0.85,1.55]
 if n==4 and ('例外 ID' in h or '合成鍵' in h): return [0.8,1.55,2.05,2.05]
 if n==4: return [0.8,1.6,2.25,1.8]
 if n==3: return [0.95,2.95,2.55]
 if n==8: return [0.46,0.58,0.58,0.72,0.72,0.58,0.58,1.5]
 return [CONTENT_W/n]*n

def add_table(doc,rows):
 if not rows:return
 n=max(len(x) for x in rows)
 rows=[r+['']*(n-len(r)) for r in rows]
 header=rows[0]; widths=width_profile(header,n)
 if sum(widths)>CONTENT_W: widths=[w*CONTENT_W/sum(widths) for w in widths]
 table=doc.add_table(rows=1,cols=n)
 table.alignment=WD_TABLE_ALIGNMENT.CENTER;table.autofit=False
 try: table.style='Table Grid'
 except: pass
 for ri,rowdata in enumerate(rows):
  cells=table.rows[0].cells if ri==0 else table.add_row().cells
  trPr=table.rows[ri]._tr.get_or_add_trPr();cant=OxmlElement('w:cantSplit');trPr.append(cant)
  if ri==0:
   repeat=OxmlElement('w:tblHeader');repeat.set(qn('w:val'),'true');trPr.append(repeat)
  for ci,text in enumerate(rowdata):
   cell=cells[ci];cell.width=Inches(widths[ci]);cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP
   set_cell_margins(cell);set_cell_border(cell)
   if ri==0: shade(cell,'17324D')
   elif ri%2==0: shade(cell,'F2F6F9')
   p=cell.paragraphs[0];p.paragraph_format.space_before=Pt(0);p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.02
   if ri==0:
    r=p.add_run(text);set_font(r,size=9.5,bold=True,color=(255,255,255))
   else:
    add_rich(p,text,size=9.5,color=(33,43,54))
   if ci==0 and n>6: p.alignment=WD_ALIGN_PARAGRAPH.CENTER
 doc.add_paragraph().paragraph_format.space_after=Pt(2)

def create_chart():
 W,H=1700,700; im=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(im)
 def f(sz): return ImageFont.truetype(FONT,sz)
 d.text((W//2,28),'年度變化趨勢｜SAMPLE / SYNTHETIC',font=f(38),fill='#17324D',anchor='mt')
 panels=[(80,120,790,620,'已辦訓練班次',[6,8,10],['基期','+33.3%','+25.0%'],'#2563A6'),(910,120,1620,620,'參訓人次',[72,104,141],['基期','+44.4%','+35.6%'],'#14806A')]
 years=['2023','2024','2025']
 for x1,y1,x2,y2,title,vals,growth,color in panels:
  d.rounded_rectangle((x1,y1,x2,y2),radius=24,outline='#CFD8E3',width=3,fill='#FBFCFE')
  d.text(((x1+x2)//2,y1+22),title,font=f(30),fill='#23364A',anchor='mt')
  px1=x1+75;px2=x2-42;py1=y1+100;py2=y2-85
  d.line((px1,py2,px2,py2),fill='#758497',width=3);d.line((px1,py1,px1,py2),fill='#758497',width=3)
  lo=min(vals)*0.75;hi=max(vals)*1.18
  pts=[]
  for i,v in enumerate(vals):
   x=px1+int((px2-px1)*i/2);y=py2-int((v-lo)/(hi-lo)*(py2-py1));pts.append((x,y))
  for i in range(2): d.line((*pts[i],*pts[i+1]),fill=color,width=8)
  for i,(x,y) in enumerate(pts):
   d.ellipse((x-12,y-12,x+12,y+12),fill='white',outline=color,width=6)
   d.text((x,y-42),str(vals[i]),font=f(28),fill=color,anchor='ms')
   d.text((x,py2+26),years[i],font=f(24),fill='#35475A',anchor='mt')
   if i: d.text((x,y+36),growth[i],font=f(20),fill='#586B7E',anchor='mt')
 d.text((W//2,H-14),'僅為公式與表件演示；不是原始點協會實績',font=f(20),fill='#9C3B37',anchor='ms')
 im.save(CHART,dpi=(220,220))

# Page and typography
doc=Document(); sec=doc.sections[0]
sec.page_width=Inches(8.27);sec.page_height=Inches(11.69)
sec.top_margin=Inches(0.68);sec.bottom_margin=Inches(0.66);sec.left_margin=Inches(MARGIN);sec.right_margin=Inches(MARGIN)
sec.header_distance=Inches(0.30);sec.footer_distance=Inches(0.30)
styles=doc.styles
normal=styles['Normal'];normal.font.name='Microsoft JhengHei';normal._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei');normal.font.size=Pt(10.5);normal.font.color.rgb=RGBColor(32,43,55)
normal.paragraph_format.space_after=Pt(6);normal.paragraph_format.line_spacing=1.08
for sty,size,color in [('Title',25,(0,0,0)),('Heading 1',17,(23,50,77)),('Heading 2',13.5,(29,83,111)),('Heading 3',11.5,(39,99,112))]:
 s=styles[sty];s.font.name='Microsoft JhengHei';s._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei');s.font.size=Pt(size);s.font.bold=True;s.font.color.rgb=RGBColor(*color)
 s.paragraph_format.space_before=Pt(10 if sty!='Title' else 0);s.paragraph_format.space_after=Pt(5);s.paragraph_format.keep_with_next=True
# Remove title border residue
ppr=styles['Title']._element.get_or_add_pPr();pb=ppr.find(qn('w:pBdr'))
if pb is not None:ppr.remove(pb)
# Header and footer
hp=sec.header.paragraphs[0];hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=hp.add_run('TTQS ONE　｜　0133　｜　I19-E22');set_font(r,size=8.5,color=(82,99,116))
fp=sec.footer.paragraphs[0];fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=fp.add_run('SAMPLE / SYNTHETIC — NOT ASSOCIATION RECORDS　　•　　第 ');set_font(r,size=8.5,bold=True,color=(151,54,50))
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');fp._p.append(fld)
r=fp.add_run(' 頁');set_font(r,size=8.5,color=(90,102,114))
# Metadata: generic producer only; no invented human approval.
doc.core_properties.title='年度訓練班次與參訓人次趨勢表'
doc.core_properties.subject='TTQS ONE 0133 I19-E22 SAMPLE SYNTHETIC evidence-use example'
doc.core_properties.author='TTQS ONE Candidate Builder'
doc.core_properties.comments='Candidate only. REAL evidence unknown. Formal acceptance not granted.'
create_chart()
lines=open(BODY,encoding='utf-8-sig').read().splitlines();i=0;first=True
pagebreak_heads=('## 6.',)
while i<len(lines):
 line=lines[i].rstrip()
 if not line.strip():i+=1;continue
 if line.startswith('|'):
  tab=[]
  while i<len(lines) and lines[i].strip().startswith('|'):
   row=parse_row(lines[i]);
   if not all(re.fullmatch(r':?-{3,}:?',x.replace(' ','')) for x in row): tab.append(row)
   i+=1
  add_table(doc,tab);continue
 if line.startswith('# '):
  p=doc.add_paragraph(style='Title');add_rich(p,line[2:],size=25,color=(0,0,0));i+=1;continue
 if line.startswith('## '):
  p=doc.add_paragraph(style='Heading 1');p.paragraph_format.page_break_before=line.startswith(pagebreak_heads);add_rich(p,line[3:],size=17,color=(23,50,77));i+=1;continue
 if line.startswith('### '):
  p=doc.add_paragraph(style='Heading 2');add_rich(p,line[4:],size=13.5,color=(29,83,111));i+=1
  if line.startswith('### 趨勢圖讀法'):
   p=doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.keep_together=True
   shape=p.add_run().add_picture(CHART,width=Inches(6.55))
   try:
    docPr=shape._inline.docPr;docPr.set('descr','SAMPLE/SYNTHETIC annual training class counts 6, 8, 10 and participant person-times 72, 104, 141; not association results.');docPr.set('title','SAMPLE synthetic annual trend chart')
   except Exception:pass
  continue
 if line.startswith('- '):
  p=doc.add_paragraph(style='List Bullet');p.paragraph_format.left_indent=Inches(0.25);p.paragraph_format.first_line_indent=Inches(-0.16);add_rich(p,line[2:],size=10.5);i+=1;continue
 m=re.match(r'^(\d+)\.\s+(.*)$',line)
 if m:
  p=doc.add_paragraph(style='List Number');p.paragraph_format.left_indent=Inches(0.28);p.paragraph_format.first_line_indent=Inches(-0.16);add_rich(p,m.group(2),size=10.5);i+=1;continue
 if line.startswith('> '):
  p=doc.add_paragraph();p.paragraph_format.left_indent=Inches(0.2);p.paragraph_format.right_indent=Inches(0.2);p.paragraph_format.keep_together=True
  add_rich(p,line[2:],size=10.5,color=(48,68,85));i+=1;continue
 p=doc.add_paragraph();p.paragraph_format.widow_control=True;p.paragraph_format.keep_together=False
 if first and line.startswith('文件編號'):
  p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.space_before=Pt(6);p.paragraph_format.space_after=Pt(10);add_rich(p,line,size=10.5)
  for rr in p.runs: rr.font.color.rgb=RGBColor(71,91,111)
  first=False
 elif line.startswith('SAMPLE / SYNTHETIC 示範版'):
  p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.space_before=Pt(4);p.paragraph_format.space_after=Pt(13);ppr=p._p.get_or_add_pPr();sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'FCE8E6');ppr.append(sh)
  r=p.add_run(line);set_font(r,size=10.5,bold=True,color=(151,54,50))
 else:add_rich(p,line,size=10.5)
 i+=1
# Ensure all tables have consistent spacing and no extra blank pages from trailing paragraph.
for p in doc.paragraphs:
 if p.style.name.startswith('Heading'):p.paragraph_format.keep_with_next=True
# Tighten first page title block; save.
os.makedirs(os.path.dirname(OUT),exist_ok=True);doc.save(OUT)
receipt={'doc_id':'0133','requirement_id':'I19-E22','status':'CANDIDATE_BUILT_NOT_ACCEPTED','body_sha256':sha(BODY),'docx_sha256':sha(OUT),'docx_bytes':os.path.getsize(OUT),'chart_sha256':sha(CHART),'builder':'python-docx bundled runtime; chart rendered with Pillow','sample_only':True,'real_evidence':'UNKNOWN','formal_acceptance':'NOT_GRANTED'}
with open(os.path.join(BASE,'qa','BUILD_RECEIPT_0133_R01.json'),'w',encoding='utf-8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print(json.dumps(receipt,ensure_ascii=False,indent=2))
