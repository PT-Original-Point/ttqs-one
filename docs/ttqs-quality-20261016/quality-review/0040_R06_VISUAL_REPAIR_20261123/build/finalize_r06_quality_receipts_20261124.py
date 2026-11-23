from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from hashlib import sha256
from datetime import datetime, timezone, timedelta
import csv, json, re

root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0040_R06_VISUAL_REPAIR_20261123')
qa=root/'qa'
doc=root/'candidate'/'0040__訓練評估方法與成效指標對照表_R06.docx'
r05=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0040_R05_SCOPED_REPAIR_20261123\candidate\0040__訓練評估方法與成效指標對照表_R05.docx')
tech0=json.loads((qa/'R06_TECHNICAL_QA.json').read_text(encoding='utf-8'))
visual0=json.loads((qa/'R06_VISUAL_QA.json').read_text(encoding='utf-8'))
semantic=json.loads((qa/'W2_SEMANTIC_REVIEW_R06.json').read_text(encoding='utf-8'))
terminal=json.loads((qa/'W2_TERMINAL_RECEIPT_R06.json').read_text(encoding='utf-8'))
layout=json.loads((qa/'R06_SCOPED_LAYOUT_REPAIR_RECEIPT.json').read_text(encoding='utf-8'))
prior=json.loads((root/'evidence'/'R05_DETERMINISTIC_QA_R01.json').read_text(encoding='utf-8'))
reg=root/'sources'/'0040_SOURCES_AND_SYNTHETIC_REPLACEMENT_REGISTER_R05.csv'
packet=root/'evidence'/'R06_W2_REVIEW_PACKET.txt'
pdf=qa/'render_R06'/'0040_R06_word_export.pdf'
pages=qa/'render_R06'/'pages'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
csha=sha(doc)
assert csha==tech0['candidate_sha256']==visual0['candidate_sha256']==semantic['candidate_sha256']==terminal['candidate_sha256'].lower()
assert all(tech0['checks'].values()) and visual0['full_document_visual_status']=='PASS'
assert visual0['rendered_page_count']==8 and semantic['verdict']=='PASS' and semantic['blocking_findings']==[]
assert terminal['worker']=='W2 Antigravity CLI' and terminal['cli_exit_code']==0 and terminal['cli_status']=='SUCCESS'
assert terminal['served_model']=='UNKNOWN' and terminal['candidate_sha256'].lower()==csha
assert prior['qa']['sample_truth_boundary']=='PASS' and prior['qa']['existing_arithmetic_invariants']=='PASS'
assert sha(reg)==semantic['scope_reviewed'].split('replacement register ')[1].split(' ')[0]
assert len(list(csv.reader(reg.open(encoding='utf-8-sig'))))-1==39
assert sha(pdf)==tech0['rendered_pdf_sha256']==visual0['rendered_pdf_sha256']

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; ns={'w':W}; q=lambda n:'{'+W+'}'+n
with ZipFile(doc) as z:
    assert z.testzip() is None
    tree=ET.fromstring(z.read('word/document.xml'))
    style_root=ET.fromstring(z.read('word/styles.xml'))
    text_nodes=[e.text or '' for e in tree.findall('.//w:t',ns)]
    raw_text=''.join(text_nodes)
    parents={child:parent for parent in tree.iter() for child in parent}
    styles={s.get(q('styleId')):s for s in style_root.findall('.//w:style',ns)}
    def run_size(rpr):
        if rpr is None:return None
        e=rpr.find('w:sz',ns)
        return int(e.get(q('val')))/2 if e is not None else None
    def style_size(sid):
        seen=set()
        while sid and sid not in seen:
            seen.add(sid); s=styles.get(sid)
            if s is None:break
            v=run_size(s.find('w:rPr',ns))
            if v is not None:return v
            b=s.find('w:basedOn',ns); sid=b.get(q('val')) if b is not None else None
        return None
    default_size=run_size(style_root.find('w:docDefaults/w:rPrDefault/w:rPr',ns))
    body_sizes=[]; table_sizes=[]; unresolved=[]
    for para in tree.findall('.//w:p',ns):
        pstyle=para.find('w:pPr/w:pStyle',ns); psid=pstyle.get(q('val')) if pstyle is not None else None
        ancestor=parents.get(para); in_table=False
        while ancestor is not None:
            if ancestor.tag==q('tc'): in_table=True; break
            ancestor=parents.get(ancestor)
        for run in para.findall('.//w:r',ns):
            text=''.join(t.text or '' for t in run.findall('.//w:t',ns)).strip()
            if not text:continue
            rpr=run.find('w:rPr',ns); size=run_size(rpr)
            if size is None:
                char=rpr.find('w:rStyle',ns) if rpr is not None else None
                size=style_size(char.get(q('val')) if char is not None else None)
            if size is None:size=style_size(psid)
            if size is None:size=default_size
            if size is None:unresolved.append(text[:40])
            elif in_table:table_sizes.append(size)
            else:body_sizes.append(size)

