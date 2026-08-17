import fs from 'node:fs';

const sourcePath = 'apps-script/S3Foundation.gs';
const testPath = 'tests/gate-a-responseid-foundation.test.mjs';
const workflowPath = '.github/workflows/gate-a-builder.yml';
const selfPath = '.github/scripts/gate-a-builder.mjs';

const marker = "var TTQS_GATE_A_SOURCE_TYPE = 'GOOGLE_FORM_RESPONSE';";
const original = fs.readFileSync(sourcePath, 'utf8');
if (original.includes(marker)) throw new Error('GATE_A_FOUNDATION_ALREADY_PRESENT');

const appendix = String.raw`

var TTQS_GATE_A_SOURCE_TYPE = 'GOOGLE_FORM_RESPONSE';
var TTQS_GATE_A_SCHEMA_VERSION = 'GATE_A_V1';

function ttqsGateARequireString_(value, code) {
  var text = String(value === undefined || value === null ? '' : value).trim();
  if (!text) throw new Error(code || 'GATE_A_VALUE_REQUIRED');
  return text;
}

function ttqsGateACanonicalize_(value) {
  if (value === null) return null;
  var type = typeof value;
  if (type === 'string' || type === 'boolean') return value;
  if (type === 'number') {
    if (!isFinite(value)) throw new Error('GATE_A_CANONICAL_NUMBER_INVALID');
    return value;
  }
  if (Array.isArray(value)) {
    return value.map(function(item) { return ttqsGateACanonicalize_(item); });
  }
  if (type === 'object') {
    var out = {};
    Object.keys(value).sort().forEach(function(key) {
      if (value[key] === undefined) throw new Error('GATE_A_CANONICAL_UNDEFINED:' + key);
      out[key] = ttqsGateACanonicalize_(value[key]);
    });
    return out;
  }
  throw new Error('GATE_A_CANONICAL_TYPE_UNSUPPORTED:' + type);
}

function ttqsGateACanonicalJson_(value) {
  return JSON.stringify(ttqsGateACanonicalize_(value));
}

function ttqsGateADigestCanonical_(value) {
  return ttqsDigest_(ttqsGateACanonicalJson_(value));
}

function ttqsGateAResponseIdentity_(formId, responseId) {
  var form = ttqsGateARequireString_(formId, 'GATE_A_FORM_ID_REQUIRED');
  var response = ttqsGateARequireString_(responseId, 'GATE_A_RESPONSE_ID_REQUIRED');
  return ttqsGateADigestCanonical_({
    sourceType: TTQS_GATE_A_SOURCE_TYPE,
    formId: form,
    responseId: response
  });
}

function ttqsGateANormalizeProviderTimestamp_(value, code) {
  var text = ttqsGateARequireString_(value, code || 'GATE_A_TIMESTAMP_REQUIRED');
  var match = /^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(\d{3}|\d{6}|\d{9}))?Z$/.exec(text);
  if (!match) throw new Error((code || 'GATE_A_TIMESTAMP_INVALID') + ':' + text);
  var millis = Date.parse(match[1] + (match[2] ? '.' + match[2].slice(0, 3) : '') + 'Z');
  if (!isFinite(millis)) throw new Error((code || 'GATE_A_TIMESTAMP_INVALID') + ':' + text);
  return text;
}

function ttqsGateATimestampParts_(value) {
  var normalized = ttqsGateANormalizeProviderTimestamp_(value, 'GATE_A_TIMESTAMP_INVALID');
  var match = /^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(\d{3}|\d{6}|\d{9}))?Z$/.exec(normalized);
  var seconds = Date.parse(match[1] + 'Z') / 1000;
  var nanos = Number(String(match[2] || '').padEnd(9, '0') || '0');
  return { seconds: seconds, nanos: nanos };
}

function ttqsGateAMaxTimestamp_(current, candidate) {
  var next = ttqsGateANormalizeProviderTimestamp_(candidate, 'GATE_A_PROVIDER_LAST_SUBMITTED_TIME_INVALID');
  if (!current) return next;
  var currentNormalized = ttqsGateANormalizeProviderTimestamp_(current, 'GATE_A_CANDIDATE_WATERMARK_INVALID');
  var a = ttqsGateATimestampParts_(currentNormalized);
  var b = ttqsGateATimestampParts_(next);
  if (b.seconds > a.seconds || (b.seconds === a.seconds && b.nanos > a.nanos)) return next;
  return currentNormalized;
}

function ttqsGateAUniqueSortedIds_(values, code) {
  if (!Array.isArray(values)) throw new Error((code || 'GATE_A_FIELD_IDS_INVALID') + ':NOT_ARRAY');
  var seen = Object.create(null);
  var out = [];
  values.forEach(function(value) {
    var id = ttqsGateARequireString_(value, code || 'GATE_A_FIELD_ID_REQUIRED');
    if (seen[id]) throw new Error((code || 'GATE_A_DUPLICATE_FIELD_ID') + ':' + id);
    seen[id] = true;
    out.push(id);
  });
  out.sort();
  return out;
}

function ttqsGateASchemaContract_(schemaVersion, expectedFieldIds, requiredFieldIds) {
  var version = ttqsGateARequireString_(schemaVersion || TTQS_GATE_A_SCHEMA_VERSION, 'GATE_A_SCHEMA_VERSION_REQUIRED');
  var expected = ttqsGateAUniqueSortedIds_(expectedFieldIds, 'GATE_A_SCHEMA_EXPECTED_FIELD_INVALID');
  if (!expected.length) throw new Error('GATE_A_SCHEMA_EXPECTED_FIELDS_REQUIRED');
  var required = ttqsGateAUniqueSortedIds_(requiredFieldIds || [], 'GATE_A_SCHEMA_REQUIRED_FIELD_INVALID');
  var expectedMap = Object.create(null);
  expected.forEach(function(id) { expectedMap[id] = true; });
  required.forEach(function(id) {
    if (!expectedMap[id]) throw new Error('GATE_A_SCHEMA_REQUIRED_NOT_EXPECTED:' + id);
  });
  return {
    schema_version: version,
    expected_field_ids: expected,
    required_field_ids: required,
    field_signature: ttqsGateADigestCanonical_({ schemaVersion: version, fieldIds: expected })
  };
}

function ttqsGateAValidateResponseSchema_(response, schema) {
  if (!schema || !Array.isArray(schema.expected_field_ids)) throw new Error('GATE_A_SCHEMA_CONTRACT_REQUIRED');
  var answers = response && response.answers ? response.answers : {};
  if (!answers || typeof answers !== 'object' || Array.isArray(answers)) throw new Error('GATE_A_ANSWERS_INVALID');
  var expected = Object.create(null);
  schema.expected_field_ids.forEach(function(id) { expected[id] = true; });
  Object.keys(answers).forEach(function(id) {
    if (!expected[id]) throw new Error('GATE_A_SCHEMA_DRIFT_UNKNOWN_FIELD:' + id);
  });
  schema.required_field_ids.forEach(function(id) {
    if (!Object.prototype.hasOwnProperty.call(answers, id)) throw new Error('GATE_A_SCHEMA_REQUIRED_FIELD_MISSING:' + id);
  });
  return true;
}

function ttqsGateAResponsePayload_(response) {
  var answers = response && response.answers ? response.answers : {};
  return ttqsGateACanonicalize_({ answers: answers });
}

function ttqsGateAPlanOverlapRequest_(formId, committedWatermark, overlapMs, initialWindowStart) {
  var form = ttqsGateARequireString_(formId, 'GATE_A_FORM_ID_REQUIRED');
  var overlap = Number(overlapMs || 0);
  if (!isFinite(overlap) || overlap < 0 || Math.floor(overlap) !== overlap) throw new Error('GATE_A_OVERLAP_MS_INVALID');
  var committed = String(committedWatermark || '').trim();
  var windowStart;
  if (committed) {
    var normalizedCommitted = ttqsGateANormalizeProviderTimestamp_(committed, 'GATE_A_COMMITTED_WATERMARK_INVALID');
    var startMillis = Date.parse(normalizedCommitted) - overlap;
    if (!isFinite(startMillis)) throw new Error('GATE_A_OVERLAP_WINDOW_INVALID');
    windowStart = new Date(startMillis).toISOString();
    committed = normalizedCommitted;
  } else {
    windowStart = ttqsGateANormalizeProviderTimestamp_(initialWindowStart, 'GATE_A_INITIAL_WINDOW_START_REQUIRED');
  }
  return {
    form_id: form,
    filter: 'timestamp >= ' + windowStart,
    window_start: windowStart,
    committed_watermark_snapshot: committed
  };
}

function ttqsGateANewRun_(requestContext, runId) {
  if (!requestContext) throw new Error('GATE_A_REQUEST_CONTEXT_REQUIRED');
  return {
    run_id: ttqsGateARequireString_(runId, 'GATE_A_RUN_ID_REQUIRED'),
    form_id: ttqsGateARequireString_(requestContext.form_id, 'GATE_A_FORM_ID_REQUIRED'),
    filter: ttqsGateARequireString_(requestContext.filter, 'GATE_A_FILTER_REQUIRED'),
    window_start: ttqsGateANormalizeProviderTimestamp_(requestContext.window_start, 'GATE_A_WINDOW_START_INVALID'),
    committed_watermark_snapshot: String(requestContext.committed_watermark_snapshot || ''),
    next_page_token: '',
    page_ordinal: 0,
    staged_response_ids: [],
    staged_records: {},
    candidate_high_watermark: String(requestContext.committed_watermark_snapshot || ''),
    page_checkpoints: [],
    last_checkpoint: null,
    run_complete: false,
    reconciliation: null,
    final_watermark_candidate: ''
  };
}

function ttqsGateARequestForPage_(state) {
  if (!state) throw new Error('GATE_A_RUN_STATE_REQUIRED');
  if (state.run_complete) throw new Error('GATE_A_RUN_ALREADY_COMPLETE');
  return {
    formId: ttqsGateARequireString_(state.form_id, 'GATE_A_FORM_ID_REQUIRED'),
    filter: ttqsGateARequireString_(state.filter, 'GATE_A_FILTER_REQUIRED'),
    pageToken: String(state.next_page_token || '')
  };
}

function ttqsGateABuildL1Record_(request, response, schema, observedAt, runId, pageOrdinal) {
  if (!request) throw new Error('GATE_A_PAGE_REQUEST_REQUIRED');
  var requestFormId = ttqsGateARequireString_(request.formId, 'GATE_A_FORM_ID_REQUIRED');
  var providerFormId = ttqsGateARequireString_(response && response.formId, 'GATE_A_PROVIDER_FORM_ID_REQUIRED');
  if (providerFormId !== requestFormId) throw new Error('GATE_A_PROVIDER_FORM_ID_MISMATCH');
  var responseId = ttqsGateARequireString_(response && response.responseId, 'GATE_A_RESPONSE_ID_REQUIRED');
  ttqsGateAValidateResponseSchema_(response, schema);
  var payload = ttqsGateAResponsePayload_(response);
  var ordinal = Number(pageOrdinal);
  if (!isFinite(ordinal) || ordinal < 1 || Math.floor(ordinal) !== ordinal) throw new Error('GATE_A_PAGE_ORDINAL_INVALID');
  return {
    environment: 'TEST',
    source_type: TTQS_GATE_A_SOURCE_TYPE,
    form_id: requestFormId,
    response_id: responseId,
    source_identity: ttqsGateAResponseIdentity_(requestFormId, responseId),
    provider_create_time: ttqsGateANormalizeProviderTimestamp_(response.createTime, 'GATE_A_PROVIDER_CREATE_TIME_INVALID'),
    provider_last_submitted_time: ttqsGateANormalizeProviderTimestamp_(response.lastSubmittedTime, 'GATE_A_PROVIDER_LAST_SUBMITTED_TIME_INVALID'),
    schema_version: schema.schema_version,
    field_signature: schema.field_signature,
    payload_hash: ttqsGateADigestCanonical_(payload),
    observed_at: ttqsGateANormalizeProviderTimestamp_(observedAt, 'GATE_A_OBSERVED_AT_INVALID'),
    ingestion_run_id: ttqsGateARequireString_(runId, 'GATE_A_RUN_ID_REQUIRED'),
    page_ordinal: ordinal,
    provider_filter: ttqsGateARequireString_(request.filter, 'GATE_A_FILTER_REQUIRED')
  };
}

function ttqsGateAAssertImmutableReplay_(existingRecord, incomingRecord) {
  if (String(existingRecord.source_identity || '') !== String(incomingRecord.source_identity || '')) {
    throw new Error('GATE_A_RESPONSE_IDENTITY_MISMATCH');
  }
  if (String(existingRecord.payload_hash || '') !== String(incomingRecord.payload_hash || '')) {
    throw new Error('GATE_A_RESPONSE_ID_CONTENT_CONFLICT:' + String(incomingRecord.response_id || ''));
  }
  if (String(existingRecord.field_signature || '') !== String(incomingRecord.field_signature || '') ||
      String(existingRecord.schema_version || '') !== String(incomingRecord.schema_version || '')) {
    throw new Error('GATE_A_RESPONSE_ID_SCHEMA_CONFLICT:' + String(incomingRecord.response_id || ''));
  }
  return true;
}

function ttqsGateAClone_(value) {
  return JSON.parse(JSON.stringify(value));
}

function ttqsGateACheckpointBody_(state) {
  return {
    version: 'GATE_A_CHECKPOINT_V1',
    run_id: String(state.run_id || ''),
    form_id: String(state.form_id || ''),
    filter: String(state.filter || ''),
    window_start: String(state.window_start || ''),
    committed_watermark_snapshot: String(state.committed_watermark_snapshot || ''),
    page_ordinal: Number(state.page_ordinal || 0),
    next_page_token: String(state.next_page_token || ''),
    staged_response_ids: (state.staged_response_ids || []).slice().sort(),
    staged_records: ttqsGateAClone_(state.staged_records || {}),
    candidate_high_watermark: String(state.candidate_high_watermark || ''),
    run_complete: state.run_complete === true,
    checkpoint_history: ttqsGateAClone_(state.page_checkpoints || [])
  };
}

function ttqsGateAMakeCheckpoint_(state) {
  var body = ttqsGateACheckpointBody_(state);
  var checkpoint = ttqsGateAClone_(body);
  checkpoint.checkpoint_hash = ttqsGateADigestCanonical_(body);
  return checkpoint;
}

function ttqsGateARestoreCheckpoint_(checkpoint) {
  if (!checkpoint) throw new Error('GATE_A_CHECKPOINT_REQUIRED');
  var suppliedHash = ttqsGateARequireString_(checkpoint.checkpoint_hash, 'GATE_A_CHECKPOINT_HASH_REQUIRED');
  var body = ttqsGateAClone_(checkpoint);
  delete body.checkpoint_hash;
  if (ttqsGateADigestCanonical_(body) !== suppliedHash) throw new Error('GATE_A_CHECKPOINT_HASH_MISMATCH');
  var history = ttqsGateAClone_(body.checkpoint_history || []);
  history.push({ page_ordinal: Number(body.page_ordinal || 0), checkpoint_hash: suppliedHash });
  return {
    run_id: body.run_id,
    form_id: body.form_id,
    filter: body.filter,
    window_start: body.window_start,
    committed_watermark_snapshot: body.committed_watermark_snapshot,
    next_page_token: body.next_page_token,
    page_ordinal: Number(body.page_ordinal || 0),
    staged_response_ids: (body.staged_response_ids || []).slice().sort(),
    staged_records: ttqsGateAClone_(body.staged_records || {}),
    candidate_high_watermark: body.candidate_high_watermark,
    page_checkpoints: history,
    last_checkpoint: ttqsGateAClone_(checkpoint),
    run_complete: body.run_complete === true,
    reconciliation: null,
    final_watermark_candidate: ''
  };
}

function ttqsGateAApplyPage_(state, request, page, schema, observedAt) {
  if (!state || !request || !page) throw new Error('GATE_A_PAGE_INPUT_REQUIRED');
  if (state.run_complete) throw new Error('GATE_A_RUN_ALREADY_COMPLETE');
  if (String(request.formId || '') !== String(state.form_id || '') || String(request.filter || '') !== String(state.filter || '')) {
    throw new Error('GATE_A_PAGE_REQUEST_CONTEXT_MISMATCH');
  }
  if (String(request.pageToken || '') !== String(state.next_page_token || '')) throw new Error('GATE_A_PAGE_TOKEN_MISMATCH');
  var responses = page.responses === undefined ? [] : page.responses;
  if (!Array.isArray(responses)) throw new Error('GATE_A_PAGE_RESPONSES_INVALID');
  var next = ttqsGateAClone_(state);
  var ordinal = Number(state.page_ordinal || 0) + 1;
  responses.forEach(function(response) {
    var record = ttqsGateABuildL1Record_(request, response, schema, observedAt, state.run_id, ordinal);
    var existing = next.staged_records[record.response_id];
    if (existing) {
      ttqsGateAAssertImmutableReplay_(existing, record);
    } else {
      next.staged_records[record.response_id] = record;
    }
    next.candidate_high_watermark = ttqsGateAMaxTimestamp_(next.candidate_high_watermark, record.provider_last_submitted_time);
  });
  next.staged_response_ids = Object.keys(next.staged_records).sort();
  next.page_ordinal = ordinal;
  var nextToken = String(page.nextPageToken || '').trim();
  if (nextToken && nextToken === String(request.pageToken || '')) throw new Error('GATE_A_PAGINATION_TOKEN_STALLED');
  next.next_page_token = nextToken;
  next.run_complete = nextToken === '';
  next.reconciliation = null;
  next.final_watermark_candidate = '';
  var checkpoint = ttqsGateAMakeCheckpoint_(next);
  next.page_checkpoints.push({ page_ordinal: ordinal, checkpoint_hash: checkpoint.checkpoint_hash });
  next.last_checkpoint = checkpoint;
  return next;
}

function ttqsGateAIdSetInfo_(values, label) {
  if (!Array.isArray(values)) throw new Error('GATE_A_ID_SET_INVALID:' + label);
  var counts = Object.create(null);
  values.forEach(function(value) {
    var id = ttqsGateARequireString_(value, 'GATE_A_RESPONSE_ID_REQUIRED');
    counts[id] = Number(counts[id] || 0) + 1;
  });
  var ids = Object.keys(counts).sort();
  var duplicates = ids.filter(function(id) { return counts[id] > 1; });
  return { ids: ids, duplicates: duplicates };
}

function ttqsGateAReconcileIdSets_(providerResponseIds, l1ResponseIds) {
  var provider = ttqsGateAIdSetInfo_(providerResponseIds, 'PROVIDER');
  var l1 = ttqsGateAIdSetInfo_(l1ResponseIds, 'L1');
  var providerMap = Object.create(null);
  var l1Map = Object.create(null);
  provider.ids.forEach(function(id) { providerMap[id] = true; });
  l1.ids.forEach(function(id) { l1Map[id] = true; });
  var missing = provider.ids.filter(function(id) { return !l1Map[id]; });
  var unexpected = l1.ids.filter(function(id) { return !providerMap[id]; });
  var duplicates = provider.duplicates.map(function(id) { return 'PROVIDER:' + id; })
    .concat(l1.duplicates.map(function(id) { return 'L1:' + id; })).sort();
  return {
    provider_response_ids: provider.ids,
    l1_response_ids: l1.ids,
    missing_in_l1: missing,
    unexpected_in_l1: unexpected,
    duplicate_identities: duplicates,
    exact_match: missing.length === 0 && unexpected.length === 0 && duplicates.length === 0
  };
}

function ttqsGateAFinalizeRun_(state, l1ResponseIds) {
  if (!state || state.run_complete !== true) throw new Error('GATE_A_PAGINATION_INCOMPLETE');
  var reconciliation = ttqsGateAReconcileIdSets_(state.staged_response_ids || [], l1ResponseIds);
  if (!reconciliation.exact_match) {
    throw new Error('GATE_A_ID_SET_MISMATCH:' + ttqsGateACanonicalJson_({
      missing_in_l1: reconciliation.missing_in_l1,
      unexpected_in_l1: reconciliation.unexpected_in_l1,
      duplicate_identities: reconciliation.duplicate_identities
    }));
  }
  var next = ttqsGateAClone_(state);
  next.reconciliation = reconciliation;
  next.final_watermark_candidate = String(state.candidate_high_watermark || state.committed_watermark_snapshot || '');
  return next;
}

function ttqsGateACommitWatermark_(state) {
  if (!state || state.run_complete !== true) throw new Error('GATE_A_PAGINATION_INCOMPLETE');
  if (!state.reconciliation || state.reconciliation.exact_match !== true) throw new Error('GATE_A_RECONCILIATION_REQUIRED');
  return ttqsGateARequireString_(state.final_watermark_candidate, 'GATE_A_WATERMARK_UNAVAILABLE');
}
`;

