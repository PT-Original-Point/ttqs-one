import test from 'node:test';
import assert from 'node:assert/strict';
import { shouldPublishTestWebApp } from '../scripts/verify-clasp-status.mjs';

const env = { GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy' };

test('只有 TEST post-push 狀態檔允許版本化發布', () => {
  assert.equal(shouldPublishTestWebApp('clasp-status-after.json', env), true);
});

test('pre-push 狀態檔不得發布', () => {
  assert.equal(shouldPublishTestWebApp('clasp-status-before.json', env), false);
});

test('一般 CI 不得發布', () => {
  assert.equal(shouldPublishTestWebApp('clasp-status-after.json', {}), false);
});

test('非 deploy/test 分支不得發布', () => {
  assert.equal(shouldPublishTestWebApp('clasp-status-after.json', { ...env, GITHUB_REF: 'refs/heads/main' }), false);
});
