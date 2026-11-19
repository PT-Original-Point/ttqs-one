from pathlib import Path
import hashlib, json, zipfile, xml.etree.ElementTree as ET
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0034_I07-E02_SOURCE_PREP_R01_20261118')
docx=base/'candidate'/'0034_I07-E02_R02_RAWLS_SCOPED_REPAIR.docx'
src=base/'SOURCE_PACKET_0034_I07-E02_R01.md'
bp=base/'UNIQUE_BLUEPRINT_0034_I07-E02_R01.md'
out=base/'candidate'/'qa'/'semantic_review_r02_opencode'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest().upper()
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with zipfile.ZipFile(docx) as z:
    root=ET.fromstring(z.read('word/document.xml'))
body=root.find('w:body',ns)
parts=[]
for child in list(body):
    tag=child.tag.split('}')[-1]
    if tag=='p':
        text=''.join(t.text or '' for t in child.findall('.//w:t',ns)).strip()
        if text: parts.append(text)
    elif tag=='tbl':
        rows=[]
        for row in child.findall('w:tr',ns):
            cells=[]
            for cell in row.findall('w:tc',ns):
                cells.append(' / '.join(''.join(t.text or '' for t in p.findall('.//w:t',ns)).strip() for p in cell.findall('w:p',ns)))
            rows.append(' | '.join(cells))
        parts.append('\n'.join('TABLE_ROW: '+r for r in rows))
body_text='\n\n'.join(parts)
packet=(
'# TTQS ONE independent semantic review packet\n'
'work_id=TTQS_ONE_0034_I07-E02_SEMANTIC_REVIEW_R02\n'
'doc_id=0034 requirement=I07-E02 revision=R02 status=CANDIDATE\n'
'frozen_candidate_sha256='+sha(docx)+'\n'
'source_packet_sha256='+sha(src)+'\n'
'unique_blueprint_sha256='+sha(bp)+'\n\n'
'## REVIEW INSTRUCTIONS\nReview the supplied candidate body against the exact source packet and unique blueprint. Check requirement coverage, I07-E02-specific usability, internal arithmetic/cohort consistency, synthetic facts/register and sample-real boundaries, evidence claims, operational steps, missing/contradictory content, and concrete defects. Do not edit files or use tools. Return findings with precise section/table locators, severity, evidence, and a decision PASS or FAIL for semantic usability only; if the supplied evidence is insufficient, state UNKNOWN and why. Do not claim visual, technical, official acceptance, or GitHub acceptance. Bind every finding to the frozen candidate SHA above.\n\n'
'## OFFICIAL SOURCE PACKET\n'+src.read_text(encoding='utf-8')+'\n\n'
'## UNIQUE BLUEPRINT\n'+bp.read_text(encoding='utf-8')+'\n\n'
'## EXTRACTED CANDIDATE BODY (OOXML order; tables retained row-by-row)\n'+body_text+'\n'
)
p=out/'review_packet.txt'; p.write_text(packet,encoding='utf-8',newline='\n')
manifest={'work_id':'TTQS_ONE_0034_I07-E02_SEMANTIC_REVIEW_R02','docx_path':str(docx),'candidate_sha256':sha(docx),'source_packet_path':str(src),'source_packet_sha256':sha(src),'blueprint_path':str(bp),'blueprint_sha256':sha(bp),'extract_script_path':str(Path(__file__)),'extract_script_sha256':sha(Path(__file__)),'packet_path':str(p),'packet_sha256':sha(p),'packet_bytes':p.stat().st_size,'candidate_text_chars':len(body_text),'paragraph_table_blocks':len(parts),'review_scope':'semantic/usability only; visual/technical/acceptance not claimed'}
(out/'PACKET_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(manifest,ensure_ascii=False))
