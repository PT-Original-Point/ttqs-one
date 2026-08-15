import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('apps-script/ConsultView.gs', 'utf8');

function functionBody(name) {
  const match = source.match(new RegExp(`function ${name}\\([^)]*\\) \\{([\\s\\S]*?)\\n\\}`));
  assert.ok(match, `${name} must exist`);
  return match[1];
}

test('ConsultView remains valid JavaScript', () => {
  new vm.Script(source, { filename: 'ConsultView.gs' });
});

test('launcher resolves existing runtime form IDs without creating forms', () => {
  const body = functionBody('ttqsWebFormLaunchModel_');
  assert.match(body, /TTQS_FORM_' \+ kind \+ '_ID/);
  assert.match(body, /FormApp\.openById\(formId\)/);
  assert.match(body, /form\.getPublishedUrl\(\)/);
  assert.doesNotMatch(body, /ttqsEnsureOneForm_|FormApp\.create|setPublished|setDestination/);
});

test('all four SAMPLE flow entry points are present', () => {
  for (const token of ['NEEDS', 'REGISTRATION', 'REACTION', 'FOLLOWUP30']) assert.match(source, new RegExp(token));
  for (const label of ['需求調查', '課程報名', '課後滿意度', '30 日追蹤']) assert.match(source, new RegExp(label));
});

test('form launch links use native external navigation and no web write bridge', () => {
  assert.match(source, /target="_blank" rel="noopener noreferrer"/);
  assert.match(source, /Google Forms 原生填答頁面/);
  assert.doesNotMatch(source, /google\.script\.run/);
});

test('external preview receives no internal form launchers or health summary', () => {
  const body = functionBody('ttqsWebDashboardModel_');
  assert.match(body, /formLaunchers: view === 'INTERNAL' \? ttqsWebFormLaunchModel_\(\) : \[\]/);
  assert.match(body, /health: view === 'INTERNAL' \? ttqsWebHealthSummary_\(\) : null/);
});

test('health summary exposes counts, not internal failure payloads', () => {
  const body = functionBody('ttqsWebHealthSummary_');
  assert.match(body, /state:/);
  assert.match(body, /total:/);
  assert.match(body, /failed:/);
  const renderBody = functionBody('ttqsWebFormLaunchHtml_');
  assert.doesNotMatch(renderBody, /last_error|error_message|failed\[|actual/);
});
