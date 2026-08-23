import fs from 'node:fs';
import crypto from 'node:crypto';
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
const sha256 = value => crypto.createHash('sha256').update(String(value)).digest('hex');
const compact = (value, max = 320) => String(value || '').replace(/\s+/g, ' ').trim().slice(0, max);

function canonicalIndicatorUrl(id) {
  return `${canonical}?indicator=${String(id)}`;
}
function canonicalArtifactUrl(value) {
  return new RegExp(`^${canonical.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\?artifact=[A-Za-z0-9._~-]+$`).test(String(value || ''));
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
    if (await loc.count()) {
      const first = loc.first();
      const card = first.locator('xpath=ancestor::*[@data-indicator][1]');
      return { frame, loc: first, card };
    }
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
    return { scrollWidth, clientWidth, innerWidth, horizontalOverflow: scrollWidth > allowedWidth + 1 };
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
          actualUrl: null,
          href: null,
          resolvedHref: null,
          target: null,
          topUrl: null,
          childFrameUrls: [],
          documentCards: 0,
          chineseDocumentCards: 0,
          openDocumentButtons: 0,
          canonicalOpenDocumentButtons: 0,
          documentCardSample: null,
          domEvidence: { home: null, matrix: null },
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

          const { frame: homeFrame, loc, card } = await findIndicatorLink(page, id);
          const linkOuterHTML = await loc.evaluate(el => el.outerHTML);
          const cardOuterHTML = await card.evaluate(el => el.outerHTML);
          const cardDataIndicator = await card.getAttribute('data-indicator');
          const linkDataIndicator = await loc.getAttribute('data-indicator');
          row.href = await loc.getAttribute('href');
          row.resolvedHref = await loc.evaluate(el => el.href);
          row.target = await loc.getAttribute('target');
          row.domEvidence.home = {
            contentFrameUrl: homeFrame.url(),
            cardDataIndicator,
            linkDataIndicator,
            hrefAttribute: row.href,
            resolvedHref: row.resolvedHref,
            targetAttribute: row.target,
            linkOuterHTMLSha256: sha256(linkOuterHTML),
            linkOuterHTMLSnippet: compact(linkOuterHTML),
            cardOuterHTMLSha256: sha256(cardOuterHTML),
            cardOuterHTMLSnippet: compact(cardOuterHTML)
          };
          if (cardDataIndicator !== String(id)) throw new Error(`R7_NAV_DATA_INDICATOR_MISSING:${cardDataIndicator}`);
          if (row.href !== expectedUrl) throw new Error(`R7_NAV_HREF_NOT_CANONICAL:${row.href}`);
          if (row.resolvedHref !== expectedUrl) throw new Error(`R7_NAV_RESOLVED_HREF_NOT_CANONICAL:${row.resolvedHref}`);
          if (row.target !== '_top') throw new Error(`R7_NAV_TARGET_NOT_TOP:${row.target}`);

          await Promise.all([
            page.waitForURL(url => url.toString() === expectedUrl, { timeout: 45000 }),
            loc.click()
          ]);
          await page.waitForLoadState('domcontentloaded');
          await page.waitForTimeout(1200);

          row.topUrl = page.url();
          row.actualUrl = row.topUrl;
          finishCheck(row, 'a_topLevelCanonicalUrl', row.topUrl === expectedUrl, row.topUrl, expectedUrl);

          const topEqualsSelf = await page.evaluate(() => window.top === window.self);
          finishCheck(row, 'b_windowTopEqualsSelf', topEqualsSelf === true, topEqualsSelf, true);

          const scriptGoogleIframeCount = await countScriptGoogleIframes(page);
          row.childFrameUrls = page.frames().filter(frame => frame !== page.mainFrame()).map(frame => frame.url());
          finishCheck(row, 'c_scriptGoogleIframeCountZero', scriptGoogleIframeCount === 0, scriptGoogleIframeCount, 0);

          const matrixFrame = await findMatrixFrame(page, id);
          const heading = `指標 ${id}｜查看文件與證據`;
          const matrixText = await matrixFrame.locator('body').innerText({ timeout: 5000 });
          finishCheck(row, 'd_chineseHeadingPresent', matrixText.includes(heading), matrixText.includes(heading) ? heading : 'MISSING', heading);

          const cards = matrixFrame.locator('[data-document-card="true"]');
          row.documentCards = await cards.count();
          let firstChineseTitle = null;
          let firstChineseCardOuterHTML = null;
          let firstOpenDocument = null;
          const perCard = [];
          for (let index = 0; index < row.documentCards; index += 1) {
            const cardLoc = cards.nth(index);
            const cardText = await cardLoc.innerText({ timeout: 3000 }).catch(() => '');
            const title = await cardLoc.locator('h1,h2,h3,h4,h5,h6').first().innerText().catch(() => null);
            const titleChinese = Boolean(title && chineseText.test(title));
            if (titleChinese) {
              row.chineseDocumentCards += 1;
              if (!row.documentCardSample) row.documentCardSample = compact(cardText, 180);
              if (!firstChineseCardOuterHTML) {
                firstChineseCardOuterHTML = await cardLoc.evaluate(el => el.outerHTML).catch(() => '');
                firstChineseTitle = title;
              }
            }
            const opens = cardLoc.getByText('開啟文件', { exact: true });
            const openCount = await opens.count().catch(() => 0);
            row.openDocumentButtons += openCount;
            let canonicalOpenCount = 0;
            let cardFirstCanonicalOpen = null;
            for (let openIndex = 0; openIndex < openCount; openIndex += 1) {
              const openLoc = opens.nth(openIndex);
              const hrefAttribute = await openLoc.getAttribute('href');
              const resolved = await openLoc.evaluate(el => el.href).catch(() => null);
              const target = await openLoc.getAttribute('target');
              if (canonicalArtifactUrl(hrefAttribute) && resolved === hrefAttribute && target === '_top') {
                row.canonicalOpenDocumentButtons += 1;
                canonicalOpenCount += 1;
                const openEvidence = { hrefAttribute, resolvedHref: resolved, targetAttribute: target, outerHTMLSnippet: compact(await openLoc.evaluate(el => el.outerHTML).catch(() => '')) };
                if (!firstOpenDocument) firstOpenDocument = openEvidence;
                if (!cardFirstCanonicalOpen) cardFirstCanonicalOpen = openEvidence;
              }
            }
            perCard.push({
              cardIndex: index + 1,
              title,
              titlePresent: Boolean(title),
              titleChinese,
              openDocumentButtonCount: openCount,
              canonicalOpenDocumentButtonCount: canonicalOpenCount,
              firstCanonicalOpenDocument: cardFirstCanonicalOpen
            });
          }
          const everyCardHasTitle = row.documentCards >= 1 && perCard.every(cardRow => cardRow.titlePresent && cardRow.titleChinese);
          const everyCardHasOpenDocument = row.documentCards >= 1 && perCard.every(cardRow => cardRow.openDocumentButtonCount >= 1);
          const everyCardHasCanonicalArtifactRoute = row.documentCards >= 1 && perCard.every(cardRow => cardRow.canonicalOpenDocumentButtonCount >= 1);
          row.domEvidence.matrix = {
            contentFrameUrl: matrixFrame.url(),
            headingExpected: heading,
            headingObserved: matrixText.includes(heading) ? heading : null,
            simulationWarningPresent: matrixText.includes('TEST／SAMPLE／CONTROL'),
            documentCardCount: row.documentCards,
            chineseDocumentCardCount: row.chineseDocumentCards,
            everyCardHasTitle,
            everyCardHasOpenDocument,
            everyCardHasCanonicalArtifactRoute,
            firstChineseDocumentTitle: firstChineseTitle,
            firstChineseDocumentCardSha256: firstChineseCardOuterHTML ? sha256(firstChineseCardOuterHTML) : null,
            firstChineseDocumentCardSnippet: firstChineseCardOuterHTML ? compact(firstChineseCardOuterHTML) : null,
            openDocumentButtonCount: row.openDocumentButtons,
            canonicalOpenDocumentButtonCount: row.canonicalOpenDocumentButtons,
            firstCanonicalOpenDocument: firstOpenDocument,
            perCard
          };
          const documentLayerOk = row.documentCards >= 1 && row.chineseDocumentCards >= 1 && everyCardHasTitle && everyCardHasOpenDocument && everyCardHasCanonicalArtifactRoute && row.domEvidence.matrix.simulationWarningPresent;
          finishCheck(
            row,
            'e_chineseDocumentCardAndOpenButton',
            documentLayerOk,
            {cards: row.documentCards, chineseCards: row.chineseDocumentCards, everyCardHasTitle, everyCardHasOpenDocument, everyCardHasCanonicalArtifactRoute, simulationWarningPresent: row.domEvidence.matrix.simulationWarningPresent},
            {cardsAtLeast: 1, chineseCardsAtLeast: 1, everyCardHasTitle: true, everyCardHasOpenDocument: true, everyCardHasCanonicalArtifactRoute: true, simulationWarningPresent: true}
          );

          const allText = await allFrameText(page);
          const refusedAbsent = !forbiddenText.test(allText);
          finishCheck(row, 'f_refusedToConnectAbsent', refusedAbsent, refusedAbsent ? 'ABSENT' : 'PRESENT', 'ABSENT');

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
          process.stdout.write(`R7_NAV_BROWSER_${row.result} viewport=${row.viewport} indicator=${row.indicator} actual=${row.actualUrl || 'NOT_REACHED'} errors=${row.errors.join('|') || 'none'}\n`);
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
  humanGate: 'UNCHANGED — R7-NAV-BLOCKER=OPEN; FA-08=FAIL; NAV-02=FAIL; T Gate=NOT PASS until human re-test',
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
