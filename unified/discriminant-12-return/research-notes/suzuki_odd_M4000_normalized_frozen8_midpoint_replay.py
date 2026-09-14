#!/usr/bin/env python3
"""Independent midpoint replay of the frozen 8D odd M=4000 normalization.

This is a provenance/regression artifact, NOT an outward certificate.
It reconstructs the source-faithful C={2,...,20}, F={22,...,4000}
finite Schur matrix, loads the exact frozen dyadic Q8,L0, and checks

    C_nom = L0^{-1} Q8^T S_F Q8 L0^{-T}.

It then forms the normalized tail residual map.  The band 4002..16000 is
accumulated directly; 16002..2,000,000 uses the convergent inverse-power
Cauchy expansion (j/n <= 4000/16002 < 1/4).  This independently reproduces
the historical ~0.2244148 explicit residual-Gram scale.

Ordinary binary64/scipy source values and linear algebra are used here.
No theorem, exact-zero, RH, or GRH claim follows from this file alone.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.linalg import eigvalsh

from suzuki_odd_M4000_frozen_dyadic_Q8_L0 import Q_HEX, L0_HEX
from suzuki_even_arch_symbolic_rational_certificate import HD_polynomials

QS=(2,3,4,5,7)
LAMBDAS=(math.log(2),math.log(3),math.log(2),math.log(5),math.log(7))
ELLS=tuple(math.log(q) for q in QS)
WEIGHTS=tuple(L/math.sqrt(q) for L,q in zip(LAMBDAS,QS))


def h(t: float) -> float:
    if t == 0.0: return 0.25
    if abs(t) < 1e-7:
        return 0.25-t/48.0-t*t/32.0+7.0*t**3/11520.0
    return math.exp(-t/2.0)/(1.0-math.exp(-2.0*t))-1.0/(2.0*t)


def horner(poly,y):
    out=np.zeros_like(y,dtype=float)
    for k in range(max(poly),-1,-1):
        out=out*y+float(poly.get(k,0))
    return out


def build_finite():
    modes=np.arange(2,4001,2,dtype=float)
    k=modes*math.pi/2.0
    H,_=quad_vec(lambda t:h(float(t))*np.sin(k*t),0.0,2.0,
                 epsabs=1e-11,epsrel=1e-11)
    D,_=quad_vec(lambda t:-h(float(t))*((2.0-t)*np.cos(k*t)+np.sin(k*t)/k),
                 0.0,2.0,epsabs=1e-11,epsrel=1e-11)
    P=np.zeros_like(modes); Pd=np.zeros_like(modes)
    for w,ell in zip(WEIGHTS,ELLS):
        P += w*np.sin(modes*math.pi*ell/2.0)
        Pd -= w*((2.0-ell)*np.cos(k*ell)+np.sin(k*ell)/k)
    Si,Ci=sici(modes*math.pi)
    cusp=np.log(modes/4.0)-Ci-Si/(modes*math.pi)
    Z=2.0*P+Si+2.0*H
    m=modes[:,None]; n=modes[None,:]
    den=n*n-m*m; num=n*Z[:,None]-m*Z[None,:]
    np.fill_diagonal(den,1.0)
    A=-(2.0/math.pi)*num/den
    np.fill_diagonal(A,cusp+Pd+D)
    d=2.0*k*math.sinh(0.5)/(k*k+0.25)
    A += 2.0*np.outer(d,d)
    return modes,0.5*(A+A.T),Z,d


def tail_Z_d(ns,Hp):
    ns=np.asarray(ns,dtype=float)
    H=horner(Hp,1.0/((ns/2.0)*math.pi))
    P=np.zeros_like(ns)
    for w,ell in zip(WEIGHTS,ELLS):
        P += w*np.sin(ns*math.pi*ell/2.0)
    Si,_=sici(ns*math.pi)
    Z=2.0*P+Si+2.0*H
    k=ns*math.pi/2.0
    d=2.0*k*math.sinh(0.5)/(k*k+0.25)
    return Z,d


def report():
    modes,A,Z,d=build_finite()
    Q=np.array([[float.fromhex(x) for x in row] for row in Q_HEX])
    L0=np.array([[float.fromhex(x) for x in row] for row in L0_HEX])
    Acc=A[:10,:10]; Acf=A[:10,10:]; Aff=A[10:,10:]
    X=np.linalg.solve(Aff,Acf.T)
    S=0.5*((Acc-Acf@X)+(Acc-Acf@X).T)
    Linvt=np.linalg.inv(L0.T)
    U=Q@Linvt
    Cnom=0.5*(U.T@S@U+(U.T@S@U).T)

    # Low+finite coefficients of the normalized residual directions.
    W=np.vstack([U,-X@U])
    j=modes
    p=d@W

    Hp,_=HD_polynomials()
    def direct_rows(ns,chunk=200):
        out=np.empty((len(ns),8))
        for a in range(0,len(ns),chunk):
            t=np.asarray(ns[a:a+chunk],dtype=float)
            Zt,dt=tail_Z_d(t,Hp)
            den=t[:,None]**2-j[None,:]**2
            B=(2.0/math.pi)*(j[None,:]*Zt[:,None]-t[:,None]*Z[None,:])/den
            B += 2.0*dt[:,None]*d[None,:]
            out[a:a+len(t)]=B@W
        return out

    near=np.arange(4002,16001,2,dtype=float)
    Y=direct_rows(near)
    G=Y.T@Y

    # Exact inverse-power structure, truncated at k=8 for midpoint replay.
    # At n>=16002, rho<1/4; the omitted midpoint terms are far below the
    # displayed regression precision (compare with direct rows if desired).
    K=8
    M=np.array([(j**(2*k+1))@W for k in range(K)])
    N=np.array([((j**(2*k))*Z)@W for k in range(K)])
    for start in range(16002,2000001,200000):
        stop=min(2000000,start+200000-2)
        t=np.arange(start,stop+1,2,dtype=float)
        Zt,dt=tail_Z_d(t,Hp)
        y=1.0/t
        R=np.zeros((len(t),8))
        for k in range(K):
            R += (2.0/math.pi)*(Zt[:,None]*(y**(2*k+2))[:,None]*M[k]
                   -(y**(2*k+1))[:,None]*N[k])
        R += 2.0*dt[:,None]*p
        G += R.T@R

    Llead=-(2.0/math.pi)*N[0]+(8.0*math.sinh(0.5)/math.pi)*p
    ce=eigvalsh(Cnom)
    he=eigvalsh(0.5*(G+G.T))
    print('finite Schur first levels =',eigvalsh(S)[:5])
    print('C_nom eigenvalues =',ce)
    print('lambda_min(C_nom) =',ce[0])
    print('lambda_max(H_<=2M midpoint) =',he[-1])
    print('||far-tail leading vector L||_2 =',np.linalg.norm(Llead))
    print('historical H explicit = 0.22441479153402388')
    print('guardrail: midpoint/provenance replay only; outward C/H remains required')

    assert ce[0] > 0.99
    assert 0.2243 < he[-1] < 0.2246
    assert 43.8 < np.linalg.norm(Llead) < 43.9


if __name__=='__main__':
    report()
