import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

function sha256File(file) {
  return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}

function normalizeRepoPath(input) {
  let rel = String(input || '').trim();
  if (rel.startsWith('./')) rel = rel.slice(2);
  if (!rel || rel.includes('\\') || path.posix.isAbsolute(rel)) return null;
  const normalized = path.posix.normalize(rel);
  if (normalized !== rel || normalized === '..' || normalized.startsWith('../')) return null;
  return normalized;
}

function trackedFiles() {
  const raw = execFileSync('git', ['ls-files', '-z'], { encoding: 'utf8' });
  return raw.split('\0').filter(Boolean);
}

const manifestPath = 'release/MANIFEST.sha256';
const selfPath = 'release/MANIFEST.sha256.sha256';
const coverageExclusions = new Set([manifestPath, selfPath]);
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
  const rel = normalizeRepoPath(match[2]);
  if (!rel) {
    errors.push(`UNSAFE_PATH:${match[2]}`);
    continue;
  }
  if (coverageExclusions.has(rel)) {
    errors.push(`MANIFEST_MUST_EXCLUDE_SELF_FILES:${rel}`);
    continue;
  }
  if (seen.has(rel)) {
    errors.push(`DUPLICATE_NORMALIZED_PATH:${rel}`);
    continue;
  }
  seen.add(rel);
  if (!fs.existsSync(rel)) {
    errors.push(`MISSING:${rel}`);
    continue;
  }
  const stat = fs.lstatSync(rel);
  if (stat.isSymbolicLink()) {
    errors.push(`SYMLINK_FORBIDDEN:${rel}`);
    continue;
  }
  if (!stat.isFile()) {
    errors.push(`NOT_REGULAR_FILE:${rel}`);
    continue;
  }
  const actual = sha256File(rel);
  if (actual !== expected) errors.push(`HASH_MISMATCH:${rel}:expected=${expected}:actual=${actual}`);
}

const tracked = trackedFiles();
const trackedManaged = new Set();
for (const raw of tracked) {
  const rel = normalizeRepoPath(raw);
  if (!rel) {
    errors.push(`UNSAFE_TRACKED_PATH:${raw}`);
    continue;
  }
  if (coverageExclusions.has(rel)) continue;
  const stat = fs.lstatSync(rel);
  if (stat.isSymbolicLink()) errors.push(`TRACKED_SYMLINK_FORBIDDEN:${rel}`);
  if (!stat.isFile()) errors.push(`TRACKED_NOT_REGULAR_FILE:${rel}`);
  trackedManaged.add(rel);
}

for (const rel of trackedManaged) {
  if (!seen.has(rel)) errors.push(`UNMANIFESTED_TRACKED:${rel}`);
}
for (const rel of seen) {
  if (!trackedManaged.has(rel)) errors.push(`MANIFESTED_BUT_UNTRACKED:${rel}`);
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
  console.error(JSON.stringify({
    status: 'FAIL',
    policy: 'manifest must exactly cover git tracked regular files except manifest and self-hash files',
    trackedManaged: trackedManaged.size,
    manifestEntries: seen.size,
    errors
  }, null, 2));
  process.exit(1);
}
console.log(JSON.stringify({
  status: 'PASS',
  entries: seen.size,
  trackedManaged: trackedManaged.size,
  coverage: 'EXACT',
  manifestSelf: sha256File(manifestPath)
}, null, 2));
