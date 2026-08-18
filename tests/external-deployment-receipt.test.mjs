import test from 'node:test';
import assert from 'node:assert/strict';
import { nextReceiptBody, parseReceiptBody } from '../scripts/external-deployment-receipt.mjs';

const blankBody = `# Receipt\n\n<!-- TTQS_EXTERNAL_TEST_RECEIPT_V1 -->\n\`\`\`json\n${JSON.stringify({
  schema: 'TTQS_EXTERNAL_TEST_RECEIPT_V1',
  environment: 'TEST',
  rootDir: 'external-viewer',
  sourceSha: '',
  scriptId: '',
  deploymentId: '',
  webappUrl: '',
  anonymousBlackbox: 'NOT_RUN',
  realProdTouch: 0
}, null, 2)}\n\`\`\`\n`;

const sha = 'a'.repeat(40);
const scriptId = 'A'.repeat(30);
const deploymentId = `AKfy${'B'.repeat(30)}`;
const webappUrl = `https://script.google.com/macros/s/${deploymentId}/exec`;

test('RUNNING receipt is observable but never claims black-box PASS', () => {
  const body = nextReceiptBody(blankBody, 'RUNNING', { GITHUB_SHA: sha, GITHUB_RUN_ID: '123' });
  const receipt = parseReceiptBody(body);
  assert.equal(receipt.runStatus, 'RUNNING');
  assert.equal(receipt.sourceSha, sha);
  assert.equal(receipt.anonymousBlackbox, 'NOT_RUN');
  assert.equal(receipt.realProdTouch, 0);
  assert.match(body, /非 PASS 狀態不得解讀為成品驗收通過/);
});

test('FAILED receipt preserves previously resolved deployment identity', () => {
  const prior = nextReceiptBody(blankBody, 'PASS_PRODUCT_BLACKBOX', {
    GITHUB_SHA: sha,
    EXTERNAL_SCRIPT_ID_RESOLVED: scriptId,
    EXTERNAL_DEPLOYMENT_ID_RESOLVED: deploymentId,
    EXTERNAL_WEBAPP_URL: webappUrl
  });
  const body = nextReceiptBody(prior, 'FAILED', { GITHUB_SHA: 'b'.repeat(40), GITHUB_RUN_ID: '456' });
  const receipt = parseReceiptBody(body);
  assert.equal(receipt.runStatus, 'FAILED');
  assert.equal(receipt.scriptId, scriptId);
  assert.equal(receipt.deploymentId, deploymentId);
  assert.equal(receipt.webappUrl, webappUrl);
  assert.equal(receipt.anonymousBlackbox, 'NOT_PASS');
});

test('PASS requires script, deployment and exact canonical webapp URL', () => {
  assert.throws(() => nextReceiptBody(blankBody, 'PASS_PRODUCT_BLACKBOX', { GITHUB_SHA: sha }), /PASS_IDENTIFIERS_REQUIRED/);
  assert.throws(() => nextReceiptBody(blankBody, 'PASS_PRODUCT_BLACKBOX', {
    GITHUB_SHA: sha,
    EXTERNAL_SCRIPT_ID_RESOLVED: scriptId,
    EXTERNAL_DEPLOYMENT_ID_RESOLVED: deploymentId,
    EXTERNAL_WEBAPP_URL: 'https://example.com/not-allowed'
  }), /WEBAPP_URL_INVALID/);
  const receipt = parseReceiptBody(nextReceiptBody(blankBody, 'PASS_PRODUCT_BLACKBOX', {
    GITHUB_SHA: sha,
    GITHUB_RUN_ID: '789',
    EXTERNAL_SCRIPT_ID_RESOLVED: scriptId,
    EXTERNAL_DEPLOYMENT_ID_RESOLVED: deploymentId,
    EXTERNAL_WEBAPP_URL: webappUrl
  }));
  assert.equal(receipt.runStatus, 'PASS_PRODUCT_BLACKBOX');
  assert.equal(receipt.anonymousBlackbox, 'PASS');
  assert.equal(receipt.realProdTouch, 0);
});

test('receipt rejects REAL/PROD touch and invalid source SHA', () => {
  const polluted = blankBody.replace('"realProdTouch": 0', '"realProdTouch": 1');
  assert.throws(() => parseReceiptBody(polluted), /REAL_PROD_TOUCH_INVALID/);
  assert.throws(() => nextReceiptBody(blankBody, 'RUNNING', { GITHUB_SHA: 'not-a-sha' }), /SOURCE_SHA_INVALID/);
});
