from pathlib import Path
import csv, hashlib, json
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0066_R01')
body=root/'inputs'/'0066_BODY_R01_HUMAN_READY.md'
s=body.read_text(encoding='utf-8')
old='| 完成人數 | 10 | 10 | 上滿完整 6 小時者 |'
new='| 完成人數 | 10 | 10 | 合成設定：10 名到課者均達示例門檻（至少 5 小時）；非來源個別時數 |'
if s.count(old)!=1: raise SystemExit(f'expected one completion row, found {s.count(old)}')
s=s.replace(old,new)
old2='| 完成率 | 10 ÷ 12 | 83.3% | **與到課率定義不同**：完成以時數門檻（示例 5 小時）判定 |'
new2='| 完成率 | 10 ÷ 12 | 83.3% | **與到課率定義不同**：合成示例以至少 5 小時為完成門檻，10 名到課者均假設達門檻 |'
if s.count(old2)!=1: raise SystemExit(f'expected one completion-rate row, found {s.count(old2)}')
s=s.replace(old2,new2)
old3='| 完成人數 | 10（完成門檻示例 5 小時） |'
new3='| 完成人數 | 10（合成假設均達至少 5 小時門檻） |'
if s.count(old3)!=1: raise SystemExit(f'expected one data-card completion entry, found {s.count(old3)}')
s=s.replace(old3,new3)
body.write_text(s,encoding='utf-8',newline='')

