import hashlib,json
from pathlib import Path
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03'); ev=root/'evidence'; rev=root/'review'/'opencode_v2_review_R03'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):
 with p.open('w',encoding='utf-8',newline='\n') as f:f.write(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
font=ev/'font_size_qa_receipt_R03.json'; reviewer=rev/'independent_review_receipt_R03.json'; report=rev/'independent_semantic_review_R03.md'; visual=ev/'visual_layout_receipt_R03.json'; tech=ev/'technical_integrity_receipt_R03.json'; build=ev/'build_receipt_R03.json'; status=root/'candidate_status_R03.md'; decision=ev/'candidate_quality_decision_R03.json'
t=load(tech); t['independent_review_receipt_sha256']=sha(reviewer); t['font_size_qa_receipt_sha256']=sha(font); t['visual_layout_receipt_sha256']=sha(visual); save(tech,t)
b=load(build); b['visual_layout_receipt_sha256']=sha(visual); b['font_size_qa_receipt_sha256']=sha(font); b['independent_review_receipt_sha256']=sha(reviewer); save(build,b)
d=load(decision); d['technical_receipt_sha256']=sha(tech); d['font_receipt_sha256']=sha(font); d['review_receipt_sha256']=sha(reviewer); d['review_report_sha256']=sha(report); d['visual_receipt_sha256']=sha(visual); d['candidate_status_sha256']=sha(status); save(decision,d)
print(json.dumps({'technical_receipt_sha256':sha(tech),'build_receipt_sha256':sha(build),'decision_sha256':sha(decision),'review_receipt_sha256':sha(reviewer),'visual_receipt_sha256':sha(visual),'font_receipt_sha256':sha(font),'status_sha256':sha(status)},indent=2))
