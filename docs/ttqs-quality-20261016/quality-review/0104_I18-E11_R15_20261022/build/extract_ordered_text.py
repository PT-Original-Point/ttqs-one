import sys, zipfile, xml.etree.ElementTree as ET
from pathlib import Path
src=Path(sys.argv[1]); dst=Path(sys.argv[2])
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with zipfile.ZipFile(src) as z:
    root=ET.fromstring(z.read('word/document.xml'))
body=root.find('w:body',ns)
def text_of(el):
    return ''.join(t.text or '' for t in el.findall('.//w:t',ns))
def table_text(tbl):
    rows=[]
    for tr in tbl.findall('w:tr',ns):
        cells=[]
        for tc in tr.findall('w:tc',ns):
            parts=[]
            for p in tc.findall('w:p',ns):
                s=text_of(p)
                if s: parts.append(s)
            cells.append(' / '.join(parts))
        rows.append(' | '.join(cells))
    return '\n'.join(rows)
lines=[]
for child in list(body):
    tag=child.tag.rsplit('}',1)[-1]
    if tag=='p':
        s=text_of(child)
        if s: lines.append(s)
    elif tag=='tbl':
        lines.append('[TABLE]')
        lines.append(table_text(child))
        lines.append('[/TABLE]')
dst.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'paragraph/table-order extraction saved: {dst}; chars={sum(map(len,lines))}; blocks={len(lines)}')
