# SOURCE PACKET

PROJECT_ID=TTQS_ONE
DOC_ID=0017
REQUIREMENT_ID=I02-E05
WORK_ID=TTQS-0017-I02-E05-WEBSITE-WRITER-R01-20261116
CANDIDATE_STATE=CANDIDATE_SAMPLE_SYNTHETIC_NOT_APPROVED_NOT_PUBLIC
OFFICIAL_REQUIREMENT_TEXT=客戶提出的課程需求的相關表單 （文件），而揭露的呈現方式， 可以為EDM、海報、網站網頁等方式加以呈現。
OFFICIAL_EVIDENCE_TABLE_PAGE=1
OFFICIAL_PDF_SHA256=805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709
SOURCE_STATUS=承接既有 SOURCE_PACKET_0014_R01 的 PDF_TEXT_EXACT_PAGE_MATCH；本回合未重新開啟原始 PDF，不宣稱本回合重新核讀。
SOURCE_PACKET_0014_R01_SHA256=30ade83ab55d9ed185dae519252e114ebfb33c8ef276c8005cf77cb355e82b91
BLUEPRINT_CONTRACT_PATH=docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md
BLUEPRINT_CONTRACT_SHA256=7732c40f25d0803f18836725d1634ebe72a156925444f3ea9915b6168cc1a70a
BLUEPRINT_LOCATOR=第 33 行方框 012：客戶需求表單，包含 EDM／海報／網站文案
CROSSWALK_PATH=quality-review/0004_I01-E02_SOURCE_PREP_R03_20261030/source/crosswalk_129_to_142.csv
CROSSWALK_SHA256=4ab68ebce88ca0f2874aaaf869adb1ccc22470c2462114fb1e776262d641ed36
CROSSWALK_ROW=I02-E05,4,3,0014 | 0015 | 0016 | 0017,客戶課程需求申請表 | 客戶需求評估與回覆表 | 課程EDM完整文案 | 網站課程揭露頁完整內容
SHARED_REGISTER_PATH=quality-review/0016_I02-E05_R07_CANDIDATE_20261107/source/SYNTHETIC_REPLACEMENT_REGISTER_0016_R07.csv
SHARED_REGISTER_SHA256=8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a
SOURCE_RULE=官方要求只支持客戶課程需求相關文件可用 EDM、海報或網站頁呈現；本件只負責 0017 完整網站課程揭露頁，不推論任何實際課程、核准、招生、費用或成效。

# UNIQUE BLUEPRINT

DOC_ID=0017
REQUIREMENT_ID=I02-E05
TITLE=網站課程揭露頁完整內容
GENRE=完整網站課程資訊頁文案與頁面內容規格
PURPOSE=以網站頁結構揭露課程目的、對象、目標、內容、日期、時數、方式、費用、名額、報名狀態與聯絡資訊；提供完整 SAMPLE/SYNTHETIC 示範，不代表對外發布。
SCOPE=獨立網頁課程頁；不取代 0014 申請表、0015 需求評估與回覆、0016 EDM、0013 年度課程公開表或 0018 PDDRO 圖。
OFFICIAL_SOURCE=I02-E05 精確原文、佐證表第 1 頁；方框 012；142 crosswalk 明列 0017「網站課程揭露頁完整內容」。
REQUIRED=頁首醒目 SAMPLE/SYNTHETIC 與未公開狀態；頁面標題及摘要；課程目的、受眾、先備條件、可觀察學習目標；完整內容與議程；日期、總時數、淨教學時數、授課方式及場地；名額、費用、截止；合成講師代碼；無效且停用的報名 CTA；取消／退款示例及無交易聲明；個資與無障礙說明；FAQ；正式替換清單與發布 HOLD。
NEGATIVE_NEIGHBORS=0014 申請表；0015 評估回覆；0016 EDM；0013 年度課程公開資訊；0018 PDDRO。不得複製它們的正文；只可使用 0016 register 已登錄且屬同一示例課程的共用事實。
TRUTH_BOUNDARY=所有課程日期、費用、名額、師資、時程、聯絡及政策均為合成示例；不得暗示協會已開課、核准、招生、收款、發布或取得成果。example.invalid 網址／信箱不可用；報名關閉。
ACCEPTANCE=來源與文類對應正確；所有合成事實綁定本件 register fact_id；時數可重算；無空白表單及無根據聲稱；正文至少 10.5pt、表格至少 9.5pt；Word 原生渲染逐頁視覺檢查；獨立語意審查綁定同候選 SHA；GitHub 同來源 raw-byte readback。

