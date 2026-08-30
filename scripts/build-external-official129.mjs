import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';

const root=process.cwd();
const srcDir=path.join(root,'external-viewer');
const r7Dir=path.join(root,'release','official129');
const d004Dir=path.join(root,'release','draft004');
const outDir=path.join(root,'.external-viewer-build');
const expectedProjectionSha='94590a9bbfdca699235815fb96e4c37c69156f10689e70b6c3caa74527165a53';
const expectedRelease='ER-DEMO-20260901-DRAFT-003';
const expectedD004SourceSha='bcf9098e57b3e36cc9c4819ac8a98329bdcda34c6c9bd576b4c2dc3cef225a0b';
const expectedD004FrozenSha='cdadf024ccd93128e43d474d8735b5c7e96114fbe201dd31de62d1e620d0e3b7';
const expectedD004Release='ER-DEMO-20260901-DRAFT-004';
const expectedParts=[
  'data.part00.b64','data.part01.b64','data.part02a.b64','data.part02b.b64','data.part03.b64','data.part04.b64',
  'data.part05a.b64','data.part05b.b64','data.part06.b64','data.part07a.b64','data.part07b.b64','data.part08a.b64',
  'data.part08b.b64','data.part09a.b64','data.part09b.b64','data.part10a.b64','data.part10b.b64','data.part11.b64',
  'data.part12a.b64','data.part12b.b64','data.part13.b64','data.part14.b64'
];
const sha256=(bytes)=>crypto.createHash('sha256').update(bytes).digest('hex');
const fail=(code,detail='')=>{throw new Error(detail?`${code}:${detail}`:code);};
const readUtf8=(p)=>fs.readFileSync(p,'utf8');

