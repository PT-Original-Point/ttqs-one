import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const SCRIPT_PROJECTS = 'https://www.googleapis.com/auth/script.projects';
const SCRIPT_DEPLOYMENTS = 'https://www.googleapis.com/auth/script.deployments';
const SHEETS_READONLY = 'https://www.googleapis.com/auth/spreadsheets.readonly';
const REQUIRED_SCOPES = new Set([SCRIPT_PROJECTS, SCRIPT_DEPLOYMENTS]);
const ALLOWED_SCOPES = new Set([SCRIPT_PROJECTS, SCRIPT_DEPLOYMENTS, SHEETS_READONLY]);
const SCRIPT_API = 'https://script.googleapis.com/v1';
const TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token';
const TOKENINFO_ENDPOINT = 'https://oauth2.googleapis.com/tokeninfo';

function stableError(code, detail = '') {
  const error = new Error(detail ? `${code}:${detail}` : code);
  error.code = code;
  return error;
}

export function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i];
    const value = argv[i + 1];
    if (!key?.startsWith('--') || value === undefined) throw stableError('REST_DEPLOY_ARGS_INVALID');
    out[key.slice(2)] = value;
  }
  return out;
}

export function isDirectExecution(metaUrl, argvPath) {
  if (!metaUrl || !argvPath) return false;
  try {
    const modulePath = fs.realpathSync(fileURLToPath(metaUrl));
    const invokedPath = fs.realpathSync(path.resolve(argvPath));
    return modulePath === invokedPath;
  } catch {
    return false;
  }
}

function credentialSignature(value) {
  return [value.client_id, value.client_secret || '', value.refresh_token].join('\u0000');
}

export function extractAuthorizedUserCredentials(input) {
  const matches = [];
  const seen = new Set();
  const visit = value => {
    if (!value || typeof value !== 'object') return;
    if (typeof value.client_id === 'string' && typeof value.refresh_token === 'string') {
      const candidate = {
        type: value.type || 'authorized_user',
        client_id: value.client_id,
        client_secret: typeof value.client_secret === 'string' ? value.client_secret : '',
        refresh_token: value.refresh_token
      };
      const signature = credentialSignature(candidate);
      if (!seen.has(signature)) {
        seen.add(signature);
        matches.push(candidate);
      }
    }
    if (Array.isArray(value)) value.forEach(visit);
    else Object.values(value).forEach(visit);
  };
  visit(input);
  if (matches.length === 0) throw stableError('AUTHORIZED_USER_CREDENTIALS_NOT_FOUND');
  if (matches.length > 1) throw stableError('AUTHORIZED_USER_CREDENTIALS_AMBIGUOUS');
  const credential = matches[0];
  if (credential.type && credential.type !== 'authorized_user') throw stableError('AUTHORIZED_USER_CREDENTIAL_TYPE_INVALID');
  if (!credential.client_id.trim() || !credential.refresh_token.trim()) throw stableError('AUTHORIZED_USER_CREDENTIALS_INCOMPLETE');
  return credential;
}

export function normalizeScopes(scopeValue) {
  if (Array.isArray(scopeValue)) return [...new Set(scopeValue.map(String).map(v => v.trim()).filter(Boolean))].sort();
  return [...new Set(String(scopeValue || '').split(/\s+/).map(v => v.trim()).filter(Boolean))].sort();
}

export function assertMinimalDeploymentScopes(scopeValue) {
  const scopes = normalizeScopes(scopeValue);
  for (const required of REQUIRED_SCOPES) {
    if (!scopes.includes(required)) throw stableError('OAUTH_REQUIRED_SCOPE_MISSING', required);
  }
  const unexpected = scopes.filter(scope => !ALLOWED_SCOPES.has(scope));
  if (unexpected.length) throw stableError('OAUTH_SCOPE_NOT_MINIMAL', unexpected.join(','));
  return scopes;
}

async function parseResponse(response) {
  const text = await response.text();
  if (!text) return {};
  try {
    return JSON.parse(text);
  } catch {
    throw stableError('GOOGLE_API_NON_JSON_RESPONSE', String(response.status));
  }
}

export async function refreshAccessToken(credentials, fetchImpl = fetch) {
  const body = new URLSearchParams({
    client_id: credentials.client_id,
    refresh_token: credentials.refresh_token,
    grant_type: 'refresh_token'
  });
  if (credentials.client_secret) body.set('client_secret', credentials.client_secret);
  const response = await fetchImpl(TOKEN_ENDPOINT, {
    method: 'POST',
    headers: {'content-type': 'application/x-www-form-urlencoded'},
    body
  });
  const data = await parseResponse(response);
  if (!response.ok) {
    if (data?.error === 'invalid_grant' || data?.error_subtype === 'invalid_rapt') {
      throw stableError('AUTH_REAUTH_REQUIRED');
    }
    throw stableError('OAUTH_REFRESH_FAILED', `${response.status}:${data?.error || 'unknown'}`);
  }
  if (!data.access_token) throw stableError('OAUTH_ACCESS_TOKEN_MISSING');
  return String(data.access_token);
}

