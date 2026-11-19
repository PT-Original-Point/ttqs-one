import re, sys, os, zipfile, hashlib, json, datetime, math
import xml.etree.ElementTree as ET
from pathlib import Path

src=Path(sys.argv[1]); out=Path(sys.argv[2]); md=src.read_text(encoding='utf-8-sig')
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'; REL='http://schemas.openxmlformats.org/package/2006/relationships'; CT='http://schemas.openxmlformats.org/package/2006/content-types'; CORE='http://schemas.openxmlformats.org/package/2006/metadata/core-properties'; DC='http://purl.org/dc/elements/1.1/'; DCT='http://purl.org/dc/terms/'; APP='http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'; VT='http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes'; XML='http://www.w3.org/XML/1998/namespace'
for p,n in [(W,'w'),(R,'r'),(REL,'rel'),(CT,'ct'),(CORE,'cp'),(DC,'dc'),(DCT,'dcterms'),(APP,'ep'),(VT,'vt')]: ET.register_namespace(n,p)
def q(ns,tag): return '{%s}%s'%(ns,tag)
def el(parent,ns,tag,attrs=None,text=None):
    x=ET.SubElement(parent,q(ns,tag),attrs or {})
    if text is not None: x.text=str(text)
    return x

def inline_runs(p, text, size=None, table=False):
    pat=re.compile(r'(\*\*.+?\*\*|(?<!\*)\*[^*]+\*|`[^`]+`)')
    pos=0
    for m in pat.finditer(text):
        if m.start()>pos: add_run(p,text[pos:m.start()],size=size,table=table)
        tok=m.group(0); bold=tok.startswith('**'); italic=(tok.startswith('*') and not bold); code=tok.startswith('`')
        content=tok[2:-2] if bold else tok[1:-1] if italic or code else tok
        add_run(p,content,bold=bold,italic=italic,code=code,size=size,table=table);pos=m.end()
    if pos<len(text): add_run(p,text[pos:],size=size,table=table)

def add_run(parent,text,bold=False,italic=False,code=False,size=None,table=False):
    r=el(parent,W,'r');rp=el(r,W,'rPr')
    fonts=el(rp,W,'rFonts',{q(W,'ascii'):'Consolas' if code else 'Microsoft JhengHei',q(W,'hAnsi'):'Consolas' if code else 'Microsoft JhengHei',q(W,'eastAsia'):'Microsoft JhengHei',q(W,'cs'):'Microsoft JhengHei'})
    if bold: el(rp,W,'b')
    if italic: el(rp,W,'i')
    el(rp,W,'sz',{q(W,'val'):str(size if size is not None else (19 if table or code else 22))})
    el(rp,W,'szCs',{q(W,'val'):str(size if size is not None else (19 if table or code else 22))})
    if code: el(rp,W,'color',{q(W,'val'):'404040'})
    t=el(r,W,'t',{q(XML,'space'):'preserve'},text)

def add_p(body,text='',style=None,num=None,quote=False):
    p=el(body,W,'p');pp=el(p,W,'pPr')
    if style: el(pp,W,'pStyle',{q(W,'val'):style})
    elif quote: el(pp,W,'pStyle',{q(W,'val'):'Quote'})
    if num is not None:
        np=el(pp,W,'numPr');el(np,W,'ilvl',{q(W,'val'):'0'});el(np,W,'numId',{q(W,'val'):str(num)})
    if style and style.startswith('Heading'): el(pp,W,'keepNext')
    el(pp,W,'keepLines')
    inline_runs(p,text)
    return p