const testSource = String.raw`import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import crypto from 'node:crypto';

const source = fs.readFileSync('apps-script/S3Foundation.gs', 'utf8');
const appsscript = JSON.parse(fs.readFileSync('apps-script/appsscript.json', 'utf8'));

function digest(value) {
  return crypto.createHash('sha256').update(String(value)).digest('hex');
}

function context() {
  const ctx = {
    isFinite,
    Date,
    Math,
    JSON,
    ttqsDigest_: digest,
    ttqsAssertTestOnly_: () => true,
    ttqsStableId_: (prefix, value, length = 16) => prefix + digest(value).slice(0, length).toUpperCase(),
    ttqsParseJson_: (value, fallback) => { try { return value ? JSON.parse(value) : fallback; } catch { return fallback; } }
  };
  vm.createContext(ctx);
  vm.runInContext(source, ctx);
  return ctx;
}

function schema(ctx) {
  return ctx.ttqsGateASchemaContract_('GATE_A_V1', ['q2', 'q1'], ['q1']);
}

function response(id, submitted = '2026-08-17T04:10:00.000Z', answers = { q1: { textAnswers: { answers: [{ value: 'A' }] } } }) {
  return {
    formId: 'FORM-1',
    responseId: id,
    createTime: '2026-08-17T04:00:00.000Z',
    lastSubmittedTime: submitted,
    respondentEmail: 'must-not-persist@example.invalid',
    answers
  };
}

function initial(ctx, committed = '2026-08-17T04:05:00.000Z') {
  const request = ctx.ttqsGateAPlanOverlapRequest_('FORM-1', committed, 60000, '2026-08-17T00:00:00.000Z');
  return ctx.ttqsGateANewRun_(request, 'RUN-1');
}

function plain(value) {
  return JSON.parse(JSON.stringify(value));
}

test('Gate A source parses as Apps Script JavaScript', () => {
  new vm.Script(source, { filename: 'S3Foundation.gs' });
});

test('responseId identity is deterministic and changes with responseId', () => {
  const ctx = context();
  const a = ctx.ttqsGateAResponseIdentity_('FORM-1', 'RESP-1');
  const b = ctx.ttqsGateAResponseIdentity_('FORM-1', 'RESP-1');
  const c = ctx.ttqsGateAResponseIdentity_('FORM-1', 'RESP-2');
  assert.equal(a, b);
  assert.notEqual(a, c);
  assert.match(a, /^[0-9a-f]{64}$/);
});

test('missing responseId fails closed', () => {
  const ctx = context();
  assert.throws(() => ctx.ttqsGateAResponseIdentity_('FORM-1', ''), /GATE_A_RESPONSE_ID_REQUIRED/);
});

test('canonical answers are invariant to object key insertion order', () => {
  const ctx = context();
  const a = ctx.ttqsGateADigestCanonical_(ctx.ttqsGateAResponsePayload_({ answers: { q2: { b: 2, a: 1 }, q1: { z: true } } }));
  const b = ctx.ttqsGateADigestCanonical_(ctx.ttqsGateAResponsePayload_({ answers: { q1: { z: true }, q2: { a: 1, b: 2 } } }));
  assert.equal(a, b);
});

test('schema field signature is invariant to expected-field order', () => {
  const ctx = context();
  const a = ctx.ttqsGateASchemaContract_('V1', ['q2', 'q1'], ['q1']);
  const b = ctx.ttqsGateASchemaContract_('V1', ['q1', 'q2'], ['q1']);
  assert.equal(a.field_signature, b.field_signature);
});

test('missing required answer fails closed', () => {
  const ctx = context();
  const s = schema(ctx);
  assert.throws(() => ctx.ttqsGateAValidateResponseSchema_({ answers: { q2: {} } }, s), /GATE_A_SCHEMA_REQUIRED_FIELD_MISSING:q1/);
});

test('unknown answer questionId is explicit schema drift', () => {
  const ctx = context();
  const s = schema(ctx);
  assert.throws(() => ctx.ttqsGateAValidateResponseSchema_({ answers: { q1: {}, q3: {} } }, s), /GATE_A_SCHEMA_DRIFT_UNKNOWN_FIELD:q3/);
});

test('L1 record excludes respondentEmail and validates provider formId', () => {
  const ctx = context();
  const run = initial(ctx);
  const request = ctx.ttqsGateARequestForPage_(run);
  const record = plain(ctx.ttqsGateABuildL1Record_(request, response('RESP-1'), schema(ctx), '2026-08-17T04:11:00.000Z', 'RUN-1', 1));
  assert.equal(record.environment, 'TEST');
  assert.equal(record.source_type, 'GOOGLE_FORM_RESPONSE');
  assert.equal(record.response_id, 'RESP-1');
  assert.equal(Object.prototype.hasOwnProperty.call(record, 'respondentEmail'), false);
  const wrong = response('RESP-2');
  wrong.formId = 'FORM-2';
  assert.throws(() => ctx.ttqsGateABuildL1Record_(request, wrong, schema(ctx), '2026-08-17T04:11:00.000Z', 'RUN-1', 1), /GATE_A_PROVIDER_FORM_ID_MISMATCH/);
});

test('same responseId exact replay is idempotent', () => {
  const ctx = context();
  let run = initial(ctx);
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-1'), response('RESP-1')], nextPageToken: '' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  assert.deepEqual(plain(run.staged_response_ids), ['RESP-1']);
  assert.equal(Object.keys(run.staged_records).length, 1);
});

test('same responseId with changed canonical content fails closed', () => {
  const ctx = context();
  const run = initial(ctx);
  const changed = response('RESP-1', '2026-08-17T04:10:00.000Z', { q1: { textAnswers: { answers: [{ value: 'B' }] } } });
  assert.throws(() => ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-1'), changed], nextPageToken: '' }, schema(ctx), '2026-08-17T04:11:00.000Z'), /GATE_A_RESPONSE_ID_CONTENT_CONFLICT/);
  assert.deepEqual(plain(run.staged_response_ids), []);
});

test('same timestamp with multiple responseIds preserves every identity', () => {
  const ctx = context();
  let run = initial(ctx);
  const same = '2026-08-17T04:10:00.123456789Z';
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-A', same), response('RESP-B', same)], nextPageToken: '' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  assert.deepEqual(plain(run.staged_response_ids), ['RESP-A', 'RESP-B']);
});

test('overlap planner moves backward and uses timestamp >= filter', () => {
  const ctx = context();
  const plan = plain(ctx.ttqsGateAPlanOverlapRequest_('FORM-1', '2026-08-17T04:05:00.000Z', 60000, '2026-08-17T00:00:00.000Z'));
  assert.equal(plan.window_start, '2026-08-17T04:04:00.000Z');
  assert.equal(plan.filter, 'timestamp >= 2026-08-17T04:04:00.000Z');
});

test('initial scan requires an explicit bounded window start', () => {
  const ctx = context();
  assert.throws(() => ctx.ttqsGateAPlanOverlapRequest_('FORM-1', '', 60000, ''), /GATE_A_INITIAL_WINDOW_START_REQUIRED/);
  const plan = ctx.ttqsGateAPlanOverlapRequest_('FORM-1', '', 60000, '2026-08-01T00:00:00.000Z');
  assert.equal(plan.window_start, '2026-08-01T00:00:00.000Z');
});

test('pageToken request keeps exact original form and filter contract', () => {
  const ctx = context();
  let run = initial(ctx);
  const firstRequest = plain(ctx.ttqsGateARequestForPage_(run));
  run = ctx.ttqsGateAApplyPage_(run, firstRequest, { responses: [response('RESP-1')], nextPageToken: 'TOKEN-2' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  const secondRequest = plain(ctx.ttqsGateARequestForPage_(run));
  assert.equal(secondRequest.formId, firstRequest.formId);
  assert.equal(secondRequest.filter, firstRequest.filter);
  assert.equal(secondRequest.pageToken, 'TOKEN-2');
});

test('partial page is not final while nextPageToken exists', () => {
  const ctx = context();
  let run = initial(ctx);
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-1')], nextPageToken: 'TOKEN-2' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  assert.equal(run.run_complete, false);
  assert.equal(run.next_page_token, 'TOKEN-2');
});

test('complete multi-page traversal ends only when nextPageToken is absent', () => {
  const ctx = context();
  let run = initial(ctx);
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-1')], nextPageToken: 'TOKEN-2' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-2', '2026-08-17T04:12:00.000Z')], nextPageToken: '' }, schema(ctx), '2026-08-17T04:13:00.000Z');
  assert.equal(run.run_complete, true);
  assert.equal(run.page_ordinal, 2);
  assert.deepEqual(plain(run.staged_response_ids), ['RESP-1', 'RESP-2']);
});

test('page-one failure leaves original run and watermark untouched', () => {
  const ctx = context();
  const run = initial(ctx);
  const bad = response('RESP-1');
  delete bad.responseId;
  assert.throws(() => ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [bad], nextPageToken: '' }, schema(ctx), '2026-08-17T04:11:00.000Z'), /GATE_A_RESPONSE_ID_REQUIRED/);
  assert.equal(run.page_ordinal, 0);
  assert.equal(run.candidate_high_watermark, '2026-08-17T04:05:00.000Z');
  assert.equal(run.final_watermark_candidate, '');
});

test('middle-page failure leaves prior checkpoint state unchanged', () => {
  const ctx = context();
  let run = initial(ctx);
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-1')], nextPageToken: 'TOKEN-2' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  const before = plain(run);
  const bad = response('RESP-2');
  bad.answers.q3 = {};
  assert.throws(() => ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [bad], nextPageToken: '' }, schema(ctx), '2026-08-17T04:12:00.000Z'), /GATE_A_SCHEMA_DRIFT_UNKNOWN_FIELD/);
  assert.deepEqual(plain(run), before);
});

test('checkpoint restore resumes next page and matches uninterrupted final data state', () => {
  const ctx = context();
  let uninterrupted = initial(ctx);
  uninterrupted = ctx.ttqsGateAApplyPage_(uninterrupted, ctx.ttqsGateARequestForPage_(uninterrupted), { responses: [response('RESP-1')], nextPageToken: 'TOKEN-2' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  const checkpoint = plain(uninterrupted.last_checkpoint);
  let restored = ctx.ttqsGateARestoreCheckpoint_(checkpoint);
  const page2 = { responses: [response('RESP-2', '2026-08-17T04:12:00.000Z')], nextPageToken: '' };
  uninterrupted = ctx.ttqsGateAApplyPage_(uninterrupted, ctx.ttqsGateARequestForPage_(uninterrupted), page2, schema(ctx), '2026-08-17T04:13:00.000Z');
  restored = ctx.ttqsGateAApplyPage_(restored, ctx.ttqsGateARequestForPage_(restored), page2, schema(ctx), '2026-08-17T04:13:00.000Z');
  assert.deepEqual(plain(restored.staged_response_ids), plain(uninterrupted.staged_response_ids));
  assert.deepEqual(plain(restored.staged_records), plain(uninterrupted.staged_records));
  assert.equal(restored.candidate_high_watermark, uninterrupted.candidate_high_watermark);
  assert.equal(restored.run_complete, uninterrupted.run_complete);
});

test('checkpoint tampering fails closed', () => {
  const ctx = context();
  let run = initial(ctx);
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-1')], nextPageToken: 'TOKEN-2' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  const checkpoint = plain(run.last_checkpoint);
  checkpoint.next_page_token = 'ATTACK';
  assert.throws(() => ctx.ttqsGateARestoreCheckpoint_(checkpoint), /GATE_A_CHECKPOINT_HASH_MISMATCH/);
});

test('ID-set exact match passes', () => {
  const ctx = context();
  const result = plain(ctx.ttqsGateAReconcileIdSets_(['A', 'B'], ['B', 'A']));
  assert.equal(result.exact_match, true);
  assert.deepEqual(result.missing_in_l1, []);
  assert.deepEqual(result.unexpected_in_l1, []);
});

test('equal counts with different IDs fails ID-set reconciliation', () => {
  const ctx = context();
  const result = plain(ctx.ttqsGateAReconcileIdSets_(['A', 'B'], ['A', 'C']));
  assert.equal(result.exact_match, false);
  assert.deepEqual(result.missing_in_l1, ['B']);
  assert.deepEqual(result.unexpected_in_l1, ['C']);
});

test('missing_in_l1 and unexpected_in_l1 are explicit', () => {
  const ctx = context();
  const result = plain(ctx.ttqsGateAReconcileIdSets_(['A', 'B', 'C'], ['A', 'D']));
  assert.deepEqual(result.missing_in_l1, ['B', 'C']);
  assert.deepEqual(result.unexpected_in_l1, ['D']);
});

test('duplicate response identities are explicit failures', () => {
  const ctx = context();
  const result = plain(ctx.ttqsGateAReconcileIdSets_(['A', 'A'], ['A']));
  assert.equal(result.exact_match, false);
  assert.deepEqual(result.duplicate_identities, ['PROVIDER:A']);
});

test('finalization is forbidden before pagination completes', () => {
  const ctx = context();
  const run = initial(ctx);
  assert.throws(() => ctx.ttqsGateAFinalizeRun_(run, []), /GATE_A_PAGINATION_INCOMPLETE/);
});

test('ID-set mismatch blocks final watermark candidate', () => {
  const ctx = context();
  let run = initial(ctx);
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-1')], nextPageToken: '' }, schema(ctx), '2026-08-17T04:11:00.000Z');
  assert.throws(() => ctx.ttqsGateAFinalizeRun_(run, ['RESP-X']), /GATE_A_ID_SET_MISMATCH/);
  assert.equal(run.final_watermark_candidate, '');
});

test('watermark commits only after complete traversal and exact set reconciliation', () => {
  const ctx = context();
  let run = initial(ctx);
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-1', '2026-08-17T04:12:00.000Z')], nextPageToken: '' }, schema(ctx), '2026-08-17T04:13:00.000Z');
  const finalState = ctx.ttqsGateAFinalizeRun_(run, ['RESP-1']);
  assert.equal(ctx.ttqsGateACommitWatermark_(finalState), '2026-08-17T04:12:00.000Z');
});

test('overlap replay can never regress committed watermark', () => {
  const ctx = context();
  let run = initial(ctx, '2026-08-17T04:20:00.000Z');
  run = ctx.ttqsGateAApplyPage_(run, ctx.ttqsGateARequestForPage_(run), { responses: [response('RESP-OLD', '2026-08-17T04:19:30.000Z')], nextPageToken: '' }, schema(ctx), '2026-08-17T04:21:00.000Z');
  const finalState = ctx.ttqsGateAFinalizeRun_(run, ['RESP-OLD']);
  assert.equal(ctx.ttqsGateACommitWatermark_(finalState), '2026-08-17T04:20:00.000Z');
});

test('nanosecond provider timestamps are ordered without collapsing response identity', () => {
  const ctx = context();
  assert.equal(ctx.ttqsGateAMaxTimestamp_('2026-08-17T04:10:00.123456788Z', '2026-08-17T04:10:00.123456789Z'), '2026-08-17T04:10:00.123456789Z');
});

test('Gate A foundation contains no provider write or runtime Forms API invocation', () => {
  const start = source.indexOf("var TTQS_GATE_A_SOURCE_TYPE = 'GOOGLE_FORM_RESPONSE';");
  const gate = source.slice(start);
  assert.ok(start > 0);
  assert.doesNotMatch(gate, /UrlFetchApp|Forms\.Responses|Forms\.Forms|setValue\(|setValues\(|appendRow\(|PropertiesService/);
});

test('appsscript manifest OAuth and advanced-service contracts are unchanged', () => {
  assert.deepEqual(appsscript.oauthScopes, [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/forms',
    'https://www.googleapis.com/auth/script.scriptapp',
    'https://www.googleapis.com/auth/drive.file'
  ]);
  assert.deepEqual(appsscript.dependencies.enabledAdvancedServices, [
    { userSymbol: 'Drive', serviceId: 'drive', version: 'v3' }
  ]);
});

test('existing S3 raw-sheet source identity semantics remain present and untouched', () => {
  assert.match(source, /function ttqsS3ObservationEventId_\(sourceKey\)/);
  assert.match(source, /ttqsRawSubmission_\(locator\.sheetId, locator\.rowNumber, false\)/);
  assert.match(source, /observationIdentityMode: identityMode/);
});

test('Gate A remains source-only and is not wired into the active S3 scheduler cycle', () => {
  const cycleStart = source.indexOf('function ttqsS3ObservationCycle()');
  const cycle = source.slice(cycleStart, source.indexOf("var TTQS_GATE_A_SOURCE_TYPE = 'GOOGLE_FORM_RESPONSE';"));
  assert.doesNotMatch(cycle, /ttqsGateA/);
});
`;

fs.writeFileSync(sourcePath, original.replace(/\s*$/, '') + appendix + '\n');
fs.writeFileSync(testPath, testSource);

if (fs.existsSync(workflowPath)) fs.rmSync(workflowPath);
if (fs.existsSync(selfPath)) fs.rmSync(selfPath);
