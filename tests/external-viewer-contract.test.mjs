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
const runtime = {};
vm.createContext(runtime);
vm.runInContext(source, runtime);

test('external viewer has exact two-file deploy set', () => {
  assert.deepEqual(files, ['Code.gs', 'appsscript.json']);
});

test('external viewer source parses and only doGet is publicly callable', () => {
  new vm.Script(source, { filename: 'external-viewer/Code.gs' });
  assert.deepEqual(publicFunctions, ['doGet']);
});

test('viewer is anonymous but has zero Google data runtime permissions', () => {
  assert.deepEqual(manifest.webapp, { access: 'ANYONE_ANONYMOUS', executeAs: 'USER_DEPLOYING' });
  assert.equal(Object.hasOwn(manifest, 'oauthScopes'), false);
  assert.equal(Object.hasOwn(manifest, 'dependencies'), false);
  assert.doesNotMatch(source, /Sheets\.|SpreadsheetApp|DriveApp|UrlFetchApp/);
  assert.doesNotMatch(JSON.stringify(manifest), /spreadsheets|drive|enabledAdvancedServices/);
});

test('viewer embeds only the deidentified snapshot provenance and never the core spreadsheet id', () => {
  assert.match(source, /1yqrz0Xwj6vWQkfYor8WSGC6zV93L8EaJZkEfncATUqA/);
  assert.doesNotMatch(source, /1TzICbMmNoN2dTiRMK1dPYx-JOISKaCS-6i0i3iH68is/);
  assert.match(source, /部署版本內嵌的去識別唯讀快照/);
  assert.match(source, /不在執行期呼叫 Google Sheets／Drive API/);
});

test('static snapshot model preserves 19 indicators, six causal steps, 25 evidence rows and four unique TEST observations', () => {
  const model = runtime.ttqsExternalSnapshotModel_();
  assert.equal(model.indicators.length, 19);
  assert.equal(model.causalFlow.length, 6);
  assert.equal(model.evidence.length, 25);
  const locatorRows = model.evidence.filter((item) => item.observationId && item.sourceLocator);
  assert.equal(locatorRows.length, 7);
  assert.equal(new Set(locatorRows.map((item) => item.observationId)).size, 4);
  assert.deepEqual([...new Set(model.evidence.map((item) => item.indicatorNo))].sort((a,b) => Number(a)-Number(b)), Array.from({length:19}, (_,i) => String(i+1)));
});

test('viewer contains no write, form, worker or script bridge APIs', () => {
  const forbidden = /\.setValue\s*\(|\.setValues\s*\(|\.appendRow\s*\(|insertSheet\s*\(|deleteSheet\s*\(|PropertiesService|ScriptApp|FormApp|DriveApp|UrlFetchApp|google\.script\.run/;
  assert.doesNotMatch(source, forbidden);
});

test('D3 requires exact six-step SAMPLE causal chain', () => {
  assert.match(source, /SAMPLE 評核因果鏈/);
  assert.match(source, /SNAPSHOT_CAUSAL_SEQUENCE_INVALID/);
  for (const label of ['需求蒐集', '需求／職能落差分析', '課程設計／目標／審查', '執行／資源／班次', '評量／檢討', '追蹤／改善']) {
    assert.match(source, new RegExp(label));
  }
});

test('D5 requires SUPPORTS evidence source rows covering all 19 indicators', () => {
  assert.match(source, /SNAPSHOT_EVIDENCE_RELATION_INVALID/);
  assert.match(source, /SNAPSHOT_EVIDENCE_COVERAGE_INVALID/);
  assert.match(source, /SUPPORTS/);
  assert.match(source, /查看佐證與來源/);
});

test('runtime drilldown exposes only deidentified Observation locator metadata', () => {
  assert.match(source, /OBS-5DF457DAE87CE85418F35E8B/);
  assert.match(source, /SHEET:1145488986:ROW:5/);
  assert.match(source, /原始收件定位/);
  assert.doesNotMatch(source, /respondentEmail|emailAddress|phone|身分證字號[^或]*[0-9]{6}|問卷原始回答[^。]*顯示/);
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
