import fs from 'node:fs';
import { chromium } from 'playwright';

const canonical = String(process.env.EXTERNAL_WEBAPP_URL || '').replace(/\/+$/, '');
if (!/^https:\/\/script\.google\.com\/macros\/s\/AKfy[A-Za-z0-9_-]+\/exec$/.test(canonical)) {
  throw new Error(`R7_NAV_CANONICAL_URL_INVALID:${canonical}`);
}

const viewports = [
  { name: 'desktop', viewport: { width: 1440, height: 1000 } },
  { name: 'mobile', viewport: { width: 390, height: 844 } }
];
const forbiddenText = /拒絕連線|refused to connect/i;
const forbiddenExecFrame = /https:\/\/script\.google\.com\/macros\/s\/[^/]+\/exec(?:\?|$)/i;
const evidence = [];

function canonicalIndicatorUrl(id) {
  return `${canonical}?indicator=${encodeURIComponent(String(id))}`;
}

function normalizeUrl(raw) {
  const u = new URL(raw);
  u.hash = '';
  return u.toString();
}

async function allFrameText(page) {
  const chunks = [];
  for (const frame of page.frames()) {
    try { chunks.push(await frame.locator('body').innerText({ timeout: 3000 })); } catch {}
  }
  return chunks.join('\n');
}

async function findIndicatorLink(page, id) {
  const selector = `[data-indicator="${id}"] [data-top-level-nav="true"]`;
  for (const frame of page.frames()) {
    const loc = frame.locator(selector);
    if (await loc.count()) return { frame, loc: loc.first() };
  }
  throw new Error(`R7_NAV_LINK_NOT_FOUND:${id}`);
}

async function findMatrixFrame(page, id) {
  const selector = `[data-matrix-indicator="${id}"]`;
  for (const frame of page.frames()) {
    if (await frame.locator(selector).count()) return frame;
  }
  throw new Error(`R7_NAV_MATRIX_NOT_FOUND:${id}`);
}

const browser = await chromium.launch({ headless: true });
try {
  for (const profile of viewports) {
    const context = await browser.newContext({ viewport: profile.viewport, storageState: undefined });
    try {
      for (let id = 1; id <= 19; id += 1) {
        const page = await context.newPage();
        try {
          await page.goto(canonical, { waitUntil: 'domcontentloaded', timeout: 45000 });
          await page.waitForTimeout(1500);
          const before = await allFrameText(page);
          if (forbiddenText.test(before)) throw new Error(`R7_NAV_HOME_REFUSED:${profile.name}:${id}`);

          const { loc } = await findIndicatorLink(page, id);
          const href = await loc.getAttribute('href');
          const target = await loc.getAttribute('target');
          if (normalizeUrl(href) !== normalizeUrl(canonicalIndicatorUrl(id))) {
            throw new Error(`R7_NAV_HREF_NOT_CANONICAL:${profile.name}:${id}:${href}`);
          }
          if (target !== '_top') throw new Error(`R7_NAV_TARGET_NOT_TOP:${profile.name}:${id}:${target}`);

          await Promise.all([
            page.waitForURL(url => normalizeUrl(url.toString()) === normalizeUrl(canonicalIndicatorUrl(id)), { timeout: 45000 }),
            loc.click()
          ]);
          await page.waitForLoadState('domcontentloaded');
          await page.waitForTimeout(1500);

          const topUrl = page.url();
          if (normalizeUrl(topUrl) !== normalizeUrl(canonicalIndicatorUrl(id))) {
            throw new Error(`R7_NAV_TOP_URL_FAIL:${profile.name}:${id}:${topUrl}`);
          }
          const badFrames = page.frames().map(frame => frame.url()).filter(url => forbiddenExecFrame.test(url));
          if (badFrames.length) throw new Error(`R7_NAV_NESTED_EXEC_FRAME:${profile.name}:${id}:${badFrames.join('|')}`);

          const matrixFrame = await findMatrixFrame(page, id);
          const heading = `指標 ${id}｜查看文件與證據`;
          const text = await allFrameText(page);
          if (!text.includes(heading)) throw new Error(`R7_NAV_MATRIX_TITLE_MISSING:${profile.name}:${id}`);
          if (forbiddenText.test(text)) throw new Error(`R7_NAV_REFUSED_TEXT:${profile.name}:${id}`);
          const cards = await matrixFrame.locator('[data-document-card="true"]').count();
          if (cards < 1) throw new Error(`R7_NAV_DOCUMENT_CARD_MISSING:${profile.name}:${id}`);

          evidence.push({
            viewport: profile.name,
            indicator: id,
            href,
            target,
            topUrl,
            frameUrls: page.frames().map(frame => frame.url()),
            documentCards: cards,
            titlePresent: true,
            refusedTextAbsent: true,
            nestedExecFrameAbsent: true
          });
          process.stdout.write(`R7_NAV_BROWSER_PASS viewport=${profile.name} indicator=${id} cards=${cards} top=${topUrl}\n`);
        } finally {
          await page.close();
        }
      }
    } finally {
      await context.close();
    }
  }
} finally {
  await browser.close();
}

const receipt = {
  schema: 'TTQS_R7_NAV_BROWSER_EVIDENCE_V1',
  canonicalUrl: canonical,
  generatedAt: new Date().toISOString(),
  scope: 'TEST/SAMPLE/CONTROL only; REAL/PROD/formal scoring/official submission = 0',
  viewports: viewports.map(x => x.name),
  indicators: 19,
  checks: evidence.length,
  result: evidence.length === 38 ? 'PASS_MACHINE_BROWSER' : 'FAIL',
  evidence
};
fs.writeFileSync(process.env.R7_NAV_EVIDENCE_OUT || 'r7-nav-browser-evidence.json', `${JSON.stringify(receipt, null, 2)}\n`);
if (evidence.length !== 38) throw new Error(`R7_NAV_BROWSER_INCOMPLETE:${evidence.length}/38`);
process.stdout.write('R7_NAV_BROWSER_ALL_PASS viewports=2 indicators=19 checks=38\n');
