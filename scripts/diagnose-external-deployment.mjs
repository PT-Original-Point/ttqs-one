// CONTROL-only readback diagnostic; never merged into provider runtime.
import {googleApiRequest, obtainVerifiedAccessToken} from './apps-script-rest-deploy.mjs';

const SCRIPT_API = 'https://script.googleapis.com/v1';

function fail(code) {
  const error = new Error(code);
  error.code = code;
  throw error;
}

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i];
    const value = argv[i + 1];
    if (!key?.startsWith('--') || value === undefined) fail('PROVIDER_DIAGNOSTIC_ARGS_INVALID');
    out[key.slice(2)] = value;
  }
  return out;
}

function validateScriptId(value) {
  const id = String(value || '').trim();
  if (!/^[A-Za-z0-9_-]{20,}$/.test(id)) fail('PROVIDER_DIAGNOSTIC_SCRIPT_ID_INVALID');
  return id;
}

function validateDeploymentId(value) {
  const id = String(value || '').trim();
  if (!/^AKfy[A-Za-z0-9_-]+$/.test(id)) fail('PROVIDER_DIAGNOSTIC_DEPLOYMENT_ID_INVALID');
  return id;
}

export function sanitizeDeploymentReadback(readback) {
  const config = readback?.deploymentConfig && typeof readback.deploymentConfig === 'object'
    ? readback.deploymentConfig
    : null;
  return {
    schema: 'TTQS_PROVIDER_DEPLOYMENT_DIAGNOSTIC_V1',
    topLevelKeys: readback && typeof readback === 'object' ? Object.keys(readback).sort() : [],
    deploymentId: String(readback?.deploymentId || ''),
    deploymentConfigPresent: Boolean(config),
    deploymentConfigKeys: config ? Object.keys(config).sort() : [],
    scriptIdPresent: Boolean(config && Object.hasOwn(config, 'scriptId')),
    scriptIdType: config && Object.hasOwn(config, 'scriptId') ? typeof config.scriptId : 'missing',
    scriptId: config && Object.hasOwn(config, 'scriptId') ? String(config.scriptId ?? '') : '',
    versionNumberPresent: Boolean(config && Object.hasOwn(config, 'versionNumber')),
    versionNumberType: config && Object.hasOwn(config, 'versionNumber') ? typeof config.versionNumber : 'missing',
    versionNumber: config && Object.hasOwn(config, 'versionNumber') ? config.versionNumber : null,
    descriptionPresent: Boolean(config && Object.hasOwn(config, 'description')),
    descriptionType: config && Object.hasOwn(config, 'description') ? typeof config.description : 'missing',
    description: config && Object.hasOwn(config, 'description') ? String(config.description ?? '') : '',
    entryPointCount: Array.isArray(readback?.entryPoints) ? readback.entryPoints.length : null
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.credentials || !args['script-id'] || !args['deployment-id']) fail('PROVIDER_DIAGNOSTIC_REQUIRED_ARGS_MISSING');
  const scriptId = validateScriptId(args['script-id']);
  const deploymentId = validateDeploymentId(args['deployment-id']);
  const {accessToken} = await obtainVerifiedAccessToken(args.credentials);
  const readback = await googleApiRequest(
    accessToken,
    `${SCRIPT_API}/projects/${encodeURIComponent(scriptId)}/deployments/${encodeURIComponent(deploymentId)}`
  );
  process.stdout.write(`${JSON.stringify(sanitizeDeploymentReadback(readback))}\n`);
}

main().catch(error => {
  process.stderr.write(`${String(error?.code || error?.message || 'PROVIDER_DIAGNOSTIC_FAILED')}\n`);
  process.exitCode = 1;
});
