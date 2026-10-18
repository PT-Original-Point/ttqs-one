from __future__ import annotations
import hashlib, json, zipfile, re
from pathlib import Path
from lxml import etree

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'0056_R04.docx'
OUTPUT=BASE/'0056_R05.docx'
RECEIPT=BASE/'build'/'build_receipt_R05.json'
EXPECTED='0cf37ad689906df1eadc8034d6aa39853e9d7d5454a13d000559ded790e456a6'
OLD='REQUESTED_PENDING_RESPONSE'
NEW='\u5df2\u9001\u51fa\u7d22\u53d6\uff0c\u5f85\u56de\u8986'
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
MC='{http://schemas.openxmlformats.org/markup-compatibility/2006}'
def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    if OUTPUT.exists() or RECEIPT.exists(): raise FileExistsError('R05 output/receipt exists; refusing overwrite')
    source=SOURCE.read_bytes(); source_sha=sha(source)
    if source_sha!=EXPECTED: raise RuntimeError(f'Unexpected R04 source SHA {source_sha}')
    with zipfile.ZipFile(SOURCE) as zin:
        infos=zin.infolist(); pkg={i.filename:zin.read(i.filename) for i in infos}; comment=zin.comment
    source_pkg=dict(pkg)
    root=etree.fromstring(pkg['word/document.xml']); nsmap=dict(root.nsmap)
    hits=[node for node in root.iter(W+'t') if node.text==OLD]
    if len(hits)!=1: raise RuntimeError(f'Expected one remaining status string, found {len(hits)}')
    hits[0].text=NEW
    all_text='\n'.join(''.join(n.text or '' for n in p.iter(W+'t')) for p in root.iter(W+'p'))
    schema=re.findall(r'(?<![A-Za-z0-9_])[a-z][a-z0-9]*_[a-z0-9_]+(?![A-Za-z0-9_])',all_text)
    statuses=re.findall(r'(?<![A-Za-z0-9_])[A-Z][A-Z0-9]+_[A-Z0-9_]+(?![A-Za-z0-9_])',all_text)
    if schema or statuses: raise RuntimeError(f'Human-facing control tokens remain: schema={schema}, statuses={statuses}')
    ignorable=root.get(MC+'Ignorable','').split()
    if any(prefix not in nsmap for prefix in ignorable): raise RuntimeError('Unresolved mc:Ignorable namespace')
    pkg['word/document.xml']=etree.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True,pretty_print=False)
    if dict(etree.fromstring(pkg['word/document.xml']).nsmap)!=nsmap: raise RuntimeError('Namespace map changed')
    with zipfile.ZipFile(OUTPUT,'w') as zout:
        zout.comment=comment
        for i in infos: zout.writestr(i,pkg[i.filename])
    with zipfile.ZipFile(OUTPUT) as z:
        if z.testzip() is not None: raise RuntimeError('ZIP test failed')
        out={n:z.read(n) for n in z.namelist()}
    changed=sorted(n for n in source_pkg if source_pkg[n]!=out.get(n))
    if changed!=['word/document.xml']: raise RuntimeError(f'Unexpected package changes: {changed}')
    final_sha=sha(OUTPUT.read_bytes())
    receipt={'project_id':'TTQS_ONE','doc_id':'0056','revision':'R05','official_requirement_id':'I12-E04','official_checkbox_serial':'059','status':'CANDIDATE_BUILD_ONLY_QA_PENDING','predecessor':'0056_R04.docx','predecessor_sha256':source_sha,'candidate':'0056_R05.docx','candidate_sha256':final_sha,'candidate_bytes':OUTPUT.stat().st_size,'change':'Translate the sole remaining human-facing status key to plain Traditional Chinese.','text_change_count':1,'changed_package_members':changed,'xml_namespace_map_preserved':True,'mc_ignorable_prefixes_preserved':ignorable,'remaining_schema_keys':schema,'remaining_machine_status_keys':statuses,'human_acceptance':'NOT_GRANTED','technical_visual_semantic_qa':'PENDING'}
    RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,ensure_ascii=True,indent=2))
if __name__=='__main__': main()
