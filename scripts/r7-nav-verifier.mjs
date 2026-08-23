import {normalizeAppsScriptHtmlServiceWrapper} from './external-blackbox-classifier.mjs';

const DEFAULT_CANONICAL_RE=/^https:\/\/script\.google\.com\/macros\/s\/[A-Za-z0-9_-]+\/exec$/;

function escPattern(value){return String(value).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}

export function normalizeR7NavigationHtml(input){
  let out=normalizeAppsScriptHtmlServiceWrapper(String(input??''));
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

function headingText(card){
  const match=String(card).match(/<h[1-6]\b[^>]*>([\s\S]*?)<\/h[1-6]>/i);
  return match?.[1]?.replace(/<[^>]+>/g,'').trim()??null;
}

function linksWithText(card,text){
  const links=String(card).match(/<a\b[^>]*>[\s\S]*?<\/a>/gi)||[];
  return links.filter(link=>link.replace(/<[^>]+>/g,'').trim()===text).map(link=>{
    const open=link.match(/^<a\b[^>]*>/i)?.[0]||'';
    return {href:attrValue(open,'href'),target:attrValue(open,'target'),html:link};
  });
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

  const cardEvidence=[];
  for(let index=0;index<cards.length;index++){
    const card=cards[index];
    const title=headingText(card);
    if(!title)return {pass:false,code:'MATRIX_DOCUMENT_TITLE_MISSING',indicator:id,cardIndex:index+1,expectedHeading,documentCardCount:cards.length,normalized};
    if(!/[\u3400-\u9fff]/.test(title))return {pass:false,code:'MATRIX_DOCUMENT_TITLE_NOT_CHINESE',indicator:id,cardIndex:index+1,title,expectedHeading,documentCardCount:cards.length,normalized};
    const openLinks=linksWithText(card,'開啟文件');
    if(openLinks.length<1)return {pass:false,code:'MATRIX_OPEN_DOCUMENT_MISSING',indicator:id,cardIndex:index+1,title,expectedHeading,documentCardCount:cards.length,normalized};
    const canonicalLinks=openLinks.filter(x=>x.href&&new RegExp(`^${escPattern(canonical)}\\?artifact=[A-Za-z0-9._~-]+$`).test(x.href)&&x.target==='_top');
    if(canonicalLinks.length<1)return {pass:false,code:'MATRIX_CANONICAL_ARTIFACT_ROUTE_MISSING',indicator:id,cardIndex:index+1,title,expectedHeading,documentCardCount:cards.length,openLinks,normalized};
    cardEvidence.push({cardIndex:index+1,title,openDocumentCount:openLinks.length,canonicalArtifactCount:canonicalLinks.length,firstCanonicalArtifactUrl:canonicalLinks[0].href});
  }

  return {
    pass:true,
    code:null,
    indicator:id,
    expectedHeading,
    documentCardCount:cards.length,
    chineseDocumentCardCount:cardEvidence.length,
    openDocumentCount:cardEvidence.reduce((sum,row)=>sum+row.openDocumentCount,0),
    canonicalArtifactRouteCount:cardEvidence.reduce((sum,row)=>sum+row.canonicalArtifactCount,0),
    everyCardHasChineseTitle:true,
    everyCardHasOpenDocument:true,
    everyCardHasCanonicalArtifactRoute:true,
    firstCanonicalArtifactUrl:cardEvidence[0].firstCanonicalArtifactUrl,
    cardEvidence,
    normalized
  };
}

export function assertCanonical(canonical){
  if(!DEFAULT_CANONICAL_RE.test(String(canonical||'')))throw new Error('R7_NAV_CANONICAL_INVALID');
  return canonical;
}
