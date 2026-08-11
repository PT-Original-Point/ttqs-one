import fs from 'node:fs';
import path from 'node:path';

const appRoot = path.resolve('apps-script');
const actual = fs.readdirSync(appRoot).filter((name) => fs.statSync(path.join(appRoot, name)).isFile()).sort();
const gs = actual.filter((name) => name.endsWith('.gs'));
const expected = ['appsscript.json', ...gs].sort();
if (gs.length !== 13) throw new Error(`Expected 13 .gs files, found ${gs.length}`);
if (actual.length !== expected.length || actual.some((name, i) => name !== expected[i])) {
  throw new Error(`Unsafe apps-script directory contents: ${JSON.stringify(actual)}`);
}
const ignore = fs.readFileSync('.claspignore', 'utf8').trim().split(/\r?\n/);
const expectedIgnore = ['**/**', '!appsscript.json', '!*.gs'];
if (JSON.stringify(ignore) !== JSON.stringify(expectedIgnore)) {
  throw new Error(`Unexpected .claspignore: ${JSON.stringify(ignore)}`);
}
const forbidden = ['scripts', 'tests', '.github', 'release', 'package.json', 'package-lock.json', 'README.md'];
for (const item of forbidden) {
  if (actual.includes(item)) throw new Error(`Forbidden deploy item in apps-script/: ${item}`);
}
console.log(JSON.stringify({ status: 'PASS', deployFiles: expected, count: expected.length }, null, 2));
