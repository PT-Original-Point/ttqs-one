from pathlib import Path
import hashlib
root=Path(r"E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0086_R01")
sp=root/"worker/build_0086_R01_docx.py"
s=sp.read_text(encoding="utf-8")
needle='''        if is_heading:
            p.paragraph_format.keep_with_next = True
            for run in p.runs:
'''
replacement='''        if is_heading:
            p.paragraph_format.keep_with_next = True
            if p.style.name == "Heading 1" and p.text.startswith("14. 文件維護與交付檢核"):
                p.paragraph_format.page_break_before = True
            for run in p.runs:
'''
assert s.count(needle)==1
sp.write_text(s.replace(needle,replacement),encoding="utf-8")
prev="620286db05c92cf7d082a5d3806e861cce4afa31356eb84ac8d3f29a9a8c3982"
h=hashlib.sha256((root/"evidence/history/0086_R01_pre_finalpage_620286db.docx").read_bytes()).hexdigest()
assert h==prev
with (root/"evidence/content_correction_R01.md").open("a",encoding="utf-8") as f:
    f.write("\n## 最終版面收斂\n\n")
    f.write(f"- 前版 SHA-256 `{prev}`；Windows Word PDF 第 21 頁仍有第 14 節清單末兩列。\n")
    f.write("- 為避免自檢表拆頁，只將第 14 節移到新頁；保持全文各表格列不跨頁。重渲染後須再次檢查所有頁面與 exact SHA。\n")
print("PREVIOUS_CANDIDATE_SHA256="+h)
print("BUILDER_SHA256="+hashlib.sha256(sp.read_bytes()).hexdigest())