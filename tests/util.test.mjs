import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const sandbox = {
  Utilities: {
    DigestAlgorithm: { SHA_256: 'SHA_256' },
    Charset: { UTF_8: 'UTF_8' },
    computeDigest() { return Array.from({ length: 32 }, (_, i) => i - 16); },
    formatDate() { return '2026-08-11'; }
  },
  isFinite,
  Date,
  JSON,
  Object,
  String,
  Number,
  RegExp
};
vm.createContext(sandbox);
for (const file of ['Config.gs', 'Util.gs']) {
  vm.runInContext(fs.readFileSync(`apps-script/${file}`, 'utf8'), sandbox, { filename: file });
}

test('sample alias accepts synthetic alias', () => assert.equal(sandbox.ttqsRequireSampleAlias_('s-l06'), 'S-L06'));
test('sample alias rejects missing S prefix', () => assert.throws(() => sandbox.ttqsRequireSampleAlias_('L06')));
test('sample alias rejects email', () => assert.throws(() => sandbox.ttqsRequireSampleAlias_('a@b.com')));
test('number accepts lower bound', () => assert.equal(sandbox.ttqsNumber_('1', 1, 5), 1));
test('number accepts upper bound', () => assert.equal(sandbox.ttqsNumber_('5', 1, 5), 5));
test('number rejects zero', () => assert.throws(() => sandbox.ttqsNumber_('0', 1, 5)));
test('number rejects non number', () => assert.throws(() => sandbox.ttqsNumber_('x', 1, 5)));
test('redact email', () => assert.match(sandbox.ttqsRedactFreeText_('mail x@y.com ok'), /REDACTED_EMAIL/));
test('redact taiwan mobile', () => assert.match(sandbox.ttqsRedactFreeText_('0912-345-678'), /REDACTED_PHONE/));
test('redact long numeric token', () => assert.match(sandbox.ttqsRedactFreeText_('12345678'), /REDACTED_NUMBER/));
test('unique removes duplicates', () => assert.deepEqual(Array.from(sandbox.ttqsUnique_(['A', 'A', 'B'])), ['A', 'B']));
test('stable id has prefix', () => assert.match(sandbox.ttqsStableId_('X-', 'a', 8), /^X-[0-9A-F]{8}$/));
