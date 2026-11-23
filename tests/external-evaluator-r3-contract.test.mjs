import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const code = fs.readFileSync('external-viewer/Code.gs', 'utf8');

const required = [
  '社團法人屏東縣原始點關懷協會',
  '目前營運真實狀態',
  'REAL 訓練事證',
  '尚未發生',
  '介面覆蓋',
  '19 / 19',
  '系統能力',
  '正式可評事證',
  '官方佐證表視圖',
  'CLEAN_FIXTURE_2',
  'legacy SAMPLE-001 因時序倒掛已退出主展示',
  '12a 學員遴選',
  '12e 教學環境與設備',
  '17a 反應評估',
  '17d 成果評估',
  '開啟 FrozenArtifact',
  '?artifact=',
  'DEMO FrozenArtifact projection',
  '不構成 REAL 辦訓事證或正式 TTQS 評分',
  '正式委員主路徑不依賴協會 Google 帳號',
  '正式 cutoff_at 尚未定義'
];

test('R3 evaluator truth semantics and 3-click artifact route are present', () => {
  for (const marker of required) assert.ok(code.includes(marker), `missing R3 marker: ${marker}`);
});

test('official checklist contains exactly the expected 26 rows', () => {
  const match = code.match(/var TTQS_CHECKLIST_=\[(.*?)\];\nfunction esc_/s);
  assert.ok(match, 'TTQS_CHECKLIST_ block missing');
  const rows = [...match[1].matchAll(/\['(?:1[0-9]|[1-9]|12[a-e]|17[a-d])'/g)];
  assert.equal(rows.length, 26);
});

test('external evaluator remains runtime data-API free and non-REAL', () => {
  for (const forbidden of ['SpreadsheetApp', 'DriveApp', 'UrlFetchApp', 'Sheets.']) {
    assert.equal(code.includes(forbidden), false, `runtime API forbidden: ${forbidden}`);
  }
  assert.ok(code.includes('正式 LOCK／SUBMIT 尚未發生'));
  assert.ok(code.includes('REAL／正式評分／PROD／官方送件均未執行'));
});
