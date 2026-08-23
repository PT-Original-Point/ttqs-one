const DEFAULT_CANONICAL_RE=/^https:\/\/script\.google\.com\/macros\/s\/[A-Za-z0-9_-]+\/exec$/;

function escPattern(value){return String(value).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}

export function normalizeR7NavigationHtml(input){
  let out=String(input??'');
  for(let pass=0;pass<16;pass++){
    const before=out;
    out=out
      .replace(/\\x3c/gi,'<').replace(/\\u003c/gi,'<')
      .replace(/\\x3e/gi,'>').replace(/\\u003e/gi,'>')
      .replace(/\\x3d/gi,'=').replace(/\\u003d/gi,'=')
      .replace(/\\x22/gi,'"').replace(/\\u0022/gi,'"')
      .replace(/\\x27/gi,"'").replace(/\\u0027/gi,"'")
      .replace(/\\x26/gi,'&').replace(/\\u0026/gi,'&')
      .replace(/\\x2f/gi,'/').replace(/\\u002f/gi,'/')
      .replace(/\\\//g,'/').replace(/\\"/g,'"').replace(/\\'/g,"'")
      .replace(/&lt;/gi,'<').replace(/&gt;/gi,'>').replace(/&quot;/gi,'"')
      .replace(/&#39;|&apos;/gi,"'").replace(/&amp;/gi,'&');
    if(out===before)break;
  }
  return out;
}

function elementByDataAttribute(html,tag,attribute,value){
  const source=normalizeR7NavigationHtml(html);
  const pattern=new RegExp(`<${tag}\\b(?=[^>]*\\b${escPattern(attribute)}=["']${escPattern(value)}["'])[^>]*>[\\s\\S]*?<\\/${tag}>`,'i');
  return source.match(pattern)?.[0]||null;
}

function attrValue(openTag,name){
  const m=String(openTag).match(new RegExp(`\\b${escPattern(name)}=["']([^"']*)["']`,'i'));
  return m?.[1]??null;
}

function openTagWithAttribute(element,tag,name,value){
  const matches=String(element).match(new RegExp(`<${tag}\\b[^>]*>`,'gi'))||[];
  return matches.find(candidate=>attrValue(candidate,name)===value)||null;
}

function linkText(element,openTag){
  if(!openTag)return '';
  const start=String(element).indexOf(openTag);
  if(start<0)return '';
  const tail=String(element).slice(start+openTag.length);
  const close=tail.search(/<\/a>/i);
  if(close<0)return '';
  return tail.slice(0,close).replace(/<[^>]+>/g,'').trim();
}

export function verifyHomeIndicatorRoute(input,{indicator,canonical}){
  const id=String(indicator);
  const normalized=normalizeR7NavigationHtml(input);
  const expectedUrl=`${canonical}?indicator=${id}`;
  const card=elementByDataAttribute(normalized,'article','data-indicator',id);
  if(!card)return {pass:false,code:'HOME_INDICATOR_CARD_MISSING',indicator:id,expectedUrl,normalized};
  const linkOpen=openTagWithAttribute(card,'a','data-top-level-nav','true');
  if(!linkOpen)return {pass:false,code:'HOME_INDICATOR_LINK_MISSING',indicator:id,expectedUrl,card,normalized};
  const href=attrValue(linkOpen,'href');
  const target=attrValue(linkOpen,'target');
  const text=linkText(card,linkOpen);
  if(href===null)return {pass:false,code:'HOME_INDICATOR_HREF_MISSING',indicator:id,expectedUrl,card,linkOpen,target,linkText:text,normalized};
  if(href!==expectedUrl)return {pass:false,code:'HOME_INDICATOR_CANONICAL_URL_FAIL',indicator:id,expectedUrl,actualUrl:href,card,linkOpen,target,linkText:text,normalized};
  if(target!=='_top')return {pass:false,code:'HOME_INDICATOR_TARGET_FAIL',indicator:id,expectedUrl,actualUrl:href,target,card,linkOpen,linkText:text,normalized};
  if(text!=='查看文件與證據')return {pass:false,code:'HOME_INDICATOR_LABEL_FAIL',indicator:id,expectedUrl,actualUrl:href,target,linkText:text,card,linkOpen,normalized};
  return {pass:true,code:null,indicator:id,expectedUrl,actualUrl:href,target,linkText:text,card,linkOpen,normalized};
}

export function verifyEvidenceMatrixLayer(input,{indicator,canonical}){
  const id=String(indicator);
  const normalized=normalizeR7NavigationHtml(input);
  const expectedHeading=`指標 ${id}｜查看文件與證據`;
  if(!normalized.includes(`data-matrix-indicator="${id}"`)&&!normalized.includes(`data-matrix-indicator='${id}'`))return {pass:false,code:'MATRIX_IDENTITY_FAIL',indicator:id,expectedHeading,normalized};
  if(!normalized.includes(expectedHeading))return {pass:false,code:'MATRIX_CHINESE_HEADING_MISSING',indicator:id,expectedHeading,normalized};
  if(!normalized.includes('TEST／SAMPLE／CONTROL'))return {pass:false,code:'MATRIX_SIMULATION_WARNING_MISSING',indicator:id,expectedHeading,normalized};
  const cards=normalized.match(/<article\b(?=[^>]*\bdata-document-card=["']true["'])[^>]*>[\s\S]*?<\/article>/gi)||[];
  if(cards.length<1)return {pass:false,code:'MATRIX_DOCUMENT_CARD_MISSING',indicator:id,expectedHeading,normalized};
  const chineseCards=cards.filter(card=>/<h[1-6]\b[^>]*>[\s\S]*?[\u3400-\u9fff][\s\S]*?<\/h[1-6]>/i.test(card));
  if(chineseCards.length<1)return {pass:false,code:'MATRIX_CHINESE_DOCUMENT_CARD_MISSING',indicator:id,expectedHeading,documentCardCount:cards.length,normalized};
  const openLinks=[];
  for(const card of cards){
    const links=card.match(/<a\b[^>]*>[\s\S]*?<\/a>/gi)||[];
    for(const link of links){
      if(!link.includes('開啟文件'))continue;
      const open=link.match(/^<a\b[^>]*>/i)?.[0]||'';
      openLinks.push({href:attrValue(open,'href'),target:attrValue(open,'target'),html:link});
    }
  }
  if(openLinks.length<1)return {pass:false,code:'MATRIX_OPEN_DOCUMENT_MISSING',indicator:id,expectedHeading,documentCardCount:cards.length,normalized};
  const canonicalArtifact=openLinks.find(x=>x.href&&new RegExp(`^${escPattern(canonical)}\\?artifact=[A-Za-z0-9._~-]+$`).test(x.href)&&x.target==='_top');
  if(!canonicalArtifact)return {pass:false,code:'MATRIX_CANONICAL_ARTIFACT_ROUTE_MISSING',indicator:id,expectedHeading,documentCardCount:cards.length,openLinks,normalized};
  return {pass:true,code:null,indicator:id,expectedHeading,documentCardCount:cards.length,chineseDocumentCardCount:chineseCards.length,openDocumentCount:openLinks.length,firstCanonicalArtifactUrl:canonicalArtifact.href,normalized};
}

export function assertCanonical(canonical){
  if(!DEFAULT_CANONICAL_RE.test(String(canonical||'')))throw new Error('R7_NAV_CANONICAL_INVALID');
  return canonical;
}
