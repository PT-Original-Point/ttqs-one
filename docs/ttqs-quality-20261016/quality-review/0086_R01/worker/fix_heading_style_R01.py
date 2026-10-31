from pathlib import Path
import hashlib
root=Path(r"E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0086_R01")
sp=root/"worker/build_0086_R01_docx.py"
s=sp.read_text(encoding="utf-8")
old='if p.style.name == "Heading 1" and p.text.startswith("14. 文件維護與交付檢核"):'
new='if p.style.name == "Heading 2" and p.text.startswith("14. 文件維護與交付檢核"):'
assert s.count(old)==1
sp.write_text(s.replace(old,new),encoding="utf-8")
prev="098382788bd111cf3406171b761f0096eee1ca18ce942d83fc17cc0ca76be14e"
assert hashlib.sha256((root/"evidence/history/0086_R01_pre_sectionbreak_09838278.docx").read_bytes()).hexdigest()==prev
with (root/"evidence/content_correction_R01.md").open("a",encoding="utf-8") as f:
 f.write("\n## 分頁條件樣式修正\n\n")
 f.write(f"- 前版 SHA-256 `{prev}`；Word 讀取 Markdown `##` 為 Heading 2，前版條件錯指定 Heading 1，故分頁規則未命中。\n")
 f.write("- 已改對應 Heading 2；預期第 14 節自檢表與附錄同頁完整呈現；將與前版頁面 PNG 逐頁比較，僅重新目視變更頁。\n")
print("BUILDER_SHA256="+hashlib.sha256(sp.read_bytes()).hexdigest())