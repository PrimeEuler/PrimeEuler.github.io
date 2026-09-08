#!/usr/bin/env python3
"""Full remote-tail scale on the numerically resolved protected active line.

This checkpoint continues v13.321.  The 4x3 leading-channel matrix [L,S,T]
(prime, exact cusp, archimedean) has numerical rank three, leaving one active
unit vector p orthogonal to all three leading 1/n channels.

On this line the adverse remote-tail pieces are only the extracted remainders:

* prime remainder: O(n^-2), tail norm O(N^-3/2);
* cusp remainder: O(n^-2), tail norm O(N^-3/2);
* arch remainder: O(n^-3), tail norm O(N^-5/2).

The pole term is globally positive in the even-v sector and is not charged as
an adverse tail penalty.

The script combines conservative analytic remainder bounds with the previously
certified-form tail gap alpha_N.  It compares beta_N^2/alpha_N with the
isolated-core Rayleigh scale of p.  This is not a full Feshbach proof because
the stiff low-core and finite-buffer elimination are not included here.

All displayed decimals are non-interval numerical evaluations.  No positivity,
exact zero mode, lambda_1=0, RH, or GRH conclusion follows.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

from suzuki_arch_channel_and_third_tail_direction import (
    CORE, arch_channel, channel_geometry,
)

PRIME_BOUND=2.044764260347282
QS=(2,3,4,5,7)
WEIGHTS=(
    math.log(2)/math.sqrt(2), math.log(3)/math.sqrt(3), math.log(2)/2,
    math.log(5)/math.sqrt(5), math.log(7)/math.sqrt(7),
)
W=sum(WEIGHTS)


def odd_sum2(N): return 1/N**2+1/(2*N)
def odd_sum4(N): return 1/N**4+1/(6*N**3)
def odd_sum6(N): return 1/N**6+1/(10*N**5)


def tail_gap(N: int) -> float:
    q=2/math.pi
    M4=float(mp.zeta(3))*q**3/(4*(1-q)**3)
    Cr=19/12+4*M4
    arch=Cr*(4/math.pi**2)*odd_sum2(N)
    rank=(2/math.pi**2)*odd_sum2(N)
    c=2/math.pi**3+6/math.pi**4
    alpha=2*c/math.pi
    off=2*alpha*math.sqrt((math.pi**2/12)*odd_sum6(N))
    Cdiag=2/math.pi**2+2/math.pi**3+2/math.pi**4+6/math.pi**5
    diag=Cdiag*math.sqrt(odd_sum4(N))
    cusp=rank+off+diag
    return math.log(N/4)-(math.pi/2+PRIME_BOUND+cusp+arch)


def protected_data(dps: int = 60):
    vals,Q,L,S,T,Hvec=arch_channel(dps=dps)
    g=channel_geometry(dps=dps)
    p=np.array(g['fully_protected_active_vector'],dtype=float)
    Q4=np.array([[float(Q[i,j]) for j in range(4)] for i in range(10)])
    qcoord=Q4@p
    lam=np.array([float(vals[j]) for j in range(4)])
    core_rayleigh=float(np.sum((p*p)*lam))
    return vals,Q,p,qcoord,core_rayleigh,Hvec,g


def prime_remainder_bound(N: int, qcoord: np.ndarray) -> float:
    ms=np.array(CORE,dtype=float)
    A=np.array([
        sum(w*math.sin(m*math.pi*math.log(q)/2) for q,w in zip(QS,WEIGHTS))
        for m in CORE
    ])
    den=1-(19/N)**2
    fac=(4/math.pi)/den
    B=float(np.sum(np.abs(qcoord)*np.abs(A)*ms**2))
    M=float(np.sum(np.abs(qcoord)*ms))*W
    return fac*(B*math.sqrt(odd_sum6(N))+M*math.sqrt(odd_sum4(N)))


def cusp_remainder_bound(N: int, qcoord: np.ndarray) -> float:
    ms=np.array(CORE,dtype=float)
    sim=np.array([float(mp.si(m*mp.pi)) for m in CORE])
    den=1-(19/N)**2
    fac=(2/math.pi)/den
    B=float(np.sum(np.abs(qcoord)*np.abs(sim)*ms**2))
    M=2*float(np.sum(np.abs(qcoord)*ms))
    return fac*(B*math.sqrt(odd_sum6(N))+M*math.sqrt(odd_sum4(N)))


def arch_remainder_bound(N: int, qcoord: np.ndarray, Hvec) -> float:
    ms=np.array(CORE,dtype=float)
    Hv=np.array([float(Hvec[i]) for i in range(10)])
    den=1-(19/N)**2
    fac=(4/math.pi)/den
    C=float(np.sum(np.abs(qcoord)*(np.abs(Hv)*ms**2+ms/math.pi)))
    return fac*C*math.sqrt(odd_sum6(N))


def protected_tail_bound(N: int, dps: int = 60):
    _,_,p,qcoord,core,Hvec,g=protected_data(dps=dps)
    bp=prime_remainder_bound(N,qcoord)
    bc=cusp_remainder_bound(N,qcoord)
    ba=arch_remainder_bound(N,qcoord,Hvec)
    beta=bp+bc+ba
    alpha=tail_gap(N)
    penalty=math.inf if alpha<=0 else beta*beta/alpha
    return {
        'N':N,'alpha':alpha,'prime':bp,'cusp':bc,'arch':ba,
        'beta':beta,'penalty':penalty,'core_rayleigh':core,
        'active_vector':p,'coordinate_vector':qcoord,
        'channel_singular_values':g['channel_singular_values'],
    }


def first_cutoff_below_core(start=151, stop=20001):
    for N in range(start if start%2 else start+1,stop+1,2):
        r=protected_tail_bound(N)
        if r['penalty'] < r['core_rayleigh']:
            return r
    return None


def report():
    base=protected_data()
    print('protected active vector =',base[2])
    print('protected coordinate vector =',base[3])
    print('isolated-core Rayleigh =',base[4])
    for N in (401,501,701,1001,2001,5001,10001):
        r=protected_tail_bound(N)
        print(N,r['alpha'],r['beta'],r['penalty'],r['prime'],r['cusp'],r['arch'])
    print('first odd cutoff with penalty below isolated-core Rayleigh:')
    print(first_cutoff_below_core())


if __name__ == '__main__':
    report()
