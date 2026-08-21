/* R7 official-evidence integration. TEST/SAMPLE/CONTROL only; no REAL/PROD/scoring/submission. */
var TTQS_R7_RELEASE_ID_='ER-DEMO-20260901-DRAFT-002';
var TTQS_R7_DATA_CLASS_='TEST/SAMPLE/CONTROL';
var TTQS_R7_PROJECTION_RAW_SHA256_='7567530e1f72ef5c8ec491aa38936bf7884ef258943df5f01e0fce08c0c3f2de';
var TTQS_R7_MANIFEST_SHA256_='2673e9abd5942eb3b3c27a5a54e05b1f73339a902035787344b65d2027e052ee';
var TTQS_R7_OFFLINE_ZIP_SHA256_='5026066430bd65c57f4c2adb59cef6e4bad70a6fcda298f89d864938dba0c676';
var TTQS_R7_DATA_CACHE_=null;

function ttqsR7Data_(){
  if(TTQS_R7_DATA_CACHE_)return TTQS_R7_DATA_CACHE_;
  var gz=Utilities.base64Decode(TTQS_R7_DATA_GZIP_B64_);
  var jsonText=Utilities.ungzip(Utilities.newBlob(gz,'application/gzip')).getDataAsString('UTF-8');
  var parsed=JSON.parse(jsonText);
  if(!parsed||parsed.releaseId!==TTQS_R7_RELEASE_ID_||!Array.isArray(parsed.items)||parsed.items.length!==129)throw new Error('R7_STATIC_PROJECTION_INTEGRITY_FAIL');
  TTQS_R7_DATA_CACHE_=parsed;
  return parsed;
}
function ttqsR7BaseIndicator_(value){var m=String(value||'').match(/^\d+/);return m?m[0]:'';}
function ttqsR7IndicatorItems_(indicator){var id=String(indicator||'');if(!/^(?:[1-9]|1[0-9])$/.test(id))return [];return ttqsR7Data_().items.filter(function(x){return ttqsR7BaseIndicator_(x.indicator)===id;});}
function ttqsR7FindItem_(artifactCode){var id=String(artifactCode||'');var xs=ttqsR7Data_().items;for(var i=0;i<xs.length;i++)if(xs[i].artifactCode===id)return xs[i];return null;}
function ttqsR7AbsUrl_(query){return TTQS_R3_CANONICAL_EXEC_URL_+'?'+query;}
function ttqsR7Level_(v){return String(v||'')||'一般佐證';}
function ttqsR7Focus_(id){
  for(var i=0;i<TTQS_EXTERNAL_OFFICIAL_FOCUS_.length;i++)if(String(TTQS_EXTERNAL_OFFICIAL_FOCUS_[i][0])===String(id))return TTQS_EXTERNAL_OFFICIAL_FOCUS_[i];
  return [String(id),'依現行訓練機構版查核佐證文件資料表逐項調閱。',[],''];
}
function ttqsR7Status_(id){var r=TTQS_INDICATORS_[Number(id)-1]||[];return {formal:String(r[3]||'NOT_FORMAL_READY'),sub:String(r[6]||'')};}
function ttqsR7Head_(title){return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc_(title)+'</title><style>'+css_()+'.r7wrap{max-width:1240px;margin:18px auto;padding:0 12px}.r7warn{background:#fff1c9;border:2px solid #b36a00;border-radius:12px;padding:12px;line-height:1.65}.r7muted{color:#52616b}.r7mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;overflow-wrap:anywhere}.r7cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}.r7card{background:#fff;border:1px solid #d8e1e7;border-radius:14px;padding:14px}.r7badge{display:inline-block;background:#eaf2f6;border-radius:999px;padding:3px 8px;margin:2px;font-size:12px}.r7table{width:100%;border-collapse:collapse}.r7table th,.r7table td{border-bottom:1px solid #dde5ea;padding:8px;text-align:left;vertical-align:top}.r7artifact pre{white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.62;background:#fff;border:1px solid #d9e2e8;border-radius:12px;padding:16px;max-height:none}.r7bar{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}.r7button{display:inline-block;padding:8px 12px;border-radius:9px;background:#164e63;color:white;text-decoration:none}.r7button.secondary{background:#475569}.r7group{background:#f8fafc;border-left:4px solid #64748b;padding:8px;margin-top:14px}</style></head><body><main class="r7wrap">';}
function ttqsR7Foot_(){return '</main></body></html>';}
function ttqsR7Warning_(){return '<div class="r7warn"><b>⚠️ 模擬評核查驗｜TEST／SAMPLE／CONTROL｜非正式事證</b><br>協會目前沒有 REAL 辦訓課程、學員、講師、成果或 Outcome。本頁只驗證 TTQS ONE 的 DEMO 證據架構與查驗路徑；不得用於正式 TTQS 評分、牌等推論或官方送件。<br><b>129</b> 是依官方表「常見參考佐證資料」逐條拆分的 TTQS ONE 內部加嚴 DEMO 覆蓋數；官方原文為「以下為例，但不以此為限」，並非官方強制 129 份文件。</div>';}

