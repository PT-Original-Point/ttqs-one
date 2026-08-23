import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import {R7_REQUIRED_PRODUCT_MARKERS,REQUIRED_PRODUCT_MARKERS} from '../scripts/external-blackbox-classifier.mjs';
import {normalizeR7NavigationHtml,verifyHomeIndicatorRoute,verifyEvidenceMatrixLayer} from '../scripts/r7-nav-verifier.mjs';

const fixtureDir=path.join('tests','fixtures','r7-nav-verifier-repair','provider-v11-source-53c6f5-20260824');
const fixture=JSON.parse(fs.readFileSync(path.join(fixtureDir,'fixture.json'),'utf8'));
const raw=fs.readFileSync(path.join(fixtureDir,'home.raw.html'),'utf8');
const browserHome=fs.readFileSync(path.join(fixtureDir,'browser.content.body.outerHTML.html'),'utf8');
const browserMatrix=()=>fs.readFileSync(path.join(fixtureDir,'browser.matrix.body.outerHTML.html'),'utf8');
const canonical=fixture.source.canonicalUrl;

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

test('V-01/V-02 fixture is actual anonymous TEST provider evidence, not a handwritten mock',()=>{
  assert.equal(fixture.schema,'TTQS_R7_NAV_VERIFIER_ACTUAL_FIXTURE_V1');
  assert.equal(fixture.source.kind,'ACTUAL_TEST_PROVIDER');
  assert.equal(fixture.source.anonymousGet,true);
  assert.equal(fixture.source.providerVersion,11);
  assert.equal(fixture.source.providerSourceSha,'53c6f5f05886bd3e5e48e682043dec3b492af3ed');
  assert.match(fixture.capturedAt,/^2026-08-23T22:/);
  assert.equal(fixture.browserDom.indicator1.linkGetAttributeDataIndicator,null);
  assert.equal(fixture.browserDom.indicator1.cardGetAttributeDataIndicator,'1');
  assert.equal(fixture.browserDom.click.actualPageUrl,`${canonical}?indicator=1`);
  assert.equal(fixture.browserDom.click.windowTopEqualsSelfAfter,true);
  assert.equal(fixture.browserDom.click.scriptGoogleIframeCountAfter,0);
});

test('V-05 actual raw fixture reproduces the old HOME_INDICATOR_LINK_MISSING false negative',()=>{
  const normalized=normalizeR7NavigationHtml(raw);
  assert.equal(normalized.includes('data-matrix-indicator="1"'),false,'old homepage verifier condition must remain reproducible as false');
  assert.equal(normalized.includes('data-indicator="1"'),true);
  assert.equal(normalized.includes(`${canonical}?indicator=1`),true);
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

test('V-05 actual DOM without card data-indicator remains fail-closed',()=>{
  const broken=browserHome.replace(' data-indicator="1"','');
  assert.notEqual(broken,browserHome);
  const result=verifyHomeIndicatorRoute(broken,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'HOME_INDICATOR_CARD_MISSING');
});

test('V-05 actual DOM without href remains fail-closed instead of being treated as escaping',()=>{
  const card=fs.readFileSync(path.join(fixtureDir,'indicator1.card.outerHTML.html'),'utf8');
  const broken=removeAttributeOnce(card,'href');
  const result=verifyHomeIndicatorRoute(broken,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'HOME_INDICATOR_HREF_MISSING');
});

test('V-06 homepage layer requires 查看文件與證據 but never requires second-layer 開啟文件',()=>{
  assert.equal(browserHome.includes('查看文件與證據'),true);
  assert.equal(browserHome.includes('開啟文件'),false);
  assert.equal(verifyHomeIndicatorRoute(browserHome,{indicator:1,canonical}).pass,true);
  assert.equal(R7_REQUIRED_PRODUCT_MARKERS.includes('開啟文件'),false);
  assert.equal(R7_REQUIRED_PRODUCT_MARKERS.includes('data-indicator='),true);
});

test('V-07 actual Playwright Matrix DOM satisfies Chinese card, warning, open control and canonical artifact route',()=>{
  const matrix=browserMatrix();
  const result=verifyEvidenceMatrixLayer(matrix,{indicator:1,canonical});
  assert.equal(result.pass,true,result.code||'unexpected failure');
  assert.ok(result.documentCardCount>=1);
  assert.ok(result.chineseDocumentCardCount>=1);
  assert.ok(result.openDocumentCount>=1);
  assert.match(result.firstCanonicalArtifactUrl,new RegExp('^'+canonical.replace(/[.*+?^${}()|[\\]\\]/g,'\\$&')+'\\?artifact='));
});

test('V-07 Matrix verifier independently fail-closes missing second-layer requirements',()=>{
  const matrix=browserMatrix();
  const cases=[
    ['開啟文件','MATRIX_OPEN_DOCUMENT_MISSING'],
    ['TEST／SAMPLE／CONTROL','MATRIX_SIMULATION_WARNING_MISSING'],
    ['指標 1｜查看文件與證據','MATRIX_CHINESE_HEADING_MISSING']
  ];
  for(const [needle,code] of cases){
    const result=verifyEvidenceMatrixLayer(removeOnce(matrix,needle),{indicator:1,canonical});
    assert.equal(result.pass,false,needle);
    assert.equal(result.code,code,needle);
  }
  const brokenHref=matrix.replace(`${canonical}?artifact=DOC-129-01`,'https://example.invalid/not-canonical');
  assert.notEqual(brokenHref,matrix);
  const result=verifyEvidenceMatrixLayer(brokenHref,{indicator:1,canonical});
  assert.equal(result.pass,false);
  assert.equal(result.code,'MATRIX_CANONICAL_ARTIFACT_ROUTE_MISSING');
});

test('V-04 R2 acceptance marker contract remains exactly 19 required markers',()=>{
  assert.equal(REQUIRED_PRODUCT_MARKERS.length,19);
  for(const marker of ['查看文件與證據','19 指標佐證與來源下鑽','不在執行期呼叫 Google Sheets／Drive API','本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL']) assert.ok(REQUIRED_PRODUCT_MARKERS.includes(marker),marker);
});
