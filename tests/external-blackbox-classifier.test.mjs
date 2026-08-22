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
const wrappedProduct = rawProduct
  .replace('19 / 19', '19 \\/ 19')
  .replace('AttemptHistory=append-only', 'AttemptHistory\\x3dappend-only');

const D8_ACCEPTANCE_MARKERS = [
  '官方 19 指標評核語意導航',
  '12a 學員遴選',
  '12e 教學環境與設備',
  '17a 反應評估',
  '17d 成果評估',
  'SAMPLE 評核因果鏈',
  '四類 TEST Google Forms 生命週期',
  '4/4 類別都有 ACCEPTED 來源',
  '故障 → 重試 → 對帳 → FINAL_ACCEPTED',
  'MATCHED_EXACTLY_ONCE',
  'AttemptHistory=append-only',
  '19 指標佐證與來源下鑽',
  'Google Drive 連結只是選配，不是顧問調閱成功的必要條件',
  '不在執行期呼叫 Google Sheets／Drive API',
  '本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL'
];

test('raw external product markers pass', () => {
  assert.equal(classifyExternalBlackbox(rawProduct).pass, true);
});

test('blackbox contract explicitly covers D8 consultant acceptance semantics', () => {
  for (const marker of D8_ACCEPTANCE_MARKERS) {
    assert.ok(REQUIRED_PRODUCT_MARKERS.includes(marker), `missing D8 blackbox contract marker: ${marker}`);
  }
});

test('Apps Script HtmlService escaped slash and equals are normalized before marker classification', () => {
  assert.match(wrappedProduct, /19 \\\/ 19/);
  assert.match(wrappedProduct, /AttemptHistory\\x3dappend-only/);
  const normalized = normalizeAppsScriptHtmlServiceWrapper(wrappedProduct);
  assert.match(normalized, /19 \/ 19/);
  assert.match(normalized, /AttemptHistory=append-only/);
  assert.equal(classifyExternalBlackbox(wrappedProduct).pass, true);
});

test('observed HtmlService attribute quote codepoints 005C 005C 0022 normalize exactly without escape-syntax ambiguity', () => {
  const observedQuote = String.fromCharCode(92, 92, 34);
  assert.deepEqual(Array.from(observedQuote, ch => ch.codePointAt(0)), [92, 92, 34]);
  const observed = `data-matrix-indicator=${observedQuote}1${observedQuote} href=${observedQuote}https://script.google.com/macros/s/DEMO/exec?indicator=1${observedQuote}`;
  const normalized = normalizeAppsScriptHtmlServiceWrapper(observed);
  assert.equal(normalized, 'data-matrix-indicator="1" href="https://script.google.com/macros/s/DEMO/exec?indicator=1"');
  assert.equal(normalized.includes('data-matrix-indicator="1"'), true);
  assert.equal(normalized.includes('?indicator=1'), true);
  assert.equal(normalized.includes(observedQuote), false);
});

test('hex, unicode and HTML entity escaped slash/equals variants are normalized', () => {
  assert.equal(classifyExternalBlackbox(rawProduct.replace('19 / 19', '19 \\x2f 19')).pass, true);
  assert.equal(classifyExternalBlackbox(rawProduct.replace('19 / 19', '19 \\u002F 19')).pass, true);
  for (const escaped of ['AttemptHistory\\x3Dappend-only', 'AttemptHistory\\u003dappend-only', 'AttemptHistory&#61;append-only', 'AttemptHistory&#x3D;append-only', 'AttemptHistory&equals;append-only']) {
    assert.equal(classifyExternalBlackbox(rawProduct.replace('AttemptHistory=append-only', escaped)).pass, true, escaped);
  }
});

test('every required product marker independently fails closed when missing', () => {
  for (const marker of REQUIRED_PRODUCT_MARKERS) {
    const result = classifyExternalBlackbox(rawProduct.replace(marker, ''));
    assert.equal(result.pass, false, `classifier must fail when marker is absent: ${marker}`);
    assert.ok(result.missing.includes(marker), `missing list must identify absent marker: ${marker}`);
  }
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
