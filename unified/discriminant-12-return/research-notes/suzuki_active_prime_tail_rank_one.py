#!/usr/bin/env python3
"""Active-prime-tail asymptotic rank-one audit for Suzuki's a=1 even-v sector.

This checkpoint continues v13.317.  Let q^(j), j=1,...,4, denote the first
four high-precision eigenvectors of the 10x10 low core n=1,3,...,19.  Using
v13.315's exact off-diagonal prime formula

    (B_prime)_{mn}=-(4/pi)(n A_m-m A_n)/(n^2-m^2),

with

    A_k = sum_q Lambda(q)/sqrt(q) * sin(k*pi*log(q)/2),

we project the remote prime tail directly onto the active basis.

For fixed active vector q^(j),

    g_j(n)=sum_m q_m^(j) (B_prime)_{mn}
          =-(4/pi) L_j/n + O(n^-2),

where

    L_j=sum_m q_m^(j) A_m.

Hence the 4x4 tail Gram matrix has leading form

    Gamma_N = (16/pi^2) (sum_{odd n>=N} 1/n^2) L L^T + lower order,

which is rank one.  Thus only one active combination carries the leading
N^-1/2 prime-tail coupling; three orthogonal active combinations are protected
from that leading channel.

The script reports the high-precision L vector and exploratory finite-tail Gram
spectra.  Reported decimals are not interval-certified.  This checkpoint does
not prove positivity, an exact zero mode, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

CORE = tuple(range(1,20,2))
QS = (2,3,4,5,7)


def high_precision_active_basis(dps: int = 60):
    """Rebuild the 10x10 core and return the first four eigenvectors."""
    with mp.workdps(dps):
        ws = (mp.log(2)/mp.sqrt(2), mp.log(3)/mp.sqrt(3), mp.log(2)/2,
              mp.log(5)/mp.sqrt(5), mp.log(7)/mp.sqrt(7))
        th = tuple(mp.pi*mp.log(q)/2 for q in QS)

        def amp(j):
            return sum(w*mp.sin(j*t) for w,t in zip(ws,th))

        def cusp(m,n):
            if m == n:
                return mp.log(mp.mpf(n)/4)-mp.ci(n*mp.pi)-mp.si(n*mp.pi)/(n*mp.pi)
            return (2/mp.pi)*(n*mp.si(m*mp.pi)-m*mp.si(n*mp.pi))/(m*m-n*n)

        def shift(m,n,t):
            if m == n:
                k=n*mp.pi/2
                return (2-t)*mp.cos(k*t)+mp.sin(k*t)/k
            theta=mp.pi*t/2
            return (4/mp.pi)*(n*mp.sin(m*theta)-m*mp.sin(n*theta))/(n*n-m*m)

        def prime(m,n):
            if m == n:
                return -sum(w*shift(n,n,mp.log(q)) for q,w in zip(QS,ws))
            return -(4/mp.pi)*(n*amp(m)-m*amp(n))/(n*n-m*m)

        def rr(t):
            if t == 0:
                return mp.mpf(1)/4
            return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)

        def pole_c(n):
            k=n*mp.pi/2
            return 2*k*mp.cosh(mp.mpf('0.5'))/(k*k+mp.mpf('0.25'))

        cv=[pole_c(n) for n in CORE]
        A=mp.matrix(10)
        for i,m in enumerate(CORE):
            for j in range(i,10):
                n=CORE[j]
                ar=mp.quad(lambda t: -rr(t)*shift(m,n,t), [0,2])
                v=cusp(m,n)+prime(m,n)+ar+2*cv[i]*cv[j]
                A[i,j]=A[j,i]=v
        vals,Q=mp.eigsy(A)
        Avec=mp.matrix([amp(m) for m in CORE])
        L=[(Q[:,j].T*Avec)[0] for j in range(4)]
        return vals,Q,L


def projected_prime_tail_gram(N: int, max_n: int = 50001, dps: int = 60):
    """Exploratory direct summation of the projected prime tail.

    A leading-rank-one asymptotic remainder is appended beyond max_n.  This is
    descriptive, not an interval enclosure of the full tail.
    """
    vals,Qmp,Lmp=high_precision_active_basis(dps=dps)
    Q4=np.array([[float(Qmp[i,j]) for j in range(4)] for i in range(10)])
    m=np.array(CORE,dtype=float)
    weights=np.array([math.log(2)/math.sqrt(2), math.log(3)/math.sqrt(3),
                      math.log(2)/2, math.log(5)/math.sqrt(5),
                      math.log(7)/math.sqrt(7)])
    theta=np.array([math.pi*math.log(q)/2 for q in QS])
    Acore=np.sin(m[:,None]*theta[None,:]) @ weights

    n0=N if N%2 else N+1
    ns=np.arange(n0,max_n+1,2,dtype=float)
    An=np.sin(ns[:,None]*theta[None,:]) @ weights
    den=ns[:,None]**2-m[None,:]**2
    B=-(4/math.pi)*(ns[:,None]*Acore[None,:]-m[None,:]*An[:,None])/den
    G=B @ Q4
    gram=G.T @ G

    L=np.array([float(x) for x in Lmp])
    gram += (16/math.pi**2)*np.outer(L,L)*(1/(2*max_n))
    return {
        'core_eigenvalues': np.array([float(vals[j]) for j in range(10)]),
        'L': L,
        'gram_eigenvalues': np.linalg.eigvalsh(gram),
        'operator_norm': float(math.sqrt(max(0.0,np.linalg.eigvalsh(gram)[-1]))),
    }


def report():
    vals,Q,L=high_precision_active_basis()
    print('first six core eigenvalues')
    for j in range(6):
        print(j+1, mp.nstr(vals[j],20))
    print('active leading prime-tail vector L')
    for j,x in enumerate(L,1):
        print(j, mp.nstr(x,18))
    print('cutoff / projected prime-tail norm / Gram eigenvalues')
    for N in (237,301,401,501,701,1001):
        r=projected_prime_tail_gram(N)
        print(N, r['operator_norm'], r['gram_eigenvalues'])


if __name__ == '__main__':
    report()
