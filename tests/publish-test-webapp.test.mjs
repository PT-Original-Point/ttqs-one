import test from 'node:test';
import assert from 'node:assert/strict';
import {
  TEST_WEBAPP_MARKER,
  isManagedDeploymentDescription,
  publishTestWebApp,
  selectManagedDeployment,
} from '../scripts/publish-test-webapp.mjs';

const deployEnv = {
  GITHUB_ACTIONS: 'true',
  GITHUB_REF: 'refs/heads/deploy/test',
  GITHUB_JOB: 'deploy',
  GITHUB_SHA: '1234567890abcdef1234567890abcdef12345678',
};

function runnerFor(listResult, deployResult, calls = []) {
  return (args) => {
    calls.push(args);
    if (args[0] === 'list-deployments') return listResult;
    if (args[0] === 'create-deployment') return deployResult;
    throw new Error(`unexpected command: ${args[0]}`);
  };
}

test('非 TEST deploy context 必須略過', () => {
  assert.deepEqual(publishTestWebApp({}, () => { throw new Error('runner must not execute'); }), {
    status: 'SKIP',
    reason: 'NOT_TEST_DEPLOY_CONTEXT',
  });
});

test('GITHUB_SHA 不合法即阻擋', () => {
  assert.throws(() => publishTestWebApp({ ...deployEnv, GITHUB_SHA: 'bad' }, () => []), /TEST_WEBAPP_GITHUB_SHA_INVALID/);
});

test('沒有既有標記 deployment 時建立新 deployment', () => {
  const calls = [];
  const description = `${TEST_WEBAPP_MARKER} ${deployEnv.GITHUB_SHA}`;
  const result = publishTestWebApp(deployEnv, runnerFor([], { deploymentId: 'DEPLOY_NEW', versionNumber: 7, description }, calls));
  assert.equal(result.action, 'CREATED');
  assert.deepEqual(calls, [
    ['list-deployments', '--json'],
    ['create-deployment', '--description', description, '--json'],
  ]);
});

test('唯一舊 marker deployment 會更新同一 ID', () => {
  const calls = [];
  const description = `${TEST_WEBAPP_MARKER} ${deployEnv.GITHUB_SHA}`;
  const result = publishTestWebApp(
    deployEnv,
    runnerFor([{ deploymentId: 'DEPLOY_1', description: TEST_WEBAPP_MARKER }], { deploymentId: 'DEPLOY_1', versionNumber: 8, description }, calls),
  );
  assert.equal(result.action, 'UPDATED');
  assert.deepEqual(calls[1], ['create-deployment', '--description', description, '--deploymentId', 'DEPLOY_1', '--json']);
});

test('唯一帶 SHA marker deployment 會更新同一 ID', () => {
  const old = `${TEST_WEBAPP_MARKER} aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`;
  const description = `${TEST_WEBAPP_MARKER} ${deployEnv.GITHUB_SHA}`;
  const result = publishTestWebApp(
    deployEnv,
    runnerFor([{ deploymentId: 'DEPLOY_2', description: old }], { deploymentId: 'DEPLOY_2', versionNumber: 9, description }),
  );
  assert.equal(result.deploymentId, 'DEPLOY_2');
});

test('相似前綴不得誤認為受管 deployment', () => {
  assert.equal(isManagedDeploymentDescription(`${TEST_WEBAPP_MARKER}_OLD`), false);
  assert.equal(isManagedDeploymentDescription(`${TEST_WEBAPP_MARKER} not-a-sha`), false);
});

test('多個受管 deployment 必須失敗即阻擋', () => {
  assert.throws(
    () => selectManagedDeployment([
      { deploymentId: 'A', description: TEST_WEBAPP_MARKER },
      { deploymentId: 'B', description: `${TEST_WEBAPP_MARKER} aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` },
    ]),
    /TEST_WEBAPP_MULTIPLE_MANAGED_DEPLOYMENTS/,
  );
});

test('既有 deployment 缺 ID 必須阻擋', () => {
  assert.throws(() => selectManagedDeployment([{ description: TEST_WEBAPP_MARKER }]), /TEST_WEBAPP_EXISTING_DEPLOYMENT_ID_REQUIRED/);
});

test('部署結果缺 ID 必須阻擋', () => {
  const description = `${TEST_WEBAPP_MARKER} ${deployEnv.GITHUB_SHA}`;
  assert.throws(() => publishTestWebApp(deployEnv, runnerFor([], { versionNumber: 1, description })), /TEST_WEBAPP_DEPLOYMENT_ID_REQUIRED/);
});

test('更新既有 deployment 時 ID 漂移必須阻擋', () => {
  const description = `${TEST_WEBAPP_MARKER} ${deployEnv.GITHUB_SHA}`;
  assert.throws(
    () => publishTestWebApp(deployEnv, runnerFor([{ deploymentId: 'A', description: TEST_WEBAPP_MARKER }], { deploymentId: 'B', versionNumber: 1, description })),
    /TEST_WEBAPP_DEPLOYMENT_ID_DRIFT/,
  );
});

test('部署描述與 source SHA 不一致必須阻擋', () => {
  assert.throws(
    () => publishTestWebApp(deployEnv, runnerFor([], { deploymentId: 'A', versionNumber: 1, description: TEST_WEBAPP_MARKER })),
    /TEST_WEBAPP_DEPLOYMENT_DESCRIPTION_MISMATCH/,
  );
});

test('版本號不存在或非正整數必須阻擋', () => {
  const description = `${TEST_WEBAPP_MARKER} ${deployEnv.GITHUB_SHA}`;
  assert.throws(
    () => publishTestWebApp(deployEnv, runnerFor([], { deploymentId: 'A', versionNumber: 0, description })),
    /TEST_WEBAPP_VERSION_NUMBER_INVALID/,
  );
});
