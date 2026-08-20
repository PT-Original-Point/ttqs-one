import fs from 'node:fs';
import { normalizeRegistry, verifyReportedHashes } from './hash-registry-control.mjs';

function parseArgs(argv) {
  const out = { registry: null, inputs: [], context: 'REPORT' };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--registry') out.registry = argv[++i];
    else if (arg === '--input') out.inputs.push(argv[++i]);
    else if (arg === '--context') out.context = argv[++i];
    else throw new Error(`unknown argument: ${arg}`);
  }
  if (!out.registry) throw new Error('--registry is required; verification fails closed without an authoritative registry export/readback');
  if (!out.inputs.length) throw new Error('at least one --input file is required');
  return out;
}

const options = parseArgs(process.argv.slice(2));
const registryRaw = JSON.parse(fs.readFileSync(options.registry, 'utf8'));
const registry = normalizeRegistry(registryRaw);
const aggregate = [];
let failed = false;
for (const input of options.inputs) {
  const text = fs.readFileSync(input, 'utf8');
  const result = verifyReportedHashes(registry, text, `${options.context}:${input}`);
  aggregate.push({ input, ...result });
  if (result.status !== 'PASS') failed = true;
}

const output = {
  status: failed ? 'FAIL' : 'PASS',
  policy: 'Every reported 64-hex SHA-256 must resolve to a READBACK_MATCHED_COMPUTED Hash Registry entry',
  registry_entries: registry.entries.length,
  results: aggregate
};

const writer = failed ? console.error : console.log;
writer(JSON.stringify(output, null, 2));
if (failed) process.exit(1);
