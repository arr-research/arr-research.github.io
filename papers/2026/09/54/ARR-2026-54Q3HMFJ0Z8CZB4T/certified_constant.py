"""Compute gamma_(N,d) by proposing LP solutions and certifying them exactly.

Requires NumPy/SciPy only for proposals. Every accepted value has exact rational
primal and dual witnesses. Stops with an error if rationalization fails; no
uncertified output is labelled proved. The manuscript gives the finite algorithm
with an exact rational LP oracle; this implementation uses a checked proposal.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import argparse,json,hashlib
import numpy as np
from scipy.optimize import linprog
from geometry import cut_vertices,D
from verify_balanced_four import horn

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--N',type=int,default=4)
    parser.add_argument('--ambient',type=int)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();N=args.N;d=args.ambient or 2*N
    if not (2<=N and d>=2*N):raise ValueError('Require N>=2 and d>=2N')
    vertices,_,_=cut_vertices(N)
    triples=[t for r in range(1,d) for t in horn(r,d)]
    lower=[]
    for I,J,K in triples:
        row=[0]*(d-1)
        for i in I:
            if i<d:row[i-1]+=1
        for j in J:
            if j>1:row[d-j]-=1
        lower.append(row)
    for i in range(d-2):
        row=[0]*(d-1);row[i]=1;row[i+1]=-1;lower.append(row)
    A=-np.array(lower,dtype=float)
    reports=[]
    for a,b in vertices:
        if a<b:continue
        lam=a+(Q(0),)*(d-2*N)+tuple(-x for x in reversed(b))
        rhs=[sum(lam[k-1] for k in K) for I,J,K in triples]+[Q(0)]*(d-2)
        res=linprog(np.ones(d-1),A_ub=A,b_ub=-np.array(rhs,dtype=float),bounds=(0,None),method='highs')
        if not res.success:raise ValueError(res.message)
        s=tuple(Q(float(x)).limit_denominator(10**8) for x in res.x)
        if min(s)<0:raise ValueError('Rational primal is negative')
        den=lcm(*(x.denominator for x in s+tuple(rhs)))
        si=[int(x*den) for x in s];ri=[int(x*den) for x in rhs]
        if any(sum(x*y for x,y in zip(row,si))<r for row,r in zip(lower,ri)):
            raise ValueError('Rational primal violates an exact constraint')
        dual=[];coeff=[Q(0)]*(d-1);objective=Q(0)
        for index,marginal in enumerate(res.ineqlin.marginals):
            if abs(marginal)<1e-9:continue
            weight=-Q(float(marginal)).limit_denominator(10**8)
            if weight<0:raise ValueError('Rational dual has negative weight')
            coeff=[x+weight*y for x,y in zip(coeff,lower[index])]
            objective+=weight*rhs[index]
            term={'weight':weight}
            if index<len(triples):term['Horn_triple']=triples[index]
            else:term['ordering_index']=index-len(triples)+1
            dual.append(term)
        if any(x>1 for x in coeff):raise ValueError('Rational dual exceeds objective coefficients')
        if sum(s)!=objective:raise ValueError('Exact primal-dual objectives differ')
        distance=D(a,b);cost=sum(s)
        ratio=(Q(N+1,2)-cost)/distance if distance else None
        reports.append({'a':a,'b':b,'common_spectrum':s+(Q(0),),'D':distance,'exact_cost':cost,
                        'ratio':ratio,'dual_terms':dual,'dual_nonnegative_residual':tuple(1-x for x in coeff)})
    gamma=min(x['ratio'] for x in reports if x['ratio'] is not None)
    report={'status':'EXACT_PRIMAL_DUAL_PASS','N':N,'ambient_dimension':d,'ordered_vertices':len(vertices),
            'LPs_solved_up_to_sign':len(reports),'optimal_forward_coefficient':gamma,'Horn_triples':len(triples),
            'certificates':reports,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'The finite values are certified exactly. General validity of the cell reduction and Horn sufficiency is supplied by the manuscript and its stated antecedents. This checked-proposal implementation may stop rather than certify difficult floating-point proposals.'}
    out=args.output or Path(__file__).with_name(f'optimal_constant_N{N}_d{d}.json')
    out.write_text(json.dumps(report,default=str,indent=2)+'\n',encoding='utf-8',newline='\n')
    print({k:v for k,v in report.items() if k not in ['certificates','scope']})

if __name__=='__main__':main()
