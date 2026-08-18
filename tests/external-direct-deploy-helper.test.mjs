import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {spawnSync} from 'node:child_process';

const helperPath = 'scripts/reauth-external-test-direct.sh';
const helper = fs.readFileSync(helperPath, 'utf8');

test('direct deploy helper has valid bash syntax', () => {
  const result = spawnSync('bash', ['-n', helperPath], {encoding: 'utf8'});
  assert.equal(result.status, 0, result.stderr);
});

test('direct helper has no GitHub CLI or GitHub auth dependency', () => {
  assert.doesNotMatch(helper, /\bgh\b|GH_BIN|GH_RELEASE_API|github\.com\/login\/device|secret set|workflow run/);
});

test('direct helper uses isolated temporary HOME and cleans credentials', () => {
  assert.match(helper, /mktemp -d/);
  assert.match(helper, /AUTH_HOME="\$TMP_ROOT\/home"/);
  assert.match(helper, /HOME="\$AUTH_HOME" npx/);
  assert.match(helper, /trap cleanup EXIT INT TERM/);
  assert.match(helper, /rm -rf "\$TMP_ROOT"/);
});

test('direct helper isolates clasp auth project from canonical push project', () => {
  assert.match(helper, /AUTH_PROJECT_DIR="\$TMP_ROOT\/auth-project"/);
  assert.match(helper, /PROJECT_DIR="\$TMP_ROOT\/project"/);
  assert.match(helper, /cat > "\$AUTH_PROJECT_DIR\/\.clasp\.json"/);
  assert.match(helper, /cat > "\$AUTH_PROJECT_DIR\/appsscript\.json"/);
  assert.match(helper, /"oauthScopes": \[\]/);
  assert.match(helper, /cd "\$AUTH_PROJECT_DIR"/);
  assert.match(helper, /"\$PROJECT_DIR\/Code\.gs"/);
  assert.match(helper, /"\$PROJECT_DIR\/appsscript\.json"/);
  assert.doesNotMatch(helper, /cat > "\$PROJECT_DIR\/\.clasp\.json"/);
});

test('direct helper reuses existing TEST project and deployment', () => {
  assert.match(helper, /EXTERNAL_SCRIPT_ID_HINT="1hjS_1IZ3rqwCe8wxi3cICUu_zcVk1EPI2QRrrchEb3wh6ySJ_ZHAMrUA"/);
  assert.match(helper, /EXTERNAL_DEPLOYMENT_ID_HINT="AKfycbznbXi-0XWNV68E-vGU9CiAE6ElXGIlDmy27EePXMdGpRaorURzKZq0dDgsNBaaZOLh"/);
  assert.match(helper, /--script-id "\$EXTERNAL_SCRIPT_ID_HINT"/);
  assert.match(helper, /--deployment-id "\$EXTERNAL_DEPLOYMENT_ID_HINT"/);
  assert.match(helper, /EXTERNAL_MODE:-.*REUSE/);
  assert.match(helper, /deployment identity 漂移/);
  assert.doesNotMatch(helper, /--script-id ""/);
  assert.doesNotMatch(helper, /--deployment-id ""/);
});

test('direct helper requests exactly two deployment Google scopes', () => {
  assert.match(helper, /PROJECT_SCOPE="https:\/\/www\.googleapis\.com\/auth\/script\.projects"/);
  assert.match(helper, /DEPLOY_SCOPE="https:\/\/www\.googleapis\.com\/auth\/script\.deployments"/);
  assert.match(helper, /只會要求 Google 2 個最小部署 scope/);
  assert.match(helper, /--use-project-scopes/);
  assert.match(helper, /--extra-scopes "\$PROJECT_SCOPE,\$DEPLOY_SCOPE"/);
  assert.doesNotMatch(helper, /spreadsheets\.readonly|cloud-platform|drive\.file|gmail|userinfo/);
});

test('direct helper downloads canonical main artifacts, REST deployer and black-box classifier', () => {
  assert.match(helper, /RAW_BASE="https:\/\/raw\.githubusercontent\.com\/PT-Original-Point\/ttqs-one\/main"/);
  assert.match(helper, /scripts\/apps-script-rest-deploy\.mjs/);
  assert.match(helper, /scripts\/external-blackbox-classifier\.mjs/);
  assert.match(helper, /external-viewer\/Code\.gs/);
  assert.match(helper, /external-viewer\/appsscript\.json/);
  assert.match(helper, /auth-check/);
  assert.match(helper, /ensure-project/);
  assert.match(helper, /push-content/);
  assert.match(helper, /deploy/);
});

test('direct helper fails closed if REST CLI silently does not execute', () => {
  assert.match(helper, /AUTH_OUTPUT=/);
  assert.match(helper, /AUTH_MINIMAL_SCOPE_PASS/);
  assert.match(helper, /未真正執行 auth-check/);
  assert.match(helper, /ENSURE_OUTPUT=/);
  assert.match(helper, /test -s "\$ENV_FILE"/);
  assert.match(helper, /沒有寫入專案收據/);
  assert.match(helper, /PUSH_OUTPUT=/);
  assert.match(helper, /EXTERNAL_CONTENT_PUSH_READBACK_PASS/);
  assert.match(helper, /DEPLOY_OUTPUT=/);
});

test('direct helper requires provider effective anonymous web app config', () => {
  assert.match(helper, /EXTERNAL_WEBAPP_ACCESS:-.*ANYONE_ANONYMOUS/);
  assert.match(helper, /EXTERNAL_WEBAPP_EXECUTE_AS:-.*USER_DEPLOYING/);
  assert.match(helper, /Google provider readback 不是 ANYONE_ANONYMOUS/);
  assert.match(helper, /Google provider readback 不是 USER_DEPLOYING/);
  assert.match(helper, /webappAccess=\$EXTERNAL_WEBAPP_ACCESS/);
  assert.match(helper, /webappExecuteAs=\$EXTERNAL_WEBAPP_EXECUTE_AS/);
});

test('direct helper diagnoses anonymous HTTP failure without curl -f hiding status', () => {
  assert.match(helper, /-w '%\{http_code\}\|%\{url_effective\}'/);
  assert.match(helper, /anonymousHttpStatus=\$LAST_HTTP_STATUS/);
  assert.match(helper, /anonymousFinalHost=\$FINAL_HOST/);
  assert.match(helper, /HTTP_403_AFTER_PROVIDER_ANYONE_ANONYMOUS/);
  assert.doesNotMatch(helper, /curl -fLsS --max-time 30/);
});

test('direct helper uses normalized classifier instead of raw HtmlService marker grep', () => {
  assert.match(helper, /BLACKBOX_CLASSIFIER=/);
  assert.match(helper, /node "\$BLACKBOX_CLASSIFIER" --html "\$HTML"/);
  assert.match(helper, /anonymousMarkerDiagnostic=/);
  assert.match(helper, /PASS_PRODUCT_BLACKBOX/);
  assert.doesNotMatch(helper, /grep -q '19 \/ 19'/);
});

test('direct helper remains TEST-only', () => {
  assert.match(helper, /realProdTouch=0/);
  assert.doesNotMatch(helper, /deploy\/prod|PROD_ENABLE|REAL_WRITE/);
});
