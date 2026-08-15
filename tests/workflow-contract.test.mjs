import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import { APPROVED_TEST_SCRIPT_ID_SHA256, isTestDeployContext, verifyApprovedTestTarget } from '../scripts/verify-clasp-status.mjs';

const paths = fs.existsSync('.github/workflows') ? fs.readdirSync('.github/workflows') : [];

test('no PROD workflow', () => assert.equal(paths.some((p) => /prod/i.test(p)), false));
test('ci workflow exists after build', () => assert.ok(paths.includes('ci.yml')));
test('dev workflow exists after build', () => assert.ok(paths.includes('deploy-dev.yml')));
test('test workflow exists after build', () => assert.ok(paths.includes('deploy-test.yml')));

test('approved TEST target fingerprint is pinned', () => {
  assert.equal(APPROVED_TEST_SCRIPT_ID_SHA256, '949a2d8127c3be600fe93b6d3e76a83e3daf296412e0f930115415eb66aab703');
});

test('target verification only activates for TEST deploy job', () => {
  assert.equal(isTestDeployContext({ GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy' }), true);
  assert.equal(isTestDeployContext({ GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'verify' }), false);
});

test('synthetic approved TEST target passes verifier logic', () => {
  const id = 'approved-test-id';
  const expectedHash = crypto.createHash('sha256').update(id, 'utf8').digest('hex');
  const result = verifyApprovedTestTarget(
    { scriptId: id, rootDir: 'apps-script' },
    { GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy' },
    expectedHash
  );
  assert.equal(result.scriptIdSha256, expectedHash);
});

test('wrong TEST target fails closed', () => {
  assert.throws(() => verifyApprovedTestTarget(
    { scriptId: 'wrong-target', rootDir: 'apps-script' },
    { GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy' }
  ), /TEST_TARGET_SCRIPT_ID_MISMATCH/);
});

test('missing scriptId fails closed', () => {
  assert.throws(() => verifyApprovedTestTarget(
    { rootDir: 'apps-script' },
    { GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy' }
  ), /TEST_TARGET_SCRIPT_ID_REQUIRED/);
});

test('wrong rootDir fails closed', () => {
  assert.throws(() => verifyApprovedTestTarget(
    { scriptId: 'anything', rootDir: 'wrong-root' },
    { GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy' }
  ), /TEST_TARGET_ROOT_DIR_MISMATCH/);
});
