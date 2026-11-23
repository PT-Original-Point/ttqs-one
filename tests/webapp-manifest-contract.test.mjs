import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const internal = JSON.parse(fs.readFileSync('apps-script/appsscript.json', 'utf8'));
const external = JSON.parse(fs.readFileSync('external-viewer/appsscript.json', 'utf8'));

test('內部 Web App 僅允許部署帳號使用', () => {
  assert.deepEqual(internal.webapp, { access: 'MYSELF', executeAs: 'USER_DEPLOYING' });
});

test('內部 Web App 不新增 userinfo.email scope', () => {
  assert.equal(internal.oauthScopes.some((scope) => scope.includes('userinfo.email')), false);
});

test('外部 Viewer 使用匿名唯讀 Web App 設定', () => {
  assert.deepEqual(external.webapp, { access: 'ANYONE_ANONYMOUS', executeAs: 'USER_DEPLOYING' });
});

test('外部 Viewer 不宣告 Google 資料執行期 OAuth scope', () => {
  assert.equal(Object.hasOwn(external, 'oauthScopes'), false);
});

test('外部 Viewer 不啟用進階服務或 Google 資料 API 相依', () => {
  assert.equal(Object.hasOwn(external, 'dependencies'), false);
  const serialized = JSON.stringify(external);
  assert.doesNotMatch(serialized, /spreadsheets|drive|enabledAdvancedServices|executionApi/);
});
