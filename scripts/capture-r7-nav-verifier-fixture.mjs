import fs from 'node:fs';
import crypto from 'node:crypto';
import { chromium } from 'playwright';

const canonical = String(process.env.EXTERNAL_WEBAPP_URL || '').replace(/\/+$/, '');
const rawPath = process.env.R7_RAW_HTML || '.r7-nav-fixture/home.raw.html';
const commentsPath = process.env.R7_PROVIDER_COMMENTS || '.r7-nav-fixture/provider-comments.json';
const outDir = process.env.R7_FIXTURE_OUT_DIR || '.r7-nav-fixture';
if (!/^https:\/\/script\.google\.com\/macros\/s\/[A-Za-z0-9_-]+\/exec$/.test(canonical)) {
  throw new Error(`R7_FIXTURE_CANONICAL_INVALID:${canonical}`);
}
fs.mkdirSync(outDir, { recursive: true });
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
const raw = fs.readFileSync(rawPath);
const rawText = raw.toString('utf8');

function parseLatestProviderReceipt() {
  const pages = JSON.parse(fs.readFileSync(commentsPath, 'utf8'));
  const comments = Array.isArray(pages) && Array.isArray(pages[0]) ? pages.flat() : pages;
  const matches = comments.filter(c => String(c?.body || '').includes('TTQS_EXTERNAL_PROVIDER_VERSION_RECEIPT_V2'));
  if (!matches.length) throw new Error('R7_FIXTURE_PROVIDER_RECEIPT_MISSING');
  const latest = matches[matches.length - 1];
  const fence = String(latest.body).match(/```json\s*([\s\S]*?)\s*```/);
  if (!fence) throw new Error('R7_FIXTURE_PROVIDER_RECEIPT_JSON_MISSING');
  const payload = JSON.parse(fence[1]);
  if (!Number.isInteger(payload.versionNumber) || !/^[0-9a-f]{40}$/.test(String(payload.providerSourceSha || ''))) {
    throw new Error('R7_FIXTURE_PROVIDER_RECEIPT_INVALID');
  }
  return { payload, commentUrl: latest.html_url || latest.url || null };
}

function rawSnippet(needles, radius = 260) {
  for (const needle of needles) {
    const index = rawText.indexOf(needle);
    if (index < 0) continue;
    return {
      needle,
      index,
      text: rawText.slice(Math.max(0, index - radius), Math.min(rawText.length, index + needle.length + radius))
    };
  }
  return { needle: null, index: -1, text: null };
}

async function countScriptGoogleIframes(page) {
  let count = 0;
  for (const frame of page.frames()) {
    try { count += await frame.locator('iframe[src*="script.google.com"]').count(); } catch {}
  }
  return count;
}

async function frameBodyOuterHtml(frame) {
  return frame.evaluate(() => document.body?.outerHTML || '');
}

async function findIndicatorLink(page, id) {
  const selector = `[data-indicator="${id}"] [data-top-level-nav="true"]`;
  for (const frame of page.frames()) {
    const loc = frame.locator(selector);
    if (await loc.count()) return { frame, link: loc.first(), card: loc.first().locator('xpath=ancestor::*[@data-indicator][1]') };
  }
  throw new Error(`R7_FIXTURE_INDICATOR_LINK_MISSING:${id}`);
}

