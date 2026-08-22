import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync, spawnSync } from 'node:child_process';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const generator = path.join(repoRoot, 'scripts', 'generate-manifest.mjs');

function git(cwd, args) {
  return execFileSync('git', args, { cwd, encoding: 'utf8' });
}

function node(cwd, args, expectSuccess = true) {
  const result = spawnSync(process.execPath, [generator, ...args], { cwd, encoding: 'utf8' });
  if (expectSuccess && result.status !== 0) {
    throw new Error(`generator failed: ${result.stderr}`);
  }
  return result;
}

function sha256(value) {
  return crypto.createHash('sha256').update(value).digest('hex');
}

function initRepo() {
  const cwd = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-manifest-'));
  git(cwd, ['init', '-q']);
  git(cwd, ['config', 'user.email', 'test@example.invalid']);
  git(cwd, ['config', 'user.name', 'TTQS Test']);
  fs.writeFileSync(path.join(cwd, 'a.txt'), 'committed\n');
  git(cwd, ['add', 'a.txt']);
  git(cwd, ['commit', '-qm', 'initial']);
  return cwd;
}

test('commit mode hashes commit blobs and ignores dirty working-tree bytes', () => {
  const cwd = initRepo();
  const first = node(cwd, ['--ref', 'HEAD']).stdout;
  fs.writeFileSync(path.join(cwd, 'a.txt'), 'dirty working tree\n');
  const second = node(cwd, ['--ref', 'HEAD']).stdout;
  assert.equal(second, first);
});

test('index mode hashes staged blob bytes rather than working-tree bytes', () => {
  const cwd = initRepo();
  const committed = node(cwd, ['--ref', 'HEAD']).stdout;
  fs.writeFileSync(path.join(cwd, 'a.txt'), 'staged bytes\n');
  git(cwd, ['add', 'a.txt']);
  fs.writeFileSync(path.join(cwd, 'a.txt'), 'different unstaged bytes\n');
  const staged = node(cwd, ['--index']).stdout;
  assert.notEqual(staged, committed);
  assert.match(staged, new RegExp(`^${sha256('staged bytes\n')}  a\\.txt`, 'm'));
});

test('manifest paths use NFC, Unicode code-point ordering, and LF line endings', () => {
  const cwd = initRepo();
  const nfdName = `e\u0301.txt`;
  const bmpName = `\uE000.txt`;
  const astralName = `\u{10000}.txt`;
  fs.writeFileSync(path.join(cwd, nfdName), 'nfd\n');
  fs.writeFileSync(path.join(cwd, bmpName), 'bmp\n');
  fs.writeFileSync(path.join(cwd, astralName), 'astral\n');
  git(cwd, ['add', nfdName, bmpName, astralName]);
  git(cwd, ['commit', '-qm', 'unicode paths']);

  const manifest = node(cwd, ['--ref', 'HEAD']).stdout;
  assert.equal(manifest.includes('\r'), false);
  assert.match(manifest, /é\.txt/m);
  assert.equal(manifest.includes(nfdName), false);
  assert.ok(manifest.indexOf(`${bmpName}\n`) < 0 || manifest.indexOf(bmpName) < manifest.indexOf(astralName));
  assert.ok(manifest.indexOf(bmpName) < manifest.indexOf(astralName));
});

test('NFC-normalized path collisions fail closed', () => {
  const cwd = initRepo();
  const nfdName = `e\u0301.txt`;
  const nfcName = `é.txt`;
  fs.writeFileSync(path.join(cwd, nfdName), 'nfd\n');
  fs.writeFileSync(path.join(cwd, nfcName), 'nfc\n');
  git(cwd, ['add', nfdName, nfcName]);
  git(cwd, ['commit', '-qm', 'normalization collision']);

  const result = node(cwd, ['--ref', 'HEAD'], false);
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /NFC_PATH_COLLISION/);
});

test('sidecar hashes exact manifest bytes without circular self-inclusion', () => {
  const cwd = initRepo();
  fs.mkdirSync(path.join(cwd, 'release'));
  const manifestOut = path.join(cwd, 'release', 'MANIFEST.sha256');
  const selfOut = path.join(cwd, 'release', 'MANIFEST.sha256.sha256');
  node(cwd, ['--ref', 'HEAD', '--manifest-out', manifestOut, '--self-out', selfOut]);

  const manifest = fs.readFileSync(manifestOut);
  const sidecar = fs.readFileSync(selfOut, 'utf8');
  assert.equal(manifest.includes(Buffer.from('\r')), false);
  assert.equal(sidecar, `${sha256(manifest)}  release/MANIFEST.sha256\n`);
  assert.equal(manifest.toString('utf8').includes('release/MANIFEST.sha256'), false);
  assert.equal(manifest.toString('utf8').includes('release/MANIFEST.sha256.sha256'), false);
});

test('--check fails closed when committed manifest is stale', () => {
  const cwd = initRepo();
  const manifest = node(cwd, ['--ref', 'HEAD']).stdout;
  fs.mkdirSync(path.join(cwd, 'release'));
  fs.writeFileSync(path.join(cwd, 'release', 'MANIFEST.sha256'), manifest);
  fs.writeFileSync(
    path.join(cwd, 'release', 'MANIFEST.sha256.sha256'),
    `${sha256(manifest)}  release/MANIFEST.sha256\n`
  );
  git(cwd, ['add', 'release']);
  git(cwd, ['commit', '-qm', 'add manifest']);

  fs.writeFileSync(path.join(cwd, 'a.txt'), 'new committed bytes\n');
  git(cwd, ['add', 'a.txt']);
  git(cwd, ['commit', '-qm', 'change without manifest refresh']);

  const result = node(cwd, ['--ref', 'HEAD', '--check'], false);
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /GENERATED_MANIFEST_MISMATCH/);
});
