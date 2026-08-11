import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';

function sha256File(file) {
  return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}

const manifestPath = 'release/MANIFEST.sha256';
const selfPath = 'release/MANIFEST.sha256.sha256';
const lines = fs.readFileSync(manifestPath, 'utf8').split(/\r?\n/).filter(Boolean);
const seen = new Set();
const errors = [];

for (const line of lines) {
  const match = line.match(/^([0-9a-f]{64})\s+(.+)$/);
  if (!match) {
    errors.push(`INVALID_LINE:${line}`);
    continue;
  }
  const expected = match[1];
  let rel = match[2].trim();
  if (rel.startsWith('./')) rel = rel.slice(2);
  if (seen.has(rel)) {
    errors.push(`DUPLICATE_PATH:${rel}`);
    continue;
  }
  seen.add(rel);
  if (!fs.existsSync(rel) || !fs.statSync(rel).isFile()) {
    errors.push(`MISSING:${rel}`);
    continue;
  }
  const actual = sha256File(rel);
  if (actual !== expected) errors.push(`HASH_MISMATCH:${rel}:expected=${expected}:actual=${actual}`);
}

const selfLine = fs.readFileSync(selfPath, 'utf8').trim();
const selfMatch = selfLine.match(/^([0-9a-f]{64})\s+release\/MANIFEST\.sha256$/);
if (!selfMatch) {
  errors.push('INVALID_MANIFEST_SELF_LINE');
} else {
  const actualSelf = sha256File(manifestPath);
  if (actualSelf !== selfMatch[1]) errors.push(`MANIFEST_SELF_MISMATCH:expected=${selfMatch[1]}:actual=${actualSelf}`);
}

if (errors.length) {
  console.error(JSON.stringify({ status: 'FAIL', errors }, null, 2));
  process.exit(1);
}
console.log(JSON.stringify({ status: 'PASS', entries: seen.size, manifestSelf: sha256File(manifestPath) }, null, 2));
