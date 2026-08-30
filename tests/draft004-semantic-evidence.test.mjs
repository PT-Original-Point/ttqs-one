import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import zlib from 'node:zlib';

const read=(p)=>fs.readFileSync(p,'utf8');
const sha=(b)=>crypto.createHash('sha256').update(b).digest('hex');
const decode=(p)=>zlib.gunzipSync(Buffer.from(read(p).trim(),'base64'));
const dataBytes=decode('release/draft004/curated_evidence.json.gz.b64');
const frozenBytes=decode('release/draft004/frozen_bytes_manifest.json.gz.b64');
const data=JSON.parse(dataBytes);
const frozen=JSON.parse(frozenBytes);
const runtime=read('release/draft004/CuratedEvidenceRuntime.gs');
const build=read('scripts/build-external-official129.mjs');

const forbidden=['TruthDataset','strategic_theme_','portal_static_projection_source','MANIFEST.sha256','Frozen DEMO build'];
const bodyText=(u)=>[u.title,...(u.blocks||[]).flatMap(b=>[b.heading||'',b.text||'',...(b.headers||[]),...(b.rows||[]).flat()])].join('\n');
const norm=(s)=>String(s||'').replace(/\s+/g,'');

test('DRAFT-004 source identity and curated coverage are exact',()=>{
  assert.equal(data.schema,'TTQS_DRAFT004_CURATED_EVIDENCE_V1');
  assert.equal(data.releaseId,'ER-DEMO-20260901-DRAFT-004');
  assert.equal(data.realFabrication,0);
  assert.equal(data.units.length,28);
  assert.equal(sha(dataBytes),'bcf9098e57b3e36cc9c4819ac8a98329bdcda34c6c9bd576b4c2dc3cef225a0b');
  assert.equal(sha(frozenBytes),'cdadf024ccd93128e43d474d8735b5c7e96114fbe201dd31de62d1e620d0e3b7');
  assert.equal(frozen.curatedEvidenceCount,28);
  assert.equal(frozen.pdfCount,28);
  assert.equal(frozen.pageCount,50);
  const mains=data.units.filter(x=>x.subitem===null);
  assert.equal(mains.length,19);
  assert.deepEqual(mains.map(x=>String(x.indicator)).sort((a,b)=>Number(a)-Number(b)),Array.from({length:19},(_,i)=>String(i+1)));
  assert.deepEqual(data.units.filter(x=>x.subitem!==null).map(x=>x.subitem).sort(),['12a','12b','12c','12d','12e','17a','17b','17c','17d']);
});

test('every consultant-visible unit is a semantic business document, not an engineering placeholder',()=>{
  for(const u of data.units){
    const text=bodyText(u);
    assert.ok(String(u.warning||'').includes('SAMPLE'),`${u.id}: SAMPLE warning`);
    assert.ok(String(u.warning||'').includes('不得用於正式 TTQS 評分或官方送件'),`${u.id}: non-formal warning`);
    assert.ok(Array.isArray(u.requiredTerms)&&u.requiredTerms.length>=3,`${u.id}: required terms`);
    for(const term of u.requiredTerms)assert.ok(norm(text).includes(norm(term)),`${u.id}: missing semantic term ${term}`);
    for(const token of forbidden)assert.equal(text.includes(token),false,`${u.id}: forbidden engineering token ${token}`);
    assert.equal(text.split(/\r?\n/).filter(line=>/^\s*[A-Za-z_][A-Za-z0-9_.-]*\s*=/.test(line)).length,0,`${u.id}: key=value dump`);
    assert.ok((u.blocks||[]).filter(b=>b.type==='section').length>=2,`${u.id}: document sections`);
    assert.ok((u.blocks||[]).some(b=>b.type==='table'),`${u.id}: business table`);
  }
});

test('Indicator 1 and Indicator 15 have the required human document structures',()=>{
  const i1=data.units.find(x=>x.id==='I01'),i15=data.units.find(x=>x.id==='I15');
  for(const term of ['組織','環境','SWOT','三年','策略目標','KPI','Roadmap','責任','風險','PDCA'])assert.ok(norm(bodyText(i1)).includes(norm(term)),`I01 missing ${term}`);
  for(const term of ['會議名稱','日期','主席','紀錄','與會角色','議程','討論','決議','責任人','完成期限','前次','追蹤'])assert.ok(norm(bodyText(i15)).includes(norm(term)),`I15 missing ${term}`);
});

test('frozen PDF metadata matches all 28 curated identities and online/offline release identity',()=>{
  assert.equal(frozen.releaseId,data.releaseId);
  assert.equal(frozen.semanticContract,'28/28_PASS');
  assert.equal(frozen.visualQa,'50/50_PAGE_PASS');
  const ids=new Set(data.units.map(x=>x.id));
  assert.deepEqual(new Set(frozen.items.map(x=>x.id)),ids);
  for(const item of frozen.items){assert.match(item.pdfSha256,/^[0-9a-f]{64}$/);assert.match(item.docxSha256,/^[0-9a-f]{64}$/);assert.ok(item.pages>=1);}
});

test('consultant runtime defaults to DRAFT-004 and confines technical metadata to admin details',()=>{
  assert.match(runtime,/TTQS_D004_RELEASE_ID_='ER-DEMO-20260901-DRAFT-004'/);
  assert.match(runtime,/技術細節（管理員用）/);
  assert.match(runtime,/data-artifact-id=/);
  assert.match(runtime,/data-matrix-indicator=/);
  assert.match(runtime,/legacy129/);
  assert.match(runtime,/if\(p\.artifact\).*ttqsD004ArtifactHtml_/s);
  assert.match(runtime,/if\(p\.indicator\).*ttqsD004MatrixHtml_/s);
  assert.match(runtime,/return HtmlService\.createHtmlOutput\(ttqsD004HomeHtml_\(\)\)/);
  for(const token of forbidden)assert.equal(runtime.includes(token),false,`runtime primary code contains forbidden token ${token}`);
  assert.equal(/SpreadsheetApp|DriveApp|UrlFetchApp|Sheets\./.test(runtime),false);
});

test('build preserves 129 regression but injects DRAFT-004 last',()=>{
  assert.match(build,/items\.length!==129/);
  assert.match(build,/d004Data\.units\.length!==28/);
  const legacy=build.indexOf("readUtf8(path.join(r7Dir,'Official129LegacyRegression.gs'))");
  const curated=build.indexOf("readUtf8(path.join(d004Dir,'CuratedEvidenceRuntime.gs'))");
  assert.ok(legacy>=0&&curated>legacy);
  const codeLine=build.indexOf("var TTQS_D004_DATA_GZIP_B64_");
  assert.ok(codeLine>=0);
  assert.match(build,/d004Runtime\+'\\n';/);
});
