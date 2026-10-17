from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from itertools import product, combinations
import hashlib, json, math, sys
import numpy as np

ROOT=Path(__file__).resolve().parent
SOURCE=Path(r'D:\Proyectos\airr-investigacion\2026-10-17_saturacion-indecidible\averaged-gap-candidate.txt')
data=SOURCE.read_bytes()
assert hashlib.sha256(data).hexdigest()=='d462ac3b6c31860c839874f1a8d8631a069277f6e3afa6f8f9d656562f6d275a'
(ROOT/'candidate-reviewed.txt').write_bytes(data)
(ROOT/'candidate-numbered.txt').write_text(''.join(f'{i}: {x}\n' for i,x in enumerate(data.decode('utf-8-sig').splitlines(),1)),encoding='utf-8')
rng=np.random.default_rng(202610171400)
def n2(a): return float(np.vdot(a,a).real/a.shape[0])
def unitary(m):
    q,r=np.linalg.qr(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)))
    return q@np.diag(np.diag(r)/np.abs(np.diag(r)))
def invol(m):
    q=unitary(m)
    return (q*rng.choice([-1,1],size=m))@q.conj().T
def polar(a):
    u,_,v=np.linalg.svd(a)
    return u@v
def sign(a):
    v,q=np.linalg.eigh((a+a.conj().T)/2)
    return (q*np.where(v>=0,1.,-1.))@q.conj().T
def wordval(word,v):
    ans=np.eye(next(iter(v.values())).shape[0],dtype=complex)
    for x in word: ans=ans@v[x]
    return ans
def words_from_rows(rows):
    result=[]
    for inds,sgn in rows:
        assert 1<=len(inds)<=3 and len(set(inds))==len(inds)
        row=[([x,x],1) for x in inds]+[(list(inds),sgn)]
        row += [([x,y,x,y],1) for x,y in combinations(inds,2)]
        row += [([],1)]*(7-len(row))
        assert len(row)==7
        result+=row
    return result
def compile_words(gens,words,mode):
    labels=list(gens)+['z','t']; gates=[]; assigned=[]; prefixes=[]
    for wi,(word,sgn) in enumerate(words):
        chain=list(word)+['t','t']; ids=[]; current=chain[0]
        for j,nxt in enumerate(chain[1:],1):
            final=j==len(chain)-1
            out='z' if final else f'p{wi}_{j}'
            if not final: labels.append(out); prefixes.append((out,list(chain[:j+1])))
            ids.append(len(gates)); gates.append((current,nxt,out,sgn if final else 1))
            current=out
        ids.append(len(gates)); gates.append(('t','t','z',1))
        assigned.append(ids)
    weights=Counter({l:1 for l in labels})
    for u,v,w,sgn in gates:
        weights[u]+=9;weights[v]+=9;weights[w]+=16;weights['z']+=16
        # Exact local coefficient checks, independently assembled.
        mats={l:[[F(0),F(0)],[F(0),F(0)]] for l in {u,v,w,'z'}}
        mats[u][0][0]+=F(3,5);mats[v][1][1]-=F(3,5)
        mats[w][0][1]+=sgn*F(4,5);mats['z'][1][0]+=F(4,5)
        for transpose in (False,True):
            out=[[sum(sum((a[k][i]*a[k][j] if transpose else a[i][k]*a[j][k]) for k in range(2)) for a in mats.values()) for j in range(2)] for i in range(2)]
            assert out==[[1,0],[0,1]]
        assert all(sum(mats[l][i][j]*mats[h][i][j] for i in range(2) for j in range(2))==0 for l,h in combinations(mats,2))
    initial_sum=sum(weights.values())
    assert initial_sum==len(labels)+50*len(gates)
    if mode=='heavy':
        M=max(weights.values()); final={l:2*M for l in labels}; D=2*len(labels)*M
        singles={l:1+2*M-weights[l] for l in labels}
        assert min(singles.values())>=M+1
        scaling=None
    else:
        w={l:math.isqrt(2*q)+(math.isqrt(2*q)**2<2*q) for l,q in weights.items()}
        assert all(2*weights[l]<=w[l]**2<=6*weights[l] for l in labels)
        final={l:w[l]**2 for l in labels}; singles={l:1+final[l]-weights[l] for l in labels}
        D0=sum(final.values()); t=math.isqrt(D0)+(math.isqrt(D0)**2<D0); D=t*t
        assert D0<=6*initial_sum and D<=4*D0
        for i in range(D-D0):
            name=f'free{i}';labels.append(name);final[name]=1;singles[name]=1;w[name]=1
        scaling={l:F(t,w[l]) for l in labels}
        assert all(F(final[l],D)*scaling[l]**2==1 for l in labels)
        assert sum(F(final[l],D) for l in labels)==1
        assert 200*len(words)<=D<=8000*len(words)
    assert sum(final.values())==D==sum(singles.values())+50*len(gates)
    assert all(2*singles[l]>=final[l] for l in labels)
    assert sorted(j for ids in assigned for j in ids)==list(range(len(gates)))
    return dict(labels=labels,gates=gates,singles=singles,weights=final,D=D,prefixes=prefixes,assigned=assigned,scaling=scaling)

