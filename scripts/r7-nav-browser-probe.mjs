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
const chineseText = /[\u3400-\u9fff]/;
const evidence = [];

function canonicalIndicatorUrl(id) {
  return `${canonical}?indicator=${String(id)}`;
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

async function countScriptGoogleIframes(page) {
  let count = 0;
  for (const frame of page.frames()) {
    try { count += await frame.locator('iframe[src*="script.google.com"]').count(); } catch {}
  }
  return count;
}

async function layoutMetrics(frame) {
  return frame.evaluate(() => {
    const root = document.documentElement;
    const body = document.body;
    const scrollWidth = Math.max(root?.scrollWidth || 0, body?.scrollWidth || 0);
    const clientWidth = Math.max(root?.clientWidth || 0, body?.clientWidth || 0);
    const innerWidth = window.innerWidth || 0;
    const allowedWidth = Math.max(clientWidth, innerWidth);
    return {
      scrollWidth,
      clientWidth,
      innerWidth,
      horizontalOverflow: scrollWidth > allowedWidth + 1
    };
  });
}

function fail(row, code, detail = '') {
  row.errors.push(detail ? `${code}:${detail}` : code);
}

function finishCheck(row, key, pass, actual, expected) {
  row.checks[key] = { pass: Boolean(pass), expected, actual };
  if (!pass) fail(row, key, typeof actual === 'string' ? actual : JSON.stringify(actual));
}

const browser = await chromium.launch({ headless: true });
try {
  for (const profile of viewports) {
    const context = await browser.newContext({ viewport: profile.viewport, storageState: undefined });
    try {
      for (let id = 1; id <= 19; id += 1) {
        const expectedUrl = canonicalIndicatorUrl(id);
        const row = {
          viewport: profile.name,
          viewportWidth: profile.viewport.width,
          indicator: id,
          expectedUrl,
          href: null,
          target: null,
          topUrl: null,
          childFrameUrls: [],
          documentCards: 0,
          chineseDocumentCards: 0,
          openDocumentButtons: 0,
          documentCardSample: null,
          checks: {},
          errors: [],
          result: 'FAIL'
        };
        const page = await context.newPage();
        try {
          await page.goto(canonical, { waitUntil: 'domcontentloaded', timeout: 45000 });
          await page.waitForTimeout(1200);
          const homeText = await allFrameText(page);
          if (forbiddenText.test(homeText)) throw new Error(`R7_NAV_HOME_REFUSED:${profile.name}:${id}`);

          const { loc } = await findIndicatorLink(page, id);
          row.href = await loc.getAttribute('href');
          row.target = await loc.getAttribute('target');
          if (row.href !== expectedUrl) throw new Error(`R7_NAV_HREF_NOT_CANONICAL:${row.href}`);
          if (row.target !== '_top') throw new Error(`R7_NAV_TARGET_NOT_TOP:${row.target}`);

          await Promise.all([
            page.waitForURL(url => url.toString() === expectedUrl, { timeout: 45000 }),
            loc.click()
          ]);
          await page.waitForLoadState('domcontentloaded');
          await page.waitForTimeout(1200);

          // a. The browser top-level URL must be the exact canonical /exec?indicator=<id> URL.
          row.topUrl = page.url();
          finishCheck(row, 'a_topLevelCanonicalUrl', row.topUrl === expectedUrl, row.topUrl, expectedUrl);

          // b. Evaluate in Playwright's top page context, not in the HtmlService content frame.
          const topEqualsSelf = await page.evaluate(() => window.top === window.self);
          finishCheck(row, 'b_windowTopEqualsSelf', topEqualsSelf === true, topEqualsSelf, true);

          // c. Apps Script may use its own googleusercontent content frame, but the product must
          // never create a nested iframe whose src points back to script.google.com.
          const scriptGoogleIframeCount = await countScriptGoogleIframes(page);
          row.childFrameUrls = page.frames().filter(frame => frame !== page.mainFrame()).map(frame => frame.url());
          finishCheck(row, 'c_scriptGoogleIframeCountZero', scriptGoogleIframeCount === 0, scriptGoogleIframeCount, 0);

          const matrixFrame = await findMatrixFrame(page, id);

          // d. Human-facing Chinese Evidence Matrix heading.
          const heading = `指標 ${id}｜查看文件與證據`;
          const matrixText = await matrixFrame.locator('body').innerText({ timeout: 5000 });
          finishCheck(row, 'd_chineseHeadingPresent', matrixText.includes(heading), matrixText.includes(heading) ? heading : 'MISSING', heading);

          // e. At least one Chinese document card and one 「開啟文件」 control must be present.
          const cards = matrixFrame.locator('[data-document-card="true"]');
          row.documentCards = await cards.count();
          for (let index = 0; index < row.documentCards; index += 1) {
            const card = cards.nth(index);
            const cardText = await card.innerText({ timeout: 3000 }).catch(() => '');
            if (chineseText.test(cardText)) {
              row.chineseDocumentCards += 1;
              if (!row.documentCardSample) row.documentCardSample = cardText.replace(/\s+/g, ' ').trim().slice(0, 180);
            }
            row.openDocumentButtons += await card.getByText('開啟文件', { exact: true }).count().catch(() => 0);
          }
          const documentLayerOk = row.documentCards >= 1 && row.chineseDocumentCards >= 1 && row.openDocumentButtons >= 1;
          finishCheck(
            row,
            'e_chineseDocumentCardAndOpenButton',
            documentLayerOk,
            {cards: row.documentCards, chineseCards: row.chineseDocumentCards, openButtons: row.openDocumentButtons},
            {cardsAtLeast: 1, chineseCardsAtLeast: 1, openButtonsAtLeast: 1}
          );

          // f. Neither the top shell nor any content frame may expose the browser refusal text.
          const allText = await allFrameText(page);
          const refusedAbsent = !forbiddenText.test(allText);
          finishCheck(row, 'f_refusedToConnectAbsent', refusedAbsent, refusedAbsent ? 'ABSENT' : 'PRESENT', 'ABSENT');

          // g. Mobile 390px must have no horizontal overflow in both the top document and
          // the actual Matrix content document. Desktop records the same metric as diagnostic.
          const topLayout = await layoutMetrics(page.mainFrame());
          const matrixLayout = await layoutMetrics(matrixFrame);
          const noHorizontalOverflow = !topLayout.horizontalOverflow && !matrixLayout.horizontalOverflow;
          finishCheck(
            row,
            'g_mobile390NoHorizontalOverflow',
            profile.name === 'mobile' ? noHorizontalOverflow : true,
            {applicable: profile.name === 'mobile', top: topLayout, matrix: matrixLayout},
            profile.name === 'mobile' ? 'NO_HORIZONTAL_OVERFLOW_AT_390PX' : 'NOT_APPLICABLE_DESKTOP'
          );

          row.result = row.errors.length === 0 ? 'PASS' : 'FAIL';
        } catch (error) {
          fail(row, 'ROUTE_EXCEPTION', String(error?.message || error));
          row.result = 'FAIL';
        } finally {
          evidence.push(row);
          process.stdout.write(`R7_NAV_BROWSER_${row.result} viewport=${row.viewport} indicator=${row.indicator} top=${row.topUrl || 'NOT_REACHED'} errors=${row.errors.join('|') || 'none'}\n`);
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

const passCount = evidence.filter(row => row.result === 'PASS').length;
const receipt = {
  schema: 'TTQS_R7_NAV_ROUTE_EVIDENCE_V2',
  canonicalUrl: canonical,
  generatedAt: new Date().toISOString(),
  scope: 'TEST/SAMPLE/CONTROL only; REAL/PROD/formal scoring/official submission = 0',
  humanGate: 'UNCHANGED — FA-08=FAIL; NAV-02=FAIL; T Gate=NOT PASS until human re-test',
  viewports: viewports.map(x => ({name: x.name, ...x.viewport})),
  indicators: 19,
  checks: evidence.length,
  passCount,
  failCount: evidence.length - passCount,
  result: evidence.length === 38 && passCount === 38 ? 'PASS_MACHINE_BROWSER' : 'FAIL_MACHINE_BROWSER',
  evidence
};
fs.writeFileSync(process.env.R7_NAV_EVIDENCE_OUT || 'r7-nav-browser-evidence.json', `${JSON.stringify(receipt, null, 2)}\n`);
if (evidence.length !== 38 || passCount !== 38) {
  throw new Error(`R7_NAV_BROWSER_FAIL:${passCount}/38`);
}
process.stdout.write('R7_NAV_BROWSER_ALL_PASS viewports=2 indicators=19 checks=38\n');
