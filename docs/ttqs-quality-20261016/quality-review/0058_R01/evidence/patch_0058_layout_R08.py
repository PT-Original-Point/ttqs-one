from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from hashlib import sha256
from lxml import etree
import json, shutil
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0058_R01')
src=root/'candidate/0058_R06.docx'; dst=root/'candidate/0058_R08.docx'
expected='B7F8806A204EB6CB9C1F9FA2F84B016B6F1EAFB56FF43E5C7C02E2499CE13B07'
sha=lambda b:sha256(b).hexdigest().upper()
assert sha(src.read_bytes())==expected and not dst.exists()
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; q=lambda n:'{'+W+'}'+n
parser=etree.XMLParser(remove_blank_text=False,resolve_entities=False)
with ZipFile(src,'r') as zin: files={i.filename:(i,zin.read(i.filename)) for i in zin.infolist()}
rootxml=etree.fromstring(files['word/document.xml'][1],parser); body=rootxml.find('.//'+q('body'))
caption_text='表 10-3：文件修訂與版本管制紀錄表'
caption_matches=[(i,e) for i,e in enumerate(body) if e.tag==q('p') and caption_text in ''.join(e.itertext())]
assert len(caption_matches)==1
idx,caption=caption_matches[0]; assert idx+1<len(body) and body[idx+1].tag==q('tbl')
ppr=caption.find(q('pPr'))
if ppr is None:ppr=etree.Element(q('pPr'));caption.insert(0,ppr)
assert ppr.find(q('pageBreakBefore')) is None
order=['pStyle','keepNext','keepLines','pageBreakBefore','framePr','widowControl','numPr','suppressLineNumbers','pBdr','shd','tabs','suppressAutoHyphens','kinsoku','wordWrap','overflowPunct','topLinePunct','autoSpaceDE','autoSpaceDN','bidi','adjustRightInd','snapToGrid','spacing','ind','contextualSpacing','mirrorIndents','suppressOverlap','jc','textDirection','textAlignment','textboxTightWrap','outlineLvl','divId','cnfStyle','rPr','sectPr','pPrChange']
new=etree.Element(q('pageBreakBefore'));ni=order.index('pageBreakBefore');pos=len(ppr)
for j,node in enumerate(ppr):
 name=etree.QName(node).localname
 if name in order and order.index(name)>ni:pos=j;break
ppr.insert(pos,new)
table=body[idx+1]; rows=table.findall(q('tr')); assert len(rows)==8
modified=0; before_line_values=set()
for ri,row in enumerate(rows[1:],start=1):
 for p in row.iter(q('p')):
  ppr=p.find(q('pPr'))
  if ppr is None:ppr=etree.Element(q('pPr'));p.insert(0,ppr)
  spacing=ppr.find(q('spacing'))
  if spacing is None:spacing=etree.Element(q('spacing'));ppr.insert(0,spacing)
  old=spacing.get(q('line')); before_line_values.add(old)
  assert old=='276', (ri,old)
  spacing.set(q('line'),'240');spacing.set(q('lineRule'),'auto');modified+=1
assert modified==35 and before_line_values=={'276'}
newxml=etree.tostring(rootxml,xml_declaration=True,encoding='UTF-8',standalone=True)
files['word/document.xml']=(files['word/document.xml'][0],newxml)
with ZipFile(dst,'w',compression=ZIP_DEFLATED,compresslevel=6) as zout:
 for name,(info,data) in files.items():zout.writestr(info,data)
with ZipFile(src) as z0,ZipFile(dst) as z1:
 assert set(z0.namelist())==set(z1.namelist())
 diffs=[n for n in z0.namelist() if z0.read(n)!=z1.read(n)];assert diffs==['word/document.xml']
 old=etree.fromstring(z0.read('word/document.xml'),parser);new=etree.fromstring(z1.read('word/document.xml'),parser)
 cp0=next(p for p in old.iter(q('p')) if caption_text in ''.join(p.itertext()));cp1=next(p for p in new.iter(q('p')) if caption_text in ''.join(p.itertext()))
 assert ''.join(cp0.itertext())==''.join(cp1.itertext())
 for p in cp1.iter(q('pageBreakBefore')):p.getparent().remove(p)
 rows1=[e for e in new.find('.//'+q('body')) if e.tag==q('tbl')][-1].findall(q('tr'))
 for row in rows1[1:]:
  for p in row.iter(q('p')):
   sp=p.find(q('pPr')).find(q('spacing'));assert sp.get(q('line'))=='240';sp.set(q('line'),'276')
 assert etree.tostring(old,method='c14n')==etree.tostring(new,method='c14n')
 assert z0.testzip() is None and z1.testzip() is None
for oldname,newname in [('0058_SYNTHETIC_REPLACEMENT_REGISTER_R06.csv','0058_SYNTHETIC_REPLACEMENT_REGISTER_R08.csv'),('0058_CONTENT_R06.json','0058_CONTENT_R08.json')]:
 a=root/'worker/antigravity'/oldname;b=root/'worker/antigravity'/newname;assert a.exists() and not b.exists();shutil.copyfile(a,b);assert sha(a.read_bytes())==sha(b.read_bytes())
receipt={'operation':'targeted_table_layout_repair','source_revision':'R06','target_revision':'R08','source_docx_sha256':expected,'output_docx_sha256':sha(dst.read_bytes()),'candidate_path':'candidate/0058_R08.docx','root_cause':'R06 placed the Table 10-3 caption/header at the bottom of page 30. Adding pageBreakBefore moved it to page 31 but all data rows have cantSplit; at 13.8pt leading the final R06 revision row moved alone to page 33.','repair':['Move Table 10-3 caption to a new page.','Change only Table 10-3 body-cell paragraph line spacing from 13.8pt (276 twips) to 12pt (240 twips), preserving 9.5pt font, all words, data, rows, borders, and decisions.'],'modified_data_cell_paragraphs':modified,'caption_text_unchanged':True,'changed_ooxml_parts':['word/document.xml'],'other_package_parts_byte_identical':True,'document_xml_canonical_equal_after_reversing_pagebreak_and_spacing':True,'sidecars_copied_byte_identically':['0058_SYNTHETIC_REPLACEMENT_REGISTER_R08.csv','0058_CONTENT_R08.json'],'rendered_pages':'PENDING','visual_review':'PENDING','independent_semantic_review':'PENDING exact R08 SHA','formal_acceptance':'NOT_CLAIMED'}
(root/'evidence/patch_0058_layout_R08.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_sha256':expected,'output_sha256':receipt['output_docx_sha256'],'changed_parts':diffs,'paragraphs_compacted':modified,'output_bytes':dst.stat().st_size},ensure_ascii=True))