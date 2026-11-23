import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import zlib from 'node:zlib';
import {FRAGMENT_NAMES,sha256,splitProjection} from '../scripts/split-official129-projection.mjs';

const root=process.cwd();
const r7Dir=path.join(root,'release','official129');
const expectedProjectionSha='94590a9bbfdca699235815fb96e4c37c69156f10689e70b6c3caa74527165a53';
const expectedRelease='ER-DEMO-20260901-DRAFT-003';

test('P-03 splitter round-trips exact source bytes through 22 fragments',()=>{
  const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'ttqs-p03-'));
  try{
    const sourcePath=path.join(tmp,'source.json'),outDir=path.join(tmp,'parts');
    const source=Buffer.from(JSON.stringify({releaseId:'P03-FIXTURE',items:Array.from({length:64},(_,i)=>({seq:i+1,text:`fixture-${i+1}-${'x'.repeat(64)}`}))})+'\n','utf8');
    fs.writeFileSync(sourcePath,source);
    const result=splitProjection({sourcePath,outDir});
    assert.equal(result.fragmentCount,22);assert.equal(result.sourceSha256,sha256(source));assert.equal(result.recoveredSha256,result.sourceSha256);
    assert.deepEqual(fs.readdirSync(outDir).sort(),[...FRAGMENT_NAMES].sort());
  }finally{fs.rmSync(tmp,{recursive:true,force:true});}
});

test('P-03 committed DRAFT-003 fragments reconstruct exact registered source hash and release identity',()=>{
  assert.deepEqual(FRAGMENT_NAMES.filter(name=>!fs.existsSync(path.join(r7Dir,name))),[],'P03_FRAGMENT_SET_INCOMPLETE');
  const joined=FRAGMENT_NAMES.map(name=>fs.readFileSync(path.join(r7Dir,name),'utf8').trim()).join('');
  const recovered=zlib.gunzipSync(Buffer.from(joined,'base64'));
  assert.equal(sha256(recovered),expectedProjectionSha,'P03_CANONICAL_SOURCE_HASH_MISMATCH');
  const data=JSON.parse(recovered.toString('utf8'));
  assert.equal(data.releaseId,expectedRelease);assert.equal(data.items.length,129);
});
