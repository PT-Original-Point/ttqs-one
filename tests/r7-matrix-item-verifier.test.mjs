import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import {verifyEvidenceMatrixItemIdentity} from '../scripts/r7-matrix-item-verifier.mjs';

const fixtureDir=path.join('tests','fixtures','r7-nav-verifier-repair','provider-v11-source-53c6f5-20260824');
const fixture=JSON.parse(fs.readFileSync(path.join(fixtureDir,'fixture.json'),'utf8'));
const matrix=fs.readFileSync(path.join(fixtureDir,'browser.matrix.body.outerHTML.html'),'utf8');
const canonical=fixture.source.canonicalUrl;

function verify(input,overrides={}){
  return verifyEvidenceMatrixItemIdentity(input,{
    officialRefId:'OEV-1-01',
    artifactCode:'DOC-129-01',
    canonical,
    ...overrides
  });
}

test('actual provider Matrix card binds OEV ref to exact canonical artifact route',()=>{
  const result=verify(matrix);
  assert.equal(result.pass,true,result.code||'unexpected failure');
  assert.equal(result.officialRefId,'OEV-1-01');
  assert.equal(result.artifactCode,'DOC-129-01');
  assert.equal(result.expectedUrl,`${canonical}?artifact=DOC-129-01`);
});

test('matrix item verifier fail-closes when official reference text is absent from its card',()=>{
  const broken=matrix.replace('OEV-1-01','OEV-X-XX');
  assert.notEqual(broken,matrix);
  const result=verify(broken);
  assert.equal(result.pass,false);
  assert.equal(result.code,'MATRIX_REF_MISSING');
});

test('matrix item verifier fail-closes when exact canonical artifact route is absent',()=>{
  const broken=matrix.replace(`${canonical}?artifact=DOC-129-01`,'https://example.invalid/not-canonical');
  assert.notEqual(broken,matrix);
  const result=verify(broken);
  assert.equal(result.pass,false);
  assert.equal(result.code,'MATRIX_CANONICAL_ARTIFACT_ROUTE_MISSING');
});
