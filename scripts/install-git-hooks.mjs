import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const hookDir = path.join(root, '.githooks');
const hookPath = path.join(hookDir, 'pre-push');
const hook = `#!/bin/sh\nset -eu\nnpm run build\n`;

fs.mkdirSync(hookDir, { recursive: true });
fs.writeFileSync(hookPath, hook, { mode: 0o755 });
try { fs.chmodSync(hookPath, 0o755); } catch {}
execFileSync('git', ['config', 'core.hooksPath', '.githooks'], { cwd: root, stdio: 'inherit' });
process.stdout.write('TTQS_PRE_PUSH_HOOK_INSTALLED .githooks/pre-push -> npm run build\n');
