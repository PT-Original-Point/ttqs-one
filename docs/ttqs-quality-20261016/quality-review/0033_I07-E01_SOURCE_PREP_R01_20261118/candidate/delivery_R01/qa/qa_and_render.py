import json, re, sys, hashlib
from pathlib import Path
from docx import Document
import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw
docx=Path(sys.argv[1]); pdf=Path(sys.argv[2]); out=Path(sys.argv[3])
d=Document(str(docx))
paras=[p.text.strip() for p in d.paragraphs if p.text.strip()]
alltext='\n'.join(paras+[c.text for t in d.tables for row in t.rows for c in row.cells])
empty=[[ti,ri,ci] for ti,t in enumerate(d.tables) for ri,row in enumerate(t.rows) for ci,c in enumerate(row.cells) if not c.text.strip()]
body_sizes=[r.font.size.pt for p in d.paragraphs for r in p.runs if r.text.strip() and r.font.size]
table_sizes=[r.font.size.pt for t in d.tables for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs if r.text.strip() and r.font.size]
sections={str(i):any(re.match(rf'^{i}\.\s',p) for p in paras) for i in range(1,11)}
checks={
 'opens':True,'title':bool(d.core_properties.title),'sections_1_to_10':all(sections.values()),
 'all_fact_ids_01_to_18':all(f'F0033-{i:02d}' in alltext for i in range(1,19)),
 'sample_and_synthetic_labels':('SAMPLE' in alltext and 'SYNTHETIC' in alltext),
 'no_placeholder_terms':not re.search(r'待填|待核|保持空白|會後填寫|TODO|TBD',alltext),
 'no_empty_table_cells':not empty,
 'five_calculations_present':all(s in alltext for s in ['45／120＝37.5%','32／40＝80.0%','18／45＝40.0%','20／32＝62.5%','9／45＝20.0%']),
 'source_packet_bound': '303DC058B0D48D3FE4AEF1D1238F7F14F860C28259EA50901DAF750F58843F69' in alltext,
 'blueprint_bound': '06FC689334483BDCDA35076D0D9226DF0A1B01A96FD0B1F782EEAB8D1D65ACE3' in alltext,
 'body_font_floor':min(body_sizes or [0])>=10.5,'table_font_floor':min(table_sizes or [0])>=9.5,
}
out.mkdir(parents=True,exist_ok=True)
pdfdoc=pdfium.PdfDocument(str(pdf))
pages=[]
for i in range(len(pdfdoc)):
    bitmap=pdfdoc[i].render(scale=1.35)
    im=bitmap.to_pil().convert('RGB')
    dest=out/f'page-{i+1:03d}.png'; im.save(dest)
    pages.append({'page':i+1,'path':str(dest),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'width':im.width,'height':im.height})
# contact sheet at a readable overview scale
thumbs=[]
for item in pages:
    im=Image.open(item['path']).convert('RGB')
    im.thumbnail((520,735))
    canvas=Image.new('RGB',(540,775),'white')
    canvas.paste(im,((540-im.width)//2,25))
    ImageDraw.Draw(canvas).text((12,5),f"PAGE {item['page']}",fill='black')
    thumbs.append(canvas)
cols=2; rows=(len(thumbs)+cols-1)//cols
sheet=Image.new('RGB',(cols*540,rows*775),(220,220,220))
for i,im in enumerate(thumbs): sheet.paste(im,((i%cols)*540,(i//cols)*775))
sheetpath=out/'contact-sheet.png'; sheet.save(sheetpath)
result={'docx_sha256':hashlib.sha256(docx.read_bytes()).hexdigest(),'docx_bytes':docx.stat().st_size,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_bytes':pdf.stat().st_size,'paragraph_count':len(paras),'table_count':len(d.tables),'table_cell_count':sum(len(r.cells) for t in d.tables for r in t.rows),'empty_cells':empty,'body_min_pt':min(body_sizes or [0]),'table_min_pt':min(table_sizes or [0]),'section_presence':sections,'checks':checks,'static_all_pass':all(checks.values()),'page_count':len(pages),'pages':pages,'contact_sheet':str(sheetpath)}
(Path(sys.argv[4])).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('pages','checks','section_presence')},ensure_ascii=False,indent=2))
print('CHECKS='+json.dumps(checks,ensure_ascii=False))
print('SECTIONS='+json.dumps(sections))