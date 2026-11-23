import hashlib, json, re, sys, zipfile
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET
src=Path(sys.argv[1]); dst=Path(sys.argv[2]); receipt=Path(sys.argv[3])
expected='4e2d56c9ce46b8acdb2d8b3288ed6083a054c4bb2955edf2127a4f16c058792d'
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
if sha(src)!=expected: raise SystemExit('Source candidate SHA mismatch; refusing patch.')
with zipfile.ZipFile(src,'r') as zin:
    original={i.filename:zin.read(i.filename) for i in zin.infolist()}
    infos=zin.infolist()
xml=original['word/document.xml'].decode('utf-8')
paragraphs=re.findall(r'<w:p(?: [^>]*)?>.*?</w:p>',xml,flags=re.S)
h14=[p for p in paragraphs if '14. 持續改善紀錄表' in p]
s14=[p for p in paragraphs if '14.1 空白可重用' in p]
if len(h14)!=1 or len(s14)!=1: raise SystemExit(f'Expected one heading each; got section14={len(h14)}, subsection14_1={len(s14)}')
if '<w:pageBreakBefore/>' not in s14[0]: raise SystemExit('Expected page break on 14.1 was not found.')
if '<w:pageBreakBefore/>' in h14[0]: raise SystemExit('Section 14 already has page break; refusing unintended change.')
old14=h14[0]; new14=old14.replace('<w:pStyle w:val="Heading2"/>','<w:pStyle w:val="Heading2"/><w:pageBreakBefore/>',1)
if new14==old14: raise SystemExit('Could not add page break to section 14 heading.')
olds=s14[0]; news=olds.replace('<w:pageBreakBefore/>','',1)
if news==olds: raise SystemExit('Could not remove page break from subsection 14.1.')
patched=xml.replace(old14,new14,1).replace(olds,news,1)
if patched.count('<w:t>14. 持續改善紀錄表</w:t>')!=1 or patched.count('<w:t>14.1 空白可重用（TEMPLATE／未填）</w:t>')!=1: raise SystemExit('Target heading text changed unexpectedly.')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def text_sequence(raw):
    root=ET.fromstring(raw)
    return [e.text or '' for e in root.findall('.//w:t',ns)]
if text_sequence(xml.encode())!=text_sequence(patched.encode()): raise SystemExit('Document text changed; refusing candidate.')
newfiles=dict(original); newfiles['word/document.xml']=patched.encode('utf-8')
with zipfile.ZipFile(dst,'w') as zout:
    for info in infos: zout.writestr(info,newfiles[info.filename])
with zipfile.ZipFile(dst,'r') as z:
    bad=z.testzip()
    if bad: raise SystemExit('DOCX ZIP integrity failed at '+bad)
    for info in infos:
        if info.filename!='word/document.xml' and z.read(info.filename)!=original[info.filename]: raise SystemExit('Unexpected package part changed: '+info.filename)
    finalxml=z.read('word/document.xml').decode('utf-8')
finalparas=re.findall(r'<w:p(?: [^>]*)?>.*?</w:p>',finalxml,flags=re.S)
final14=[p for p in finalparas if '14. 持續改善紀錄表' in p]
finals=[p for p in finalparas if '14.1 空白可重用' in p]
if '<w:pageBreakBefore/>' not in final14[0] or '<w:pageBreakBefore/>' in finals[0]: raise SystemExit('Page-break relocation verification failed.')
obj={'project_id':'TTQS_ONE','doc_id':'0063','revision':'R02','source_candidate':'0063_R01.docx','source_sha256':expected,'candidate_path':'candidate/0063_R02.docx','candidate_sha256':sha(dst),'change_type':'layout-only page-break relocation','defect_source':'visual_review_R04.json','change':'Relocated w:pageBreakBefore from Heading 3 “14.1 空白可重用（TEMPLATE／未填）” to Heading 2 “14. 持續改善紀錄表” so the section heading stays with its first subsection.','content_text_unchanged':True,'only_changed_package_part':'word/document.xml','all_other_package_parts_unchanged':True,'docx_zip_integrity':'PASS','targeted_property_verification':'PASS','render_and_visual_qa':'PENDING','independent_exact_sha_semantic_review':'PENDING','candidate_status':'CANDIDATE','created_utc':datetime.now(timezone.utc).isoformat()}
receipt.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(obj,ensure_ascii=False,indent=2))
