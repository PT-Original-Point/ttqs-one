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
function tryGunzip(bytes){
  try{return {raw:zlib.gunzipSync(bytes),error:null};}
  catch(error){return {raw:null,error:String(error&&error.message||error)};}
}
function inflateGzipPayloadIgnoringTrailer(bytes){
  if(bytes.length<18||bytes[0]!==0x1f||bytes[1]!==0x8b||bytes[2]!==8)return {raw:null,error:'INVALID_GZIP_HEADER'};
  const flags=bytes[3];
  if(flags&0xe0)return {raw:null,error:`RESERVED_GZIP_FLAGS:${flags}`};
  let offset=10;
  try{
    if(flags&0x04){
      if(offset+2>bytes.length-8)throw new Error('GZIP_EXTRA_LENGTH_TRUNCATED');
      const xlen=bytes.readUInt16LE(offset);offset+=2+xlen;
    }
    if(flags&0x08){while(offset<bytes.length-8&&bytes[offset]!==0)offset+=1;offset+=1;}
    if(flags&0x10){while(offset<bytes.length-8&&bytes[offset]!==0)offset+=1;offset+=1;}
    if(flags&0x02)offset+=2;
    if(offset>=bytes.length-8)throw new Error('GZIP_DEFLATE_PAYLOAD_MISSING');
    const raw=zlib.inflateRawSync(bytes.subarray(offset,bytes.length-8));
    return {raw,error:null,headerBytes:offset,trailerHex:bytes.subarray(bytes.length-8).toString('hex')};
  }catch(error){return {raw:null,error:String(error&&error.message||error)};}
}
function decodeProjection(partNames){
  const tokens=partNames.map((name)=>{
    const token=readUtf8(path.join(r7Dir,name)).trim();
    if(!/^[A-Za-z0-9+/=]+$/.test(token))fail('R7_DATA_B64_INVALID',name);
    return {name,token};
  });
  const attempts=[];

  const joinedBase64=Buffer.from(tokens.map(x=>x.token).join(''),'base64');
  const joined=tryGunzip(joinedBase64);
  attempts.push({mode:'JOIN_BASE64_TEXT',compressedBytes:joinedBase64.length,error:joined.error,rawSha256:joined.raw?sha256(joined.raw):null});
  if(joined.raw&&sha256(joined.raw)===expectedProjectionSha)return {raw:joined.raw,mode:'JOIN_BASE64_TEXT',tokens,attempts};

  const trailerRecovery=inflateGzipPayloadIgnoringTrailer(joinedBase64);
  attempts.push({mode:'GZIP_TRAILER_RECOVERY_BY_CANONICAL_RAW_SHA',compressedBytes:joinedBase64.length,error:trailerRecovery.error,rawSha256:trailerRecovery.raw?sha256(trailerRecovery.raw):null,headerBytes:trailerRecovery.headerBytes||null,trailerHex:trailerRecovery.trailerHex||null});
  if(trailerRecovery.raw&&sha256(trailerRecovery.raw)===expectedProjectionSha){
    return {raw:trailerRecovery.raw,mode:'GZIP_TRAILER_RECOVERY_BY_CANONICAL_RAW_SHA',tokens,attempts};
  }

  const decodedParts=tokens.map(x=>Buffer.from(x.token,'base64'));
  const binaryConcat=Buffer.concat(decodedParts);
  const perPart=tryGunzip(binaryConcat);
  attempts.push({mode:'DECODE_EACH_PART_THEN_CONCAT_BINARY',compressedBytes:binaryConcat.length,error:perPart.error,rawSha256:perPart.raw?sha256(perPart.raw):null});
  if(perPart.raw&&sha256(perPart.raw)===expectedProjectionSha)return {raw:perPart.raw,mode:'DECODE_EACH_PART_THEN_CONCAT_BINARY',tokens,attempts};

  const diagnostics={
    expectedProjectionSha,
    parts:tokens.map((x,i)=>({name:x.name,base64Chars:x.token.length,padding:(x.token.match(/=+$/)||[''])[0].length,decodedBytes:decodedParts[i].length})),
    attempts
  };
  fail('R7_PROJECTION_RECONSTRUCTION_FAILED',JSON.stringify(diagnostics));
}

const baseFiles=fs.readdirSync(srcDir).sort();
if(JSON.stringify(baseFiles)!==JSON.stringify(['Code.gs','appsscript.json']))fail('EXTERNAL_BASE_PUSH_SET_INVALID',baseFiles.join(','));
const parts=fs.readdirSync(r7Dir).filter(x=>/^data\.part\d+(?:[a-z])?\.b64$/.test(x)).sort(compareParts);
if(parts.length<2)fail('R7_DATA_PARTS_MISSING');
const decoded=decodeProjection(parts);
const raw=decoded.raw;
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
const projectionGzipB64=zlib.gzipSync(raw,{level:9,mtime:0}).toString('base64');
const code=base+'\n\n/* build-time injected R7 frozen projection; source sha256='+expectedProjectionSha+' */\nvar TTQS_R7_DATA_GZIP_B64_='+JSON.stringify(projectionGzipB64)+';\n'+runtimeAll+'\n';
fs.rmSync(outDir,{recursive:true,force:true});fs.mkdirSync(outDir,{recursive:true});
fs.writeFileSync(path.join(outDir,'Code.gs'),code);
fs.writeFileSync(path.join(outDir,'appsscript.json'),manifest);
const buildSha=sha256(Buffer.from(code,'utf8'));
process.stdout.write(`R7_EXTERNAL_BUILD_PASS items=129 parts=${parts.length} reconstruction=${decoded.mode} projectionSha256=${expectedProjectionSha} buildCodeSha256=${buildSha} buildBytes=${Buffer.byteLength(code)}\n`);
