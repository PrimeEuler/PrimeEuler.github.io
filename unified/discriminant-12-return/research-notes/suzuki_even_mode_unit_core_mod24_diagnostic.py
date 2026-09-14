#!/usr/bin/env python3
"""Midpoint diagnostic for ramified/unit-core splitting of the odd Suzuki high block.

This script is deliberately diagnostic, not a positivity certificate.
It reconstructs the source-faithful pole-free finite-high matrix on

    F = {22,24,...,4000}

and classifies each even Fourier index n by its unit core

    u(n) = n / (2^v2(n) 3^v3(n))  (mod 12),

so u(n) lies in {1,5,7,11}.  For the v2(n)=1, 3\nmid n stratum this is
exactly the mod-24 lift

    n mod 24 = 2,10,14,22  <->  u mod 12 = 1,5,7,11.

Reported quantities are binary64/scipy midpoint diagnostics only.
No V4 invariance of the Suzuki operator is assumed or inferred.
"""
from __future__ import annotations

from math import exp, log, pi, sqrt
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.sparse.linalg import eigsh, svds

QS=(2,3,4,5,7)
LAMBDAS=(log(2),log(3),log(2),log(5),log(7))
ELLS=tuple(log(q) for q in QS)
WEIGHTS=tuple(L/sqrt(q) for L,q in zip(LAMBDAS,QS))


def h(t: float) -> float:
    if t == 0.0:
        return 0.25
    if abs(t) < 1e-7:
        return 0.25 - t/48.0 - t*t/32.0 + 7.0*t**3/11520.0
    return exp(-t/2.0)/(1.0-exp(-2.0*t)) - 1.0/(2.0*t)


def pole_free_matrix():
    modes=np.arange(22,4001,2,dtype=float)
    k=modes*pi/2.0
    H,_=quad_vec(lambda t:h(float(t))*np.sin(k*t),0.0,2.0,epsabs=1e-11,epsrel=1e-11)
    arch,_=quad_vec(lambda t:-h(float(t))*((2.0-t)*np.cos(k*t)+np.sin(k*t)/k),0.0,2.0,epsabs=1e-11,epsrel=1e-11)

    prime_seq=np.zeros_like(modes)
    prime_diag=np.zeros_like(modes)
    for w,ell in zip(WEIGHTS,ELLS):
        prime_seq += w*np.sin(modes*pi*ell/2.0)
        prime_diag -= w*((2.0-ell)*np.cos(k*ell)+np.sin(k*ell)/k)

    Si,Ci=sici(modes*pi)
    cusp=np.log(modes/4.0)-Ci-Si/(modes*pi)
    Z=2.0*prime_seq+Si+2.0*H

    m=modes[:,None]
    n=modes[None,:]
    den=n*n-m*m
    num=n*Z[:,None]-m*Z[None,:]
    np.fill_diagonal(den,1.0)
    A=-(2.0/pi)*num/den
    np.fill_diagonal(A,cusp+prime_diag+arch)
    return modes.astype(int),0.5*(A+A.T)


def vp(n,p):
    a=0
    while n%p==0:
        n//=p
        a+=1
    return a


def unit_core_mod12(n):
    while n%2==0:
        n//=2
    while n%3==0:
        n//=3
    return n%12


def report():
    modes,A0=pole_free_matrix()
    B=A0-0.53*np.eye(len(A0))
    vals,vecs=eigsh(B,k=1,which='SA',tol=1e-12)
    v=vecs[:,0]

    labels=np.array([unit_core_mod12(int(n)) for n in modes])
    classes=(1,5,7,11)
    print('shifted full minimum =',repr(float(vals[0])))
    print('unit-core class diagnostics:')
    groups={}
    for r in classes:
        idx=np.where(labels==r)[0]
        groups[r]=idx
        Br=B[np.ix_(idx,idx)]
        lmin=float(eigsh(Br,k=1,which='SA',return_eigenvectors=False,tol=1e-11)[0])
        mass=float(np.sum(v[idx]**2))
        print(r,'count=',len(idx),'shifted block min=',repr(lmin),'lowest-vector mass=',repr(mass))

    print('pairwise off-block operator norms:')
    for i,r in enumerate(classes):
        for s in classes[i+1:]:
            M=B[np.ix_(groups[r],groups[s])]
            norm=float(svds(M,k=1,which='LM',return_singular_vectors=False,tol=1e-8)[0])
            print((r,s),repr(norm))

    mask=np.array([(vp(int(n),2)==1 and int(n)%3!=0) for n in modes])
    residues,counts=np.unique(modes[mask]%24,return_counts=True)
    print('v2=1, 3∤n mod-24 residues/counts =',list(zip(residues.tolist(),counts.tolist())))
    print('mapping /2 mod12: 2->1, 10->5, 14->7, 22->11')
    print('guardrail: midpoint structural diagnostic only; no operator symmetry theorem')


if __name__=='__main__':
    report()
