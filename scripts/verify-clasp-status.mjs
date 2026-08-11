import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2] || 'clasp-status.json';
const raw = fs.readFileSync(file, 'utf8').trim();
if (!raw) throw new Error('Empty clasp status output');
let parsed;
try {
  parsed = JSON.parse(raw);
} catch (err) {
  throw new Error(`clasp status is not JSON: ${raw.slice(0, 300)}`);
}

function collectStrings(value, out = []) {
  if (typeof value === 'string') out.push(value);
  else if (Array.isArray(value)) value.forEach((v) => collectStrings(v, out));
  else if (value && typeof value === 'object') Object.values(value).forEach((v) => collectStrings(v, out));
  return out;
}

const strings = collectStrings(parsed).map((s) => s.replaceAll('\\', '/'));
const appFiles = fs.readdirSync('apps-script').filter((n) => n === 'appsscript.json' || n.endsWith('.gs')).sort();
const matched = appFiles.filter((name) => strings.some((s) => s === name || s.endsWith('/' + name)));
const forbiddenPatterns = [
  /(^|\/)scripts\//,
  /(^|\/)tests\//,
  /(^|\/)\.github\//,
  /(^|\/)release\//,
  /package\.json$/,
  /package-lock\.json$/,
  /README\.md$/,
  /\.clasprc\.json$/,
  /\.clasp\.json$/
];
const forbiddenHits = strings.filter((s) => forbiddenPatterns.some((re) => re.test(s)));
if (forbiddenHits.length) throw new Error(`Forbidden clasp push-set entries: ${JSON.stringify(forbiddenHits)}`);
if (matched.length !== appFiles.length) {
  throw new Error(`clasp status missing expected deploy files. matched=${JSON.stringify(matched)} expected=${JSON.stringify(appFiles)} raw=${raw.slice(0, 1000)}`);
}
console.log(JSON.stringify({ status: 'PASS', matched: matched.sort(), count: matched.length }, null, 2));
