import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {
  R7_REQUIRED_PRODUCT_MARKERS,
  evaluateExternalBlackbox
} from '../scripts/external-blackbox-classifier.mjs';

const rawR7Product = R7_REQUIRED_PRODUCT_MARKERS.join(' | ');

test('R7 successful black-box result carries auditable per-marker evidence and derives total PASS from details', () => {
  const result = evaluateExternalBlackbox(rawR7Product);
  assert.equal(result.pass, true);
  assert.equal(result.mode, 'R7_DRAFT003');
  assert.equal(result.evidenceMode, 'R7_DRAFT003');
  assert.equal(result.markerEvidence.length, R7_REQUIRED_PRODUCT_MARKERS.length);

  for (let index = 0; index < result.markerEvidence.length; index += 1) {
    const row = result.markerEvidence[index];
    assert.equal(row.markerId, `R7_DRAFT003-M${String(index + 1).padStart(2, '0')}`);
    assert.equal(row.expected, R7_REQUIRED_PRODUCT_MARKERS[index]);
    assert.equal(row.actual, row.expected);
    assert.equal(row.result, 'PASS');
    assert.equal(row.evidence.matchType, 'NORMALIZED_SUBSTRING');
    assert.ok(row.evidence.normalizedIndex >= 0);
    assert.ok(row.evidence.excerpt.includes(row.expected));
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
  assert.equal(result.derivation.markerPassCount, R7_REQUIRED_PRODUCT_MARKERS.length);
  assert.equal(result.derivation.markerTotal, R7_REQUIRED_PRODUCT_MARKERS.length);
  assert.equal(result.derivation.selectedContractPass, true);
  assert.equal(result.derivation.safetyPass, true);
  assert.equal(result.derivation.acceptedContractPass, true);
  assert.equal(result.derivation.totalPass, true);
  assert.equal(
    result.derivation.totalPass,
    result.markerEvidence.every(row => row.result === 'PASS') && result.safetyEvidence.result === 'PASS'
  );
});

test('missing R7 marker has expected actual FAIL and direct negative evidence without weakening fail-closed', () => {
  const missingMarker = R7_REQUIRED_PRODUCT_MARKERS[4];
  const result = evaluateExternalBlackbox(rawR7Product.replace(missingMarker, ''));
  const row = result.markerEvidence.find(item => item.expected === missingMarker);
  assert.equal(result.pass, false);
  assert.equal(result.evidenceMode, 'R7_DRAFT003');
  assert.ok(row);
  assert.equal(row.actual, null);
  assert.equal(row.result, 'FAIL');
  assert.equal(row.evidence.normalizedIndex, -1);
  assert.equal(row.evidence.excerpt, null);
  assert.ok(result.missing.includes(missingMarker));
  assert.equal(result.derivation.totalPass, false);
});

test('friendly error safety detail fails total result even when every R7 marker passes', () => {
  const result = evaluateExternalBlackbox(`${rawR7Product} 目前無法載入唯讀快照`);
  assert.equal(result.mode, 'R7_DRAFT003');
  assert.equal(result.markerEvidence.every(row => row.result === 'PASS'), true);
  assert.equal(result.safetyEvidence.expected, 'ABSENT');
  assert.equal(result.safetyEvidence.actual, '目前無法載入唯讀快照');
  assert.equal(result.safetyEvidence.result, 'FAIL');
  assert.equal(result.derivation.selectedContractPass, true);
  assert.equal(result.derivation.safetyPass, false);
  assert.equal(result.derivation.totalPass, false);
  assert.equal(result.pass, false);
});

test('CLI persists TTQS_BLACKBOX_MARKER_EVIDENCE_V1 with expected actual PASS-FAIL evidence details', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-marker-evidence-'));
  const html = path.join(dir, 'page.html');
  const evidence = path.join(dir, 'marker-evidence.json');
  try {
    fs.writeFileSync(html, rawR7Product, 'utf8');
    const run = spawnSync(process.execPath, [
      'scripts/external-blackbox-classifier.mjs',
      '--html', html,
      '--evidence-out', evidence
    ], {encoding: 'utf8'});
    assert.equal(run.status, 0, run.stderr);
    assert.match(run.stdout, /BLACKBOX_MARKER_DETAIL/);
    assert.match(run.stdout, /BLACKBOX_SAFETY_DETAIL/);
    assert.match(run.stdout, /BLACKBOX_MARKERS_PASS mode=R7_DRAFT003 markers=11\/11 safety=PASS/);

    const receipt = JSON.parse(fs.readFileSync(evidence, 'utf8'));
    assert.equal(receipt.schema, 'TTQS_BLACKBOX_MARKER_EVIDENCE_V1');
    assert.equal(receipt.mode, 'R7_DRAFT003');
    assert.equal(receipt.evidenceMode, 'R7_DRAFT003');
    assert.equal(receipt.markerEvidence.length, 11);
    assert.equal(receipt.markerEvidence.every(row => row.expected === row.actual && row.result === 'PASS'), true);
    assert.equal(receipt.markerEvidence.every(row => row.evidence.normalizedIndex >= 0 && row.evidence.excerpt.includes(row.expected)), true);
    assert.equal(receipt.safetyEvidence.result, 'PASS');
    assert.equal(receipt.derivation.totalPass, true);
  } finally {
    fs.rmSync(dir, {recursive: true, force: true});
  }
});
