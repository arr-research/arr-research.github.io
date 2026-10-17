"""Finite diagnostics for the weighted determinant reduction; not a proof of RE-hardness."""
from pathlib import Path
from collections import Counter
from itertools import combinations
from fractions import Fraction
import json, math
import numpy as np
import sympy as sp

A=Fraction(3,5); B=Fraction(4,5)
def ceil_sqrt(n):
    r=math.isqrt(n)
    return r+(r*r<n)

def compile_contexts(contexts):
    assert contexts and all(1<=len(v)<=3 and len(set(v))==len(v) and sign in (-1,1) for v,sign in contexts)
    generators=sorted({j for v,_ in contexts for j in v})
    # Caller variable identifiers are integers; private compiler labels are strings.
    assert all(isinstance(j,int) for j in generators)
    words=[]
    for row,sign in contexts:
        current=[([j,j],1) for j in row]+[(list(row),sign)]
        current += [([j,k,j,k],1) for j,k in combinations(row,2)]
        current += [([],1)]*(7-len(current))
        words.extend(current)
    labels=['z','t']+generators
    gates=[]; groups=[]
    for wi,(word,sign) in enumerate(words):
        padded=word+['t','t']; group=[]; u=padded[0]
        for j,v in enumerate(padded[1:],1):
            if j==len(padded)-1:
                w='z'; sg=sign
            else:
                w=f'p{wi}_{j}'; sg=1; labels.append(w)
            group.append(len(gates));gates.append((u,v,w,sg));u=w
        group.append(len(gates));gates.append(('t','t','z',1))
        assert len(group)<=6
        groups.append(group)
    q=Counter({l:1 for l in labels})
    for u,v,w,sg in gates:
        assert u!='z' and v!='z' and w not in (u,v)
        q[u]+=9;q[v]+=9;q[w]+=16;q['z']+=16
    w={l:ceil_sqrt(2*q[l]) for l in labels}
    singles={l:1+w[l]**2-q[l] for l in labels}
    D0=sum(v*v for v in w.values());t=ceil_sqrt(D0);D=t*t
    for i in range(D-D0):
        l=f'free{i}';labels.append(l);w[l]=1;singles[l]=1
    assert sum(singles.values())+50*len(gates)==D
    assert sum(v*v for v in w.values())==D
    assert all(2*singles[l]>=w[l]**2 for l in labels)
    normsq=Counter(singles)
    for u,v,vout,sg in gates:
        normsq[u]+=9;normsq[v]+=9;normsq[vout]+=16;normsq['z']+=16
    assert all(normsq[l]==w[l]**2 for l in labels)
    # Exact coefficient rescaling gives normalized Gram I and density sum one.
    assert all(Fraction(t,w[l])**2*normsq[l]/D==1 for l in labels)
    assert sum(Fraction(w[l]**2,D) for l in labels)==1
    R=len(words);assert 200*R<=D<=8000*R
    return dict(contexts=contexts,words=words,labels=labels,gates=gates,groups=groups,
                q=q,w=w,singles=singles,D0=D0,D=D,t=t,R=R,rho=R/D)

def hs2(x):return float(np.linalg.norm(x,'fro')**2/x.shape[0])
def polar(x):
    u,_,vh=np.linalg.svd(x);return u@vh
def sign_hermitian(x):
    ev,u=np.linalg.eigh((x+x.conj().T)/2)
    return (u*np.where(ev>=0,1.,-1.))@u.conj().T
def product(word,values):
    result=np.eye(next(iter(values.values())).shape[0],dtype=complex)
    for l in word:result=result@values[l]
    return result
def word_error(c,values):
    I=np.eye(next(iter(values.values())).shape[0])
    return sum(hs2(product(word,values)-sign*I) for word,sign in c['words'])/c['R']