def H(g,v):
    u,x,w,sgn=g
    return np.block([[.6*v[u],.8*sgn*v[w]],[.8*v['z'],-.6*v[x]]])
def objective_and_defects(c,v):
    m=next(iter(v.values())).shape[0];D=c['D'];logdet=0.;pol=0.;energy=0.
    for g in c['gates']:
        h=H(g,v);logdet+=25*np.linalg.slogdet(h)[1]
        pol+=25*np.linalg.norm(h-polar(h),'fro')**2
        energy+=25*np.linalg.norm(h,'fro')**2
    for l,mult in c['singles'].items():
        logdet+=mult*np.linalg.slogdet(v[l])[1]
        pol+=mult*np.linalg.norm(v[l]-polar(v[l]),'fro')**2
        energy+=mult*np.linalg.norm(v[l],'fro')**2
    return math.exp(2*logdet/(D*m)),pol/(D*m),energy/(D*m)

counts=Counter();max_ratios=Counter();cases=[]
for case in range(36):
    N=1+case%4; rows=[]
    for j in range(N):
        k=1+(case+j)%3
        rows.append((list(range(k)),1 if case%3 else -1))
    words=words_from_rows(rows);gens=sorted(set(x for row,_ in rows for x in row))
    R=len(words)
    for mode in ('heavy','square'):
        c=compile_words(gens,words,mode);D=c['D'];rho=R/D
        counts['exact_compiler_instances']+=1
        m=1+case%4;I=np.eye(m,dtype=complex)
        base={g:unitary(m) for g in gens};base.update(z=I,t=I)
        for l,word in c['prefixes']:base[l]=wordval(word,base)
        for l in c['labels']:
            if l not in base:base[l]=I
        xi=sum(n2(wordval(w,base)-sgn*I) for w,sgn in words)/R
        obj,dp,energy=objective_and_defects(c,base)
        assert abs(energy-1)<2e-12
        assert -math.log(obj)<=(3600/49)*rho*xi+1e-11
        counts['forward_average_checks']+=1
        # Perturb arbitrary labels, normalize in the exact weighted Gram metric.
        z={l:base[l]+.015*(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))) for l in c['labels']}
        en=sum(c['weights'][l]*n2(z[l]) for l in c['labels'])/D
        z={l:a/math.sqrt(en) for l,a in z.items()}
        obj,Delta2,en=objective_and_defects(c,z);delta=1-obj
        assert abs(en-1)<2e-12 and Delta2<=2*delta+1e-11
        v={l:polar(z[l]) for l in c['labels']}
        avg=sum(c['weights'][l]*n2(z[l]-v[l]) for l in c['labels'])/D
        assert avg<=2*Delta2+1e-11
        gateerr=[]
        for u,x,w,sgn in c['gates']:
            gateerr.append(n2(v[u]@v['z'].conj().T-sgn*v[w]@v[x].conj().T))
        C0=(144/25)*(3+2*math.sqrt(2))
        assert (50*(12/25)**2/D)*sum(gateerr)<=C0*Delta2+1e-11
        vg={l:a@v['z'].conj().T for l,a in v.items()}
        errs=[n2(wordval(w,vg)-sgn*I) for w,sgn in words]
        for er,ids in zip(errs,c['assigned']):assert er<=6*sum(gateerr[j] for j in ids)+1e-10
        xi=sum(errs)/R
        assert xi<=(18+12*math.sqrt(2))*delta/rho+1e-10
        counts['reverse_average_checks']+=1
        max_ratios['reverse_bound_ratio']=max(max_ratios['reverse_bound_ratio'],xi/((18+12*math.sqrt(2))*delta/rho))
        cases.append(dict(case=case,mode=mode,N=N,R=R,s=len(c['labels']),G=len(c['gates']),D=D,rho=rho))

def errors(values,sgn):
    k=len(values);I=np.eye(values[0].shape[0]);prod=I.astype(complex)
    for x in values:prod=prod@x
    return [n2(x@x-I) for x in values],n2(prod-sgn*I),[n2(x@y@x@y-I) for x,y in combinations(values,2)]

