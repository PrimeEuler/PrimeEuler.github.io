#!/usr/bin/env python3
"""Exact cusp-tail channel and protected-plane audit for Suzuki a=1 even-v.

This checkpoint continues v13.319 and corrects one asymptotic point there.
For odd core mode m and odd remote mode n, the exact cusp matrix entry is

    C_mn = (2/pi) [n Si(m pi)-m Si(n pi)]/(m^2-n^2).

For fixed m and n->infinity the exact leading coefficient is therefore

    C_mn = -(2/pi) Si(m pi)/n + O_m(n^-2),

not merely the decomposition-level coefficient

    -(1 + 2/(pi^2 m))/n.

After subtracting the exact fixed-core channel,

    R^c_mn = -(2/pi)/(1-m^2/n^2)
             [m^2 Si(m pi)/n^3 - m Si(n pi)/n^2],

so the remainder is O_m(n^-2).  Projecting onto the first four high-precision
core eigenvectors gives an O(N^-3/2) Hilbert-Schmidt remote-tail remainder.

Combining with v13.318-v13.319 prime channel L produces a 4x2 channel matrix
[L,S], where

    S_j = -(2/pi) sum_m q_m^(j) Si(m pi).

Since rank[L,S]=2 numerically and structurally unless the two vectors become
collinear, the four-dimensional active space contains a two-dimensional plane
orthogonal to both leading nonsmooth channels.  On that plane both prime and
cusp couplings begin at O(n^-2).

Reported decimals are ordinary high-precision / floating evaluations, not
interval-certified enclosures.  This is a tail-structure reduction only; it
does not establish positivity, an exact zero mode, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

CORE = tuple(range(1, 20, 2))
QS = (2, 3, 4, 5, 7)


def high_precision_active_basis(dps: int = 60):
    with mp.workdps(dps):
        ws = (mp.log(2)/mp.sqrt(2), mp.log(3)/mp.sqrt(3), mp.log(2)/2,
              mp.log(5)/mp.sqrt(5), mp.log(7)/mp.sqrt(7))

        def amp(j):
            return sum(w*mp.sin(j*mp.pi*mp.log(q)/2)
                       for q,w in zip(QS,ws))

        def cusp(m,n):
            if m == n:
                return (mp.log(mp.mpf(n)/4)-mp.ci(n*mp.pi)
                        -mp.si(n*mp.pi)/(n*mp.pi))
            return ((2/mp.pi)*(n*mp.si(m*mp.pi)-m*mp.si(n*mp.pi))
                    /(m*m-n*n))

        def shift(m,n,t):
            if m == n:
                k=n*mp.pi/2
                return (2-t)*mp.cos(k*t)+mp.sin(k*t)/k
            th=mp.pi*t/2
            return ((4/mp.pi)*(n*mp.sin(m*th)-m*mp.sin(n*th))
                    /(n*n-m*m))

        def prime(m,n):
            if m == n:
                return -sum(w*shift(n,n,mp.log(q))
                            for q,w in zip(QS,ws))
            return (-(4/mp.pi)*(n*amp(m)-m*amp(n))/(n*n-m*m))

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
        return vals,Q


def channels(dps: int = 60):
    vals,Q=high_precision_active_basis(dps=dps)
    with mp.workdps(dps):
        ws=(mp.log(2)/mp.sqrt(2), mp.log(3)/mp.sqrt(3), mp.log(2)/2,
            mp.log(5)/mp.sqrt(5), mp.log(7)/mp.sqrt(7))
        Avec=mp.matrix([
            sum(w*mp.sin(m*mp.pi*mp.log(q)/2) for q,w in zip(QS,ws))
            for m in CORE
        ])
        Svec=mp.matrix([-(2/mp.pi)*mp.si(m*mp.pi) for m in CORE])
        L=[(Q[:,j].T*Avec)[0] for j in range(4)]
        S=[(Q[:,j].T*Svec)[0] for j in range(4)]
        return vals,Q,L,S


def odd_sum4_tail_bound(N: int) -> float:
    return 1.0/N**4 + 1.0/(6.0*N**3)


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0/N**6 + 1.0/(10.0*N**5)


def cusp_remainder_hs_bound(N: int, dps: int = 60) -> float:
    """Conservative active 4D HS bound after exact S/n subtraction.

    For odd n>=N>19 use |Si(n pi)|<2 and

      |R^c_mn| <= (2/pi)/(1-(19/N)^2)
                   [m^2 |Si(m pi)|/n^3 + 2m/n^2].

    Each active row is bounded by coefficientwise triangle inequality and the
    four rows are combined in Hilbert-Schmidt norm.
    """
    _,Q,_,_=channels(dps=dps)
    Q4=np.array([[float(Q[i,j]) for j in range(4)] for i in range(10)])
    ms=np.array(CORE,dtype=float)
    sim=np.array([float(mp.si(m*mp.pi)) for m in CORE])
    den=1.0-(19.0/N)**2
    fac=(2.0/math.pi)/den
    s4=math.sqrt(odd_sum4_tail_bound(N))
    s6=math.sqrt(odd_sum6_tail_bound(N))
    rows=[]
    for j in range(4):
        q=np.abs(Q4[:,j])
        B=float(np.sum(q*np.abs(sim)*ms**2))
        M=float(np.sum(q*ms))
        rows.append(fac*(B*s6+2.0*M*s4))
    return float(math.sqrt(sum(x*x for x in rows)))


def protected_plane(dps: int = 60):
    vals,Q,Lmp,Smp=channels(dps=dps)
    L=np.array([float(x) for x in Lmp])
    S=np.array([float(x) for x in Smp])
    M=np.column_stack([L,S])
    U,s,Vt=np.linalg.svd(M,full_matrices=True)
    protected=U[:,2:]
    cos=float(np.dot(L,S)/(np.linalg.norm(L)*np.linalg.norm(S)))
    return {
        'L':L,
        'S':S,
        'cos_angle':cos,
        'singular_values':s,
        'protected_basis':protected,
        'orthogonality_residual':M.T@protected,
    }


def report():
    r=protected_plane()
    print('prime channel L =', r['L'])
    print('exact cusp channel S =', r['S'])
    print('cos(L,S) =', r['cos_angle'])
    print('singular values [L S] =', r['singular_values'])
    print('protected plane basis columns =')
    print(r['protected_basis'])
    print('channel orthogonality residual =')
    print(r['orthogonality_residual'])
    print('cutoff / active cusp remainder HS bound')
    for N in (237,301,401,501,701,1001):
        print(N, cusp_remainder_hs_bound(N))


if __name__ == '__main__':
    report()
