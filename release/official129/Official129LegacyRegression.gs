/* Visible regression summary: preserves the already-approved D6/D8 evaluator semantics while R7 adds 129-item drill-down. */
(function(){
  var prior=ttqsR7HomeHtml_;
  ttqsR7HomeHtml_=function(){
    var html=prior();
    var block='<section class="r3panel" id="existing-contract-regression"><h2>既有 TEST／SAMPLE 驗證契約｜回歸摘要</h2>'+
      '<p><b>TTQS ONE · 測試／示範資料（TEST／SAMPLE）· EXTERNAL_READONLY</b></p>'+
      '<p><b>官方指標範圍：</b>19 / 19；本頁仍提供官方 19 指標評核語意導航。指標 12 保留 12a 學員遴選、12e 教學環境與設備；指標 17 保留 17a 反應評估、17d 成果評估等子項語意。</p>'+
      '<p><b>SAMPLE 評核因果鏈：</b>需求 → 設計 → 執行 → 查核 → 改善。既有四類 TEST Google Forms 生命週期仍屬系統回歸基準；4/4 類別都有 ACCEPTED 來源。</p>'+
      '<p><b>故障治理回歸：</b>故障 → 重試 → 對帳 → FINAL_ACCEPTED；MATCHED_EXACTLY_ONCE；AttemptHistory=append-only。</p>'+
      '<p><b>19 指標佐證與來源下鑽：</b>每一指標都可按「查看佐證與來源｜Evidence Matrix」再開 FrozenArtifact。Google Drive 連結只是選配，不是顧問調閱成功的必要條件。</p>'+
      '<p><b>靜態唯讀邊界：</b>不在執行期呼叫 Google Sheets／Drive API；本唯讀檢視器不會把 SAMPLE／CONTROL 宣稱為 REAL。</p>'+
      '</section>';
    return html.replace(ttqsR7Foot_(),block+ttqsR7Foot_());
  };
})();
