import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

const source = fs.readFileSync(new URL('../release/official129/Official129LegacyRegression.gs', import.meta.url), 'utf8');
const canonical = 'TTQS_R3_CANONICAL_EXEC_URL_';

test('R7-NAV-BLOCKER: all Web App navigation is canonical and top-level', () => {
  assert.ok(source.includes('function canonicalUrl_'), 'single canonical URL resolver must exist');
  assert.ok(source.includes(canonical), 'resolver must use canonical /exec constant');
  assert.ok(source.includes('<base target="_top">'), 'page default target must be top-level');
  assert.ok(source.includes('target="_top"'), 'navigation links must explicitly escape Apps Script iframe');
  assert.ok(source.includes('data-top-level-nav="true"'));
  assert.ok(!/<iframe\b[^>]*\bsrc=["'][^"']*script\.google\.com\/macros\/s\//i.test(source), 'must never iframe a script.google.com Web App');
  assert.ok(!/href=["']\?indicator=/i.test(source), 'relative indicator URLs are forbidden');
  assert.ok(!/\/u\/\d+\//.test(source), 'Google multi-login /u/N/ routes are forbidden');
});

test('R7-NAV-BLOCKER: evaluator-facing wording is plain Chinese', () => {
  assert.ok(source.includes('查看文件與證據'));
  assert.ok(source.includes('目前尚未有正式辦訓證據'));
  assert.ok(source.includes('技術細節（管理員用）'));
  assert.ok(!source.includes('查看佐證與來源｜Evidence Matrix'));
});

test('R7-NAV-BLOCKER: indicator page contract includes title and document card', () => {
  assert.ok(source.includes('指標 '+"'+esc_(id)+'"+'｜查看文件與證據'));
  assert.ok(source.includes('data-document-card="true"'));
  assert.ok(source.includes("canonicalUrl_({indicator:id})"));
  assert.ok(source.includes("canonicalUrl_({artifact:x.artifactCode})"));
  assert.ok(!/拒絕連線|refused to connect/i.test(source));
});
