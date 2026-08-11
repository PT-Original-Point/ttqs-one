import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const forms = fs.readFileSync('apps-script/Forms.gs', 'utf8');
const router = fs.readFileSync('apps-script/FormRouter.gs', 'utf8');
const survey = fs.readFileSync('apps-script/SurveyWriter.gs', 'utf8');

const expectedTokens = [
  'NEEDS', 'REGISTRATION', 'REACTION', 'FOLLOWUP30',
  'TTQS_ALIAS_CODE', 'TTQS_NEED_SCORE', 'TTQS_NEED_TEXT',
  'TTQS_SAMPLE_CONFIRM',
  'TTQS_30D_SAFE_ACTION', 'TTQS_30D_BOUNDARY', 'TTQS_30D_TEXT'
];
for (const token of expectedTokens) test(`form contract contains ${token}`, () => assert.ok((forms + router).includes(token)));

test('forms prohibit real PII in description', () => assert.match(forms, /Do not enter real/));
test('forms do not collect email', () => assert.match(forms, /setCollectEmail\(false\)/));
test('forms expose no arbitrary text response item', () => assert.doesNotMatch(forms, /addTextItem|addParagraphTextItem/));
test('aliases are controlled SAMPLE choices', () => assert.match(forms, /\['S-L01', 'S-L02', 'S-L03', 'S-L04', 'S-L05', 'S-L06', 'S-L07'\]/));
test('forms use controlled SAMPLE narrative choices', () => assert.match(forms, /SAMPLE：希望增加更多安全情境案例/));
test('all forms target core spreadsheet', () => assert.match(forms, /setDestination\(FormApp\.DestinationType\.SPREADSHEET/));
test('form creation explicitly publishes form', () => assert.match(forms, /setPublished\(true\)/));
test('form publication is read back fail-closed', () => assert.match(forms, /isPublished\(\) !== true/));
test('published responder URL is required', () => assert.match(forms, /FORM_PUBLISHED_URL_EMPTY/));
test('raw response persists immutable event ID', () => assert.match(router, /TTQS_EVENT_ID/));
test('raw response identity excludes row number from source ref', () => assert.match(router, /'FORM_SUITE:' \+ formId \+ ':' \+ eventId/));
test('raw retry resolves immutable ref by scanning current rows', () => assert.match(router, /ttqsFindRawSubmissionByRef_/));
test('idempotency key binds immutable raw ref', () => assert.match(router, /'TEST:' \+ raw\.rawRef/));
test('registration writes a survey stage after party stage', () => assert.match(router, /surveyType: 'REGISTRATION'/));
test('survey dedupe checks source_ref', () => assert.match(survey, /DUPLICATE_SURVEY_SOURCE_REF/));
test('runtime survey is sample-only', () => assert.match(survey, /YES_SAMPLE_NO_PII/));
test('runtime survey carries provider fingerprint and job linkage', () => assert.match(survey, /provider_raw_fingerprint/));
test('runtime survey ensures evidence even on duplicate replay', () => assert.match(survey, /ttqsEnsureRuntimeEvidence_\(spec, responseId\)/));

for (const code of ['CLARITY', 'RELEVANCE', 'SAFETY', 'PRACTICE', 'OVERALL']) test(`reaction dimension list contains ${code}`, () => assert.ok(forms.includes(`'${code}'`)));
test('reaction item prefix is generated deterministically', () => assert.match(forms, /'TTQS_REACTION_' \+ code/));
