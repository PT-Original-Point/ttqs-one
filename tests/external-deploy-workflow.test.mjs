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

test('deployment identity is persisted in TEST control issue after black-box PASS', () => {
  assert.match(source, /EXTERNAL_RECEIPT_ISSUE: '39'/);
  assert.match(source, /TTQS_EXTERNAL_TEST_RECEIPT_V1/);
  assert.match(source, /gh issue view/);
  assert.match(source, /gh issue edit/);
  assert.match(source, /anonymousBlackbox: 'PASS'/);
  assert.match(source, /realProdTouch: 0/);
  assert.doesNotMatch(source, /config\/external-test-deployment\.json/);
});

test('empty receipt recovers exact titled script before creating another project', () => {
  assert.match(source, /list-scripts/);
  assert.match(source, /EXTERNAL_SCRIPT_TITLE/);
  assert.match(source, /EXTERNAL_SCRIPT_TITLE_AMBIGUOUS/);
  assert.match(source, /create-script --type standalone/);
});

test('receipt identifiers are validated before reuse', () => {
  assert.match(source, /EXTERNAL_RECEIPT_SCRIPT_ID_INVALID/);
  assert.match(source, /EXTERNAL_RECEIPT_DEPLOYMENT_ID_INVALID/);
  assert.match(source, /EXTERNAL_RECEIPT_DEPLOYMENT_WITHOUT_SCRIPT/);
});
