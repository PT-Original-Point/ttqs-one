from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
import hashlib, json, os

lane=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0102_I18-E09_R01_20261021')
inp=lane/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R03.docx'
out=lane/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R04.docx'
tmp=out.with_name(out.stem+'.tmp.docx')
receipt=lane/'evidence'/'docx_pagination_patch_receipt_0102_R04.json'
if not inp.is_file(): raise SystemExit('R03 input missing')
if out.exists() or tmp.exists() or receipt.exists(): raise SystemExit('Refuse overwrite R04 output/receipt')
NS='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns={'w':NS}
W=lambda name:f'{{{NS}}}{name}'
with ZipFile(inp,'r') as zin:
    names=zin.namelist()
    data={n:zin.read(n) for n in names}
root=etree.fromstring(data['word/document.xml'])
page_breaks=[]
stray_fixed=[]
for p in root.xpath('.//w:body/w:p',namespaces=ns):
    txt=''.join(p.xpath('.//w:t/text()',namespaces=ns))
    if txt.startswith('9.2 '): label='9.2 判定門檻'
    elif txt.startswith('10.1 CASE-01'): label='10.1 CASE-01'
    elif txt.startswith('11.2 '): label='11.2 本示範資料集'
    else: label=None
    if label:
        ppr=p.find(W('pPr'))
        if ppr is None:
            ppr=etree.Element(W('pPr')); p.insert(0,ppr)
        old=ppr.find(W('pageBreakBefore'))
        if old is not None: raise SystemExit(f'Already has page break: {label}')
        el=etree.Element(W('pageBreakBefore')); el.set(W('val'),'1'); ppr.append(el)
        page_breaks.append(label)
    if '`0/2=0%`' in txt:
        replaced=0
        for t in p.xpath('.//w:t',namespaces=ns):
            if t.text and '`0/2=0%`' in t.text:
                t.text=t.text.replace('`0/2=0%`','0/2=0%'); replaced+=1
        if replaced!=1: raise SystemExit(f'Expected one inline-markup repair, got {replaced}')
        stray_fixed.append({'paragraph_prefix':txt[:48],'text_nodes_repaired':replaced})
if len(page_breaks)!=3: raise SystemExit(f'Expected 3 targeted page breaks, got {page_breaks}')
if len(stray_fixed)!=1: raise SystemExit(f'Expected 1 stray markup repair, got {stray_fixed}')
data['word/document.xml']=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
footer_updates=[]
for n in names:
    if n.startswith('word/footer') and n.endswith('.xml') and b'R03' in data[n]:
        count=data[n].count(b'R03')
        if count!=1: raise SystemExit(f'Unexpected footer R03 occurrences {n}: {count}')
        data[n]=data[n].replace(b'R03',b'R04')
        footer_updates.append({'part':n,'replacements':count})
if len(footer_updates)!=1: raise SystemExit(f'Expected one footer revision update, got {footer_updates}')
with ZipFile(tmp,'w',ZIP_DEFLATED) as zout:
    for n in names: zout.writestr(n,data[n])
os.replace(tmp,out)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'doc_id':'0102','requirement_id':'I18-E09','input_docx':str(inp),'input_sha256':sha(inp),'output_docx':str(out),'output_sha256':sha(out),'bytes':out.stat().st_size,'patch_scope':'three pageBreakBefore repairs for orphaned section/table starts; one visible inline-Markdown delimiter repair; footer revision label R03 to R04','targeted_page_breaks':page_breaks,'inline_markup_fixes':stray_fixed,'footer_updates':footer_updates,'sample_boundary':'unchanged','content_source':'R03 DOCX exact bytes; no manuscript regeneration','status':'PATCHED_PENDING_WORD_EXPORT_AND_VISUAL_RECHECK'}
receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
