from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from hashlib import sha256
import json
lane=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0102_I18-E09_R01_20261021')
doc=lane/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R06.docx'
pdf=lane/'render'/'R06_final'/'0102_word_native_export.pdf'
prior=lane/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R04.docx'
out=lane/'evidence'/'technical_qa_receipt_0102_R06.json'
NS='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; ns={'w':NS}; q='{%s}'%NS
with ZipFile(doc) as z:
    bad=z.testzip()
    if bad: raise SystemExit('ZIP CRC failure: '+bad)
    xmlparts=[n for n in z.namelist() if n.startswith('word/') and n.endswith('.xml')]
    parsed={n:etree.fromstring(z.read(n)) for n in xmlparts}
root=parsed['word/document.xml']; body=root.find('.//w:body',ns)
body_sizes=[]; table_sizes=[]; body_cs=[]; table_cs=[]; rows=[]; unsplit=0
for child in body:
    if child.tag==q+'tbl':
        for run in child.xpath('.//w:r[.//w:t]',namespaces=ns):
            rpr=run.find(q+'rPr'); sz=rpr.find(q+'sz') if rpr is not None else None; cs=rpr.find(q+'szCs') if rpr is not None else None
            table_sizes.append(int(sz.get(q+'val')) if sz is not None else 0)
            table_cs.append(int(cs.get(q+'val')) if cs is not None else 0)
        trs=child.findall('.//w:tr',ns); rows.extend(trs)
        unsplit+=sum(1 for tr in trs if tr.find('w:trPr/w:cantSplit',ns) is not None)
    elif child.tag==q+'p':
        for run in child.xpath('.//w:r[.//w:t]',namespaces=ns):
            rpr=run.find(q+'rPr'); sz=rpr.find(q+'sz') if rpr is not None else None; cs=rpr.find(q+'szCs') if rpr is not None else None
            body_sizes.append(int(sz.get(q+'val')) if sz is not None else 0)
            body_cs.append(int(cs.get(q+'val')) if cs is not None else 0)
txt=''.join(root.xpath('.//w:body//w:t/text()',namespaces=ns))
def paragraph(prefix):
    for p in root.xpath('.//w:body/w:p',namespaces=ns):
        s=''.join(p.xpath('.//w:t/text()',namespaces=ns))
        if s.startswith(prefix): return p
    raise SystemExit('missing paragraph '+prefix)
breaks={}
for label in ['4.2 已填 SAMPLE','8.4 已填 SAMPLE','9.2 判定門檻','10.1 CASE-01','11.2 本示範資料集']:
    p=paragraph(label)
    breaks[label]=p.find('w:pPr/w:pageBreakBefore',ns) is not None
with ZipFile(prior) as z: priorroot=etree.fromstring(z.read('word/document.xml'))
priortext=''.join(priorroot.xpath('.//w:body//w:t/text()',namespaces=ns))
if txt!=priortext: raise SystemExit('Body text differs from R04')
assert min(body_sizes)>=21 and min(body_cs)>=21, (min(body_sizes),min(body_cs))
assert min(table_sizes)>=19 and min(table_cs)>=19, (min(table_sizes),min(table_cs))
assert all(breaks[k] for k in ['4.2 已填 SAMPLE','8.4 已填 SAMPLE','9.2 判定門檻'])
assert not breaks['10.1 CASE-01'] and not breaks['11.2 本示範資料集']
assert (chr(96)+'0/2=0%'+chr(96)) not in txt
record={'doc_id':'0102','official_requirement_id':'I18-E09','docx_sha256':sha256(doc.read_bytes()).hexdigest(),'pdf_sha256':sha256(pdf.read_bytes()).hexdigest(),'zip_crc':'PASS','word_xml_parts_parsed':len(xmlparts),'body_text_unchanged_from_R04':True,'body_text_chars':len(txt),'body_run_count':len(body_sizes),'body_min_half_points':min(body_sizes),'body_min_pt':min(body_sizes)/2,'body_min_complex_script_half_points':min(body_cs),'table_run_count':len(table_sizes),'table_min_half_points':min(table_sizes),'table_min_pt':min(table_sizes)/2,'table_min_complex_script_half_points':min(table_cs),'table_row_count':len(rows),'rows_with_cantSplit':unsplit,'targeted_page_breaks':breaks,'literal_markdown_delimiter_check':'PASS','status':'TECHNICAL_QA_PASS_PENDING_FULL_VISUAL_AND_INDEPENDENT_SEMANTIC_REVIEW'}
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
