import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {
  REQUIRED_PRODUCT_MARKERS,
  R7_REQUIRED_PRODUCT_MARKERS,
  evaluateExternalBlackbox
} from '../scripts/external-blackbox-classifier.mjs';

const rawR2Product = REQUIRED_PRODUCT_MARKERS.join(' | ');
const rawR7Diagnostics = R7_REQUIRED_PRODUCT_MARKERS.join(' | ');
const rawD003Product = `${rawR2Product} | ${rawR7Diagnostics}`;

const R2_SAFETY_MARKER_IDS = new Map([
  ['G02-M01', REQUIRED_PRODUCT_MARKERS[0]],
  ['G02-M17', REQUIRED_PRODUCT_MARKERS[16]],
  ['G02-M18', REQUIRED_PRODUCT_MARKERS[17]],
  ['G02-M19', REQUIRED_PRODUCT_MARKERS[18]]
]);

test('R2 successful black-box result carries all 19 auditable required markers and derives total PASS only from them plus safety', () => {
  const result = evaluateExternalBlackbox(rawD003Product);
  assert.equal(result.pass, true);
  assert.equal(result.mode, 'R7_DRAFT003');
  assert.equal(result.contractId, 'R2_G02_19_REQUIRED');
  assert.equal(result.evidenceMode, 'R2_G02_19_REQUIRED');
  assert.equal(result.markerEvidence.length, 19);

  for (let index = 0; index < result.markerEvidence.length; index += 1) {
    const row = result.markerEvidence[index];
    assert.equal(row.markerId, `G02-M${String(index + 1).padStart(2, '0')}`);
    assert.equal(row.expected, REQUIRED_PRODUCT_MARKERS[index]);
    assert.equal(row.actual, row.expected);
    assert.equal(row.result, 'PASS');
    assert.equal(row.evidence.matchType, 'NORMALIZED_SUBSTRING');
    assert.ok(row.evidence.normalizedIndex >= 0);
    assert.ok(row.evidence.excerpt.includes(row.expected));
  }

  for (const [markerId, expected] of R2_SAFETY_MARKER_IDS) {
    const row = result.markerEvidence.find(item => item.markerId === markerId);
    assert.ok(row, `${markerId} must remain required`);
    assert.equal(row.expected, expected);
    assert.equal(row.result, 'PASS');
  }

  assert.deepEqual(result.safetyEvidence, {
    checkId: 'FRIENDLY_ERROR_ABSENT',
    expected: 'ABSENT',
    actual: 'ABSENT',
    result: 'PASS',
    evidence: {
      matchType: 'NEGATIVE_NORMALIZED_SUBSTRING_CHECK',
      normalizedIndex: -1,
      excerpt: null
    }
  });
  assert.equal(result.derivation.markerPassCount, 19);
  assert.equal(result.derivation.markerTotal, 19);
  assert.equal(result.derivation.requiredContractPass, true);
  assert.equal(result.derivation.acceptedContractPass, true);
  assert.equal(result.derivation.safetyPass, true);
  assert.equal(result.derivation.totalPass, true);
  assert.equal(
    result.derivation.totalPass,
    result.markerEvidence.every(row => row.result === 'PASS') && result.safetyEvidence.result === 'PASS'
  );
});

test('R7 11 diagnostics alone can never substitute for the R2 19-marker acceptance contract', () => {
  const result = evaluateExternalBlackbox(rawR7Diagnostics);
  assert.equal(result.mode, 'R7_DRAFT003');
  assert.equal(result.r7InterfaceEvidence.every(row => row.result === 'PASS'), true);
  assert.equal(result.derivation.r7DiagnosticsPass, true);
  assert.equal(result.derivation.requiredContractPass, false);
  assert.equal(result.markerEvidence.length, 19);
  assert.equal(result.markerEvidence.every(row => row.result === 'FAIL'), true);
  assert.equal(result.pass, false);
});

