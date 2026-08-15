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

test('viewer has read-only spreadsheet scope only', () => {
  assert.deepEqual(manifest.oauthScopes, ['https://www.googleapis.com/auth/spreadsheets.readonly']);
});

test('viewer knows snapshot but never core spreadsheet id', () => {
  assert.match(source, /1yqrz0Xwj6vWQkfYor8WSGC6zV93L8EaJZkEfncATUqA/);
  assert.doesNotMatch(source, /1TzICbMmNoN2dTiRMK1dPYx-JOISKaCS-6i0i3iH68is/);
});

test('viewer contains no write or worker APIs', () => {
  const forbidden = /\.setValue\s*\(|\.setValues\s*\(|\.appendRow\s*\(|insertSheet\s*\(|deleteSheet\s*\(|PropertiesService|ScriptApp|FormApp|DriveApp|UrlFetchApp|google\.script\.run/;
  assert.doesNotMatch(source, forbidden);
});

test('viewer validates exact 19-indicator snapshot schema', () => {
  assert.match(source, /SNAPSHOT_SCHEMA_MISMATCH/);
  assert.match(source, /SNAPSHOT_INDICATOR_COUNT_INVALID/);
  assert.match(source, /indicators\.length !== 19/);
});

test('viewer states external read-only and no self-scoring', () => {
  assert.match(source, /外部唯讀/);
  assert.match(source, /不計算 TTQS 官方分數/);
  assert.match(source, /17–19 的正式成果仍須以實際營運證據為準/);
});
