import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const paths = fs.existsSync('.github/workflows') ? fs.readdirSync('.github/workflows') : [];

test('no PROD workflow', () => assert.equal(paths.some((p) => /prod/i.test(p)), false));
test('ci workflow exists after build', () => assert.ok(paths.includes('ci.yml')));
test('dev workflow exists after build', () => assert.ok(paths.includes('deploy-dev.yml')));
test('test workflow exists after build', () => assert.ok(paths.includes('deploy-test.yml')));
