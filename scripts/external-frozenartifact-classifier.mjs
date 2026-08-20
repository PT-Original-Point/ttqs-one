import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {normalizeAppsScriptHtmlServiceWrapper} from './external-blackbox-classifier.mjs';

export const FROZEN_ARTIFACT_ID = 'FA-DEMO-002';
export const CANONICAL_EXEC_URL = 'https://script.google.com/macros/s/AKfycbznbXi-0XWNV68E-vGU9CiAE6ElXGIlDmy27EePXMdGpRaorURzKZq0dDgsNBaaZOLh/exec';
export const REQUIRED_CONTENT_MARKERS = [
  '四、FrozenArtifact enforcement（F-01/F-02）',
  'ER-03: 委員主查驗路徑以 frozen copy 為準'
];

function decodeWrapperForInspection(source) {
  return normalizeAppsScriptHtmlServiceWrapper(source)
    .replace(/\\x3[cC]|\\u003[cC]/g, '<')
    .replace(/\\x3[eE]|\\u003[eE]/g, '>')
    .replace(/\\x26|\\u0026/g, '&')
    .replace(/\\x27|\\u0027/g, "'")
    .replace(/\\x22|\\u0022/g, '"')
    .replace(/\\n/g, '\n')
    .replace(/\\r/g, '\r')
    .replace(/\\t/g, '\t');
}

