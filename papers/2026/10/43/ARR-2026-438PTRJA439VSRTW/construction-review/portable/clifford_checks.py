"""Independent Clifford-family and normal-form checks, using only our compiler."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, itertools, json, math, sys
import numpy as np
import scipy.linalg as la
import independent_checks as core

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'clifford-supplement-reviewed.txt'
EXPECTED='67a99cbb8820895af581ececfe692b6058b8d4f1aa1d4c43a635b76d23e09de4'
RNG=np.random.default_rng(202610180001)

def tensor(factors):
    out=np.ones((1,1),dtype=complex)
    for a in factors:
        out=np.kron(out,a)
    return out

def clifford(n):
    k=n//2
    x=np.array([[0,1],[1,0]],dtype=complex)
    y=np.array([[0,-1j],[1j,0]],dtype=complex)
    z=np.diag([1,-1]).astype(complex)
    ident=np.eye(2,dtype=complex)
    generators=[]
    for r in range(k):
        generators.append(tensor([z]*r+[x]+[ident]*(k-r-1)))
        generators.append(tensor([z]*r+[y]+[ident]*(k-r-1)))
    if n%2:
        generators.append(tensor([z]*k))
    return generators

def words(n):
    return [((i,i),1) for i in range(n)]+[((i,j,i,j),-1) for i in range(n) for j in range(i+1,n)]

def multiply(n,g,h):
    a,s=g
    b,t=h
    crosses=sum(1 for i in range(n) for j in range(i) if s>>i&1 and t>>j&1)
    return ((a+b+crosses)%2,s^t)

def normal_value(g,gen):
    a,mask=g
    out=(-1)**a*np.eye(len(gen[0]),dtype=complex)
    for i,x in enumerate(gen):
        if mask>>i&1:
            out=out@x
    return out

def main():
    data=SOURCE.read_bytes()
    core.require(hashlib.sha256(data).hexdigest()==EXPECTED,'Supplement hash changed')
    (ROOT/'clifford-supplement-reviewed.txt').write_bytes(data)
    (ROOT/'clifford-supplement-numbered.txt').write_text(''.join(f'{i:4d}: {line}\n' for i,line in enumerate(data.decode('utf-8-sig').splitlines(),1)),encoding='utf-8')
    examples=[]
    for n in range(2,11):
        spec=core.compile_words(n,words(n))
        s=2*n*n+n+2
        mass=48*n*n+16*n+33
        gates=(5*n*n+n+2)//2
        core.require(spec['s']==s and spec['M']==mass and len(spec['gates'])==gates and spec['D']==s*mass,
                     'Explicit polynomial size formula')
        core.require(spec['D']<=100*(n+1)**4,'Simple polynomial D upper bound')
        gen=clifford(n)
        m=2**(n//2)
        identity=np.eye(m,dtype=complex)
        # Entries are Gaussian integers and every product below is exact in binary arithmetic.
        core.require(all(np.array_equal(x@x,identity) for x in gen),'Exact Clifford squares')
        core.require(all(np.array_equal(gen[i]@gen[j],-gen[j]@gen[i])
                         for i in range(n) for j in range(i+1,n)), 'Exact Clifford anticommutation')
        labels=core.extend_prefix(spec,gen)
        for u,v,w,z,sign in spec['gates']:
            core.require(np.array_equal(labels[u]@labels[z].conj().T,sign*labels[w]@labels[v].conj().T),
                         'Every compiled Clifford gate is exact')
        eps=F(1,(10000*spec['D']*(n+1)**2)**2)
        examples.append(dict(n=n,s=s,D=spec['D'],M=mass,gates=gates,exact_dimension=m,
                             necessary_approximate_dimension=F(m,2).__str__(),epsilon=str(eps)))
    # Verify the normal-form multiplication table for small finite Clifford groups.
    diagnostics=[]
    for n in range(2,6):
        gen=clifford(n)
        elements=list(itertools.product(range(2),range(2**n)))
        exact={g:normal_value(g,gen) for g in elements}
        for g in elements:
            for h in elements:
                core.require(np.array_equal(exact[g]@exact[h],exact[multiply(n,g,h)]),'Exact normal form multiplication')
        perturbed=[]
        for x in gen:
            raw=RNG.normal(size=x.shape)+1j*RNG.normal(size=x.shape)
            h=(raw+raw.conj().T)/2
            perturbed.append(la.expm(1j*.0001*h)@x)
        identity=np.eye(len(gen[0]))
        positive_errors=[core.norm2(x@x-identity) for x in perturbed]
        inverse_errors=[]
        for i in range(n):
            for j in range(i+1,n):
                x,y=perturbed[i],perturbed[j]
                positive_errors.append(core.norm2(x@y@x@y+identity))
                inverse_errors.append(core.norm2(x@y@x.conj().T@y.conj().T+identity))
        eta=max(positive_errors)
        core.require(max(inverse_errors)<=3*eta+1e-12,'Factor-three inverse conversion')
        theta=max(positive_errors[:n]+inverse_errors)
        approx={g:normal_value(g,perturbed) for g in elements}
        largest=max(core.norm2(approx[g]@approx[h]-approx[multiply(n,g,h)]) for g in elements for h in elements)
        core.require(largest<=(n+1)**2*theta+1e-11,'Normal form (n+1)^2 bound')
        diagnostics.append(dict(n=n,group_order=len(elements),products_checked=len(elements)**2,
                                max_presentation_error=theta,max_multiplicativity_error=largest,
                                ratio_to_claimed_bound=largest/((n+1)**2*theta)))
    u=F(180,10000)
    core.require(42*u==F(189,250) and 42*u<2 and u<F(1,16),'Exact stability tolerance constants')
    core.require(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED,'Supplement modified during review')
    report=dict(status='all checks passed',source=str(SOURCE),sha256=EXPECTED,
                formulas=dict(s='2 n^2+n+2',M='48 n^2+16 n+33',gates='(5 n^2+n+2)/2',
                              D='96 n^4+80 n^3+178 n^2+65 n+66',D_upper='100(n+1)^4',
                              inverse_epsilon_upper='10^12 (n+1)^12',dense_input_entries='s D^2=O(n^10)'),
                examples=examples,normal_form_diagnostics=diagnostics,
                exact_constants=dict(u=str(u),threshold_42u=str(42*u),J_distance='2'),
                qualification='Finite exact matrix checks and numerical perturbation diagnostics, alongside a separate analytic proof review.')
    (ROOT/'clifford-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