def split_cells(line): return [c.strip() for c in line.strip().strip('|').split('|')]
def add_table(body,rows):
    if not rows:return
    n=max(len(r) for r in rows); width=9950
    cols=[[str(row[ci]).replace('**','').replace(chr(96),'') for row in rows if ci<len(row) and str(row[ci]).strip()] for ci in range(n)]
    scores=[]
    for vals in cols:
        lengths=[max(1,len(v)) for v in vals] or [1]
        scores.append(math.sqrt(max(1.0,0.6*sum(lengths)/len(lengths)+0.4*max(lengths))))
    low=max(520,int(width*0.052)); high=int(width*0.38); widths=[0]*n; active=set(range(n)); remaining=width
    while active:
        weight=sum(scores[i] for i in active)
        capped=[]
        for i in list(active):
            tentative=remaining*scores[i]/weight
            if tentative<low: widths[i]=low;remaining-=low;active.remove(i);capped.append(i)
            elif tentative>high: widths[i]=high;remaining-=high;active.remove(i);capped.append(i)
        if not capped:
            alloc={i:remaining*scores[i]/weight for i in active}
            for i in active: widths[i]=int(alloc[i])
            remaining-=sum(widths[i] for i in active)
            for i in sorted(active):
                if remaining<=0: break
                widths[i]+=1;remaining-=1
            break
    if sum(widths)!=width: widths[-1]+=width-sum(widths)
    tbl=el(body,W,'tbl');pr=el(tbl,W,'tblPr')
    el(pr,W,'tblW',{q(W,'w'):str(width),q(W,'type'):'dxa'});el(pr,W,'tblLayout',{q(W,'type'):'fixed'})
    borders=el(pr,W,'tblBorders')
    for edge in ['top','left','bottom','right','insideH','insideV']: el(borders,W,edge,{q(W,'val'):'single',q(W,'sz'):'4',q(W,'space'):'0',q(W,'color'):'8092A5'})
    mar=el(pr,W,'tblCellMar')
    for edge,val in [('top','55'),('start','65'),('bottom','55'),('end','65')]: el(mar,W,edge,{q(W,'w'):val,q(W,'type'):'dxa'})
    grid=el(tbl,W,'tblGrid')
    for w in widths: el(grid,W,'gridCol',{q(W,'w'):str(w)})
    for ri,row in enumerate(rows):
        tr=el(tbl,W,'tr')
        if ri==0: trpr=el(tr,W,'trPr');el(trpr,W,'tblHeader',{q(W,'val'):'true'})
        vals=row+['']*(n-len(row))
        for ci,val in enumerate(vals):
            tc=el(tr,W,'tc');tcp=el(tc,W,'tcPr');el(tcp,W,'tcW',{q(W,'w'):str(widths[ci]),q(W,'type'):'dxa'})
            if ri==0: el(tcp,W,'shd',{q(W,'val'):'clear',q(W,'color'):'auto',q(W,'fill'):'D9EAF7'})
            p=el(tc,W,'p');pp=el(p,W,'pPr');el(pp,W,'pStyle',{q(W,'val'):'TableText'});el(pp,W,'spacing',{q(W,'after'):'20',q(W,'line'):'230',q(W,'lineRule'):'auto'});inline_runs(p,val,size=19,table=True)
    return tbl

root=ET.Element(q(W,'document'));body=el(root,W,'body');rows=[];in_ul=False;in_ol=False;title_used=False
for raw in md.splitlines():
    s=raw.strip()
    if s.startswith('|') and s.endswith('|'):
        if re.match(r'^\|\s*:?-{3,}',s): continue
        rows.append(split_cells(s));continue
    if rows: add_table(body,rows);rows=[]
    if not s or re.fullmatch(r'-{3,}',s): continue
    h=re.match(r'^(#{1,6})\s+(.+)$',s)
    if h:
        level=len(h.group(1))
        if level==1 and not title_used: add_p(body,h.group(2),'Title');title_used=True
        else: add_p(body,h.group(2),'Heading'+str(min(level,6)))
        continue
    b=re.match(r'^[-*+]\s+(.+)$',s)
    if b: add_p(body,b.group(1),num=1);continue
    o=re.match(r'^\d+[.)]\s+(.+)$',s)
    if o: add_p(body,o.group(1),num=2);continue
    quote=re.match(r'^>\s?(.*)$',s)
    if quote: add_p(body,quote.group(1),quote=True);continue
    add_p(body,s)
if rows:add_table(body,rows)
sect=el(body,W,'sectPr');el(sect,W,'footerReference',{q(W,'type'):'default',q(R,'id'):'rId3'});pg=el(sect,W,'pgSz',{q(W,'w'):'11906',q(W,'h'):'16838'});el(sect,W,'pgMar',{q(W,'top'):'963',q(W,'right'):'963',q(W,'bottom'):'963',q(W,'left'):'963',q(W,'header'):'480',q(W,'footer'):'480',q(W,'gutter'):'0'});el(sect,W,'cols',{q(W,'space'):'720'})
xml_decl=b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n';document=xml_decl+ET.tostring(root,encoding='utf-8')
styles=ET.Element(q(W,'styles'));dd=el(styles,W,'docDefaults');rdd=el(dd,W,'rPrDefault');rpr=el(rdd,W,'rPr');el(rpr,W,'rFonts',{q(W,'ascii'):'Microsoft JhengHei',q(W,'hAnsi'):'Microsoft JhengHei',q(W,'eastAsia'):'Microsoft JhengHei'});el(rpr,W,'sz',{q(W,'val'):'22'});el(rpr,W,'szCs',{q(W,'val'):'22'});pdd=el(dd,W,'pPrDefault');ppr=el(pdd,W,'pPr');el(ppr,W,'spacing',{q(W,'after'):'100',q(W,'line'):'276',q(W,'lineRule'):'auto'});el(ppr,W,'widowControl')
def style(id,name,based=None,size=None,bold=False,color=None,keep=False):
    st=el(styles,W,'style',{q(W,'type'):'paragraph',q(W,'styleId'):id});el(st,W,'name',{q(W,'val'):name})
    if based:el(st,W,'basedOn',{q(W,'val'):based})
    if id=='Normal':el(st,W,'qFormat')
    pp=el(st,W,'pPr')
    if keep:el(pp,W,'keepNext')
    if size or bold or color:
        rp=el(st,W,'rPr');el(rp,W,'rFonts',{q(W,'ascii'):'Microsoft JhengHei',q(W,'hAnsi'):'Microsoft JhengHei',q(W,'eastAsia'):'Microsoft JhengHei'})
        if size:el(rp,W,'sz',{q(W,'val'):str(size)});el(rp,W,'szCs',{q(W,'val'):str(size)})
        if bold:el(rp,W,'b')
        if color:el(rp,W,'color',{q(W,'val'):color})
    return st
