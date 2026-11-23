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

test('SAMPLE evaluator flow is explicit and ordered from needs through improvement', () => {
  for (const label of ['需求蒐集', '需求／職能落差分析', '課程設計／目標／審查', '執行／資源／班次', '評量／檢討', '追蹤／改善']) {
    assert.match(source, new RegExp(label));
  }
  assert.match(source, /SAMPLE 評核因果鏈/);
  assert.match(source, /href="#indicator-/);
});

test('internal evaluator drilldown projects SUPPORTS relationship from EvidenceMaster tags', () => {
  assert.match(source, /relation: 'SUPPORTS'/);
  assert.match(source, /EvidenceMaster\.ttqs_indicator_tags 現行相容投影/);
  assert.match(source, /查看佐證與來源/);
  assert.match(source, /此處只做TEST\/SAMPLE追溯，不代表官方評分/);
});

test('runtime evidence can drill down from processed object to Observation source locator', () => {
  assert.match(source, /processed_object_id/);
  assert.match(source, /source_locator/);
  assert.match(source, /observation_id/);
  assert.match(source, /原始收件定位/);
});

test('external preview receives indicator counts but no evidence detail payload', () => {
  assert.match(source, /ttqsWebIndicatorModel_\(view === 'INTERNAL'\)/);
  assert.match(source, /evidence: includeEvidenceDetails \? evidence\.map/);
});

test('document drilldown only permits Google Drive or Google Docs source links', () => {
  assert.match(source, /docs\\\.google\\\.com\|drive\\\.google\\\.com/);
  assert.match(source, /開啟原始文件/);
});
