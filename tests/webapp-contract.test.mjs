import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('apps-script/ConsultView.gs', 'utf8');

test('ConsultView.gs remains valid JavaScript', () => {
  new vm.Script(source, { filename: 'ConsultView.gs' });
});

test('web app exposes doGet and server-rendered HTML only', () => {
  assert.match(source, /function doGet\(e\)/);
  assert.match(source, /HtmlService\.createHtmlOutput\(/);
  assert.doesNotMatch(source, /google\.script\.run/);
});

test('web app always renders all 19 indicators', () => {
  assert.match(source, /for \(var i = 1; i <= 19; i\+\+\)/);
  assert.match(source, /TTQS 19 指標佐證投影/);
});

test('external view is explicitly preview-only, not an authorization boundary', () => {
  assert.match(source, /此切換僅為內部測試預覽，不是權限控制/);
  assert.match(source, /尚未建立正式外部部署/);
});

test('user-facing status avoids self-scoring claims', () => {
  assert.match(source, /不計算官方分數，也不宣稱評核結果/);
  assert.doesNotMatch(source, />PASS</);
  assert.doesNotMatch(source, />READY</);
});

test('web app keeps TEST and SAMPLE boundary visible', () => {
  assert.match(source, /TTQS ONE · 測試／示範資料（TEST／SAMPLE）/);
  assert.match(source, /所有正式資料寫入（REAL）仍停用/);
});
