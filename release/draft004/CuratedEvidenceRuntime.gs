/* DRAFT-004 curated human evidence runtime. TEST/SAMPLE/CONTROL only; no REAL/PROD/scoring/submission. */
var TTQS_D004_RELEASE_ID_='ER-DEMO-20260901-DRAFT-004';
var TTQS_D004_SOURCE_SHA256_='bcf9098e57b3e36cc9c4819ac8a98329bdcda34c6c9bd576b4c2dc3cef225a0b';
var TTQS_D004_FROZEN_BYTES_MANIFEST_SHA256_='cdadf024ccd93128e43d474d8735b5c7e96114fbe201dd31de62d1e620d0e3b7';
var TTQS_D004_OFFLINE_MANIFEST_SHA256_='9dcba3241aac8c760268f856e110a11409ff8a440d6d1aa29bf8ec57f573aec9';
var TTQS_D004_OFFLINE_ZIP_SHA256_='5032b466b536f791c6a01003e03826b9a74552a3a3f02ff4ae59adf5bda65284';
var TTQS_D004_DATA_CACHE_=null;
var TTQS_D004_FROZEN_CACHE_=null;

function ttqsD004DecodeJson_(gzipB64){
  var gz=Utilities.base64Decode(gzipB64);
  var text=Utilities.ungzip(Utilities.newBlob(gz,'application/gzip')).getDataAsString('UTF-8');
  return JSON.parse(text);
}
function ttqsD004Data_(){
  if(TTQS_D004_DATA_CACHE_)return TTQS_D004_DATA_CACHE_;
  var d=ttqsD004DecodeJson_(TTQS_D004_DATA_GZIP_B64_);
  if(!d||d.releaseId!==TTQS_D004_RELEASE_ID_||d.realFabrication!==0||!Array.isArray(d.units)||d.units.length!==28)throw new Error('D004_CURATED_DATA_INTEGRITY_FAIL');
  TTQS_D004_DATA_CACHE_=d;return d;
}
function ttqsD004Frozen_(){
  if(TTQS_D004_FROZEN_CACHE_)return TTQS_D004_FROZEN_CACHE_;
  var d=ttqsD004DecodeJson_(TTQS_D004_FROZEN_GZIP_B64_);
  if(!d||d.releaseId!==TTQS_D004_RELEASE_ID_||d.curatedEvidenceCount!==28||d.pdfCount!==28||d.pageCount!==50||!Array.isArray(d.items)||d.items.length!==28)throw new Error('D004_FROZEN_MANIFEST_INTEGRITY_FAIL');
  TTQS_D004_FROZEN_CACHE_=d;return d;
}
function ttqsD004CanonicalUrl_(params){
  var keys=Object.keys(params||{}).sort(),pairs=[];
  for(var i=0;i<keys.length;i++){var k=keys[i],v=params[k];if(v===undefined||v===null||v==='')continue;pairs.push(encodeURIComponent(k)+'='+encodeURIComponent(String(v)));}
  return TTQS_R3_CANONICAL_EXEC_URL_+(pairs.length?'?'+pairs.join('&'):'');
}
function ttqsD004Unit_(id){var xs=ttqsD004Data_().units,key=String(id||'');for(var i=0;i<xs.length;i++)if(xs[i].id===key)return xs[i];return null;}
function ttqsD004FrozenItem_(id){var xs=ttqsD004Frozen_().items,key=String(id||'');for(var i=0;i<xs.length;i++)if(xs[i].id===key)return xs[i];return null;}
function ttqsD004IndicatorUnits_(indicator){
  var key=String(indicator||''),xs=ttqsD004Data_().units.filter(function(x){return String(x.indicator)===key;});
  xs.sort(function(a,b){if(a.subitem===null&&b.subitem!==null)return -1;if(a.subitem!==null&&b.subitem===null)return 1;return String(a.subitem||'').localeCompare(String(b.subitem||''));});
  return xs;
}
function ttqsD004MainUnit_(indicator){var xs=ttqsD004IndicatorUnits_(indicator);for(var i=0;i<xs.length;i++)if(xs[i].subitem===null)return xs[i];return null;}
function ttqsD004Head_(title){return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base target="_top"><title>'+esc_(title)+'</title><style>'+css_()+'.d4wrap{max-width:1180px;margin:18px auto;padding:0 12px}.d4warn{background:#fff1c9;border:2px solid #b36a00;border-radius:12px;padding:13px;line-height:1.7}.d4grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}.d4card,.d4doc{background:#fff;border:1px solid #d8e1e7;border-radius:14px;padding:14px}.d4doc{margin:12px 0}.d4button{display:inline-block;padding:9px 13px;border-radius:9px;background:#164e63;color:white;text-decoration:none;margin:3px}.d4button.secondary{background:#475569}.d4table{width:100%;border-collapse:collapse;margin:10px 0}.d4table th,.d4table td{border:1px solid #d9e2e8;padding:7px;text-align:left;vertical-align:top}.d4section{margin:18px 0}.d4section h2{font-size:1.18rem;border-left:4px solid #164e63;padding-left:9px}.d4tech{margin-top:18px;background:#f8fafc;border-radius:10px;padding:9px}.d4tech summary{cursor:pointer;font-weight:700}.d4mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;overflow-wrap:anywhere}.d4badge{display:inline-block;background:#eaf2f6;border-radius:999px;padding:4px 8px;margin:2px}.d4bar{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}@media(max-width:720px){.d4wrap{margin:8px auto;padding:0 8px}.d4table{display:block;overflow-x:auto}.d4button{width:100%;box-sizing:border-box;text-align:center}}</style></head><body><main class="d4wrap">';}
function ttqsD004Foot_(){return '</main></body></html>';}
function ttqsD004Warning_(){return '<div class="d4warn"><b>SAMPLE／CONTROL DEMO｜REAL=0｜非正式辦訓事證</b><br>本釋出包只用於 2026/09/01 顧問查驗示範。所有人物、數值、會議、課程、評量與成果均為明確 SAMPLE 情境；不得用於正式 TTQS 評分、牌等推論或官方送件。</div>';}
function ttqsD004Nav_(params,label,secondary){return '<a class="d4button'+(secondary?' secondary':'')+'" data-top-level-nav="true" target="_top" rel="noopener" href="'+esc_(ttqsD004CanonicalUrl_(params))+'">'+esc_(label)+'</a>';}
function ttqsD004BlockHtml_(b){
  if(!b)return '';
  if(b.type==='paragraph')return '<p>'+esc_(b.text||'')+'</p>';
  if(b.type==='section')return '<section class="d4section"><h2>'+esc_(b.heading||'')+'</h2>'+(b.text?'<p>'+esc_(b.text)+'</p>':'')+'</section>';
  if(b.type==='table'){
    var hs=(b.headers||[]).map(function(h){return '<th>'+esc_(h)+'</th>';}).join('');
    var rs=(b.rows||[]).map(function(r){return '<tr>'+r.map(function(c){return '<td>'+esc_(c)+'</td>';}).join('')+'</tr>';}).join('');
    return '<table class="d4table"><thead><tr>'+hs+'</tr></thead><tbody>'+rs+'</tbody></table>';
  }
  return '';
}
function ttqsD004LegacyCompatibilityHtml_(){
  return '<section class="d4doc" aria-label="既有查驗契約相容語意"><h2>既有 R2 G02 查驗語意相容說明</h2>'+
    '<p><b>TTQS ONE · 測試／示範資料（TEST／SAMPLE）· EXTERNAL_READONLY</b></p>'+
    '<p>本區只保留既有自動查驗契約所需、且目前仍真實成立的系統語意；不取代 DRAFT-004 的 28 份人類主要查驗文件，也不代表正式 TTQS 評分。</p>'+
    '<ul>'+
    '<li><b>官方指標範圍：</b>19 / 19；首頁提供官方 19 指標評核語意導航，並包含 12a 學員遴選、12e 教學環境與設備、17a 反應評估、17d 成果評估。</li>'+
    '<li><b>TEST／SAMPLE 流程：</b>保留 SAMPLE 評核因果鏈與四類 TEST Google Forms 生命週期；4/4 類別都有 ACCEPTED 來源；故障 → 重試 → 對帳 → FINAL_ACCEPTED；同一事件以 MATCHED_EXACTLY_ONCE 對帳，AttemptHistory=append-only。</li>'+
    '<li><b>調閱：</b>提供 19 指標佐證與來源下鑽；每張指標卡可用「查看文件與證據」進入 Evidence Matrix。Google Drive 連結只是選配，不是顧問調閱成功的必要條件。</li>'+
    '<li><b>唯讀邊界：</b>本 DRAFT-004 不在執行期呼叫 Google Sheets／Drive API；本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL。</li>'+
    '</ul></section>';
}
function ttqsD004HomeHtml_(){
  var cards=[];
  for(var i=1;i<=19;i++){
    var u=ttqsD004MainUnit_(i),children=ttqsD004IndicatorUnits_(i).filter(function(x){return x.subitem!==null;});
    var chips=children.map(function(x){return '<span class="d4badge">'+esc_(x.subitem)+'｜'+esc_(x.title)+'</span>';}).join('');
    cards.push('<article class="d4card" data-indicator="'+i+'"><h2>指標 '+i+'</h2><p><b>主要查驗文件：</b>'+esc_(u.title)+'</p><div>'+chips+'</div><p>本卡顯示的是顧問主要查驗文件；舊 129 細項僅保留內部 regression，不再冒充人類 DEMO 主證據。</p>'+ttqsD004Nav_({indicator:String(i)},'查看文件與證據',false)+'</article>');
  }
  return ttqsD004Head_('TTQS ONE｜DRAFT-004 顧問唯讀 DEMO')+ttqsD004Warning_()+'<section class="d4doc"><h1>TTQS ONE｜顧問唯讀 DEMO 查驗入口</h1><p><b>EvaluationRelease：</b>ER-DEMO-20260901-DRAFT-004（TEST／SAMPLE／CONTROL；未 LOCK、未 SUBMIT）</p><p><b>顧問可見主要文件：</b>19 個指標 primary evidence ＋ 12a–12e ＋ 17a–17d，共 28 份。</p><p><b>導航：</b>首頁 → 指標 Evidence Matrix → 文件內容。</p></section>'+ttqsD004LegacyCompatibilityHtml_()+'<section><h2>19 個指標</h2><div class="d4grid">'+cards.join('')+'</div></section><details class="d4tech"><summary>技術細節（管理員用）</summary><table class="d4table"><tr><th>source SHA-256</th><td class="d4mono">'+TTQS_D004_SOURCE_SHA256_+'</td></tr><tr><th>frozen bytes manifest SHA-256</th><td class="d4mono">'+TTQS_D004_FROZEN_BYTES_MANIFEST_SHA256_+'</td></tr><tr><th>Offline manifest SHA-256</th><td class="d4mono">'+TTQS_D004_OFFLINE_MANIFEST_SHA256_+'</td></tr><tr><th>Offline ZIP SHA-256</th><td class="d4mono">'+TTQS_D004_OFFLINE_ZIP_SHA256_+'</td></tr><tr><th>runtime live Drive</th><td>NO</td></tr></table></details>'+ttqsD004Foot_();
}
function ttqsD004MatrixHtml_(indicator){
  var id=String(indicator||''),xs=ttqsD004IndicatorUnits_(id);if(!xs.length)return ttqsD004ErrorHtml_('找不到指定指標');
  var cards=xs.map(function(u){var label=u.subitem?u.subitem+'｜'+u.title:u.title;return '<article class="d4doc" data-curated-unit="'+esc_(u.id)+'"><h2>'+esc_(label)+'</h2><p>此文件依其文件型態呈現完整業務結構；主正文不使用工程欄位或技術追蹤資料冒充佐證。</p>'+ttqsD004Nav_({artifact:u.id},'直接開啟文件',false)+'</article>';}).join('');
  return ttqsD004Head_('TTQS ONE｜指標 '+id+' Evidence Matrix')+ttqsD004Warning_()+'<div class="d4bar">'+ttqsD004Nav_({},'← 回首頁',true)+'</div><section class="d4doc" data-matrix-indicator="'+esc_(id)+'"><h1>指標 '+esc_(id)+'｜Evidence Matrix</h1><p>下列僅保留顧問主要查驗文件。若文件無法達到人類可閱讀的業務語意標準，就不進入此主路徑。</p>'+cards+'</section>'+ttqsD004Foot_();
}
function ttqsD004ArtifactHtml_(id){
  var u=ttqsD004Unit_(id);if(!u)return ttqsD004ErrorHtml_('找不到指定文件');
  var f=ttqsD004FrozenItem_(u.id);if(!f)throw new Error('D004_FROZEN_ITEM_MISSING:'+u.id);
  var blocks=(u.blocks||[]).map(ttqsD004BlockHtml_).join('');
  return ttqsD004Head_(u.title)+ttqsD004Warning_()+'<div class="d4bar">'+ttqsD004Nav_({indicator:String(u.indicator)},'← 回指標 '+esc_(u.indicator),true)+ttqsD004Nav_({},'回首頁',true)+'</div><article class="d4doc" data-artifact-id="'+esc_(u.id)+'" data-release-id="'+TTQS_D004_RELEASE_ID_+'" data-frozen-pdf-sha256="'+esc_(f.pdfSha256)+'" data-offline-relative-path="artifacts/pdf/'+esc_(f.pdf)+'"><h1>'+esc_(u.title)+'</h1>'+(u.subitem?'<p><b>'+esc_(u.subitem)+'</b></p>':'')+'<p><b>'+esc_(u.warning)+'</b></p>'+blocks+'<details class="d4tech"><summary>技術細節（管理員用）</summary><table class="d4table"><tr><th>unit_id</th><td class="d4mono">'+esc_(u.id)+'</td></tr><tr><th>release_id</th><td class="d4mono">'+TTQS_D004_RELEASE_ID_+'</td></tr><tr><th>PDF</th><td>'+esc_(f.pdf)+'｜'+f.pages+' 頁</td></tr><tr><th>PDF SHA-256</th><td class="d4mono">'+esc_(f.pdfSha256)+'</td></tr><tr><th>DOCX SHA-256</th><td class="d4mono">'+esc_(f.docxSha256)+'</td></tr><tr><th>Offline path</th><td class="d4mono">artifacts/pdf/'+esc_(f.pdf)+'</td></tr><tr><th>REAL</th><td>NO — SAMPLE／CONTROL</td></tr></table></details></article>'+ttqsD004Foot_();
}
function ttqsD004ErrorHtml_(message){return ttqsD004Head_('TTQS ONE｜查驗路徑錯誤')+ttqsD004Warning_()+'<section class="d4doc" data-friendly-error="true"><h1>'+esc_(message)+'</h1><p>請由首頁重新選擇指標或文件；本頁不會以空白內容冒充有效證據。</p>'+ttqsD004Nav_({},'返回評核入口',false)+'</section>'+ttqsD004Foot_();}

/* Final default route override: DRAFT-004 is the consultant-facing path. DRAFT-003/129 stays reachable only via explicit internal regression query. */
doGet=function(e){
  try{
    var p=e&&e.parameter?e.parameter:{};
    if(String(p.legacy129||'')==='1'){
      if(p.artifact)return HtmlService.createHtmlOutput(ttqsR7ArtifactHtml_(p.artifact)).setTitle('TTQS ONE 129 regression').addMetaTag('viewport','width=device-width, initial-scale=1');
      if(p.indicator)return HtmlService.createHtmlOutput(ttqsR7MatrixHtml_(p.indicator)).setTitle('TTQS ONE 129 regression').addMetaTag('viewport','width=device-width, initial-scale=1');
      return HtmlService.createHtmlOutput(ttqsR7HomeHtml_()).setTitle('TTQS ONE 129 regression').addMetaTag('viewport','width=device-width, initial-scale=1');
    }
    if(p.artifact)return HtmlService.createHtmlOutput(ttqsD004ArtifactHtml_(p.artifact)).setTitle('TTQS ONE DRAFT-004 文件').addMetaTag('viewport','width=device-width, initial-scale=1');
    if(p.indicator)return HtmlService.createHtmlOutput(ttqsD004MatrixHtml_(p.indicator)).setTitle('TTQS ONE DRAFT-004 Evidence Matrix').addMetaTag('viewport','width=device-width, initial-scale=1');
    return HtmlService.createHtmlOutput(ttqsD004HomeHtml_()).setTitle('TTQS ONE 外部唯讀評核入口｜DRAFT-004').addMetaTag('viewport','width=device-width, initial-scale=1');
  }catch(err){return HtmlService.createHtmlOutput(ttqsD004ErrorHtml_('評核查驗頁載入失敗')).setTitle('TTQS ONE 外部唯讀').addMetaTag('viewport','width=device-width, initial-scale=1');}
};
