import assert from 'node:assert/strict';
import test from 'node:test';
import {
  extractWebAppAccess,
  inspectDeploymentWebAppAccess
} from '../scripts/inspect-external-webapp-access.mjs';

const SCRIPT_ID = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA';
const DEPLOYMENT_ID = 'AKfyBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB';
const WEBAPP_URL = `https://script.google.com/macros/s/${DEPLOYMENT_ID}/exec`;

function jsonResponse(value, status = 200) {
  return {
    ok: status >= 200 && status < 300,
    status,
    async text() { return JSON.stringify(value); }
  };
}

function deployment(overrides = {}) {
  return {
    deploymentId: DEPLOYMENT_ID,
    deploymentConfig: {
      scriptId: SCRIPT_ID,
      versionNumber: 7,
      description: 'TTQS_ONE_TEST_EXTERNAL'
    },
    entryPoints: [{
      entryPointType: 'WEB_APP',
      webApp: {
        url: WEBAPP_URL,
        entryPointConfig: {
          access: 'ANYONE_ANONYMOUS',
          executeAs: 'USER_DEPLOYING'
        }
      }
    }],
    ...overrides
  };
}

test('P-01 extractor returns provider values without converting mismatch into expected values', () => {
  const readback = deployment();
  readback.entryPoints[0].webApp.entryPointConfig.access = 'DOMAIN';
  const actual = extractWebAppAccess(readback);
  assert.equal(actual.access, 'DOMAIN');
  assert.equal(actual.executeAs, 'USER_DEPLOYING');
  assert.equal(actual.webAppUrl, WEBAPP_URL);
});

test('P-01 inspector performs exactly one GET and returns deployment/version/access/executeAs', async () => {
  const calls = [];
  const result = await inspectDeploymentWebAppAccess({
    accessToken: 'token',
    scriptId: SCRIPT_ID,
    deploymentId: DEPLOYMENT_ID,
    fetchImpl: async (url, options) => {
      calls.push({url, method: options?.method || 'GET'});
      return jsonResponse(deployment());
    }
  });
  assert.equal(calls.length, 1);
  assert.equal(calls[0].method, 'GET');
  assert.equal(result.schema, 'TTQS_PROVIDER_WEBAPP_ACCESS_READBACK_V1');
  assert.equal(result.versionNumber, 7);
  assert.equal(result.access, 'ANYONE_ANONYMOUS');
  assert.equal(result.executeAs, 'USER_DEPLOYING');
  assert.equal(result.deploymentId, DEPLOYMENT_ID);
});

test('P-01 inspector fails closed on duplicate or missing WEB_APP entry point', () => {
  assert.throws(() => extractWebAppAccess({...deployment(), entryPoints: []}), /EXTERNAL_WEBAPP_ENTRYPOINT_INVALID/);
  const two = deployment();
  two.entryPoints.push(two.entryPoints[0]);
  assert.throws(() => extractWebAppAccess(two), /EXTERNAL_WEBAPP_ENTRYPOINT_INVALID/);
});