export async function inspectAccessTokenScopes(accessToken, fetchImpl = fetch) {
  const response = await fetchImpl(`${TOKENINFO_ENDPOINT}?access_token=${encodeURIComponent(accessToken)}`);
  const data = await parseResponse(response);
  if (!response.ok) throw stableError('OAUTH_TOKENINFO_FAILED', String(response.status));
  return assertMinimalDeploymentScopes(data.scope || '');
}

export async function googleApiRequest(accessToken, url, options = {}, fetchImpl = fetch) {
  const response = await fetchImpl(url, {
    ...options,
    headers: {
      authorization: `Bearer ${accessToken}`,
      accept: 'application/json',
      ...(options.body ? {'content-type': 'application/json'} : {}),
      ...(options.headers || {})
    }
  });
  const data = await parseResponse(response);
  if (!response.ok) {
    const reason = data?.error?.status || data?.error?.message || data?.error || 'unknown';
    throw stableError('GOOGLE_API_REQUEST_FAILED', `${response.status}:${String(reason).slice(0, 160)}`);
  }
  return data;
}

export function buildProjectFiles(rootDir) {
  const files = fs.readdirSync(rootDir).sort();
  const expected = ['Code.gs', 'appsscript.json'];
  if (JSON.stringify(files) !== JSON.stringify(expected)) throw stableError('EXTERNAL_PUSH_SET_INVALID');
  const code = fs.readFileSync(path.join(rootDir, 'Code.gs'), 'utf8');
  const manifest = fs.readFileSync(path.join(rootDir, 'appsscript.json'), 'utf8');
  JSON.parse(manifest);
  return [
    {name: 'Code', type: 'SERVER_JS', source: code},
    {name: 'appsscript', type: 'JSON', source: manifest}
  ];
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

function appendEnv(envFile, entries) {
  if (!envFile) return;
  const lines = Object.entries(entries).map(([key, value]) => `${key}=${String(value)}\n`).join('');
  fs.appendFileSync(envFile, lines);
}

export async function obtainVerifiedAccessToken(credentialsPath, fetchImpl = fetch) {
  const parsed = JSON.parse(fs.readFileSync(credentialsPath, 'utf8'));
  const credentials = extractAuthorizedUserCredentials(parsed);
  const accessToken = await refreshAccessToken(credentials, fetchImpl);
  const scopes = await inspectAccessTokenScopes(accessToken, fetchImpl);
  return {accessToken, scopes};
}

export async function ensureProject({accessToken, scriptId, title, fetchImpl = fetch}) {
  if (scriptId) {
    const id = validateScriptId(scriptId);
    const project = await googleApiRequest(accessToken, `${SCRIPT_API}/projects/${encodeURIComponent(id)}`, {}, fetchImpl);
    if (String(project.scriptId || '') !== id) throw stableError('EXTERNAL_SCRIPT_READBACK_MISMATCH');
    return {scriptId: id, mode: 'REUSE'};
  }
  if (!String(title || '').trim()) throw stableError('EXTERNAL_SCRIPT_TITLE_REQUIRED');
  const project = await googleApiRequest(accessToken, `${SCRIPT_API}/projects`, {
    method: 'POST',
    body: JSON.stringify({title: String(title).trim()})
  }, fetchImpl);
  const id = validateScriptId(project.scriptId);
  return {scriptId: id, mode: 'BOOTSTRAP'};
}

export async function pushProjectContent({accessToken, scriptId, rootDir, fetchImpl = fetch}) {
  const id = validateScriptId(scriptId);
  const files = buildProjectFiles(rootDir);
  const content = await googleApiRequest(accessToken, `${SCRIPT_API}/projects/${encodeURIComponent(id)}/content`, {
    method: 'PUT',
    body: JSON.stringify({files})
  }, fetchImpl);
  const returned = Array.isArray(content.files) ? content.files.map(file => `${file.name}:${file.type}`).sort() : [];
  const expected = ['Code:SERVER_JS', 'appsscript:JSON'];
  if (JSON.stringify(returned) !== JSON.stringify(expected)) throw stableError('EXTERNAL_PUSH_READBACK_MISMATCH');
  return {files: expected};
}

export async function createVersion({accessToken, scriptId, description, fetchImpl = fetch}) {
  const id = validateScriptId(scriptId);
  const version = await googleApiRequest(accessToken, `${SCRIPT_API}/projects/${encodeURIComponent(id)}/versions`, {
    method: 'POST',
    body: JSON.stringify({description: String(description || '')})
  }, fetchImpl);
  return validateVersionNumber(version.versionNumber);
}

function deploymentConfig(scriptId, versionNumber, description) {
  return {
    scriptId,
    versionNumber,
    manifestFileName: 'appsscript',
    description: String(description || '')
  };
}

export async function createOrUpdateDeployment({accessToken, scriptId, deploymentId, versionNumber, description, fetchImpl = fetch}) {
  const id = validateScriptId(scriptId);
  const version = validateVersionNumber(versionNumber);
  let deployment;
  if (deploymentId) {
    const priorId = validateDeploymentId(deploymentId);
    deployment = await googleApiRequest(accessToken, `${SCRIPT_API}/projects/${encodeURIComponent(id)}/deployments/${encodeURIComponent(priorId)}`, {
      method: 'PUT',
      body: JSON.stringify({deploymentConfig: deploymentConfig(id, version, description)})
    }, fetchImpl);
    if (String(deployment.deploymentId || '') !== priorId) throw stableError('EXTERNAL_DEPLOYMENT_ID_DRIFT');
  } else {
    deployment = await googleApiRequest(accessToken, `${SCRIPT_API}/projects/${encodeURIComponent(id)}/deployments`, {
      method: 'POST',
      body: JSON.stringify({versionNumber: version, manifestFileName: 'appsscript', description: String(description || '')})
    }, fetchImpl);
  }
  const resolvedId = validateDeploymentId(deployment.deploymentId);
  const readback = await googleApiRequest(accessToken, `${SCRIPT_API}/projects/${encodeURIComponent(id)}/deployments/${encodeURIComponent(resolvedId)}`, {}, fetchImpl);
  if (String(readback.deploymentId || '') !== resolvedId) throw stableError('EXTERNAL_DEPLOYMENT_READBACK_MISMATCH');
  if (Number(readback.deploymentConfig?.versionNumber) !== version) throw stableError('EXTERNAL_DEPLOYMENT_VERSION_READBACK_MISMATCH');
  return {deploymentId: resolvedId, webappUrl: `https://script.google.com/macros/s/${resolvedId}/exec`};
}

async function main() {
  const [command, ...rest] = process.argv.slice(2);
  const args = parseArgs(rest);
  if (!command) throw stableError('REST_DEPLOY_COMMAND_REQUIRED');
  if (!args.credentials) throw stableError('REST_DEPLOY_CREDENTIALS_REQUIRED');
  const {accessToken, scopes} = await obtainVerifiedAccessToken(args.credentials);

  if (command === 'auth-check') {
    process.stdout.write(`AUTH_MINIMAL_SCOPE_PASS ${scopes.length}\n`);
    return;
  }

  if (command === 'ensure-project') {
    const result = await ensureProject({accessToken, scriptId: args['script-id'] || '', title: args.title || ''});
    appendEnv(args['env-file'], {
      EXTERNAL_SCRIPT_ID_RESOLVED: result.scriptId,
      EXTERNAL_MODE: result.mode
    });
    process.stdout.write(`EXTERNAL_SCRIPT_ID_RESOLVED=${result.scriptId}\nEXTERNAL_MODE=${result.mode}\n`);
    return;
  }

  if (command === 'push-content') {
    if (!args['script-id'] || !args['root-dir']) throw stableError('PUSH_CONTENT_ARGS_REQUIRED');
    await pushProjectContent({accessToken, scriptId: args['script-id'], rootDir: args['root-dir']});
    process.stdout.write('EXTERNAL_CONTENT_PUSH_READBACK_PASS\n');
    return;
  }

  if (command === 'deploy') {
    if (!args['script-id']) throw stableError('DEPLOY_ARGS_REQUIRED');
    const description = args.description || '';
    const versionNumber = await createVersion({accessToken, scriptId: args['script-id'], description});
    const result = await createOrUpdateDeployment({
      accessToken,
      scriptId: args['script-id'],
      deploymentId: args['deployment-id'] || '',
      versionNumber,
      description
    });
    appendEnv(args['env-file'], {
      EXTERNAL_VERSION_NUMBER: versionNumber,
      EXTERNAL_DEPLOYMENT_ID_RESOLVED: result.deploymentId,
      EXTERNAL_WEBAPP_URL: result.webappUrl
    });
    process.stdout.write(`EXTERNAL_VERSION_NUMBER=${versionNumber}\nEXTERNAL_DEPLOYMENT_ID_RESOLVED=${result.deploymentId}\nEXTERNAL_WEBAPP_URL=${result.webappUrl}\n`);
    return;
  }

  throw stableError('REST_DEPLOY_COMMAND_INVALID', command);
}

if (isDirectExecution(import.meta.url, process.argv[1])) {
  main().catch(error => {
    const message = String(error?.code || error?.message || 'REST_DEPLOY_FAILED');
    process.stderr.write(`${message}\n`);
    process.exit(1);
  });
}
