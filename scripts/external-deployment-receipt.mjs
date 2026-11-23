import fs from 'node:fs';

const MARKER = '<!-- TTQS_EXTERNAL_TEST_RECEIPT_V1 -->';
export const NOTES_MARKER = '<!-- TTQS_EXTERNAL_TEST_NOTES -->';
const VALID_STATES = new Set(['RUNNING', 'FAILED', 'PASS_PRODUCT_BLACKBOX']);

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i];
    const value = argv[i + 1];
    if (!key?.startsWith('--') || value === undefined) throw new Error('RECEIPT_ARGS_INVALID');
    out[key.slice(2)] = value;
  }
  return out;
}

function validateSha(value, code) {
  if (!/^[0-9a-f]{40}$/.test(String(value || ''))) throw new Error(code);
}

function preservedNotes(body) {
  const source = String(body || '');
  const index = source.indexOf(NOTES_MARKER);
  return index === -1 ? '' : source.slice(index).trimEnd();
}

export function parseReceiptBody(body) {
  if (!String(body || '').includes(MARKER)) throw new Error('EXTERNAL_RECEIPT_MARKER_MISSING');
  const match = String(body).match(/<!-- TTQS_EXTERNAL_TEST_RECEIPT_V1 -->[\s\S]*?```json\s*([\s\S]*?)```/);
  if (!match) throw new Error('EXTERNAL_RECEIPT_JSON_MISSING');
  const receipt = JSON.parse(match[1]);
  if (receipt.schema !== 'TTQS_EXTERNAL_TEST_RECEIPT_V1') throw new Error('EXTERNAL_RECEIPT_SCHEMA_INVALID');
  if (receipt.environment !== 'TEST' || receipt.rootDir !== 'external-viewer') throw new Error('EXTERNAL_RECEIPT_CONTEXT_INVALID');
  if (Number(receipt.realProdTouch || 0) !== 0) throw new Error('EXTERNAL_RECEIPT_REAL_PROD_TOUCH_INVALID');
  if (receipt.verificationSha) validateSha(receipt.verificationSha, 'EXTERNAL_RECEIPT_VERIFICATION_SHA_INVALID');
  return receipt;
}

function validateScriptId(value) {
  if (value && !/^[A-Za-z0-9_-]{20,}$/.test(value)) throw new Error('EXTERNAL_RECEIPT_SCRIPT_ID_INVALID');
}

function validateDeploymentId(value) {
  if (value && !/^AKfy[A-Za-z0-9_-]+$/.test(value)) throw new Error('EXTERNAL_RECEIPT_DEPLOYMENT_ID_INVALID');
}

function validateWebappUrl(value, deploymentId) {
  if (!value) return;
  const expected = `https://script.google.com/macros/s/${deploymentId}/exec`;
  if (!deploymentId || value !== expected) throw new Error('EXTERNAL_RECEIPT_WEBAPP_URL_INVALID');
}

export function nextReceiptBody(body, state, env = {}) {
  if (!VALID_STATES.has(state)) throw new Error('EXTERNAL_RECEIPT_STATE_INVALID');
  const prior = parseReceiptBody(body);
  const verificationSha = String(env.GITHUB_SHA || '').trim();
  validateSha(verificationSha, 'EXTERNAL_RECEIPT_SOURCE_SHA_INVALID');

  // A black-box-only verification must not pretend verifier-only commits were
  // deployed to Apps Script. Full provider deployments leave the override empty
  // and therefore use GITHUB_SHA as both sourceSha and verificationSha.
  const sourceSha = String(env.EXTERNAL_RECEIPT_SOURCE_SHA || verificationSha).trim();
  validateSha(sourceSha, 'EXTERNAL_RECEIPT_SOURCE_SHA_INVALID');

  const scriptId = String(env.EXTERNAL_SCRIPT_ID_RESOLVED || prior.scriptId || '').trim();
  const deploymentId = String(env.EXTERNAL_DEPLOYMENT_ID_RESOLVED || prior.deploymentId || '').trim();
  const webappUrl = String(env.EXTERNAL_WEBAPP_URL || prior.webappUrl || '').trim();
  validateScriptId(scriptId);
  validateDeploymentId(deploymentId);
  if (deploymentId && !scriptId) throw new Error('EXTERNAL_RECEIPT_DEPLOYMENT_WITHOUT_SCRIPT');
  validateWebappUrl(webappUrl, deploymentId);

  if (state === 'PASS_PRODUCT_BLACKBOX' && (!scriptId || !deploymentId || !webappUrl)) {
    throw new Error('EXTERNAL_RECEIPT_PASS_IDENTIFIERS_REQUIRED');
  }

  const receipt = {
    schema: 'TTQS_EXTERNAL_TEST_RECEIPT_V1',
    environment: 'TEST',
    rootDir: 'external-viewer',
    runStatus: state,
    sourceSha,
    verificationSha,
    scriptId,
    deploymentId,
    webappUrl,
    anonymousBlackbox: state === 'PASS_PRODUCT_BLACKBOX' ? 'PASS' : (state === 'FAILED' ? 'NOT_PASS' : 'NOT_RUN'),
    workflowRunId: String(env.GITHUB_RUN_ID || ''),
    realProdTouch: 0
  };

  const headline = state === 'PASS_PRODUCT_BLACKBOX'
    ? '此 Issue 是 TEST／SAMPLE 控制面。匿名產品黑箱已通過。'
    : '此 Issue 是 TEST／SAMPLE 控制面。非 PASS 狀態不得解讀為成品驗收通過。';

  const generated = [
    '# TTQS ONE TEST External Evaluator Portal Deployment Receipt',
    '',
    headline,
    '',
    `目前狀態：\`${state}\``,
    '',
    MARKER,
    '```json',
    JSON.stringify(receipt, null, 2),
    '```',
    '',
    '部署成功不代表 REAL／PROD 啟動；`realProdTouch` 必須維持 0。'
  ].join('\n');

  const notes = preservedNotes(body);
  return notes ? `${generated}\n\n${notes}\n` : `${generated}\n`;
}

if (process.argv[1] && import.meta.url === new URL(`file://${process.argv[1]}`).href) {
  const args = parseArgs(process.argv.slice(2));
  if (!args.input || !args.output || !args.state) throw new Error('RECEIPT_ARGS_REQUIRED');
  const body = fs.readFileSync(args.input, 'utf8');
  fs.writeFileSync(args.output, nextReceiptBody(body, args.state, process.env));
}
