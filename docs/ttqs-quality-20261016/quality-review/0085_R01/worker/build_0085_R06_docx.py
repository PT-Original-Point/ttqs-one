from __future__ import annotations
import copy, hashlib, json, re, subprocess
from datetime import datetime, timezone
from pathlib import Path
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(r"E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0085_R01")
BODY=ROOT/'worker'/'0085_R06_body.md'
SVG=ROOT/'evidence'/'0085_workflow_w1_w7.svg'
PNG=ROOT/'evidence'/'0085_workflow_w1_w7.png'
TEMP_MD=ROOT/'worker'/'0085_R06_pandoc_input.md'
REF=ROOT/'inputs'/'pandoc_reference_R02.docx'
DOCX=ROOT/'candidate'/'0085_R06.docx'
BUILD=ROOT/'evidence'/'build_receipt_R06.json'
PANDOC=Path(r'C:\Users\J\AppData\Local\Pandoc\pandoc.exe')


def h(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def set_run_font(run, name='Microsoft JhengHei', size=None, bold=None, color=None):
    run.font.name=name
    rpr=run._element.get_or_add_rPr()
    rfonts=rpr.rFonts
    if rfonts is None:
        rfonts=OxmlElement('w:rFonts'); rpr.insert(0,rfonts)
    for attr in ('ascii','hAnsi','eastAsia','cs'): rfonts.set(qn('w:'+attr),name)
    if size is not None: run.font.size=Pt(size)
    if bold is not None: run.bold=bold
    if color is not None: run.font.color.rgb=RGBColor(*color)
def set_section(sectPr, landscape:bool, section_type='nextPage'):
    pgSz=sectPr.find(qn('w:pgSz'))
    if pgSz is None: pgSz=OxmlElement('w:pgSz'); sectPr.insert(0,pgSz)
    if landscape:
        pgSz.set(qn('w:w'),'16838'); pgSz.set(qn('w:h'),'11906'); pgSz.set(qn('w:orient'),'landscape')
    else:
        pgSz.set(qn('w:w'),'11906'); pgSz.set(qn('w:h'),'16838'); pgSz.attrib.pop(qn('w:orient'),None)
    pgMar=sectPr.find(qn('w:pgMar'))
    if pgMar is None: pgMar=OxmlElement('w:pgMar'); sectPr.append(pgMar)
    for k,v in {'top':'850','bottom':'850','left':'850','right':'850','header':'425','footer':'425','gutter':'0'}.items(): pgMar.set(qn('w:'+k),v)
    typ=sectPr.find(qn('w:type'))
    if section_type:
        if typ is None: typ=OxmlElement('w:type'); sectPr.insert(0,typ)
        typ.set(qn('w:val'),section_type)
    elif typ is not None:
        sectPr.remove(typ)

def draw_svg(path:Path):
    width,height=1620,830
    cards=[
      (35,85,'W1','收集問題／知識需求','ROLE-COORD · Form-Q','個資疑慮或問題不具體 → RETURN / HOLD'),
      (430,85,'W2','選題與框架設計','ROLE-FACIL · Form-T','把討論直接寫成正式政策 → REJECT'),
      (825,85,'W3','記錄互動與相異意見','ROLE-RECORDER · Form-D / T','假共識或填寫真名 → REJECT'),
      (1220,85,'W4','抽取與整編知識產出','ROLE-CURATOR · Form-K','沒有來源卻寫成結論 → HOLD / RETURN'),
      (825,500,'W5','實務應用嘗試記錄','ROLE-COORD / ROLE-MEMBER · Form-A','以自述代替實際套用證據 → RETURN'),
      (430,500,'W6','檢查結果證據','ROLE-AUDIT · OUT1–OUT9','把觀察宣稱為學習因果成效 → REJECT'),
      (35,500,'W7','排程與後續行動追蹤','ROLE-FACIL · Form-F','追蹤責任、期限與未決事項'),
    ]
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
      '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#385B7A"/></marker></defs>',
      '<rect width="100%" height="100%" fill="#FFFFFF"/>',
      '<text x="810" y="34" text-anchor="middle" font-family="Microsoft JhengHei,sans-serif" font-size="24" font-weight="700" fill="#17365D">知識管理社群 W1–W7 作業流程與退回／保留條件</text>']
    # Main route arrows, top left-to-right, then down and bottom right-to-left.
    for x1,x2 in [(390,430),(785,825),(1180,1220)]:
        parts.append(f'<path d="M{x1} 180 L{x2-9} 180" stroke="#385B7A" stroke-width="5" fill="none" marker-end="url(#arrow)"/>')
    parts.append('<path d="M1397 295 L1397 400 L1002 400 L1002 491" stroke="#385B7A" stroke-width="5" fill="none" marker-end="url(#arrow)"/>')
    for x1,x2 in [(825,785),(430,390)]:
        parts.append(f'<path d="M{x1} 595 L{x2+9} 595" stroke="#385B7A" stroke-width="5" fill="none" marker-end="url(#arrow)"/>')
    for x,y,step,title,role,gate in cards:
        parts.append(f'<rect x="{x}" y="{y}" width="355" height="210" rx="18" fill="#F4F7FB" stroke="#5B7894" stroke-width="3"/>')
        parts.append(f'<rect x="{x}" y="{y}" width="355" height="42" rx="18" fill="#17365D"/>')
        parts.append(f'<text x="{x+18}" y="{y+29}" font-family="Microsoft JhengHei,sans-serif" font-size="24" font-weight="700" fill="#FFFFFF">{step}</text>')
        parts.append(f'<text x="{x+177}" y="{y+78}" text-anchor="middle" font-family="Microsoft JhengHei,sans-serif" font-size="22" font-weight="700" fill="#17365D">{title}</text>')
        parts.append(f'<text x="{x+177}" y="{y+111}" text-anchor="middle" font-family="Microsoft JhengHei,sans-serif" font-size="16" fill="#334E68">{role}</text>')
        parts.append(f'<line x1="{x+14}" y1="{y+132}" x2="{x+341}" y2="{y+132}" stroke="#C5D1DC" stroke-width="2"/>')
        parts.append(f'<text x="{x+177}" y="{y+157}" text-anchor="middle" font-family="Microsoft JhengHei,sans-serif" font-size="15" fill="#8B2C2C">{gate}</text>')
    parts.append('<text x="810" y="805" text-anchor="middle" font-family="Microsoft JhengHei,sans-serif" font-size="15" fill="#5B6573">所有節點均屬 SAMPLE / SYNTHETIC 流程示範；實際活動須另附 REAL 原始紀錄。</text>')
    parts.append('</svg>')
    path.write_text('\n'.join(parts),encoding='utf-8')

