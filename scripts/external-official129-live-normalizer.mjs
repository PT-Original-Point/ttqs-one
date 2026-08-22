import {normalizeAppsScriptHtmlServiceWrapper} from './external-blackbox-classifier.mjs';

function normalizeExternalOfficial129LiveLayer(source) {
  const decoded = normalizeAppsScriptHtmlServiceWrapper(source)
    .replace(/\\x3[cC]/g, '<')
    .replace(/\\u003[cC]/g, '<')
    .replace(/\\x3[eE]/g, '>')
    .replace(/\\u003[eE]/g, '>')
    .replace(/\\x26/g, '&')
    .replace(/\\u0026/g, '&')
    .replace(/\\x27/g, "'")
    .replace(/\\u0027/g, "'")
    .replace(/\\x22/g, '"')
    .replace(/\\u0022/g, '"');

  // The live-only decode above can reveal an escape sequence already covered by
  // the shared HtmlService normalizer (for example: \\\x22 -> \\" -> ").
  // Feed the decoded bytes back through the same explicit whitelist before the
  // layer is considered stable. No generic unescape/eval/JSON decoding is used.
  return normalizeAppsScriptHtmlServiceWrapper(decoded);
}

export function normalizeExternalOfficial129LiveHtml(source) {
  let normalized = String(source ?? '');
  for (let round = 0; round < 8; round += 1) {
    const next = normalizeExternalOfficial129LiveLayer(normalized);
    if (next === normalized) return normalized;
    normalized = next;
  }
  return normalized;
}
