#!/usr/bin/env python3
"""Level-1 chi12-blind Suzuki source-response diagnostic.

Construct source-separated Suzuki matrices for q=5,7,11,13, but freeze the
whitening metric from the canonical baseline q={2,3,4,5,7}.  No chi12 value,
epsilon, or character label enters matrix construction, whitening, SVD, or the
response fingerprints.  Character labels are used only after fingerprints are
frozen to evaluate the predeclared 2+2 comparison.

Finite binary64 midpoint diagnostic only.  No operator theorem, Pell/Suzuki
intertwiner, positivity/index improvement, RH, or GRH statement is implied.
"""
from math import exp, log, pi, sqrt
import argparse
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.linalg import cholesky, solve_triangular, svd

CLASSES=(1,5,7,11)
BASE_QS=(2,3,4,5,7)
TEST_QS=(5,7,11,13)


def h(t):
    if t==0.0: return 0.25
    if abs(t)<1e-7: return 0.25-t/48.0-t*t/32.0+7.0*t**3/11520.0
    return exp(-t/2.0)/(1.0-exp(-2.0*t))-1.0/(2.0*t)


def core(n):
    while n%2==0: n//=2
    while n%3==0: n//=3
    return n%12


def components(M):
    modes=np.arange(22,M+1,2,dtype=float); k=modes*pi/2.0
    H,_=quad_vec(lambda t:h(float(t))*np.sin(k*t),0.0,2.0,epsabs=1e-11,epsrel=1e-11)
    arch,_=quad_vec(lambda t:-h(float(t))*((2.0-t)*np.cos(k*t)+np.sin(k*t)/k),0.0,2.0,epsabs=1e-11,epsrel=1e-11)
    Si,Ci=sici(modes*pi); cusp=np.log(modes/4.0)-Ci-Si/(modes*pi)
    def make(Z,diag):
        m=modes[:,None]; n=modes[None,:]; den=n*n-m*m
        num=n*Z[:,None]-m*Z[None,:]; np.fill_diagonal(den,1.0)
        A=-(2.0/pi)*num/den; np.fill_diagonal(A,diag)
        return 0.5*(A+A.T)
    out={'arch':make(Si+2.0*H,cusp+arch)-0.53*np.eye(len(modes))}
    for q in sorted(set(BASE_QS+TEST_QS)):
        Lambda=log(2) if q==4 else log(q)
        ell=log(q); w=Lambda/sqrt(q)
        Z=2.0*w*np.sin(modes*pi*ell/2.0)
        d=-w*((2.0-ell)*np.cos(k*ell)+np.sin(k*ell)/k)
        out[str(q)]=make(Z,d)
    return modes.astype(int),out


def fingerprints(M):
    modes,C=components(M)
    B=C['arch'].copy()
    for q in BASE_QS: B+=C[str(q)]
    labels=np.array([core(int(n)) for n in modes])
    I={r:np.where(labels==r)[0] for r in CLASSES}
    L={r:cholesky(B[np.ix_(I[r],I[r])],lower=True,check_finite=False) for r in CLASSES}
    def wb(A,r,s):
        y=solve_triangular(L[r],A,lower=True,check_finite=False)
        return solve_triangular(L[s],y.T,lower=True,check_finite=False).T
    out={}
    for q in TEST_QS:
        amp=log(q)/sqrt(q); R=[]; F=[]
        for r in CLASSES:
            outer=[s for s in CLASSES if s!=r]
            blocks=[wb(C[str(q)][np.ix_(I[r],I[s])],r,s) for s in outer]
            W=np.concatenate(blocks,axis=1)
            U,S,Vh=svd(W,full_matrices=False,check_finite=False)
            u=U[:,0].copy(); v=Vh[0].copy()
            j=int(np.argmax(np.abs(u)))
            if u[j]<0.0: u=-u; v=-v
            R.append(float(S[0]/amp)); off=0
            for Q in blocks:
                n=Q.shape[1]
                F.append(float((u@Q@v[off:off+n])/S[0])); off+=n
        out[q]=(np.array(R),np.array(F))
    return out


def report(M):
    A=fingerprints(M)
    print('M',M,'BASE_QS',BASE_QS,'TEST_QS',TEST_QS)
    for q in TEST_QS:
        print('R',q,*[format(x,'.17g') for x in A[q][0]])
        print('F',q,*[format(x,'.17g') for x in A[q][1]])
    def D(q,r): return float(np.linalg.norm(A[q][1]-A[r][1])/sqrt(12.0))
    pairs=((5,7),(11,13),(5,11),(5,13),(7,11),(7,13))
    ds={p:D(*p) for p in pairs}
    for p in pairs: print('D',*p,format(ds[p],'.17g'))
    max_within=max(ds[(5,7)],ds[(11,13)])
    min_cross=min(ds[(5,11)],ds[(5,13)],ds[(7,11)],ds[(7,13)])
    print('max_within',format(max_within,'.17g'))
    print('min_cross',format(min_cross,'.17g'))
    print('pairwise_gap',format(min_cross-max_within,'.17g'))
    print('blind_gate', 'PASS' if min_cross>max_within else 'FAIL')
    print('guardrail: chi12 labels enter only after frozen fingerprints; finite binary64 midpoint diagnostic')


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--M',type=int,default=1999)
    report(ap.parse_args().M)