const baseFiles=fs.readdirSync(srcDir).sort();
if(JSON.stringify(baseFiles)!==JSON.stringify(['Code.gs','appsscript.json']))fail('EXTERNAL_BASE_PUSH_SET_INVALID',baseFiles.join(','));
const actualParts=fs.readdirSync(r7Dir).filter(x=>/^data\.part\d+(?:[a-z])?\.b64$/.test(x)).sort();
if(new Set(actualParts).size!==expectedParts.length||expectedParts.some(x=>!actualParts.includes(x)))fail('R7_DATA_PART_SET_INVALID',actualParts.join(','));
const tokens=expectedParts.map(name=>{const t=readUtf8(path.join(r7Dir,name)).trim();if(!/^[A-Za-z0-9+/=]+$/.test(t))fail('R7_DATA_B64_INVALID',name);return t;});
let raw;
try{raw=zlib.gunzipSync(Buffer.from(tokens.join(''),'base64'));}catch(error){fail('R7_PROJECTION_GUNZIP_FAIL',String(error&&error.message||error));}
const actualProjectionSha=sha256(raw);
if(actualProjectionSha!==expectedProjectionSha)fail('R7_PROJECTION_HASH_MISMATCH',actualProjectionSha);
let data;
try{data=JSON.parse(raw.toString('utf8'));}catch(error){fail('R7_PROJECTION_JSON_INVALID',String(error&&error.message||error));}
if(data.releaseId!==expectedRelease)fail('R7_RELEASE_ID_MISMATCH',String(data.releaseId));
if(!Array.isArray(data.items)||data.items.length!==129)fail('R7_ITEM_COUNT_MISMATCH',String(data.items?.length));
for(const key of ['artifactCode','officialRefId']){const vals=data.items.map(x=>String(x[key]||''));if(vals.some(x=>!x)||new Set(vals).size!==129)fail('R7_IDENTITY_UNIQUENESS_FAIL',key);}
for(let i=1;i<=19;i++){const n=data.items.filter(x=>String(x.indicator).match(/^\d+/)?.[0]===String(i)).length;if(n<1)fail('R7_INDICATOR_EMPTY',String(i));}
for(const x of data.items){
  if(!String(x.warning||'').includes('模擬資料')||!String(x.warning||'').includes('不得用於正式 TTQS 評分或官方送件'))fail('R7_SAMPLE_WARNING_MISSING',String(x.artifactCode));
  if(!/^artifacts\/pdf\//.test(String(x.offlinePdfPath||'')))fail('R7_OFFLINE_PATH_INVALID',String(x.artifactCode));
}

const decodeFrozenB64=(name)=>{try{return zlib.gunzipSync(Buffer.from(readUtf8(path.join(d004Dir,name)).trim(),'base64'));}catch(error){fail('D004_FROZEN_B64_DECODE_FAIL',name+':'+String(error&&error.message||error));}};
const d004Source=decodeFrozenB64('curated_evidence.json.gz.b64');
const d004Frozen=decodeFrozenB64('frozen_bytes_manifest.json.gz.b64');
if(sha256(d004Source)!==expectedD004SourceSha)fail('D004_SOURCE_HASH_MISMATCH',sha256(d004Source));
if(sha256(d004Frozen)!==expectedD004FrozenSha)fail('D004_FROZEN_HASH_MISMATCH',sha256(d004Frozen));
let d004Data,d004FrozenData;
try{d004Data=JSON.parse(d004Source.toString('utf8'));d004FrozenData=JSON.parse(d004Frozen.toString('utf8'));}catch(error){fail('D004_JSON_INVALID',String(error&&error.message||error));}
if(d004Data.releaseId!==expectedD004Release||d004Data.realFabrication!==0||!Array.isArray(d004Data.units)||d004Data.units.length!==28)fail('D004_SOURCE_CONTRACT_FAIL');
if(d004FrozenData.releaseId!==expectedD004Release||d004FrozenData.curatedEvidenceCount!==28||d004FrozenData.pdfCount!==28||d004FrozenData.pageCount!==50||!Array.isArray(d004FrozenData.items)||d004FrozenData.items.length!==28)fail('D004_FROZEN_CONTRACT_FAIL');
const mainIndicators=d004Data.units.filter(x=>x.subitem===null).map(x=>String(x.indicator));
if(mainIndicators.length!==19||new Set(mainIndicators).size!==19)fail('D004_MAIN_INDICATOR_COVERAGE_FAIL');
const subitems=d004Data.units.filter(x=>x.subitem!==null).map(x=>String(x.subitem)).sort();
const expectedSubitems=['12a','12b','12c','12d','12e','17a','17b','17c','17d'];
if(JSON.stringify(subitems)!==JSON.stringify(expectedSubitems))fail('D004_SUBITEM_COVERAGE_FAIL',subitems.join(','));

const runtime=readUtf8(path.join(r7Dir,'Official129Runtime.gs'));
const legacy=readUtf8(path.join(r7Dir,'Official129LegacyRegression.gs'));
const d004Runtime=readUtf8(path.join(d004Dir,'CuratedEvidenceRuntime.gs'));
const runtimeAll=runtime+'\n'+legacy+'\n'+d004Runtime;
for(const forbidden of [/Sheets\./,/SpreadsheetApp/,/DriveApp/,/UrlFetchApp/])if(forbidden.test(runtimeAll))fail('R7_RUNTIME_GOOGLE_DATA_API_FORBIDDEN',String(forbidden));
const base=readUtf8(path.join(srcDir,'Code.gs'));
const appsscript=readUtf8(path.join(srcDir,'appsscript.json'));
const projectionGzipB64=zlib.gzipSync(raw,{level:9,mtime:0}).toString('base64');
const d004GzipB64=zlib.gzipSync(d004Source,{level:9,mtime:0}).toString('base64');
const d004FrozenGzipB64=zlib.gzipSync(d004Frozen,{level:9,mtime:0}).toString('base64');
const code=base+'\n\n/* build-time injected R7 frozen projection; source sha256='+expectedProjectionSha+' */\nvar TTQS_R7_DATA_GZIP_B64_='+JSON.stringify(projectionGzipB64)+';\n'+runtime+'\n'+legacy+'\n\n/* build-time injected DRAFT-004 curated human evidence; source sha256='+expectedD004SourceSha+' */\nvar TTQS_D004_DATA_GZIP_B64_='+JSON.stringify(d004GzipB64)+';\nvar TTQS_D004_FROZEN_GZIP_B64_='+JSON.stringify(d004FrozenGzipB64)+';\n'+d004Runtime+'\n';
fs.rmSync(outDir,{recursive:true,force:true});fs.mkdirSync(outDir,{recursive:true});
fs.writeFileSync(path.join(outDir,'Code.gs'),code);fs.writeFileSync(path.join(outDir,'appsscript.json'),appsscript);
process.stdout.write(`R7_EXTERNAL_BUILD_PASS items=129 parts=${expectedParts.length} projectionSha256=${expectedProjectionSha} d004Units=28 d004SourceSha256=${expectedD004SourceSha} buildCodeSha256=${sha256(Buffer.from(code,'utf8'))} buildBytes=${Buffer.byteLength(code)}\n`);
