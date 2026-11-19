from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from hashlib import sha256
from lxml import etree
import json, shutil
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0058_R01')
src=root/'candidate/0058_R06.docx'; dst=root/'candidate/0058_R07.docx'
expected='B7F8806A204EB6CB9C1F9FA2F84B016B6F1EAFB56FF43E5C7C02E2499CE13B07'
sha=lambda b:sha256(b).hexdigest().upper()
assert sha(src.read_bytes())==expected
assert not dst.exists(), 'Refusing to overwrite an existing R07 candidate.'
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q=lambda name:f'{{{W}}}{name}'
parser=etree.XMLParser(remove_blank_text=False,resolve_entities=False)
with ZipFile(src,'r') as zin:
    files={info.filename:(info,zin.read(info.filename)) for info in zin.infolist()}
xml=files['word/document.xml'][1]
rootxml=etree.fromstring(xml,parser)
body=rootxml.find('.//'+q('body'))
caption_text='表 10-3：文件修訂與版本管制紀錄表'
matches=[]
for i,child in enumerate(body):
    if child.tag==q('p'):
        text=''.join(child.itertext())
        if caption_text in text: matches.append((i,child,text))
assert len(matches)==1, f'Expected one Table 10-3 caption, got {len(matches)}'
idx,caption,text=matches[0]
assert idx+1<len(body) and body[idx+1].tag==q('tbl'), 'Caption must directly precede its table.'
ppr=caption.find(q('pPr'))
if ppr is None:
    ppr=etree.Element(q('pPr')); caption.insert(0,ppr)
assert ppr.find(q('pageBreakBefore')) is None, 'Source already has pageBreakBefore.'
# Insert pageBreakBefore in the OOXML paragraph-property schema order.
order=['pStyle','keepNext','keepLines','pageBreakBefore','framePr','widowControl','numPr','suppressLineNumbers','pBdr','shd','tabs','suppressAutoHyphens','kinsoku','wordWrap','overflowPunct','topLinePunct','autoSpaceDE','autoSpaceDN','bidi','adjustRightInd','snapToGrid','spacing','ind','contextualSpacing','mirrorIndents','suppressOverlap','jc','textDirection','textAlignment','textboxTightWrap','outlineLvl','divId','cnfStyle','rPr','sectPr','pPrChange']
new=etree.Element(q('pageBreakBefore'))
new_i=order.index('pageBreakBefore')
insert_at=len(ppr)
for j,node in enumerate(ppr):
    local=etree.QName(node).localname
    if local in order and order.index(local)>new_i:
        insert_at=j; break
ppr.insert(insert_at,new)
newxml=etree.tostring(rootxml,xml_declaration=True,encoding='UTF-8',standalone=True)
assert caption.find(q('pPr')).find(q('pageBreakBefore')) is not None
files['word/document.xml']=(files['word/document.xml'][0],newxml)
with ZipFile(dst,'w',compression=ZIP_DEFLATED,compresslevel=6) as zout:
    for name,(info,data) in files.items(): zout.writestr(info,data)
# Verify only the target paragraph property changed at the XML tree level.
with ZipFile(src) as z1, ZipFile(dst) as z2:
    assert set(z1.namelist())==set(z2.namelist())
    diffs=[n for n in z1.namelist() if z1.read(n)!=z2.read(n)]
    assert diffs==['word/document.xml'],diffs
    before=etree.fromstring(z1.read('word/document.xml'),parser)
    after=etree.fromstring(z2.read('word/document.xml'),parser)
    cap1=next(p for p in before.iter(q('p')) if caption_text in ''.join(p.itertext()))
    cap2=next(p for p in after.iter(q('p')) if caption_text in ''.join(p.itertext()))
    assert ''.join(cap1.itertext())==''.join(cap2.itertext())
    for p in cap2.iter(q('pageBreakBefore')): p.getparent().remove(p)
    assert etree.tostring(before,method='c14n')==etree.tostring(after,method='c14n')
    assert z1.testzip() is None and z2.testzip() is None
for old,newname in [('0058_SYNTHETIC_REPLACEMENT_REGISTER_R06.csv','0058_SYNTHETIC_REPLACEMENT_REGISTER_R07.csv'),('0058_CONTENT_R06.json','0058_CONTENT_R07.json')]:
    source=root/'worker/antigravity'/old; target=root/'worker/antigravity'/newname
    assert source.exists() and not target.exists(); shutil.copyfile(source,target)
receipt={
 'operation':'targeted_layout_repair','source_revision':'R06','target_revision':'R07',
 'source_docx_sha256':expected,'output_docx_sha256':sha(dst.read_bytes()),
 'candidate_path':'candidate/0058_R07.docx','target_defect':'Table 10-3 caption and header were stranded at the bottom of rendered page 30 while data rows began on page 31.',
 'repair':'Set pageBreakBefore on the exact Table 10-3 caption paragraph; no wording, data, table, or decision changed.',
 'source_caption_text':text,'caption_followed_by_table':True,'package_parts_changed':['word/document.xml'],
 'all_other_uncompressed_package_parts_identical':True,'canonical_document_xml_equal_after_removing_added_page_break':True,
 'sidecars_copied_byte_identically':['0058_SYNTHETIC_REPLACEMENT_REGISTER_R07.csv','0058_CONTENT_R07.json'],
 'semantic_review':'PENDING exact R07 SHA','visual_review':'PENDING fresh R07 Word render','formal_acceptance':'NOT_CLAIMED'
}
(root/'evidence/patch_0058_layout_R07.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_sha256':expected,'output_sha256':receipt['output_docx_sha256'],'changed_parts':diffs,'caption_text_sha256':sha(text.encode()),'output_bytes':dst.stat().st_size},ensure_ascii=True))