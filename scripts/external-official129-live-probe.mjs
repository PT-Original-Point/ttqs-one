import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {normalizeAppsScriptHtmlServiceWrapper} from './external-blackbox-classifier.mjs';

const root=process.cwd();
const r7Dir=path.join(root,'release','official129');
const expectedRelease='ER-DEMO-20260901-DRAFT-002';
const expectedProjectionSha='7567530e1f72ef5c8ec491aa38936bf7884ef258943df5f01e0fce08c0c3f2de';
const expectedManifestSha='2673e9abd5942eb3b3c27a5a54e05b1f73339a902035787344b65d2027e052ee';
const expectedOfflineZipSha='5026066430bd65c57f4c2adb59cef6e4bad70a6fcda298f89d864938dba0c676';
const canonical=String(process.env.EXTERNAL_WEBAPP_URL||'').replace(/\/+$/,'');
if(!/^https:\/\/script\.google\.com\/macros\/s\/[A-Za-z0-9_-]+\/exec$/.test(canonical))throw new Error('OFFICIAL129_CANONICAL_EXEC_URL_INVALID');
const sha256=b=>crypto.createHash('sha256').update(b).digest('hex');

function projection(){
  const parts=fs.readdirSync(r7Dir).filter(x=>/^data\.part\d+(?:[a-z])?\.b64$/.test(x)).sort();
  const b64=parts.map(f=>fs.readFileSync(path.join(r7Dir,f),'utf8').trim()).join('');
  const raw=zlib.gunzipSync(Buffer.from(b64,'base64'));
  if(sha256(raw)!==expectedProjectionSha)throw new Error('OFFICIAL129_LOCAL_PROJECTION_HASH_MISMATCH');
  const data=JSON.parse(raw.toString('utf8'));
  if(data.releaseId!==expectedRelease||data.items?.length!==129)throw new Error('OFFICIAL129_LOCAL_PROJECTION_IDENTITY_FAIL');
  return data;
}

function normalize(body){
  return normalizeAppsScriptHtmlServiceWrapper(body)
    .replace(/\\x3[cC]/g,'<').replace(/\\u003[cC]/g,'<')
    .replace(/\\x3[eE]/g,'>').replace(/\\u003[eE]/g,'>')
    .replace(/\\x26/g,'&').replace(/\\u0026/g,'&')
    .replace(/\\x27/g,"'").replace(/\\u0027/g,"'")
    .replace(/\\x22/g,'"').replace(/\\u0022/g,'"');
}

