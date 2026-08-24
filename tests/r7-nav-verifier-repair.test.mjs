import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import {normalizeAppsScriptHtmlServiceWrapper,R7_REQUIRED_PRODUCT_MARKERS,REQUIRED_PRODUCT_MARKERS} from '../scripts/external-blackbox-classifier.mjs';
import {normalizeHtmlServiceSerializedAttributes,verifyHomeIndicatorRoute,verifyEvidenceMatrixLayer} from '../scripts/r7-nav-verifier.mjs';

const fixtureDir=path.join('tests','fixtures','r7-nav-verifier-repair','provider-v11-source-53c6f5-20260824');
const fixture=JSON.parse(fs.readFileSync(path.join(fixtureDir,'fixture.json'),'utf8'));
const matrixProvenance=JSON.parse(fs.readFileSync(path.join(fixtureDir,'matrix-capture-provenance.json'),'utf8'));
const rawB64=Array.from({length:7},(_,index)=>fs.readFileSync(path.join(fixtureDir,`home.raw.b64.part${String(index).padStart(2,'0')}`),'utf8')).join('');
const rawBuffer=Buffer.from(rawB64,'base64');
const raw=rawBuffer.toString('utf8');
const browserHome=fs.readFileSync(path.join(fixtureDir,'browser.content.body.outerHTML.html'),'utf8');
const browserCard=fs.readFileSync(path.join(fixtureDir,'indicator1.card.outerHTML.html'),'utf8');
const browserLink=fs.readFileSync(path.join(fixtureDir,'indicator1.link.outerHTML.html'),'utf8').trim();
const browserMatrix=()=>fs.readFileSync(path.join(fixtureDir,'browser.matrix.body.outerHTML.html'),'utf8');
const canonical=fixture.source.canonicalUrl;
const sha256=value=>crypto.createHash('sha256').update(value).digest('hex');

function removeOnce(source,needle){
  const index=source.indexOf(needle);
  assert.notEqual(index,-1,`actual fixture missing needle: ${needle}`);
  return source.slice(0,index)+source.slice(index+needle.length);
}

function removeAttributeOnce(source,name){
  const pattern=new RegExp(`\\s${name}="[^"]*"`);
  assert.match(source,pattern);
  return source.replace(pattern,'');
}

// Exact historical homepage condition from the pre-repair exhaustive live verifier:
// normalize the HtmlService wrapper, then require data-matrix-indicator="N" on HOME.
// The actual TEST homepage uses data-indicator on the card, so this old condition must
// reproduce HOME_INDICATOR_LINK_MISSING:N on the same real V-01 bytes.
function historicalOldHomeVerifier(input,{indicator}){
  const id=String(indicator);
  const normalized=normalizeAppsScriptHtmlServiceWrapper(input)
    .replace(/\\x3[cC]/g,'<').replace(/\\u003[cC]/g,'<')
    .replace(/\\x3[eE]/g,'>').replace(/\\u003[eE]/g,'>')
    .replace(/\\x26/g,'&').replace(/\\u0026/g,'&')
    .replace(/\\x27/g,"'").replace(/\\u0027/g,"'")
    .replace(/\\x22/g,'"').replace(/\\u0022/g,'"');
  return normalized.includes(`data-matrix-indicator="${id}"`)
    ? {pass:true,code:null}
    : {pass:false,code:`HOME_INDICATOR_LINK_MISSING:${id}`};
}