function ttqsR7HomeHtml_(){
  var data=ttqsR7Data_();var cards=[];var countTotal=0;
  for(var i=1;i<=19;i++){
    var id=String(i),items=ttqsR7IndicatorItems_(id),focus=ttqsR7Focus_(id),st=ttqsR7Status_(id);countTotal+=items.length;
    var chips=st.sub?st.sub.split('|').map(function(x){return '<span class="r7badge">'+esc_(x)+'</span>';}).join(''):'';
    cards.push('<article class="r7card" data-indicator="'+id+'"><h2>指標 '+id+'</h2><p>'+esc_(focus[1])+'</p><div>'+chips+'</div><p><b>DEMO 常見佐證細項：</b>'+items.length+'</p><p><b>正式可評事證：</b>'+esc_(st.formal)+'</p><a class="r7button" data-matrix-indicator="'+id+'" href="'+esc_(ttqsR7AbsUrl_('indicator='+id))+'">查看佐證與來源｜Evidence Matrix</a></article>');
  }
  return ttqsR7Head_('TTQS ONE 外部唯讀評核入口｜TEST/SAMPLE')+ttqsR7Warning_()+
    '<section class="r3panel"><h1>TTQS ONE｜顧問唯讀 DEMO 查驗入口</h1><p><b>受評客體：</b>社團法人屏東縣原始點關懷協會之 TTQS ONE TEST/SAMPLE 系統。</p><p><b>19/19：</b>只表示介面與查驗路徑涵蓋 19 個 TTQS 指標；不表示正式指標達成、合格或分數。</p><p><b>EvaluationRelease：</b><span class="r7mono">'+TTQS_R7_RELEASE_ID_+'</span>（DRAFT DEMO，未 LOCK、未 SUBMIT）</p><p><b>導航：</b>首頁 → 指標 Evidence Matrix → FrozenArtifact；最多 2 次連結導航即可到文件內容，低於 Mission 上限 3 次。</p><p><b>Offline Pack：</b>同一 release 含 129 PDF／DOCX／PNG、130-sheet XLSX、離線 index、manifest 與 route map；斷網可直接開 index.html。</p></section>'+
    '<section class="r3panel"><h2>19 指標｜Evidence Matrix 入口</h2><div class="r7cards">'+cards.join('')+'</div></section>'+
    '<section class="r3panel"><h2>覆蓋口徑與查驗治理</h2><table class="r7table"><tr><th>19</th><td>TTQS 訓練機構版指標主軸。</td></tr><tr><th>26</th><td>TTQS ONE 既有 OfficialEvidenceChecklistDraft 的指標／子項評核列視圖（含 12a–e、17a–d）；不是 129 的替代品。</td></tr><tr><th>129</th><td>依現行訓練機構版查核佐證文件資料表「常見參考佐證資料」逐條拆出的 DEMO 細項，共 '+countTotal+' / 129；是內部加嚴覆蓋，不是官方強制文件數。</td></tr><tr><th>REAL</th><td>0；SAMPLE 永不得轉 REAL。</td></tr></table></section>'+
    '<section class="r3panel"><details><summary>完整性技術資訊（管理員用）</summary><table class="r7table"><tr><th>projection source SHA-256</th><td class="r7mono">'+TTQS_R7_PROJECTION_RAW_SHA256_+'</td></tr><tr><th>Offline MANIFEST SHA-256</th><td class="r7mono">'+TTQS_R7_MANIFEST_SHA256_+'</td></tr><tr><th>Offline ZIP SHA-256</th><td class="r7mono">'+TTQS_R7_OFFLINE_ZIP_SHA256_+'</td></tr><tr><th>runtime live Drive</th><td>NO</td></tr></table></details></section>'+ttqsR7Foot_();
}

