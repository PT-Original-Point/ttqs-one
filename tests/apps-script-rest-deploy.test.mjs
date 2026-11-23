import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {pathToFileURL} from 'node:url';
import {
  extractAuthorizedUserCredentials,
  assertMinimalDeploymentScopes,
  refreshAccessToken,
  buildProjectFiles,
  ensureProject,
  pushProjectContent,
  createVersion,
  createOrUpdateDeployment,
  readEffectiveWebAppEntryPoint,
  isDirectExecution
} from '../scripts/apps-script-rest-deploy.mjs';

const PROJECTS = 'https://www.googleapis.com/auth/script.projects';
const DEPLOYMENTS = 'https://www.googleapis.com/auth/script.deployments';
const SHEETS_READONLY = 'https://www.googleapis.com/auth/spreadsheets.readonly';
const SCRIPT_ID = 'A'.repeat(30);
const DEPLOYMENT_ID = `AKfy${'B'.repeat(30)}`;
const WEBAPP_URL = `https://script.google.com/macros/s/${DEPLOYMENT_ID}/exec`;

function jsonResponse(body, status = 200) {
  return new Response(JSON.stringify(body), {status, headers: {'content-type': 'application/json'}});
}

function deploymentReadback(versionNumber, overrides = {}) {
  return {
    deploymentId: DEPLOYMENT_ID,
    deploymentConfig: {scriptId: SCRIPT_ID, versionNumber},
    entryPoints: [{
      entryPointType: 'WEB_APP',
      webApp: {
        url: WEBAPP_URL,
        entryPointConfig: {
          access: 'ANYONE_ANONYMOUS',
          executeAs: 'USER_DEPLOYING',
          ...(overrides.entryPointConfig || {})
        },
        ...(overrides.webApp || {})
      },
      ...(overrides.entryPoint || {})
    }],
    ...overrides.deployment
  };
}

test('extracts one authorized_user credential from clasp user-key store', () => {
  const input = {
    default: {client_id: 'client', client_secret: 'secret', refresh_token: 'refresh', type: 'authorized_user'}
  };
  assert.deepEqual(extractAuthorizedUserCredentials(input), {
    client_id: 'client', client_secret: 'secret', refresh_token: 'refresh', type: 'authorized_user'
  });
});

test('deduplicates identical nested credential copies', () => {
  const credential = {client_id: 'client', client_secret: 'secret', refresh_token: 'refresh', type: 'authorized_user'};
  assert.equal(extractAuthorizedUserCredentials({a: credential, b: {credential}}).refresh_token, 'refresh');
});

test('fails closed on multiple distinct authorized_user credentials', () => {
  assert.throws(() => extractAuthorizedUserCredentials({
    a: {client_id: 'client-a', refresh_token: 'refresh-a'},
    b: {client_id: 'client-b', refresh_token: 'refresh-b'}
  }), /AUTHORIZED_USER_CREDENTIALS_AMBIGUOUS/);
});

test('minimal OAuth scope contract accepts only deployment scopes plus snapshot read-only', () => {
  assert.deepEqual(assertMinimalDeploymentScopes(`${DEPLOYMENTS} ${SHEETS_READONLY} ${PROJECTS}`), [DEPLOYMENTS, PROJECTS, SHEETS_READONLY].sort());
});

test('minimal OAuth scope contract rejects missing required deployment scope', () => {
  assert.throws(() => assertMinimalDeploymentScopes(`${PROJECTS} ${SHEETS_READONLY}`), /OAUTH_REQUIRED_SCOPE_MISSING/);
});

test('minimal OAuth scope contract rejects cloud-platform and broad clasp defaults', () => {
  assert.throws(() => assertMinimalDeploymentScopes(`${PROJECTS} ${DEPLOYMENTS} https://www.googleapis.com/auth/cloud-platform`), /OAUTH_SCOPE_NOT_MINIMAL/);
  assert.throws(() => assertMinimalDeploymentScopes(`${PROJECTS} ${DEPLOYMENTS} https://www.googleapis.com/auth/drive.file`), /OAUTH_SCOPE_NOT_MINIMAL/);
});

