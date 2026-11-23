import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';

const root=process.cwd();
const r7Dir=path.join(root,'release','official129');
const sourceDir=path.join(root,'external-viewer');
const basePath=path.join(r7Dir,'R3BaseCode.gs');
const currentPath=path.join(sourceDir,'Code.gs');

fs.mkdirSync(r7Dir,{recursive:true});
if(!fs.existsSync(basePath)){
  const current=fs.readFileSync(currentPath,'utf8');
  if(current.includes('build-time injected R7 frozen projection'))throw new Error('R7_BASE_BACKUP_MISSING_AFTER_MATERIALIZATION');
  fs.writeFileSync(basePath,current);
}
execFileSync(process.execPath,['scripts/build-external-official129.mjs'],{cwd:root,stdio:'inherit'});
const built=path.join(root,'.external-viewer-build','Code.gs');
if(!fs.existsSync(built))throw new Error('R7_BUILT_CODE_MISSING');
fs.copyFileSync(built,currentPath);
process.stdout.write(`R7_EXTERNAL_MATERIALIZE_PASS base=${path.relative(root,basePath)} target=${path.relative(root,currentPath)} bytes=${fs.statSync(currentPath).size}\n`);
