from pathlib import Path
import difflib,hashlib,json
base=Path(r'C:\Trabajo\airr\2026-10-17_revision-seis-estados'); old=base/'input'; new=base/'revision-2/input'; out=base/'revision-2/output/evidence'
diff=''.join(difflib.unified_diff((old/'main.tex').read_text(encoding='utf-8').splitlines(keepends=True),(new/'main.tex').read_text(encoding='utf-8').splitlines(keepends=True),fromfile='original-reviewed/main.tex',tofile='revised/main.tex'))
provided=(new/'source-diff.patch').read_text(encoding='utf-8')
assert diff.strip()==provided.strip()
checks=[]
for p in sorted((old/'supplement').rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(old)
 q=new/rel
 assert q.is_file() and p.read_bytes()==q.read_bytes(),str(rel)
 checks.append({'path':str(rel).replace('\\','/'),'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
for fn in ['supplement.zip','standard-rubric.txt']:
 assert (old/fn).read_bytes()==(new/fn).read_bytes()
 checks.append({'path':fn,'sha256':hashlib.sha256((new/fn).read_bytes()).hexdigest()})
oldinv=json.loads((base/'output/hash-inventory.json').read_text(encoding='utf-8'))
for row in oldinv['files']:
 p=base/row['path']
 assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],str(p)
refs=[]
for rel in ['manuscript-review.txt','assessment.json','independent_checks.py','novelty_cycle6_check.py','evidence/independent-results.json','evidence/novelty-cycle6-check.json','evidence/supplement-reproduction/supplement-reproduction.log','hash-inventory.json']:
 p=base/'output'/rel
 refs.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
record={'status':'PASS','computed_source_diff_matches_provided':True,'unchanged_supplement_and_rubric':checks,'prior_review_inventory_all_files_unchanged':True,'prior_evidence_references':refs,'new_root_README_present':(new/'README.txt').is_file(),'note':'The new packet has no root README.txt; scope is supplied by the follow-up task. Prior packet instructions remain available.'}
(out/'revision-integrity-and-evidence-links.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
(out/'computed-source-diff.patch').write_text(diff,encoding='utf-8')
print(json.dumps({'status':'PASS','unchanged_files':len(checks),'prior_artifacts_linked':len(refs),'prior_inventory_files_rechecked':len(oldinv['files']),'new_root_README_present':False},indent=2))
