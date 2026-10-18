from pathlib import Path
import json, hashlib, shutil, subprocess, sys, re
import mpmath as mp

R=Path(__file__).resolve().parent
S=R/'supplement'; B=R.parent.parent
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((S/'manifest.json').read_text())
for r in manifest['entries']:
    p=S/r['name']; assert p.stat().st_size==r['bytes'] and digest(p)==r['sha256']
reused=[]
mapping={
 'verify_escape.py':B/'review-manuscript-2'/'output',
 'verification-1.json':B/'review-manuscript-2'/'output',
 'verify_extension_2.py':B/'review-manuscript-2'/'output',
 'extension-verification-2.json':B/'review-manuscript-2'/'output',
 'verify_general_noise_2.py':B/'review-general-noise-1'/'reviewed-inputs',
 'general-noise-verification-2.json':B/'review-general-noise-1'/'reviewed-inputs',
 'verify_mismatch_1.py':B/'review-adaptive-1'/'reviewed-inputs',
 'mismatch-verification-1.json':B/'review-adaptive-1'/'reviewed-inputs',
}
for name,base in mapping.items():
    matches=[p for p in base.rglob(name) if digest(p)==digest(S/name)]
    assert matches, (name,base)
    reused.append({'file':name,'sha256':digest(S/name),'identical_previous_file':str(matches[0]),'same_bytes':True})
rerun=[]
for script,out in [('verify_table_3.py','table-verification-3.json'),('verify_mismatch_1.py','mismatch-verification-1.json')]:
    target=R/'reproduction'/Path(script).stem; target.mkdir(exist_ok=True)
    shutil.copy2(S/script,target/script)
    p=subprocess.run([sys.executable,'-B',str(target/script)],capture_output=True,text=True,check=True)
    (target/'stdout.txt').write_text(p.stdout,encoding='utf-8')
    original=json.loads((S/out).read_text()); reproduced=json.loads((target/out).read_text())
    original.pop('created_at',None);reproduced.pop('created_at',None)
    assert original==reproduced, script
    rerun.append({'script':script,'equal_except_created_at':True,'output':str((target/out).relative_to(R))})

# Independent table derivation: 130 decimal digits, stable entropy form,
# entropy = log Z - mean(j) log r for the truncated geometric law.
mp.mp.dps=130
ln2=mp.log(2)
def thermal_entropy(x):return (mp.log(x)+(x+1)*mp.log1p(1/x))/ln2
def f(x):return x*mp.log(x)/ln2 if x else mp.mpf(0)
record=json.loads((S/'table-verification-3.json').read_text())
tex=(R/'reviewed-inputs'/'main.tex').read_text(encoding='utf-8')
pdftext=(R/'main-extracted.txt').read_text(encoding='utf-8')
rows=[]
for original in record['analytic_table']:
    n=original['N']; N=mp.mpf(n); lam=mp.mpf(7)/10
    K=int(mp.ceil(mp.sqrt(N))); m=N-K
    log_r=-mp.log1p(1/m); d=int(mp.ceil(2*(m+1)*mp.log1p(N)));t=mp.exp(d*log_r)
    mean=m-d*t/(1-t)
    log_partition=mp.log1p(-t)+mp.log(m+1)
    entropy=(log_partition-mean*log_r)/ln2
    a=thermal_entropy(N)-entropy
    delta=(1-lam)*min(mp.mpf(1),mp.mpf(10)/K)
    b=f(lam+delta)-f(lam)-f(delta)
    bounds=[lam*a+b,(2*lam-1)*a+b,2*lam*a+b,lam*a+b+delta*mp.log(5)/ln2]
    rounded=[f'{int(mp.ceil(x*10**6))//10**6}.{int(mp.ceil(x*10**6))%10**6:06d}' for x in bounds]
    errors=[abs(x-mp.mpf(y)) for x,y in zip(bounds,original['exact_bounds'])]
    assert K==original['K'] and d==original['d']
    assert rounded==original['upward_6']
    print('High precision residual', n, mp.nstr(max(errors),12))
    assert max(errors)<mp.mpf('1e-88'), (n,mp.nstr(max(errors),20))
    assert all(v in tex and v in pdftext for v in rounded)
    assert 0 <= K+mean < N
    assert t<=1/(N+1)**2
    rows.append({'N':n,'K':K,'d':d,'rounded_up_6':rounded,'max_difference_from_95_digit_author_record':mp.nstr(max(errors),8),'entropy_loss':mp.nstr(a,120),'bounds':[mp.nstr(x,120) for x in bounds],'strict_energy_slack':mp.nstr(N-K-mean,30),'tail_bound_verified':True})
out={'manifest_valid':True,'reused_identical_files':reused,'new_author_reproductions':rerun,'independent_table_precision_decimal':130,'table_rows':rows,'table_entries_verified':24,'all_entries_present_in_tex_and_pdf':True,'passed':True,'limits':'Finite algebra and reproducibility only. No numerical test establishes asymptotic coding, security, capacities or priority.'}
(R/'supplement-verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'passed':True,'reused_files':len(reused),'new_runs':rerun,'independent_precision':130,'table_entries':24},indent=2))
