from pathlib import Path
from docx import Document
import csv,hashlib,json
from datetime import datetime,timezone
pkg=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R02')
docp=pkg/'candidate/0053_R02.docx'; regp=pkg/'SYNTHETIC_REPLACEMENT_REGISTER_0053_R02.csv'
old_sha='c50118aa0ff1e9085c56fcc8b08b19819b2cb18afe95b2044fc9c1117f16973d'
current=hashlib.sha256(docp.read_bytes()).hexdigest(); assert current==old_sha,current
d=Document(str(docp))
old='G1 90 分鐘的分段檢查：基線 31.5 分說明、18 分示範、31.5 分練習，三段相加 81 分；提案 18+18+45=81 分。兩者均尚有 9 分鐘須在正式教案交代轉場或回饋安排。此表重算百分比，不推定實際授課分鐘。'
new='G1 90 分鐘的分段檢查：基線 35+20+35=90 分鐘；方案 A 20+20+50=90 分鐘。引導練習增加 15 分鐘，占比由 35/90=38.9% 升至 50/90=55.6%（+16.7 個百分點），達本例 50% 合成門檻。分段取自 0052 R01 SAMPLE；REAL 核定及授課分鐘仍 UNKNOWN。'
found=[]
for i,p in enumerate(d.paragraphs,1):
    if p.text==old:
        nonempty=[r for r in p.runs if r.text]
        assert len(nonempty)==1
        nonempty[0].text=new; found.append(i)
assert len(found)==1,found
d.save(str(docp)); new_sha=hashlib.sha256(docp.read_bytes()).hexdigest()
with regp.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
assert len(rows)==38 and len({r['fact_id'] for r in rows})==38
for r in rows:r['candidate_sha256']=new_sha
with regp.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys(),lineterminator='\n');w.writeheader();w.writerows(rows)
receiptp=pkg/'evidence/build_receipt_R02.json'
r=json.loads(receiptp.read_text(encoding='utf-8'))
r['candidate_sha256']=new_sha;r['candidate_bytes']=docp.stat().st_size;r['register_sha256']=hashlib.sha256(regp.read_bytes()).hexdigest()
r['corrected_text_items']=12;r['corrected_locators'].append('p10 / section 08 / G1 segment computation paragraph')
r['final_correction_note']='A first R02 render showed the calculation paragraph on page 10 still had R01 wording; that paragraph was then corrected and the complete document was rerendered for final review.'
receiptp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
log=pkg/'evidence/correction_log_R02.md'; s=log.read_text(encoding='utf-8')
s=s.replace('New candidate SHA: `c50118aa0ff1e9085c56fcc8b08b19819b2cb18afe95b2044fc9c1117f16973d`',f'Final candidate SHA: `{new_sha}`')
s += '\n\n## Final-render correction\n\nThe first R02 Word render exposed one unchanged paragraph on physical page 10. The intermediate DOCX/PDF are preserved in `evidence/history/`. The paragraph is now aligned with the source: 35+20+35=90 minutes; 20+20+50=90 minutes; practice 35/90=38.9% to 50/90=55.6%. The final candidate SHA is recorded above.\n'
log.write_text(s,encoding='utf-8')
print(json.dumps({'intermediate_sha256':old_sha,'final_sha256':new_sha,'candidate_bytes':docp.stat().st_size,'register_sha256':r['register_sha256'],'patched_paragraph_index':found[0]},ensure_ascii=False,indent=2))
