import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const workflow = fs.readFileSync('.github/workflows/deploy-external-test.yml', 'utf8');

test('successful anonymous product probe writes per-marker evidence before PASS can be published', () => {
  assert.match(workflow, /--evidence-out external-blackbox-marker-evidence\.json/);
  assert.match(workflow, /rm -f external-page\.html external-blackbox-marker-evidence\.json/);
  const probe = workflow.indexOf('- name: Anonymous product black-box probe');
  const upload = workflow.indexOf('- name: Preserve per-marker black-box evidence');
  const publish = workflow.indexOf('- name: Publish durable deployment receipt after black-box PASS');
  assert.ok(probe >= 0 && upload > probe && publish > upload);
});

test('per-marker evidence is durably uploaded with pinned GitHub artifact action', () => {
  assert.match(workflow, /actions\/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a/);
  assert.match(workflow, /name: external-blackbox-marker-evidence-\$\{\{ github\.run_id \}\}/);
  assert.match(workflow, /path: external-blackbox-marker-evidence\.json/);
  assert.match(workflow, /if-no-files-found: error/);
  assert.match(workflow, /retention-days: 30/);
});
