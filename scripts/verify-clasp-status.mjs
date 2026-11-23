import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { pathToFileURL } from 'node:url';
import { publishTestWebApp } from './publish-test-webapp.mjs';

export const APPROVED_TEST_SCRIPT_ID_SHA256 = '949a2d8127c3be600fe93b6d3e76a83e3daf296412e0f930115415eb66aab703';

export function isTestDeployContext(env = process.env) {
  return env.GITHUB_ACTIONS === 'true' && env.GITHUB_REF === 'refs/heads/deploy/test' && env.GITHUB_JOB === 'deploy';
}

export function shouldPublishTestWebApp(file, env = process.env) {
  return isTestDeployContext(env) && path.basename(String(file || '')) === 'clasp-status-after.json';
}

export function verifyApprovedTestTarget(clasp, env = process.env, expectedHash = APPROVED_TEST_SCRIPT_ID_SHA256) {
  if (!isTestDeployContext(env)) return null;
  if (!clasp || clasp.rootDir !== 'apps-script') throw new Error('TEST_TARGET_ROOT_DIR_MISMATCH');
  if (typeof clasp.scriptId !== 'string' || !clasp.scriptId.trim()) throw new Error('TEST_TARGET_SCRIPT_ID_REQUIRED');
  if (!/^[0-9a-f]{64}$/.test(String(expectedHash || ''))) throw new Error('TEST_TARGET_POLICY_HASH_INVALID');
  const actualHash = crypto.createHash('sha256').update(clasp.scriptId.trim(), 'utf8').digest('hex');
  if (actualHash !== expectedHash) throw new Error(`TEST_TARGET_SCRIPT_ID_MISMATCH:${actualHash}`);
  return { environment: 'TEST', rootDir: 'apps-script', scriptIdSha256: actualHash };
}

function collectStrings(value, out = []) {
  if (typeof value === 'string') out.push(value);
  else if (Array.isArray(value)) value.forEach((v) => collectStrings(v, out));
  else if (value && typeof value === 'object') Object.values(value).forEach((v) => collectStrings(v, out));
  return out;
}

function main() {
  const file = process.argv[2] || 'clasp-status.json';
  const raw = fs.readFileSync(file, 'utf8').trim();
  if (!raw) throw new Error('Empty clasp status output');
  let parsed;
  try {
    parsed = JSON.parse(raw);
  } catch (err) {
    throw new Error(`clasp status is not JSON: ${raw.slice(0, 300)}`);
  }

  const strings = collectStrings(parsed).map((s) => s.replaceAll('\\', '/'));
  const appFiles = fs.readdirSync('apps-script').filter((n) => n === 'appsscript.json' || n.endsWith('.gs')).sort();
  const matched = appFiles.filter((name) => strings.some((s) => s === name || s.endsWith('/' + name)));
  const forbiddenPatterns = [
    /(^|\/)scripts\//,
    /(^|\/)tests\//,
    /(^|\/)\.github\//,
    /(^|\/)release\//,
    /package\.json$/,
    /package-lock\.json$/,
    /README\.md$/,
    /\.clasprc\.json$/,
    /\.clasp\.json$/
  ];
  const forbiddenHits = strings.filter((s) => forbiddenPatterns.some((re) => re.test(s)));
  if (forbiddenHits.length) throw new Error(`Forbidden clasp push-set entries: ${JSON.stringify(forbiddenHits)}`);
  if (matched.length !== appFiles.length) {
    throw new Error(`clasp status missing expected deploy files. matched=${JSON.stringify(matched)} expected=${JSON.stringify(appFiles)} raw=${raw.slice(0, 1000)}`);
  }

  let target = null;
  if (isTestDeployContext()) {
    let clasp;
    try {
      clasp = JSON.parse(fs.readFileSync('.clasp.json', 'utf8'));
    } catch {
      throw new Error('TEST_TARGET_CLASP_CONFIG_UNREADABLE');
    }
    target = verifyApprovedTestTarget(clasp);
  }

  const webappDeployment = shouldPublishTestWebApp(file) ? publishTestWebApp() : { status: 'SKIP', reason: 'NOT_POST_PUSH_PHASE' };
  console.log(JSON.stringify({ status: 'PASS', matched: matched.sort(), count: matched.length, target, webappDeployment }, null, 2));
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main();