rows=[
('SYN-001','案例識別與班名','SYN-0060-2026-A01；社區志工接待與資源轉介界線；2026-08-15','0060 R08 SAMPLE 案例標籤沿用；不是 REAL 班次','0060 R08 DOCX SHA-256 92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3','SAMPLE/SYNTHETIC','以實際班次識別、核定課名與日期取代','封面、資料卡、全篇案例連結','不代表協會實際開課'),
('SYN-002','報告建檔日與文件流程日期','報告 2026-09-22；回饋 2026-08-20；追蹤 2026-09-14；改善樣張 2026-09-20','本 R01 示範配置；日期均非原始紀錄','0066 R01 Writer 產出；原始回覆 JSON SHA 見 worker/session export','SAMPLE/SYNTHETIC','以原始簽收、彙整及核定日期取代','封面、導讀、流程、來源清冊','不得視為實際文件建立日或事件日'),
('SYN-003','NEE/NAN/PLN/LSN 日期與內容','NEE 07-20、NAN 07-31、PLN 08-05、LSN 08-10；志工接待、界線、澄清、轉介','為使示範呈現需求至教案鏈而合成','Blueprint 0066_UNIQUE_BLUEPRINT_R01.md；來源事項在 0066_BODY_R01_HUMAN_READY.md','SAMPLE/SYNTHETIC','替換為核准的需求分析、計畫、教案原件與版本','來源清冊、需求鏈','計畫與教案未核准'),
('SYN-004','示範課程目標及教學方法','四項目標：界線、最少必要澄清、轉介選項、隱私；示範及角色練習','本文件為需求及量規示範而新增','Blueprint 0066 R01; Body SHA-256 待 DOCX 固定','SAMPLE/SYNTHETIC','以核定課程目標、教案和實際方法取代','需求鏈、課表、量規','不得宣稱實際教學目標'),
('SYN-005','計畫與實際逐時課表','09:00–16:20；教學 360 分、休息20分、午餐60分；練習35分並以補充示範15分替代','用於示範計畫與實際差異的合成日誌','0066 R01 body; 0060 固定案例脈絡','SAMPLE/SYNTHETIC','以核定課表、簽到與授課日誌取代','逐時課表、一致性表','時間差異不得再重複計入總分鐘'),
('SYN-006','報名／到課／缺席總數','報名12、到課10、缺席2','沿用 0060 R08 合成案例固定值','0060 R08 DOCX SHA 92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3；source register SHA add1f2bcf77c77df6ba921e1dfa68494ac867a3e3368b795aa56c439aa824c4b','SAMPLE/SYNTHETIC','以去識別化名冊與簽到原件取代','資料卡、分母橋接','不含姓名'),
('SYN-007','結訓門檻與完成人數','門檻至少5小時；合成假設10名到課者均達門檻，完成人數10，10/12=83.3%','本 R01 新增的明確示範假設；非來源個別時數','0066 BODY R01 修訂後 exact hash 應以本套件 receipt 核定','SAMPLE/SYNTHETIC','以核定門檻、逐人可核驗時數及完成判定取代','資料卡、分母橋接','不得寫成所有人實到滿6小時'),
('SYN-008','評量有效性與結果總數','有效9、達標8、未達標1、無有效評量1；覆蓋9/10=90%；達標8/9=88.9%','沿用0060 SAMPLE彙總；無個人分數','0060 R08 DOCX SHA 92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3','SAMPLE/SYNTHETIC','以核定量規、原始評量、無效判準和彙總取代','分母表、量規結果','9+1=10；不得補造個人資料'),
('SYN-009','四項角色評量量規','4項各0–2分；總分0–8；總分至少6且第1項不得為0','0066 示範量規設計','Unique Blueprint R01／Writer body','SAMPLE/SYNTHETIC','以正式核定量規、版本日期取代','評量章','來源彙總不能證明正式量規相同'),
('SYN-010','問卷總量與整體正向','發出10、有效9、整體正向8；回收90%、正向88.9%','總量沿用0060 SAMPLE；原始逐題分布為合成','0060 R08 DOCX SHA 92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3','SAMPLE/SYNTHETIC','以問卷版本、去識別原始回覆及彙總取代','分母表、問卷表','不可冒稱原問卷'),
('SYN-011','逐題問卷人數分布','6題、各n=9；目標清楚8/9正向，示範有幫助8/9，界線易分辨8/9，練習足夠4/9，教材清楚7/9，整體滿意8/9','為展示可重算分布而新增的合成列聯值','0066 BODY R01','SAMPLE/SYNTHETIC','以原始問卷逐題計數取代','逐題問卷表','每列總數9；正向定義4或5分'),
('SYN-012','追蹤數字與日期','目標10、回覆8、未回2、自述使用6；回覆率80%、自述6/8=75%；追蹤日09-14','沿用0060 SAMPLE的聚合值；日期及逐題結果為合成','0060 R08 SHA 92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3','SAMPLE/SYNTHETIC','以追蹤名單、回覆證據、客觀成效記錄取代','追蹤表、改善閉環','6/8為自述，非客觀Outcome'),
('SYN-013','資源使用','模擬教室1、功能角色教學6小時/班務1日、投影設備1、材料備12發10回收2','本 R01 合成資源樣例','0066 BODY R01','SAMPLE/SYNTHETIC','以真實資源清冊、借用、簽領取代','資源表','不代表存在真實場地或設備'),
('SYN-014','財務預算及支出四項','預算8,000；材料2,500/2,750；交通3,000/2,500；場地1,500/1,000；其他1,000/1,400；總支出7,650','沿用0065 R02之合成金額，無帳冊、無憑證','0065 R02 DOCX SHA 43eac240f56e1dc3dcd2d26820ae2a309b3db98eff7ef26af129f73ec1bbb856；Blueprint e4638275843c5ee62edaae08b0efdf29d33e15abc5f5ade1fd6d399046010dda','SAMPLE/SYNTHETIC','以核定預算、明細帳、逐項憑證取代','財務表','他項未拆細；不得視為真支出'),
('SYN-015','財務衍生計算','差額-350；差異率-4.375%≈-4.4%；使用率95.625%≈95.6%；每登錄者637.50；每到課者765','由合成基礎金額計算','0066 BODY R01；計算以Python重算並留QA receipt','SAMPLE/SYNTHETIC','替換真實基礎數據後重新計算','財務核算、一致性表','計算不等於憑證證明'),
('SYN-016','改善建議六項','練習不足15分；評量覆蓋缺1；問卷缺1；追蹤未回2；其他費用差異400且無明細；缺席原因未知','由合成課表、彙總和財務差異推導的建議；均未核定／未執行','0066 BODY R01','SAMPLE/SYNTHETIC','以有來源的檢討決議、負責單位及後續驗證取代','改善閉環','責任均為功能角色，不是真人指派'),
('SYN-017','改善期限與驗證指標','10-02、10-09、10-16等示範期限；覆蓋率、回收率與明細指標','本 R01 建議性示範，不是已排定行動','0066 BODY R01','SAMPLE/SYNTHETIC','使用經核定期限、責任分工與追蹤紀錄取代','改善表','不得對外宣稱已核定'),
('SYN-018','功能角色','班務、資料彙整、課程規劃、經費核銷功能','描述建議職能分工，不指向真人或正式組織','0066 BODY R01','SAMPLE/SYNTHETIC','填入經確認的實際職務並保留授權依據','程序、改善表','沒有姓名或簽名'),
('SYN-019','資料來源日期清冊','NEE/NAN/PLN/LSN、資源、簽到、日誌、評量、回饋、追蹤、修正、改善日期','為展示文件鏈而合成的來源日期','0066 BODY R01','SAMPLE/SYNTHETIC','以實際文件版次及可查建立時間取代','來源清冊','不得作為原始文件存在的證明'),
('SYN-020','0065意見引用','VO-S-01「希望先看完整示範，再分組練習轉介說明」','沿用0065中明確標為合成、非原問卷引文的示例','0065 R02 DOCX SHA 43eac240f56e1dc3dcd2d26820ae2a309b3db98eff7ef26af129f73ec1bbb856','SAMPLE/SYNTHETIC','若引用真實建議，連結匿名化原始回饋及同意基礎','文類辨析、跨文件關聯','不能冒充0060原始問卷'),
('SYN-021','HOLD/退件清單與結論','十項HOLD/退件條件；示範結案完成、真實證據HOLD、改善未執行','本 R01 操作性風險控制示例','0066 BODY R01','SAMPLE/SYNTHETIC','依正式內控、證據完整度及實際核決更新','HOLD/退件、導讀','不構成正式協會結案判定'),
('SYN-022','空白工作表及附件索引','A-1至A-11附件標示SAMPLE/空白，11個採集欄位未填','模板欄位為文件功能示範；不是附件原件','0066 BODY R01','SAMPLE TEMPLATE','以真正的來源附件與核准表單逐件替換','附件索引、附錄','留白不得解讀為無問題或已完成'),
]
register=root/'inputs'/'0066_SYNTHETIC_REPLACEMENT_REGISTER_R01.csv'
with register.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f); w.writerow(['register_id','scope','values_or_claims_in_document','basis_and_provenance','source_identity_or_hash','evidence_class','required_real_replacement','document_locations','limits_and_controls']); w.writerows(rows)

