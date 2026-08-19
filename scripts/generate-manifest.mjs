import crypto from 'node:crypto';
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';

const MANIFEST_PATH = 'release/MANIFEST.sha256';
const SELF_PATH = 'release/MANIFEST.sha256.sha256';
const EXCLUDED = new Set([MANIFEST_PATH, SELF_PATH]);

function runGit(args, options = {}) {
  return execFileSync('git', args, { maxBuffer: 128 * 1024 * 1024, ...options });
}

function parseArgs(argv) {
  const out = { source: 'commit', ref: 'HEAD', check: false, manifestOut: null, selfOut: null };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--index') out.source = 'index';
    else if (arg === '--check') out.check = true;
    else if (arg === '--ref') out.ref = argv[++i];
    else if (arg === '--manifest-out') out.manifestOut = argv[++i];
    else if (arg === '--self-out') out.selfOut = argv[++i];
    else throw new Error(`unknown argument: ${arg}`);
  }
  if (out.source === 'index' && out.ref !== 'HEAD') throw new Error('--index and --ref are mutually exclusive');
  return out;
}

function safePath(value) {
  if (!value || value.includes('\n') || value.includes('\r') || value.includes('\\')) return false;
  if (value.startsWith('/') || value === '..' || value.startsWith('../') || value.includes('/../')) return false;
  return true;
}

function parseCommitEntries(ref) {
  const raw = runGit(['ls-tree', '-r', '-z', '--full-tree', ref]);
  return raw.toString('utf8').split('\0').filter(Boolean).map((record) => {
    const tab = record.indexOf('\t');
    if (tab < 0) throw new Error(`invalid ls-tree record: ${record}`);
    const meta = record.slice(0, tab).split(' ');
    const filePath = record.slice(tab + 1);
    if (meta.length !== 3) throw new Error(`invalid ls-tree metadata: ${record}`);
    const [mode, type, oid] = meta;
    return { mode, type, oid, path: filePath };
  });
}

function parseIndexEntries() {
  const raw = runGit(['ls-files', '--stage', '-z']);
  return raw.toString('utf8').split('\0').filter(Boolean).map((record) => {
    const tab = record.indexOf('\t');
    if (tab < 0) throw new Error(`invalid ls-files record: ${record}`);
    const meta = record.slice(0, tab).split(' ');
    const filePath = record.slice(tab + 1);
    if (meta.length !== 3) throw new Error(`invalid ls-files metadata: ${record}`);
    const [mode, oid, stage] = meta;
    if (stage !== '0') throw new Error(`unmerged index entry forbidden: ${filePath}`);
    return { mode, type: 'blob', oid, path: filePath };
  });
}

function normalizedEntries(options) {
  const entries = options.source === 'index' ? parseIndexEntries() : parseCommitEntries(options.ref);
  for (const entry of entries) {
    if (!safePath(entry.path)) throw new Error(`unsafe tracked path: ${entry.path}`);
    if (entry.type !== 'blob') throw new Error(`non-blob tracked object forbidden: ${entry.path}:${entry.type}`);
    if (entry.mode === '120000') throw new Error(`tracked symlink forbidden: ${entry.path}`);
    if (!/^100(644|755)$/.test(entry.mode)) throw new Error(`unsupported tracked file mode: ${entry.path}:${entry.mode}`);
  }
  return entries
    .filter((entry) => !EXCLUDED.has(entry.path))
    .sort((a, b) => Buffer.compare(Buffer.from(a.path, 'utf8'), Buffer.from(b.path, 'utf8')));
}

function objectBytes(oid) {
  return runGit(['cat-file', 'blob', oid]);
}

function sourceFileBytes(options, filePath) {
  const spec = options.source === 'index' ? `:${filePath}` : `${options.ref}:${filePath}`;
  const oid = runGit(['rev-parse', '--verify', spec], { encoding: 'utf8' }).trim();
  return objectBytes(oid);
}

function sha256(bytes) {
  return crypto.createHash('sha256').update(bytes).digest('hex');
}

function manifestMap(bytes) {
  const map = new Map();
  for (const line of bytes.toString('utf8').split(/\r?\n/).filter(Boolean)) {
    const match = line.match(/^([0-9a-f]{64})\s+(.+)$/);
    if (match) map.set(match[2], match[1]);
  }
  return map;
}

export function generateManifest(options) {
  const entries = normalizedEntries(options);
  const lines = entries.map((entry) => `${sha256(objectBytes(entry.oid))}  ${entry.path}`);
  const manifest = Buffer.from(`${lines.join('\n')}\n`, 'utf8');
  const self = Buffer.from(`${sha256(manifest)}  ${MANIFEST_PATH}\n`, 'utf8');
  return { entries, manifest, self };
}

function checkStored(options, generated) {
  const storedManifest = sourceFileBytes(options, MANIFEST_PATH);
  const storedSelf = sourceFileBytes(options, SELF_PATH);
  const errors = [];
  if (!storedManifest.equals(generated.manifest)) errors.push('GENERATED_MANIFEST_MISMATCH');
  if (!storedSelf.equals(generated.self)) errors.push('GENERATED_MANIFEST_SELF_MISMATCH');
  if (errors.length) {
    const stored = manifestMap(storedManifest);
    const expected = manifestMap(generated.manifest);
    const paths = new Set([...stored.keys(), ...expected.keys()]);
    const entryDiffs = [...paths].sort().flatMap((filePath) => {
      const storedHash = stored.get(filePath) || null;
      const expectedHash = expected.get(filePath) || null;
      return storedHash === expectedHash ? [] : [{ path: filePath, stored: storedHash, expected: expectedHash }];
    });
    console.error(JSON.stringify({
      status: 'FAIL',
      source: options.source,
      ref: options.ref,
      errors,
      entryDiffs,
      expectedManifestSha256: sha256(generated.manifest),
      expectedSelfLine: generated.self.toString('utf8').trim()
    }, null, 2));
    process.exit(1);
  }
}

const options = parseArgs(process.argv.slice(2));
const generated = generateManifest(options);
if (options.manifestOut) fs.writeFileSync(options.manifestOut, generated.manifest);
if (options.selfOut) fs.writeFileSync(options.selfOut, generated.self);
if (options.check) checkStored(options, generated);
if (!options.manifestOut && !options.check) process.stdout.write(generated.manifest);
console.error(JSON.stringify({
  status: 'PASS',
  source: options.source,
  ref: options.ref,
  entries: generated.entries.length,
  manifestSha256: sha256(generated.manifest)
}, null, 2));
