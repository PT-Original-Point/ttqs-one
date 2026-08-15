import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import crypto from 'node:crypto';

const source = fs.readFileSync('apps-script/Schema.gs', 'utf8');
const config = fs.readFileSync('apps-script/Config.gs', 'utf8');

function functionBody(name) {
  const match = source.match(new RegExp(`function ${name}\\([^)]*\\) \\{([\\s\\S]*?)\\n\\}`));
  assert.ok(match, `${name} must exist`);
  return match[1];
}

test('Observation source parses', () => new vm.Script(source, { filename: 'Schema.gs' }));

test('Observation shadow mode and temporary sheet are explicit', () => {
  assert.match(config, /OBSERVATION_SHADOW_MODE: true/);
  assert.match(config, /OBSERVATION: '17_Observation_原始收件索引'/);
});

test('source identity function has no row-number or locator argument', () => {
  assert.match(source, /function ttqsObservationSourceKey_\(kind, formId, providerTimestamp, payloadHash\)/);
});

test('source key is stable for provider identity inputs', () => {
  const context = {
    ttqsDigest_: (value) => crypto.createHash('sha256').update(String(value)).digest('hex')
  };
  vm.createContext(context);
  vm.runInContext(source, context);
  const a = context.ttqsObservationSourceKey_('NEEDS', 'FORM-1', '2026-08-15T00:00:00.001Z', 'abc');
  const b = context.ttqsObservationSourceKey_('NEEDS', 'FORM-1', '2026-08-15T00:00:00.001Z', 'abc');
  assert.equal(a, b);
});

test('raw candidate builders never write to linked raw sheet', () => {
  const rowBody = functionBody('ttqsObservationCandidateFromRow_');
  const valuesBody = functionBody('ttqsObservationCandidateFromValues_');
  assert.doesNotMatch(rowBody, /\.setValue|\.setValues|appendRow|ttqsEnsureEventId_/);
  assert.doesNotMatch(valuesBody, /\.setValue|\.setValues|appendRow|ttqsEnsureEventId_/);
  assert.match(valuesBody, /source_locator:/);
});

test('source-key collision and raw mutation fail into quarantine', () => {
  assert.match(source, /SOURCE_KEY_COLLISION/);
  assert.match(source, /RAW_MUTATION_DETECTED/);
  assert.match(source, /processing_status = 'QUARANTINED'/);
});

test('scheduler scans before acquiring short write lock', () => {
  const body = functionBody('ttqsScheduler');
  assert.match(body, /var scan = ttqsObservationScanRaw_\(\);/);
  assert.match(body, /ttqsWithScriptLock_\(function\(\) \{ return ttqsObservationApplyCandidates_\(scan\.candidates\); \}\)/);
});

test('shadow scheduler does not invoke legacy processing or ledger', () => {
  assert.doesNotMatch(source, /ttqsProcessSubmission_|ttqsLedgerEnsure_|ttqsLedgerStart_|ttqsWriteSurvey_/);
  assert.match(source, /legacy_processing_unchanged: true/);
});

test('reconciliation exposes required hard conditions', () => {
  assert.match(source, /unexplained:/);
  assert.match(source, /unknown_internal:/);
  assert.match(source, /formal_duplicate_acceptance:/);
  assert.match(source, /PASS_WITH_QUARANTINE/);
});
