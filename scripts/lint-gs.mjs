import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const root = path.resolve('apps-script');
const files = fs.readdirSync(root).filter((name) => name.endsWith('.gs')).sort();
if (files.length !== 16) throw new Error(`Expected 16 Apps Script sources, found ${files.length}`);
for (const file of files) {
  const code = fs.readFileSync(path.join(root, file), 'utf8');
  new vm.Script(code, { filename: file });
}
console.log(`PASS Apps Script parse ${files.length}/${files.length}`);