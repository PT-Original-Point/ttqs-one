import fs from 'node:fs';
import {fileURLToPath} from 'node:url';

export const REQUIRED_PRODUCT_MARKERS = [
  // Product identity and anonymous TEST/SAMPLE boundary.
  'TTQS ONE · 測試／示範資料（TEST／SAMPLE）· EXTERNAL_READONLY',

  // D8 official 19-indicator semantics, including the two official sub-item clusters
  // that are easy to accidentally flatten during a UI refactor.
  '官方指標範圍',
  '19 / 19',
  '官方 19 指標評核語意導航',
  '12a 學員遴選',
  '12e 教學環境與設備',
  '17a 反應評估',
  '17d 成果評估',

  // D8 SAMPLE causal chain and four TEST form lifecycle projection.
  'SAMPLE 評核因果鏈',
  '四類 TEST Google Forms 生命週期',
  '4/4 類別都有 ACCEPTED 來源',

  // D6/S3 runtime proof required for the 9/1 consultant walkthrough.
  '故障 → 重試 → 對帳 → FINAL_ACCEPTED',
  'MATCHED_EXACTLY_ONCE',
  'AttemptHistory=append-only',

  // Evidence drill-down plus the controlled-source fallback contract.
  '19 指標佐證與來源下鑽',
  '查看佐證與來源',
  'Google Drive 連結只是選配，不是顧問調閱成功的必要條件',

  // External static/read-only and SAMPLE/REAL safety boundary.
  '不在執行期呼叫 Google Sheets／Drive API',
  '本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL'
];

export function normalizeAppsScriptHtmlServiceWrapper(source) {
  return String(source ?? '')
    .replace(/\\\//g, '/')
    .replace(/\\x2[fF]/g, '/')
    .replace(/\\u002[fF]/g, '/');
}

export function classifyExternalBlackbox(source) {
  const normalized = normalizeAppsScriptHtmlServiceWrapper(source);
  const missing = REQUIRED_PRODUCT_MARKERS.filter(marker => !normalized.includes(marker));
  const friendlyError = normalized.includes('目前無法載入唯讀快照');
  return {
    pass: missing.length === 0 && !friendlyError,
    missing,
    friendlyError
  };
}

function isDirectExecution() {
  if (!process.argv[1]) return false;
  try {
    return fs.realpathSync(process.argv[1]) === fs.realpathSync(fileURLToPath(import.meta.url));
  } catch {
    return false;
  }
}

function parseHtmlPath(argv) {
  const index = argv.indexOf('--html');
  if (index === -1 || !argv[index + 1] || argv[index + 2]) {
    throw new Error('BLACKBOX_CLASSIFIER_ARGS_INVALID');
  }
  return argv[index + 1];
}

function main() {
  const htmlPath = parseHtmlPath(process.argv.slice(2));
  const body = fs.readFileSync(htmlPath, 'utf8');
  const result = classifyExternalBlackbox(body);
  if (result.pass) {
    process.stdout.write('BLACKBOX_MARKERS_PASS\n');
    return;
  }
  process.stdout.write(`BLACKBOX_MARKERS_FAIL missing=${result.missing.join('|') || 'none'} friendlyError=${result.friendlyError ? 1 : 0}\n`);
  process.exitCode = 2;
}

if (isDirectExecution()) main();