def draw_png(path:Path):
    width,height=1620,830
    im=Image.new('RGB',(width,height),'white'); d=ImageDraw.Draw(im)
    fontpath=Path(r'C:\Windows\Fonts\msjh.ttc')
    if not fontpath.exists(): fontpath=Path(r'C:\Windows\Fonts\msyh.ttc')
    if not fontpath.exists(): raise FileNotFoundError('Traditional Chinese UI font missing')
    ftitle=ImageFont.truetype(str(fontpath),24); fstep=ImageFont.truetype(str(fontpath),22)
    frole=ImageFont.truetype(str(fontpath),16); fgate=ImageFont.truetype(str(fontpath),16)
    fsmall=ImageFont.truetype(str(fontpath),16)
    d.text((810,34),'知識管理社群 W1–W7 作業流程與退回／保留條件',font=ftitle,fill='#17365D',anchor='mm')
    cards=[
      (35,85,'W1','收集問題／知識需求','ROLE-COORD · Form-Q','個資疑慮或問題不具體 → RETURN / HOLD'),
      (430,85,'W2','選題與框架設計','ROLE-FACIL · Form-T','把討論直接寫成正式政策 → REJECT'),
      (825,85,'W3','記錄互動與相異意見','ROLE-RECORDER · Form-D / T','假共識或填寫真名 → REJECT'),
      (1220,85,'W4','抽取與整編知識產出','ROLE-CURATOR · Form-K','沒有來源卻寫成結論 → HOLD / RETURN'),
      (825,500,'W5','實務應用嘗試記錄','ROLE-COORD / ROLE-MEMBER · Form-A','以自述代替實際套用證據 → RETURN'),
      (430,500,'W6','檢查結果證據','ROLE-AUDIT · OUT1–OUT9','把觀察宣稱為學習因果成效 → REJECT'),
      (35,500,'W7','排程與後續行動追蹤','ROLE-FACIL · Form-F','追蹤責任、期限與未決事項'),
    ]
    def arrow(points):
        d.line(points,fill='#385B7A',width=5,joint='curve')
        x1,y1=points[-2]; x2,y2=points[-1]
        import math
        a=math.atan2(y2-y1,x2-x1); L=15; spread=.58
        p1=(x2-L*math.cos(a-spread),y2-L*math.sin(a-spread)); p2=(x2-L*math.cos(a+spread),y2-L*math.sin(a+spread))
        d.polygon([(x2,y2),p1,p2],fill='#385B7A')
    for x1,x2 in [(390,430),(785,825),(1180,1220)]: arrow([(x1,190),(x2-8,190)])
    arrow([(1397,295),(1397,405),(1002,405),(1002,491)])
    for x1,x2 in [(825,785),(430,390)]: arrow([(x1,605),(x2+8,605)])
    for x,y,step,title,role,gate in cards:
        d.rounded_rectangle((x,y,x+355,y+210),radius=18,fill='#F4F7FB',outline='#5B7894',width=3)
        d.rounded_rectangle((x,y,x+355,y+44),radius=18,fill='#17365D')
        d.rectangle((x,y+24,x+355,y+44),fill='#17365D')
        d.text((x+18,y+23),step,font=fstep,fill='white',anchor='lm')
        d.text((x+177,y+84),title,font=fstep,fill='#17365D',anchor='mm')
        d.text((x+177,y+117),role,font=frole,fill='#334E68',anchor='mm')
        d.line((x+14,y+140,x+341,y+140),fill='#C5D1DC',width=2)
        d.text((x+177,y+174),gate,font=fgate,fill='#8B2C2C',anchor='mm')
    d.text((810,805),'所有節點均屬 SAMPLE / SYNTHETIC 流程示範；實際活動須另附 REAL 原始紀錄。',font=fsmall,fill='#5B6573',anchor='mm')
    im.save(path,format='PNG',optimize=True)