test('V-01/V-02 fixture is actual anonymous TEST provider evidence, not a handwritten mock',()=>{
  assert.equal(fixture.schema,'TTQS_R7_NAV_VERIFIER_ACTUAL_FIXTURE_V1');
  assert.equal(fixture.source.kind,'ACTUAL_TEST_PROVIDER');
  assert.equal(fixture.source.anonymousGet,true);
  assert.equal(fixture.source.providerVersion,11);
  assert.equal(fixture.source.providerSourceSha,'53c6f5f05886bd3e5e48e682043dec3b492af3ed');
  assert.match(fixture.capturedAt,/^2026-08-23T22:/);
  assert.equal(rawBuffer.length,fixture.rawHtmlService.bytes);
  assert.equal(sha256(rawBuffer),fixture.rawHtmlService.sha256);
  assert.equal(fixture.browserDom.indicator1.linkGetAttributeDataIndicator,null);
  assert.equal(fixture.browserDom.indicator1.cardGetAttributeDataIndicator,'1');
  assert.equal(fixture.browserDom.click.actualPageUrl,`${canonical}?indicator=1`);
  assert.equal(fixture.browserDom.click.windowTopEqualsSelfAfter,true);
  assert.equal(fixture.browserDom.click.scriptGoogleIframeCountAfter,0);
});

test('V-02 Matrix fixture is exact bytes from the second actual Playwright capture',()=>{
  const matrix=browserMatrix();
  assert.equal(matrixProvenance.schema,'TTQS_R7_NAV_MATRIX_ACTUAL_FIXTURE_PROVENANCE_V1');
  assert.equal(matrixProvenance.source,'ACTUAL_TEST_PROVIDER_PLAYWRIGHT');
  assert.equal(matrixProvenance.providerVersion,11);
  assert.equal(matrixProvenance.providerSourceSha,fixture.source.providerSourceSha);
  assert.equal(matrixProvenance.canonicalUrl,canonical);
  assert.equal(matrixProvenance.mutation,'NONE');
  assert.equal(Buffer.byteLength(matrix),matrixProvenance.bytes);
  assert.equal(sha256(matrix),matrixProvenance.sha256);
});

test('V-05 same actual raw fixture fails historical verifier and passes repaired verifier',()=>{
  const oldResult=historicalOldHomeVerifier(raw,{indicator:1});
  assert.equal(oldResult.pass,false);
  assert.equal(oldResult.code,'HOME_INDICATOR_LINK_MISSING:1');

  const normalized=normalizeHtmlServiceSerializedAttributes(raw);
  assert.equal(normalized.includes('data-indicator="1"'),true);
  const repaired=verifyHomeIndicatorRoute(raw,{indicator:1,canonical});
  assert.equal(repaired.pass,true,repaired.code||'unexpected repaired-verifier failure');
});

test('V-03 repaired home verifier reads the same actual serialized provider link',()=>{
  const result=verifyHomeIndicatorRoute(raw,{indicator:1,canonical});
  assert.equal(result.pass,true,result.code||'unexpected failure');
  assert.equal(result.actualUrl,`${canonical}?indicator=1`);
  assert.equal(result.target,'_top');
  assert.equal(result.linkText,'查看文件與證據');
});

test('V-03 repaired home verifier also reads the real Playwright DOM representation',()=>{
  const result=verifyHomeIndicatorRoute(browserHome,{indicator:1,canonical});
  assert.equal(result.pass,true,result.code||'unexpected failure');
  assert.equal(result.actualUrl,fixture.browserDom.indicator1.hrefAttribute);
  assert.equal(result.target,fixture.browserDom.indicator1.targetAttribute);
});

test('V-05 fail closed: actual card missing data-indicator',()=>{
  const broken=browserHome.replace(' data-indicator="1"','');
  assert.notEqual(broken,browserHome);
  const result=verifyHomeIndicatorRoute(broken,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'HOME_INDICATOR_CARD_MISSING');
});

test('V-05 fail closed: indicator card missing 查看文件與證據 link',()=>{
  const broken=removeOnce(browserCard,browserLink);
  const result=verifyHomeIndicatorRoute(broken,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'HOME_INDICATOR_LINK_MISSING');
});

test('V-05 fail closed: actual DOM without href is not treated as escaping',()=>{
  const broken=removeAttributeOnce(browserCard,'href');
  const result=verifyHomeIndicatorRoute(broken,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'HOME_INDICATOR_HREF_MISSING');
});

