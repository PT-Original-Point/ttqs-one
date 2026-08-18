import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {spawnSync} from 'node:child_process';

const helperPath = 'scripts/reauth-external-test.sh';
const helper = fs.readFileSync(helperPath, 'utf8');
const workflow = fs.readFileSync('.github/workflows/deploy-external-test.yml', 'utf8');

test('reauth helper has valid bash syntax', () => {
  const result = spawnSync('bash', ['-n', helperPath], {encoding: 'utf8'});
  assert.equal(result.status, 0, result.stderr);
});

test('reauth helper uses isolated temporary HOME and cleans it', () => {
  assert.match(helper, /mktemp -d/);
  assert.match(helper, /AUTH_HOME="\$TMP_ROOT\/home"/);
  assert.match(helper, /HOME="\$AUTH_HOME" npx/);
  assert.match(helper, /trap cleanup EXIT INT TERM/);
  assert.match(helper, /rm -rf "\$TMP_ROOT"/);
});

test('missing gh bootstraps an official temporary macOS binary instead of requiring package installation', () => {
  assert.doesNotMatch(helper, /need gh/);
  assert.match(helper, /GH_RELEASE_API="https:\/\/api\.github\.com\/repos\/cli\/cli\/releases\/latest"/);
  assert.match(helper, /asset\.digest/);
  assert.match(helper, /sha256:\[0-9a-f\]\{64\}/);
  assert.match(helper, /shasum -a 256/);
  assert.match(helper, /GitHub CLI 暫存版已完成 SHA-256 驗證/);
  assert.doesNotMatch(helper, /brew install gh|sudo installer/);
});

test('GitHub authentication is self-healing with one browser login when needed', () => {
  assert.match(helper, /"\$GH_BIN" auth status -h github\.com/);
  assert.match(helper, /"\$GH_BIN" auth login -h github\.com --git-protocol https --web/);
  const status = helper.indexOf('auth status -h github.com');
  const login = helper.indexOf('auth login -h github.com --git-protocol https --web');
  const repo = helper.indexOf('repo view "$REPO"');
  assert.ok(status >= 0 && login > status && repo > login);
});

test('reauth helper requests exactly project manifest scope plus two Apps Script deployment scopes', () => {
  assert.match(helper, /SHEETS_SCOPE="https:\/\/www\.googleapis\.com\/auth\/spreadsheets\.readonly"/);
  assert.match(helper, /PROJECT_SCOPE="https:\/\/www\.googleapis\.com\/auth\/script\.projects"/);
  assert.match(helper, /DEPLOY_SCOPE="https:\/\/www\.googleapis\.com\/auth\/script\.deployments"/);
  assert.match(helper, /--use-project-scopes/);
  assert.match(helper, /--extra-scopes "\$PROJECT_SCOPE,\$DEPLOY_SCOPE"/);
  assert.doesNotMatch(helper, /--include-clasp-scopes/);

  const loginStart = helper.indexOf('HOME="$AUTH_HOME" npx');
  const authFileStart = helper.indexOf('AUTH_FILE="$AUTH_HOME/.clasprc.json"');
  assert.ok(loginStart >= 0 && authFileStart > loginStart);
  const executableLoginBlock = helper.slice(loginStart, authFileStart);
  assert.doesNotMatch(executableLoginBlock, /cloud-platform|drive\.file|userinfo\.email|userinfo\.profile/);
});

test('reauth helper pins clasp version and uses dedicated credential profile', () => {
  assert.match(helper, /CLASP_VERSION="3\.3\.0"/);
  assert.match(helper, /PROFILE="ttqs-external-test"/);
  assert.match(helper, /--user "\$PROFILE"/);
});

test('reauth helper fail-closes through REST auth-check before GitHub secret mutation', () => {
  const authCheck = helper.indexOf('auth-check --credentials "$AUTH_FILE"');
  const secretSet = helper.indexOf('"$GH_BIN" secret set "$SECRET_NAME"');
  assert.ok(authCheck >= 0 && secretSet > authCheck);
  assert.match(helper, /OAuth scope 或 refresh token 驗證未通過；GitHub Secret 未變更/);
});

test('reauth helper sends secret through stdin and never prints its value', () => {
  assert.match(helper, /printf '%s' "\$OAUTH_B64" \| "\$GH_BIN" secret set/);
  assert.match(helper, /unset OAUTH_B64/);
  assert.doesNotMatch(helper, /say .*OAUTH_B64|printf .*AUTH_FILE.*stdout/);
});

test('reauth helper reads back GitHub environment secret metadata', () => {
  assert.match(helper, /"\$GH_BIN" secret list --env "\$ENVIRONMENT" --repo "\$REPO" --json name,updatedAt/);
  assert.match(helper, /select\(\.name==\\"\$SECRET_NAME\\"\)/);
  assert.match(helper, /readback updatedAt=/);
});

test('reauth helper automatically dispatches only deploy/test workflow after secret readback', () => {
  const readback = helper.indexOf('UPDATED_AT=');
  const dispatch = helper.indexOf('"$GH_BIN" workflow run deploy-external-test.yml');
  assert.ok(readback >= 0 && dispatch > readback);
  assert.match(helper, /--ref deploy\/test/);
  assert.doesNotMatch(helper, /deploy\/prod|--ref main/);
});

test('external TEST workflow supports explicit workflow_dispatch while retaining deploy/test ref guard', () => {
  assert.match(workflow, /workflow_dispatch:/);
  assert.match(workflow, /github\.ref == 'refs\/heads\/deploy\/test'/);
  assert.match(workflow, /test \"\$GITHUB_REF\" = \"refs\/heads\/deploy\/test\"/);
});
