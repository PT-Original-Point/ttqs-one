import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

export const TEST_WEBAPP_MARKER = 'TTQS_ONE_TEST_INTERNAL';
export const CLASP_PACKAGE = '@google/clasp@3.3.0';

export function isTestDeployContext(env = process.env) {
  return env.GITHUB_ACTIONS === 'true' && env.GITHUB_REF === 'refs/heads/deploy/test' && env.GITHUB_JOB === 'deploy';
}

export function isManagedDeploymentDescription(description) {
  if (description === TEST_WEBAPP_MARKER) return true;
  if (typeof description !== 'string') return false;
  const prefix = `${TEST_WEBAPP_MARKER} `;
  if (!description.startsWith(prefix)) return false;
  return /^[0-9a-f]{40}$/.test(description.slice(prefix.length));
}

export function parseClaspJson(raw, label) {
  const text = String(raw ?? '').trim();
  if (!text) throw new Error(`${label}_EMPTY`);
  try {
    return JSON.parse(text);
  } catch {
    throw new Error(`${label}_INVALID_JSON`);
  }
}

export function runClaspJson(args, options = {}) {
  const result = spawnSync('npx', ['--yes', CLASP_PACKAGE, ...args], {
    cwd: options.cwd ?? process.cwd(),
    encoding: 'utf8',
    env: options.env ?? process.env,
  });
  if (result.error) throw result.error;
  if (result.status !== 0) {
    const stderr = String(result.stderr ?? '').trim().slice(0, 1200);
    throw new Error(`CLASP_COMMAND_FAILED:${args[0]}:${result.status}:${stderr}`);
  }
  return parseClaspJson(result.stdout, `CLASP_${String(args[0] || 'COMMAND').toUpperCase().replaceAll('-', '_')}`);
}

export function selectManagedDeployment(deployments) {
  if (!Array.isArray(deployments)) throw new Error('TEST_WEBAPP_DEPLOYMENTS_NOT_ARRAY');
  const matches = deployments.filter((item) => isManagedDeploymentDescription(item?.description));
  if (matches.length > 1) throw new Error('TEST_WEBAPP_MULTIPLE_MANAGED_DEPLOYMENTS');
  if (!matches.length) return null;
  const deploymentId = matches[0]?.deploymentId;
  if (typeof deploymentId !== 'string' || !deploymentId.trim()) {
    throw new Error('TEST_WEBAPP_EXISTING_DEPLOYMENT_ID_REQUIRED');
  }
  return matches[0];
}

export function publishTestWebApp(env = process.env, runner = runClaspJson) {
  if (!isTestDeployContext(env)) {
    return { status: 'SKIP', reason: 'NOT_TEST_DEPLOY_CONTEXT' };
  }

  const sha = String(env.GITHUB_SHA ?? '').trim().toLowerCase();
  if (!/^[0-9a-f]{40}$/.test(sha)) throw new Error('TEST_WEBAPP_GITHUB_SHA_INVALID');
  const description = `${TEST_WEBAPP_MARKER} ${sha}`;

  const deployments = runner(['list-deployments', '--json'], { env });
  const existing = selectManagedDeployment(deployments);
  const args = ['create-deployment', '--description', description];
  if (existing) args.push('--deploymentId', existing.deploymentId);
  args.push('--json');

  const deployed = runner(args, { env });
  const deploymentId = deployed?.deploymentId;
  if (typeof deploymentId !== 'string' || !deploymentId.trim()) {
    throw new Error('TEST_WEBAPP_DEPLOYMENT_ID_REQUIRED');
  }
  if (existing && deploymentId !== existing.deploymentId) {
    throw new Error('TEST_WEBAPP_DEPLOYMENT_ID_DRIFT');
  }
  if (deployed?.description !== description) {
    throw new Error('TEST_WEBAPP_DEPLOYMENT_DESCRIPTION_MISMATCH');
  }
  if (!Number.isInteger(deployed?.versionNumber) || deployed.versionNumber <= 0) {
    throw new Error('TEST_WEBAPP_VERSION_NUMBER_INVALID');
  }

  return {
    status: 'PASS',
    action: existing ? 'UPDATED' : 'CREATED',
    deploymentId,
    versionNumber: deployed.versionNumber,
    description,
  };
}

function main() {
  console.log(JSON.stringify(publishTestWebApp(), null, 2));
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main();
