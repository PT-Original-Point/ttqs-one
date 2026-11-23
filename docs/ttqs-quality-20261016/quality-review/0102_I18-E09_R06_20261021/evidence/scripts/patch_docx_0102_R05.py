from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
import hashlib, json, os

lane=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0102_I18-E09_R01_20261021')
inp=lane/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R04.docx'
out=lane/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R05.docx'
tmp=out.with_name(out.stem+'.tmp.docx')
receipt=lane/'evidence'/'docx_typography_patch_receipt_0102_R05.json'
if not inp.is_file(): raise SystemExit('R04 input missing')
if out.exists() or tmp.exists() or receipt.exists(): raise SystemExit('Refuse overwrite R05 output/receipt')
NS='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns={'w':NS}
W=lambda name:f'{{{NS}}}{name}'
with ZipFile(inp,'r') as zin:
    names=zin.namelist()
    data={n:zin.read(n) for n in names}
root=etree.fromstring(data['word/document.xml'])
counts={'body_runs_raised_to_10_5pt':0,'table_runs_raised_to_9_5pt':0,'body_szCs_added_or_raised':0,'table_szCs_added_or_raised':0}
sizes_before={'body':{},'table':{}}
sizes_after={'body':{},'table':{}}
def bump_runs(el, location, floor):
    for run in el.xpath('.//w:r[.//w:t]',namespaces=ns):
        rpr=run.find(W('rPr'))
        if rpr is None:
            rpr=etree.Element(W('rPr'))
            run.insert(0,rpr)
        sz=rpr.find(W('sz'))
        if sz is None:
            raise SystemExit(f'Missing explicit w:sz in {location} run')
        original=int(sz.get(W('val')))
        sizes_before[location][str(original)]=sizes_before[location].get(str(original),0)+1
        target=max(original,floor)
        if target!=original:
            sz.set(W('val'),str(target))
            counts['body_runs_raised_to_10_5pt' if location=='body' else 'table_runs_raised_to_9_5pt']+=1
        cs=rpr.find(W('szCs'))
        if cs is None:
            cs=etree.Element(W('szCs')); rpr.append(cs)
        cs_original=int(cs.get(W('val'))) if cs.get(W('val')) else 0
        cs_target=max(cs_original,target,floor)
        if cs_original<floor:
            counts['body_szCs_added_or_raised' if location=='body' else 'table_szCs_added_or_raised']+=1
        cs.set(W('val'),str(cs_target))
        sizes_after[location][str(target)]=sizes_after[location].get(str(target),0)+1
body=root.find('.//w:body',ns)
for child in body:
    if child.tag==W('tbl'):
        bump_runs(child,'table',19)
    elif child.tag==W('p'):
        bump_runs(child,'body',21)
data['word/document.xml']=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
styles=etree.fromstring(data['word/styles.xml'])
style_targets={'Normal':21,'BodyText3':21,'BodyText3Char':21,'Caption':21,'Heading8':21,'Heading9':21,'MacroText':21,'MacroTextChar':21}
updated_styles=[]
for style in styles.xpath('.//w:style',namespaces=ns):
    sid=style.get(W('styleId'))
    if sid not in style_targets: continue
    floor=style_targets[sid]
    for tag in ('sz','szCs'):
        el=style.find('w:rPr/w:'+tag,ns)
        if el is not None and (el.get(W('val')) is None or int(el.get(W('val')))<floor):
            old=el.get(W('val'))
            el.set(W('val'),str(floor))
            updated_styles.append({'style_id':sid,'element':tag,'from':old,'to':floor})
data['word/styles.xml']=etree.tostring(styles,xml_declaration=True,encoding='UTF-8',standalone=True)
footer_updates=[]
for n in names:
    if n.startswith('word/footer') and n.endswith('.xml') and b'R04' in data[n]:
        count=data[n].count(b'R04')
        if count!=1: raise SystemExit(f'Unexpected footer R04 occurrences {n}: {count}')
        data[n]=data[n].replace(b'R04',b'R05')
        footer_updates.append({'part':n,'replacements':count})
if len(footer_updates)!=1: raise SystemExit(f'Expected one footer revision update, got {footer_updates}')
with ZipFile(tmp,'w',ZIP_DEFLATED) as zout:
    for n in names: zout.writestr(n,data[n])
os.replace(tmp,out)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'doc_id':'0102','requirement_id':'I18-E09','input_docx':str(inp),'input_sha256':sha(inp),'output_docx':str(out),'output_sha256':sha(out),'bytes':out.stat().st_size,'patch_scope':'raise all explicit body run sizes below 10.5pt to 10.5pt and all table-cell run sizes below 9.5pt to 9.5pt; add matching complex-script sizes; raise body style defaults; update footer revision R04 to R05; no manuscript text changes','raised_run_counts':counts,'before_half_point_distribution':sizes_before,'after_half_point_distribution':sizes_after,'updated_styles':updated_styles,'footer_updates':footer_updates,'status':'PATCHED_PENDING_NATIVE_WORD_EXPORT_TECHNICAL_QA_AND_VISUAL_REVIEW'}
receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
