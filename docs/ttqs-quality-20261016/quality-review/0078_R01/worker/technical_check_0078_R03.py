from pathlib import Path
import csv, hashlib, json, re, zipfile, xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
docx=root/'candidate'/'0078_R03.docx'
body=root/'candidate'/'0078_R03_body.md'
activity=root/'inputs'/'SYNTHETIC_ACTIVITY_INDEX_0078_R01.csv'
register=root/'inputs'/'SYNTHETIC_REPLACEMENT_REGISTER_0078_R01.csv'
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ptext(node): return ''.join(t.text or '' for t in node.findall('.//w:t',ns))
with zipfile.ZipFile(docx) as z:
    bad=z.testzip()
    xml=ET.fromstring(z.read('word/document.xml'))
    rel=ET.fromstring(z.read('word/_rels/document.xml.rels'))
    media=[n for n in z.namelist() if n.startswith('word/media/')]
    external=[e.attrib.get('Target','') for e in rel if e.attrib.get('TargetMode')=='External']
    body_el=xml.find('w:body',ns)
    out=[]; tables=0; tr_count=0
    for el in list(body_el):
        if el.tag.endswith('}p'):
            s=ptext(el)
            if s: out.append(s)
        elif el.tag.endswith('}tbl'):
            tables+=1; out.append('')
            for tr in el.findall('./w:tr',ns):
                tr_count+=1
                cells=[]
                for tc in tr.findall('./w:tc',ns):
                    cells.append(ptext(tc).replace('|','\\|').replace('\n',' '))
                out.append('| '+' | '.join(cells)+' |')
            out.append('')
text='\n'.join(out)
(root/'evidence'/'docx_extracted_R03.md').write_text(text,encoding='utf-8')
with activity.open(encoding='utf-8-sig',newline='') as f: acts=list(csv.DictReader(f))
with register.open(encoding='utf-8-sig',newline='') as f: regs=list(csv.DictReader(f))
ids=[r.get('synthetic_id','') for r in regs]
expected={f'SYN-078-A{i:02d}' for i in range(1,9)}
activity_ids={r.get('activity_id','') for r in acts}
checks={
 'zip_integrity_pass': bad is None,
 'document_xml_present': True,
 'activity_csv_eight_unique_rows': len(acts)==8 and len(activity_ids)==8,
 'register_csv_64_unique_ids': len(regs)==64 and len(set(ids))==64,
 'register_activity_coverage': {r.get('sample_activity_id','') for r in regs}==expected,
 'register_required_fields_complete': all(all(r.get(k,'').strip() for k in ['synthetic_id','sample_activity_id','field','sample_value','genuine_source_required','verification_rule','hold_or_reject_if','boundary']) for r in regs),
 'docx_mentions_all_eight_activity_ids': all(x in text for x in expected),
 'docx_candidate_only_status': 'CANDIDATE_ONLY' in text and 'NOT_GRANTED' in text,
 'docx_real_hold_status': 'REAL=UNKNOWN/HOLD' in text,
 'docx_checkbox_084_partial_hold': '084' in text and 'PARTIAL/HOLD' in text,
 'all_eight_photo_ids_mentioned': all(f'SYN-078-PH-{i:02d}' in text for i in range(1,9)),
 'no_image_boundary_present': 'NO IMAGE ATTACHED' in text and 'NOT_CAPTURED' in text,
 'revision_r03_present': 'R03' in text,
 'current_revision_marker_r03': '候選修訂：R03' in text,
 'old_candidate_revision_markers_absent': '候選修訂：R01' not in text and '候選修訂：R02' not in text,
 'crosswalk_prohibition_explicit': '不建立任何身分對照' in text and '不映射 P01–P16 或 S01–S16' in text,
 'no_embedded_media': len(media)==0,
}
receipt={
 'schema':'TTQS_ONE_0078_R03_TECHNICAL_REVIEW.v1','document_id':'0078','requirement_id':'I17B-E01','official_checkbox_serial':'084',
 'candidate_docx_sha256':sha(docx),'candidate_docx_bytes':docx.stat().st_size,'body_sha256':sha(body),
 'extracted_text_sha256':sha(root/'evidence'/'docx_extracted_R03.md'),
 'activity_csv_sha256':sha(activity),'activity_rows':len(acts),'register_csv_sha256':sha(register),'register_rows':len(regs),
 'docx_zip_test_error':bad,'document_tables':tables,'table_rows':tr_count,'embedded_media_count':len(media),
 'external_relationship_targets':external,'checks':checks,'result':'PASS' if all(checks.values()) else 'FAIL',
 'scope':'Package integrity, content presence, synthetic ID/CSV counts, status-boundary strings, no embedded media; visual review is in visual_review_R03.json; semantic acceptance is separate and pending.'}
(root/'evidence'/'technical_review_R03.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