async function get(url){
  const started=performance.now();
  const response=await fetch(url,{redirect:'follow',headers:{'cache-control':'no-cache','user-agent':'TTQS-ONE-R7-LIVE-PROBE/1.0'}});
  const body=await response.text();
  const ms=Math.round(performance.now()-started);
  return {url,finalUrl:response.url,status:response.status,body,normalized:normalize(body),ms};
}
function require_(condition,code,detail=''){if(!condition){const e=new Error(detail?`${code}:${detail}`:code);e.code=code;throw e;}}
function escPattern(s){return String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function attr(body,name,value){return new RegExp(`${escPattern(name)}=[\\"']${escPattern(value)}[\\"']`).test(body);}
function indicatorBase(v){return String(v).match(/^\d+/)?.[0]||'';}
async function mapLimit(items,limit,fn){const out=new Array(items.length);let next=0;async function worker(){while(true){const i=next++;if(i>=items.length)return;out[i]=await fn(items[i],i);}}await Promise.all(Array.from({length:Math.min(limit,items.length)},worker));return out;}

const data=projection();
const results={releaseId:expectedRelease,canonical,home:{},matrices:[],artifacts:[],negative:[],performance:{matrixOver2s:[],artifactOver2s:[],hardFailures:[]},result:'FAIL'};

try{
  const cold=await get(canonical);
  require_(cold.status===200,'HOME_HTTP_STATUS',String(cold.status));
  require_(!cold.normalized.includes('data-friendly-error="true"'),'HOME_FRIENDLY_ERROR');
  for(const marker of ['TTQS ONE｜顧問唯讀 DEMO 查驗入口','TEST／SAMPLE／CONTROL','19/19','26','129','不是官方強制 129 份文件',expectedRelease,expectedProjectionSha,expectedManifestSha,expectedOfflineZipSha])require_(cold.normalized.includes(marker),'HOME_MARKER_MISSING',marker);
  for(let i=1;i<=19;i++)require_(cold.normalized.includes(`data-matrix-indicator="${i}"`),'HOME_INDICATOR_LINK_MISSING',String(i));
  require_(cold.ms<=8000,'HOME_COLD_PERFORMANCE_HARD_FAIL',String(cold.ms));
  const warm=await get(canonical);
  require_(warm.status===200,'HOME_WARM_HTTP_STATUS',String(warm.status));
  require_(warm.ms<=6000,'HOME_WARM_PERFORMANCE_HARD_FAIL',String(warm.ms));
  results.home={coldMs:cold.ms,warmMs:warm.ms,status:200};
  if(warm.ms>3000)results.performance.homeWarmOver3s=warm.ms;

  const indicatorIds=Array.from({length:19},(_,i)=>String(i+1));
  results.matrices=await mapLimit(indicatorIds,6,async id=>{
    const expected=data.items.filter(x=>indicatorBase(x.indicator)===id);
    const r=await get(`${canonical}?indicator=${id}`);
    require_(r.status===200,'MATRIX_HTTP_STATUS',`${id}:${r.status}`);
    require_(!r.normalized.includes('data-friendly-error="true"'),'MATRIX_FRIENDLY_ERROR',id);
    require_(r.normalized.includes(`data-matrix-indicator="${id}"`),'MATRIX_IDENTITY_FAIL',id);
    for(const x of expected){
      require_(r.normalized.includes(`data-official-ref-id="${x.officialRefId}"`),'MATRIX_REF_MISSING',x.officialRefId);
      require_(r.normalized.includes(`data-artifact-code="${x.artifactCode}"`),'MATRIX_ARTIFACT_CODE_MISSING',x.artifactCode);
      require_(r.normalized.includes(`data-frozen-artifact-id="${x.artifactCode}"`),'MATRIX_ARTIFACT_LINK_MISSING',x.artifactCode);
      require_(r.normalized.includes(`${canonical}?artifact=${encodeURIComponent(x.artifactCode)}`),'MATRIX_CANONICAL_LINK_FAIL',x.artifactCode);
    }
    if(r.ms>4000)results.performance.hardFailures.push({kind:'matrix',id,ms:r.ms}); else if(r.ms>2000)results.performance.matrixOver2s.push({id,ms:r.ms});
    return {indicator:id,expectedItems:expected.length,status:r.status,ms:r.ms,pass:true};
  });
  require_(results.performance.hardFailures.length===0,'MATRIX_PERFORMANCE_HARD_FAIL',JSON.stringify(results.performance.hardFailures));

  results.artifacts=await mapLimit(data.items,6,async x=>{
    const r=await get(`${canonical}?artifact=${encodeURIComponent(x.artifactCode)}`);
    require_(r.status===200,'ARTIFACT_HTTP_STATUS',`${x.artifactCode}:${r.status}`);
    require_(!r.normalized.includes('data-friendly-error="true"'),'ARTIFACT_FRIENDLY_ERROR',x.artifactCode);
    for(const [name,value] of [['data-artifact-id',x.artifactCode],['data-official-ref-id',x.officialRefId],['data-release-id',expectedRelease],['data-frozen-pdf-sha256',x.pdfSha256],['data-text-sha256',x.pdfTextSha256],['data-offline-relative-path',x.offlinePdfPath]])require_(attr(r.normalized,name,value),'ARTIFACT_IDENTITY_OR_HASH_FAIL',`${x.artifactCode}:${name}`);
    for(const marker of ['TEST／SAMPLE／CONTROL','不得用於正式 TTQS 評分','Frozen PDF 文字投影',x.officialRefId,x.pdfFilename,x.pdfSha256,x.pdfTextSha256])require_(r.normalized.includes(marker),'ARTIFACT_MARKER_MISSING',`${x.artifactCode}:${marker.slice(0,80)}`);
    require_(r.body.length>=Math.max(2500,Math.floor(String(x.text).length*0.7)),'ARTIFACT_PAYLOAD_TOO_SHORT',`${x.artifactCode}:${r.body.length}`);
    if(r.ms>4000)results.performance.hardFailures.push({kind:'artifact',id:x.artifactCode,ms:r.ms}); else if(r.ms>2000)results.performance.artifactOver2s.push({id:x.artifactCode,ms:r.ms});
    return {artifactCode:x.artifactCode,officialRefId:x.officialRefId,status:r.status,bodyBytes:Buffer.byteLength(r.body),ms:r.ms,pass:true};
  });
  require_(results.performance.hardFailures.length===0,'ARTIFACT_PERFORMANCE_HARD_FAIL',JSON.stringify(results.performance.hardFailures.slice(0,20)));

  for(const [kind,url] of [['indicator',`${canonical}?indicator=999`],['artifact',`${canonical}?artifact=DOC-129-999`]]){
    const r=await get(url);
    require_(r.status===200,'NEGATIVE_HTTP_STATUS',`${kind}:${r.status}`);
    require_(r.normalized.includes('data-friendly-error="true"'),'NEGATIVE_FAIL_CLOSED_MARKER_MISSING',kind);
    require_(r.normalized.includes('不會以空白或 HTTP 200 冒充有效證據'),'NEGATIVE_NONBLANK_EXPLANATION_MISSING',kind);
    require_(r.body.length>500,'NEGATIVE_BODY_BLANK',kind);
    results.negative.push({kind,status:r.status,bodyBytes:Buffer.byteLength(r.body),ms:r.ms,pass:true});
  }

  const legacy=await get(`${canonical}?artifact=FA-DEMO-002`);
  require_(legacy.status===200,'R3_LEGACY_HTTP_STATUS',String(legacy.status));
  for(const marker of ['FA-DEMO-002','TTQS ONE｜Implementation Contract CONTROL｜2026-08-19 DRAFT R3','四、FrozenArtifact enforcement（F-01/F-02）','ER-03: 委員主查驗路徑以 frozen copy 為準'])require_(legacy.normalized.includes(marker),'R3_LEGACY_REGRESSION',marker);
  results.legacyR3={status:legacy.status,ms:legacy.ms,pass:true};

  results.result='PASS';
  process.stdout.write(`${JSON.stringify(results,null,2)}\nOFFICIAL129_LIVE_BLACKBOX_PASS items=129 matrices=19 negatives=2 release=${expectedRelease}\n`);
}catch(error){
  results.error={message:error.message,code:error.code||null};
  process.stderr.write(`${JSON.stringify(results,null,2)}\nOFFICIAL129_LIVE_BLACKBOX_FAIL ${error.message}\n`);
  process.exitCode=2;
}
