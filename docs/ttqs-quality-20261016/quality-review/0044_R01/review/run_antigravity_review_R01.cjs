const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { spawn } = require('node:child_process');
const { finished } = require('node:stream/promises');

const [packetRoot, agyPath] = process.argv.slice(2);
const sha = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const manifestPath = path.join(packetRoot, 'review_packet_manifest_R01.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const inventory = () => manifest.files.map(x => ({ path:x.path, sha256:sha(path.join(packetRoot,x.path)) }));
const beforeInventory = inventory();
const candidatePath = path.join(packetRoot, 'candidate', '0044_R01.docx');
const candidateBefore = sha(candidatePath);
const binarySha = sha(agyPath);
const stdoutPath = path.join(packetRoot, 'antigravity_cli_R01.stdout.raw');
const stderrPath = path.join(packetRoot, 'antigravity_cli_R01.stderr.raw');
const stdout = fs.createWriteStream(stdoutPath, {flags:'wx'});
const stderr = fs.createWriteStream(stderrPath, {flags:'wx'});
const started = new Date();
const promptPath = path.join(packetRoot, 'review_prompt_R01.txt');
const prompt = fs.readFileSync(promptPath, 'utf8');
const args = [
  '--model','gemini-3.8-flash-high',
  '--effort','high',
  '--sandbox',
  '--disable-slash-commands',
  '--add-dir',packetRoot,
  '--output-format','json',
  '--print-timeout','0',
  '--print',prompt
];
const child = spawn(agyPath,args,{cwd:packetRoot,windowsHide:true,stdio:['ignore','pipe','pipe']});
child.stdout.pipe(stdout);
child.stderr.pipe(stderr);
let spawnError = null;
child.on('error',e=>{spawnError=String(e && e.stack || e);});
child.on('close',async(code,signal)=>{
  try {
    await Promise.all([finished(stdout),finished(stderr)]);
    const afterInventory=inventory();
    const changed=beforeInventory.filter((x,i)=>afterInventory[i].sha256!==x.sha256).map(x=>x.path);
    const candidateAfter=sha(candidatePath);
    const receipt={
      project_id:'TTQS_ONE',doc_id:'0044',requirement_id:'I09-E04',official_checkbox_sequence:'045',candidate_revision:'R01',
      candidate_path:'candidate/0044_R01.docx',candidate_sha256_before:candidateBefore,candidate_sha256_after:candidateAfter,candidate_unchanged:candidateBefore===candidateAfter,
      cli_path:agyPath,cli_sha256:binarySha,model_requested:'gemini-3.8-flash-high',effort_requested:'high',sandbox:true,computer_use:false,
      working_directory:packetRoot,prompt_path:'review_prompt_R01.txt',prompt_sha256:sha(promptPath),packet_manifest_path:'review_packet_manifest_R01.json',
      packet_manifest_sha256:sha(manifestPath),packet_inputs_unchanged:changed.length===0,packet_changed_paths:changed,input_count:manifest.files.length,
      started_local:started.toISOString(),completed_local:new Date().toISOString(),elapsed_seconds:(Date.now()-started.getTime())/1000,
      process_exit_code:code,signal,spawn_error:spawnError,timed_out:false,
      raw_stdout_path:'antigravity_cli_R01.stdout.raw',raw_stdout_sha256:sha(stdoutPath),raw_stderr_path:'antigravity_cli_R01.stderr.raw',raw_stderr_sha256:sha(stderrPath),
      status:code===0 && !spawnError ? 'PROCESS_SUCCESS':'PROCESS_ERROR'
    };
    const receiptPath=path.join(packetRoot,'antigravity_execution_receipt_R01.json');
    fs.writeFileSync(receiptPath,JSON.stringify(receipt,null,2),'utf8');
    process.stdout.write(JSON.stringify({status:receipt.status,exit:code,signal,elapsed_seconds:receipt.elapsed_seconds,stdout_sha256:receipt.raw_stdout_sha256,stderr_sha256:receipt.raw_stderr_sha256,receipt:receiptPath})+'\n');
  } catch(e) {
    process.stderr.write(String(e && e.stack || e)+'\n');
    process.exitCode=1;
  }
});
