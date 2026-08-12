import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const forms = fs.readFileSync('apps-script/Forms.gs', 'utf8');
const router = fs.readFileSync('apps-script/FormRouter.gs', 'utf8');
const survey = fs.readFileSync('apps-script/SurveyWriter.gs', 'utf8');
const manifest = fs.readFileSync('apps-script/appsscript.json', 'utf8');

const expectedTokens = [
  'NEEDS', 'REGISTRATION', 'REACTION', 'FOLLOWUP30',
  'TTQS_ALIAS_CODE', 'TTQS_NEED_SCORE', 'TTQS_NEED_TEXT',
  'TTQS_SAMPLE_CONFIRM',
  'TTQS_30D_SAFE_ACTION', 'TTQS_30D_BOUNDARY', 'TTQS_30D_TEXT'
];
for (const token of expectedTokens) test(`form contract contains ${token}`, () => assert.ok((forms + router).includes(token)));

test('demo form titles are Traditional Chinese and clearly marked', () => {
  assert.match(forms, /【顧問示範／測試資料】TTQS ONE－課前需求調查/);
  assert.match(forms, /【顧問示範／測試資料】TTQS ONE－課程報名/);
  assert.match(forms, /【顧問示範／測試資料】TTQS ONE－課後滿意度/);
  assert.match(forms, /【顧問示範／測試資料】TTQS ONE－30 日追蹤/);
});
test('forms prohibit real PII in Traditional Chinese description', () => assert.match(forms, /不要填寫真實姓名/));
test('forms explain demo value rather than exposing engineering field labels', () => {
  assert.match(forms, /展示 TTQS ONE/);
  assert.match(forms, /示範學員代碼/);
  assert.match(forms, /課程內容清楚度/);
});
test('forms do not collect email', () => assert.match(forms, /setCollectEmail\(false\)/));
test('forms expose no arbitrary text response item', () => assert.doesNotMatch(forms, /addTextItem|addParagraphTextItem/));
test('aliases are controlled SAMPLE choices', () => assert.match(forms, /\['S-L01', 'S-L02', 'S-L03', 'S-L04', 'S-L05', 'S-L06', 'S-L07'\]/));
test('forms use controlled Traditional Chinese SAMPLE narrative choices', () => assert.match(forms, /【示範】希望增加更多安全情境案例/));
test('form UI has contextual help text and localized scale labels', () => {
  assert.match(forms, /setHelpText\(spec\.help\)/);
  assert.match(forms, /1｜較低/);
  assert.match(forms, /5｜較高/);
});
test('all forms target core spreadsheet', () => assert.match(forms, /setDestination\(FormApp\.DestinationType\.SPREADSHEET/));
test('form creation explicitly publishes form', () => assert.match(forms, /setPublished\(true\)/));
test('form publication is read back fail-closed', () => assert.match(forms, /isPublished\(\) !== true/));
test('published responder URL is required', () => assert.match(forms, /FORM_PUBLISHED_URL_EMPTY/));
test('anyone-with-link responder access is provisioned only on published view', () => {
  assert.match(forms, /type: 'anyone'/);
  assert.match(forms, /view: 'published'/);
  assert.match(forms, /role: 'reader'/);
  assert.match(forms, /FORM_ANYONE_WITH_LINK_RESPONDER_NOT_CONFIRMED/);
});
test('Drive advanced service uses least-privilege per-file scope', () => {
  assert.match(manifest, /"userSymbol": "Drive"/);
  assert.match(manifest, /"serviceId": "drive"/);
  assert.match(manifest, /"version": "v3"/);
  assert.match(manifest, /https:\/\/www\.googleapis\.com\/auth\/drive\.file/);
  assert.doesNotMatch(manifest, /"https:\/\/www\.googleapis\.com\/auth\/drive"/);
});
test('existing legacy headers and new Chinese headers canonicalize to stable field codes', () => {
  assert.match(forms, /function ttqsCanonicalFieldCode_\(title\)/);
  assert.match(router, /var canonicalHeader = ttqsCanonicalFieldCode_\(header\)/);
  assert.match(router, /named\[String\(canonicalHeader\)\]/);
});
test('existing form items are synchronized in place instead of rebuilt when shape is compatible', () => {
  assert.match(forms, /function ttqsSyncExistingFormItems_\(form, kind\)/);
  assert.match(forms, /items\.forEach\(function\(item, i\) \{ ttqsApplyItemUi_\(item, expectedCodes\[i\]\); \}\)/);
});
test('forms tolerate provider no-response-destination exception before setDestination', () => {
  assert.match(forms, /function ttqsFormDestinationSnapshot_\(form\)/);
  assert.match(forms, /no response destination/);
  assert.match(forms, /return \{ id: '', type: null \}/);
  assert.match(forms, /var destination = ttqsFormDestinationSnapshot_\(form\)/);
});
test('unexpected destination inspection errors remain fail-closed', () => assert.match(forms, /throw err;/));
test('raw response persists immutable event ID', () => assert.match(router, /TTQS_EVENT_ID/));
test('raw response identity excludes row number from source ref', () => assert.match(router, /'FORM_SUITE:' \+ formId \+ ':' \+ eventId/));
test('raw retry resolves immutable ref by scanning current rows', () => assert.match(router, /ttqsFindRawSubmissionByRef_/));
test('idempotency key binds immutable raw ref', () => assert.match(router, /'TEST:' \+ raw\.rawRef/));
test('registration writes a survey stage after party stage', () => assert.match(router, /surveyType: 'REGISTRATION'/));
test('survey dedupe checks source_ref', () => assert.match(survey, /DUPLICATE_SURVEY_SOURCE_REF/));
test('runtime survey is sample-only', () => assert.match(survey, /YES_SAMPLE_NO_PII/));
test('runtime survey carries provider fingerprint and job linkage', () => assert.match(survey, /provider_raw_fingerprint/));
test('runtime survey ensures evidence even on duplicate replay', () => assert.match(survey, /ttqsEnsureRuntimeEvidence_\(spec, responseId\)/));

for (const code of ['CLARITY', 'RELEVANCE', 'SAFETY', 'PRACTICE', 'OVERALL']) test(`reaction dimension code remains present ${code}`, () => assert.ok(forms.includes(`TTQS_REACTION_${code}`)));
