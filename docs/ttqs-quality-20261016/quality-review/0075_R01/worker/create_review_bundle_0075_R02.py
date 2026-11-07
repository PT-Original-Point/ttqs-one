from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from pypdf import PdfReader
import subprocess,hashlib
root=Path(r'E:\TTQS\_github_sync_0064')
base=root/'docs/ttqs-quality-20261016/quality-review/0075_R01'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
docx=base/'candidate/0075_R02.docx'
doc=Document(str(docx))
parts=[]
for child in doc.element.body.iterchildren():
    tag=child.tag.rsplit('}',1)[-1]
    if tag=='p':
        p=Paragraph(child,doc); t=p.text.strip()
        if not t: continue
        st=p.style.name if p.style else 'Normal'
        if st=='Title': parts.append('# '+t)
        elif st.startswith('Heading '):
            try: level=min(6,int(st.split()[-1])+1)
            except Exception: level=3
            parts.append('#'*level+' '+t)
        else: parts.append(t)
    elif tag=='tbl':
        t=Table(child,doc)
        rows=[[c.text.replace('\n',' / ').replace('|','\\|').strip() for c in r.cells] for r in t.rows]
        if rows:
            parts.append('| '+' | '.join(rows[0])+' |')
            parts.append('| '+' | '.join(['---']*len(rows[0]))+' |')
            for row in rows[1:]: parts.append('| '+' | '.join(row)+' |')
extracted='\n\n'.join(parts)+'\n'
(base/'evidence/docx_extracted_R02.md').write_text(extracted,encoding='utf-8')
source_packet=(base/'inputs/SOURCE_PACKET_0075_R01.md').read_text(encoding='utf-8')
blueprint=(base/'inputs/UNIQUE_BLUEPRINT_0075_R01.md').read_text(encoding='utf-8')
manual=subprocess.run(['git','show','HEAD:docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md'],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True).stdout
lines=manual.splitlines(); start=next(i for i,x in enumerate(lines) if '指標 17a' in x); end=next((i for i in range(start+1,len(lines)) if '指標 17b' in lines[i]),min(start+60,len(lines)))
manual17='\n'.join(lines[start:end])
blueprint_src=subprocess.run(['git','show','HEAD:docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md'],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True).stdout
blines=blueprint_src.splitlines(); bstart=next(i for i,x in enumerate(blines) if '082｜' in x); excerpt='\n'.join(blines[max(0,bstart-4):bstart+4])
pdf=root/'docs/ttqs-quality-20261016/quality-review/0070_R01/inputs/official_checklist_source.pdf'
reader=PdfReader(str(pdf)); req='\n'.join([f'--- PAGE {i+1} ---\n'+reader.pages[i].extract_text() for i in [4,5]])
register=(base/'inputs/SYNTHETIC_REPLACEMENT_REGISTER_0075_R01.csv').read_text(encoding='utf-8-sig')
commit=subprocess.run(['git','rev-parse','HEAD'],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True).stdout.strip()
blob_manual=subprocess.run(['git','rev-parse','HEAD:docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md'],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True).stdout.strip()
blob_blueprint=subprocess.run(['git','rev-parse','HEAD:docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md'],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True).stdout.strip()
sha_docx=sha(docx)
sections=[
('Review identity',f'Independent semantic review of DOCX 0075 / I17A-E03 / official checkbox 082. Candidate exact SHA-256: {sha_docx}. Current branch source head for the cited official text: {commit}. This is a review of a candidate only; no formal acceptance is requested or implied.'),
('Official checklist source',f'Full PDF SHA-256: {sha(pdf)}. Text extracted from official PDF pages 5 and 6 follows.\n\n{req}'),
('Official indicator writing manual',f'Git blob SHA: {blob_manual}.\n\n{manual17}'),
('Official checkbox guidance',f'Git blob SHA: {blob_blueprint}.\n\n{excerpt}'),
('Source packet',source_packet),
('Unique Blueprint',blueprint),
('Exact DOCX text extraction from the candidate SHA above',extracted),
('Replacement register companion',register),
]
bundle='\n\n---\n\n'.join('# '+title+'\n\n'+content for title,content in sections)+'\n'
out=base/'review/semantic_review_bundle_R02.md'; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(bundle,encoding='utf-8')
print(f'candidate_sha256={sha_docx}\nextracted_sha256={sha(base/"evidence/docx_extracted_R02.md")}\nbundle={out}\nbundle_bytes={out.stat().st_size}\nmanual_blob={blob_manual}\nblueprint_blob={blob_blueprint}\nofficial_pdf_sha256={sha(pdf)}')
