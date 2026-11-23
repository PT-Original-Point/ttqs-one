import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { assessDeployControls, isDeployControlContext, verifyGitHubDeployControls } from '../scripts/verify-github-deploy-controls.mjs';

const good = {
  branch: { name: 'main', protected: true },
  environment: { deployment_branch_policy: { protected_branches: false, custom_branch_policies: true } },
  branchPolicies: { branch_policies: [{ name: 'deploy/test' }] }
};

test('gate passes only the exact minimum control state', () => {
  assert.equal(assessDeployControls(good).status, 'PASS');
});

test('unprotected main fails closed', () => {
  assert.match(assessDeployControls({ ...good, branch: { name: 'main', protected: false } }).errors.join('|'), /MAIN_BRANCH_NOT_PROTECTED/);
});

test('missing TEST deployment branch policy fails closed', () => {
  assert.match(assessDeployControls({ ...good, environment: { deployment_branch_policy: null } }).errors.join('|'), /TEST_CUSTOM_BRANCH_POLICY_NOT_ENABLED/);
});

test('protected-branches mode is not accepted in place of exact custom allowlist', () => {
  const environment = { deployment_branch_policy: { protected_branches: true, custom_branch_policies: false } };
  assert.match(assessDeployControls({ ...good, environment }).errors.join('|'), /TEST_CUSTOM_BRANCH_POLICY_NOT_ENABLED/);
});

test('wildcard deployment branch policy fails closed', () => {
  const branchPolicies = { branch_policies: [{ name: 'deploy/*' }] };
  assert.match(assessDeployControls({ ...good, branchPolicies }).errors.join('|'), /TEST_DEPLOY_BRANCH_ALLOWLIST_INVALID/);
});

test('extra deployment branches fail closed', () => {
  const branchPolicies = { branch_policies: [{ name: 'deploy/test' }, { name: 'main' }] };
  assert.match(assessDeployControls({ ...good, branchPolicies }).errors.join('|'), /TEST_DEPLOY_BRANCH_ALLOWLIST_INVALID/);
});

test('deploy gate activates only for deploy/test deploy job', () => {
  const env = { GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy' };
  assert.equal(isDeployControlContext(env), true);
  assert.equal(isDeployControlContext({ ...env, GITHUB_JOB: 'verify' }), false);
  assert.equal(isDeployControlContext({ ...env, GITHUB_REF: 'refs/heads/main' }), false);
});

async function withMockFetch(responses, fn) {
  const original = globalThis.fetch;
  let index = 0;
  globalThis.fetch = async () => {
    const value = responses[index++];
    if (!value) throw new Error('UNEXPECTED_FETCH');
    return { ok: value.ok !== false, status: value.status || 200, json: async () => value.body };
  };
  try { return await fn(); } finally { globalThis.fetch = original; }
}

test('real deploy context fails before credentials when controls are not configured', async () => {
  const env = {
    GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy',
    GITHUB_REPOSITORY: 'PT-Original-Point/ttqs-one', GITHUB_API_URL: 'https://api.github.com'
  };
  await assert.rejects(
    withMockFetch([
      { body: { name: 'main', protected: false } },
      { body: { name: 'TEST', deployment_branch_policy: null } }
    ], () => verifyGitHubDeployControls(env)),
    /MAIN_BRANCH_NOT_PROTECTED.*TEST_CUSTOM_BRANCH_POLICY_NOT_ENABLED/
  );
});

test('real deploy context passes only after exact controls are present', async () => {
  const env = {
    GITHUB_ACTIONS: 'true', GITHUB_REF: 'refs/heads/deploy/test', GITHUB_JOB: 'deploy',
    GITHUB_REPOSITORY: 'PT-Original-Point/ttqs-one', GITHUB_API_URL: 'https://api.github.com'
  };
  const result = await withMockFetch([
    { body: { name: 'main', protected: true } },
    { body: { name: 'TEST', deployment_branch_policy: { protected_branches: false, custom_branch_policies: true } } },
    { body: { branch_policies: [{ name: 'deploy/test' }] } }
  ], () => verifyGitHubDeployControls(env));
  assert.equal(result.status, 'PASS');
});

test('package verify includes deployment control gate', () => {
  const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
  assert.match(pkg.scripts.verify, /verify:deploy-controls/);
});

test('deploy workflow runs npm verify before restoring TEST credentials', () => {
  const workflow = fs.readFileSync('.github/workflows/deploy-test.yml', 'utf8');
  const verifyAt = workflow.indexOf('npm run verify');
  const restoreAt = workflow.indexOf('Restore TEST-only clasp credentials');
  const pushAt = workflow.indexOf('Push TEST');
  assert.ok(verifyAt >= 0 && restoreAt > verifyAt && pushAt > restoreAt);
});
