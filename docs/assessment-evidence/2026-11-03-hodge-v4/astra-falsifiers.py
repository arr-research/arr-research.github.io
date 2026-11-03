from pathlib import Path
from itertools import product
import json, numpy as np
from scipy.linalg import null_space

rng = np.random.default_rng(2631)
results = {'seed':2631,'interpretation':'Finite floating-point falsifier attempts, not proofs or Lean verification.'}

def forward(a,k): return np.roll(a,-1,axis=k)-a
def divergence(a,d):
    return sum(a[...,i,:]-np.roll(a[...,i,:],1,axis=i) for i in range(d))
def hodge(a,d):
    curl=sum(float(np.sum((forward(a[...,j,:],i)-forward(a[...,i,:],j))**2))
             for i in range(d) for j in range(i+1,d))
    return curl+float(np.sum(divergence(a,d)**2))
def gradient(a,d): return np.stack([forward(a,k) for k in range(d)],axis=-1)
def innerq(a,b,d,w):
    ga,gb=gradient(a,d),gradient(b,d)
    return float(np.sum(ga*gb*(1+w[...,None,:])))

checks=[]
for d,n in [(1,1),(1,2),(1,7),(2,2),(2,3),(2,4),(2,7),(3,2),(3,4),(4,3)]:
    a=rng.normal(size=(n,)*d+(d,3))
    q=hodge(a,d); g=float(np.sum(gradient(a,d)**2))
    err=abs(q-g)/max(1,g)
    assert err<1e-12
    checks.append({'d':d,'n':n,'relative_hodge_gradient_error':err})
results['whole_space_hodge']=checks

checks=[]
for ell in [2,3,4,5,7]:
    for coarse in [1,2]:
        d,n=2,ell*coarse
        grid=np.indices((n,)*d)
        z=np.exp(2j*np.pi*grid[1]/ell)
        a=np.zeros((n,n,d,3)); a[...,0,0]=z.real; a[...,0,1]=z.imag
        q=np.zeros((coarse,coarse,d,3))
        for y in product(range(coarse),repeat=d):
            for offset in product(range(ell),repeat=d):
                x=tuple(ell*y[t]+offset[t] for t in range(d))
                for j in range(d):
                    for k in range(ell):
                        xx=list(x); xx[j]=(xx[j]+k)%n
                        q[y+(j,)]+=a[tuple(xx)+(j,)]/ell**d
        residual=float(np.linalg.norm(q)); diverr=float(np.linalg.norm(divergence(a,d)))
        quotient=hodge(a,d)/float(np.sum(a*a)); target=4*np.sin(np.pi/ell)**2
        assert residual<1e-12 and diverr<1e-12 and abs(quotient-target)<1e-12
        checks.append({'ell':ell,'Nprime':coarse,'Q_residual':residual,
                       'divergence_residual':diverr,'energy_quotient':quotient,'target':target})
results['original_block_kernel']=checks

