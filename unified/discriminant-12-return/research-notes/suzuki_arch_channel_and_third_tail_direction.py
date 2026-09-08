#!/usr/bin/env python3
"""Archimedean active-tail channel audit for Suzuki a=1 even-v sector.

Continuing v13.320, write h(t)=r''(t), where

    h(t)=exp(-t/2)/(1-exp(-2t))-1/(2t),  h(0)=1/4.

For odd Dirichlet modes and m != n,

    K_arch(m,n)=-(4/pi) [n H_m-m H_n]/(n^2-m^2),
    H_j=int_0^2 h(t) sin(j*pi*t/2) dt.

Thus for fixed m,

    K_arch(m,n)=-(4/pi) H_m/n + R_arch(m,n).

Since h is positive and decreasing on [0,2], integration by parts gives for
odd n

    |H_n| <= 1/(pi n).

Consequently

    |R_arch(m,n)| <= (4/pi)/(1-m^2/n^2)
        [ |H_m| m^2/n^3 + m/(pi n^3) ],

so after extracting the active channel T the arch remainder is O(n^-3), with
Hilbert-Schmidt tail O(N^-5/2).

The script compares the active arch channel T with the prime/cusp channels
L,S from v13.320.  Numerically T lies very close to span{L,S}, but has a small
nonzero transverse component, so [L,S,T] has rank three and leaves one active
combination orthogonal to all three leading 1/n channels.

All displayed decimals are ordinary high-precision/floating evaluations, not
interval enclosures.  No exact zero mode, positivity, lambda_1=0, RH, or GRH
claim follows.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

from suzuki_exact_cusp_channel_protected_plane import (
    CORE, channels, high_precision_active_basis,
)


def h(t):
    t=mp.mpf(t)
    if t == 0:
        return mp.mpf(1)/4
    return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)


def H(m: int, dps: int = 60):
    with mp.workdps(dps):
        return mp.quad(lambda t: h(t)*mp.sin(m*mp.pi*t/2), [0,2])


def arch_channel(dps: int = 60):
    vals,Q=high_precision_active_basis(dps=dps)
    with mp.workdps(dps):
        Hvec=mp.matrix([H(m,dps=dps) for m in CORE])
        Tcoord=(-4/mp.pi)*Hvec
        T=[(Q[:,j].T*Tcoord)[0] for j in range(4)]
    _,_,L,S=channels(dps=dps)
    return vals,Q,L,S,T,Hvec


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0/N**6 + 1.0/(10.0*N**5)


def arch_remainder_hs_bound(N: int, dps: int = 60) -> float:
    _,Q,_,_,_,Hvec=arch_channel(dps=dps)
    Q4=np.array([[float(Q[i,j]) for j in range(4)] for i in range(10)])
    ms=np.array(CORE,dtype=float)
    Hv=np.array([float(Hvec[i]) for i in range(10)])
    den=1.0-(19.0/N)**2
    fac=(4.0/math.pi)/den
    s6=math.sqrt(odd_sum6_tail_bound(N))
    rows=[]
    for j in range(4):
        q=np.abs(Q4[:,j])
        coeff=float(np.sum(q*(np.abs(Hv)*ms**2 + ms/math.pi)))
        rows.append(fac*coeff*s6)
    return float(math.sqrt(sum(x*x for x in rows)))


def channel_geometry(dps: int = 60):
    _,_,Lmp,Smp,Tmp,_=arch_channel(dps=dps)
    L=np.array([float(x) for x in Lmp])
    S=np.array([float(x) for x in Smp])
    T=np.array([float(x) for x in Tmp])
    LS=np.column_stack([L,S])
    coef,_,_,_=np.linalg.lstsq(LS,T,rcond=None)
    residual=T-LS@coef
    M=np.column_stack([L,S,T])
    U,s,Vt=np.linalg.svd(M,full_matrices=True)
    return {
        'L':L,'S':S,'T':T,
        'T_projection_coefficients':coef,
        'T_transverse_norm':float(np.linalg.norm(residual)),
        'T_relative_transverse':float(np.linalg.norm(residual)/np.linalg.norm(T)),
        'channel_singular_values':s,
        'fully_protected_active_vector':U[:,3],
        'orthogonality_residual':M.T@U[:,3],
    }


def report():
    r=channel_geometry()
    print('L =',r['L'])
    print('S =',r['S'])
    print('T =',r['T'])
    print('T projection coefficients on [L,S] =',r['T_projection_coefficients'])
    print('T transverse norm =',r['T_transverse_norm'])
    print('T relative transverse =',r['T_relative_transverse'])
    print('singular values [L S T] =',r['channel_singular_values'])
    print('fully protected active vector =',r['fully_protected_active_vector'])
    print('orthogonality residual =',r['orthogonality_residual'])
    print('cutoff / arch remainder 4D HS bound')
    for N in (237,301,401,501,701,1001):
        print(N,arch_remainder_hs_bound(N))


if __name__ == '__main__':
    report()
