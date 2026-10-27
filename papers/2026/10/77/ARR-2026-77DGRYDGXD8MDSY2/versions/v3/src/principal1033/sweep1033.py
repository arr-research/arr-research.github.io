from pathlib import Path
import concurrent.futures,datetime,hashlib,json,urllib.request
C=Path(__file__).parent;B=Path(r'D:\Proyectos\airr-investigacion');old=json.loads((B/'2026-10-27_knowledge1028/READINGS1028.json').read_text())
previous={x['url']:x for x in old['sources']}
urls=[('https://api.github.com/repos/openai/math/commits?per_page=1','latest commit metadata only'),('https://api.github.com/repos/google-deepmind/formal-conjectures/commits?per_page=1','latest commit metadata only; formal statement inventory is not proof audit'),('https://www.anthropic.com/research','research index only'),('https://arxiv.org/html/2011.05949v4','HTTP identity refreshed; selected reading from1028 reused, no new whole-paper proof audit'),('https://airr.science/','public catalogue index only'),('https://www.ai.vixra.org/author/lluis_eriksson','author index only, not every proof read'),('https://api.github.com/users/lluiseriksson/repos?type=owner&sort=updated&per_page=100','first100public repository metadata only, not exhaustive content sweep')]
def one(item):
 url,depth=item;out=dict(url=url,read_depth=depth,retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'AIRR-directed-primary-research/1.0'}),timeout=45) as r:b=r.read();out.update(status=r.status,etag=r.headers.get('ETag'),last_modified=r.headers.get('Last-Modified'))
  out.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  if '/commits?' in url:
   out['latest_observed_commit']=json.loads(b)[0]['sha'];out['previous_commit']=previous.get(url,{}).get('latest_observed_commit');out['commit_changed']=out['latest_observed_commit']!=out['previous_commit']
  if '/users/' in url:out['public_repositories']=[dict(name=x['name'],pushed_at=x['pushed_at'],default_branch=x['default_branch']) for x in json.loads(b)]
 except Exception as ex:out['error']=str(ex)
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(one,urls))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Current directed primary-source sweep; inventories, read statements and audited own proofs remain distinct. No exhaustive or worldwidepriority claim, no foreign fulltext copied.',sources=rows,search_queries=['site:arxiv.org depolarizing chi-square ancilla','site:arxiv.org depolarizing Petz order','site:arxiv.org complete contraction coefficients unital'],search_result='Historical1028 narrow queries returned none. Current1033 additional queries found primary leads1008.1557 and2204.09963, abstracts read separately; no exhaustive coverage claim.',comparison='Selected Weyl passages concern channel order/degradability and ordinary/fixed-reference optimizations. They provide prior CP range and comparison tools; these passages alone neither establish nor exclude worldwide coverage of the constrainedcompleteSLDclassification.',new_grade=None)
(C/'READINGS1033.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(endpoints=len(rows),errors=[x['url'] for x in rows if 'error' in x],commits=[dict(url=x['url'],changed=x['commit_changed']) for x in rows if 'commit_changed' in x])))