function decodeEntities(value) {
  return value
    .replace(/&nbsp;/gi, ' ')
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>')
    .replace(/&quot;/gi, '"')
    .replace(/&#39;|&#x27;/gi, "'")
    .replace(/&amp;/gi, '&');
}

function normalizeText(value) {
  return decodeEntities(String(value ?? '').replace(/<[^>]+>/g, ' ').replace(/\\["']/g, '').replace(/\s+/g, ' ').trim());
}

function artifactPayloadText(source) {
  const decoded = decodeWrapperForInspection(source);
  const pre = decoded.match(/<pre\b[^>]*class=["']?frozen-text["']?[^>]*>([\s\S]*?)<\/pre>/i)?.[1];
  if (pre) return normalizeText(pre);
  const first = decoded.indexOf(REQUIRED_CONTENT_MARKERS[0]);
  const second = decoded.indexOf(REQUIRED_CONTENT_MARKERS[1]);
  if (first >= 0 && second >= 0) {
    const start = Math.min(first, second);
    const end = Math.max(first + REQUIRED_CONTENT_MARKERS[0].length, second + REQUIRED_CONTENT_MARKERS[1].length);
    return normalizeText(decoded.slice(start, end));
  }
  return normalizeText(decoded
    .replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi, ' ')
    .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, ' '));
}

function extractAttr(source, name) {
  const decoded = decodeWrapperForInspection(source);
  const re = new RegExp(`${name}\\s*=\\s*\\?["']([^"']+)\\?["']`, 'i');
  return decoded.match(re)?.[1] || '';
}

function extractRenderedArtifactId(source) {
  const decoded = decodeWrapperForInspection(source);
  const attr = extractAttr(source, 'data-artifact-id');
  if (attr) return attr;
  const labelMatch = decoded.match(/artifact_id[\s\S]{0,320}?(FA-DEMO-[A-Za-z0-9_-]+)/i);
  if (labelMatch) return labelMatch[1];
  return '';
}

function extractTitle(source) {
  const decoded = decodeWrapperForInspection(source);
  const h1 = decoded.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/i)?.[1] || '';
  const title = decoded.match(/<title\b[^>]*>([\s\S]*?)<\/title>/i)?.[1] || '';
  return normalizeText(h1 || title);
}

function evidence(actual, extra = {}) { return {actual, ...extra}; }

export function classifyFrozenArtifact({source, requestedUrl, requestedArtifactId, httpStatus, effectiveUrl = ''}) {
  const decoded = decodeWrapperForInspection(source);
  const text = artifactPayloadText(source);
  const renderedArtifactId = extractRenderedArtifactId(source);
  const title = extractTitle(source);
  const friendlyError = decoded.includes('找不到指定的評核凍結文件') || decoded.includes('目前無法載入唯讀快照');
  const expectedUrl = `${CANONICAL_EXEC_URL}?artifact=${encodeURIComponent(requestedArtifactId)}`;
  const markerResults = REQUIRED_CONTENT_MARKERS.map((marker) => ({marker, pass: decoded.includes(marker), actual: decoded.includes(marker) ? marker : 'MISSING'}));
  const checks = [
    {id:'FA-01', expected:expectedUrl, pass:requestedUrl === expectedUrl && requestedArtifactId === FROZEN_ARTIFACT_ID, evidence:evidence(requestedUrl,{effectiveUrl,note:'Google may use internal delivery URLs after the canonical navigation target; browser top-level address remains a HUMAN check.'})},
    {id:'FA-02', expected:'artifact payload visible text >= 200 and not a friendly-error shell', pass:text.length >= 200 && !friendlyError, evidence:evidence(text.length,{friendlyError,measurement:'decoded frozen artifact payload, wrapper-safe'})},
    {id:'FA-03', expected:'non-empty document title', pass:title.length > 0, evidence:evidence(title)},
    {id:'FA-04', expected:'visible TEST/CONTROL simulation warning and explicit non-REAL boundary', pass:decoded.includes('模擬評核查驗｜TEST／CONTROL｜非正式事證') && decoded.includes('不是協會 REAL 辦訓紀錄'), evidence:evidence(decoded.includes('模擬評核查驗｜TEST／CONTROL｜非正式事證') ? 'warning-present' : 'warning-missing')},
    {id:'FA-05', expected:requestedArtifactId, pass:requestedArtifactId === FROZEN_ARTIFACT_ID && renderedArtifactId === requestedArtifactId, evidence:evidence(renderedArtifactId,{requestedArtifactId,manifestReference:FROZEN_ARTIFACT_ID,measurement:'data attribute or visible artifact_id table field'})},
    {id:'FA-06', expected:REQUIRED_CONTENT_MARKERS, pass:markerResults.length >= 2 && markerResults.every((item)=>item.pass), evidence:markerResults}
  ];
  const machineInputsPass = checks.every((item)=>item.pass);
  checks.push({id:'FA-07', expected:'HTTP 200 + FA-01..FA-06 all PASS; HTTP 200 alone is insufficient', pass:String(httpStatus)==='200' && machineInputsPass && !friendlyError, evidence:evidence(String(httpStatus),{fa01ToFa06Pass:machineInputsPass,friendlyError})});
  checks.push({id:'FA-08', expected:'clean-browser human visual confirmation', pass:null, result:'HUMAN_REQUIRED', evidence:evidence('NOT_MACHINE_DECIDABLE')});
  return {artifactId:requestedArtifactId,requestedUrl,effectiveUrl,httpStatus:String(httpStatus),friendlyError,machinePass:checks.slice(0,7).every((item)=>item.pass),checks:checks.map((item)=>({...item,result:item.result||(item.pass?'PASS':'FAIL')}))};
}

function isDirectExecution(){if(!process.argv[1])return false;try{return fs.realpathSync(process.argv[1])===fs.realpathSync(fileURLToPath(import.meta.url));}catch{return false;}}
function parseArgs(argv){const out={};for(let i=0;i<argv.length;i+=2){const key=argv[i],value=argv[i+1];if(!key?.startsWith('--')||value===undefined)throw new Error('FROZEN_CLASSIFIER_ARGS_INVALID');out[key.slice(2)]=value;}for(const key of ['html','requested-url','artifact-id','http-status'])if(!out[key])throw new Error(`FROZEN_CLASSIFIER_ARG_MISSING:${key}`);return out;}
function main(){const args=parseArgs(process.argv.slice(2));const source=fs.readFileSync(args.html,'utf8');const result=classifyFrozenArtifact({source,requestedUrl:args['requested-url'],requestedArtifactId:args['artifact-id'],httpStatus:args['http-status'],effectiveUrl:args['effective-url']||''});process.stdout.write(`${JSON.stringify(result,null,2)}\n`);process.stdout.write(result.machinePass?'FROZEN_ARTIFACT_MACHINE_PASS\n':'FROZEN_ARTIFACT_MACHINE_FAIL\n');if(!result.machinePass)process.exitCode=2;}
if(isDirectExecution())main();
