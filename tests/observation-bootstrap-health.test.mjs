import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const bootstrap = fs.readFileSync('apps-script/Bootstrap.gs', 'utf8');
const health = fs.readFileSync('apps-script/Health.gs', 'utf8');

test('modified Apps Script sources parse', () => {
  new vm.Script(bootstrap, { filename: 'Bootstrap.gs' });
  new vm.Script(health, { filename: 'Health.gs' });
});

test('Observation schema is ensured before bootstrap pre-health', () => {
  const ensureAt = bootstrap.indexOf('ttqsEnsureObservationSheet_();');
  const preHealthAt = bootstrap.indexOf('var preHealth = ttqsHealthCheck();');
  assert.ok(ensureAt >= 0 && preHealthAt > ensureAt);
});

test('Observation ensure is shadow-gated and does not run scheduler', () => {
  assert.match(bootstrap, /OBSERVATION_SHADOW_MODE === true/);
  assert.doesNotMatch(bootstrap, /ttqsScheduler\s*\(/);
});

test('managed trigger contract remains legacy four-trigger contract', () => {
  assert.doesNotMatch(bootstrap, /newTrigger\('ttqsScheduler'\)/);
  for (const name of ['ttqsOnSpreadsheetFormSubmit', 'ttqsRetryFailedJobs', 'ttqsReconcile', 'ttqsRefreshConsultView']) {
    assert.match(bootstrap, new RegExp(`newTrigger\\('${name}'\\)`));
  }
});

test('Health requires exact Observation headers in shadow mode', () => {
  assert.match(health, /required\[cfg\.SHEETS\.OBSERVATION\] = ttqsObservationColumns_\(\)\.map/);
});
