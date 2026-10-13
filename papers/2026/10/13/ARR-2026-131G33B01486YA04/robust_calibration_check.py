"""Independent numerical stress tests of spectral diagonal surrogate.
These supplement the analytic proof; no finite test proves universality.
"""
import numpy as np, pathlib, json
from scipy.linalg import eigh
R=pathlib.Path(__file__).parent
rng=np.random.default_rng(27182818)
records=[]
for i in range(1000):
    d=int(rng.integers(2,7));Q=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    off=10.**rng.uniform(-6,3)
    H=np.diag(rng.normal(size=d)*10**rng.uniform(-2,3))+off*(Q+Q.conj().T)/2
    e,V=eigh(H);rho=np.ones((d,d))/d
    nu=10**rng.uniform(-2,3)
    kernel=nu/(nu+1j*(e[:,None]-e[None,:]))
    out=V@((V.conj().T@rho@V)*kernel)@V.conj().T
    weights=np.abs(V)**2
    surrogate=weights@kernel@weights.T
    gaps=e[:,None]-e[None,:]
    leakage=np.einsum('ja,ab,jb->j',weights,gaps*gaps/(nu*nu+gaps*gaps),weights)
    bound=np.sqrt(d-1)*(np.sqrt(leakage[:,None])+np.sqrt(leakage[None,:]))+(d-1)*np.sqrt(leakage[:,None]*leakage[None,:])
    diff=np.abs(d*out-surrogate);np.fill_diagonal(diff,0)
    excess=float(np.max(diff-bound));assert excess<1e-8,(i,excess)
    kernel4=4*nu/(4*nu+1j*(e[:,None]-e[None,:]))
    L4=np.einsum('ja,ab,jb->j',weights,gaps*gaps/(16*nu*nu+gaps*gaps),weights)
    assert np.max(L4-leakage)<1e-8
    if d==3:
        o4=V@((V.conj().T@rho@V)*kernel4)@V.conj().T
        W=1.5*np.real(out[0,1]+out[1,2])+13.5*np.real(o4[0,1]+o4[1,2])-15*np.real(o4[0,2])
        delta=float(np.max(leakage));static_bound=5+30*np.sqrt(2*delta)+30*delta
        assert W<=static_bound+1e-8
    records.append({'dimension':d,'excess':excess})
report={'status':'PASS','cases':len(records),'dimensions':[2,3,4,5,6],'maximum_bound_excess':max(x['excess'] for x in records),'population_comparison':'L_j(4nu) <= L_j(nu)','witness_bound':'W <= 5 + 30 sqrt(2 delta) + 30 delta','assumption':'Common static Hamiltonian law for all reset preparations and rates','not_a_formal_proof':True}
(R/'robust-calibration-verification.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps(report,indent=2))