test('invalid_rapt becomes stable AUTH_REAUTH_REQUIRED without leaking provider payload', async () => {
  const fakeFetch = async () => jsonResponse({error: 'invalid_grant', error_subtype: 'invalid_rapt'}, 400);
  await assert.rejects(
    refreshAccessToken({client_id: 'client', client_secret: 'secret', refresh_token: 'refresh'}, fakeFetch),
    error => error.code === 'AUTH_REAUTH_REQUIRED'
  );
});

test('direct execution detection resolves a symlinked invocation path', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-rest-entrypoint-'));
  const realPath = path.resolve('scripts/apps-script-rest-deploy.mjs');
  const linkPath = path.join(dir, 'rest-deploy.mjs');
  try {
    fs.symlinkSync(realPath, linkPath);
    assert.equal(isDirectExecution(pathToFileURL(realPath).href, linkPath), true);
  } finally {
    fs.rmSync(dir, {recursive: true, force: true});
  }
});

test('REST deploy CLI actually enters main when invoked through a symlink', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-rest-cli-'));
  const realPath = path.resolve('scripts/apps-script-rest-deploy.mjs');
  const linkPath = path.join(dir, 'rest-deploy.mjs');
  try {
    fs.symlinkSync(realPath, linkPath);
    const result = spawnSync(process.execPath, [linkPath, 'auth-check'], {encoding: 'utf8'});
    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /REST_DEPLOY_CREDENTIALS_REQUIRED/);
  } finally {
    fs.rmSync(dir, {recursive: true, force: true});
  }
});

test('project payload contains exactly Code SERVER_JS and appsscript JSON', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-rest-deploy-'));
  try {
    fs.writeFileSync(path.join(dir, 'Code.gs'), 'function doGet() { return true; }\n');
    fs.writeFileSync(path.join(dir, 'appsscript.json'), '{"timeZone":"Asia/Taipei"}\n');
    assert.deepEqual(buildProjectFiles(dir), [
      {name: 'Code', type: 'SERVER_JS', source: 'function doGet() { return true; }\n'},
      {name: 'appsscript', type: 'JSON', source: '{"timeZone":"Asia/Taipei"}\n'}
    ]);
  } finally {
    fs.rmSync(dir, {recursive: true, force: true});
  }
});

test('project payload fails closed when an unexpected third deploy file appears', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-rest-deploy-'));
  try {
    fs.writeFileSync(path.join(dir, 'Code.gs'), '');
    fs.writeFileSync(path.join(dir, 'appsscript.json'), '{}');
    fs.writeFileSync(path.join(dir, 'Unexpected.gs'), '');
    assert.throws(() => buildProjectFiles(dir), /EXTERNAL_PUSH_SET_INVALID/);
  } finally {
    fs.rmSync(dir, {recursive: true, force: true});
  }
});

test('ensureProject creates standalone project and validates returned script id', async () => {
  const calls = [];
  const fakeFetch = async (url, options = {}) => {
    calls.push({url, options});
    return jsonResponse({scriptId: SCRIPT_ID, title: 'TTQS ONE TEST External Evaluator Portal'});
  };
  const result = await ensureProject({accessToken: 'token', title: 'TTQS ONE TEST External Evaluator Portal', fetchImpl: fakeFetch});
  assert.deepEqual(result, {scriptId: SCRIPT_ID, mode: 'BOOTSTRAP'});
  assert.equal(calls[0].url, 'https://script.googleapis.com/v1/projects');
  assert.equal(calls[0].options.method, 'POST');
});

test('pushProjectContent writes exact content and validates provider readback', async () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-rest-deploy-'));
  try {
    fs.writeFileSync(path.join(dir, 'Code.gs'), 'function doGet() {}\n');
    fs.writeFileSync(path.join(dir, 'appsscript.json'), '{}\n');
    const fakeFetch = async (url, options = {}) => {
      assert.match(url, new RegExp(`/projects/${SCRIPT_ID}/content$`));
      assert.equal(options.method, 'PUT');
      const body = JSON.parse(options.body);
      assert.deepEqual(body.files.map(file => `${file.name}:${file.type}`).sort(), ['Code:SERVER_JS', 'appsscript:JSON']);
      return jsonResponse({files: body.files});
    };
    await pushProjectContent({accessToken: 'token', scriptId: SCRIPT_ID, rootDir: dir, fetchImpl: fakeFetch});
  } finally {
    fs.rmSync(dir, {recursive: true, force: true});
  }
});

