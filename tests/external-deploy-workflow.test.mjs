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

test('verifier-only deploy/test pushes skip OAuth and all provider mutation', () => {
  assert.match(source, /git diff --quiet "\$BEFORE" "\$GITHUB_SHA" -- external-viewer/);
  assert.match(source, /FULL_DEPLOY=0/);
  assert.match(source, /EXTERNAL_FULL_DEPLOY="\$FULL_DEPLOY"/);
  assert.match(source, /BLACKBOX_ONLY_NO_PROVIDER_MUTATION/);
  assert.match(source, /EXTERNAL_RECEIPT_SOURCE_SHA/);
  const guarded = source.match(/if: env\.EXTERNAL_FULL_DEPLOY == '1'/g) || [];
  assert.ok(guarded.length >= 7, `expected provider mutation steps to be guarded, got ${guarded.length}`);
  for (const name of [
    'Restore TEST OAuth credential material',
    'Verify minimal OAuth deployment contract',
    'Recover or bootstrap external TEST Apps Script project via REST',
    'Persist external script identity before content push',
    'Push external TEST viewer via Apps Script REST',
    'Create or update external TEST web app deployment via REST',
    'Persist external deployment identity before black-box probe'
  ]) {
    const start = source.indexOf(`- name: ${name}`);
    assert.ok(start >= 0, `missing provider step: ${name}`);
    const block = source.slice(start, source.indexOf('\n      - name:', start + 1) === -1 ? undefined : source.indexOf('\n      - name:', start + 1));
    assert.match(block, /if: env\.EXTERNAL_FULL_DEPLOY == '1'/, `provider step is not guarded: ${name}`);
  }
});

test('blackbox-only mode requires existing durable deployment identity and keeps deployed source SHA', () => {
  assert.match(source, /EXTERNAL_BLACKBOX_ONLY_IDENTITY_REQUIRED/);
  assert.match(source, /EXTERNAL_RECEIPT_SOURCE_SHA='\+src/);
  assert.match(source, /EXTERNAL_SCRIPT_ID_RESOLVED='\+s/);
  assert.match(source, /EXTERNAL_DEPLOYMENT_ID_RESOLVED='\+d/);
  assert.match(source, /EXTERNAL_WEBAPP_URL='\+u/);
});

test('external deployment requires normalized anonymous product black-box proof in every mode', () => {
  assert.match(source, /Anonymous product black-box probe/);
  assert.match(source, /scripts\/external-blackbox-classifier\.mjs --html external-page\.html/);
  assert.match(source, /EXTERNAL_PRODUCT_BLACKBOX_PASS/);
  assert.match(source, /EXTERNAL_PRODUCT_BLACKBOX_FAIL status=/);
  assert.doesNotMatch(source, /grep -Fq '19 \/ 19'/);
  const probe = source.indexOf('- name: Anonymous product black-box probe');
  const shell = source.indexOf('shell: bash', probe);
  assert.ok(probe >= 0 && shell > probe);
  assert.doesNotMatch(source.slice(probe, shell), /if:/);
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

test('durable receipt is read before RUNNING state is published', () => {
  const read = source.indexOf('- name: Read durable receipt and select provider mutation mode');
  const running = source.indexOf('- name: Mark external deployment receipt RUNNING');
  assert.ok(read >= 0 && running > read);
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
  assert.match(source, /EXTERNAL_RECEIPT_WEBAPP_URL_INVALID/);
});
