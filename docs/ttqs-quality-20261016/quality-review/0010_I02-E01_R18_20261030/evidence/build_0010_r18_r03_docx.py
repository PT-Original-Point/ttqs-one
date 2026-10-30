from pathlib import Path
from hashlib import sha256
import json,re
from datetime import datetime
from zoneinfo import ZoneInfo
from docx import Document
from docx.enum.section import WD_ORIENT,WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT,WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches,Pt,RGBColor

ROOT=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030')
SOURCE=ROOT/'worker'/'0010_I02-E01_R18_R02.md'
OUTPUT=ROOT/'candidate'/'0010_I02-E01_R18_R03.docx'
FONT='Microsoft JhengHei'; NAVY='17365D'; PALE='EAF1F8'; GRID='D9E2F3'

def digest(p):return sha256(p.read_bytes()).hexdigest()
def set_font(run,size=10.5,bold=None,color='000000',italic=None):
 run.font.name=FONT
 rp=run._element.get_or_add_rPr()
 rfonts=rp.rFonts
 if rfonts is None:
  rfonts=OxmlElement('w:rFonts');rp.insert(0,rfonts)
 for k in ('ascii','hAnsi','eastAsia','cs'):rfonts.set(qn('w:'+k),FONT)
 run.font.size=Pt(size);run.font.color.rgb=RGBColor.from_string(color)
 if bold is not None:run.bold=bold
 if italic is not None:run.italic=italic

def inline(p,text,size=10.5,bold=False,color='000000'):
 rx=re.compile(r'(\*\*.*?\*\*|(?<!\*)\*[^*]+\*(?!\*))');pos=0
 for m in rx.finditer(text):
  if m.start()>pos:set_font(p.add_run(text[pos:m.start()]),size,bold,color)
  tok=m.group(0)
  if tok.startswith('**'):set_font(p.add_run(tok[2:-2]),size,True,color)
  else:set_font(p.add_run(tok[1:-1]),size,bold,color,True)
  pos=m.end()
 if pos<len(text):set_font(p.add_run(text[pos:]),size,bold,color)

def shade(cell,fill):
 tcpr=cell._tc.get_or_add_tcPr();el=tcpr.find(qn('w:shd'))
 if el is None:el=OxmlElement('w:shd');tcpr.append(el)
 el.set(qn('w:fill'),fill)

def margins(cell):
 tcpr=cell._tc.get_or_add_tcPr();mar=tcpr.first_child_found_in('w:tcMar')
 if mar is None:mar=OxmlElement('w:tcMar');tcpr.append(mar)
 for edge,val in [('top','75'),('start','75'),('bottom','75'),('end','75')]:
  e=OxmlElement('w:'+edge);e.set(qn('w:w'),val);e.set(qn('w:type'),'dxa');mar.append(e)

def borders(table):
 pr=table._tbl.tblPr;b=pr.first_child_found_in('w:tblBorders')
 if b is None:b=OxmlElement('w:tblBorders');pr.append(b)
 for edge in ('top','left','bottom','right','insideH','insideV'):
  e=OxmlElement('w:'+edge);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),GRID);b.append(e)

def repeat_header(row):row._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
def keep_row(row):row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))

def add_page_field(p):
 r=p.add_run();set_font(r,8.5,color='52647A')
 begin=OxmlElement('w:fldChar');begin.set(qn('w:fldCharType'),'begin')
 instr=OxmlElement('w:instrText');instr.set(qn('xml:space'),'preserve');instr.text=' PAGE '
 sep=OxmlElement('w:fldChar');sep.set(qn('w:fldCharType'),'separate')
 val=OxmlElement('w:t');val.text='1'
 end=OxmlElement('w:fldChar');end.set(qn('w:fldCharType'),'end')
 r._r.extend([begin,instr,sep,val,end])