style('Normal','Normal',size=22);style('Title','Title','Normal',34,True,'000000',True);style('Heading1','heading 1','Normal',36,True,'17365D',True);style('Heading2','heading 2','Normal',30,True,'1F4E79',True);style('Heading3','heading 3','Normal',26,True,'2F5597',True);style('Heading4','heading 4','Normal',23,True,'2F5597',True);style('Heading5','heading 5','Normal',22,True,'2F5597',True);style('Heading6','heading 6','Normal',22,True,'2F5597',True);style('TableText','Table Text','Normal',19)
stylesxml=xml_decl+ET.tostring(styles,encoding='utf-8')
num=ET.Element(q(W,'numbering'))
for aid,fmt,txt in [(0,'bullet','•'),(1,'decimal','%1.')]:
    ab=el(num,W,'abstractNum',{q(W,'abstractNumId'):str(aid)});el(ab,W,'multiLevelType',{q(W,'val'):'singleLevel'});lvl=el(ab,W,'lvl',{q(W,'ilvl'):'0'});el(lvl,W,'start',{q(W,'val'):'1'});el(lvl,W,'numFmt',{q(W,'val'):fmt});el(lvl,W,'lvlText',{q(W,'val'):txt});el(lvl,W,'lvlJc',{q(W,'val'):'left'});pp=el(lvl,W,'pPr');el(pp,W,'tabs');el(pp,W,'ind',{q(W,'left'):'720',q(W,'hanging'):'360'});rp=el(lvl,W,'rPr');el(rp,W,'rFonts',{q(W,'ascii'):'Symbol' if aid==0 else 'Microsoft JhengHei',q(W,'hAnsi'):'Symbol' if aid==0 else 'Microsoft JhengHei'})