for case in range(360):
    k=1+case%3;m=1+case%6;sgn=(-1)**case;I=np.eye(m)
    V=[unitary(m) for _ in range(k)];X=[sign((v+v.conj().T)/2) for v in V]
    old=errors(V,sgn);new=errors(X,sgn)
    assert all(n2(v-x)<=e+1e-11 for v,x,e in zip(V,X,old[0]))
    oldsum=sum(old[0])+old[1]+sum(old[2]);newsum=new[1]+sum(new[2])
    assert newsum<=28*oldsum+1e-10
    if k==3:
        a,b,z=X;T=(b+a@b@a)/2;bp=sign(T)
        assert n2(b-bp)<=n2(a@b-b@a)/2+1e-10
        A=[a,bp,sgn*a@bp]
    elif k==2:A=[X[0],sgn*X[0]]
    else:A=[sgn*I]
    assert all(n2(a@a-I)<1e-20 for a in A)
    assert all(n2(a@b-b@a)<1e-20 for a,b in combinations(A,2))
    failure=sum(n2(a-x) for a,x in zip(A,X))/(4*k)
    assert failure<=newsum/4+1e-10 and failure<=7*oldsum+1e-10
    counts['word_to_strategy_checks']+=1
    # Reverse local direction with honest commuting parity observables.
    q=unitary(m);diags=[rng.choice([-1,1],size=m) for _ in range(k-1)]
    last=np.full(m,sgn)
    for d in diags:last*=d
    AA=[(q*d)@q.conj().T for d in diags+[last]];BB=[invol(m) for _ in range(k)]
    e=sum(n2(a-b) for a,b in zip(AA,BB))/(4*k)
    er=errors(BB,sgn);xi=(sum(er[0])+er[1]+sum(er[2]))/7
    assert xi<=34*e+1e-10
    counts['strategy_to_word_checks']+=1

# Boundary pinching case T=0, where sign(0)=+1 is required to define a PVM.
pauli_x=np.array([[0,1],[1,0]],complex);pauli_z=np.diag([1.,-1.])
T=(pauli_x+pauli_z@pauli_x@pauli_z)/2
assert np.linalg.norm(T)==0
assert abs(n2(pauli_x-sign(T))-n2(pauli_z@pauli_x-pauli_x@pauli_z)/2)<1e-12
counts['pinching_zero_boundary']=1

patterns=[(0,1,2),(0,0,1),(0,1,0),(0,1,1),(0,0,0)]
for case in range(400):
    pat=patterns[case%len(patterns)];m=1+case%5;sgn=(-1)**case
    probs=rng.random(3);probs/=sum(probs)
    if case%4==0:probs=np.array([1.,0.,0.])
    Q=unitary(m);d1=rng.choice([-1,1],size=m);d2=rng.choice([-1,1],size=m)
    A=[(Q*d)@Q.conj().T for d in (d1,d2,sgn*d1*d2)]
    X={j:invol(m) for j in set(pat)}
    source_fail=sum(probs[p]*n2(A[p]-X[pat[p]]) for p in range(3))/4
    lifted_fail=sum(probs[p]*n2(A[p]-X[pat[p]]) for p in range(3))/16
    assert abs(lifted_fail-source_fail/4)<1e-12
    U=[invol(m) for _ in range(3)];E=[invol(m) for _ in range(3)]
    new_fail=sum(n2(A[p]-U[p]) for p in range(3))/24
    new_fail+=sum(probs[p]*(n2(U[p]-E[p])+n2(E[p]-X[pat[p]])) for p in range(3))/16
    assert source_fail<=18*new_fail+1e-10
    counts['slot_normalization_checks']+=1

# Exact scalar negative control: cancelling repeated variables changes the game.
def best_scalar(repeated):
    best=F(0)
    for a,b in product([-1,1],repeat=2):
        # Row one: (a,a,b)=+1 with slot consistency, or b=+1 after cancellation.
        if repeated:
            win1=max(F(sum(x==y for x,y in zip(ans,(a,a,b))),3) for ans in product([-1,1],repeat=3) if math.prod(ans)==1)
        else:win1=F(b==1)
        win2=F(b==-1)
        best=max(best,(win1+win2)/2)
    return best
assert best_scalar(True)==F(5,6) and best_scalar(False)==F(1,2)

epsilon=F(1,2**40);beta=F(1,4536000);gamma=beta/F(8000)
alpha=F(3600,49)*34
assert alpha*epsilon<=beta/4
# For the normalized repair: e_new<=epsilon/4 and rho<=1/200.
yes_loss=alpha*epsilon/F(800)
assert yes_loss<=gamma/4
assert gamma==F(1,36288000000)
result=dict(status='PASS',candidate_sha256=hashlib.sha256(data).hexdigest(),python=sys.version,numpy=np.__version__,
            counts=dict(counts),max_ratios=dict(max_ratios),compiler_cases=cases,
            negative_control=dict(slot_game_classical_value=str(best_scalar(True)),naively_cancelled_value=str(best_scalar(False))),
            repaired_constants=dict(source_soundness='71/72',normalized_game_soundness='1295/1296',
              beta=str(beta),rho_lower='1/8000',rho_upper='1/200',gamma=str(gamma),epsilon=str(epsilon),
              yes_uniform_loss_upper=str(yes_loss),yes_loss_over_gamma=float(yes_loss/gamma)),
            limitations='Finite diagnostics and exact arithmetic checks; not a proof of undecidability or the external source theorem.')
(ROOT/'checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='compiler_cases'},indent=2))
