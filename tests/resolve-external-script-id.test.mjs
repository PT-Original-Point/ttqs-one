import test from 'node:test';
import assert from 'node:assert/strict';
import { resolveExternalScriptId } from '../scripts/resolve-external-script-id.mjs';

const title = 'TTQS ONE TEST External Evaluator Portal';
const id = 'A'.repeat(30);

test('resolves clasp list-scripts en dash output', () => {
  assert.equal(resolveExternalScriptId(`${title} – ${id}\nOther – ${'B'.repeat(30)}\n`, title), id);
});

test('resolves hyphen variants and deduplicates same id', () => {
  assert.equal(resolveExternalScriptId(`${title} - ${id}\n${title} — ${id}\n`, title), id);
});

test('returns empty when no exact title exists', () => {
  assert.equal(resolveExternalScriptId(`TTQS ONE TEST External Evaluator Portal old – ${id}\n`, title), '');
});

test('fails closed on ambiguous exact title ids', () => {
  assert.throws(() => resolveExternalScriptId(`${title} – ${id}\n${title} – ${'C'.repeat(30)}\n`, title), /EXTERNAL_SCRIPT_TITLE_AMBIGUOUS/);
});

test('requires title', () => {
  assert.throws(() => resolveExternalScriptId('', ''), /EXTERNAL_SCRIPT_TITLE_REQUIRED/);
});