test('each R2 safety marker M01 M17 M18 M19 independently fails closed when missing', () => {
  for (const [markerId, marker] of R2_SAFETY_MARKER_IDS) {
    const result = evaluateExternalBlackbox(rawD003Product.replace(marker, ''));
    const row = result.markerEvidence.find(item => item.markerId === markerId);
    assert.ok(row);
    assert.equal(row.actual, 'MISSING');
    assert.equal(row.result, 'FAIL');
    assert.equal(result.pass, false, `${markerId} must fail closed`);
  }
});

test('missing required R2 marker records expected actual=MISSING FAIL and direct negative evidence', () => {
  const missingMarker = REQUIRED_PRODUCT_MARKERS[8];
  const result = evaluateExternalBlackbox(rawD003Product.replace(missingMarker, ''));
  const row = result.markerEvidence.find(item => item.expected === missingMarker);
  assert.equal(result.pass, false);
  assert.equal(result.evidenceMode, 'R2_G02_19_REQUIRED');
  assert.ok(row);
  assert.equal(row.actual, 'MISSING');
  assert.equal(row.result, 'FAIL');
  assert.equal(row.evidence.normalizedIndex, -1);
  assert.equal(row.evidence.excerpt, null);
  assert.ok(result.missing.includes(missingMarker));
  assert.equal(result.derivation.totalPass, false);
});

test('friendly error safety detail fails total result even when all R2 markers pass', () => {
  const result = evaluateExternalBlackbox(`${rawD003Product} 目前無法載入唯讀快照`);
  assert.equal(result.markerEvidence.every(row => row.result === 'PASS'), true);
  assert.equal(result.safetyEvidence.expected, 'ABSENT');
  assert.equal(result.safetyEvidence.actual, '目前無法載入唯讀快照');
  assert.equal(result.safetyEvidence.result, 'FAIL');
  assert.equal(result.derivation.requiredContractPass, true);
  assert.equal(result.derivation.safetyPass, false);
  assert.equal(result.derivation.totalPass, false);
  assert.equal(result.pass, false);
});

test('CLI persists V2 R2 G-02 evidence with 19 exact IDs and derived PASS', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-marker-evidence-'));
  const html = path.join(dir, 'page.html');
  const evidence = path.join(dir, 'marker-evidence.json');
  try {
    fs.writeFileSync(html, rawD003Product, 'utf8');
    const run = spawnSync(process.execPath, [
      'scripts/external-blackbox-classifier.mjs',
      '--html', html,
      '--evidence-out', evidence
    ], {encoding: 'utf8'});
    assert.equal(run.status, 0, run.stderr);
    assert.match(run.stdout, /BLACKBOX_MARKER_DETAIL/);
    assert.match(run.stdout, /BLACKBOX_SAFETY_DETAIL/);
    assert.match(run.stdout, /BLACKBOX_MARKERS_PASS contract=R2_G02_19_REQUIRED markers=19\/19 safety=PASS mode=R7_DRAFT003/);

    const receipt = JSON.parse(fs.readFileSync(evidence, 'utf8'));
    assert.equal(receipt.schema, 'TTQS_BLACKBOX_MARKER_EVIDENCE_V2');
    assert.equal(receipt.contractId, 'R2_G02_19_REQUIRED');
    assert.equal(receipt.mode, 'R7_DRAFT003');
    assert.equal(receipt.evidenceMode, 'R2_G02_19_REQUIRED');
    assert.equal(receipt.markerEvidence.length, 19);
    assert.deepEqual(receipt.markerEvidence.map(row => row.markerId), Array.from({length: 19}, (_, index) => `G02-M${String(index + 1).padStart(2, '0')}`));
    assert.equal(receipt.markerEvidence.every(row => row.expected === row.actual && row.result === 'PASS'), true);
    assert.equal(receipt.markerEvidence.every(row => row.evidence.normalizedIndex >= 0 && row.evidence.excerpt.includes(row.expected)), true);
    assert.equal(receipt.safetyEvidence.result, 'PASS');
    assert.equal(receipt.derivation.markerPassCount, 19);
    assert.equal(receipt.derivation.markerTotal, 19);
    assert.equal(receipt.derivation.requiredContractPass, true);
    assert.equal(receipt.derivation.totalPass, true);
  } finally {
    fs.rmSync(dir, {recursive: true, force: true});
  }
});
