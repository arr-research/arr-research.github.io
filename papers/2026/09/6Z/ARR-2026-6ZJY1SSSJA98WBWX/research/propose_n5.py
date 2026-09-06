"""Propose N=5 common spectra and certify rational primal/dual equality."""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import json,time,hashlib
import numpy as np
from scipy.optimize import linprog
from geometry import cut_vertices,D

ROOT=Path(__file__).resolve().parent
def main():
    started=time.monotonic();N=5;d=10
    horn=json.loads((ROOT/'horn_10.json').read_text());triples=horn['triples']
    rows=np.zeros((len(triples)+d-2,d-1),dtype=np.int64)
    rhs_map=np.zeros((len(triples)+d-2,d),dtype=np.int64)
    for t,(I,J,K) in enumerate(triples):
        for i in I:
            if i<d:rows[t,i-1]+=1
        for j in J:
            if j>1:rows[t,d-j]-=1
        for k in K:rhs_map[t,k-1]+=1
    for i in range(d-2):rows[len(triples)+i,i]=1;rows[len(triples)+i,i+1]=-1
    unique,inverse=np.unique(rows,axis=0,return_inverse=True)
    print('constraints',len(rows),'distinct left sides',len(unique),flush=True)
    vertices,_,_=cut_vertices(N);reports=[]
    out=ROOT/'optimal_constant_N5_d10.json'
    for a,b in vertices:
        if a<b:continue
        lam=a+tuple(-x for x in reversed(b));den=lcm(*(x.denominator for x in lam))
        li=np.array([int(x*den) for x in lam],dtype=np.int64)
        rhs=rhs_map@li
        maximal=np.full(len(unique),-10**12,dtype=np.int64)
        np.maximum.at(maximal,inverse,rhs)
        sol=linprog(np.ones(d-1),A_ub=-unique.astype(float),b_ub=-maximal/den,bounds=(0,None),method='highs')
        assert sol.success,sol.message
        s=tuple(Q(float(x)).limit_denominator(10**7) for x in sol.x)
        common=lcm(den,*(x.denominator for x in s))
        si=np.array([int(x*common) for x in s],dtype=np.int64)
        assert max(abs(int(x)) for x in si)*d<2**60
        slacks=rows@si-rhs*(common//den)
        assert min(si)>=0 and min(slacks)>=0,(a,b,min(slacks))
        dual=[];coeff=[Q(0)]*(d-1);objective=Q(0)
        for index,marginal in enumerate(sol.ineqlin.marginals):
            if abs(marginal)<1e-9:continue
            weight=-Q(float(marginal)).limit_denominator(10**7)
            assert weight>=0
            original=int(np.flatnonzero((inverse==index)&(rhs==maximal[index]))[0])
            coeff=[x+weight*int(y) for x,y in zip(coeff,rows[original])]
            objective+=weight*Q(int(rhs[original]),den)
            term={'weight':weight}
            if original<len(triples):term['Horn_triple']=triples[original]
            else:term['ordering_index']=original-len(triples)+1
            dual.append(term)
        assert all(x<=1 for x in coeff) and objective==sum(s),(objective,sum(s))
        distance=D(a,b);cost=sum(s);ratio=(Q(3)-cost)/distance if distance else None
        reports.append({'a':a,'b':b,'common_spectrum':s+(Q(0),),'D':distance,'exact_cost':cost,
                        'ratio':ratio,'dual_terms':dual,'dual_nonnegative_residual':[1-x for x in coeff]})
        gamma=min((x['ratio'] for x in reports if x['ratio'] is not None),default=None)
        report={'status':'IN_PROGRESS','N':5,'ambient_dimension':10,'ordered_vertices':len(vertices),
                'LPs_solved_up_to_sign':len(reports),'optimal_forward_coefficient_so_far':gamma,
                'Horn_triples':len(triples),'Horn_counts':horn['counts'],'certificates':reports}
        out.write_text(json.dumps(report,default=str,indent=2)+'\n')
        if len(reports)%10==0:print('certified',len(reports),'gamma_so_far',gamma,'seconds',round(time.monotonic()-started,1),flush=True)
    report['status']='EXACT_PRIMAL_DUAL_PASS';report['optimal_forward_coefficient']=gamma
    report['source_hashes']={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['propose_n5.py','geometry.py','horn_fast.py']}
    out.write_text(json.dumps(report,default=str,indent=2)+'\n')
    print('DONE',len(reports),gamma,'seconds',round(time.monotonic()-started,1),flush=True)
    print('minimizers',[(x['a'],x['b'],x['exact_cost']) for x in reports if x['ratio']==gamma],flush=True)
if __name__=='__main__':main()
