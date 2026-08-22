import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {pathToFileURL} from 'node:url';

export const FRAGMENT_NAMES = [
  'data.part00.b64','data.part01.b64','data.part02a.b64','data.part02b.b64',
  'data.part03.b64','data.part04.b64','data.part05a.b64','data.part05b.b64',
  'data.part06.b64','data.part07a.b64','data.part07b.b64','data.part08a.b64',
  'data.part08b.b64','data.part09a.b64','data.part09b.b64','data.part10a.b64',
  'data.part10b.b64','data.part11.b64','data.part12a.b64','data.part12b.b64',
  'data.part13.b64','data.part14.b64'
];

export function sha256(bytes){
  return crypto.createHash('sha256').update(bytes).digest('hex');
}

function splitBase64AtQuanta(text,count){
  if(text.length%4!==0)throw new Error('P03_BASE64_NOT_QUANTIZED');
  const quanta=text.length/4;
  if(quanta<count)throw new Error('P03_SOURCE_TOO_SMALL_FOR_22_FRAGMENTS');
  const base=Math.floor(quanta/count);
  const extra=quanta%count;
  const parts=[];
  let cursor=0;
  for(let i=0;i<count;i++){
    const q=base+(i<extra?1:0);
    const chars=q*4;
    parts.push(text.slice(cursor,cursor+chars));
    cursor+=chars;
  }
  if(cursor!==text.length)throw new Error('P03_SPLIT_CURSOR_MISMATCH');
  return parts;
}

export function splitProjection({sourcePath,outDir}){
  if(!sourcePath||!fs.existsSync(sourcePath))throw new Error(`P03_CANONICAL_SOURCE_MISSING:${sourcePath||''}`);
  const source=fs.readFileSync(sourcePath);
  if(source.length===0)throw new Error('P03_CANONICAL_SOURCE_EMPTY');
  const sourceHash=sha256(source);

  const gzip=zlib.gzipSync(source,{level:9,mtime:0});
  const encoded=gzip.toString('base64');
  const fragments=splitBase64AtQuanta(encoded,FRAGMENT_NAMES.length);

  fs.rmSync(outDir,{recursive:true,force:true});
  fs.mkdirSync(outDir,{recursive:true});
  for(let i=0;i<FRAGMENT_NAMES.length;i++){
    fs.writeFileSync(path.join(outDir,FRAGMENT_NAMES[i]),fragments[i]+'\n',{encoding:'utf8'});
  }

  const concatenated=FRAGMENT_NAMES.map(name=>fs.readFileSync(path.join(outDir,name),'utf8').trim()).join('');
  const recovered=zlib.gunzipSync(Buffer.from(concatenated,'base64'));
  const recoveredHash=sha256(recovered);
  if(!source.equals(recovered))throw new Error('P03_ROUNDTRIP_BYTE_MISMATCH');
  if(recoveredHash!==sourceHash)throw new Error(`P03_ROUNDTRIP_HASH_MISMATCH:${sourceHash}:${recoveredHash}`);

  return {
    sourcePath,
    sourceBytes:source.length,
    sourceSha256:sourceHash,
    gzipBytes:gzip.length,
    base64Chars:encoded.length,
    fragmentCount:FRAGMENT_NAMES.length,
    recoveredBytes:recovered.length,
    recoveredSha256:recoveredHash,
    result:'PASS'
  };
}

function arg(name){
  const i=process.argv.indexOf(name);
  return i>=0?process.argv[i+1]:null;
}

if(process.argv[1]&&import.meta.url===pathToFileURL(path.resolve(process.argv[1])).href){
  const sourcePath=arg('--source');
  const outDir=arg('--out-dir');
  if(!sourcePath||!outDir){
    console.error('usage: node scripts/split-official129-projection.mjs --source <exact-json-bytes> --out-dir <fragment-dir>');
    process.exit(2);
  }
  try{
    const result=splitProjection({sourcePath:path.resolve(sourcePath),outDir:path.resolve(outDir)});
    process.stdout.write(`P03_FRAGMENT_ROUNDTRIP_PASS sourceSha256=${result.sourceSha256} fragments=${result.fragmentCount} sourceBytes=${result.sourceBytes}\n`);
  }catch(error){
    console.error(String(error&&error.stack||error));
    process.exit(1);
  }
}
