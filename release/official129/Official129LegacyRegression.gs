/* R7 navigation blocker fix. TEST/SAMPLE/CONTROL only; no REAL/PROD/scoring/submission. */
(function(){
  function canonicalUrl_(params){
    var keys=Object.keys(params||{}).sort(),pairs=[];
    for(var i=0;i<keys.length;i++){
      var key=keys[i],value=params[key];
      if(value===undefined||value===null||value==='')continue;
      pairs.push(encodeURIComponent(key)+'='+encodeURIComponent(String(value)));
    }
    return TTQS_R3_CANONICAL_EXEC_URL_+(pairs.length?'?'+pairs.join('&'):'');
  }
  function nav_(url,label,extra){
    return '<a class="r7button'+(extra&&extra.secondary?' secondary':'')+'" data-top-level-nav="true" target="_top" rel="noopener" href="'+esc_(url)+'">'+esc_(label)+'</a>';
  }
  function formalHuman_(value){
    var v=String(value||'');
    if(!v||v==='NOT_FORMAL_READY'||v.indexOf('FORMAL_BLOCKED')>=0||v.indexOf('NOT_FORMAL')>=0)return '目前尚未有正式辦訓證據';
    if(v.indexOf('正式可評事證')>=0&&v.indexOf('NOT_FORMAL_READY')>=0)return '目前尚未有正式辦訓證據';
    return v.replace(/NOT_FORMAL_READY/g,'目前尚未有正式辦訓證據').replace(/FORMAL_BLOCKED_NEEDS_REAL/g,'目前尚未有正式辦訓證據');
  }
  function head_(title){
    return '<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base target="_top"><title>'+esc_(title)+'</title><style>'+css_()+'.r7wrap{max-width:1240px;margin:18px auto;padding:0 12px}.r7warn{background:#fff1c9;border:2px solid #b36a00;border-radius:12px;padding:12px;line-height:1.65}.r7muted{color:#52616b}.r7mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;overflow-wrap:anywhere}.r7cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}.r7card{background:#fff;border:1px solid #d8e1e7;border-radius:14px;padding:14px}.r7badge{display:inline-block;background:#eaf2f6;border-radius:999px;padding:3px 8px;margin:2px;font-size:12px}.r7table{width:100%;border-collapse:collapse}.r7table th,.r7table td{border-bottom:1px solid #dde5ea;padding:8px;text-align:left;vertical-align:top}.r7artifact pre{white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.62;background:#fff;border:1px solid #d9e2e8;border-radius:12px;padding:16px;max-height:none}.r7bar{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}.r7button{display:inline-block;padding:9px 13px;border-radius:9px;background:#164e63;color:white;text-decoration:none}.r7button.secondary{background:#475569}.r7group{background:#f8fafc;border-left:4px solid #64748b;padding:8px;margin-top:14px}.r7doc{background:#fff;border:1px solid #d8e1e7;border-radius:14px;padding:14px;margin:12px 0}.r7doc h3{margin-top:0}.r7tech{margin-top:12px;background:#f8fafc;border-radius:10px;padding:8px}.r7tech summary{cursor:pointer;font-weight:700}.r7tech table{margin-top:8px}@media(max-width:720px){.r7wrap{margin:8px auto;padding:0 8px}.r7table{display:block;overflow-x:auto}.r7button{width:100%;box-sizing:border-box;text-align:center}}</style></head><body><main class="r7wrap">';
  }
  function foot_(){return '</main></body></html>';}
  function warning_(){return '<div class="r7warn"><b>⚠️ 模擬評核查驗｜TEST／SAMPLE／CONTROL｜非正式事證</b><br>協會目前沒有 REAL 辦訓課程、學員、講師、成果或 Outcome。本頁只驗證 TTQS ONE 的 DEMO 證據架構與查驗路徑；不得用於正式 TTQS 評分、牌等推論或官方送件。<br><b>129</b> 是依官方表「常見參考佐證資料」逐條拆分的內部加嚴 DEMO 覆蓋數，並非官方強制 129 份文件。<br><b>開啟提醒：</b>如果用 Chrome 且登入多個 Google 帳號時看到錯誤，請改用無痕視窗或 Safari 私密瀏覽開啟。</div>';}

  ttqsR7HomeHtml_=function(){
    var cards=[],countTotal=0;
    for(var i=1;i<=19;i++){
      var id=String(i),items=ttqsR7IndicatorItems_(id),focus=ttqsR7Focus_(id),st=ttqsR7Status_(id);countTotal+=items.length;
      var chips=st.sub?st.sub.split('|').map(function(x){return '<span class="r7badge">'+esc_(x)+'</span>';}).join(''):'';
      cards.push('<article class="r7card" data-indicator="'+id+'"><h2>指標 '+id+'</h2><p>'+esc_(focus[1])+'</p><div>'+chips+'</div><p><b>可查看的模擬佐證細項：</b>'+items.length+'</p><p><b>正式辦訓證據：</b>'+esc_(formalHuman_(st.formal))+'</p>'+nav_(canonicalUrl_({indicator:id}),'查看文件與證據')+'</article>');
    }
    return head_('TTQS ONE 外部唯讀評核入口｜TEST/SAMPLE')+warning_()+
      '<section class="r3panel"><h1>TTQS ONE｜顧問唯讀 DEMO 查驗入口</h1><p><b>受評客體：</b>社團法人屏東縣原始點關懷協會之 TTQS ONE TEST／SAMPLE 系統。</p><p><b>19/19：</b>只表示畫面可依 19 個 TTQS 指標查找文件與證據，不表示正式指標達成、合格或分數。</p><p><b>導航：</b>首頁 → 指標 → 文件與證據 → 文件內容；所有 Apps Script 頁面都以瀏覽器頂層頁面開啟，不使用巢狀 Web App。</p><details class="r7tech"><summary>技術細節（管理員用）</summary><table class="r7table"><tr><th>EvaluationRelease</th><td class="r7mono">'+esc_(TTQS_R7_RELEASE_ID_)+'</td></tr><tr><th>projection SHA-256</th><td class="r7mono">'+esc_(TTQS_R7_PROJECTION_RAW_SHA256_)+'</td></tr><tr><th>MANIFEST SHA-256</th><td class="r7mono">'+esc_(TTQS_R7_MANIFEST_SHA256_)+'</td></tr><tr><th>Offline ZIP SHA-256</th><td class="r7mono">'+esc_(TTQS_R7_OFFLINE_ZIP_SHA256_)+'</td></tr><tr><th>canonical /exec</th><td class="r7mono">'+esc_(TTQS_R3_CANONICAL_EXEC_URL_)+'</td></tr><tr><th>runtime live Drive</th><td>NO</td></tr></table></details></section>'+
      '<section class="r3panel"><h2>19 個指標｜查看文件與證據</h2><div class="r7cards">'+cards.join('')+'</div></section>'+
      '<section class="r3panel"><h2>覆蓋口徑</h2><table class="r7table"><tr><th>19</th><td>TTQS 訓練機構版指標主軸。</td></tr><tr><th>26</th><td>內部把部分指標子項拆開的查驗視圖；不是官方文件數。</td></tr><tr><th>129</th><td>依現行訓練機構版查核佐證文件資料表「常見參考佐證資料」逐條拆出的 DEMO 細項，共 '+countTotal+' / 129；是內部加嚴覆蓋，不是官方強制文件數。</td></tr><tr><th>REAL</th><td>0；SAMPLE 永不得轉 REAL。</td></tr></table></section>'+foot_();
  };

  ttqsR7MatrixHtml_=function(indicator){
    var id=String(indicator||''),items=ttqsR7IndicatorItems_(id);
    if(!items.length)return ttqsR7ErrorHtml_('找不到指定指標','indicator='+id);
    var focus=ttqsR7Focus_(id),st=ttqsR7Status_(id),cards=[];
    items.forEach(function(x){
      cards.push('<article class="r7doc" data-document-card="true"><h3>'+esc_(x.title)+'</h3><p>'+esc_(x.officialText)+'</p><p><b>模擬文件內容：</b>PDF '+x.pdfPages+' 頁，可直接開啟查看凍結文字投影。</p>'+nav_(canonicalUrl_({artifact:x.artifactCode}),'開啟文件')+'<details class="r7tech"><summary>技術細節（管理員用）</summary><table class="r7table"><tr><th>官方細項編號</th><td class="r7mono">'+esc_(x.officialRefId)+'</td></tr><tr><th>文件 ID</th><td class="r7mono">'+esc_(x.artifactCode)+'</td></tr><tr><th>情境代碼</th><td class="r7mono">'+esc_(x.scenario)+'</td></tr><tr><th>PDF SHA-256</th><td class="r7mono">'+esc_(x.pdfSha256)+'</td></tr><tr><th>文字投影 SHA-256</th><td class="r7mono">'+esc_(x.pdfTextSha256)+'</td></tr><tr><th>Offline path</th><td class="r7mono">'+esc_(x.offlinePdfPath)+'</td></tr></table></details></article>');
    });
    return head_('TTQS ONE｜指標 '+id+'｜文件與證據')+warning_()+'<section class="r3panel" data-matrix-indicator="'+esc_(id)+'"><div class="r7bar">'+nav_(canonicalUrl_({}),'← 回首頁',{secondary:true})+'</div><h1>指標 '+esc_(id)+'｜查看文件與證據</h1><p>'+esc_(focus[1])+'</p><p><b>正式辦訓證據：</b>'+esc_(formalHuman_(st.formal))+'</p><p><b>本指標可查看的模擬文件：</b>'+items.length+'</p>'+cards.join('')+'</section>'+foot_();
  };

  ttqsR7ArtifactHtml_=function(artifactCode){
    var requested=String(artifactCode||'');
    if(requested==='FA-DEMO-002')return ttqsR3ArtifactHtml_(requested);
    var x=ttqsR7FindItem_(requested);if(!x)return ttqsR7ErrorHtml_('找不到指定文件','artifact='+requested);
    var base=ttqsR7BaseIndicator_(x.indicator);
    return head_(x.title)+warning_()+'<article class="r3panel r7artifact" data-artifact-id="'+esc_(x.artifactCode)+'"><div class="r7bar">'+nav_(canonicalUrl_({indicator:base}),'← 回指標 '+base,{secondary:true})+nav_(canonicalUrl_({}),'回首頁',{secondary:true})+'</div><h1>'+esc_(x.title)+'</h1><h2>'+esc_(x.officialText)+'</h2><p>下方是同一凍結 PDF 的靜態文字投影；此 DEMO 執行時不查詢 live Drive。斷網時可改用同一釋出包內的離線 PDF。</p><pre class="frozen-text">'+esc_(x.text)+'</pre><details class="r7tech"><summary>技術細節（管理員用）</summary><table class="r7table"><tr><th>文件 ID</th><td class="r7mono">'+esc_(x.artifactCode)+'</td></tr><tr><th>官方細項編號</th><td class="r7mono">'+esc_(x.officialRefId)+'</td></tr><tr><th>EvaluationRelease</th><td class="r7mono">'+esc_(TTQS_R7_RELEASE_ID_)+'</td></tr><tr><th>情境代碼</th><td class="r7mono">'+esc_(x.scenario)+'</td></tr><tr><th>PDF</th><td>'+esc_(x.pdfFilename)+'｜'+x.pdfPages+' 頁</td></tr><tr><th>PDF SHA-256</th><td class="r7mono">'+esc_(x.pdfSha256)+'</td></tr><tr><th>文字投影 SHA-256</th><td class="r7mono">'+esc_(x.pdfTextSha256)+'</td></tr><tr><th>DOCX SHA-256</th><td class="r7mono">'+esc_(x.docxSha256)+'</td></tr><tr><th>PNG SHA-256</th><td class="r7mono">'+esc_(x.chartSha256)+'</td></tr><tr><th>Offline path</th><td class="r7mono">'+esc_(x.offlinePdfPath)+'</td></tr><tr><th>REAL</th><td>NO — SAMPLE／CONTROL，不構成正式辦訓事證。</td></tr></table></details></article>'+foot_();
  };

  ttqsR7ErrorHtml_=function(title,detail){return head_('TTQS ONE｜查驗路徑錯誤')+warning_()+'<section class="r3panel" data-friendly-error="true"><h1>'+esc_(title)+'</h1><p>此頁不會以空白或 HTTP 200 冒充有效證據。請由首頁重新選擇指標或文件。</p>'+nav_(canonicalUrl_({}),'返回評核入口')+'<details class="r7tech"><summary>技術細節（管理員用）</summary><p class="r7mono">'+esc_(detail||'')+'</p></details></section>'+foot_();};

  /* All Apps Script routes render through the same doGet(e); links force top-level navigation. */
  doGet=function(e){try{var p=e&&e.parameter?e.parameter:{};if(p.artifact)return HtmlService.createHtmlOutput(ttqsR7ArtifactHtml_(p.artifact)).setTitle('TTQS ONE 文件內容｜TEST/SAMPLE').addMetaTag('viewport','width=device-width, initial-scale=1');if(p.indicator)return HtmlService.createHtmlOutput(ttqsR7MatrixHtml_(p.indicator)).setTitle('TTQS ONE 文件與證據｜TEST/SAMPLE').addMetaTag('viewport','width=device-width, initial-scale=1');return HtmlService.createHtmlOutput(ttqsR7HomeHtml_()).setTitle('TTQS ONE 外部唯讀評核入口｜TEST/SAMPLE').addMetaTag('viewport','width=device-width, initial-scale=1');}catch(err){return HtmlService.createHtmlOutput(ttqsR7ErrorHtml_('查驗入口發生受控錯誤',String(err&&err.message||err))).setTitle('TTQS ONE 外部唯讀｜受控錯誤').addMetaTag('viewport','width=device-width, initial-scale=1');}};
})();

