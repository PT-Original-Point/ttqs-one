from pathlib import Path
import hashlib
root=Path(r"E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0086_R01")
bodyp=root/"candidate/0086_R01_body.md"
lines=bodyp.read_text(encoding="utf-8").splitlines()
bullet="- 本文神秘客方法以機構書面授權、法遵確認與核准延後揭露為前提；如要求個別事前告知／同意或不明，即不適用。"
assert lines.count(bullet)==1, "expected exactly one repeated appendix line"
lines.remove(bullet)
idx=next((i for i,line in enumerate(lines) if line.startswith("## 附錄 B｜表單索引")),None)
assert idx is not None, "missing appendix B index"
assert not any(line.startswith("## ") for line in lines[idx+1:]), "appendix B unexpectedly not final"
text="\n".join(lines[:idx]).rstrip()+"\n"
bodyp.write_text(text,encoding="utf-8")
sp=root/"worker/build_0086_R01_docx.py"
s=sp.read_text(encoding="utf-8")
needle="        for ri, row in enumerate(table.rows):\n            for cell in row.cells:\n"
replacement="        for ri, row in enumerate(table.rows):\n            tr_pr = row._tr.get_or_add_trPr()\n            cant_split = OxmlElement(\"w:cantSplit\")\n            cant_split.set(qn(\"w:val\"), \"1\")\n            tr_pr.append(cant_split)\n            for cell in row.cells:\n"
assert s.count(needle)==1, "expected unique table row style loop"
s=s.replace(needle,replacement)
needle2='    receipt = {\n        "project_id": "TTQS_ONE", "document_id": "0086",'
replacement2='    receipt = {\n        "builder_sha256": sha(Path(__file__)),\n        "project_id": "TTQS_ONE", "document_id": "0086",'
assert s.count(needle2)==1, "expected unique receipt start"
s=s.replace(needle2,replacement2)
sp.write_text(s,encoding="utf-8")
pre_sha="4215ae00acb4de912670e0adcec31b0cf3de57d0c3fdeee66ef64943e6f3f462"
hist_sha=hashlib.sha256((root/"evidence/history/0086_R01_pre-layout_4215ae00.docx").read_bytes()).hexdigest()
assert hist_sha==pre_sha
pdfpre=root/"evidence/render_R01/0086_R01.pdf"
pdfsha=hashlib.sha256(pdfpre.read_bytes()).hexdigest()
with (root/"evidence/content_correction_R01.md").open("a",encoding="utf-8") as f:
    f.write("\n## 視覺檢查後的精確版面修復\n\n")
    f.write(f"- 保留前版 Word SHA-256 `{pre_sha}`；其 Word 原生 PDF 為 21 頁，SHA-256 `{pdfsha}`。\n")
    f.write("- 逐頁發現第 11–12 頁的 SYN-FND-03 列，以及第 17–18 頁的表 G 簽章列跨頁拆裂；其餘頁面完成目視檢查。\n")
    f.write("- 只在建置器加入 Word `cantSplit` 以保持每列完整；移除已由 §4／§10 完整涵蓋的重複附錄神秘客限制句及重複 A–H 索引，避免孤立第 21 頁；不改變表單或示範決策。\n")
    f.write("- 前版候選及建置收據已保存在 `evidence/history/`；重新建置後仍為候選，需重做最終 SHA 的技術、版面及獨立語意驗收。\n")
print("BODY_SHA256="+hashlib.sha256(bodyp.read_bytes()).hexdigest())
print("BUILDER_SHA256="+hashlib.sha256(sp.read_bytes()).hexdigest())
print("PRE_LAYOUT_DOCX_SHA256="+hist_sha)
print("PRE_LAYOUT_PDF_SHA256="+pdfsha)