def extend_labels(c,variables):
    I=np.eye(next(iter(variables.values())).shape[0],dtype=complex)
    values=dict(variables,z=I,t=I)
    for l in c['labels']:
        if isinstance(l,str) and l.startswith('free'):values[l]=I
    for wi,(word,sign) in enumerate(c['words']):
        padded=word+['t','t'];p=values[padded[0]]
        for j,l in enumerate(padded[1:],1):
            p=p@values[l]
            if j<len(padded)-1:values[f'p{wi}_{j}']=p
    assert set(values)==set(c['labels'])
    return values
def gate(g,values):
    u,v,w,sign=g
    return np.block([[.6*values[u],.8*sign*values[w]],[.8*values['z'],-.6*values[v]]])
def log_objective(c,values):
    m=next(iter(values.values())).shape[0]
    value=sum(count*np.linalg.slogdet(values[l])[1] for l,count in c['singles'].items())
    value+=25*sum(np.linalg.slogdet(gate(g,values))[1] for g in c['gates'])
    return float(2*value/(c['D']*m))
def recover_strategy(c,values):
    inv={l:sign_hermitian(values[l]) for row,_ in c['contexts'] for l in row}
    failure=0.
    for row,sigma in c['contexts']:
        k=len(row);X=inv[row[0]];I=np.eye(X.shape[0])
        if k==1: alice=[sigma*I]
        elif k==2: alice=[X,sigma*X]
        else:
            Y=inv[row[1]];Yp=sign_hermitian((Y+X@Y@X)/2)
            assert hs2(X@Yp-Yp@X)<1e-22
            assert hs2(Y-Yp)<=hs2(X@Y-Y@X)/2+1e-11
            alice=[X,Yp,sigma*X@Yp]
        assert hs2(product(list(range(k)),dict(enumerate(alice)))-sigma*I)<1e-22
        failure+=sum(hs2(alice[i]-inv[l]) for i,l in enumerate(row))/(4*k*len(c['contexts']))
    return failure

