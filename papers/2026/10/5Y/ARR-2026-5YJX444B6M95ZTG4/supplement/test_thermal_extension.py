"""Exploratory only: test an inequality stronger than source Theorem3.1.
No proof/novelty/validated paper is implied by a positive numerical screen.
"""
from pathlib import Path
import numpy as np,json
rng=np.random.default_rng(170026519)
def ent(a):
    vals=np.linalg.eigvalsh(a)
    assert vals.min()>-1e-10
    vals=vals[vals>1e-16]
    return float(-np.dot(vals,np.log(vals)))
def g(u):
    r=np.sqrt(max(0.,1-4*u));a=(1+r)/2;b=(1-r)/2
    return float(-a*np.log(a)-(b*np.log(b) if b>0 else 0))
best=dict(gap=1e9);slope=dict(gap=1e9);count=0
for index in range(16000):
    d,e=((2,2),(2,3),(3,2),(3,4),(4,4))[index%5]
    X=rng.normal(size=(d,e))+1j*rng.normal(size=(d,e));X/=np.linalg.norm(X)
    Y=rng.normal(size=(d,e))+1j*rng.normal(size=(d,e));Y/=np.linalg.norm(Y)
    a,b,c,z=rng.dirichlet([.5,.5,.5,.5])
    if a*z<b*c:a,b,c,z=b,a,z,c
    k0=np.sqrt(a*z-b*c);k=rng.random()*k0
    xx=X@X.conj().T;yy=Y@Y.conj().T;xy=X@Y.conj().T
    def mat(t):return np.block([[a*xx+b*yy,t*xy],[t*xy.conj().T,c*xx+z*yy]])
    u=(a+b)*(c+z)-k*k;u0=(a+b)*(c+z)-k0*k0
    lhs=ent(mat(k));rhs=(a+c)*ent(xx)+(b+z)*ent(yy)+g(u)
    gap=lhs-rhs;growth=lhs-ent(mat(k0))-g(u)+g(u0)
    rec=dict(gap=gap,index=index,shape=[d,e],coefficients=[a,b,c,z],k=k,k0=k0)
    if gap<best['gap']:
        best=rec;np.savez(Path(__file__).with_name('thermal-min-gap.npz'),X=X,Y=Y,coefficients=[a,b,c,z],k=k)
    if growth<slope['gap']:slope=dict(rec,gap=growth)
    count+=1
result=dict(status='numerical exploratory screen only',cases=count,min_target_gap=best,min_dephasing_growth_gap=slope,claim='No exact certificate, theorem, prior-art conclusion or manuscript grade')
Path(__file__).with_name('thermal-extension-screen.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
