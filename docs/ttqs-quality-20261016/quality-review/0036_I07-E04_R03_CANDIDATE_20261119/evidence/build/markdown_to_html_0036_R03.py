from pathlib import Path
import html,re,json,hashlib
w=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\EXTERNAL_WORK\TTQS_ONE_0036_I07-E04_VISUAL_REPAIR_R03_20261118")
src=w/"CANDIDATE_BODY_0036_R03.md"
body=src.read_text(encoding="utf-8")
def inline(s):
    bt=chr(96)
    s=html.escape(s,quote=False)
    s=re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",r'<a href="\2">\1</a>',s)
    s=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",s)
    s=re.sub(r"\*(.+?)\*",r"<em>\1</em>",s)
    s=re.sub(bt+r"([^"+bt+r"]+)"+bt,r"<code>\1</code>",s)
    return s
lines=body.splitlines()
out=[]
i=0
bt=chr(96)
while i<len(lines):
    line=lines[i]
    if not line.strip():
        i+=1
        continue
    if re.match(r"^#{1,6}\s",line):
        m=re.match(r"^(#{1,6})\s+(.*)$",line)
        level=min(len(m.group(1)),4)
        out.append("<h%d>%s</h%d>"%(level,inline(m.group(2)),level))
        i+=1
        continue
    if re.fullmatch(r"\s*---+\s*",line):
        out.append("<hr/>")
        i+=1
        continue
    if line.lstrip().startswith("|"):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith("|"):
            cells=[x.strip() for x in lines[i].strip().strip("|").split("|")]
            if not all(c and set(c)<=set(":- ") for c in cells):
                rows.append(cells)
            i+=1
        if rows:
            head=rows[0]
            out.append("<table><thead><tr>"+''.join("<th>"+inline(x)+"</th>" for x in head)+"</tr></thead><tbody>")
            for row in rows[1:]:
                if len(row)!=len(head):
                    row=(row+[""]*len(head))[:len(head)]
                out.append("<tr>"+''.join("<td>"+inline(x)+"</td>" for x in row)+"</tr>")
            out.append("</tbody></table>")
        continue
    if line.startswith(bt*3):
        lang=line[3:].strip()
        code=[]
        i+=1
        while i<len(lines) and not lines[i].startswith(bt*3):
            code.append(lines[i])
            i+=1
        if i<len(lines):
            i+=1
        out.append("<pre>"+html.escape("\n".join(code))+"</pre>")
        continue
    m=re.match(r"^\s*[-*]\s+(.*)$",line)
    if m:
        items=[]
        while i<len(lines):
            m2=re.match(r"^\s*[-*]\s+(.*)$",lines[i])
            if not m2:
                break
            items.append(m2.group(1))
            i+=1
        out.append("<ul>"+''.join("<li>"+inline(x)+"</li>" for x in items)+"</ul>")
        continue
    m=re.match(r"^\s*\d+[.)]\s+(.*)$",line)
    if m:
        items=[]
        while i<len(lines):
            m2=re.match(r"^\s*\d+[.)]\s+(.*)$",lines[i])
            if not m2:
                break
            items.append(m2.group(1))
            i+=1
        out.append("<ol>"+''.join("<li>"+inline(x)+"</li>" for x in items)+"</ol>")
        continue
    para=[line.strip()]
    i+=1
    while i<len(lines) and lines[i].strip() and not re.match(r"^(#{1,6}\s|\||"+bt*3+r")",lines[i]) and not re.fullmatch(r"\s*---+\s*",lines[i]) and not re.match(r"^\s*(?:[-*]\s+|\d+[.)]\s+)",lines[i]):
        para.append(lines[i].strip())
        i+=1
    out.append("<p>"+inline(" ".join(para))+"</p>")
css="""@page { size: 595.3pt 841.9pt; margin: 49pt 42pt 49pt 42pt; }
body { font-family: Arial, "Microsoft JhengHei", sans-serif; font-size: 10.5pt; color:#202a36; line-height:1.2; }
h1 { font-family:"Microsoft JhengHei",sans-serif; font-size:19pt; color:#152b45; font-weight:bold; margin:0 0 6pt 0; page-break-after:avoid; }
h2 { font-size:14pt; color:#183b5b; border-bottom:1px solid #b8c8d6; margin:14pt 0 5pt; page-break-after:avoid; }
h3 { font-size:11.5pt; color:#224d70; margin:10pt 0 4pt; page-break-after:avoid; }
h4 { font-size:10.5pt; color:#294e68; margin:8pt 0 3pt; page-break-after:avoid; }
p { margin:0 0 5pt 0; word-wrap:break-word; overflow-wrap:anywhere; }
ul,ol { margin:2pt 0 6pt 22pt; padding:0; }
li { margin:0 0 2pt 0; }
table { width:100%; border-collapse:collapse; table-layout:auto; margin:5pt 0 8pt; font-size:9.5pt; }
th,td { border:0.5pt solid #D9D9D9; padding:4pt 5pt; vertical-align:middle; word-wrap:break-word; }
th { background:#183b5b; color:#ffffff; font-weight:bold; }
tbody tr:nth-child(even) td { background:#edf3f8; }
pre { white-space:pre-wrap; font-family:Consolas,"Courier New",monospace; font-size:8.5pt; background:#f1f4f7; padding:6pt; border:0.5pt solid #d9d9d9; }
code { font-family:Consolas,"Courier New",monospace; font-size:9.5pt; }
hr { border:0; border-top:0.5pt solid #c8d2dc; margin:8pt 0; }
a { color:#135e96; text-decoration:underline; }
"""
doc='<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+''.join(out)+'</body></html>'
target=w/"CANDIDATE_HTML_0036_R03.html"
target.write_text(doc,encoding="utf-8")
receipt={"body_sha256":hashlib.sha256(src.read_bytes()).hexdigest().upper(),"html_sha256":hashlib.sha256(target.read_bytes()).hexdigest().upper(),"html_bytes":target.stat().st_size,"markdown_table_count":body.count("\n|"),"html_table_count":doc.count("<table>"),"heading_count":len(re.findall(r"<h[1-4]>",doc)),"paragraph_count":doc.count("<p>")}
(w/"HTML_CONVERSION_RECEIPT_R03.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False))