def main():
    rng=np.random.default_rng(202610171345)
    def unitary(n):
        q,r=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
        return q@np.diag(np.diag(r)/abs(np.diag(r)))
    def perturb(x,eta):
        h=rng.normal(size=x.shape)+1j*rng.normal(size=x.shape);h=(h+h.conj().T)/2
        ev,u=np.linalg.eigh(h)
        return ((u*np.exp(1j*eta*ev))@u.conj().T)@x
    compilations=[];localtypes=set();minrho=1.;maxrho=0.
    for it in range(70):
        n=1+it%11;N=1+it%17
        contexts=[(rng.choice(n,size=min(n,1+j%3),replace=False).tolist(),int(rng.choice([-1,1]))) for j in range(N)]
        c=compile_contexts(contexts);minrho=min(minrho,c['rho']);maxrho=max(maxrho,c['rho'])
        compilations.append({'rows':N,'words':c['R'],'labels':len(c['labels']),'gates':len(c['gates']),'D':c['D']})
        for g in c['gates']:
            u,v,w,sg=g;names=[]
            for l in (u,v,w,'z'):
                if l not in names:names.append(l)
            pattern=tuple(names.index(l) for l in (u,v,w,'z'))+(sg,)
            if pattern in localtypes:continue
            localtypes.add(pattern);coeff={l:sp.zeros(2) for l in names}
            coeff[u][0,0]+=sp.Rational(3,5);coeff[w][0,1]+=sg*sp.Rational(4,5)
            coeff['z'][1,0]+=sp.Rational(4,5);coeff[v][1,1]-=sp.Rational(3,5)
            assert sum((x*x.T for x in coeff.values()),sp.zeros(2))==sp.eye(2)
            assert sum((x.T*x for x in coeff.values()),sp.zeros(2))==sp.eye(2)
            assert all(sp.trace(x.T*y)==0 for l,x in coeff.items() for k,y in coeff.items() if l!=k)
    forward=reverse=rounding=0;negative=0;worst_reverse=0.
    for it in range(48):
        k=1+it%3;m=1+it%4;contexts=[(list(range(k)),int(rng.choice([-1,1])))]
        c=compile_contexts(contexts);vars={l:unitary(m) for l in range(k)}
        vals=extend_labels(c,vars);xi=word_error(c,vars);logf=log_objective(c,vals)
        assert -logf<=(3600/49)*c['rho']*xi+1e-11;forward+=1
        fail=recover_strategy(c,vars);assert fail<=50*xi+1e-11;rounding+=1
        # General nonunitary input, normalized using the exact weighted energy.
        values={l:vals[l]+.04*(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))) for l in c['labels']}
        energy=sum(c['w'][l]**2*hs2(x) for l,x in values.items())/c['D']
        values={l:x/math.sqrt(energy) for l,x in values.items()}
        delta=-math.expm1(log_objective(c,values));assert 0<=delta<=1
        polars={l:polar(x) for l,x in values.items()}
        gauge=polars['z'].conj().T
        vv={l:x@gauge for l,x in polars.items()};got=word_error(c,vv)
        bound=35*delta/c['rho'];assert got<=bound+1e-10
        worst_reverse=max(worst_reverse,got/bound if bound else 0);reverse+=1
        # Direct check that the heavy singletons control all weighted label errors.
        dist=sum(count*hs2(values[l]-polars[l]) for l,count in c['singles'].items())
        dist+=50*sum(hs2(gate(g,values)-polar(gate(g,values))) for g in c['gates'])
        dist/=c['D']
        labeldist=sum(c['w'][l]**2*hs2(values[l]-polars[l]) for l in c['labels'])/c['D']
        assert labeldist<=2*dist+1e-11 and dist<=2*delta+1e-11
        negative+=int(xi>1e-6 and -logf>1e-9)
    # Exact perfect magic-square example (4-dimensional quantum assignment).
    X=sp.Matrix([[0,1],[1,0]]);Z=sp.diag(1,-1);Y=sp.Matrix([[0,-sp.I],[sp.I,0]]);I=sp.eye(2)
    obs=[sp.kronecker_product(X,I),sp.kronecker_product(I,X),sp.kronecker_product(X,X),
         sp.kronecker_product(I,Z),sp.kronecker_product(Z,I),sp.kronecker_product(Z,Z),
         sp.kronecker_product(X,Z),sp.kronecker_product(Z,X),sp.kronecker_product(Y,Y)]
    rows=[([0,1,2],1),([3,4,5],1),([6,7,8],1),([0,3,6],1),([1,4,7],1),([2,5,8],-1)]
    c=compile_contexts(rows)
    for word,sgn in c['words']:
        v=sp.eye(4)
        for l in word:v=v*obs[l]
        assert v==sgn*sp.eye(4)
    for mask in range(512):
        signs=[1 if (mask>>j)&1 else -1 for j in range(9)]
        assert not all(math.prod(signs[j] for j in row)==sgn for row,sgn in rows)
    qv=extend_labels(c,{j:np.array(v.tolist(),dtype=complex) for j,v in enumerate(obs)})
    assert abs(log_objective(c,qv))<1e-12
    result=dict(status='PASS',scope='Finite diagnostics; no proof of undecidability or global novelty.',
        exact_local_patterns=len(localtypes),exact_balancing_cases=len(compilations),
        forward_cases=forward,reverse_cases=reverse,rounding_cases=rounding,
        negative_controls=negative,max_reverse_bound_ratio=worst_reverse,
        observed_rho_range=[minrho,maxrho],magic_square=dict(D=c['D'],labels=len(c['labels']),
          gates=len(c['gates']),words=c['R'],capacity=1,auxiliary_dimension=4,scalar_assignments_rejected=512),
        cases=compilations)
    out=Path(__file__).with_name('weighted-diagnostics.json');out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))

if __name__=='__main__':main()
