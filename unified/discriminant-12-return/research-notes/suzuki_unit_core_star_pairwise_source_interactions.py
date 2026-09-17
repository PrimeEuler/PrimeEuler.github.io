#!/usr/bin/env python3
"""Binary64 midpoint diagnostic for source interactions in Suzuki unit-core stars.

Reconstructs the source-faithful pole-free finite-high matrix at M=3999,
decomposes it linearly into archimedean and q=2,3,4,5,7 pieces, freezes
the full block-diagonal whitening metric, and computes four tetrahedral
star singular values. Diagnostic only: no positivity/index theorem.
"""
from math import exp, log, pi, sqrt
import itertools
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.linalg import cholesky, solve_triangular, svdvals

CLASSES=(1,5,7,11); QS=(2,3,4,5,7)
LAMBDAS=(log(2),log(3),log(2),log(5),log(7))
ELLS=tuple(log(q) for q in QS)
WEIGHTS=tuple(L/sqrt(q) for L,q in zip(LAMBDAS,QS))

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

def main():
    modes,C=components(); names=('arch','2','3','4','5','7'); B=sum(C.values())
    labels=np.array([core(int(n)) for n in modes]); I={r:np.where(labels==r)[0] for r in CLASSES}
    L={r:cholesky(B[np.ix_(I[r],I[r])],lower=True,check_finite=False) for r in CLASSES}
    def wb(M,r,s):
        x=solve_triangular(L[r],M,lower=True,check_finite=False)
        return solve_triangular(L[s],x.T,lower=True,check_finite=False).T
    def sigma(M,r):
        W=np.concatenate([wb(M[np.ix_(I[r],I[s])],r,s) for s in CLASSES if s!=r],axis=1)
        return float(svdvals(W,check_finite=False)[0])
    def stars(M): return {r:sigma(M,r) for r in CLASSES}
    def gap(x): return x[5]-max(x[1],x[7],x[11])
    full=stars(B); singles={j:stars(C[j]) for j in names}
    ablate={j:stars(B-C[j]) for j in names}
    print('full stars',full,'G5',gap(full))
    print('\nsingle-source fixed-full-D stars')
    for j in names: print(j,singles[j],'G5',gap(singles[j]))
    print('\npair-only connected G5 interactions J=G(i+j)-G(i)-G(j)')
    for a,b in itertools.combinations(names,2):
        p=stars(C[a]+C[b]); J=gap(p)-gap(singles[a])-gap(singles[b])
        print((a,b),'Gpair',gap(p),'J',J)
    print('\nfull-context pair interactions C=G(all)-G(-i)-G(-j)+G(-i,-j)')
    rows=[]
    for a,b in itertools.combinations(names,2):
        minus2=stars(B-C[a]-C[b])
        val=gap(full)-gap(ablate[a])-gap(ablate[b])+gap(minus2)
        rows.append((abs(val),a,b,val,gap(minus2)))
    for _,a,b,val,gminus in sorted(rows,reverse=True):
        print((a,b),'interaction',val,'G_without_both',gminus)
    print('\nguardrail: finite binary64 midpoint diagnostic; fixed full whitening; no theorem promotion')

if __name__=='__main__': main()
