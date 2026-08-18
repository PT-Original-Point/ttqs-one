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

test('external deploy is isolated to external-viewer and anonymous read-only manifest', () => {
  assert.match(source, /rootDir:'external-viewer'/);
  assert.match(source, /ANYONE_ANONYMOUS/);
  assert.match(source, /USER_DEPLOYING/);
  assert.match(source, /spreadsheets\.readonly/);
  assert.match(source, /enabledAdvancedServices/);
  assert.doesNotMatch(source, /rootDir:'apps-script'/);
});

test('external workflow never contains REAL or PROD deployment actions', () => {
  assert.doesNotMatch(source, /deploy\/prod|environment:\s*PROD|ENABLE_REAL_WRITES|PROD_ENABLE/);
  assert.match(source, /REAL\/PROD: not performed/);
});

test('external deployment requires anonymous product black-box proof', () => {
  assert.match(source, /Anonymous product black-box probe/);
  assert.match(source, /SAMPLE 評核因果鏈/);
  assert.match(source, /查看佐證與來源/);
  assert.match(source, /EXTERNAL_READONLY/);
  assert.match(source, /EXTERNAL_PRODUCT_BLACKBOX_PASS/);
  assert.match(source, /19 \/ 19/);
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

test('PASS receipt is published only after anonymous black-box step', () => {
  const probe = source.indexOf('- name: Anonymous product black-box probe');
  const publish = source.indexOf('- name: Publish durable deployment receipt after black-box PASS');
  assert.ok(probe >= 0 && publish > probe);
  assert.match(source.slice(publish), /--state PASS_PRODUCT_BLACKBOX/);
});

test('empty receipt uses tested resolver before creating another project', () => {
  assert.match(source, /list-scripts/);
  assert.match(source, /scripts\/resolve-external-script-id\.mjs/);
  assert.match(source, /--title "\$EXTERNAL_SCRIPT_TITLE"/);
  assert.match(source, /create-script --type standalone/);
});

test('recover/bootstrap block has no nested Node heredoc regression', () => {
  const start = source.indexOf('- name: Recover or bootstrap external TEST Apps Script project');
  const end = source.indexOf('- name: Verify external push set before deploy');
  assert.ok(start >= 0 && end > start);
  const block = source.slice(start, end);
  assert.doesNotMatch(block, /node - <<['"]?NODE/);
});

test('receipt identifiers are validated before reuse', () => {
  assert.match(source, /EXTERNAL_RECEIPT_SCRIPT_ID_INVALID/);
  assert.match(source, /EXTERNAL_RECEIPT_DEPLOYMENT_ID_INVALID/);
  assert.match(source, /EXTERNAL_RECEIPT_DEPLOYMENT_WITHOUT_SCRIPT/);
});
