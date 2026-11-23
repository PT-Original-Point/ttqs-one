import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {
  googleApiRequest,
  obtainVerifiedAccessToken
} from './apps-script-rest-deploy.mjs';

const SCRIPT_API = 'https://script.googleapis.com/v1';

function stableError(code, detail = '') {
  const error = new Error(detail ? `${code}:${detail}` : code);
  error.code = code;
  return error;
}

function validateScriptId(value) {
  const id = String(value || '').trim();
  if (!/^[A-Za-z0-9_-]{20,}$/.test(id)) throw stableError('EXTERNAL_SCRIPT_ID_INVALID');
  return id;
}

function validateDeploymentId(value) {
  const id = String(value || '').trim();
  if (!/^AKfy[A-Za-z0-9_-]+$/.test(id)) throw stableError('EXTERNAL_DEPLOYMENT_ID_INVALID');
  return id;
}

function validateVersionNumber(value) {
  const number = Number(value);
  if (!Number.isInteger(number) || number <= 0) throw stableError('EXTERNAL_VERSION_INVALID');
  return number;
}

export function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i];
    const value = argv[i + 1];
    if (!key?.startsWith('--') || value === undefined) throw stableError('WEBAPP_ACCESS_INSPECT_ARGS_INVALID');
    out[key.slice(2)] = value;
  }
  return out;
}

export function extractWebAppAccess(readback) {
  const entries = Array.isArray(readback?.entryPoints) ? readback.entryPoints : [];
  const webApps = entries.filter(entry => entry?.entryPointType === 'WEB_APP' && entry?.webApp);
  if (webApps.length !== 1) throw stableError('EXTERNAL_WEBAPP_ENTRYPOINT_INVALID', String(webApps.length));
  const webApp = webApps[0].webApp;
  const config = webApp.entryPointConfig && typeof webApp.entryPointConfig === 'object'
    ? webApp.entryPointConfig
    : null;
  if (!config) throw stableError('EXTERNAL_WEBAPP_ENTRY_CONFIG_MISSING');
  return {
    entryPointType: 'WEB_APP',
    webAppUrl: String(webApp.url || '').trim(),
    access: String(config.access || '').trim(),
    executeAs: String(config.executeAs || '').trim()
  };
}

export async function inspectDeploymentWebAppAccess({accessToken, scriptId, deploymentId, fetchImpl = fetch}) {
  const script = validateScriptId(scriptId);
  const deployment = validateDeploymentId(deploymentId);
  const readback = await googleApiRequest(
    accessToken,
    `${SCRIPT_API}/projects/${encodeURIComponent(script)}/deployments/${encodeURIComponent(deployment)}`,
    {},
    fetchImpl
  );
  if (String(readback.deploymentId || '') !== deployment) throw stableError('EXTERNAL_DEPLOYMENT_READBACK_MISMATCH');
  if (String(readback.deploymentConfig?.scriptId || '') !== script) throw stableError('EXTERNAL_DEPLOYMENT_SCRIPT_READBACK_MISMATCH');
  const versionNumber = validateVersionNumber(readback.deploymentConfig?.versionNumber);
  const webApp = extractWebAppAccess(readback);
  return {
    schema: 'TTQS_PROVIDER_WEBAPP_ACCESS_READBACK_V1',
    scriptId: script,
    deploymentId: deployment,
    versionNumber,
    description: String(readback.deploymentConfig?.description || ''),
    ...webApp
  };
}

function isDirectExecution(metaUrl, argvPath) {
  if (!metaUrl || !argvPath) return false;
  try {
    return fs.realpathSync(fileURLToPath(metaUrl)) === fs.realpathSync(argvPath);
  } catch {
    return false;
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.credentials || !args['script-id'] || !args['deployment-id']) {
    throw stableError('WEBAPP_ACCESS_INSPECT_REQUIRED_ARGS_MISSING');
  }
  const {accessToken} = await obtainVerifiedAccessToken(args.credentials);
  const result = await inspectDeploymentWebAppAccess({
    accessToken,
    scriptId: args['script-id'],
    deploymentId: args['deployment-id']
  });
  process.stdout.write(`${JSON.stringify(result)}\n`);
}

if (isDirectExecution(import.meta.url, process.argv[1])) {
  main().catch(error => {
    process.stderr.write(`${String(error?.code || error?.message || 'WEBAPP_ACCESS_INSPECT_FAILED')}\n`);
    process.exitCode = 1;
  });
}
