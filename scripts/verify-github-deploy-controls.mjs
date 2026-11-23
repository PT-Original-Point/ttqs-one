const API_VERSION = '2022-11-28';

export function isDeployControlContext(env = process.env) {
  return env.GITHUB_ACTIONS === 'true' &&
    env.GITHUB_REF === 'refs/heads/deploy/test' &&
    env.GITHUB_JOB === 'deploy';
}

export function assessDeployControls({ branch, environment, branchPolicies }) {
  const errors = [];
  if (!branch || branch.name !== 'main' || branch.protected !== true) {
    errors.push('MAIN_BRANCH_NOT_PROTECTED');
  }

  const policy = environment && environment.deployment_branch_policy;
  if (!policy || policy.custom_branch_policies !== true || policy.protected_branches !== false) {
    errors.push('TEST_CUSTOM_BRANCH_POLICY_NOT_ENABLED');
  }

  const names = branchPolicies && Array.isArray(branchPolicies.branch_policies)
    ? branchPolicies.branch_policies.map((item) => String(item && item.name || '')).filter(Boolean).sort()
    : [];
  if (names.length !== 1 || names[0] !== 'deploy/test') {
    errors.push('TEST_DEPLOY_BRANCH_ALLOWLIST_INVALID:' + names.join(','));
  }

  return {
    status: errors.length ? 'FAIL' : 'PASS',
    mainProtected: !!(branch && branch.protected === true),
    customBranchPolicies: !!(policy && policy.custom_branch_policies === true),
    allowedBranches: names,
    errors
  };
}

async function fetchJson(url, env = process.env) {
  const headers = {
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': API_VERSION,
    'User-Agent': 'ttqs-one-deploy-control-gate'
  };
  if (env.GITHUB_TOKEN) headers.Authorization = `Bearer ${env.GITHUB_TOKEN}`;
  const response = await fetch(url, { headers });
  if (!response.ok) throw new Error(`GITHUB_CONTROL_READ_FAILED:${response.status}:${url}`);
  return response.json();
}

export async function verifyGitHubDeployControls(env = process.env) {
  if (!isDeployControlContext(env)) {
    return { status: 'SKIP', reason: 'NOT_TEST_DEPLOY_JOB' };
  }
  const repository = String(env.GITHUB_REPOSITORY || '');
  if (!/^[^/]+\/[^/]+$/.test(repository)) throw new Error('GITHUB_REPOSITORY_REQUIRED');
  const api = String(env.GITHUB_API_URL || 'https://api.github.com').replace(/\/$/, '');
  const base = `${api}/repos/${repository}`;
  const branch = await fetchJson(`${base}/branches/main`, env);
  const environment = await fetchJson(`${base}/environments/TEST`, env);
  let branchPolicies = { branch_policies: [] };
  if (environment && environment.deployment_branch_policy && environment.deployment_branch_policy.custom_branch_policies === true) {
    branchPolicies = await fetchJson(`${base}/environments/TEST/deployment-branch-policies`, env);
  }
  const result = assessDeployControls({ branch, environment, branchPolicies });
  if (result.status !== 'PASS') {
    throw new Error(`GITHUB_DEPLOY_CONTROL_GATE_FAIL:${result.errors.join('|')}`);
  }
  return result;
}

if (import.meta.url === new URL(`file://${process.argv[1]}`).href) {
  verifyGitHubDeployControls().then((result) => {
    console.log(JSON.stringify(result, null, 2));
  }).catch((err) => {
    console.error(String(err && err.message || err));
    process.exit(1);
  });
}