function ttqsR7MatrixHtml_(indicator){
  var id=String(indicator||'');var items=ttqsR7IndicatorItems_(id);if(!items.length)return ttqsR7ErrorHtml_('找不到指定指標','indicator='+id);
  var focus=ttqsR7Focus_(id),st=ttqsR7Status_(id),groups={},order=[];
  items.forEach(function(x){var g=(id==='17'?x.indicator:ttqsR7Level_(x.level));if(!groups[g]){groups[g]=[];order.push(g);}groups[g].push(x);});
  var sections=order.map(function(g){var rows=groups[g].map(function(x){return '<tr data-official-ref-id="'+esc_(x.officialRefId)+'" data-artifact-code="'+esc_(x.artifactCode)+'"><td>'+x.seq+'</td><td><b>'+esc_(x.officialRefId)+'</b><br>'+esc_(x.officialText)+'</td><td>'+esc_(x.scenario)+'</td><td><span class="r7mono">'+esc_(x.artifactCode)+'</span><br>PDF '+x.pdfPages+' 頁／文字 '+x.pdfTextChars+' 字元</td><td><a class="r7button" data-frozen-artifact-id="'+esc_(x.artifactCode)+'" target="_blank" rel="noopener noreferrer" href="'+esc_(ttqsR7AbsUrl_('artifact='+encodeURIComponent(x.artifactCode)))+'">開啟 FrozenArtifact</a></td></tr>';}).join('');return '<div class="r7group"><b>'+esc_(g)+'</b></div><table class="r7table"><thead><tr><th>#</th><th>官方常見參考佐證細項</th><th>模擬情境</th><th>Frozen source</th><th>查驗</th></tr></thead><tbody>'+rows+'</tbody></table>';}).join('');
  return ttqsR7Head_('TTQS ONE｜指標 '+id+' Evidence Matrix')+ttqsR7Warning_()+
   '<section class="r3panel" data-matrix-indicator="'+esc_(id)+'"><div class="r7bar"><a class="r7button secondary" href="'+esc_(TTQS_R3_CANONICAL_EXEC_URL_)+'">← 回首頁</a></div><h1>指標 '+esc_(id)+'｜Evidence Matrix</h1><p>'+esc_(focus[1])+'</p><p><b>正式可評事證：</b>'+esc_(st.formal)+'</p><p><b>本指標 DEMO 細項：</b>'+items.length+'；每列均有獨立 artifact code、PDF SHA-256、文字投影 SHA-256 與 Offline 相對路徑。</p>'+sections+'</section>'+ttqsR7Foot_();
}