/* Preserve the existing R2/G-02 semantic regression contract without exposing engineering jargon as primary evaluator UI. */
(function(){
  var priorHome=ttqsR7HomeHtml_;
  ttqsR7HomeHtml_=function(){
    var html=priorHome();
    var block='<details class="r7tech" id="existing-contract-regression"><summary>技術細節（管理員用）｜既有驗證契約回歸摘要</summary>'+
      '<p><b>TTQS ONE · 測試／示範資料（TEST／SAMPLE）· EXTERNAL_READONLY</b></p>'+
      '<p><b>官方指標範圍：</b>19 / 19；本頁仍提供官方 19 指標評核語意導航。指標 12 保留 12a 學員遴選、12e 教學環境與設備；指標 17 保留 17a 反應評估、17d 成果評估等子項語意。</p>'+
      '<p><b>SAMPLE 評核因果鏈：</b>需求 → 設計 → 執行 → 查核 → 改善。既有四類 TEST Google Forms 生命週期仍屬系統回歸基準；4/4 類別都有 ACCEPTED 來源。</p>'+
      '<p><b>故障治理回歸：</b>故障 → 重試 → 對帳 → FINAL_ACCEPTED；MATCHED_EXACTLY_ONCE；AttemptHistory=append-only。</p>'+
      '<p><b>19 指標佐證與來源下鑽：</b>每一指標都可按「查看文件與證據」再開文件內容。Google Drive 連結只是選配，不是顧問調閱成功的必要條件。</p>'+
      '<p><b>靜態唯讀邊界：</b>不在執行期呼叫 Google Sheets／Drive API；本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL。</p>'+
      '</details>';
    return html.replace('</main></body></html>',block+'</main></body></html>');
  };
})();
