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

test('direct helper requests only three minimal Google scopes', () => {
  assert.match(helper, /spreadsheets\.readonly/);
  assert.match(helper, /script\.projects/);
  assert.match(helper, /script\.deployments/);
  assert.match(helper, /--use-project-scopes/);
  assert.match(helper, /--extra-scopes "\$PROJECT_SCOPE,\$DEPLOY_SCOPE"/);
  assert.doesNotMatch(helper, /cloud-platform|drive\.file|gmail|userinfo/);
});

test('direct helper downloads canonical main artifacts and uses REST deployer', () => {
  assert.match(helper, /RAW_BASE="https:\/\/raw\.githubusercontent\.com\/PT-Original-Point\/ttqs-one\/main"/);
  assert.match(helper, /scripts\/apps-script-rest-deploy\.mjs/);
  assert.match(helper, /external-viewer\/Code\.gs/);
  assert.match(helper, /external-viewer\/appsscript\.json/);
  assert.match(helper, /auth-check/);
  assert.match(helper, /ensure-project/);
  assert.match(helper, /push-content/);
  assert.match(helper, /deploy/);
});

test('direct helper is TEST-only and proves anonymous product markers', () => {
  assert.match(helper, /realProdTouch=0/);
  assert.match(helper, /EXTERNAL_READONLY/);
  assert.match(helper, /19 \/ 19/);
  assert.match(helper, /SAMPLE 評核因果鏈/);
  assert.match(helper, /19 指標佐證與來源下鑽/);
  assert.match(helper, /查看佐證與來源/);
  assert.match(helper, /PASS_PRODUCT_BLACKBOX/);
  assert.doesNotMatch(helper, /deploy\/prod|PROD_ENABLE|REAL_WRITE/);
});
