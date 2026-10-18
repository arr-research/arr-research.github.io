"""Exact, solver-free replay of the one-calibration-query witness.
Run with Python 3.10+ from any directory. Q.json and R.json must be adjacent.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import hashlib, json
HERE=Path(__file__).resolve().parent
N=32

def require(ok,msg):
    if not ok: raise ValueError(msg)

def load(name):
    a=[[F(x) for x in row] for row in json.loads((HERE/name).read_text())]
    require(len(a)==N and all(len(row)==N for row in a),'shape')
    require(all(a[i][j]==a[j][i] for i in range(N) for j in range(N)),'symmetry')
    return a

def psd(a):
    a=[row[:] for row in a]; pivots=[]
    for k in range(len(a)):
        p=a[k][k]; require(p>=0,'negative pivot');pivots.append(p)
        if not p:
            require(all(a[k][j]==0 for j in range(k+1,len(a))),'zero pivot with nonzero row')
            continue
        for i in range(k+1,len(a)):
            for j in range(i,len(a)):
                a[i][j]-=a[i][k]*a[k][j]/p
                a[j][i]=a[i][j]
    return {'rank':sum(p>0 for p in pivots),'pivots':list(map(str,pivots))}

def causal(q):
    for k in range(5,0,-1):
        require(all(q[i][j]==0 for i in range(2**k) for j in range(2**k) if (i&1)!=(j&1)),'last-symbol orthogonality')
        q=[[q[2*i][2*j]+q[2*i+1][2*j+1] for j in range(2**(k-1))] for i in range(2**(k-1))]
    require(q==[[F(1)]],'normalization')

def null(r):
    require(all(sum(r[i][j] for j in range(N) if j.bit_count()==w)==0 for i in range(N) for w in range(6)),'null annihilation')

def must_fail(fn):
    try: fn()
    except ValueError: return True
    raise ValueError('negative control incorrectly accepted')

def main():
    q=load('Q.json');r=load('R.json');causal(q);null(r)
    checks={label:psd(a) for label,a in [('Q',q),('R',r),('Q-R',[[q[i][j]-r[i][j] for j in range(N)] for i in range(N)])]}
    require([checks[k]['rank'] for k in ['Q','R','Q-R']]==[32,26,32],'rank')
    eta=F(7,10)
    # Exact Fourier moments of |0>+exp(i phi)|1>, measured covariantly.
    mu=lambda k: F(1) if k==0 else F(1,2) if abs(k)==1 else F(0)
    # Seven equally spaced phases integrate every Fourier mode through degree 6.
    require(all((k%7==0)==(k==0) for k in range(-6,7)),'seven-point quadrature')
    for k in range(-5,6):
        require(sum(weight for frequency,weight in [(k,F(1)),(k-1,F(1,2)),(k+1,F(1,2))] if frequency%7==0)==mu(k),'finite POVM Fourier moment')
    s=sum(r[i][j]*eta**((i^j).bit_count())*mu(i.bit_count()-j.bit_count()) for i in range(N) for j in range(N))
    s0=sum(r[i][j]*eta**((i^j).bit_count()) for i in range(N) for j in range(N) if i.bit_count()==j.bit_count())
    per_type=[sum(F(comb(w,j)*comb(5-w,j))*eta**(2*j) for j in range(min(w,5-w)+1))/comb(5,w) for w in range(6)]
    parallel=min(per_type);gap=s-(1-parallel)
    require(s==F(8547317228981067,16000000000000000),'rejection value')
    require(parallel==F(46603,100000),'parallel value')
    require(gap==F(3797228981067,16000000000000000)>0,'positive gap')
    require(s0<=1-parallel,'uncalibrated sanity check')
    parallel6=sum(F(comb(3,j)**2)*eta**(2*j) for j in range(4))/20
    require(parallel6==F(7688549,20000000)<1-s,'fungible-cost countercomparison')
    # Alternative exact expansion over all 32 independent I/Z noise histories.
    p=(1+eta)/2;qprob=1-p
    mixed=F(0)
    for z in range(N):
        prob=p**(5-z.bit_count())*qprob**z.bit_count()
        branch=sum(r[i][j]*(-1)**((z&(i^j)).bit_count())*mu(i.bit_count()-j.bit_count()) for i in range(N) for j in range(N))
        require(0<=branch<=1,'trajectory probability')
        mixed+=prob*branch
    require(mixed==s,'noise history replay')
    badq=[row[:] for row in q];badq[0][0]+=1
    badr=[row[:] for row in r];badr[0][0]+=1
    controls=[must_fail(lambda:causal(badq)),must_fail(lambda:null(badr)),must_fail(lambda:psd([[F(-1)]])),must_fail(lambda:psd([[F(0),F(1)],[F(1),F(0)]]))]
    report={'status':'all exact checks passed','arithmetic':'standard-library Fraction; no numerical solver',
        'sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ['Q.json','R.json','verify.py']},
        'psd':checks,'causal_levels_checked':5,'null_types_checked':6,'parallel_by_weight':list(map(str,per_type)),
        'rejection':str(s),'failure':str(1-s),'parallel_failure':str(parallel),'strict_gap':str(gap),'strict_gap_decimal':float(gap),
        'uncalibrated_rejection_same_witness':str(s0),'six_signal_parallel_failure':str(parallel6),
        'noise_histories_replayed':32,'finite_phase_POVM_outcomes':7,'negative_controls_passed':len(controls),
        'not_claimed':['causal optimality','global minimum signal query count','experimental realization','novelty or peer review','AIRR score']}
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(report['status']);print('Exact advantage:',gap);print('Failure:',float(1-s))

if __name__=='__main__':main()
