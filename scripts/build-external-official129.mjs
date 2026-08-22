import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';

const root=process.cwd();
const srcDir=path.join(root,'external-viewer');
const r7Dir=path.join(root,'release','official129');
const outDir=path.join(root,'.external-viewer-build');
const expectedProjectionSha='7567530e1f72ef5c8ec491aa38936bf7884ef258943df5f01e0fce08c0c3f2de';
const expectedRelease='ER-DEMO-20260901-DRAFT-002';

function fail(code,detail=''){throw new Error(detail?`${code}:${detail}`:code);}
function sha256(buf){return crypto.createHash('sha256').update(buf).digest('hex');}
function readUtf8(p){return fs.readFileSync(p,'utf8');}
function partKey(name){
  const m=String(name).match(/^data\.part(\d+)([a-z]?)\.b64$/);
  if(!m)fail('R7_DATA_PART_NAME_INVALID',String(name));
  return {number:Number(m[1]),suffix:m[2]||''};
}
function compareParts(a,b){
  const ka=partKey(a),kb=partKey(b);
  if(ka.number!==kb.number)return ka.number-kb.number;
  if(ka.suffix<kb.suffix)return -1;
  if(ka.suffix>kb.suffix)return 1;
  return 0;
}

const baseFiles=fs.readdirSync(srcDir).sort();
if(JSON.stringify(baseFiles)!==JSON.stringify(['Code.gs','appsscript.json']))fail('EXTERNAL_BASE_PUSH_SET_INVALID',baseFiles.join(','));
const parts=fs.readdirSync(r7Dir).filter(x=>/^data\.part\d+(?:[a-z])?\.b64$/.test(x)).sort(compareParts);
if(parts.length<2)fail('R7_DATA_PARTS_MISSING');
const b64=parts.map(f=>readUtf8(path.join(r7Dir,f)).trim()).join('');
if(!/^[A-Za-z0-9+/=]+$/.test(b64))fail('R7_DATA_B64_INVALID');
let raw;
try{raw=zlib.gunzipSync(Buffer.from(b64,'base64'));}catch(e){fail('R7_DATA_GZIP_INVALID',e.message);}
if(sha256(raw)!==expectedProjectionSha)fail('R7_PROJECTION_HASH_MISMATCH',sha256(raw));
let data;
try{data=JSON.parse(raw.toString('utf8'));}catch(e){fail('R7_PROJECTION_JSON_INVALID',e.message);}
if(data.releaseId!==expectedRelease)fail('R7_RELEASE_ID_MISMATCH',String(data.releaseId));
if(!Array.isArray(data.items)||data.items.length!==129)fail('R7_ITEM_COUNT_MISMATCH',String(data.items?.length));
for(const key of ['artifactCode','officialRefId']){
  const vals=data.items.map(x=>String(x[key]||''));
  if(vals.some(x=>!x)||new Set(vals).size!==129)fail('R7_IDENTITY_UNIQUENESS_FAIL',key);
}
for(let i=1;i<=19;i++){
  const n=data.items.filter(x=>String(x.indicator).match(/^\d+/)?.[0]===String(i)).length;
  if(n<1)fail('R7_INDICATOR_EMPTY',String(i));
}
const runtime=readUtf8(path.join(r7Dir,'Official129Runtime.gs'));
const legacy=readUtf8(path.join(r7Dir,'Official129LegacyRegression.gs'));
const runtimeAll=runtime+'\n'+legacy;
for(const forbidden of [/Sheets\./,/SpreadsheetApp/,/DriveApp/,/UrlFetchApp/])if(forbidden.test(runtimeAll))fail('R7_RUNTIME_GOOGLE_DATA_API_FORBIDDEN',String(forbidden));
const base=readUtf8(path.join(srcDir,'Code.gs'));
const manifest=readUtf8(path.join(srcDir,'appsscript.json'));
const code=base+'\n\n/* build-time injected R7 frozen projection; source sha256='+expectedProjectionSha+' */\nvar TTQS_R7_DATA_GZIP_B64_='+JSON.stringify(b64)+';\n'+runtimeAll+'\n';
fs.rmSync(outDir,{recursive:true,force:true});fs.mkdirSync(outDir,{recursive:true});
fs.writeFileSync(path.join(outDir,'Code.gs'),code);
fs.writeFileSync(path.join(outDir,'appsscript.json'),manifest);
const buildSha=sha256(Buffer.from(code,'utf8'));
const summary={releaseId:expectedRelease,itemCount:129,partCount:parts.length,projectionSha256:expectedProjectionSha,buildCodeSha256:buildSha,buildBytes:Buffer.byteLength(code),result:'PASS'};
process.stdout.write(`R7_EXTERNAL_BUILD_PASS items=129 parts=${parts.length} projectionSha256=${expectedProjectionSha} buildCodeSha256=${buildSha} buildBytes=${summary.buildBytes}\n`);