def config_section(sec,landscape=False):
 sec.orientation=WD_ORIENT.LANDSCAPE if landscape else WD_ORIENT.PORTRAIT
 if landscape:sec.page_width,sec.page_height=Inches(11.69),Inches(8.27);sec.left_margin=sec.right_margin=Inches(.42);sec.top_margin=sec.bottom_margin=Inches(.50)
 else:sec.page_width,sec.page_height=Inches(8.27),Inches(11.69);sec.left_margin=sec.right_margin=Inches(.68);sec.top_margin=Inches(.67);sec.bottom_margin=Inches(.65)
 sec.header_distance=sec.footer_distance=Inches(.28);sec.header.is_linked_to_previous=False;sec.footer.is_linked_to_previous=False
 h=sec.header.paragraphs[0];h.alignment=WD_ALIGN_PARAGRAPH.RIGHT;set_font(h.add_run('TTQS ONE  |  0010  |  I02-E01  |  CANDIDATE  |  SAMPLE / SYNTHETIC'),8.5,color='52647A')
 f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.CENTER;set_font(f.add_run('非核定示範  ·  頁 '),8.5,color='52647A');add_page_field(f)

def section_mode(line):
 if re.match(r'^##\s+(3\.|4\.|5\.|6\.|7\.|8\.|9\.|10\.|11\.|15\.)',line):return True
 if re.match(r'^##\s+(12\.|13\.|14\.)',line):return False
 return None

def split_row(line):
 s=line.strip();s=s[1:] if s.startswith('|') else s;s=s[:-1] if s.endswith('|') else s
 cells=[];cur=[];esc=False
 for ch in s:
  if ch=='|' and not esc:cells.append(''.join(cur).strip());cur=[]
  else:cur.append(ch)
  if ch=='\\' and not esc:esc=True
  else:esc=False
 cells.append(''.join(cur).strip())
 return [x.replace(r'\|','|').replace(r'\\','\\') for x in cells]

def separator(line):return bool(re.match(r'^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$',line))

def table_widths(header,landscape):
 n=len(header);usable=10.55 if landscape else 6.90;first=header[0].strip().lower() if header else ''
 special={
  (6,'目標'):[.65,1.25,.55,2.7,2.15,3.25],
  (6,'題'):[.45,1.70,2.0,2.0,2.0,2.0],
  (6,'指標'):[.62,1.98,1.98,1.98,1.98,1.98],
  (8,'個案'):[.83,3.50,.75,1.30,1.30,1.05,.75,1.07],
  (7,'ev id'):[1.50,.75,.75,4.20,1.35,.55,1.45],
  (5,'個案'):[.80,1.23,1.35,1.40,5.77],
  (4,'新測驗向量'):[1.05,1.08,7.35,1.07],
  (6,'ev id'):[1.72,.82,.75,1.2,4.55,1.25],
  (6,'fact id'):[1.18,1.22,1.12,2.10,2.30,2.57],
  (9,'fact id'):[.65,1.05,.85,1.35,1.30,1.05,1.55,1.45,1.30],
  (3,'統計'):[1.65,2.10,3.15],
 }
 values=special.get((n,first))
 if values and abs(sum(values)-usable)<.20:return values
 weights=[max(1,len(x)) for x in header];return [usable*w/sum(weights) for w in weights]

def add_table(doc,rows,landscape):
 if not rows:return
 n=max(len(r) for r in rows);rows=[r+['']*(n-len(r)) for r in rows]
 t=doc.add_table(rows=1,cols=n);t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False;t.style='Table Grid';borders(t)
 ws=table_widths(rows[0],landscape)
 for i,w in enumerate(ws):t.columns[i].width=Inches(w)
 repeat_header(t.rows[0])
 for ri,vals in enumerate(rows):
  row=t.rows[0] if ri==0 else t.add_row();keep_row(row)
  for ci,val in enumerate(vals):
   c=row.cells[ci];c.width=Inches(ws[ci]);c.text='';p=c.paragraphs[0]
   p.paragraph_format.space_before=Pt(0);p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.04
   if ri==0:p.paragraph_format.keep_with_next=True
   p.alignment=WD_ALIGN_PARAGRAPH.CENTER if ri==0 or (ci==0 and n>3) else WD_ALIGN_PARAGRAPH.LEFT
   inline(p,val,9.5,bold=(ri==0),color='FFFFFF' if ri==0 else '000000');c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER;margins(c)
   if ri==0:shade(c,NAVY)
   elif ri%2==0:shade(c,PALE)