def apply_table_width(table, total_inches, widths=None, font_size=8.0):
    n=max(1,len(table.columns))
    if widths is None: widths=[total_inches/n]*n
    if len(widths)!=n: widths=[total_inches/n]*n
    twips=[str(round(w*1440)) for w in widths]
    tblPr=table._tbl.tblPr
    tblW=tblPr.find(qn('w:tblW'))
    if tblW is None: tblW=OxmlElement('w:tblW'); tblPr.append(tblW)
    tblW.set(qn('w:w'),str(sum(int(x) for x in twips))); tblW.set(qn('w:type'),'dxa')
    layout=tblPr.find(qn('w:tblLayout'))
    if layout is None: layout=OxmlElement('w:tblLayout'); tblPr.append(layout)
    layout.set(qn('w:type'),'fixed')
    grid=table._tbl.tblGrid
    for child in list(grid): grid.remove(child)
    for w in twips:
        gc=OxmlElement('w:gridCol'); gc.set(qn('w:w'),w); grid.append(gc)
    for row in table.rows:
        trPr=row._tr.get_or_add_trPr()
        if trPr.find(qn('w:cantSplit')) is None:
            trPr.append(OxmlElement('w:cantSplit'))
        for j,cell in enumerate(row.cells):
            w=twips[min(j,len(twips)-1)]
            cell.width=Inches(float(w)/1440)
            tcPr=cell._tc.get_or_add_tcPr()
            tcW=tcPr.find(qn('w:tcW'))
            if tcW is None: tcW=OxmlElement('w:tcW'); tcPr.append(tcW)
            tcW.set(qn('w:w'),w); tcW.set(qn('w:type'),'dxa')
            cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            for para in cell.paragraphs:
                para.paragraph_format.space_before=Pt(0); para.paragraph_format.space_after=Pt(1)
                for run in para.runs: set_run_font(run,size=font_size)
    if table.rows:
        trPr=table.rows[0]._tr.get_or_add_trPr()
        hdr=OxmlElement('w:tblHeader'); hdr.set(qn('w:val'),'true'); trPr.append(hdr)
        for cell in table.rows[0].cells:
            tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),'1F4E78'); tcPr.append(shd)
            for para in cell.paragraphs:
                # Keep a table's header row with its first data row when a page
                # break would otherwise leave a blue header stranded at the
                # bottom of the preceding page.
                para.paragraph_format.keep_with_next=True
                for run in para.runs: set_run_font(run,size=font_size,bold=True,color=(255,255,255))

