from pathlib import Path
p=Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01\evidence\build_0063_R01.py")
s=p.read_text(encoding="utf-8")
repls=[
('BLUE="17365D"; ACCENT="1F4E78"; LIGHT="F4F7FA"; GRID="B7C9D6"; TEXT="23313D"; WHITE="FFFFFF"',
 'BLUE="17365D"; INK="000000"; ACCENT="1F4E78"; LIGHT="F4F7FA"; GRID="B7C9D6"; TEXT="23313D"; WHITE="FFFFFF"'),
('    if OUT.exists(): raise FileExistsError("Refusing to overwrite an existing candidate")',
'''    previous_sha=sha(OUT) if OUT.exists() else None
    if OUT.exists():
        if not RECEIPT.exists(): raise FileExistsError("Existing candidate has no matching build receipt")
        old_receipt=json.loads(RECEIPT.read_text(encoding="utf-8"))
        if old_receipt.get("candidate_sha256")!=previous_sha: raise FileExistsError("Existing candidate SHA does not match its build receipt")
        hist=ROOT/"evidence/history/build_receipt_R01_pre_style.json"
        hist.parent.mkdir(parents=True,exist_ok=True)
        if not hist.exists(): hist.write_text(json.dumps(old_receipt,ensure_ascii=False,indent=2),encoding="utf-8")'''),
('("Title",21,BLUE),("Heading 1",14,BLUE),("Heading 2",12,ACCENT),("Heading 3",10.8,ACCENT)',
 '("Title",21,INK),("Heading 1",14,INK),("Heading 2",12,INK),("Heading 3",10.8,INK)'),
('add_rich(hp,"TTQS ONE｜候選示範文件｜SAMPLE／SYNTHETIC",8.5,"667788")',
 'add_rich(hp,"TTQS ONE｜候選示範文件｜SAMPLE／SYNTHETIC",8.5,INK)'),
('add_rich(fp,"文件 0063｜候選版本，非協會核定制度｜",8.5,"667788")',
 'add_rich(fp,"文件 0063｜候選版本，非協會核定制度｜",8.5,INK)'),
('add_rich(p,title,21,BLUE,True)','add_rich(p,title,21,INK,True)'),
('BLUE if level==1 else ACCENT','INK'),
('"status":"BUILT_CANDIDATE_PENDING_RENDER_AND_INDEPENDENT_REVIEW"',
 '"prior_candidate_sha256":previous_sha,"iteration_reason":"Title, headings and page headers set to black per document skill; content unchanged","status":"BUILT_CANDIDATE_PENDING_RENDER_AND_INDEPENDENT_REVIEW"')
]
for old,new in repls:
    n=s.count(old)
    if n!=1: raise SystemExit(f"Expected one occurrence, got {n}: {old[:50]}")
    s=s.replace(old,new)
p.write_text(s,encoding="utf-8")
print("BUILDER_STYLE_PATCH=APPLIED")
