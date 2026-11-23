import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

function loadBootstrap(sandbox) {
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync('apps-script/Bootstrap.gs', 'utf8'), sandbox, { filename: 'Bootstrap.gs' });
  return sandbox;
}

test('bootstrap missing consent stops before lock and all side effects', () => {
  const order = [];
  const sandbox = loadBootstrap({
    Object, JSON, String, Number, Date, Error,
    ScriptApp: {
      AuthMode: { FULL: 'FULL' },
      requireAllScopes(mode) {
        order.push('auth:' + mode);
        throw new Error('AUTH_REQUIRED');
      }
    },
    ttqsWithScriptLock_() {
      order.push('lock');
      return 'UNREACHABLE';
    }
  });
  assert.throws(() => sandbox.ttqsBootstrapTest(), /AUTH_REQUIRED/);
  assert.deepEqual(order, ['auth:FULL']);
});

test('bootstrap granted consent enters lock only after FULL authorization preflight', () => {
  const order = [];
  const sandbox = loadBootstrap({
    Object, JSON, String, Number, Date, Error,
    ScriptApp: {
      AuthMode: { FULL: 'FULL' },
      requireAllScopes(mode) { order.push('auth:' + mode); }
    },
    ttqsWithScriptLock_() {
      order.push('lock');
      return 'LOCKED';
    }
  });
  assert.equal(sandbox.ttqsBootstrapTest(), 'LOCKED');
  assert.deepEqual(order, ['auth:FULL', 'lock']);
});
