import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {inspectDeploymentVersion, sanitizeDeploymentReadback} from '../scripts/inspect-external-deployment.mjs';

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

test('sanitized provider readback exposes only structural identity/version fields',()=>{
  const diagnostic=sanitizeDeploymentReadback({
    deploymentId:DEPLOYMENT_ID,
    deploymentConfig:{scriptId:SCRIPT_ID,versionNumber:7,description:`TTQS_ONE_TEST_EXTERNAL ${SOURCE_SHA}`},
    entryPoints:[{entryPointType:'WEB_APP'}]
  },{scriptId:SCRIPT_ID,deploymentId:DEPLOYMENT_ID});
  assert.equal(diagnostic.schema,'TTQS_PROVIDER_DEPLOYMENT_READBACK_SHAPE_V1');
  assert.deepEqual(diagnostic.deploymentConfigKeys,['description','scriptId','versionNumber']);
  assert.equal(diagnostic.versionNumber,7);
  assert.equal(diagnostic.description,`TTQS_ONE_TEST_EXTERNAL ${SOURCE_SHA}`);
  assert.equal(diagnostic.entryPointCount,1);
  assert.equal(Object.hasOwn(diagnostic,'accessToken'),false);
  assert.equal(Object.hasOwn(diagnostic,'credentials'),false);
});

test('provider GET diagnostic is written before strict script identity rejection',async()=>{
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'ttqs-provider-readback-'));
  const diagnosticFile=path.join(dir,'provider-diagnostic.json');
  try{
    await assert.rejects(
      inspectDeploymentVersion({
        accessToken:'token',
        scriptId:SCRIPT_ID,
        deploymentId:DEPLOYMENT_ID,
        diagnosticFile,
        fetchImpl:async()=>jsonResponse({
          deploymentId:DEPLOYMENT_ID,
          deploymentConfig:{versionNumber:7,description:`TTQS_ONE_TEST_EXTERNAL ${SOURCE_SHA}`}
        })
      }),
      /EXTERNAL_DEPLOYMENT_SCRIPT_READBACK_MISMATCH/
    );
    const diagnostic=JSON.parse(fs.readFileSync(diagnosticFile,'utf8'));
    assert.equal(diagnostic.expectedScriptId,SCRIPT_ID);
    assert.equal(diagnostic.scriptIdPresent,false);
    assert.equal(diagnostic.versionNumber,7);
    assert.equal(diagnostic.description,`TTQS_ONE_TEST_EXTERNAL ${SOURCE_SHA}`);
  }finally{
    fs.rmSync(dir,{recursive:true,force:true});
  }
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

test('provider-version workflow is post-deploy, durable, observable on failure, and contains no provider mutation command',()=>{
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
  assert.match(workflow,/TTQS_EXTERNAL_PROVIDER_VERSION_FAILURE_V1/);
  assert.match(workflow,/Publish FAILED provider-version receipt for observability/);
  assert.match(workflow,/if: \$\{\{ failure\(\) \}\}/);
  assert.match(workflow,/workflow_run_id:/);
  assert.equal(/apps-script-rest-deploy\.mjs\s+(?:push-content|deploy|ensure-project)/.test(workflow),false);
  assert.equal(/inspect-external-deployment\.mjs[\s\S]*--root-dir/.test(workflow),false);
});

test('deploy workflow persists sanitized provider GET shape and exports same-step source SHA before strict comparison',()=>{
  const workflow=fs.readFileSync('.github/workflows/deploy-external-test.yml','utf8');
  const blackboxReceipt=workflow.indexOf('Publish durable deployment receipt after black-box PASS');
  const providerGet=workflow.indexOf('Read back exact Apps Script provider version after black-box PASS');
  const providerReceipt=workflow.indexOf('TTQS_EXTERNAL_PROVIDER_VERSION_RECEIPT_V2');
  assert.ok(blackboxReceipt>=0);
  assert.ok(providerGet>blackboxReceipt);
  assert.ok(providerReceipt>providerGet);
  const postBlackbox=workflow.slice(blackboxReceipt);
  assert.match(postBlackbox,/PROVIDER_SOURCE_SHA="\$\{EXTERNAL_RECEIPT_SOURCE_SHA:-\$GITHUB_SHA\}"\s*\n\s*export PROVIDER_SOURCE_SHA/);
  assert.match(postBlackbox,/inspect-external-deployment\.mjs/);
  assert.match(postBlackbox,/--diagnostic-file "provider-inspection-diagnostic\.json"/);
  assert.match(postBlackbox,/provider_inspection_diagnostic_sha256/);
  assert.match(postBlackbox,/cat provider-inspection-diagnostic\.json/);
  assert.match(postBlackbox,/POST_DEPLOY_READ_ONLY_PROVIDER_GET/);
  assert.match(postBlackbox,/mutation:'NONE'/);
  assert.match(postBlackbox,/PROVIDER_VERSION_SOURCE_DESCRIPTION_MISMATCH/);
  assert.match(postBlackbox,/TTQS_EXTERNAL_PROVIDER_VERSION_INTEGRATED_FAILURE_V1/);
  assert.equal(/apps-script-rest-deploy\.mjs\s+(?:ensure-project|push-content|deploy)\b/.test(postBlackbox),false);
});
