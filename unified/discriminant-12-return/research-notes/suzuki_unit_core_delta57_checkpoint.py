#!/usr/bin/env python3
"""Reproduce the M=3999 fixed-full-D Hadamard Delta_57 checkpoint.

Finite binary64 midpoint diagnostic only.  This does not certify an operator
symmetry, positivity/index improvement, asymptotic statement, or Pell/Suzuki
bridge.
"""
from math import exp, log, pi, sqrt
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.linalg import cholesky, solve_triangular, svd

CLASSES=(1,5,7,11); QS=(2,3,4,5,7)
LAMBDAS=(log(2),log(3),log(2),log(5),log(7))
ELLS=tuple(log(q) for q in QS)
WEIGHTS=tuple(L/sqrt(q) for L,q in zip(LAMBDAS,QS))
H4=np.array([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],dtype=float)

EXPECTED={
 (2,3): {1:-0.9029267235997576,5:+0.5359576668827004,7:-0.7250522420661470,11:-0.6151381598919492},
 (3,5): {1:-0.9408356856671705,5:-0.02861044046328676,7:-0.8192276598694792,11:+0.1146480703384783},
}

def h(t):
    if t==0.0: return 0.25
    if abs(t)<1e-7: return 0.25-t/48.0-t*t/32.0+7.0*t**3/11520.0
    return exp(-t/2.0)/(1.0-exp(-2.0*t))-1.0/(2.0*t)

def core(n):
    while n%2==0: n//=2
    while n%3==0: n//=3
    return n%12

def components(M=3999):
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
    for q,w,ell in zip(QS,WEIGHTS,ELLS):
        Z=2.0*w*np.sin(modes*pi*ell/2.0)
        d=-w*((2.0-ell)*np.cos(k*ell)+np.sin(k*ell)/k)
        out[str(q)]=make(Z,d)
    return modes.astype(int),out

def delta57(x):
    a,b,c=x
    return 4.0*(a-b)*c/(3.0*np.dot(x,x))

def main():
    modes,C=components(); B=sum(C.values())
    labels=np.array([core(int(n)) for n in modes])
    I={r:np.where(labels==r)[0] for r in CLASSES}
    L={r:cholesky(B[np.ix_(I[r],I[r])],lower=True,check_finite=False) for r in CLASSES}
    def wb(M,r,s):
        y=solve_triangular(L[r],M,lower=True,check_finite=False)
        return solve_triangular(L[s],y.T,lower=True,check_finite=False).T
    def response(pair,r):
        M=C[str(pair[0])]+C[str(pair[1])]
        outer=[s for s in CLASSES if s!=r]
        blocks=[wb(M[np.ix_(I[r],I[s])],r,s) for s in outer]
        W=np.concatenate(blocks,axis=1)
        U,S,Vh=svd(W,full_matrices=False,check_finite=False)
        u=U[:,0]; v=Vh[0]; vals={}; off=0
        for s,Q in zip(outer,blocks):
            n=Q.shape[1]; vals[s]=float(u@Q@v[off:off+n]); off+=n
        residue=np.array([vals.get(s,0.0) for s in CLASSES])
        chars=H4@residue/2.0
        x=chars[1:]
        return float(S[0]),residue,chars,delta57(x)
    err=0.0
    for pair in ((2,3),(3,5)):
        print('pair',pair)
        for r in CLASSES:
            sigma,residue,chars,d=response(pair,r)
            err=max(err,abs(d-EXPECTED[pair][r]))
            print('star',r,'sigma',format(sigma,'.17g'))
            print(' residue',*[format(z,'.17g') for z in residue])
            print(' chars',*[format(z,'.17g') for z in chars])
            print(' Delta57',format(d,'.17g'))
    print('max_expected_error',format(err,'.17g'))
    print('identity: Delta57=4*(a-b)*c/(3*(a*a+b*b+c*c))')
    print('guardrail: finite binary64 midpoint; M=3999; fixed full Cholesky whitening; no theorem promotion')
    assert err < 5e-15

if __name__=='__main__': main()
