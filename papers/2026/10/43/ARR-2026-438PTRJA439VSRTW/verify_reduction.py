"""Finite diagnostics for a proposed reduction, not a proof of undecidability."""
from pathlib import Path
from collections import Counter
import json, math
import sympy as sp
import numpy as np

a,b=sp.Rational(3,5),sp.Rational(4,5)

def compile_words(generators, words):
    labels=['reference']+list(generators)+['padding']
    signed=[(list(w)+['padding','padding'],sign) for w,sign in words]
    signed.append((['padding','padding'],1))
    gates=[]
    for wi,(word,sign) in enumerate(signed):
        u=word[0]
        for j in range(1,len(word)):
            v=word[j]
            if j==len(word)-1:
                w='reference';sgn=sign
            else:
                w=f'prefix_{wi}_{j}';labels.append(w);sgn=1
            gates.append((u,v,w,sgn))
            u=w
    counts=Counter({l:1 for l in labels})
    for u,v,w,sgn in gates:
        counts[u]+=9;counts[v]+=9;counts[w]+=16;counts['reference']+=16
    M=max(counts.values());D=len(labels)*M
    singles={l:1+M-counts[l] for l in labels}
    assert sum(singles.values())+50*len(gates)==D
    for u,v,w,sgn in gates:
        assert u!='reference' and v!='reference' and w not in (u,v)
        coeff={l:sp.zeros(2) for l in {u,v,w,'reference'}}
        coeff[u][0,0]+=a;coeff[w][0,1]+=b*sgn
        coeff['reference'][1,0]+=b;coeff[v][1,1]-=a
        assert sum((C*C.T for C in coeff.values()),sp.zeros(2))==sp.eye(2)
        assert sum((C.T*C for C in coeff.values()),sp.zeros(2))==sp.eye(2)
        for l,C in coeff.items():
            for k,E in coeff.items():
                if l!=k: assert sp.trace(C.T*E)==0
    balanced=Counter(singles)
    for u,v,w,sgn in gates:
        balanced[u]+=9;balanced[v]+=9;balanced[w]+=16;balanced['reference']+=16
    assert set(balanced.values())=={M}
    return labels,gates,singles,D,M

def evaluate_labels(generators, words, matrices):
    dim=next(iter(matrices.values())).rows
    values=dict(matrices,reference=sp.eye(dim),padding=sp.eye(dim))
    signed=[(list(w)+['padding','padding'],sign) for w,sign in words]
    signed.append((['padding','padding'],1))
    for wi,(word,sign) in enumerate(signed):
        product=values[word[0]]
        for j in range(1,len(word)):
            product=product*values[word[j]]
            if j<len(word)-1:values[f'prefix_{wi}_{j}']=product
        assert product==sign*sp.eye(dim)
    return values

X=sp.Matrix([[0,1],[1,0]]);Z=sp.diag(1,-1);Y=sp.Matrix([[0,-sp.I],[sp.I,0]]);I=sp.eye(2)
observables=[sp.kronecker_product(X,I),sp.kronecker_product(I,X),sp.kronecker_product(X,X),
sp.kronecker_product(I,Z),sp.kronecker_product(Z,I),sp.kronecker_product(Z,Z),
sp.kronecker_product(X,Z),sp.kronecker_product(Z,X),sp.kronecker_product(Y,Y)]
gens=[f'x{i}' for i in range(9)]
contexts=[([0,1,2],1),([3,4,5],1),([6,7,8],1),([0,3,6],1),([1,4,7],1),([2,5,8],-1)]
words=[([g,g],1) for g in gens]
for indices,sign in contexts:
    words.append(([gens[i] for i in indices],sign))
    for n,i in enumerate(indices):
        for j in indices[n+1:]:words.append(([gens[i],gens[j],gens[i],gens[j]],1))
labels,gates,singles,D,M=compile_words(gens,words)
values=evaluate_labels(gens,words,dict(zip(gens,observables)))
for u,v,w,sgn in gates:
    H=(a*values[u]).row_join(b*sgn*values[w]).col_join((b*values['reference']).row_join(-a*values[v]))
    assert H*H.H==sp.eye(8)
    assert abs(H.det())==1
for mask in range(512):
    scalar=[1 if mask&(1<<i) else -1 for i in range(9)]
    assert not all(math.prod(scalar[i] for i in indices)==sign for indices,sign in contexts)

# Empty, length-one, repeated-symbol, contradictory and ordinary word inputs.
for ww in [[([],1)],[([],-1)],[(['g'],-1)],[(['g','g'],1),(['g','g'],-1)],[(['g','h','g','h'],1)]]:
    compile_words(['g','h'],ww)

rng=np.random.default_rng(202610171058)
def unitary(n):
    q,r=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
    return q@np.diag(np.diag(r)/np.abs(np.diag(r)))
worst_min=1.;worst_log_bound_ratio=0.;negative_controls=0
for it in range(300):
    n=1+it%5;U,V,W,Zn=[unitary(n) for _ in range(4)]
    if it%3==0: W=U@Zn.conj().T@V
    H=np.block([[.6*U,.8*W],[.8*Zn,-.6*V]])
    ev=np.linalg.eigvalsh(H@H.conj().T)
    assert ev.min()>=1/25-1e-12 and ev.max()<=49/25+1e-12
    R=U@Zn.conj().T-W@V.conj().T
    loss=-np.linalg.slogdet(H)[1]/n
    bound=(72/49)*np.linalg.norm(R,'fro')**2/n
    assert loss<=bound+1e-12
    if bound>1e-12:worst_log_bound_ratio=max(worst_log_bound_ratio,loss/bound)
    if it%3==0:assert np.linalg.norm(H@H.conj().T-np.eye(2*n))<1e-11
    else:negative_controls+=int(np.linalg.norm(H@H.conj().T-np.eye(2*n))>1e-8)
    worst_min=min(worst_min,float(ev.min()))

result={'status':'PASS','scope':'Finite diagnostics only; no formal proof and no empirical test can establish undecidability.',
'magic_square':{'labels':len(labels),'gates_before_25fold_replication':len(gates),'base_dimension':D,'equal_squared_coefficient_norm':M,'capacity_exact':'1/'+str(len(labels)),'auxiliary_dimension':4,'all_gate_unitarity_exact':True,'all_scalar_assignments_rejected':512},
'edge_case_compilations':5,'random_complex_gate_cases':300,'smallest_observed_squared_singular_value':worst_min,'max_observed_log_bound_ratio':worst_log_bound_ratio,'negative_controls_rejected':negative_controls}
Path(__file__).with_name('diagnostics.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
