import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {inspectDeploymentVersion} from '../scripts/inspect-external-deployment.mjs';

const SCRIPT_ID='A'.repeat(30);
const DEPLOYMENT_ID=`AKfy${'B'.repeat(30)}`;
const SOURCE_SHA='58e748221f0332d9078567fe1eae74ecb0f443fc';

function jsonResponse(body,status=200){
  return new Response(JSON.stringify(body),{status,headers:{'content-type':'application/json'}});
}

test('provider version inspection performs one read-only deployment GET and validates identity',async()=>{
  const calls=[];
  const fakeFetch=async(url,options={})=>{
    calls.push({url,options});
    return jsonResponse({
      deploymentId:DEPLOYMENT_ID,
      deploymentConfig:{
        scriptId:SCRIPT_ID,
        versionNumber:7,
        description:`TTQS_ONE_TEST_EXTERNAL ${SOURCE_SHA}`
      }
    });
  };
  const result=await inspectDeploymentVersion({
    accessToken:'token',scriptId:SCRIPT_ID,deploymentId:DEPLOYMENT_ID,fetchImpl:fakeFetch
  });
  assert.deepEqual(result,{
    scriptId:SCRIPT_ID,
    deploymentId:DEPLOYMENT_ID,
    versionNumber:7,
    description:`TTQS_ONE_TEST_EXTERNAL ${SOURCE_SHA}`
  });
  assert.equal(calls.length,1);
  assert.match(calls[0].url,new RegExp(`/projects/${SCRIPT_ID}/deployments/${DEPLOYMENT_ID}$`));
  assert.equal(calls[0].options.method,undefined);
  assert.equal(calls[0].options.body,undefined);
});

test('provider version inspection fails closed on deployment, script, or version drift',async()=>{
  await assert.rejects(
    inspectDeploymentVersion({accessToken:'token',scriptId:SCRIPT_ID,deploymentId:DEPLOYMENT_ID,fetchImpl:async()=>jsonResponse({deploymentId:'AKfyWRONG',deploymentConfig:{scriptId:SCRIPT_ID,versionNumber:7}})}),
    /EXTERNAL_DEPLOYMENT_READBACK_MISMATCH/
  );
  await assert.rejects(
    inspectDeploymentVersion({accessToken:'token',scriptId:SCRIPT_ID,deploymentId:DEPLOYMENT_ID,fetchImpl:async()=>jsonResponse({deploymentId:DEPLOYMENT_ID,deploymentConfig:{scriptId:'C'.repeat(30),versionNumber:7}})}),
    /EXTERNAL_DEPLOYMENT_SCRIPT_READBACK_MISMATCH/
  );
  await assert.rejects(
    inspectDeploymentVersion({accessToken:'token',scriptId:SCRIPT_ID,deploymentId:DEPLOYMENT_ID,fetchImpl:async()=>jsonResponse({deploymentId:DEPLOYMENT_ID,deploymentConfig:{scriptId:SCRIPT_ID,versionNumber:0}})}),
    /EXTERNAL_VERSION_INVALID/
  );
});

test('provider-version workflow is post-deploy, durable, and contains no provider mutation command',()=>{
  const workflow=fs.readFileSync('.github/workflows/verify-external-provider-version.yml','utf8');
  assert.match(workflow,/workflows:\s*\n\s*- Deploy External TEST Evaluator Portal/);
  assert.match(workflow,/environment: TEST/);
  assert.match(workflow,/node-version: '22'/);
  assert.match(workflow,/inspect-external-deployment\.mjs/);
  assert.match(workflow,/TTQS_EXTERNAL_PROVIDER_VERSION_RECEIPT_V1/);
  assert.match(workflow,/provider-version-evidence\.json/);
  assert.match(workflow,/evidence_sha256/);
  assert.match(workflow,/READ_ONLY_PROVIDER_INSPECTION/);
  assert.match(workflow,/mutation: `NONE`/);
  assert.equal(/apps-script-rest-deploy\.mjs\s+(?:push-content|deploy|ensure-project)/.test(workflow),false);
  assert.equal(/inspect-external-deployment\.mjs[\s\S]*--root-dir/.test(workflow),false);
});
