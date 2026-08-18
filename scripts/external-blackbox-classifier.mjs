import fs from 'node:fs';
import {fileURLToPath} from 'node:url';

export const REQUIRED_PRODUCT_MARKERS = [
  'TTQS ONE · 測試／示範資料（TEST／SAMPLE）· EXTERNAL_READONLY',
  '官方指標範圍',
  '19 / 19',
  'SAMPLE 評核因果鏈',
  '19 指標佐證與來源下鑽',
  '查看佐證與來源'
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
