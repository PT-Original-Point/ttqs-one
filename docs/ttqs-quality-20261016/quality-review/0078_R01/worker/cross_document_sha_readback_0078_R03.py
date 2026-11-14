from pathlib import Path
import hashlib,json,datetime
base=Path(__file__).resolve().parents[1].parent
rows=[
('0073','R08','0073_R01/candidate/0073_R08.docx','a454cf0691a53173ae7838c9cd84522cf419d1d940cb63a7ddc168b497bc9b13'),
('0074','R01','0074_R01/candidate/0074_R01.docx','d5a15e087d7323dd0d9c44191ae26fc0cca6bef052de8af85daa94e621e1f190'),
('0075','R02','0075_R01/candidate/0075_R02.docx','ca81a4791febbe6f303a755f441705e41fb465c869098e17cc3c5c222a2c6961'),
('0076','R01','0076_R01/candidate/0076_R01.docx','885fe403b46144639034a3f6b26c2b74916c22c7b5a5a971628136f376a115f3'),
('0077','R01','0077_R01/candidate/0077_R01.docx','cc545510cf503e9ecb16238c2b8dcdf6b15cbc43a28360b3b76f97513017edf7')]
items=[]
for did,rev,rel,expected in rows:
 p=base/rel; actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
 items.append({'document_id':did,'revision':rev,'path':rel,'expected_sha256':expected,'actual_sha256':actual,'matches':actual==expected})
r={'schema':'TTQS_ONE_0078_CROSS_DOCUMENT_SHA_READBACK_R03.v1','source_packet_sha256':'8f648688fef2292dfb4c72db70446e4d169425b827508767c37b9f00d0528ae0','read_at_local':datetime.datetime.now().astimezone().isoformat(),'documents':items,'result':'PASS' if all(x['matches'] for x in items) else 'FAIL','status_note':'Hashes confirm source-packet cross-references only; they do not confer semantic or formal acceptance.'}
out=Path(__file__).resolve().parents[1]/'evidence'/'cross_document_sha_readback_R03.json';out.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,ensure_ascii=False,indent=2))
