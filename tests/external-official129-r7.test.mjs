import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {execFileSync} from 'node:child_process';

const root=process.cwd();
const r7Dir=path.join(root,'release','official129');
const expectedProjectionSha='7567530e1f72ef5c8ec491aa38936bf7884ef258943df5f01e0fce08c0c3f2de';
const expectedRelease='ER-DEMO-20260901-DRAFT-002';
const canonical='https://script.google.com/macros/s/AKfycbznbXi-0XWNV68E-vGU9CiAE6ElXGIlDmy27EePXMdGpRaorURzKZq0dDgsNBaaZOLh/exec';
const sha256=(buf)=>crypto.createHash('sha256').update(buf).digest('hex');

function compareParts(a,b){
  const ma=String(a).match(/^data\.part(\d+)([a-z]?)\.b64$/);
  const mb=String(b).match(/^data\.part(\d+)([a-z]?)\.b64$/);
  assert.ok(ma&&mb,'projection part names must be canonical');
  const na=Number(ma[1]),nb=Number(mb[1]);
  if(na!==nb)return na-nb;
  return ma[2]<mb[2]?-1:ma[2]>mb[2]?1:0;
}

function projection(){
  const parts=fs.readdirSync(r7Dir).filter(x=>/^data\.part\d+(?:[a-z])?\.b64$/.test(x)).sort(compareParts);
  assert.ok(parts.length>=15,'projection is intentionally split and build-time assembled');
  const b64=parts.map(f=>fs.readFileSync(path.join(r7Dir,f),'utf8').trim()).join('');
  assert.match(b64,/^[A-Za-z0-9+/=]+$/);
  const raw=zlib.gunzipSync(Buffer.from(b64,'base64'));
  assert.equal(sha256(raw),expectedProjectionSha);
  return {parts,raw,data:JSON.parse(raw.toString('utf8'))};
}

test('R7 static projection is exact, immutable and contains 129 unique official-reference artifacts',()=>{
  const {data}=projection();
  assert.equal(data.releaseId,expectedRelease);
  assert.equal(data.items.length,129);
  assert.equal(new Set(data.items.map(x=>x.artifactCode)).size,129);
  assert.equal(new Set(data.items.map(x=>x.officialRefId)).size,129);
  assert.deepEqual(data.items.map(x=>x.seq),Array.from({length:129},(_,i)=>i+1));
});

test('R7 all 19 base indicators have non-empty detailed coverage and sum to 129',()=>{
  const {data}=projection();
  let total=0;
  for(let i=1;i<=19;i++){
    const xs=data.items.filter(x=>String(x.indicator).match(/^\d+/)?.[0]===String(i));
    assert.ok(xs.length>0,`indicator ${i} must have detailed evidence rows`);
    total+=xs.length;
  }
  assert.equal(total,129);
});

test('R7 each frozen artifact has complete text, page-warning QA, hashes and offline route',()=>{
  const {data}=projection();
  for(const x of data.items){
    assert.match(x.artifactCode,/^DOC-129-\d{3}$/);
    assert.match(x.officialRefId,/^OEV-/);
    assert.ok(String(x.officialText).length>=2,x.artifactCode);
    assert.ok(String(x.text).length>=1000,`${x.artifactCode} frozen text too short`);
    assert.ok(Number(x.pdfPages)>0,x.artifactCode);
    assert.equal(x.warningAllPages,true,x.artifactCode);
    for(const key of ['pdfSha256','pdfTextSha256','docxSha256','chartSha256'])assert.match(String(x[key]),/^[0-9a-f]{64}$/,`${x.artifactCode}:${key}`);
    assert.equal(x.offlinePdfPath,`pdf/${x.pdfFilename}`);
  }
});

test('R7 runtime exposes evaluator navigation, simulation boundary, 19/26/129 governance and legacy R3 control route',()=>{
  const src=fs.readFileSync(path.join(r7Dir,'Official129Runtime.gs'),'utf8');
  for(const marker of ['TEST／SAMPLE／CONTROL','不得用於正式 TTQS 評分','129','19','26','Evidence Matrix','開啟 FrozenArtifact','FA-DEMO-002','runtime 不查詢 live Drive'])assert.ok(src.includes(marker),marker);
  assert.match(src,/ttqsR7AbsUrl_\('indicator='\+/);
  assert.match(src,/ttqsR7AbsUrl_\('artifact='\+/);
  assert.match(src,/data-friendly-error/);
});

test('R7 runtime cannot query live Drive or Sheets and cannot invoke REAL/PROD submission paths',()=>{
  const src=fs.readFileSync(path.join(r7Dir,'Official129Runtime.gs'),'utf8');
  for(const forbidden of ['SpreadsheetApp','DriveApp','UrlFetchApp','Sheets.','FORMAL_SCORING','OFFICIAL_SUBMISSION','REAL_WRITE','PROD_ENABLE'])assert.equal(src.includes(forbidden),false,forbidden);
});

test('R7 build assembles exact two-file Apps Script push set from frozen static projection',()=>{
  const output=execFileSync(process.execPath,['scripts/build-external-official129.mjs'],{cwd:root,encoding:'utf8'});
  assert.match(output,/R7_EXTERNAL_BUILD_PASS items=129/);
  const outDir=path.join(root,'.external-viewer-build');
  assert.deepEqual(fs.readdirSync(outDir).sort(),['Code.gs','appsscript.json']);
  const code=fs.readFileSync(path.join(outDir,'Code.gs'),'utf8');
  assert.ok(code.includes(expectedProjectionSha));
  assert.ok(code.includes(expectedRelease));
  assert.ok(code.includes('ttqsR7HomeHtml_'));
  assert.ok(code.includes('var TTQS_R7_DATA_GZIP_B64_='));
});

test('R7 built Apps Script remains static-data-only while preserving canonical absolute navigation',()=>{
  execFileSync(process.execPath,['scripts/build-external-official129.mjs'],{cwd:root,encoding:'utf8'});
  const code=fs.readFileSync(path.join(root,'.external-viewer-build','Code.gs'),'utf8');
  for(const forbidden of ['SpreadsheetApp','DriveApp','UrlFetchApp','Sheets.'])assert.equal(code.includes(forbidden),false,forbidden);
  assert.ok(code.includes(canonical));
  assert.match(code,/data-matrix-indicator/);
  assert.match(code,/data-frozen-artifact-id/);
  assert.match(code,/data-artifact-id/);
  assert.match(code,/data-official-ref-id/);
});

test('R7 route contract fails closed for unknown indicator/artifact and never treats HTTP 200 shell as proof',()=>{
  const src=fs.readFileSync(path.join(r7Dir,'Official129Runtime.gs'),'utf8');
  assert.match(src,/if\(!items\.length\)return ttqsR7ErrorHtml_/);
  assert.match(src,/if\(!x\)return ttqsR7ErrorHtml_/);
  assert.ok(src.includes('此頁不會以空白或 HTTP 200 冒充有效證據'));
  assert.ok(src.includes('data-friendly-error="true"'));
});
