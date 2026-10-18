from pathlib import Path
import hashlib,json,shutil,subprocess,sys,re
root=Path(__file__).parent; out=root/'output'; sup=out/'work/supplement'; run=out/'work/reproduction';run.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,x):(out/n).write_text(json.dumps(x,indent=2,ensure_ascii=False),encoding='utf-8')
manifest=json.loads((sup/'manifest.json').read_text())
assert all(sha(sup/e['name'])==e['sha256'] and (sup/e['name']).stat().st_size==e['bytes'] for e in manifest['entries'])
shutil.copy2(sup/'verify_minimax_6.py',run/'verify_minimax_6.py')
if not (run/'minimax-verification-6.json').exists():
    r=subprocess.run([sys.executable,'-B',str(run/'verify_minimax_6.py')],capture_output=True,text=True,check=True)
    (run/'stdout.txt').write_text(r.stdout,encoding='utf-8')
a=json.loads((sup/'minimax-verification-6.json').read_text());b=json.loads((run/'minimax-verification-6.json').read_text())
for x in (a,b):x.pop('time',None)
assert a==b
old=root.parent/'review-manuscript-4/output'
reuse=out/'reused-evidence';reuse.mkdir(exist_ok=True)
for name in ['supplement-verification.json','source-register.json','assessment.json','reference-check.json']:
    shutil.copy2(old/name,reuse/('manuscript-4-'+name))
prior=root.parent/'review-dossier-10/output'
for name in ['referee-checks.json','check_referee.py','source-register.json','audit-report.txt','verdict.json']:
    shutil.copy2(prior/name,reuse/('dossier-10-'+name))
src=root.parent/'adaptive-research-1/minimax-additional-sources-10'
sources=out/'sources';sources.mkdir(exist_ok=True)
for name in ['bsst-1999.pdf','bsst-1999.txt']:shutil.copy2(src/name,sources/name)
table=json.loads((old/'supplement-verification.json').read_text())['table']
tex=(root/'input/main.tex').read_text(encoding='utf-8');pdf=(out/'pdf-text.txt').read_text(encoding='utf-8')
rows=table['rows'] if 'rows' in table else table.get('checked_rows',[])
if not rows:
    for value in table.values():
        if isinstance(value,list) and value and isinstance(value[0],dict) and 'rounded_up_6' in value[0]:rows=value
assert len(rows)==6,table
for row in rows:
    assert all(s in tex and s in pdf for s in row['rounded_up_6'])
oldtex=(root.parent/'review-manuscript-4/input/main.tex').read_text(encoding='utf-8')
def tablepart(t):return t[t.index('\\begin{table}'):t.index('\\end{table}')+11]
assert tablepart(tex)==tablepart(oldtex)
assert '??' not in pdf
labels=re.findall(r'\\label\{([^}]+)\}',tex);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
bibs=re.findall(r'\\bibitem\{([^}]+)\}',tex)
cites=[s for x in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',tex) for s in x.split(',')]
assert set(cites)<=set(bibs)
comp=json.loads((out/'supplement-comparison.json').read_text())
result={'manifest_valid':True,'supplement_files':len(comp),'manifest_entries':len(manifest['entries']),'identical_prior_files':sum(x['identical_to_manuscript_4'] for x in comp),'new_script':'verify_minimax_6.py','new_script_sha256':sha(sup/'verify_minimax_6.py'),'new_reproduction_equal_except_time':True,'exact_cases':len(a['exact_cases']),'numerical_parameter_cases':len(a['numeric_cases']),'errors':a['errors'],'old_table_unchanged':True,'table_rows':6,'table_entries':24,'table_precision_reused':{'author':100,'independent':130},'all_roundings_in_exact_tex_and_pdf':True,'labels_and_citations_resolve':True,'table_evidence':table,'limits':'Algebra only, not operational coding/security proof. Identical prior files and independent dossier-10 checks reused with explicit scope.'}
dump('verification.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='table_evidence'},indent=2))
