#!/usr/bin/env python3
"""Expanded label-blind Suzuki response-ray diagnostic.

New exploratory lane opened after v13.555.  The sample is predeclared as the
first twelve primes >=5.  The construction is exactly the Level-1 source
formula with the canonical B0={arch,2,3,4,5,7} whitening.  No arithmetic
character or explanatory label enters the geometry.

Observable: U_q=F_q/||F_q||.  Pair geometry is the angle acos(U_q dot U_r).
The seed persistence gate asks whether q=5 and q=13 remain mutual nearest
neighbors after sample expansion.  Finite binary64 diagnostic only.
"""
from math import exp,log,pi,sqrt,acos
import argparse
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.linalg import cholesky,solve_triangular,svd

CLASSES=(1,5,7,11)
BASE_QS=(2,3,4,5,7)
EXP_QS=(5,7,11,13,17,19,23,29,31,37,41,43)

def h(t):
    if t==0.0:return .25
    if abs(t)<1e-7:return .25-t/48-t*t/32+7*t**3/11520
    return exp(-t/2)/(1-exp(-2*t))-1/(2*t)

def core(n):
    while n%2==0:n//=2
    while n%3==0:n//=3
    return n%12

def fingerprints(M):
    modes=np.arange(22,M+1,2,dtype=float); k=modes*pi/2
    H,_=quad_vec(lambda t:h(float(t))*np.sin(k*t),0,2,epsabs=1e-11,epsrel=1e-11)
    arch,_=quad_vec(lambda t:-h(float(t))*((2-t)*np.cos(k*t)+np.sin(k*t)/k),0,2,epsabs=1e-11,epsrel=1e-11)
    Si,Ci=sici(modes*pi); cusp=np.log(modes/4)-Ci-Si/(modes*pi)
    def make(Z,d):
        m=modes[:,None]; n=modes[None,:]; den=n*n-m*m
        num=n*Z[:,None]-m*Z[None,:]; np.fill_diagonal(den,1)
        A=-(2/pi)*num/den; np.fill_diagonal(A,d)
        return .5*(A+A.T)
    C={'arch':make(Si+2*H,cusp+arch)-.53*np.eye(len(modes))}
    for q in sorted(set(BASE_QS+EXP_QS)):
        La=log(2) if q==4 else log(q); ell=log(q); w=La/sqrt(q)
        C[str(q)]=make(2*w*np.sin(modes*pi*ell/2),-w*((2-ell)*np.cos(k*ell)+np.sin(k*ell)/k))
    B=C['arch'].copy()
    for q in BASE_QS:B+=C[str(q)]
    labels=np.array([core(int(n)) for n in modes])
    I={r:np.where(labels==r)[0] for r in CLASSES}
    L={r:cholesky(B[np.ix_(I[r],I[r])],lower=True,check_finite=False) for r in CLASSES}
    def wb(X,r,s):
        y=solve_triangular(L[r],X,lower=True,check_finite=False)
        return solve_triangular(L[s],y.T,lower=True,check_finite=False).T
    out={}
    for q in EXP_QS:
        f=[]
        for r in CLASSES:
            outer=[s for s in CLASSES if s!=r]
            blocks=[wb(C[str(q)][np.ix_(I[r],I[s])],r,s) for s in outer]
            W=np.concatenate(blocks,axis=1); U,S,Vh=svd(W,full_matrices=False,check_finite=False)
            u=U[:,0].copy(); v=Vh[0].copy(); j=int(np.argmax(np.abs(u)))
            if u[j]<0:u=-u;v=-v
            off=0
            for Q in blocks:
                n=Q.shape[1]; f.append(float((u@Q@v[off:off+n])/S[0])); off+=n
        f=np.array(f); out[q]=f/np.linalg.norm(f)
    return out

def report(M):
    F=fingerprints(M); angles={}
    for i,q in enumerate(EXP_QS):
        for r in EXP_QS[i+1:]:
            angles[(q,r)]=acos(float(np.clip(F[q]@F[r],-1,1)))*180/pi
    nearest={}
    for q in EXP_QS:
        candidates=[(a,b if x==q else x) for (x,b),a in angles.items() if x==q or b==q]
        nearest[q]=min(candidates)
    print('M',M,'EXP_QS',EXP_QS)
    for p,a in sorted(angles.items(),key=lambda z:z[1]): print('ANGLE',*p,format(a,'.17g'))
    for q in EXP_QS: print('NEAREST',q,nearest[q][1],format(nearest[q][0],'.17g'))
    print('seed_5_13',format(angles[(5,13)],'.17g'))
    print('seed_gate','PASS-SEED' if nearest[5][1]==13 and nearest[13][1]==5 else 'FAIL-SEED')
    print('guardrail: label-blind finite binary64 ray geometry; no explanatory invariant tested')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--M',type=int,default=499)
    report(ap.parse_args().M)