def main():
 if OUTPUT.exists():raise FileExistsError(OUTPUT)
 lines=SOURCE.read_text(encoding='utf-8-sig').splitlines()
 d=Document();normal=d.styles['Normal'];normal.font.name=FONT;normal._element.rPr.rFonts.set(qn('w:eastAsia'),FONT);normal.font.size=Pt(10.5);normal.paragraph_format.space_after=Pt(5);normal.paragraph_format.line_spacing=1.10
 for name,size in [('Title',23),('Heading 1',15),('Heading 2',12.5),('Heading 3',11)]:
  st=d.styles[name];st.font.name=FONT;st._element.rPr.rFonts.set(qn('w:eastAsia'),FONT);st.font.size=Pt(size);st.font.bold=True;st.paragraph_format.keep_with_next=True;st.paragraph_format.space_before=Pt(10);st.paragraph_format.space_after=Pt(5)
 d.styles['Caption'].font.name=FONT;d.styles['Caption'].font.size=Pt(10.5);d.styles['Caption'].font.bold=True;d.styles['Caption'].paragraph_format.keep_with_next=True
 landscape=False;config_section(d.sections[0],False);title_written=False;i=0;code_mode=False
 while i<len(lines):
  line=lines[i].rstrip()
  if line.startswith('```'):code_mode=not code_mode;i+=1;continue
  if code_mode:
   p=d.add_paragraph();p.paragraph_format.left_indent=Inches(.25);inline(p,line,size=10.5);i+=1;continue
  if not line.strip():i+=1;continue
  want=section_mode(line)
  if want is not None and want!=landscape:
   sec=d.add_section(WD_SECTION.NEW_PAGE);config_section(sec,want);landscape=want
  if line.startswith('# '):
   title=re.sub(r'^#\s*','',line);title=re.sub(r'[｜|]\s*R\d+(?:[a-z])?\s*$','',title).strip()
   p=d.add_paragraph(style='Title' if not title_written else 'Heading 1')
   inline(p,('0010 '+title) if not title_written else title,size=23 if not title_written else 15,bold=True);title_written=True;i+=1;continue
  h=re.match(r'^(#{2,4})\s+(.*)$',line)
  if h:
   style={2:'Heading 1',3:'Heading 2',4:'Heading 3'}[len(h.group(1))];p=d.add_paragraph(style=style);inline(p,h.group(2),size={'Heading 1':15,'Heading 2':12.5,'Heading 3':11}[style],bold=True);i+=1;continue
  if line.lstrip().startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].lstrip().startswith('|'):
    cur=lines[i].strip()
    if not separator(cur):rows.append(split_row(cur))
    i+=1
   add_table(d,rows,landscape);continue
  if re.match(r'^\s*[-*]\s+',line):
   p=d.add_paragraph(style='List Bullet');p.paragraph_format.space_after=Pt(4);inline(p,re.sub(r'^\s*[-*]\s+','',line));i+=1;continue
  if re.match(r'^\s*\d+\.\s+',line):
   p=d.add_paragraph(style='List Number');p.paragraph_format.space_after=Pt(4);inline(p,re.sub(r'^\s*\d+\.\s+','',line));i+=1;continue
  if line.startswith('**') and line.endswith('**'):
   p=d.add_paragraph(style='Caption');inline(p,line[2:-2],size=10.5,bold=True);i+=1;continue
  p=d.add_paragraph();inline(p,line);i+=1
 d.core_properties.title='0010 學員訓練成果評核標準與說明'
 d.core_properties.subject='I02-E01；SAMPLE/SYNTHETIC候選，不代表核定或實際施測'
 d.core_properties.keywords='TTQS ONE, 0010, I02-E01, SAMPLE, SYNTHETIC, candidate'
 OUTPUT.parent.mkdir(parents=True,exist_ok=True);d.save(OUTPUT)
 print(json.dumps({'docx':str(OUTPUT),'sha256':digest(OUTPUT),'bytes':OUTPUT.stat().st_size,'paragraphs':len(d.paragraphs),'tables':len(d.tables),'sections':len(d.sections),'source_sha256':digest(SOURCE),'built_at_taipei':datetime.now().astimezone().isoformat()},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
