import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const path = '.github/workflows/deploy-external-test.yml';
const source = fs.readFileSync(path, 'utf8');

test('external TEST workflow is bound to existing deploy/test control branch', () => {
  assert.match(source, /branches:\s*\n\s*- deploy\/test/);
  assert.match(source, /github\.ref == 'refs\/heads\/deploy\/test'/);
  assert.match(source, /environment: TEST/);
});

test('external TEST workflow requires source SHA to already be in main', () => {
  assert.match(source, /git merge-base --is-ancestor "\$GITHUB_SHA" origin\/main/);
});

test('external deploy is isolated to zero-runtime-permission external-viewer', () => {
  assert.match(source, /--root-dir external-viewer/);
  assert.match(source, /ANYONE_ANONYMOUS/);
  assert.match(source, /USER_DEPLOYING/);
  assert.match(source, /EXTERNAL_RUNTIME_OAUTH_SCOPE_FORBIDDEN/);
  assert.match(source, /EXTERNAL_RUNTIME_ADVANCED_SERVICE_FORBIDDEN/);
  assert.match(source, /EXTERNAL_RUNTIME_GOOGLE_DATA_API_FORBIDDEN/);
  assert.doesNotMatch(source, /spreadsheets\.readonly|enabledAdvancedServices/);
  assert.doesNotMatch(source, /--root-dir apps-script/);
});

test('external workflow never contains REAL or PROD deployment actions', () => {
  assert.doesNotMatch(source, /deploy\/prod|environment:\s*PROD|ENABLE_REAL_WRITES|PROD_ENABLE/);
  assert.match(source, /REAL\/PROD: not performed/);
});

test('deployment no longer invokes clasp in CI and uses tested Apps Script REST deployer', () => {
  assert.doesNotMatch(source, /@google\/clasp|\bnpx\s+.*clasp|\.clasprc\.json/);
  assert.match(source, /scripts\/apps-script-rest-deploy\.mjs auth-check/);
  assert.match(source, /scripts\/apps-script-rest-deploy\.mjs ensure-project/);
  assert.match(source, /scripts\/apps-script-rest-deploy\.mjs push-content/);
  assert.match(source, /scripts\/apps-script-rest-deploy\.mjs deploy/);
  assert.match(source, /Apps Script REST API with minimal deployment OAuth contract/);
});

test('OAuth credential material is decoded into runner temp and checked before provider mutation', () => {
  assert.match(source, /OAUTH_FILE="\$RUNNER_TEMP\/ttqs-external-oauth\.json"/);
  assert.match(source, /chmod 600 "\$OAUTH_FILE"/);
  const authCheck = source.indexOf('- name: Verify minimal OAuth deployment contract');
  const ensureProject = source.indexOf('- name: Recover or bootstrap external TEST Apps Script project via REST');
  assert.ok(authCheck >= 0 && ensureProject > authCheck);
});

test('external deployment requires normalized anonymous product black-box proof', () => {
  assert.match(source, /Anonymous product black-box probe/);
  assert.match(source, /scripts\/external-blackbox-classifier\.mjs --html external-page\.html/);
  assert.match(source, /EXTERNAL_PRODUCT_BLACKBOX_PASS/);
  assert.match(source, /EXTERNAL_PRODUCT_BLACKBOX_FAIL status=/);
  assert.doesNotMatch(source, /grep -Fq '19 \/ 19'/);
});

test('deployment lifecycle is observable through TEST control issue', () => {
  assert.match(source, /EXTERNAL_RECEIPT_ISSUE: '39'/);
  assert.match(source, /Mark external deployment receipt RUNNING/);
  assert.match(source, /--state RUNNING/);
  assert.match(source, /--state PASS_PRODUCT_BLACKBOX/);
  assert.match(source, /Publish FAILED receipt for observability/);
  assert.match(source, /--state FAILED/);
  assert.match(source, /if: \$\{\{ failure\(\) \}\}/);
  assert.match(source, /gh issue view/);
  assert.match(source, /gh issue edit/);
});

test('new script identity is durably persisted before any content push', () => {
  const ensure = source.indexOf('- name: Recover or bootstrap external TEST Apps Script project via REST');
  const persist = source.indexOf('- name: Persist external script identity before content push');
  const push = source.indexOf('- name: Push external TEST viewer via Apps Script REST');
  assert.ok(ensure >= 0 && persist > ensure && push > persist);
  assert.match(source.slice(persist, push), /--state RUNNING/);
});

test('deployment identity is durably persisted before anonymous black-box probe', () => {
  const deploy = source.indexOf('- name: Create or update external TEST web app deployment via REST');
  const persist = source.indexOf('- name: Persist external deployment identity before black-box probe');
  const probe = source.indexOf('- name: Anonymous product black-box probe');
  assert.ok(deploy >= 0 && persist > deploy && probe > persist);
  assert.match(source.slice(persist, probe), /--state RUNNING/);
});

test('PASS receipt is published only after anonymous black-box step', () => {
  const probe = source.indexOf('- name: Anonymous product black-box probe');
  const publish = source.indexOf('- name: Publish durable deployment receipt after black-box PASS');
  assert.ok(probe >= 0 && publish > probe);
  assert.match(source.slice(publish), /--state PASS_PRODUCT_BLACKBOX/);
});

test('workflow has no Node heredoc regression', () => {
  assert.doesNotMatch(source, /node - <<['"]?NODE/);
});

test('receipt identifiers are validated before reuse', () => {
  assert.match(source, /EXTERNAL_RECEIPT_SCRIPT_ID_INVALID/);
  assert.match(source, /EXTERNAL_RECEIPT_DEPLOYMENT_ID_INVALID/);
  assert.match(source, /EXTERNAL_RECEIPT_DEPLOYMENT_WITHOUT_SCRIPT/);
});
