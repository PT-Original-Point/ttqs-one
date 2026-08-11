function ttqsNow_() {
  return Utilities.formatDate(new Date(), ttqsConfig_().TIME_ZONE, "yyyy-MM-dd'T'HH:mm:ssZ");
}

function ttqsDateOnly_(date) {
  return Utilities.formatDate(date || new Date(), ttqsConfig_().TIME_ZONE, 'yyyy-MM-dd');
}

function ttqsDigest_(value) {
  var bytes = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, String(value), Utilities.Charset.UTF_8);
  return bytes.map(function(b) {
    var v = b < 0 ? b + 256 : b;
    return ('0' + v.toString(16)).slice(-2);
  }).join('');
}

function ttqsStableId_(prefix, value, length) {
  return prefix + ttqsDigest_(value).slice(0, length || 16).toUpperCase();
}

function ttqsParseJson_(value, fallback) {
  if (!value) return fallback;
  try { return JSON.parse(value); } catch (err) { return fallback; }
}

function ttqsRedactFreeText_(value) {
  var text = String(value || '');
  text = text.replace(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi, '[REDACTED_EMAIL]');
  text = text.replace(/(?:\+?886[- ]?)?0?9\d{2}[- ]?\d{3}[- ]?\d{3}/g, '[REDACTED_PHONE]');
  text = text.replace(/\b\d{8,12}\b/g, '[REDACTED_NUMBER]');
  return text.slice(0, 1000);
}

function ttqsRequireSampleAlias_(aliasCode) {
  var value = String(aliasCode || '').trim().toUpperCase();
  if (!/^S-[A-Z0-9-]{2,24}$/.test(value)) {
    throw new Error('SAMPLE_ALIAS_REQUIRED_FORMAT_S_XXX');
  }
  return value;
}

function ttqsNumber_(value, min, max) {
  var n = Number(value);
  if (!isFinite(n) || n < min || n > max) throw new Error('INVALID_NUMERIC_RESPONSE');
  return n;
}

function ttqsUnique_(values) {
  var seen = {};
  return values.filter(function(v) {
    var key = String(v);
    if (seen[key]) return false;
    seen[key] = true;
    return true;
  });
}
