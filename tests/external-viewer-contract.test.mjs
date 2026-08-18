import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const root = 'external-viewer';
const source = fs.readFileSync(`${root}/Code.gs`, 'utf8');
const manifest = JSON.parse(fs.readFileSync(`${root}/appsscript.json`, 'utf8'));
const files = fs.readdirSync(root).sort();
const functions = [...source.matchAll(/function\s+([A-Za-z0-9_]+)\s*\(/g)].map((m) => m[1]);
const publicFunctions = functions.filter((name) => !name.endsWith('_'));

test('external viewer has exact two-file deploy set', () => {
  assert.deepEqual(files, ['Code.gs', 'appsscript.json']);
});

test('external viewer source parses', () => {
  new vm.Script(source, { filename: 'external-viewer/Code.gs' });
});

test('only doGet is publicly callable', () => {
  assert.deepEqual(publicFunctions, ['doGet']);
});

test('viewer has anonymous external webapp and read-only spreadsheet scope only', () => {
  assert.deepEqual(manifest.webapp, { access: 'ANYONE_ANONYMOUS', executeAs: 'USER_DEPLOYING' });
  assert.deepEqual(manifest.oauthScopes, ['https://www.googleapis.com/auth/spreadsheets.readonly']);
});

test('viewer enables Sheets v4 advanced service and does not use SpreadsheetApp', () => {
  assert.deepEqual(manifest.dependencies?.enabledAdvancedServices, [
    { userSymbol: 'Sheets', version: 'v4', serviceId: 'sheets' }
  ]);
  assert.match(source, /Sheets\.Spreadsheets\.Values\.get/);
  assert.doesNotMatch(source, /SpreadsheetApp/);
});

test('viewer knows snapshot but never core spreadsheet id', () => {
  assert.match(source, /1yqrz0Xwj6vWQkfYor8WSGC6zV93L8EaJZkEfncATUqA/);
  assert.doesNotMatch(source, /1TzICbMmNoN2dTiRMK1dPYx-JOISKaCS-6i0i3iH68is/);
});

test('viewer contains no write, form, worker or script bridge APIs', () => {
  const forbidden = /\.setValue\s*\(|\.setValues\s*\(|\.appendRow\s*\(|insertSheet\s*\(|deleteSheet\s*\(|PropertiesService|ScriptApp|FormApp|DriveApp|UrlFetchApp|google\.script\.run|Sheets\.Spreadsheets\.Values\.(?:update|append|batchUpdate)/;
  assert.doesNotMatch(source, forbidden);
});

test('viewer uses bounded snapshot ranges only', () => {
  assert.ok(source.includes("'發布摘要'!A1:B10"));
  assert.ok(source.includes("'19指標佐證'!A1:F20"));
  assert.match(source, /TTQS_EXTERNAL_CAUSAL_SHEET_[^\n]+A1:G7/);
  assert.match(source, /TTQS_EXTERNAL_SOURCE_SHEET_[^\n]+A1:L120/);
});

test('viewer validates exact 19-indicator snapshot schema', () => {
  assert.match(source, /SNAPSHOT_SCHEMA_MISMATCH/);
  assert.match(source, /SNAPSHOT_INDICATOR_COUNT_INVALID/);
  assert.match(source, /indicators\.length !== 19/);
});

test('D3 requires exact six-step SAMPLE causal chain', () => {
  assert.match(source, /SAMPLE因果鏈/);
  assert.match(source, /SNAPSHOT_CAUSAL_SCHEMA_MISMATCH/);
  assert.match(source, /SNAPSHOT_CAUSAL_SEQUENCE_INVALID/);
  for (const label of ['需求蒐集', '需求／職能落差分析', '課程設計／目標／審查', '執行／資源／班次', '評量／檢討', '追蹤／改善']) {
    assert.match(source, new RegExp(label));
  }
});

test('D5 requires SUPPORTS evidence source rows covering all 19 indicators', () => {
  assert.match(source, /佐證來源定位/);
  assert.match(source, /SNAPSHOT_EVIDENCE_SCHEMA_MISMATCH/);
  assert.match(source, /SNAPSHOT_EVIDENCE_RELATION_INVALID/);
  assert.match(source, /SNAPSHOT_EVIDENCE_COVERAGE_INVALID/);
  assert.match(source, /SUPPORTS/);
  assert.match(source, /查看佐證與來源/);
});

test('runtime drilldown exposes only deidentified Observation locator metadata', () => {
  assert.match(source, /Observation ID/);
  assert.match(source, /原始收件定位/);
  assert.match(source, /observationId/);
  assert.match(source, /sourceLocator/);
  assert.doesNotMatch(source, /respondentEmail|emailAddress|phone|身分證|問卷原始回答[^。]*顯示/);
});

test('document source links are allowlisted to Google Drive or Docs', () => {
  assert.match(source, /SNAPSHOT_SOURCE_URL_UNSAFE/);
  assert.match(source, /docs\\\.google\\\.com\|drive\\\.google\\\.com/);
  assert.match(source, /開啟受控來源（依 Drive 權限）/);
});

test('viewer states external read-only, snapshot isolation and no self-scoring', () => {
  assert.match(source, /EXTERNAL_READONLY/);
  assert.match(source, /不直接連線 TTQS ONE 核心資料庫/);
  assert.match(source, /不計算 TTQS 官方分數/);
  assert.match(source, /17–19 的正式成果仍須以實際營運證據（REAL）為準/);
});
