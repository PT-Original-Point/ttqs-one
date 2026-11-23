import {normalizeR7NavigationHtml} from './r7-nav-verifier.mjs';

function escPattern(value){return String(value).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}

function documentCards(input){
  const normalized=normalizeR7NavigationHtml(input);
  return {
    normalized,
    cards:normalized.match(/<article\b(?=[^>]*\bdata-document-card=["']true["'])[^>]*>[\s\S]*?<\/article>/gi)||[]
  };
}

export function verifyEvidenceMatrixItemIdentity(input,{officialRefId,artifactCode,canonical}){
  const ref=String(officialRefId);
  const code=String(artifactCode);
  const expectedUrl=`${canonical}?artifact=${encodeURIComponent(code)}`;
  const {normalized,cards}=documentCards(input);
  const linkPattern=new RegExp(`<a\\b(?=[^>]*\\bhref=["']${escPattern(expectedUrl)}["'])(?=[^>]*\\btarget=["']_top["'])[^>]*>[\\s\\S]*?開啟文件[\\s\\S]*?<\\/a>`,'i');
  const matched=cards.filter(card=>linkPattern.test(card));
  if(matched.length===0)return {pass:false,code:'MATRIX_CANONICAL_ARTIFACT_ROUTE_MISSING',officialRefId:ref,artifactCode:code,expectedUrl,normalized};
  if(matched.length!==1)return {pass:false,code:'MATRIX_ARTIFACT_CARD_AMBIGUOUS',officialRefId:ref,artifactCode:code,expectedUrl,matchedCount:matched.length,normalized};
  const card=matched[0];
  if(!card.includes(ref))return {pass:false,code:'MATRIX_REF_MISSING',officialRefId:ref,artifactCode:code,expectedUrl,card,normalized};
  if(!card.includes(code))return {pass:false,code:'MATRIX_ARTIFACT_CODE_MISSING',officialRefId:ref,artifactCode:code,expectedUrl,card,normalized};
  return {pass:true,code:null,officialRefId:ref,artifactCode:code,expectedUrl,card};
}
