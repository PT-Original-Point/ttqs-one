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
GH_RELEASE_API="https://api.github.com/repos/cli/cli/releases/latest"

say() { printf '%s\n' "$*"; }
fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
need() { command -v "$1" >/dev/null 2>&1 || fail "缺少必要工具：$1"; }

need node
need npx
need curl
need base64
need unzip
need shasum
need awk
need find
need uname

node -e "const [maj]=process.versions.node.split('.').map(Number); if(maj<22) process.exit(1)" \
  || fail "Node.js 必須為 22 以上版本。"

TMP_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/ttqs-external-reauth.XXXXXX")"
cleanup() {
  rm -rf "$TMP_ROOT"
}
trap cleanup EXIT INT TERM

GH_BIN=""
ensure_gh() {
  if command -v gh >/dev/null 2>&1; then
    GH_BIN="$(command -v gh)"
    return 0
  fi

  test "$(uname -s)" = "Darwin" || fail "缺少 GitHub CLI，且目前自動暫存版只支援 macOS。"

  local arch
  case "$(uname -m)" in
    arm64) arch="arm64" ;;
    x86_64) arch="amd64" ;;
    *) fail "不支援的 Mac CPU 架構：$(uname -m)" ;;
  esac

  say "未偵測到 gh；正在下載 GitHub 官方最新版暫存 CLI，不會安裝系統套件。"

  local release_json="$TMP_ROOT/gh-release.json"
  local gh_meta gh_asset_name gh_asset_url gh_asset_digest gh_zip gh_extract expected actual
  curl -fsSL --retry 3 "$GH_RELEASE_API" -o "$release_json"

  gh_meta="$(node - "$release_json" "$arch" <<'NODE'
const fs = require('fs');
const [file, arch] = process.argv.slice(2);
const release = JSON.parse(fs.readFileSync(file, 'utf8'));
const assets = Array.isArray(release.assets) ? release.assets : [];
const re = new RegExp(`^gh_[0-9.]+_macOS_${arch}\\.zip$`);
const matches = assets.filter((a) => re.test(String(a.name || '')));
if (matches.length !== 1) {
  console.error(`GH_ASSET_RESOLUTION_FAILED:${matches.length}`);
  process.exit(1);
}
const asset = matches[0];
const digest = String(asset.digest || '');
if (!/^sha256:[0-9a-f]{64}$/.test(digest)) {
  console.error('GH_ASSET_DIGEST_MISSING');
  process.exit(1);
}
const url = String(asset.browser_download_url || '');
if (!/^https:\/\/github\.com\/cli\/cli\/releases\/download\//.test(url)) {
  console.error('GH_ASSET_URL_INVALID');
  process.exit(1);
}
process.stdout.write([asset.name, url, digest].join('\t'));
NODE
)" || fail "無法從 GitHub 官方 release metadata 解析可驗證的 macOS gh。"

  IFS=$'\t' read -r gh_asset_name gh_asset_url gh_asset_digest <<< "$gh_meta"
  test -n "$gh_asset_name" && test -n "$gh_asset_url" && test -n "$gh_asset_digest" \
    || fail "GitHub CLI release metadata 不完整。"

  gh_zip="$TMP_ROOT/$gh_asset_name"
  curl -fL --retry 3 "$gh_asset_url" -o "$gh_zip"
  expected="${gh_asset_digest#sha256:}"
  actual="$(shasum -a 256 "$gh_zip" | awk '{print $1}')"
  test "$actual" = "$expected" || fail "GitHub CLI 下載檔 SHA-256 驗證失敗。"

  gh_extract="$TMP_ROOT/gh"
  mkdir -p "$gh_extract"
  unzip -q "$gh_zip" -d "$gh_extract"
  GH_BIN="$(find "$gh_extract" -type f -path '*/bin/gh' -print -quit)"
  test -n "$GH_BIN" && test -x "$GH_BIN" || fail "GitHub CLI 解壓後找不到可執行檔。"
  "$GH_BIN" --version >/dev/null 2>&1 || fail "GitHub CLI 暫存執行檔無法啟動。"
  say "GitHub CLI 暫存版已完成 SHA-256 驗證；離開腳本後會自動刪除。"
}

ensure_gh

if ! "$GH_BIN" auth status -h github.com >/dev/null 2>&1; then
  say "GitHub 尚未登入；現在啟動一次瀏覽器登入。"
  "$GH_BIN" auth login -h github.com --git-protocol https --web
fi
"$GH_BIN" auth status -h github.com >/dev/null 2>&1 \
  || fail "GitHub 登入未完成。"
"$GH_BIN" repo view "$REPO" >/dev/null 2>&1 \
  || fail "目前 GitHub 身分無法存取 $REPO。"

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
printf '%s' "$OAUTH_B64" | "$GH_BIN" secret set "$SECRET_NAME" \
  --env "$ENVIRONMENT" \
  --repo "$REPO"
unset OAUTH_B64

UPDATED_AT="$("$GH_BIN" secret list --env "$ENVIRONMENT" --repo "$REPO" --json name,updatedAt \
  --jq ".[] | select(.name==\"$SECRET_NAME\") | .updatedAt" | head -n 1)"
test -n "$UPDATED_AT" || fail "GitHub Secret 寫入後讀回失敗。"

say "GitHub TEST Secret 已安全更新；值未顯示於終端輸出。"
say "readback updatedAt=$UPDATED_AT"

say "正在觸發 External TEST provider 部署……"
"$GH_BIN" workflow run deploy-external-test.yml --repo "$REPO" --ref deploy/test
say "已觸發。請回到 ChatGPT 輸入：授權完成"
say "ChatGPT 會接手檢查 Issue #39、匿名 Web App 黑箱與後續修復；你不需要再手改 GitHub 或 Apps Script。"
