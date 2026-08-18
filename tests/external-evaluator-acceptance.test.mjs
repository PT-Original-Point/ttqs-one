import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('external-viewer/Code.gs', 'utf8');
const runtime = {};
vm.createContext(runtime);
vm.runInContext(source, runtime);
const model = runtime.ttqsExternalSnapshotModel_();
const rendered = runtime.ttqsExternalRender_(model);

function indicator(no) {
  return model.indicators.find((item) => String(item.no) === String(no));
}

test('D8 official semantic layer covers all 19 indicators without self-scoring', () => {
  assert.equal(model.official.length, 19);
  assert.equal(model.indicators.length, 19);
  assert.deepEqual(
    Array.from(indicator('12').officialFocus.subitems),
    ['12a 學員遴選', '12b 教材選擇', '12c 師資遴選', '12d 教學方法', '12e 教學環境與設備']
  );
  assert.deepEqual(
    Array.from(indicator('17').officialFocus.subitems),
    ['17a 反應評估', '17b 學習評估', '17c 行為評估', '17d 成果評估']
  );
  assert.match(rendered, /官方 19 指標評核語意導航/);
  assert.match(rendered, /不在系統內自動評分/);
  assert.doesNotMatch(source, /officialScore|recommendedScore|建議分數|自動評分結果/);
});

test('D8 embeds all four TEST form lifecycles from current deidentified readback', () => {
  assert.equal(model.forms.length, 4);
  assert.equal(model.formObservationTotal, 14);
  assert.deepEqual(
    Array.from(model.forms, (item) => item.kind),
    ['NEEDS', 'REGISTRATION', 'REACTION', 'FOLLOWUP30']
  );
  assert.ok(model.forms.every((item) => item.status === 'ACCEPTED'));
  assert.ok(model.forms.every((item) => /^OBS-/.test(item.observationId)));
  assert.ok(model.forms.every((item) => /^SHEET:\d+:ROW:\d+$/.test(item.sourceLocator)));
  assert.match(rendered, /四類 TEST Google Forms 生命週期/);
  assert.match(rendered, /4\/4 類別都有 ACCEPTED 來源/);
});

test('D6 human-readable S3 trace preserves failure, retry, exactly-once and final acceptance', () => {
  const trace = model.s3Trace;
  assert.equal(trace.topology, 'S3_SINGLE_SCHEDULER：1 master / 0 form-submit');
  assert.equal(trace.failure.status, 'FAILED');
  assert.equal(trace.failure.attemptNo, '1');
  assert.equal(trace.recovery.status, 'SUCCESS');
  assert.equal(trace.recovery.attemptNo, '2');
  assert.equal(trace.reconciliationStatus, 'MATCHED_EXACTLY_ONCE');
  assert.equal(trace.finalAcceptanceStatus, 'FINAL_ACCEPTED');
  assert.deepEqual(JSON.parse(JSON.stringify(trace.duplicateCounts)), {job:0, party:0, survey:0, evidence:0});
  assert.equal(trace.rawProviderWrite, '0');
  assert.match(rendered, /故障 → 重試 → 對帳 → FINAL_ACCEPTED/);
  assert.match(rendered, /TTQS_INJECTED_PARTIAL_FAILURE_AFTER_PARTY_ALIAS/);
  assert.match(rendered, /AttemptHistory=append-only/);
});

test('D5 every linked controlled document has embedded locator and summary fallback', () => {
  const linked = model.evidence.filter((item) => item.sourceUrl);
  assert.ok(linked.length >= 1);
  assert.ok(linked.every((item) => item.controlledLocator.length > 0));
  assert.ok(linked.every((item) => item.embeddedSummary.length > 0));
  assert.match(rendered, /受控章節／物件定位/);
  assert.match(rendered, /去識別摘要/);
  assert.match(rendered, /選配：開啟受控 Drive 來源（可能需登入）/);
  assert.match(rendered, /Google Drive 連結只是選配，不是顧問調閱成功的必要條件/);
});

test('external acceptance layer remains static read-only and does not gain Google data runtime APIs', () => {
  assert.doesNotMatch(source, /Sheets\.|SpreadsheetApp|DriveApp|UrlFetchApp|FormApp|PropertiesService|ScriptApp|google\.script\.run/);
  assert.doesNotMatch(source, /\.setValue\s*\(|\.setValues\s*\(|\.appendRow\s*\(|insertSheet\s*\(|deleteSheet\s*\(/);
  assert.match(rendered, /EXTERNAL_READONLY/);
  assert.match(rendered, /不在執行期呼叫 Google Sheets／Drive API/);
  assert.match(rendered, /不得視為正式營運（REAL）的正式評核證據/);
});
