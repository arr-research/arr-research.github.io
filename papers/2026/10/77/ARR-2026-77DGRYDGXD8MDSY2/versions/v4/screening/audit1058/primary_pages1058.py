"""Read public bibliographic pages in memory; persist metadata, not foreign text."""
from pathlib import Path
import requests,hashlib,json,datetime
P=Path(__file__).parent
targets=[
 ('author_makur','https://www.cs.purdue.edu/homes/amakur/publications.html','Author publication entry, title and IEEE link only.'),
 ('conference_abstract','https://easychair.org/smart-program/2024Allerton/2024-09-25.html','Lee-Makur author conference abstract; title, topic, closed-form claim; no formula or proof.'),
 ('conference_slides_index','https://easychair.org/smart-program/2024Allerton/slides.html','Two listed presentations; neither is the Lee-Makur paper.'),
 ('author_lee','https://dongmin.dev/','Author publication entry and DOI; no accessible paper formula located.')]
rows=[]
for tag,url,level in targets:
 rec={'tag':tag,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'read_level':level,'foreign_body_saved':False}
 try:
  r=requests.get(url,timeout=35);rec.update(status=r.status_code,final_url=r.url,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status()
 except Exception as ex:rec['error']=repr(ex)
 rows.append(rec)
(P/'PRIMARY_PAGES1058.json').write_text(json.dumps({'receipts':rows,'excluded_access':'IEEE returned418 in browser tool; not retried here or bypassed; no purchase or contact'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows,indent=2))