def main():
    if not REF.exists():
        res=subprocess.run([str(PANDOC),'--print-default-data-file','reference.docx'],check=True,capture_output=True)
        REF.write_bytes(res.stdout)
    draw_svg(SVG)
    draw_png(PNG)
    text=BODY.read_text(encoding='utf-8')
    pat=r'```mermaid\s*\n.*?\n```'
    text,n=re.subn(pat,'![W1-W7 流程圖](0085_workflow_w1_w7.png)',text,count=1,flags=re.S|re.I)
    if n!=1: raise RuntimeError(f'mermaid block replacement count={n}')
    TEMP_MD.write_text(text,encoding='utf-8')
    DOCX.parent.mkdir(parents=True,exist_ok=True)
    cmd=[str(PANDOC),str(TEMP_MD),'--from=gfm+raw_html','--to=docx',f'--reference-doc={REF}',f'--output={DOCX}',f'--resource-path={ROOT / "evidence"}']
    run=subprocess.run(cmd,cwd=str(ROOT),capture_output=True,text=True,encoding='utf-8',errors='replace')
    if run.returncode: raise RuntimeError(json.dumps({'returncode':run.returncode,'stdout':run.stdout[-2000:],'stderr':run.stderr[-4000:]}))
    doc=Document(str(DOCX))
    # Preserve a restrained, readable Chinese Word style.
    if 'Table Grid' not in [st.name for st in doc.styles]:
        doc.styles.add_style('Table Grid', WD_STYLE_TYPE.TABLE)
    for s in doc.sections:
        s.page_width=Inches(8.27); s.page_height=Inches(11.69)
        s.top_margin=Inches(.59); s.bottom_margin=Inches(.59); s.left_margin=Inches(.59); s.right_margin=Inches(.59)
        s.header_distance=Inches(.28); s.footer_distance=Inches(.28)
    for stylename,size,color in [('Normal',10,(45,55,65)),('Body Text',10,(45,55,65)),('Heading 1',16,(31,78,121)),('Heading 2',13,(31,78,121)),('Heading 3',11,(55,90,125)),('Heading 4',10,(55,90,125))]:
        st=doc.styles[stylename]; st.font.name='Microsoft JhengHei'; st.font.size=Pt(size); st.font.color.rgb=RGBColor(*color)
        rpr=st._element.get_or_add_rPr(); rf=rpr.rFonts
        if rf is None: rf=OxmlElement('w:rFonts'); rpr.insert(0,rf)
        for a in ('ascii','hAnsi','eastAsia','cs'): rf.set(qn('w:'+a),'Microsoft JhengHei')
        if stylename.startswith('Heading'): st.paragraph_format.keep_with_next=True
    for p in doc.paragraphs:
        for r in p.runs: set_run_font(r)
    # Add header/footer text and a live PAGE field before cloning section properties.
    for section in doc.sections:
        hp=section.header.paragraphs[0]; hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        hp.text='TTQS ONE｜DOCX 0085｜候選 R06';
        for r in hp.runs: set_run_font(r,size=8,color=(95,105,115))
        fp=section.footer.paragraphs[0]; fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
        fp.text='SAMPLE / SYNTHETIC｜REAL = UNKNOWN/HOLD｜頁 ';
        for r in fp.runs: set_run_font(r,size=8,color=(95,105,115))
        fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); fp._p.append(fld)
    body=doc._element.body
    boundaries=[
      ('11A.2 Form-T',True),('11A.4 Form-K',False),
      
      ('\u9644\u9304 E\uff1a\u5408\u6210\u8cc7\u6599\u66ff\u63db\u6e05\u518a',True),
    ]
    targets=[]
    for needle,orient in boundaries:
        found=None
        for p in doc.paragraphs:
            if needle in p.text:
                found=p._p; break
        if found is None: raise RuntimeError(f'heading boundary missing: {needle}')
        targets.append((found,orient,needle))
    # Insert continuous section breaks; each p-level sectPr captures the section that ends there.
    final=body.sectPr
    current=False
    for target,desired,needle in targets:
        br=OxmlElement('w:p'); ppr=OxmlElement('w:pPr')
        props=copy.deepcopy(final)
        set_section(props,current,'nextPage')
        ppr.append(props); br.append(ppr); target.addprevious(br)
        current=desired
    set_section(final,current,None)
    # Assign tables to portrait/landscape sections and set fixed readable widths.
    active=False
    current_heading=''
    for child in body.iterchildren():
        if child.tag==qn('w:p'):
            tx=''.join(child.itertext())
            ppr=child.find(qn('w:pPr'))
            pstyle=ppr.find(qn('w:pStyle')) if ppr is not None else None
            if pstyle is not None and pstyle.get(qn('w:val'), '').startswith('Heading'):
                current_heading=tx
            for target,desired,needle in targets:
                if child is target: active=desired; break
        elif child.tag==qn('w:tbl'):
            from docx.table import Table
            table=Table(child,doc._body)
            coln=max(1,len(table.columns))
            alltext=' '.join(cell.text for row in table.rows for cell in row.cells)
            if 'R85-001' in alltext:
                widths=[.60,1.55,1.25,2.70,1.40,2.90]; total=sum(widths); fs=7.2
            else:
                total=10.3 if active else 7.1
                fs=7.4 if coln>=8 else (8.0 if active else 8.3)
                widths=None
            table.style='Table Grid'
            tblPr=table._tbl.tblPr
            borders=tblPr.find(qn('w:tblBorders'))
            if borders is None: borders=OxmlElement('w:tblBorders'); tblPr.append(borders)
            for edge in ('top','left','bottom','right','insideH','insideV'):
                tag=qn('w:'+edge); el=borders.find(tag)
                if el is None: el=OxmlElement('w:'+edge); borders.append(el)
                el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'4'); el.set(qn('w:space'),'0'); el.set(qn('w:color'),'C7D2DE')
            apply_table_width(table,total,widths,fs)
            min_height=None
            if '11A.2 Form-T' in current_heading: min_height=800
            elif '11A.3 Form-D' in current_heading: min_height=780
            elif '11A.6 Form-F' in current_heading: min_height=600
            if min_height:
                for row in table.rows[1:]:
                    trPr=row._tr.get_or_add_trPr()
                    trHeight=OxmlElement('w:trHeight'); trHeight.set(qn('w:val'),str(min_height)); trHeight.set(qn('w:hRule'),'atLeast'); trPr.append(trHeight)
    # Keep heading lines together and improve paragraph rhythm.
    for p in doc.paragraphs:
        if p.style and p.style.name.startswith('Heading'):
            p.paragraph_format.keep_with_next=True
        if p.style and p.style.name in ('Normal','Body Text'):
            p.paragraph_format.space_after=Pt(4)
            p.paragraph_format.line_spacing=1.08
    doc.core_properties.title='DOCX 0085｜知識管理社群：討論主題、互動與學習應用分析｜候選 R06'
    doc.core_properties.subject='I17C-E04｜官方方框091｜SAMPLE/SYNTHETIC candidate'
    doc.core_properties.author='原始點協會 TTQS ONE 文件候選產製流程'
    doc.save(str(DOCX))
    receipt={'project_id':'TTQS_ONE','doc_id':'0085','requirement_id':'I17C-E04','checkbox':'091','revision':'R06','method':'Pandoc 3.6.3 Markdown conversion + python-docx styles, usable-row heights for blank Form-T/D/F, repeat table headers, A4 portrait/landscape sectioning, SVG source and PNG workflow diagram','source_body_sha256':h(BODY),'blueprint_sha256':h(ROOT/'inputs'/'UNIQUE_BLUEPRINT_0085_R02.md'),'diagram_svg_sha256':h(SVG),'diagram_png_sha256':h(PNG),'docx_path':str(DOCX),'docx_sha256':h(DOCX),'docx_bytes':DOCX.stat().st_size,'pandoc_returncode':run.returncode,'pandoc_stderr':run.stderr[-2000:],'built_at_utc':datetime.now(timezone.utc).isoformat(),'state':'CANDIDATE_NOT_ACCEPTED'}
    BUILD.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,ensure_ascii=False,indent=2))
if __name__=='__main__': main()

