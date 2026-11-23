#!/bin/bash
set -euo pipefail

CLASP_VERSION="3.3.0"
PROFILE="ttqs-external-test-direct"
PROJECT_SCOPE="https://www.googleapis.com/auth/script.projects"
DEPLOY_SCOPE="https://www.googleapis.com/auth/script.deployments"
RAW_BASE="https://raw.githubusercontent.com/PT-Original-Point/ttqs-one/main"
TITLE="TTQS ONE External Evaluator Portal TEST"
EXTERNAL_SCRIPT_ID_HINT="1hjS_1IZ3rqwCe8wxi3cICUu_zcVk1EPI2QRrrchEb3wh6ySJ_ZHAMrUA"
EXTERNAL_DEPLOYMENT_ID_HINT="AKfycbznbXi-0XWNV68E-vGU9CiAE6ElXGIlDmy27EePXMdGpRaorURzKZq0dDgsNBaaZOLh"

say() { printf '%s\n' "$*"; }
fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
need() { command -v "$1" >/dev/null 2>&1 || fail "缺少必要工具：$1"; }

need node
need npx
need curl
need open

node -e "const [maj]=process.versions.node.split('.').map(Number); if(maj<22) process.exit(1)" \
  || fail "Node.js 必須為 22 以上版本。"

TMP_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/ttqs-external-direct.XXXXXX")"
cleanup() { rm -rf "$TMP_ROOT"; }
trap cleanup EXIT INT TERM

AUTH_HOME="$TMP_ROOT/home"
AUTH_PROJECT_DIR="$TMP_ROOT/auth-project"
PROJECT_DIR="$TMP_ROOT/project"
ENV_FILE="$TMP_ROOT/deploy.env"
mkdir -p "$AUTH_HOME" "$AUTH_PROJECT_DIR" "$PROJECT_DIR"
chmod 700 "$AUTH_HOME"

cat > "$AUTH_PROJECT_DIR/.clasp.json" <<'JSON'
{
  "scriptId": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
  "rootDir": "."
}
JSON

cat > "$AUTH_PROJECT_DIR/appsscript.json" <<'JSON'
{
  "timeZone": "Asia/Taipei",
  "runtimeVersion": "V8",
  "oauthScopes": []
}
JSON

say "TTQS ONE｜External TEST 直接部署"
say "這條流程不需要 GitHub CLI，也不要求 GitHub 裝置驗證。"
say "只會要求 Google 2 個最小部署 scope："
say "  1. script.projects"
say "  2. script.deployments"
say "REAL／PROD 不在本流程範圍。"
say "本次固定續用既有 TEST Apps Script 專案與既有 deployment，不重複建立。"
say "接下來若瀏覽器跳出 Google 授權頁，請使用協會 Google Workspace 部署帳號登入並同意。"

(
  cd "$AUTH_PROJECT_DIR"
  HOME="$AUTH_HOME" npx --yes "@google/clasp@$CLASP_VERSION" login \
    --user "$PROFILE" \
    --use-project-scopes \
    --extra-scopes "$PROJECT_SCOPE,$DEPLOY_SCOPE"
)

AUTH_FILE="$AUTH_HOME/.clasprc.json"
test -s "$AUTH_FILE" || fail "Google OAuth 已返回，但未產生授權檔。"
chmod 600 "$AUTH_FILE"

REST_HELPER="$TMP_ROOT/apps-script-rest-deploy.mjs"
BLACKBOX_CLASSIFIER="$TMP_ROOT/external-blackbox-classifier.mjs"
curl -fsSL "$RAW_BASE/scripts/apps-script-rest-deploy.mjs" -o "$REST_HELPER"
curl -fsSL "$RAW_BASE/scripts/external-blackbox-classifier.mjs" -o "$BLACKBOX_CLASSIFIER"
test -s "$REST_HELPER" || fail "無法取得 Apps Script REST 部署器。"
test -s "$BLACKBOX_CLASSIFIER" || fail "無法取得 External TEST 黑箱分類器。"

curl -fsSL "$RAW_BASE/external-viewer/Code.gs" -o "$PROJECT_DIR/Code.gs"
curl -fsSL "$RAW_BASE/external-viewer/appsscript.json" -o "$PROJECT_DIR/appsscript.json"
test -s "$PROJECT_DIR/Code.gs" && test -s "$PROJECT_DIR/appsscript.json" \
  || fail "無法取得 External TEST Viewer 成品。"

AUTH_OUTPUT="$(node "$REST_HELPER" auth-check --credentials "$AUTH_FILE")" \
  || fail "Google OAuth scope 或 refresh token 驗證未通過。"
case "$AUTH_OUTPUT" in
  *AUTH_MINIMAL_SCOPE_PASS*) ;;
  *) fail "Apps Script REST 部署器未真正執行 auth-check；已停止在任何專案變更之前。" ;;
esac
say "$AUTH_OUTPUT"

: > "$ENV_FILE"
ENSURE_OUTPUT="$(node "$REST_HELPER" ensure-project \
  --credentials "$AUTH_FILE" \
  --script-id "$EXTERNAL_SCRIPT_ID_HINT" \
  --title "$TITLE" \
  --env-file "$ENV_FILE")" \
  || fail "既有 Apps Script TEST 專案讀回失敗；已停止，未建立第二個專案。"
say "$ENSURE_OUTPUT"
test -s "$ENV_FILE" || fail "Apps Script REST 部署器沒有寫入專案收據；已停止，請勿盲目重跑。"

