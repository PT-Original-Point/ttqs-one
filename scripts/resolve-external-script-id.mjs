import fs from 'node:fs';

export function resolveExternalScriptId(text, title) {
  if (!title || !String(title).trim()) throw new Error('EXTERNAL_SCRIPT_TITLE_REQUIRED');
  const matches = [];
  for (const raw of String(text || '').split(/\r?\n/)) {
    const line = raw.trim();
    if (!line.startsWith(title)) continue;
    const tail = line.slice(title.length).trim();
    const match = tail.match(/^[–—-]\s*([A-Za-z0-9_-]{20,})(?:\s|$)/);
    if (match) matches.push(match[1]);
  }
  const unique = [...new Set(matches)];
  if (unique.length > 1) throw new Error('EXTERNAL_SCRIPT_TITLE_AMBIGUOUS');
  return unique[0] || '';
}

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i];
    const value = argv[i + 1];
    if (!key?.startsWith('--') || value === undefined) throw new Error('RESOLVE_ARGS_INVALID');
    out[key.slice(2)] = value;
  }
  return out;
}

if (process.argv[1] && import.meta.url === new URL(`file://${process.argv[1]}`).href) {
  const args = parseArgs(process.argv.slice(2));
  if (!args.input || !args.title) throw new Error('RESOLVE_ARGS_REQUIRED');
  const text = fs.readFileSync(args.input, 'utf8');
  process.stdout.write(resolveExternalScriptId(text, args.title));
}
