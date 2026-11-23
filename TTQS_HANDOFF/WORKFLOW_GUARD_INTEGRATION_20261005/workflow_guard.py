"""Small local checks before expensive model work. No quota reserves."""
import json,re,hashlib
HUMAN_FIELDS=('document_purpose','plain_language_intro','sections','tables','questionnaire_items','sop_steps','minutes','assessment_mechanics','sample_synthetic_content')
PROMPT_LEAKS=('拒絕相鄰分件','拒絕相鄰','界限隔離承諾','絕不抄襲或複製','CRITICAL EVALUATOR BODY CONTRACT','FROM_SOURCE_ONLY','deterministic checks','replacement-register','reviewer_prompt','validator','NAS','不捏造法定年數','不說協會真的已有設備')
def strings(value):
 if isinstance(value,str):yield value
 elif isinstance(value,list):
  for v in value:yield from strings(v)
 elif isinstance(value,dict):
  for v in value.values():yield from strings(v)
def body_preflight(payload):
 text='\n'.join(t for k in HUMAN_FIELDS for t in strings(payload.get(k)))
 leaks=[x for x in PROMPT_LEAKS if x in text]
 return {'allowed':not leaks,'prompt_leaks':leaks,'body_characters':len(text),'semantic_review_still_required':True}
def extract_final_review(raw,expected_sha,work_id):
 """Read only a final JSON object and reject earlier prompt/template objects."""
 value=str(raw or '').strip()
 marker=re.compile(r'\ntokens used\s*\n([\d,]+)\s*\n',re.I)
 markers=list(marker.finditer(value))
 if markers and value[markers[-1].end():].lstrip().startswith(('{','```')):
  value=value[markers[-1].end():].strip()
 trailer=re.search(r'\n+tokens used\s*\n[\d,]+\s*$',value,re.I)
 if trailer:value=value[:trailer.start()].strip()
 value=re.sub(r'^```(?:json)?\s*','',value.strip(),flags=re.I);value=re.sub(r'\s*```$','',value)
 try:
  obj=json.loads(value)
 except json.JSONDecodeError:
  decoder=json.JSONDecoder();obj=None
  # Search backward, accepting only an object that consumes the remainder.
  index=value.rfind('{')
  while index>=0:
   try:
    candidate,end=decoder.raw_decode(value[index:])
    if isinstance(candidate,dict) and not value[index+end:].strip():obj=candidate;break
   except json.JSONDecodeError:pass
   index=value.rfind('{',0,index)
  if obj is None:raise ValueError('FINAL_RESULT_NOT_JSON_OBJECT')
 if not isinstance(obj,dict):raise ValueError('FINAL_RESULT_NOT_OBJECT')
 if obj.get('verdict') not in ('PASS','FAIL','FAIL_REPAIRABLE','FAIL_SYSTEMIC'):raise ValueError('TEMPLATE_OR_INVALID_VERDICT')
 if obj.get('work_id')!=work_id or str(obj.get('reviewed_sha256','')).lower()!=expected_sha.lower():raise ValueError('FINAL_BINDING_MISMATCH')
 return obj
def review_fingerprint(candidate_sha,contract_sha,source_sha,facts):
 stable=json.dumps(facts,ensure_ascii=False,sort_keys=True,separators=(',',':'))
 return hashlib.sha256((candidate_sha+'|'+contract_sha+'|'+source_sha+'|'+stable).encode('utf-8')).hexdigest()
def packet_preflight(packet_bytes,source_ready,active_same_slot=False):
 reasons=[]
 if not source_ready:reasons.append('SOURCE_NOT_READY')
 if active_same_slot:reasons.append('MODEL_SLOT_BUSY')
 if packet_bytes>32768:reasons.append('COMPACT_REQUIRED_BEFORE_MODEL')
 return {'allowed':not reasons,'reasons':reasons,'percentage_reserve':False}
def provider_event(error):
 if not isinstance(error,dict):return {'classification':'UNKNOWN','automatic_retry_allowed':False}
 status=error.get('status') or error.get('status_code');kind=str(error.get('type','')).lower()
 body=(error.get('response') or {}).get('body','')
 try:inner=json.loads(body).get('error',{}) if isinstance(body,str) else body.get('error',{})
 except (ValueError,AttributeError):inner={}
 if status==429 or 'quota' in kind or inner.get('type')=='FreeUsageLimitError':
  return {'classification':'PROVIDER_USAGE_REJECTED','status_observed':status,'permanent_ban_proven':False,'automatic_retry_allowed':False,'resume_condition':'Official availability/reset evidence; no timer-driven probe or different-account bypass'}
 return {'classification':'OTHER_PROVIDER_ERROR','status_observed':status,'permanent_ban_proven':False,'automatic_retry_allowed':False}