function ttqsR7ArtifactHtml_(artifactCode){
  var requested=String(artifactCode||'');
  if(requested==='FA-DEMO-002')return ttqsR3ArtifactHtml_(requested);
  var x=ttqsR7FindItem_(requested);if(!x)return ttqsR7ErrorHtml_('找不到指定 FrozenArtifact','artifact='+requested);
  var base=ttqsR7BaseIndicator_(x.indicator);
  return ttqsR7Head_(x.title+'｜'+x.artifactCode)+ttqsR7Warning_()+
    '<article class="r3panel r7artifact" data-artifact-id="'+esc_(x.artifactCode)+'" data-official-ref-id="'+esc_(x.officialRefId)+'" data-release-id="'+esc_(TTQS_R7_RELEASE_ID_)+'" data-frozen-pdf-sha256="'+esc_(x.pdfSha256)+'" data-text-sha256="'+esc_(x.pdfTextSha256)+'" data-offline-relative-path="'+esc_(x.offlinePdfPath)+'"><div class="r7bar"><a class="r7button secondary" href="'+esc_(ttqsR7AbsUrl_('indicator='+base))+'">← 回指標 '+esc_(base)+' Matrix</a><a class="r7button secondary" href="'+esc_(TTQS_R3_CANONICAL_EXEC_URL_)+'">回首頁</a></div><h1>'+esc_(x.title)+'</h1><h2>'+esc_(x.officialRefId)+'｜'+esc_(x.officialText)+'</h2><p>下方是 Offline Pack 同一凍結 PDF 以 <span class="r7mono">pdftotext -layout</span> 產生的 build-time 靜態文字投影；runtime 不查詢 live Drive。若網路中斷，以同一 release 的 <span class="r7mono">'+esc_(x.offlinePdfPath)+'</span> 為離線原件。</p><table class="r7table"><tr><th>scenario</th><td>'+esc_(x.scenario)+'</td></tr><tr><th>level</th><td>'+esc_(ttqsR7Level_(x.level))+'</td></tr><tr><th>PDF</th><td>'+esc_(x.pdfFilename)+'｜'+x.pdfPages+' 頁</td></tr><tr><th>PDF SHA-256</th><td class="r7mono">'+esc_(x.pdfSha256)+'</td></tr><tr><th>文字投影 SHA-256</th><td class="r7mono">'+esc_(x.pdfTextSha256)+'</td></tr><tr><th>DOCX SHA-256</th><td class="r7mono">'+esc_(x.docxSha256)+'</td></tr><tr><th>PNG SHA-256</th><td class="r7mono">'+esc_(x.chartSha256)+'</td></tr><tr><th>Offline path</th><td class="r7mono">'+esc_(x.offlinePdfPath)+'</td></tr><tr><th>REAL</th><td>NO — SAMPLE/CONTROL，不構成正式辦訓事證。</td></tr></table><h2>Frozen PDF 文字投影</h2><pre class="frozen-text">'+esc_(x.text)+'</pre></article>'+ttqsR7Foot_();
}

function ttqsR7ErrorHtml_(title,detail){return ttqsR7Head_('TTQS ONE｜查驗路徑錯誤')+ttqsR7Warning_()+'<section class="r3panel" data-friendly-error="true"><h1>'+esc_(title)+'</h1><p>此頁不會以空白或 HTTP 200 冒充有效證據。請由首頁重新選擇指標或 FrozenArtifact。</p><p class="r7mono">'+esc_(detail||'')+'</p><a class="r7button" href="'+esc_(TTQS_R3_CANONICAL_EXEC_URL_)+'">返回評核入口</a></section>'+ttqsR7Foot_();}

/* Final R7 route override. Existing R3 FA-DEMO-002 remains as regression/control route. */
doGet=function(e){try{var p=e&&e.parameter?e.parameter:{};if(p.artifact)return HtmlService.createHtmlOutput(ttqsR7ArtifactHtml_(p.artifact)).setTitle('TTQS ONE FrozenArtifact｜TEST/SAMPLE').addMetaTag('viewport','width=device-width, initial-scale=1');if(p.indicator)return HtmlService.createHtmlOutput(ttqsR7MatrixHtml_(p.indicator)).setTitle('TTQS ONE Evidence Matrix｜TEST/SAMPLE').addMetaTag('viewport','width=device-width, initial-scale=1');return HtmlService.createHtmlOutput(ttqsR7HomeHtml_()).setTitle('TTQS ONE 外部唯讀評核入口｜TEST/SAMPLE').addMetaTag('viewport','width=device-width, initial-scale=1');}catch(err){return HtmlService.createHtmlOutput(ttqsR7ErrorHtml_('查驗入口發生受控錯誤',String(err&&err.message||err))).setTitle('TTQS ONE 外部唯讀｜受控錯誤').addMetaTag('viewport','width=device-width, initial-scale=1');}};
