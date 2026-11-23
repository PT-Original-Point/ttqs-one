import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync('apps-script/SchedulerOrchestrator.gs', 'utf8');
const bootstrap = fs.readFileSync('apps-script/Bootstrap.gs', 'utf8');
const shadow = fs.readFileSync('apps-script/SchedulerShadow.gs', 'utf8');

function body(text, name, next) {
  const re = next ? new RegExp(`function ${name}\\([^)]*\\) \\{([\\s\\S]*?)\\n\\}\\n\\nfunction ${next}`) : new RegExp(`function ${name}\\([^)]*\\) \\{([\\s\\S]*?)\\n\\}\\s*$`);
  const m = text.match(re); assert.ok(m, `${name} body must be isolatable`); return m[1];
}

test('S3 topology sources parse', () => { new vm.Script(source); new vm.Script(bootstrap); new vm.Script(shadow); });

test('master scheduler accepts S2 and S3 but not legacy mode', () => {
  const b = body(source, 'ttqsSchedulerMasterModeActive_', 'ttqsS2TaskDefinitions_');
  const c = { TTQS_S2_MODE:'S2', TTQS_S3_MODE:'S3', mode:'LEGACY' }; c.ttqsSchedulerRuntimeMode_=()=>c.mode; vm.createContext(c); vm.runInContext(`function ttqsSchedulerMasterModeActive_(){${b}\n}`,c);
  c.mode='S2'; assert.equal(c.ttqsSchedulerMasterModeActive_(),true); c.mode='S3'; assert.equal(c.ttqsSchedulerMasterModeActive_(),true); c.mode='LEGACY'; assert.equal(c.ttqsSchedulerMasterModeActive_(),false);
  assert.match(source,/reason: 'MODE_NOT_MASTER'/); assert.match(body(source,'ttqsSchedulerMasterTrigger','ttqsS2MasterTriggers_'),/SCHEDULER_MASTER_RUNTIME_MODE_REQUIRED/);
});

test('S3 contract is exactly one master and no other project trigger', () => {
  const b=body(source,'ttqsAssertS3TriggerContract_','ttqsS3RecordTopology_');
  const c={TTQS_S2_MASTER_HANDLER:'ttqsSchedulerMasterTrigger',TTQS_S1_SHADOW_HANDLER:'ttqsSchedulerShadowTrigger',TTQS_S3_MODE:'S3_SINGLE_SCHEDULER',ttqsS2LegacyClockHandlers_:()=>({ttqsRetryFailedJobs:true,ttqsReconcile:true,ttqsRefreshConsultView:true})};
  c.ScriptApp={EventType:{CLOCK:'CLOCK'},TriggerSource:{CLOCK:'CLOCK'},triggers:[],getProjectTriggers(){return this.triggers;}};
  const mk=(h,e='CLOCK',s='CLOCK')=>({getHandlerFunction:()=>h,getEventType:()=>e,getTriggerSource:()=>s}); vm.createContext(c); vm.runInContext(`function ttqsAssertS3TriggerContract_(){${b}\n}`,c);
  c.ScriptApp.triggers=[mk('ttqsSchedulerMasterTrigger')]; const ok=JSON.parse(JSON.stringify(c.ttqsAssertS3TriggerContract_())); assert.equal(ok.master,1); assert.equal(ok.formSubmit,0);
  c.ScriptApp.triggers=[mk('ttqsSchedulerMasterTrigger'),mk('ttqsOnSpreadsheetFormSubmit','ON_FORM_SUBMIT','SPREADSHEETS')]; assert.throws(()=>c.ttqsAssertS3TriggerContract_(),/S3_UNEXPECTED_TRIGGER:ttqsOnSpreadsheetFormSubmit/);
  c.ScriptApp.triggers=[mk('ttqsSchedulerMasterTrigger'),mk('ttqsRetryFailedJobs')]; assert.throws(()=>c.ttqsAssertS3TriggerContract_(),/S3_FORBIDDEN_LEGACY_TRIGGER/);
  c.ScriptApp.triggers=[mk('ttqsSchedulerMasterTrigger'),mk('mysteryTrigger')]; assert.throws(()=>c.ttqsAssertS3TriggerContract_(),/S3_UNEXPECTED_TRIGGER:mysteryTrigger/);
});

test('S3 installer requires S2, preserves cadence state, removes submit, records topology and rolls back', () => {
  const i=body(source,'ttqsInstallS3SingleSchedulerTest','ttqsRollbackS3SingleSchedulerTest'); assert.match(i,/S3_S2_RUNTIME_BASELINE_REQUIRED/); assert.match(i,/ttqsAssertS2TriggerContract_/); assert.match(i,/ttqsS3RemoveFormSubmitTriggers_/); assert.match(i,/setProperty\(TTQS_S2_MODE_PROPERTY, TTQS_S3_MODE\)/); assert.match(i,/ttqsAssertS3TriggerContract_/); assert.match(i,/ttqsS3RecordTopology_\('CUTOVER'/); assert.match(i,/ttqsS3RestoreS2Topology_/); assert.doesNotMatch(i,/ttqsS2InitializeState_/);
  const r=body(source,'ttqsS3RestoreS2Topology_','ttqsInstallS3SingleSchedulerTest'); assert.match(r,/newTrigger\(TTQS_S2_MASTER_HANDLER\)/); assert.match(r,/newTrigger\('ttqsOnSpreadsheetFormSubmit'\).*onFormSubmit/s); assert.match(r,/setProperty\(TTQS_S2_MODE_PROPERTY, TTQS_S2_MODE\)/);
});

test('S3 topology writes bounded readback telemetry', () => { const r=body(source,'ttqsS3RecordTopology_','ttqsS3RestoreS2Topology_'); assert.match(r,/record_type: 'TOPOLOGY'/); assert.match(r,/task_name: '__TOPOLOGY__'/); assert.match(r,/master:/); assert.match(r,/form_submit:/); assert.match(r,/ttqsS2Bounded_/); });

test('S2 public cutover and rollback cannot overwrite active S3', () => { const i=body(source,'ttqsInstallS2ClockConsolidationTest','ttqsRollbackS2ClockConsolidationTest'); assert.match(i,/S3_RUNTIME_MODE_ACTIVE/); const r=source.match(/function ttqsRollbackS2ClockConsolidationTest\(\) \{([\s\S]*?)\n\}\n\nfunction ttqsS3FormSubmitTriggers_/); assert.ok(r); assert.match(r[1],/S3_RUNTIME_MODE_ACTIVE/); });

test('Bootstrap and S1 installer cannot resurrect replaced triggers in S3', () => { assert.match(bootstrap,/ttqsAssertS3TriggerContract_/); assert.match(bootstrap,/S3_MANAGED_TRIGGER_REINSTALL_FORBIDDEN/); const i=shadow.match(/function ttqsInstallShadowSchedulerTest\(\) \{([\s\S]*?)\n\}\n\nfunction ttqsRemoveShadowSchedulerTest/); assert.ok(i); assert.match(i[1],/S3_RUNTIME_MODE_ACTIVE/); });
