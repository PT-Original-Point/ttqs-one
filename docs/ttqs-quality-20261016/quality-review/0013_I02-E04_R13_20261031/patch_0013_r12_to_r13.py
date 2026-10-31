import hashlib, json, shutil, zipfile
from pathlib import Path
from lxml import etree

src=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\GITHUB_STAGING\0013_I02-E04_R12_20261031\candidate\0013_I02-E04_R12.docx')
out=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\GITHUB_STAGING\0013_I02-E04_R13_20261031\candidate\0013_I02-E04_R13.docx')
receipt=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\GITHUB_STAGING\0013_I02-E04_R13_20261031\evidence\R13_PATCH_RECEIPT.json')
expected='978672ae999bbcb1a71137739428ae6d37ce475b96eb59abc8d939d3cbcdc260'
sha=lambda b: hashlib.sha256(b).hexdigest()
source_bytes=src.read_bytes()
source_sha=sha(source_bytes)
if source_sha != expected: raise SystemExit(f'SOURCE_SHA_MISMATCH:{source_sha}')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with zipfile.ZipFile(src,'r') as zin:
    payloads={i.filename:zin.read(i.filename) for i in zin.infolist()}
    infos=zin.infolist()
root=etree.fromstring(payloads['word/document.xml'])
body=root.find('w:body',namespaces=ns)

def text_of(el): return ''.join(el.xpath('.//w:t/text()',namespaces=ns))

def replace_in(el,old,new):
    changed=0
    for t in el.xpath('.//w:t',namespaces=ns):
        if t.text and old in t.text:
            t.text=t.text.replace(old,new); changed+=1
    return changed

version=[p for p in body.findall('w:p',namespaces=ns) if text_of(p).startswith('版本： R11（Word 候選；SAMPLE/SYNTHETIC）')]
if len(version)!=1: raise SystemExit(f'VERSION_PARAGRAPH_COUNT:{len(version)}')
if replace_in(version[0],'R11','R13')!=1: raise SystemExit('VERSION_PARAGRAPH_REPLACE_FAILED')
tables=body.findall('w:tbl',namespaces=ns)
if len(tables)!=20: raise SystemExit(f'TABLE_COUNT:{len(tables)}')
ver_table=tables[19]
rows=ver_table.findall('w:tr',namespaces=ns)
version_rows=[]; date_rows=[]
for ri,row in enumerate(rows):
    cells=row.findall('w:tc',namespaces=ns)
    vals=[text_of(c) for c in cells]
    if len(vals)>=2 and vals[0]=='版本': version_rows.append((ri,cells[1]))
    if len(vals)>=2 and vals[0]=='草稿日期': date_rows.append((ri,cells[1]))
if len(version_rows)!=1 or text_of(version_rows[0][1])!='R11': raise SystemExit('VERSION_TABLE_CELL_MISMATCH')
if replace_in(version_rows[0][1],'R11','R13')!=1: raise SystemExit('VERSION_CELL_REPLACE_FAILED')
if len(date_rows)!=1 or text_of(date_rows[0][1])!='2026-10-30': raise SystemExit('DRAFT_DATE_CELL_MISMATCH')
if replace_in(date_rows[0][1],'2026-10-30','2026-10-31')!=1: raise SystemExit('DRAFT_DATE_REPLACE_FAILED')

prose=[p for p in body.findall('w:p',namespaces=ns) if text_of(p).startswith('遮蔽本件標題、檔名及編號後，正文仍能由年度公開課程欄位')]
if len(prose)!=1: raise SystemExit(f'ORPHAN_PARAGRAPH_COUNT:{len(prose)}')
items=list(body); idx=items.index(prose[0]);
section_break=None
for node in items[idx+1:]:
    if node.tag==f'{{{ns["w"]}}}p' and node.find('w:pPr/w:sectPr',namespaces=ns) is not None:
        section_break=node; break
    if node.tag==f'{{{ns["w"]}}}p':
        ts=text_of(node)
        if ts.startswith('12.') and section_break is None: break
if section_break is None: raise SystemExit('SECTION_BREAK_AFTER_ORPHAN_NOT_FOUND')
# Move only the conclusion paragraph to the portrait section immediately after the existing section break.
body.remove(prose[0]); section_break.addnext(prose[0])

payloads['word/document.xml']=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
out.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(out,'w') as zout:
    for info in infos:
        zout.writestr(info,payloads[info.filename])
new=out.read_bytes(); new_sha=sha(new)
with zipfile.ZipFile(out,'r') as z:
    bad=z.testzip()
    changed=[n for n in payloads if z.read(n)!=payloads[n]]
    only_docxml=all((n=='word/document.xml' or z.read(n)==zipfile.ZipFile(src).read(n)) for n in payloads)
result={
 'project_id':'TTQS_ONE','doc_id':'0013','requirement_id':'I02-E04','revision':'R13',
 'source_candidate_path':str(src),'source_candidate_sha256':source_sha,
 'candidate_path':str(out),'candidate_sha256':new_sha,'candidate_bytes':len(new),
 'changes':[
  {'locator':'§14 visible version paragraph','from':'R11','to':'R13'},
  {'locator':'§14 version table row','from':'R11','to':'R13'},
  {'locator':'§14 draft date','from':'2026-10-30','to':'2026-10-31'},
  {'locator':'section 11.2 closing paragraph','change':'moved across the existing landscape-to-portrait section break to immediately before heading 12; wording preserved'}
 ],
 'zip_integrity':'PASS' if bad is None else f'FAIL:{bad}',
 'modified_package_parts':changed,
 'all_other_package_parts_preserved':only_docxml,
 'visual_qa':'PENDING','semantic_review':'PENDING','formal_acceptance':'NOT_ACCEPTED',
 'sample_real_state':'SAMPLE_SYNTHETIC_CANDIDATE'
}
receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
