import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import crypto from 'node:crypto';

const source = fs.readFileSync('apps-script/Schema.gs', 'utf8');

function functionBody(name) {
  const match = source.match(new RegExp(`function ${name}\\([^)]*\\) \\{([\\s\\S]*?)\\n\\}`));
  assert.ok(match, `${name} must exist`);
  return match[1];
}

test('Schema parses after batch-scan optimization', () => {
  new vm.Script(source, { filename: 'Schema.gs' });
});

test('batch scanner never calls per-row candidate reader', () => {
  const body = functionBody('ttqsObservationScanRaw_');
  assert.doesNotMatch(body, /ttqsObservationCandidateFromRow_\s*\(/);
  assert.match(body, /ttqsObservationCandidateFromValues_\s*\(/);
  assert.match(body, /readStrategy: 'BATCH_PER_SOURCE'/);
});

test('each non-empty source uses one header range plus one data range', () => {
  const body = functionBody('ttqsObservationScanRaw_');
  assert.match(body, /var headers = sheet\.getRange\(1, 1, 1, lastColumn\)/);
  assert.match(body, /var dataRange = sheet\.getRange\(2, 1, rows, lastColumn\)/);
  assert.match(body, /var valueRows = dataRange\.getValues\(\)/);
  assert.match(body, /var displayRows = dataRange\.getDisplayValues\(\)/);
  assert.match(body, /range_read_calls: 3/);
});

test('in-memory candidate builder performs no sheet reads or writes', () => {
  const body = functionBody('ttqsObservationCandidateFromValues_');
  assert.doesNotMatch(body, /getRange|getValues|getDisplayValues|setValue|setValues|appendRow/);
});

test('row locator changes do not alter source identity', () => {
  const context = {
    Utilities: {
      getUuid: () => '00000000-0000-4000-8000-000000000001',
      formatDate: (value) => new Date(value).toISOString()
    },
    ttqsCanonicalFieldCode_: (header) => String(header),
    ttqsExpectedFieldCodes_: () => ['Timestamp', 'Q1'],
    ttqsDigest_: (value) => crypto.createHash('sha256').update(String(value)).digest('hex'),
    ttqsStableId_: (prefix) => `${prefix}stable`,
    ttqsNow_: () => '2026-08-15T00:00:01.000Z'
  };
  vm.createContext(context);
  vm.runInContext(source, context);
  const headers = ['Timestamp', 'Q1', 'TTQS_EVENT_ID'];
  const display = ['2026/08/15 08:00:00', 'A', 'legacy-id'];
  const timestamp = new Date('2026-08-15T00:00:00.000Z');
  const first = context.ttqsObservationCandidateFromValues_(101, 2, 'NEEDS', 'FORM-1', headers, display, timestamp);
  const moved = context.ttqsObservationCandidateFromValues_(101, 999, 'NEEDS', 'FORM-1', headers, display, timestamp);
  assert.equal(first.source_key, moved.source_key);
  assert.equal(first.payload_hash, moved.payload_hash);
  assert.notEqual(first.source_locator, moved.source_locator);
});

test('scheduler exposes benchmark timings and RPC-read strategy', () => {
  const body = functionBody('ttqsScheduler');
  assert.match(body, /read_strategy: scan\.readStrategy/);
  assert.match(body, /range_read_calls: scan\.rangeReadCalls/);
  assert.match(body, /timings_ms:/);
  assert.match(body, /scan: scannedAt - startedAt/);
  assert.match(body, /ingest: ingestedAt - scannedAt/);
  assert.match(body, /reconcile: reconciledAt - ingestedAt/);
  assert.match(body, /total: reconciledAt - startedAt/);
});