const provider = parseLatestProviderReceipt();
const capturedAt = new Date().toISOString();
const browser = await chromium.launch({ headless: true });
let fixture;
try {
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, storageState: undefined });
  const page = await context.newPage();
  await page.goto(canonical, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1200);
  const topBody = await frameBodyOuterHtml(page.mainFrame());
  const { frame, link, card } = await findIndicatorLink(page, 1);
  const contentBody = await frameBodyOuterHtml(frame);
  const linkOuterHTML = await link.evaluate(el => el.outerHTML);
  const cardOuterHTML = await card.evaluate(el => el.outerHTML);
  const linkDataIndicator = await link.getAttribute('data-indicator');
  const cardDataIndicator = await card.getAttribute('data-indicator');
  const hrefAttribute = await link.getAttribute('href');
  const resolvedHref = await link.evaluate(el => el.href);
  const targetAttribute = await link.getAttribute('target');
  const baseTagOuterHTML = await frame.locator('base').first().evaluate(el => el.outerHTML).catch(() => null);
  const pageUrlBeforeClick = page.url();
  const topEqualsSelfBefore = await page.evaluate(() => window.top === window.self);
  const scriptGoogleIframesBefore = await countScriptGoogleIframes(page);

  const expectedAfterClick = `${canonical}?indicator=1`;
  await Promise.all([
    page.waitForURL(url => url.toString() === expectedAfterClick, { timeout: 45000 }),
    link.click()
  ]);
  await page.waitForLoadState('domcontentloaded');
  await page.waitForTimeout(1200);
  const pageUrlAfterClick = page.url();
  const topEqualsSelfAfter = await page.evaluate(() => window.top === window.self);
  const scriptGoogleIframesAfter = await countScriptGoogleIframes(page);

  let matrixFrame = null;
  for (const candidate of page.frames()) {
    if (await candidate.locator('[data-matrix-indicator="1"]').count().catch(() => 0)) { matrixFrame = candidate; break; }
  }
  const matrix = { found: Boolean(matrixFrame) };
  if (matrixFrame) {
    const matrixBodyText = await matrixFrame.locator('body').innerText({ timeout: 5000 });
    const cards = matrixFrame.locator('[data-document-card="true"]');
    const firstCard = cards.first();
    const firstOpen = firstCard.getByText('開啟文件', { exact: true }).first();
    matrix.headingPresent = matrixBodyText.includes('指標 1｜查看文件與證據');
    matrix.warningPresent = matrixBodyText.includes('TEST／SAMPLE／CONTROL');
    matrix.documentCardCount = await cards.count();
    matrix.firstDocumentCardOuterHTML = matrix.documentCardCount ? await firstCard.evaluate(el => el.outerHTML) : null;
    matrix.firstOpenDocumentOuterHTML = await firstOpen.count() ? await firstOpen.evaluate(el => el.outerHTML) : null;
    matrix.firstOpenDocumentHrefAttribute = await firstOpen.count() ? await firstOpen.getAttribute('href') : null;
    matrix.firstOpenDocumentResolvedHref = await firstOpen.count() ? await firstOpen.evaluate(el => el.href) : null;
  }

  fs.writeFileSync(`${outDir}/browser.top.body.outerHTML.html`, topBody);
  fs.writeFileSync(`${outDir}/browser.content.body.outerHTML.html`, contentBody);
  fs.writeFileSync(`${outDir}/indicator1.link.outerHTML.html`, `${linkOuterHTML}\n`);
  fs.writeFileSync(`${outDir}/indicator1.card.outerHTML.html`, `${cardOuterHTML}\n`);

  fixture = {
    schema: 'TTQS_R7_NAV_VERIFIER_ACTUAL_FIXTURE_V1',
    capturedAt,
    source: {
      kind: 'ACTUAL_TEST_PROVIDER',
      anonymousGet: true,
      canonicalUrl: canonical,
      providerVersionEvidence: provider.commentUrl,
      providerVersion: provider.payload.versionNumber,
      providerSourceSha: provider.payload.providerSourceSha,
      deploymentId: provider.payload.deploymentId,
      providerReadbackMode: provider.payload.mode,
      providerReadbackMutation: provider.payload.mutation
    },
    rawHtmlService: {
      file: 'home.raw.html',
      bytes: raw.length,
      sha256: sha256(raw),
      indicator1NavigationSnippet: rawSnippet(['indicator\\x3d1', 'indicator\\u003d1', '?indicator=1', '查看文件與證據']),
      dataIndicatorSerialization: rawSnippet(['data-indicator']),
      hrefSerialization: rawSnippet(['href']),
      targetSerialization: rawSnippet(['target']),
      baseTagSerialization: rawSnippet(['<base', '\\x3cbase', '\\u003cbase', 'base target'])
    },
    browserDom: {
      browser: 'Playwright Chromium',
      viewport: { width: 1440, height: 1000 },
      pageUrlBeforeClick,
      topBodyFile: 'browser.top.body.outerHTML.html',
      topBodySha256: sha256(Buffer.from(topBody)),
      contentFrameUrlBeforeClick: frame.url(),
      contentBodyFile: 'browser.content.body.outerHTML.html',
      contentBodySha256: sha256(Buffer.from(contentBody)),
      indicator1: {
        linkOuterHTMLFile: 'indicator1.link.outerHTML.html',
        linkOuterHTML,
        cardOuterHTMLFile: 'indicator1.card.outerHTML.html',
        linkGetAttributeDataIndicator: linkDataIndicator,
        cardGetAttributeDataIndicator: cardDataIndicator,
        hrefAttribute,
        resolvedHref,
        targetAttribute,
        baseTagOuterHTML
      },
      click: {
        expectedUrl: expectedAfterClick,
        actualPageUrl: pageUrlAfterClick,
        windowTopEqualsSelfBefore: topEqualsSelfBefore,
        windowTopEqualsSelfAfter: topEqualsSelfAfter,
        scriptGoogleIframeCountBefore: scriptGoogleIframesBefore,
        scriptGoogleIframeCountAfter: scriptGoogleIframesAfter
      },
      matrix
    }
  };
  fs.writeFileSync(`${outDir}/fixture.json`, `${JSON.stringify(fixture, null, 2)}\n`);
  await context.close();
} finally {
  await browser.close();
}

process.stdout.write(`R7_NAV_ACTUAL_FIXTURE_CAPTURED provider_version=${fixture.source.providerVersion} source=${fixture.source.providerSourceSha} raw_sha256=${fixture.rawHtmlService.sha256} click_url=${fixture.browserDom.click.actualPageUrl}\n`);