checks=[]
for d,n in [(2,2),(2,3),(2,4),(2,5),(2,8),(3,4)]:
    i,j=0,1
    grid=np.indices((n,)*d)
    for R in sorted(set([0,1,n//2,n-1])):
        basis=[]
        for s in range(1,R+1):
            z=np.exp(2j*np.pi*s*grid[i]/n)/np.sqrt(n**d)
            for phase in [1,1j]:
                a=np.zeros((n,)*d+(d,3)); a[...,j,0]=(phase*z).real; a[...,j,1]=(phase*z).imag
                basis.append(a)
        if not basis:
            checks.append({'d':d,'n':n,'R':R,'zero_band':True}); continue
        X=np.stack([a.ravel() for a in basis],axis=1)
        gramerr=float(np.max(abs(X.T@X-np.eye(2*R))))
        diverr=max(float(np.max(abs(divergence(a,d)))) for a in basis)
        # Very large weights in unrelated directions, plus a directional point spike.
        w=rng.uniform(0,1e4,size=(n,)*d+(d,d))
        w[...,j,i]=0; w[(0,)*d+(j,i)]=n**(d+1)
        mean=float(np.mean(w[...,j,i]))
        T=np.array([[innerq(a,b,d,w) for b in basis] for a in basis])
        expected=2*(1+mean)*sum(abs(np.exp(2j*np.pi*s/n)-1)**2 for s in range(1,R+1))
        traceerr=abs(np.trace(T)-expected)/max(1,expected)
        ev=float(np.linalg.eigvalsh(T)[0])
        m=max(0,2*R//3)
        L=rng.normal(size=(m,2*R))
        U=null_space(L)
        c=float(np.linalg.eigvalsh(U.T@T@U)[0])
        slack=float(np.trace(T)-max(0,c)*(2*R-m))
        assert gramerr<1e-12 and diverr<1e-12 and traceerr<1e-12 and ev>-1e-9 and slack>-1e-8
        checks.append({'d':d,'n':n,'R':R,'dim':int(np.linalg.matrix_rank(X)),
                       'gram_error':gramerr,'divergence_error':diverr,'mean':mean,
                       'max_weight':float(np.max(w)),'trace_relative_error':traceerr,
                       'min_compressed_eigenvalue':ev,'random_kernel_trace_slack':slack})
results['actual_divergence_free_strip']=checks

d,n,R=2,9,2
grid=np.indices((n,)*d)
band=[]
for k in product(range(-R,R+1),repeat=d):
    z=np.exp(2j*np.pi*sum(k[t]*grid[t] for t in range(d))/n)/np.sqrt(n**d)
    for phase in [1,1j]:
        a=np.zeros((n,)*d+(d,3)); a[...,0,0]=(phase*z).real; a[...,0,1]=(phase*z).imag
        band.append(a)
X=np.stack([a.ravel() for a in band],axis=1)
C=rng.normal(size=(7,X.shape[0])); VA=rng.normal(size=(X.shape[0],9)); VB=rng.normal(size=(9,X.shape[0])); V=VA@VB
U=null_space(np.vstack([C@X,VB@X])); vec=X@U[:,0]; a=vec.reshape((n,)*d+(d,3))
ratio=hodge(a,d)/float(np.sum(a*a)); bound=4*np.pi**2*d*R**2/n**2
assert U.shape[1]>=50-7-9 and ratio<=bound+1e-12
results['finite_budget_nonsymmetric_repair']={'dimension':50,'measurement_dim':7,'repair_rank':int(np.linalg.matrix_rank(V)),
  'joint_kernel_dimension':U.shape[1],'C_residual':float(np.linalg.norm(C@vec)),
  'V_residual':float(np.linalg.norm(V@vec)),'rayleigh':ratio,'bound':bound}

checks=[]
for d,n in [(2,1),(2,2),(2,3),(2,4),(3,2),(3,3)]:
    eigenvalues=[2.0]
    for k in product(range(n),repeat=d):
        if any(k): eigenvalues.append(2*d*n*n*sum(abs(np.exp(2j*np.pi*s/n)-1)**2 for s in k))
    assert min(eigenvalues)>=1
    checks.append({'d':d,'n':n,'minimum_eigenvalue_repair_plus_mean_penalty':min(eigenvalues)})
results['quadratic_boundary']=checks

results['analytic_counterexample_spotchecks']={
  'curved_quadratic_sector': [{'t':t,'quotient':t*t/(1+t*t)} for t in [0.1,0.01,0.001]],
  'nonquadratic_C1_energy_sector': [{'u_norm':t,'quotient':1/(1+t**(2/3))} for t in [0.1,0.01,0.001]],
  'schur_fiber_unpenalized_value': [{'t':t,'value':1-2*t} for t in [1,10,100]],
  'penalty_power_composition': [{'x_norm':t,'ratio':((t**1.5)**(4/3))/(t*t)} for t in [0.1,0.01,0.001]]}

path=Path(__file__).with_name('astra-tests.json')
path.write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps({'status':'all assertions passed','hodge_cases':len(results['whole_space_hodge']),
 'strip_cases':len(results['actual_divergence_free_strip']),'budget':results['finite_budget_nonsymmetric_repair'],
 'max_hodge_error':max(x['relative_hodge_gradient_error'] for x in results['whole_space_hodge']),
 'max_strip_trace_error':max(x.get('trace_relative_error',0) for x in checks if 'trace_relative_error' in x) if False else max(x.get('trace_relative_error',0) for x in results['actual_divergence_free_strip'])},indent=2))
