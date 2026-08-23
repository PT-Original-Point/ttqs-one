import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

const SOURCE = fs.readFileSync(new URL('../release/official129/Official129Runtime.gs', import.meta.url), 'utf8');
const REQUIRED = '如果用 Chrome 且登入多個 Google 帳號時看到錯誤，請改用無痕視窗或 Safari 私密瀏覽開啟。';

test('P-04 homepage source contains the exact Chrome multi-account recovery guidance', () => {
  assert.ok(SOURCE.includes(REQUIRED));
  const homeStart = SOURCE.indexOf('function ttqsR7HomeHtml_');
  const warningStart = SOURCE.indexOf('function ttqsR7Warning_');
  assert.ok(homeStart >= 0);
  assert.ok(warningStart >= 0);
  assert.ok(SOURCE.indexOf(REQUIRED) < homeStart, 'guidance must be emitted by the warning included on homepage');
});
