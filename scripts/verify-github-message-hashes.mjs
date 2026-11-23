import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
import { normalizeRegistry, verifyReportedHashes } from './hash-registry-control.mjs';

const registryPath = process.env.TTQS_HASH_REGISTRY_FILE;
if (!registryPath) {
  console.error(JSON.stringify({
    status: 'FAIL',
    reason: 'TTQS_HASH_REGISTRY_FILE is required; CI must fail closed when the authoritative registry source is unavailable'
  }, null, 2));
  process.exit(1);
}

const registry = normalizeRegistry(JSON.parse(fs.readFileSync(registryPath, 'utf8')));
const contexts = [];

if (process.env.GITHUB_EVENT_PATH && fs.existsSync(process.env.GITHUB_EVENT_PATH)) {
  const event = JSON.parse(fs.readFileSync(process.env.GITHUB_EVENT_PATH, 'utf8'));
  if (event.pull_request) {
    contexts.push(['PR_TITLE', event.pull_request.title || '']);
    contexts.push(['PR_BODY', event.pull_request.body || '']);
  }
  if (event.head_commit?.message) contexts.push(['PUSH_HEAD_COMMIT', event.head_commit.message]);
}

try {
  const message = execFileSync('git', ['show', '-s', '--format=%B', 'HEAD'], { encoding: 'utf8' });
  contexts.push(['HEAD_COMMIT', message]);
} catch (error) {
  console.error(JSON.stringify({ status: 'FAIL', reason: 'unable to read HEAD commit message', detail: error.message }, null, 2));
  process.exit(1);
}

const results = contexts.map(([name, text]) => verifyReportedHashes(registry, text, `GITHUB:${name}`));
const failed = results.some((result) => result.status !== 'PASS');
const output = {
  status: failed ? 'FAIL' : 'PASS',
  policy: 'PR title/body and commit messages may contain only SHA-256 values present in the authoritative readback-matched Hash Registry',
  contexts: results
};

(failed ? console.error : console.log)(JSON.stringify(output, null, 2));
if (failed) process.exit(1);