test('V-05 fail closed: 查看文件與證據 href must be exact canonical indicator route',()=>{
  const broken=browserCard.replace(`${canonical}?indicator=1`,'https://example.invalid/not-canonical');
  assert.notEqual(broken,browserCard);
  const result=verifyHomeIndicatorRoute(broken,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'HOME_INDICATOR_CANONICAL_URL_FAIL');
});

test('V-05 fail closed: canonical href with non-top target is rejected',()=>{
  const broken=browserCard.replace('target="_top"','target="_self"');
  assert.notEqual(broken,browserCard);
  const result=verifyHomeIndicatorRoute(broken,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'HOME_INDICATOR_TARGET_FAIL');
});

test('V-06 homepage layer requires 查看文件與證據 but never requires second-layer 開啟文件',()=>{
  assert.equal(browserHome.includes('查看文件與證據'),true);
  assert.equal(browserHome.includes('開啟文件'),false);
  assert.equal(verifyHomeIndicatorRoute(browserHome,{indicator:1,canonical}).pass,true);
  assert.equal(R7_REQUIRED_PRODUCT_MARKERS.includes('開啟文件'),false);
  assert.equal(R7_REQUIRED_PRODUCT_MARKERS.includes('data-indicator='),true);
});

test('V-07 actual Playwright Matrix DOM satisfies every-card title, open control and canonical artifact route',()=>{
  const matrix=browserMatrix();
  const result=verifyEvidenceMatrixLayer(matrix,{indicator:1,canonical});
  assert.equal(result.pass,true,result.code||'unexpected failure');
  assert.equal(result.documentCardCount,6);
  assert.equal(result.chineseDocumentCardCount,6);
  assert.equal(result.everyCardHasChineseTitle,true);
  assert.equal(result.everyCardHasOpenDocument,true);
  assert.equal(result.everyCardHasCanonicalArtifactRoute,true);
  assert.ok(result.openDocumentCount>=result.documentCardCount);
  assert.ok(result.firstCanonicalArtifactUrl.startsWith(`${canonical}?artifact=`));
});

test('V-07 Matrix verifier independently fail-closes missing second-layer requirements',()=>{
  const matrix=browserMatrix();
  const withoutAnyOpenDocument=matrix.replaceAll('開啟文件','');
  assert.notEqual(withoutAnyOpenDocument,matrix);
  let result=verifyEvidenceMatrixLayer(withoutAnyOpenDocument,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'MATRIX_OPEN_DOCUMENT_MISSING');

  for(const [needle,code] of [
    ['TEST／SAMPLE／CONTROL','MATRIX_SIMULATION_WARNING_MISSING'],
    ['指標 1｜查看文件與證據','MATRIX_CHINESE_HEADING_MISSING']
  ]){
    result=verifyEvidenceMatrixLayer(removeOnce(matrix,needle),{indicator:1,canonical});
    assert.equal(result.pass,false,needle);
    assert.equal(result.code,code,needle);
  }

  const withoutFirstTitle=matrix.replace('<h3>中長程業務發展規劃與策略地圖</h3>','');
  assert.notEqual(withoutFirstTitle,matrix);
  result=verifyEvidenceMatrixLayer(withoutFirstTitle,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'MATRIX_DOCUMENT_TITLE_MISSING');
  assert.equal(result.cardIndex,1);

  const brokenHref=matrix.replace(`${canonical}?artifact=DOC-129-01`,'https://example.invalid/not-canonical');
  assert.notEqual(brokenHref,matrix);
  result=verifyEvidenceMatrixLayer(brokenHref,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'MATRIX_CANONICAL_ARTIFACT_ROUTE_MISSING');
  assert.equal(result.cardIndex,1);
});

test('V-04 R2 acceptance marker contract remains exactly 19 required markers',()=>{
  assert.equal(REQUIRED_PRODUCT_MARKERS.length,19);
  for(const marker of ['查看文件與證據','19 指標佐證與來源下鑽','不在執行期呼叫 Google Sheets／Drive API','本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL']) assert.ok(REQUIRED_PRODUCT_MARKERS.includes(marker),marker);
});