# SYNTHETIC REGISTER

fact_id,value,classification,source_binding,document_location,real_replacement_source,responsible_role
S-004,"非營利專案紀錄入門：從需求到證據的練習",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","頁面標題、FAQ","核准課名與課綱","課程負責人"
S-005,"課程目標、內容主張、合成案例、SAMPLE-WORKSHEET-01 教材代碼",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","介紹、目標、教材","核准課綱與教材版本","課程負責人"
S-006,"2027-03-18 09:30–12:30；總時段180分含休息；淨教學170分",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","日期、時數、議程","核准排程與時數核算","課程負責人"
S-007,"七段議程含休息；精確段落見 S17-008",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","議程","核准教案與排程","課程負責人"
S-008,"線上示例；ROOM-SAMPLE-01",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","授課方式","真實平台與會議連結","課程承辦人"
S-009,"講師代碼 T-SAMPLE-01，不指涉真人",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","講師資訊","本人確認、同意及資格證據","課程承辦人"
S-010,"示例受眾描述；本例不設定先備條件",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","受眾及先備","核准招生條件","課程負責人"
S-011,"示例名額18人",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","名額","核准上限與容量","招生承辦人"
S-012,"示例費用新臺幣1,200元；不收款",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","費用","核准價格及交易資訊","財務／招生"
S-013,"示例截止2027-03-12 17:00",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","截止","核准生效期限","招生承辦人"
S-015,"取消／退款只屬示例，本例不收款、不成立交易；詳細本頁值見 S17-010",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","取消／退款","正式適用條款與核准","招生／財務"
S-017,"course-info@example.invalid",shared_sample_course_fact,"0016 R07 register 8f7cf823b535046109b3ed470d9cceb8bc6c1b109f3c2da406547f2eb17f2f7a","聯絡","可回覆的真實管道","課程承辦人"
S17-001,"SAMPLE-0017-WEB-R01；CANDIDATE_SAMPLE_SYNTHETIC_NOT_APPROVED_NOT_PUBLIC","synthetic page identity/status","本次新增","頁首與頁尾狀態","正式頁面識別與發布讀回","網站維護"
S17-002,"https://example.invalid/courses/sample-0017","invalid reserved-domain sample URL","本次新增","頁面網址示例","核准正式網址","網站維護"
S17-003,"https://example.invalid/register/sample-0017；CTA 停用","invalid reserved-domain registration URL","本次新增","報名按鈕與狀態","有效報名頁與系統測試","招生承辦人"
S17-004,"非營利／社福組織中負責課程活動或專案紀錄的行政與方案承辦角色；設計假設，非訪談結果","synthetic audience assumption","本次新增","適合對象","真實需求調查或核准招生描述","課程負責人"
S17-005,"完成一份 SAMPLE 專案紀錄，含需求來源、行動、責任、日期、成果定位及替換界線；非真實學習成效","synthetic intended outcome","本次新增","可帶走成果","核准課綱與評量證據","課程負責人"
S17-006,"區分來源事實與推論；把需求轉為可觀察目標；連結活動、紀錄與佐證；檢查缺漏及待補原件","synthetic learning objectives","本次新增","學習目標","核准課綱與評量規準","課程負責人"
S17-007,"課程頁內容包括目的、對象、目標、內容、時程、方式、名額、費用、報名、聯絡、取消、個資及無障礙","synthetic web-page structure","本次新增","整體頁面","正式網站資訊架構","網站維護"
S17-008,"09:30–09:50 來源與目的20分；09:50–10:15 事實／推論25分；10:15–10:40 需求定位25分；10:40–10:50休息10分；10:50–11:20目標與活動30分；11:20–11:55範例紀錄35分；11:55–12:30檢核修正35分；淨170分、總180分","synthetic agenda schedule","新增；與S-006共用時段","議程表","核准教案與排程重算","課程負責人"
S17-009,"頁面及搜尋標題／摘要；不得聲稱實際成效、政府推薦、核准或保證","synthetic web copy metadata","本次新增","搜尋摘要與頁面標題","正式品牌與發布文案核准","網站維護"
S17-010,"取消示例：2027-03-12 17:00前提出全額退回；截止後本合成案例不退款；處理時間示例7個工作日；不適用真實交易，本例不收款","synthetic cancellation example","本次新增","取消／退款","實際適用條款與法務／權責核定","招生／財務"
S17-011,"本頁不收集個資，報名停用；正式頁須連結經核定的蒐集目的、欄位、利用期間／對象／方式與權利窗口","synthetic privacy boundary","本次新增","個資說明","實際隱私告知與權責核定","個資權責"
S17-012,"字幕或其他參與需求可示例寄至 course-info@example.invalid；此保留網域無法收信，正式頁須換可回覆窗口並驗證支援","synthetic accessibility contact","以S-017為共用聯絡值","無障礙聯絡","有效窗口與已驗證服務能力","課程承辦人"
S17-013,"示例頁不接收報名、不收款、不發送確認信，未證明課程開辦","synthetic operation status","本次新增","CTA、費用旁及頁尾","報名、金流及開課狀態原始收據","招生／網站"
S17-014,"純文字示例頁；以單一主標題、逐級標題、明確連結名稱與具名表格呈現，不含圖片","synthetic accessible page representation","本次新增","頁面結構附註","實際 HTML 的鍵盤、螢幕閱讀器、對比測試","網站維護"
S17-015,"維護角色代碼 WEB-SAMPLE-OWNER，不指涉實際員工","synthetic role code","本次新增","文件追溯附錄","正式核定的內容負責人與授權","網站維護"