for nid,aid in [(1,0),(2,1)]: n=el(num,W,'num',{q(W,'numId'):str(nid)});el(n,W,'abstractNumId',{q(W,'val'):str(aid)})
numberingxml=xml_decl+ET.tostring(num,encoding='utf-8')
settings=ET.Element(q(W,'settings'));el(settings,W,'zoom',{q(W,'percent'):'100'});el(settings,W,'defaultTabStop',{q(W,'val'):'720'});compat=el(settings,W,'compat');el(compat,W,'compatSetting',{q(W,'name'):'compatibilityMode',q(W,'uri'):'http://schemas.microsoft.com/office/word',q(W,'val'):'15'})
footer=ET.Element(q(W,'ftr'));p=el(footer,W,'p');pp=el(p,W,'pPr');el(pp,W,'jc',{q(W,'val'):'center'});add_run(p,'頁碼 ',size=18);r=el(p,W,'r');el(r,W,'fldChar',{q(W,'fldCharType'):'begin'});r=el(p,W,'r');el(r,W,'instrText',{q(XML,'space'):'preserve'},' PAGE ');r=el(p,W,'r');el(r,W,'fldChar',{q(W,'fldCharType'):'end'})
rels=ET.Element(q(REL,'Relationships'));ET.SubElement(rels,q(REL,'Relationship'),{'Id':'rId1','Type':R+'/styles','Target':'styles.xml'});ET.SubElement(rels,q(REL,'Relationship'),{'Id':'rId2','Type':R+'/numbering','Target':'numbering.xml'});ET.SubElement(rels,q(REL,'Relationship'),{'Id':'rId3','Type':R+'/footer','Target':'footer1.xml'})
## footerReference was attached once when sectPr was first created; avoid duplicate relationship elements.
# settings/styles and document part relationships
rootrels=ET.Element(q(REL,'Relationships'));ET.SubElement(rootrels,q(REL,'Relationship'),{'Id':'rId1','Type':'http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument','Target':'word/document.xml'});ET.SubElement(rootrels,q(REL,'Relationship'),{'Id':'rId2','Type':CORE+'/core-properties','Target':'docProps/core.xml'});ET.SubElement(rootrels,q(REL,'Relationship'),{'Id':'rId3','Type':APP+'/extended-properties','Target':'docProps/app.xml'})
content=ET.Element(q(CT,'Types'));ET.SubElement(content,q(CT,'Default'),{'Extension':'rels','ContentType':'application/vnd.openxmlformats-package.relationships+xml'});ET.SubElement(content,q(CT,'Default'),{'Extension':'xml','ContentType':'application/xml'});ET.SubElement(content,q(CT,'Override'),{'PartName':'/word/document.xml','ContentType':'application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml'});ET.SubElement(content,q(CT,'Override'),{'PartName':'/word/styles.xml','ContentType':'application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml'});ET.SubElement(content,q(CT,'Override'),{'PartName':'/word/numbering.xml','ContentType':'application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml'});ET.SubElement(content,q(CT,'Override'),{'PartName':'/word/settings.xml','ContentType':'application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml'});ET.SubElement(content,q(CT,'Override'),{'PartName':'/word/footer1.xml','ContentType':'application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml'});ET.SubElement(content,q(CT,'Override'),{'PartName':'/docProps/core.xml','ContentType':'application/vnd.openxmlformats-package.core-properties+xml'});ET.SubElement(content,q(CT,'Override'),{'PartName':'/docProps/app.xml','ContentType':'application/vnd.openxmlformats-officedocument.extended-properties+xml'})
core=ET.Element(q(CORE,'coreProperties'));el(core,DC,'title',text='0025｜訓練評估與實施標準化作業程序SOP（SAMPLE/SYNTHETIC）');el(core,DC,'creator',text='TTQS ONE Candidate Builder');el(core,DCT,'created',text=datetime.datetime.now(datetime.timezone.utc).isoformat());el(core,DCT,'modified',text=datetime.datetime.now(datetime.timezone.utc).isoformat())
app=ET.Element(q(APP,'Properties'));el(app,APP,'Application',text='Microsoft Word');el(app,APP,'DocSecurity',text='0');el(app,APP,'ScaleCrop',text='false');vt=el(app,APP,'HeadingPairs');vec=el(vt,VT,'vector',{q(VT,'size'):'2',q(VT,'baseType'):'variant'});v=el(vec,VT,'variant');el(v,VT,'lpstr',text='Title');v=el(vec,VT,'variant');el(v,VT,'i4',text='1');el(app,APP,'TitlesOfParts');
# relationships for document parts
ET.SubElement(rels,q(REL,'Relationship'),{'Id':'rId4','Type':R+'/settings','Target':'settings.xml'})
# zip output
parts={'[Content_Types].xml':ET.tostring(content,encoding='utf-8',xml_declaration=True),'_rels/.rels':ET.tostring(rootrels,encoding='utf-8',xml_declaration=True),'word/document.xml':ET.tostring(root,encoding='utf-8',xml_declaration=True),'word/_rels/document.xml.rels':ET.tostring(rels,encoding='utf-8',xml_declaration=True),'word/styles.xml':stylesxml,'word/numbering.xml':numberingxml,'word/settings.xml':ET.tostring(settings,encoding='utf-8',xml_declaration=True),'word/footer1.xml':ET.tostring(footer,encoding='utf-8',xml_declaration=True),'docProps/core.xml':ET.tostring(core,encoding='utf-8',xml_declaration=True),'docProps/app.xml':ET.tostring(app,encoding='utf-8',xml_declaration=True)}
out.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for name,data in parts.items():z.writestr(name,data)
sha=hashlib.sha256(out.read_bytes()).hexdigest();receipt={'status':'OPENXML_DOCX_CREATED','work_id':'TTQS_ONE_0025_I04-E04_SCOPED_REPAIR_BUILD_R02_20261119','doc_id':'0025','requirement_id':'I04-E04','source_manuscript_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'candidate_path':str(out),'candidate_sha256':sha,'bytes':out.stat().st_size,'paragraph_count':len(root.findall('.//'+q(W,'p'))),'table_count':len(root.findall('.//'+q(W,'tbl'))),'table_cell_text_min_half_points':19,'body_style_points':11,'page_size':'A4','created_at_local':datetime.datetime.now().astimezone().isoformat(),'generator':'Scoped standard-library OpenXML builder; no third-party packages'}
Path(str(out)+'.build.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
