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
    if (!key?.startsWith('--') || value === undefined) throw stableError('PROVIDER_INSPECT_ARGS_INVALID');
    out[key.slice(2)] = value;
  }
  return out;
}

export function sanitizeDeploymentReadback(readback, expected = {}) {
  const config = readback?.deploymentConfig && typeof readback.deploymentConfig === 'object'
    ? readback.deploymentConfig
    : null;
  return {
    schema: 'TTQS_PROVIDER_DEPLOYMENT_READBACK_SHAPE_V1',
    topLevelKeys: readback && typeof readback === 'object' ? Object.keys(readback).sort() : [],
    expectedDeploymentId: String(expected.deploymentId || ''),
    returnedDeploymentId: String(readback?.deploymentId || ''),
    deploymentConfigPresent: Boolean(config),
    deploymentConfigKeys: config ? Object.keys(config).sort() : [],
    expectedScriptId: String(expected.scriptId || ''),
    scriptIdPresent: Boolean(config && Object.hasOwn(config, 'scriptId')),
    returnedScriptId: config && Object.hasOwn(config, 'scriptId') ? String(config.scriptId ?? '') : '',
    versionNumberPresent: Boolean(config && Object.hasOwn(config, 'versionNumber')),
    versionNumberType: config && Object.hasOwn(config, 'versionNumber') ? typeof config.versionNumber : 'missing',
    versionNumber: config && Object.hasOwn(config, 'versionNumber') ? config.versionNumber : null,
    descriptionPresent: Boolean(config && Object.hasOwn(config, 'description')),
    description: config && Object.hasOwn(config, 'description') ? String(config.description ?? '') : '',
    entryPointCount: Array.isArray(readback?.entryPoints) ? readback.entryPoints.length : null
  };
}

function writeDiagnosticFile(diagnosticFile, diagnostic) {
  if (!diagnosticFile) return;
  fs.writeFileSync(diagnosticFile, `${JSON.stringify(diagnostic)}\n`);
}

export async function inspectDeploymentVersion({accessToken, scriptId, deploymentId, diagnosticFile = '', fetchImpl = fetch}) {
  const script = validateScriptId(scriptId);
  const deployment = validateDeploymentId(deploymentId);
  const readback = await googleApiRequest(
    accessToken,
    `${SCRIPT_API}/projects/${encodeURIComponent(script)}/deployments/${encodeURIComponent(deployment)}`,
    {},
    fetchImpl
  );
  writeDiagnosticFile(diagnosticFile, sanitizeDeploymentReadback(readback, {scriptId: script, deploymentId: deployment}));
  if (String(readback.deploymentId || '') !== deployment) {
    throw stableError('EXTERNAL_DEPLOYMENT_READBACK_MISMATCH');
  }
  if (String(readback.deploymentConfig?.scriptId || '') !== script) {
    throw stableError('EXTERNAL_DEPLOYMENT_SCRIPT_READBACK_MISMATCH');
  }
  const versionNumber = validateVersionNumber(readback.deploymentConfig?.versionNumber);
  return {
    scriptId: script,
    deploymentId: deployment,
    versionNumber,
    description: String(readback.deploymentConfig?.description || '')
  };
}

function appendEnv(envFile, entries) {
  if (!envFile) return;
  const lines = Object.entries(entries).map(([key, value]) => `${key}=${String(value)}\n`).join('');
  fs.appendFileSync(envFile, lines);
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
    throw stableError('PROVIDER_INSPECT_REQUIRED_ARGS_MISSING');
  }
  const {accessToken} = await obtainVerifiedAccessToken(args.credentials);
  const result = await inspectDeploymentVersion({
    accessToken,
    scriptId: args['script-id'],
    deploymentId: args['deployment-id'],
    diagnosticFile: args['diagnostic-file'] || ''
  });
  appendEnv(args['env-file'], {
    EXTERNAL_VERSION_NUMBER: result.versionNumber
  });
  process.stdout.write(`${JSON.stringify(result)}\n`);
  process.stdout.write(`EXTERNAL_VERSION_NUMBER=${result.versionNumber}\n`);
}

if (isDirectExecution(import.meta.url, process.argv[1])) {
  main().catch(error => {
    process.stderr.write(`${String(error?.code || error?.message || 'PROVIDER_INSPECT_FAILED')}\n`);
    process.exitCode = 1;
  });
}
