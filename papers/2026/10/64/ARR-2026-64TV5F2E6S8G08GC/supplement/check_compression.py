"""Exact checks of initial compression and one seven-state positive target.
All source subsets are represented by occupations in the full-layer example.
"""
from pathlib import Path
from collections import defaultdict
import json,math,sys,time
import sympy as sp
import previous_own_odd as own
ROOT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)

def save(name,data):(ROOT/name).write_text(json.dumps(data,ensure_ascii=True,indent=2)+'\n',encoding='utf-8')
def mat(M):return [[str(v) for v in row] for row in M.tolist()]

def compression(k,s,r):
    L,N=own.ground_positive(k,s)
    active=[i for i in range(L.rows) if any(L.row(i))]; initial=active[:r]
    W=sp.Matrix([[sp.Integer(z)**a for a in initial] for z in range(1,r+1)])
    WInv=W.inv(); coeff=WInv*sp.Matrix([[sp.Integer(z)**p for p in active] for z in range(1,r+1)])
    assert coeff[:,:r]==sp.eye(r)
    powers=[[int(p-a) for p in active[r:]] for a in initial]
    assert all(e>0 for row in powers for e in row)
    principal=L.extract(initial,initial); required=own.inertia(principal)
    assert required[0]>=2 and required[2]==0
    trials=[]
    for j in (4,6,8,10,12,16,20,24,32):
        delta=sp.Rational(1,2**j)
        T=sp.Matrix(r,len(active),lambda i,jj:coeff[i,jj]*delta**(active[jj]-initial[i]))
        normalized=T*L.extract(active,active)*T.T
        sig=own.inertia(normalized)
        trials.append({'delta':str(delta),'inertia':sig})
        if sig==required:break
    else:raise AssertionError('finite rational search exhausted')
    sig,piv=own.inertia(normalized,True)
    result={'k':k,'s':s,'r':r,'states':r+2,'active':active,'initial':initial,'discarded':active[r:],
            'W_determinant':str(W.det()),'column_coefficients_before_delta_scaling':mat(coeff),
            'omitted_delta_exponents':powers,'initial_columns_identity':True,
            'constant_normalized_block':mat(principal),'constant_inertia':required,
            'delta':str(delta),'boundary_compression_inertia':sig,'own_pivots':piv,'trials':trials}
    print(json.dumps({'compression_k':k,'s':s,'r':r,'delta':str(delta),'inertia':sig}),flush=True)
    return result

def all_layers(k,s):
    h=k*s-1; pmax=h+1; result={};count=0
    for occupation in own.compositions(h,2*k+1,s):
        count+=1;e=own.edges_inside(occupation);weight=math.prod(math.comb(s,a) for a in occupation)
        nu,edges=own.actual_profiles(occupation,s)
        P,C=result.setdefault(e,(defaultdict(int),defaultdict(int)))
        for r,nr in nu.items():
            for t,nt in nu.items():P[r,t]+=weight*nr*nt
            P[r,r]-=weight*nr
        for (r,t),c in edges.items():
            c*=weight;C[r,t]+=c;C[r+1,t]-=c;C[r,t+1]-=c;C[r+1,t+1]+=c
    matrices={}
    for e,(p,c) in result.items():
        P=sp.zeros(pmax+1);C=sp.zeros(pmax+1)
        for (r,t),value in p.items():P[r,t]=value
        for (r,t),value in c.items():C[r,t]=value
        matrices[e]=(P,C)
    return matrices,count

def seven_state_witness(delta_text):
    started=time.time();k=2;s=9;r=5;h=k*s-1
    delta=sp.Rational(delta_text);d=int(1/delta)
    layers,count=all_layers(k,s);emin=min(layers);emax=max(layers)
    P,C=layers[emin];L,N=own.ground_positive(k,s)
    expected=sp.zeros(L.rows);expected[:P.rows,:P.cols]=P-C
    assert expected==L
    pmax=h+1;trials=[]
    for j in (8,12,16,24,32,48,64,96):
        D=2**j;n=D-1
        if D<=d:continue
        # Integer multiple of Q/rho^emin; scaling factor D^(2*(emax-emin+1)).
        Q=sp.zeros(pmax+1)
        for e,(P,C) in layers.items():
            scalar=(2*D-1)**(e-emin)*D**(2*(emax-e))
            Q+=scalar*(n*n*P-D*D*C)
        den=D*d
        U=sp.Matrix([[sp.Integer(d+n*i)**p*den**(pmax-p) for p in range(pmax+1)] for i in range(1,r+1)])
        H=U*Q*U.T
        sig=own.inertia(H)
        trials.append({'ell_power_2':j,'inertia':sig})
        print(json.dumps({'positive_target_s':s,'ell_power_2':j,'inertia':sig}),flush=True)
        if sig[0]>=2:break
    else:raise AssertionError('finite pin search exhausted')
    ell=-sp.Rational(n,D);nodes=[ell,sp.S.Zero]+[-1+delta*i for i in range(1,r+1)]
    target=sp.Matrix([[1-a*b for b in nodes] for a in nodes])
    assert len(set(nodes))==7 and all(x>0 for x in target)
    assert target.rank()==2 and target[:2,:2].det()<0
    sig,piv=own.inertia(H,True)
    result={'k':k,'s':s,'states':7,'h':h,'derivative_orders':[h,(2*k+1)*s-h-2]+[0]*5,
            'delta':str(delta),'ell':str(ell),'nodes':list(map(str,nodes)),'target':mat(target),
            'target_inertia':[1,1,5],'all_entries_strictly_positive':True,
            'all_occupations_counted':count,'edge_layers':sorted(layers),'minimum_edge_layer':emin,'ground_subsets':N,
            'principal_auxiliary_hessian_inertia':sig,'positive_scalar_normalization':'H = D^(2*(emax-e0+1))*(D*d)^(2*pmax) * U_original*(Q_original/rho^e0)*U_original^T',
            'hessian_prefactor':'h!(n-h-2)!*rho^e0/theta, strictly positive',
            'integer_scaled_principal_hessian':mat(H),'own_pivots':piv,'trials':trials,
            'scope':'All edge layers by occupation enumeration; no direct enumeration of individual labeled subsets or all colorings in this run.',
            'seconds':round(time.time()-started,3)}
    save('seven-state-positive-target.json',result)
    return {'states':7,'k':k,'s':s,'all_occupations_counted':count,'delta':str(delta),'ell':str(ell),'inertia':sig}

if __name__=='__main__':
    rows=[compression(2,9,5),compression(3,20,5),compression(6,7,8)]
    save('initial-compression-checks.json',{'status':'PASS','cases':rows})
    full=seven_state_witness(rows[0]['delta'])
    save('compression-results.json',{'status':'PASS','symbolic_structure_checks':len(rows),'full_positive_target':full})
    print(json.dumps({'status':'PASS','full_target':full}),flush=True)