# WORKER REQUEST

work_id=TTQS-0017-I02-E05-WEBSITE-WRITER-R01-20261116
doc_id=0017
requirement_id=I02-E05
role=TEXT_ONLY_WRITER
requested_route=opencode/beam-free
source_packet_sha256=d0f7541faa6534eb8a43355c08a658159c359ad660fec52fab113d5f9d42b83e
unique_blueprint_sha256=41b46d8aa79a608d43cb6b64a8b898ac1e4b4e4f25d66f366b19351551345dab
synthetic_register_sha256=92e37e270ac6bac83d444901d2634391c74fc0c7c4c5ff2f4488137bdc0bbe3d

Return ONLY a complete Traditional Chinese Markdown document body for the full website course disclosure page in doc_id 0017, titled 網站課程揭露頁完整內容. Produce a useful, readable, complete SAMPLE/SYNTHETIC page, not an outline, workflow report, form, EDM, or actual HTML publication. No tools or file writes.

Official source page 1: 客戶提出的課程需求的相關表單 （文件），而揭露的呈現方式， 可以為EDM、海報、網站網頁等方式加以呈現。
The 142-to-129 crosswalk maps I02-E05 to 0014 intake form, 0015 needs assessment/reply, 0016 complete EDM copy, 0017 complete website course disclosure page. This task owns only the unique 0017 web page. Do not copy peer DOCX prose. Use the supplied 0017 blueprint and register.

Map every visible synthetic fact to exact supplied register IDs in an internal trace appendix. Shared course facts use their exact S-004 through S-017 IDs; new web facts use S17-001 through S17-015. Preserve values exactly: course title; 2027-03-18, 09:30–12:30; gross 180 minutes including 10-minute break, net instruction 170 minutes; online example; 18 seats; NT$1,200; registration deadline 2027-03-12 17:00; instructor code T-SAMPLE-01; contact course-info@example.invalid. Do not reuse the 0016 CTA URL. Use only the 0017 invalid example URLs from S17-002 and S17-003. Include exact agenda from S17-008 and reconcile arithmetic (20+25+25+30+35+35=170 teaching minutes, plus 10-minute break=180 total).
Prominently state SAMPLE/SYNTHETIC, CANDIDATE, not approved, not public, registration closed; no actual course/approval/enrollment/payment/page publication is evidenced. The CTA must be clearly inactive. No contract/payment is established. No real privacy service, accessibility service, staff identity, credentials, achievements, or association policy may be implied.
Include course introduction, audience/prerequisites, intended learning outcomes, content and agenda, time/mode/venue, seats/fee/deadline, fictional instructor, inactive CTA, synthetic cancellation conditions and explicit no-transaction disclaimer, privacy boundary, accessibility note, FAQ, real-replacement evidence checklist and stop-publication HOLD. Do not add unregistered synthetic dates/numbers/amounts/facts. Keep public-facing copy separate from internal appendix; plain readable headings; self-contained for direct DOCX conversion.