const HASH_RE = /(?<![0-9a-fA-F])(?:sha256:)?([0-9a-fA-F]{64})(?![0-9a-fA-F])/g;

function normalizeHex(value) {
  const text = String(value || '').trim().toLowerCase();
  const hex = text.startsWith('sha256:') ? text.slice(7) : text;
  if (!/^[0-9a-f]{64}$/.test(hex)) throw new Error(`invalid SHA-256 value: ${value}`);
  return hex;
}

function rowsFromSheet(values) {
  if (!Array.isArray(values) || values.length < 2) return [];
  const headers = values[0].map((value) => String(value));
  return values.slice(1).filter((row) => row.some((value) => String(value ?? '').trim() !== '')).map((row) => {
    const entry = {};
    for (let i = 0; i < headers.length; i += 1) entry[headers[i]] = row[i] ?? '';
    return entry;
  });
}

export function normalizeRegistry(input) {
  let entries;
  if (Array.isArray(input)) entries = input;
  else if (Array.isArray(input?.entries)) entries = input.entries;
  else if (Array.isArray(input?.values)) entries = rowsFromSheet(input.values);
  else if (Array.isArray(input?.result?.values)) entries = rowsFromSheet(input.result.values);
  else throw new Error('registry input must contain entries[] or sheet values[]');

  const byId = new Map();
  const byHash = new Map();
  for (const raw of entries) {
    const registryId = String(raw.registry_id || '').trim();
    const readbackStatus = String(raw.readback_status || '').trim();
    const computed = String(raw.computed_hash || '').trim();
    if (!registryId || !computed) continue;
    if (readbackStatus !== 'READBACK_MATCHED_COMPUTED') continue;
    const hex = normalizeHex(computed);
    if (byId.has(registryId)) throw new Error(`duplicate registry_id: ${registryId}`);
    if (byHash.has(hex)) throw new Error(`duplicate registered hash: ${hex}`);
    const entry = { ...raw, registry_id: registryId, computed_hash: `sha256:${hex}`, hash_hex: hex };
    byId.set(registryId, entry);
    byHash.set(hex, entry);
  }
  if (byId.size === 0) throw new Error('registry has no READBACK_MATCHED_COMPUTED entries');
  return { byId, byHash, entries: [...byId.values()] };
}

export function resolveRegisteredHash(registry, registryId) {
  const normalized = registry?.byId instanceof Map ? registry : normalizeRegistry(registry);
  const entry = normalized.byId.get(String(registryId));
  if (!entry) throw new Error(`registry_id not found or not readback-matched: ${registryId}`);
  return entry.computed_hash;
}

export function scanSha256Values(text) {
  const values = [];
  const source = String(text ?? '');
  HASH_RE.lastIndex = 0;
  for (const match of source.matchAll(HASH_RE)) {
    values.push({ raw: match[0], hash_hex: match[1].toLowerCase(), index: match.index });
  }
  return values;
}

export function verifyReportedHashes(registry, text, context = 'REPORT') {
  const normalized = registry?.byHash instanceof Map ? registry : normalizeRegistry(registry);
  const seen = scanSha256Values(text);
  const anchored = [];
  const unanchored = [];
  for (const occurrence of seen) {
    const entry = normalized.byHash.get(occurrence.hash_hex);
    if (entry) {
      anchored.push({ ...occurrence, registry_id: entry.registry_id });
    } else {
      unanchored.push({ ...occurrence, status: 'UNANCHORED_HASH', context });
    }
  }
  return {
    status: unanchored.length ? 'FAIL' : 'PASS',
    context,
    scanned: seen.length,
    anchored,
    unanchored,
    gap_events: unanchored.map((item) => ({
      area: 'REPORT_INTEGRITY',
      severity: 'HIGH',
      finding: '64-hex SHA-256 value is not present in the authoritative readback-matched Hash Registry',
      reported_value: `sha256:${item.hash_hex}`,
      corrected_or_expected_value: 'Human confirmation required; register authoritative value first or remove/correct the unanchored value',
      status: 'OPEN',
      source_context: context
    }))
  };
}