# shellcheck disable=SC1090
source "$ENV_FILE"
test -n "${EXTERNAL_SCRIPT_ID_RESOLVED:-}" || fail "Apps Script TEST 專案讀回 scriptId 失敗。"
test "$EXTERNAL_SCRIPT_ID_RESOLVED" = "$EXTERNAL_SCRIPT_ID_HINT" || fail "Apps Script TEST 專案 identity 漂移。"
test "${EXTERNAL_MODE:-}" = "REUSE" || fail "Apps Script TEST 專案未以 REUSE 模式執行；已停止避免重複 bootstrap。"

PUSH_OUTPUT="$(node "$REST_HELPER" push-content \
  --credentials "$AUTH_FILE" \
  --script-id "$EXTERNAL_SCRIPT_ID_RESOLVED" \
  --root-dir "$PROJECT_DIR")" \
  || fail "External TEST Viewer 推送或讀回失敗。"
case "$PUSH_OUTPUT" in
  *EXTERNAL_CONTENT_PUSH_READBACK_PASS*) ;;
  *) fail "External TEST Viewer 推送未取得 provider readback PASS。" ;;
esac
say "$PUSH_OUTPUT"

DEPLOY_OUTPUT="$(node "$REST_HELPER" deploy \
  --credentials "$AUTH_FILE" \
  --script-id "$EXTERNAL_SCRIPT_ID_RESOLVED" \
  --deployment-id "$EXTERNAL_DEPLOYMENT_ID_HINT" \
  --description "TTQS ONE 9/1 External Evaluator Portal TEST direct deploy" \
  --env-file "$ENV_FILE")" \
  || fail "External TEST Web App 建版／部署／有效入口讀回失敗。"
say "$DEPLOY_OUTPUT"

# shellcheck disable=SC1090
source "$ENV_FILE"
test -n "${EXTERNAL_DEPLOYMENT_ID_RESOLVED:-}" || fail "deploymentId 讀回失敗。"
test -n "${EXTERNAL_WEBAPP_URL:-}" || fail "Web App URL 讀回失敗。"
test "$EXTERNAL_DEPLOYMENT_ID_RESOLVED" = "$EXTERNAL_DEPLOYMENT_ID_HINT" || fail "Web App deployment identity 漂移。"
test "${EXTERNAL_WEBAPP_ACCESS:-}" = "ANYONE_ANONYMOUS" || fail "Google provider readback 不是 ANYONE_ANONYMOUS。"
test "${EXTERNAL_WEBAPP_EXECUTE_AS:-}" = "USER_DEPLOYING" || fail "Google provider readback 不是 USER_DEPLOYING。"

say "Apps Script TEST 外部 Portal 已完成版本更新與有效入口讀回。"
say "scriptId=$EXTERNAL_SCRIPT_ID_RESOLVED"
say "deploymentId=$EXTERNAL_DEPLOYMENT_ID_RESOLVED"
say "webappUrl=$EXTERNAL_WEBAPP_URL"
say "webappAccess=$EXTERNAL_WEBAPP_ACCESS"
say "webappExecuteAs=$EXTERNAL_WEBAPP_EXECUTE_AS"
say "realProdTouch=0"

HTML="$TMP_ROOT/portal.html"
BLACKBOX="NOT_PASS"
LAST_HTTP_STATUS="000"
LAST_FINAL_URL=""
LAST_MARKER_DIAGNOSTIC=""
for attempt in 1 2 3 4 5 6; do
  CURL_META="$(curl -LsS --max-time 30 -o "$HTML" -w '%{http_code}|%{url_effective}' "$EXTERNAL_WEBAPP_URL" 2>/dev/null || true)"
  LAST_HTTP_STATUS="${CURL_META%%|*}"
  LAST_FINAL_URL="${CURL_META#*|}"
  if [ "$LAST_HTTP_STATUS" = "200" ]; then
    if MARKER_OUTPUT="$(node "$BLACKBOX_CLASSIFIER" --html "$HTML" 2>&1)"; then
      LAST_MARKER_DIAGNOSTIC="$MARKER_OUTPUT"
      BLACKBOX="PASS_PRODUCT_BLACKBOX"
      break
    else
      LAST_MARKER_DIAGNOSTIC="$MARKER_OUTPUT"
    fi
  fi
  sleep 5
done

FINAL_HOST="$(node -e 'try{process.stdout.write(new URL(process.argv[1]).host)}catch{process.stdout.write("unknown")}' "$LAST_FINAL_URL")"
say "anonymousHttpStatus=$LAST_HTTP_STATUS"
say "anonymousFinalHost=$FINAL_HOST"
say "anonymousBlackbox=$BLACKBOX"
if [ "$BLACKBOX" != "PASS_PRODUCT_BLACKBOX" ]; then
  if [ "$LAST_HTTP_STATUS" = "403" ]; then
    say "anonymousFailure=HTTP_403_AFTER_PROVIDER_ANYONE_ANONYMOUS"
  elif [ "$LAST_HTTP_STATUS" = "200" ]; then
    say "anonymousFailure=HTTP_200_BUT_PRODUCT_MARKERS_MISSING"
    test -n "$LAST_MARKER_DIAGNOSTIC" && say "anonymousMarkerDiagnostic=$LAST_MARKER_DIAGNOSTIC"
  else
    say "anonymousFailure=HTTP_$LAST_HTTP_STATUS"
  fi
  fail "Apps Script provider 已確認匿名權限設定，但產品黑箱仍未通過；請不要重跑，我們會依 HTTP 診斷繼續查。"
fi

say "$LAST_MARKER_DIAGNOSTIC"
open "$EXTERNAL_WEBAPP_URL" >/dev/null 2>&1 || true
say "PASS_PRODUCT_BLACKBOX"
say "瀏覽器已嘗試開啟外部 TEST Portal。"
say "請回到 ChatGPT，只貼最後這六行：scriptId、deploymentId、webappUrl、webappAccess、webappExecuteAs、anonymousBlackbox。"
