import itertools,json,math,pathlib
import numpy as np
root=pathlib.Path(__file__).parent
rng=np.random.default_rng(653)
def ent(a):
    v=np.linalg.eigvalsh((a+a.conj().T)/2);v=v[v>1e-13]
    return float(-np.dot(v,np.log2(v)))
def h(x):return -x*math.log2(x)-(1-x)*math.log2(1-x) if 0<x<1 else 0.
def partial(a,keep,n):
    gone=[i for i in range(n) if i not in keep];z=a.reshape([2]*(2*n));left=n
    for i in sorted(gone,reverse=True):z=np.trace(z,axis1=i,axis2=i+left);left-=1
    return z.reshape(2**left,2**left)
def apply(a,kraus,j,n):
    out=np.zeros_like(a)
    for k in kraus:
        op=np.array([[1.]])
        for t in range(n):op=np.kron(op,k if t==j else np.eye(2))
        out+=op@a@op.conj().T
    return out
minimum_B=1e9;minimum_K=1e9;max_chain_res=0.;min_choi=1e9;cases=0
for n in (2,3):
  for trial in range(60):
    lam=float(rng.uniform(.1,.95));q=1-lam;damp=float(rng.uniform(.05,.95))
    phi=[np.diag([1,math.sqrt(1-damp)]),np.array([[0,math.sqrt(damp)],[0,0]])]
    # Independent finite classical input label X; physical outputs may be entangled.
    probs=rng.dirichlet(np.ones(3));states=[]
    for _ in probs:
        v=rng.normal(size=2**n)+1j*rng.normal(size=2**n);v/=np.linalg.norm(v);states.append(np.outer(v,v.conj()))
    if n==2 and trial==0:
        v=np.array([1,0,0,1])/math.sqrt(2);states[0]=np.outer(v,v)
    tau=np.diag([.23,.77]);replacement=[np.sqrt(tau[i,i])*np.eye(2)[:,i:i+1]@np.eye(2)[r:r+1,:] for i in range(2) for r in range(2)]
    mix=[math.sqrt(lam)*k for k in phi]+[math.sqrt(q)*k for k in replacement]
    signal=[];mixed=[]
    for a in states:
        b=a.copy();z=a.copy()
        for j in range(n):b=apply(b,phi,j,n);z=apply(z,mix,j,n)
        signal.append(b);mixed.append(z)
    Ksum=0.;Hsum=0.;signal_ent=sum(p*ent(a) for p,a in zip(probs,signal))
    for j in range(n):
        K=0.;HF=0.
        for p,a in zip(probs,states):
            z=a.copy()
            for past in range(j):z=apply(z,mix,past,n)
            b=apply(z,phi,j,n);b=partial(b,list(range(j+1)),n)
            r=partial(z,list(range(j)),n)
            reset=np.kron(r,tau);zz=lam*b+q*reset
            K+=p*(ent(b)-ent(r))
            HF+=p*(h(lam)+lam*ent(b)+q*ent(reset)-ent(zz))
        Ksum+=K;Hsum+=HF;minimum_K=min(minimum_K,K)
    lhs=sum(p*ent(a) for p,a in zip(probs,mixed))
    rhs=lam*Ksum+n*q*ent(tau)+n*h(lam)-Hsum
    max_chain_res=max(max_chain_res,abs(lhs-rhs))
    minimum_B=min(minimum_B,Ksum-signal_ent)
    cases+=1
# Explicit falsifier of an invalid per-use conditional-entropy floor: nearly
# noiseless Bell output has negative second conditional entropy, although
# the sum still obeys the global minimum-output floor.
bell=np.array([1,0,0,1])/math.sqrt(2);bell=np.outer(bell,bell).astype(complex)
phi=[np.diag([1,math.sqrt(.99)]),np.array([[0,math.sqrt(.01)],[0,0]])]
tau=np.diag([.23,.77]);rep=[np.sqrt(tau[i,i])*np.eye(2)[:,i:i+1]@np.eye(2)[r:r+1,:] for i in range(2) for r in range(2)]
mix=[math.sqrt(.999)*k for k in phi]+[math.sqrt(.001)*k for k in rep]
hybrid=apply(apply(bell,mix,0,2),phi,1,2)
negative_K=ent(hybrid)-ent(partial(hybrid,[0],2))
assert negative_K<0
assert max_chain_res<1e-10 and minimum_B>=-1e-10
out={'finite_block_cases':cases,'block_sizes':[2,3],'arbitrary_pure_entangled_inputs':True,'minimum_individual_K_in_random_cases':minimum_K,'explicit_negative_conditional_K':negative_K,'minimum_sum_K_minus_all_signal_conditional_entropy':minimum_B,'max_exact_flag_chain_residual':max_chain_res,'pass':True,'scope':'finite causal-reference/conditional-entropy identities and DPI diagnostics only; not infinite-dimensional minimum output, TRE asymptotics, operational capacity or novelty proof'}
(root/'checks653.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
