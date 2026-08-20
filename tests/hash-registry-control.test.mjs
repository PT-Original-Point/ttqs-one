import test from 'node:test';
import assert from 'node:assert/strict';
import { normalizeRegistry, resolveRegisteredHash, verifyReportedHashes } from '../scripts/hash-registry-control.mjs';

const goodHash = 'a'.repeat(64);
const otherHash = 'b'.repeat(64);
const registryInput = {
  entries: [
    {
      registry_id: 'HR-TEST-001',
      computed_hash: `sha256:${goodHash}`,
      readback_status: 'READBACK_MATCHED_COMPUTED'
    },
    {
      registry_id: 'HR-UNVERIFIED',
      computed_hash: `sha256:${otherHash}`,
      readback_status: 'PENDING'
    }
  ]
};

test('registry resolver returns only readback-matched authoritative hash', () => {
  const registry = normalizeRegistry(registryInput);
  assert.equal(resolveRegisteredHash(registry, 'HR-TEST-001'), `sha256:${goodHash}`);
  assert.throws(() => resolveRegisteredHash(registry, 'HR-UNVERIFIED'), /not found or not readback-matched/);
});

test('report verifier passes registered values and rejects unanchored 64-hex values', () => {
  const registry = normalizeRegistry(registryInput);
  const pass = verifyReportedHashes(registry, `verified sha256:${goodHash}`, 'TEST');
  assert.equal(pass.status, 'PASS');
  assert.equal(pass.anchored[0].registry_id, 'HR-TEST-001');

  const fail = verifyReportedHashes(registry, `wrong sha256:${otherHash}`, 'TEST');
  assert.equal(fail.status, 'FAIL');
  assert.equal(fail.unanchored[0].status, 'UNANCHORED_HASH');
  assert.equal(fail.gap_events.length, 1);
});

test('40-hex Git commit ids are not treated as SHA-256 report values', () => {
  const registry = normalizeRegistry(registryInput);
  const result = verifyReportedHashes(registry, 'commit dc33165ce29de995a1e9740bb92784f8b7224c1f', 'TEST');
  assert.equal(result.status, 'PASS');
  assert.equal(result.scanned, 0);
});
