#!/bin/bash
set -euo pipefail

REPO="PT-Original-Point/ttqs-one"
ENVIRONMENT="TEST"
SECRET_NAME="CLASPRC_JSON_B64"
PROFILE="ttqs-external-test"
CLASP_VERSION="3.3.0"
PROJECT_SCOPE="https://www.googleapis.com/auth/script.projects"
DEPLOY_SCOPE="https://www.googleapis.com/auth/script.deployments"
SHEETS_SCOPE="https://www.googleapis.com/auth/spreadsheets.readonly"
RAW_BASE="https://raw.githubusercontent.com/PT-Original-Point/ttqs-one/main"

say() { printf '%s\n' "$*"; }
fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
need() { command -v "$1" >/dev/null 2>&1 || fail "缺少必要工具：$1"; }

need node
need npx
need gh
need curl
need base64

node -e "const [maj]=process.versions.node.split('.').map(Number); if(maj<22) process.exit(1)" \
  || fail "Node.js 必須為 22 以上版本。"

gh auth status -h github.com >/dev/null 2>&1 \
  || fail "GitHub CLI 尚未登入。請先執行 gh auth login，完成後重新執行本命令。"
gh repo view "$REPO" >/dev/null 2>&1 \
  || fail "目前 GitHub 身分無法存取 $REPO。"

TMP_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/ttqs-external-reauth.XXXXXX")"
cleanup() {
  rm -rf "$TMP_ROOT"
}
trap cleanup EXIT INT TERM

AUTH_HOME="$TMP_ROOT/home"
PROJECT_DIR="$TMP_ROOT/project"
mkdir -p "$AUTH_HOME" "$PROJECT_DIR"
chmod 700 "$AUTH_HOME"

cat > "$PROJECT_DIR/.clasp.json" <<'JSON'
{
  "scriptId": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
  "rootDir": "."
}
JSON

cat > "$PROJECT_DIR/appsscript.json" <<JSON
{
  "timeZone": "Asia/Taipei",
  "runtimeVersion": "V8",
  "oauthScopes": [
    "$SHEETS_SCOPE"
  ]
}
JSON

say "TTQS ONE｜External TEST OAuth 重新授權"
say "只會要求 3 個 scope："
say "  1. spreadsheets.readonly"
say "  2. script.projects"
say "  3. script.deployments"
say "不要求 cloud-platform、Drive 寫入、Gmail 或 REAL/PROD 權限。"
say "接下來瀏覽器開啟 Google 授權頁時，請使用協會 Google Workspace 部署帳號完成登入與同意。"

(
  cd "$PROJECT_DIR"
  HOME="$AUTH_HOME" npx --yes "@google/clasp@$CLASP_VERSION" login \
    --user "$PROFILE" \
    --use-project-scopes \
    --extra-scopes "$PROJECT_SCOPE,$DEPLOY_SCOPE"
)

AUTH_FILE="$AUTH_HOME/.clasprc.json"
test -s "$AUTH_FILE" || fail "Google OAuth 已返回，但未產生授權檔。"
chmod 600 "$AUTH_FILE"

REST_HELPER="$TMP_ROOT/apps-script-rest-deploy.mjs"
curl -fsSL "$RAW_BASE/scripts/apps-script-rest-deploy.mjs" -o "$REST_HELPER"
test -s "$REST_HELPER" || fail "無法取得 TTQS ONE OAuth 驗證器。"

node "$REST_HELPER" auth-check --credentials "$AUTH_FILE" \
  || fail "OAuth scope 或 refresh token 驗證未通過；GitHub Secret 未變更。"

OAUTH_B64="$(base64 < "$AUTH_FILE" | tr -d '\r\n')"
test -n "$OAUTH_B64" || fail "授權資料編碼失敗。"
printf '%s' "$OAUTH_B64" | gh secret set "$SECRET_NAME" \
  --env "$ENVIRONMENT" \
  --repo "$REPO"
unset OAUTH_B64

UPDATED_AT="$(gh secret list --env "$ENVIRONMENT" --repo "$REPO" --json name,updatedAt \
  --jq ".[] | select(.name==\"$SECRET_NAME\") | .updatedAt" | head -n 1)"
test -n "$UPDATED_AT" || fail "GitHub Secret 寫入後讀回失敗。"

say "GitHub TEST Secret 已安全更新；值未顯示於終端輸出。"
say "readback updatedAt=$UPDATED_AT"

say "正在觸發 External TEST provider 部署……"
gh workflow run deploy-external-test.yml --repo "$REPO" --ref deploy/test
say "已觸發。請回到 ChatGPT 輸入：授權完成"
say "ChatGPT 會接手檢查 Issue #39、匿名 Web App 黑箱與後續修復；你不需要再手改 GitHub 或 Apps Script。"
