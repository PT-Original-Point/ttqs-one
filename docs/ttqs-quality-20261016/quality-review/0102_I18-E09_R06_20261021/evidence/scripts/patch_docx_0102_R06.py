from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
import hashlib,json,os

lane=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0102_I18-E09_R01_20261021')
inp=lane/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R05.docx'
out=lane/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R06.docx'
tmp=out.with_name(out.stem+'.tmp.docx')
receipt=lane/'evidence'/'docx_pagination_patch_receipt_0102_R06.json'
if not inp.is_file(): raise SystemExit('R05 input missing')
if out.exists() or tmp.exists() or receipt.exists(): raise SystemExit('Refuse overwrite R06 output/receipt')
NS='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns={'w':NS}
W=lambda n:f'{{{NS}}}{n}'
with ZipFile(inp,'r') as z:
    names=z.namelist(); data={n:z.read(n) for n in names}
root=etree.fromstring(data['word/document.xml'])
actions=[]
targets={
 '4.2 已填 SAMPLE': 'ADD',
 '8.4 已填 SAMPLE': 'ADD',
 '10.1 CASE-01': 'REMOVE',
 '11.2 本示範資料集': 'REMOVE'
}
seen={k:0 for k in targets}
for p in root.xpath('.//w:body/w:p',namespaces=ns):
    txt=''.join(p.xpath('.//w:t/text()',namespaces=ns))
    key=next((k for k in targets if txt.startswith(k)),None)
    if key is None: continue
    seen[key]+=1
    ppr=p.find(W('pPr'))
    if targets[key]=='ADD':
        if ppr is None:
            ppr=etree.Element(W('pPr')); p.insert(0,ppr)
        if ppr.find(W('pageBreakBefore')) is not None:
            raise SystemExit(f'Unexpected existing page break on {key}')
        pb=etree.Element(W('pageBreakBefore')); pb.set(W('val'),'1'); ppr.append(pb)
        actions.append({'target':key,'action':'ADD_pageBreakBefore'})
    else:
        if ppr is None or ppr.find(W('pageBreakBefore')) is None:
            raise SystemExit(f'Expected existing page break missing on {key}')
        ppr.remove(ppr.find(W('pageBreakBefore')))
        actions.append({'target':key,'action':'REMOVE_pageBreakBefore'})
if any(v!=1 for v in seen.values()):
    raise SystemExit(f'Expected exactly one heading match each, got {seen}')
data['word/document.xml']=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
footer_updates=[]
for n in names:
    if n.startswith('word/footer') and n.endswith('.xml') and b'R05' in data[n]:
        count=data[n].count(b'R05')
        if count!=1: raise SystemExit(f'Unexpected footer R05 count in {n}: {count}')
        data[n]=data[n].replace(b'R05',b'R06')
        footer_updates.append({'part':n,'replacements':count})
if len(footer_updates)!=1: raise SystemExit(f'Expected exactly one footer revision update, got {footer_updates}')
with ZipFile(tmp,'w',ZIP_DEFLATED) as z:
    for n in names: z.writestr(n,data[n])
os.replace(tmp,out)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'doc_id':'0102','official_requirement_id':'I18-E09','input_sha256':sha(inp),'output_sha256':sha(out),'output_path':str(out),'patch_scope':'two section/table starts moved off orphaned page footers; two unnecessary forced page breaks removed; no manuscript or source text changes; candidate footer revision R05 to R06','pagination_actions':actions,'footer_updates':footer_updates,'status':'PATCHED_PENDING_WORD_EXPORT_AND_FULL_VISUAL_RECHECK'}
receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
