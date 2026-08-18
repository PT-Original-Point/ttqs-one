import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {
  REQUIRED_PRODUCT_MARKERS,
  normalizeAppsScriptHtmlServiceWrapper,
  classifyExternalBlackbox
} from '../scripts/external-blackbox-classifier.mjs';

const rawProduct = REQUIRED_PRODUCT_MARKERS.join(' | ');
const wrappedProduct = rawProduct.replace('19 / 19', '19 \\/ 19');

test('raw external product markers pass', () => {
  assert.equal(classifyExternalBlackbox(rawProduct).pass, true);
});

test('Apps Script HtmlService escaped slash is normalized before marker classification', () => {
  assert.match(wrappedProduct, /19 \\\/ 19/);
  assert.match(normalizeAppsScriptHtmlServiceWrapper(wrappedProduct), /19 \/ 19/);
  assert.equal(classifyExternalBlackbox(wrappedProduct).pass, true);
});

test('hex and unicode escaped slash variants are normalized', () => {
  assert.equal(classifyExternalBlackbox(rawProduct.replace('19 / 19', '19 \\x2f 19')).pass, true);
  assert.equal(classifyExternalBlackbox(rawProduct.replace('19 / 19', '19 \\u002F 19')).pass, true);
});

test('missing required product marker fails closed', () => {
  const result = classifyExternalBlackbox(rawProduct.replace('查看佐證與來源', ''));
  assert.equal(result.pass, false);
  assert.deepEqual(result.missing, ['查看佐證與來源']);
});

test('friendly application error page fails closed even if other markers are present', () => {
  const result = classifyExternalBlackbox(`${rawProduct} 目前無法載入唯讀快照`);
  assert.equal(result.pass, false);
  assert.equal(result.friendlyError, true);
});

test('CLI returns PASS for HtmlService wrapper encoding', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ttqs-blackbox-'));
  const file = path.join(dir, 'page.html');
  try {
    fs.writeFileSync(file, wrappedProduct);
    const result = spawnSync(process.execPath, ['scripts/external-blackbox-classifier.mjs', '--html', file], {encoding: 'utf8'});
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /BLACKBOX_MARKERS_PASS/);
  } finally {
    fs.rmSync(dir, {recursive: true, force: true});
  }
});
