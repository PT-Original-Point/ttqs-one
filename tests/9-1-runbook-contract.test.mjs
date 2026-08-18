import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const evaluator = fs.readFileSync('docs/9-1-evaluator-drilldown-notes.md', 'utf8');
const deploy = fs.readFileSync('docs/9-1-external-direct-deploy-notes.md', 'utf8');

const canonicalUrl = 'https://script.google.com/macros/s/AKfycbznbXi-0XWNV68E-vGU9CiAE6ElXGIlDmy27EePXMdGpRaorURzKZq0dDgsNBaaZOLh/exec';

test('9/1 evaluator runbook uses canonical TEST portal and clean-session default', () => {
  assert.match(evaluator, new RegExp(canonicalUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')));
  assert.match(evaluator, /預設直接開私人／無痕視窗/);
  assert.match(evaluator, /只登入單一 Google 帳號/);
  assert.match(evaluator, /複數 Google 帳號/);
  assert.match(evaluator, /ANYONE_ANONYMOUS/);
});

test('9/1 evaluator runbook covers every Mission acceptance walkthrough axis', () => {
  for (const marker of [
    '官方 19 指標語意',
    'SAMPLE 因果鏈',
    '四類 TEST Forms 生命週期',
    '失敗／重試／exactly-once',
    '權限與 SAMPLE／REAL 邊界',
    '制度／程序／課程／證據／來源物件／Observation locator',
    '顧問問題／缺口已被收錄',
    'REAL_WRITE',
    'PROD_ENABLE',
    'REAL_COURSE_LOCK',
    'SAMPLE_AS_REAL'
  ]) {
    assert.match(evaluator, new RegExp(marker.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')), marker);
  }
});

test('direct deploy notes match the current two-scope reuse contract', () => {
  assert.match(deploy, /script\.projects/);
  assert.match(deploy, /script\.deployments/);
  assert.match(deploy, /只要求兩個最小部署 scope/);
  assert.match(deploy, /不要求 `spreadsheets\.readonly`/);
  assert.match(deploy, /重用既有 TEST Apps Script project 與既有 deployment/);
  assert.match(deploy, /BLACKBOX_ONLY_NO_PROVIDER_MUTATION/);
  assert.match(deploy, /sourceSha/);
  assert.match(deploy, /verificationSha/);
});

test('runbooks cannot upgrade TEST evidence into REAL or auto-pass the T Gate', () => {
  assert.match(evaluator, /技術黑箱 PASS 不等於整體 T Gate PASS/);
  assert.match(deploy, /不等於 REAL／PROD 啟動/);
  assert.match(evaluator, /SAMPLE／CONTROL 永不得宣稱為 REAL/);
});