test('createVersion accepts only positive provider version number', async () => {
  const fakeFetch = async () => jsonResponse({versionNumber: 7});
  assert.equal(await createVersion({accessToken: 'token', scriptId: SCRIPT_ID, description: 'test', fetchImpl: fakeFetch}), 7);
});

test('effective web app readback requires anonymous access and deploying-user execution', () => {
  assert.deepEqual(readEffectiveWebAppEntryPoint(deploymentReadback(7)), {
    url: WEBAPP_URL,
    access: 'ANYONE_ANONYMOUS',
    executeAs: 'USER_DEPLOYING'
  });
  assert.throws(
    () => readEffectiveWebAppEntryPoint(deploymentReadback(7, {entryPointConfig: {access: 'ANYONE'}})),
    /EXTERNAL_WEBAPP_ACCESS_MISMATCH/
  );
  assert.throws(
    () => readEffectiveWebAppEntryPoint(deploymentReadback(7, {entryPointConfig: {executeAs: 'USER_ACCESSING'}})),
    /EXTERNAL_WEBAPP_EXECUTE_AS_MISMATCH/
  );
  assert.throws(
    () => readEffectiveWebAppEntryPoint({...deploymentReadback(7), entryPoints: []}),
    /EXTERNAL_WEBAPP_ENTRYPOINT_INVALID/
  );
});

test('new deployment is created then provider web app entry point is read back', async () => {
  let step = 0;
  const fakeFetch = async (url, options = {}) => {
    step += 1;
    if (step === 1) {
      assert.equal(options.method, 'POST');
      const body = JSON.parse(options.body);
      assert.equal(body.versionNumber, 7);
      assert.equal(body.manifestFileName, 'appsscript');
      return jsonResponse({deploymentId: DEPLOYMENT_ID});
    }
    assert.match(url, new RegExp(`/deployments/${DEPLOYMENT_ID}$`));
    return jsonResponse(deploymentReadback(7));
  };
  const result = await createOrUpdateDeployment({
    accessToken: 'token', scriptId: SCRIPT_ID, deploymentId: '', versionNumber: 7, description: 'test', fetchImpl: fakeFetch
  });
  assert.deepEqual(result, {
    deploymentId: DEPLOYMENT_ID,
    webappUrl: WEBAPP_URL,
    webappAccess: 'ANYONE_ANONYMOUS',
    webappExecuteAs: 'USER_DEPLOYING'
  });
});

test('existing deployment update preserves id and verifies effective entry point', async () => {
  let step = 0;
  const fakeFetch = async (_url, options = {}) => {
    step += 1;
    if (step === 1) {
      assert.equal(options.method, 'PUT');
      const body = JSON.parse(options.body);
      assert.equal(body.deploymentConfig.scriptId, SCRIPT_ID);
      assert.equal(body.deploymentConfig.versionNumber, 8);
      return jsonResponse({deploymentId: DEPLOYMENT_ID});
    }
    return jsonResponse(deploymentReadback(8));
  };
  const result = await createOrUpdateDeployment({
    accessToken: 'token', scriptId: SCRIPT_ID, deploymentId: DEPLOYMENT_ID, versionNumber: 8, description: 'update', fetchImpl: fakeFetch
  });
  assert.equal(result.deploymentId, DEPLOYMENT_ID);
  assert.equal(result.webappAccess, 'ANYONE_ANONYMOUS');
});

test('deployment readback fails closed if provider downgrades anonymous access', async () => {
  let step = 0;
  const fakeFetch = async (_url, options = {}) => {
    step += 1;
    if (step === 1) return jsonResponse({deploymentId: DEPLOYMENT_ID});
    return jsonResponse(deploymentReadback(9, {entryPointConfig: {access: 'DOMAIN'}}));
  };
  await assert.rejects(
    createOrUpdateDeployment({
      accessToken: 'token', scriptId: SCRIPT_ID, deploymentId: DEPLOYMENT_ID, versionNumber: 9, description: 'policy', fetchImpl: fakeFetch
    }),
    /EXTERNAL_WEBAPP_ACCESS_MISMATCH/
  );
});
