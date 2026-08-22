import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {FRAGMENT_NAMES,sha256,splitProjection} from '../scripts/split-official129-projection.mjs';

const root=process.cwd();
const canonicalSource=path.join(root,'release','official129','portal_static_projection_source.json');

test('P-03 splitter round-trips exact source bytes through 22 fragments',()=>{
  const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'ttqs-p03-'));
  try{
    const sourcePath=path.join(tmp,'source.json');
    const outDir=path.join(tmp,'parts');
    const source=Buffer.from(JSON.stringify({releaseId:'P03-FIXTURE',items:Array.from({length:64},(_,i)=>({seq:i+1,text:`fixture-${i+1}-${'x'.repeat(64)}`}))})+'\n','utf8');
    fs.writeFileSync(sourcePath,source);
    const result=splitProjection({sourcePath,outDir});
    assert.equal(result.fragmentCount,22);
    assert.equal(result.sourceSha256,sha256(source));
    assert.equal(result.recoveredSha256,result.sourceSha256);
    assert.deepEqual(fs.readdirSync(outDir).sort(),[...FRAGMENT_NAMES].sort());
    const joined=FRAGMENT_NAMES.map(name=>fs.readFileSync(path.join(outDir,name),'utf8').trim()).join('');
    assert.ok(joined.length>0);
  }finally{
    fs.rmSync(tmp,{recursive:true,force:true});
  }
});

test('P-03 canonical DRAFT-002 source must exist as retrievable exact bytes before CI may pass',()=>{
  assert.ok(
    fs.existsSync(canonicalSource),
    'P03_CANONICAL_SOURCE_MISSING: F-11 remains open; do not reconstruct canonical truth from current fragments'
  );
  const source=fs.readFileSync(canonicalSource);
  assert.ok(source.length>0,'P03_CANONICAL_SOURCE_EMPTY');
  const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'ttqs-p03-canonical-'));
  try{
    const result=splitProjection({sourcePath:canonicalSource,outDir:path.join(tmp,'parts')});
    assert.equal(result.fragmentCount,22);
    assert.equal(result.sourceSha256,sha256(source));
    assert.equal(result.recoveredSha256,result.sourceSha256);
  }finally{
    fs.rmSync(tmp,{recursive:true,force:true});
  }
});