sourcehash=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest={
 'artifact':'TTQS ONE DOCX 0066 R01 source package',
 'doc_id':'0066','requirement_id':'I15-E02','official_checkbox_serial':'072',
 'case_id':'SYN-0060-2026-A01','status':'CANDIDATE_SOURCE_PREPARATION',
 'writer_session_id':'ses_eb067cd86ffeonmRdzWrBy0xs1',
 'writer_model':'opencode/deepseek-v4.1-flash-free',
 'writer_outcome':'succeeded','writer_cost_usd':0,
 'writer_tokens':{'input':5393,'output':7656,'reasoning':5052},
 'body_path':'inputs/0066_BODY_R01_HUMAN_READY.md',
 'body_sha256':sourcehash(body),
 'register_path':'inputs/0066_SYNTHETIC_REPLACEMENT_REGISTER_R01.csv',
 'register_sha256':sourcehash(register),
 'contract_commit':'f55522887a302c1dcb9cb7d6a1b076b578c7db24',
 'completion_rule_correction':'All 10 attendance/completion values are explicitly a synthetic assumption under the 5-hour threshold; no claim that individuals attended all 6 teaching hours.',
 'formal_acceptance':'NOT ESTABLISHED'
}
(root/'evidence'/'source_manifest_R01.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'body_sha256':manifest['body_sha256'],'register_sha256':manifest['register_sha256'],'register_rows':len(rows),'body_chars':len(s)},ensure_ascii=False))