font_receipt={
 'work_id':'TTQS_ONE_0040_I08-E03_R06_FONT_FLOOR_QA_20261124',
 'doc_id':'0040','requirement_id':'I08-E03','candidate_sha256':csha,
 'method':'OOXML run size, character style inheritance, paragraph style inheritance, and document default size; body and table text runs classified by w:tc ancestry.',
 'body_text_runs':len(body_sizes),'table_text_runs':len(table_sizes),'unresolved_text_runs':len(unresolved),
 'body_min_effective_font_pt':min(body_sizes),'table_min_effective_font_pt':min(table_sizes),
 'body_floor_pt':10.5,'table_floor_pt':9.5,
 'body_floor_pass':min(body_sizes)>=10.5,'table_floor_pass':min(table_sizes)>=9.5,
 'raw_latex_markers':{m:raw_text.count(m) for m in ('\\frac','\\sqrt','\\begin{','\\displaystyle')},
 'raw_latex_markers_absent':not any(m in raw_text for m in ('\\frac','\\sqrt','\\begin{','\\displaystyle')),
 'zip_integrity_pass':True,'source_register_sha256':sha(reg),
 'source_register_data_rows':len(list(csv.reader(reg.open(encoding='utf-8-sig'))))-1,
 'prior_exact_text_unchanged_to_R05':tech0['checks']['text_content_identical_to_R05'],
 'formal_acceptance':'NOT_GRANTED','real_evidence':'NOT_ESTABLISHED',
 'observed_at_tpe':datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')}
assert font_receipt['unresolved_text_runs']==0 and font_receipt['body_floor_pass'] and font_receipt['table_floor_pass'] and font_receipt['raw_latex_markers_absent']

font_path=qa/'R06_FONT_FLOOR_QA.json'
font_path.write_text(json.dumps(font_receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

check_rows=[{'check':k,'status':'PASS','source_receipt_sha256':sha(qa/'R06_TECHNICAL_QA.json')} for k in tech0['checks']]
check_rows += [
 {'check':'body_font_floor_10_5pt','status':'PASS','evidence_receipt':'qa/R06_FONT_FLOOR_QA.json'},
 {'check':'table_font_floor_9_5pt','status':'PASS','evidence_receipt':'qa/R06_FONT_FLOOR_QA.json'},
 {'check':'no_unresolved_text_run_font_sizes','status':'PASS','evidence_receipt':'qa/R06_FONT_FLOOR_QA.json'},
 {'check':'no_unconverted_latex_markers','status':'PASS','evidence_receipt':'qa/R06_FONT_FLOOR_QA.json'},
 {'check':'replacement_register_39_rows_and_sha','status':'PASS','source_register_sha256':sha(reg)},
 {'check':'inherited_R05_sample_truth_and_arithmetic','status':'PASS','source_receipt_sha256':sha(root/'evidence'/'R05_DETERMINISTIC_QA_R01.json'),'text_identical_to_R05':True},
]
blueprint_match=re.search(r'Unique Blueprint scope ([0-9a-f]{64})',semantic['scope_reviewed'],re.I)
assert blueprint_match
tech_norm={
 'work_id':'TTQS_ONE_0040_I08-E03_R06_TECHNICAL_QA_NORMALIZED_20261124',
 'doc_id':'0040','requirement_id':'I08-E03','official_sequence':'040',
 'candidate_sha256':csha,'technical_result':'PASS','technical_visual_status':'PASS_TECHNICAL_VISUAL',
 'check_count':len(check_rows),'checks':check_rows,
 'source_packet_sha256':sha(packet),'source_packet_path':'evidence/R06_W2_REVIEW_PACKET.txt',
 'source_register_sha256':sha(reg),'unique_blueprint_sha256':blueprint_match.group(1).lower(),
 'native_pdf_sha256':sha(pdf),'native_pdf_pages':8,
 'source_receipt_sha256':sha(qa/'R06_TECHNICAL_QA.json'),
 'font_receipt_sha256':sha(font_path),'formal_acceptance':'NOT_GRANTED','real_evidence':'NOT_ESTABLISHED'}
(qa/'TECHNICAL_QA_R06_NORMALIZED_20261124.json').write_text(json.dumps(tech_norm,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

page8=pages/'page-08.png'
visual_norm={
 'work_id':'TTQS_ONE_0040_I08-E03_R06_VISUAL_QA_NORMALIZED_20261124',
 'doc_id':'0040','requirement_id':'I08-E03','candidate_sha256':csha,
 'visual_result':'PASS','total_pages':8,'manual_pages':[8],
 'unchanged_page_inheritance':{'pages':[1,2,3,4,5,6,7],'pixel_identical':True,'prior_render_receipt_sha256':sha(qa/'R06_VISUAL_QA.json')},
 'page_png_sha256':{'page_8':sha(page8)},'word_native_pdf_sha256':sha(pdf),
 'source_visual_receipt_sha256':sha(qa/'R06_VISUAL_QA.json'),
 'scope':'Pages 1-7 inherited solely by pixel-identical PNG SHA; page 8 rendered and visually inspected in current R06 run.',
 'formal_acceptance':'NOT_GRANTED'}
(qa/'MANUAL_VISUAL_INSPECTION_R06_NORMALIZED_20261124.json').write_text(json.dumps(visual_norm,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

public_review={
 'work_id':terminal['work_id'],'worker':'W2 Antigravity CLI','reviewer_role':'Independent semantic reviewer',
 'candidate_sha256':csha,'reviewed_docx_sha256':csha,'candidate_sha256_before':csha,'candidate_sha256_after':csha,
 'candidate_mutated':False,'exit_code':terminal['cli_exit_code'],'terminal_status':'SUCCESS','verdict':'PASS',
 'requested_model':terminal['requested_model'],'served_model':'UNKNOWN',
 'terminal_receipt_sha256':sha(qa/'W2_TERMINAL_RECEIPT_R06.json'),
 'semantic_review_receipt_sha256':sha(qa/'W2_SEMANTIC_REVIEW_R06.json'),
 'raw_stdout_sha256':sha(qa/'..'/'worker'/'W2_STDOUT_R06.raw'),
 'provider_served_model':'UNKNOWN','reviewed_at_tpe':terminal['observed_at_local']}
(qa/'PUBLIC_REVIEW_RECEIPT.json').write_text(json.dumps(public_review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

print(json.dumps({'candidate_sha256':csha,'docx_bytes':doc.stat().st_size,'font_body_min_pt':min(body_sizes),'font_table_min_pt':min(table_sizes),'body_runs':len(body_sizes),'table_runs':len(table_sizes),'unresolved_fonts':len(unresolved),'register_rows':font_receipt['source_register_data_rows'],'latex_markers':font_receipt['raw_latex_markers'],'new_receipts':[p.name for p in (font_path,qa/'TECHNICAL_QA_R06_NORMALIZED_20261124.json',qa/'MANUAL_VISUAL_INSPECTION_R06_NORMALIZED_20261124.json',qa/'PUBLIC_REVIEW_RECEIPT.json')],'served_model':'UNKNOWN'},ensure_ascii=False))