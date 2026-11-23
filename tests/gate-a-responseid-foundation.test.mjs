import test from 'node:test';
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
