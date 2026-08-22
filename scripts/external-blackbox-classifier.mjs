import fs from 'node:fs';
import {fileURLToPath} from 'node:url';

export const REQUIRED_PRODUCT_MARKERS = [
  // Legacy R3/D8 product identity and anonymous TEST/SAMPLE boundary.
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

export const R7_REQUIRED_PRODUCT_MARKERS = [
  'TTQS ONE｜顧問唯讀 DEMO 查驗入口',
  'TEST／SAMPLE／CONTROL',
  '19/19',
  'Evidence Matrix',
  'FrozenArtifact',
  '共 129 / 129',
  '並非官方強制 129 份文件',
  'ER-DEMO-20260901-DRAFT-003',
  'SAMPLE 永不得轉 REAL',
  'runtime live Drive',
  '不得用於正式 TTQS 評分'
];

const FRIENDLY_ERROR_MARKERS = [
  '目前無法載入唯讀快照',
  'data-friendly-error="true"'
];

function normalizeAppsScriptHtmlServiceWrapperLayer(source) {
  const observedDoubleEscapedDoubleQuote = String.fromCharCode(92, 92, 34);
  return String(source)
    .split(observedDoubleEscapedDoubleQuote).join('"')
    .replace(/\\x22/g, '"')
    .replace(/\\u0022/g, '"')
    .replace(/\\\//g, '/')
    .replace(/\\x2[fF]/g, '/')
    .replace(/\\u002[fF]/g, '/')
    .replace(/\\x3[dD]/g, '=')
    .replace(/\\u003[dD]/g, '=')
    .replace(/&#0*61;/gi, '=')
    .replace(/&#x0*3d;/gi, '=')
    .replace(/&equals;/gi, '=');
}

export function normalizeAppsScriptHtmlServiceWrapper(source) {
  let normalized = String(source ?? '');
  for (let round = 0; round < 8; round += 1) {
    const next = normalizeAppsScriptHtmlServiceWrapperLayer(normalized);
    if (next === normalized) return normalized;
    normalized = next;
  }
  return normalized;
}

function directEvidence(normalized, expected, normalizedIndex) {
  if (normalizedIndex < 0) {
    return {
      matchType: 'NORMALIZED_SUBSTRING',
      normalizedIndex: -1,
      excerpt: null
    };
  }
  const padding = 48;
  const start = Math.max(0, normalizedIndex - padding);
  const end = Math.min(normalized.length, normalizedIndex + expected.length + padding);
  return {
    matchType: 'NORMALIZED_SUBSTRING',
    normalizedIndex,
    excerpt: normalized.slice(start, end)
  };
}

function buildMarkerEvidence(normalized, contractId, markers) {
  return markers.map((expected, index) => {
    const normalizedIndex = normalized.indexOf(expected);
    const pass = normalizedIndex >= 0;
    return {
      markerId: `${contractId}-M${String(index + 1).padStart(2, '0')}`,
      expected,
      actual: pass ? normalized.slice(normalizedIndex, normalizedIndex + expected.length) : null,
      result: pass ? 'PASS' : 'FAIL',
      evidence: directEvidence(normalized, expected, normalizedIndex)
    };
  });
}

function buildSafetyEvidence(normalized) {
  for (const marker of FRIENDLY_ERROR_MARKERS) {
    const normalizedIndex = normalized.indexOf(marker);
    if (normalizedIndex >= 0) {
      return {
        checkId: 'FRIENDLY_ERROR_ABSENT',
        expected: 'ABSENT',
        actual: marker,
        result: 'FAIL',
        evidence: directEvidence(normalized, marker, normalizedIndex)
      };
    }
  }
  return {
    checkId: 'FRIENDLY_ERROR_ABSENT',
    expected: 'ABSENT',
    actual: 'ABSENT',
    result: 'PASS',
    evidence: {
      matchType: 'NEGATIVE_NORMALIZED_SUBSTRING_CHECK',
      normalizedIndex: -1,
      excerpt: null
    }
  };
}

export function evaluateExternalBlackbox(source) {
  const normalized = normalizeAppsScriptHtmlServiceWrapper(source);
  const legacyEvidence = buildMarkerEvidence(normalized, 'LEGACY_R3_D8', REQUIRED_PRODUCT_MARKERS);
  const r7Evidence = buildMarkerEvidence(normalized, 'R7_DRAFT003', R7_REQUIRED_PRODUCT_MARKERS);
  const legacyPass = legacyEvidence.every(row => row.result === 'PASS');
  const r7Pass = r7Evidence.every(row => row.result === 'PASS');
  const safetyEvidence = buildSafetyEvidence(normalized);
  const safetyPass = safetyEvidence.result === 'PASS';
  const acceptedContractPass = legacyPass || r7Pass;
  const pass = acceptedContractPass && safetyPass;
  const mode = r7Pass ? 'R7_DRAFT003' : legacyPass ? 'LEGACY_R3_D8' : null;
  const legacyMissingCount = legacyEvidence.filter(row => row.result === 'FAIL').length;
  const r7MissingCount = r7Evidence.filter(row => row.result === 'FAIL').length;
  const evidenceMode = mode ?? (legacyMissingCount <= r7MissingCount ? 'LEGACY_R3_D8' : 'R7_DRAFT003');
  const markerEvidence = evidenceMode === 'R7_DRAFT003' ? r7Evidence : legacyEvidence;
  const markerPassCount = markerEvidence.filter(row => row.result === 'PASS').length;
  const missing = markerEvidence.filter(row => row.result === 'FAIL').map(row => row.expected);
  return {
    pass,
    mode,
    evidenceMode,
    missing,
    friendlyError: !safetyPass,
    markerEvidence,
    safetyEvidence,
    derivation: {
      markerPassCount,
      markerTotal: markerEvidence.length,
      selectedContractPass: markerEvidence.every(row => row.result === 'PASS'),
      safetyPass,
      acceptedContractPass,
      totalPass: pass
    }
  };
}

export function classifyExternalBlackbox(source) {
  return evaluateExternalBlackbox(source);
}

function isDirectExecution() {
  if (!process.argv[1]) return false;
  try {
    return fs.realpathSync(process.argv[1]) === fs.realpathSync(fileURLToPath(import.meta.url));
  } catch {
    return false;
  }
}

function parseArgs(argv) {
  let htmlPath = null;
  let evidenceOut = null;
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === '--html') {
      if (htmlPath || !argv[index + 1]) throw new Error('BLACKBOX_CLASSIFIER_ARGS_INVALID');
      htmlPath = argv[index + 1];
      index += 1;
      continue;
    }
    if (arg === '--evidence-out') {
      if (evidenceOut || !argv[index + 1]) throw new Error('BLACKBOX_CLASSIFIER_ARGS_INVALID');
      evidenceOut = argv[index + 1];
      index += 1;
      continue;
    }
    throw new Error('BLACKBOX_CLASSIFIER_ARGS_INVALID');
  }
  if (!htmlPath) throw new Error('BLACKBOX_CLASSIFIER_ARGS_INVALID');
  return {htmlPath, evidenceOut};
}

function writeEvidence(path, result) {
  if (!path) return;
  const receipt = {
    schema: 'TTQS_BLACKBOX_MARKER_EVIDENCE_V1',
    mode: result.mode,
    evidenceMode: result.evidenceMode,
    markerEvidence: result.markerEvidence,
    safetyEvidence: result.safetyEvidence,
    derivation: result.derivation
  };
  fs.writeFileSync(path, `${JSON.stringify(receipt, null, 2)}\n`, 'utf8');
}

function main() {
  const {htmlPath, evidenceOut} = parseArgs(process.argv.slice(2));
  const body = fs.readFileSync(htmlPath, 'utf8');
  const result = evaluateExternalBlackbox(body);
  writeEvidence(evidenceOut, result);
  for (const row of result.markerEvidence) {
    process.stdout.write(`BLACKBOX_MARKER_DETAIL ${JSON.stringify(row)}\n`);
  }
  process.stdout.write(`BLACKBOX_SAFETY_DETAIL ${JSON.stringify(result.safetyEvidence)}\n`);
  if (result.pass) {
    process.stdout.write(`BLACKBOX_MARKERS_PASS mode=${result.mode} markers=${result.derivation.markerPassCount}/${result.derivation.markerTotal} safety=${result.derivation.safetyPass ? 'PASS' : 'FAIL'}\n`);
    return;
  }
  process.stdout.write(`BLACKBOX_MARKERS_FAIL evidenceMode=${result.evidenceMode} missing=${result.missing.join('|') || 'none'} friendlyError=${result.friendlyError ? 1 : 0}\n`);
  process.exitCode = 2;
}

if (isDirectExecution()) main();
