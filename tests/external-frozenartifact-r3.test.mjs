import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import vm from 'node:vm';
import {classifyFrozenArtifact,CANONICAL_EXEC_URL,FROZEN_ARTIFACT_ID,REQUIRED_CONTENT_MARKERS} from '../scripts/external-frozenartifact-classifier.mjs';

const source=fs.readFileSync('external-viewer/Code.gs','utf8');
const runtime={};vm.createContext(runtime);vm.runInContext(source,runtime);
function stripTags(html){return html.replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();}

test('R3 additive patch keeps canonical /exec artifact links absolute and removes relative routing from rendered cards',()=>{const cards=runtime.r3CardsHtml_();const expected=`${CANONICAL_EXEC_URL}?artifact=${FROZEN_ARTIFACT_ID}`;assert.ok(cards.includes(expected));assert.doesNotMatch(cards,/href=["']\?artifact=/);assert.match(cards,new RegExp(`data-frozen-artifact-id=["']${FROZEN_ARTIFACT_ID}["']`));});

test('R3 static HTML projection is bound to the existing frozen PDF and exact build-time text projection',()=>{assert.equal(runtime.TTQS_R3_FROZEN_ARTIFACT_.artifactId,'FA-DEMO-002');assert.equal(runtime.TTQS_R3_FROZEN_ARTIFACT_.releaseId,'ER-DEMO-20260901-DRAFT-001');assert.equal(runtime.TTQS_R3_FROZEN_ARTIFACT_.pdfSha256,'d5b2cfd922918e873bdd604659f661277db2a4d0734403d6a46e85e371c984fd');assert.equal(runtime.TTQS_R3_FROZEN_ARTIFACT_.offlineRelativePath,'artifacts/IMPLEMENTATION_CONTRACT_CONTROL_R3.pdf');assert.equal(crypto.createHash('sha256').update(runtime.TTQS_R3_FROZEN_TEXT_).digest('hex'),runtime.TTQS_R3_FROZEN_ARTIFACT_.textSha256);});

test('FA-01 through FA-07 machine contract passes on static renderer; FA-08 stays human-only',()=>{const html=runtime.artifactHtml_(FROZEN_ARTIFACT_ID);const requestedUrl=`${CANONICAL_EXEC_URL}?artifact=${FROZEN_ARTIFACT_ID}`;const result=classifyFrozenArtifact({source:html,requestedUrl,requestedArtifactId:FROZEN_ARTIFACT_ID,httpStatus:200,effectiveUrl:requestedUrl});assert.equal(result.machinePass,true);for(const id of ['FA-01','FA-02','FA-03','FA-04','FA-05','FA-06','FA-07'])assert.equal(result.checks.find((item)=>item.id===id)?.result,'PASS',`${id} must pass`);assert.equal(result.checks.find((item)=>item.id==='FA-08')?.result,'HUMAN_REQUIRED');assert.ok(stripTags(html).length>=200);for(const marker of REQUIRED_CONTENT_MARKERS)assert.ok(html.includes(marker),`missing content marker: ${marker}`);});

test('HTTP 200 alone cannot pass an empty or friendly-error artifact response',()=>{const requestedUrl=`${CANONICAL_EXEC_URL}?artifact=${FROZEN_ARTIFACT_ID}`;const empty=classifyFrozenArtifact({source:'<html><body></body></html>',requestedUrl,requestedArtifactId:FROZEN_ARTIFACT_ID,httpStatus:200});assert.equal(empty.machinePass,false);assert.equal(empty.checks.find((item)=>item.id==='FA-07')?.result,'FAIL');const friendly=classifyFrozenArtifact({source:runtime.artifactHtml_('FA-NOT-FOUND'),requestedUrl,requestedArtifactId:FROZEN_ARTIFACT_ID,httpStatus:200});assert.equal(friendly.machinePass,false);assert.equal(friendly.friendlyError,true);});

test('wrong artifact identity fails instead of being silently translated',()=>{const wrong='FA-DEMO-999';const html=runtime.artifactHtml_(wrong);const result=classifyFrozenArtifact({source:html,requestedUrl:`${CANONICAL_EXEC_URL}?artifact=${wrong}`,requestedArtifactId:wrong,httpStatus:200});assert.equal(result.machinePass,false);assert.equal(result.checks.find((item)=>item.id==='FA-01')?.result,'FAIL');assert.equal(result.checks.find((item)=>item.id==='FA-05')?.result,'FAIL');});

test('NAV-01 route remains at most three navigation clicks and terminates at the FA machine composite',()=>{const cards=runtime.r3CardsHtml_();assert.equal((cards.match(/data-frozen-artifact-id=\"FA-DEMO-002\"/g)||[]).length,19);assert.match(runtime.r3AdditiveHtml_(),/首頁 → 指標卡 → Evidence Matrix → FrozenArtifact 為 3-click 查驗路徑/);const html=runtime.artifactHtml_(FROZEN_ARTIFACT_ID);const result=classifyFrozenArtifact({source:html,requestedUrl:`${CANONICAL_EXEC_URL}?artifact=${FROZEN_ARTIFACT_ID}`,requestedArtifactId:FROZEN_ARTIFACT_ID,httpStatus:200});assert.equal(result.machinePass,true);});
