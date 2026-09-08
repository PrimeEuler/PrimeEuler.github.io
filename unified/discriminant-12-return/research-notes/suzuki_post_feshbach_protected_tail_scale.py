#!/usr/bin/env python3
"""Remote-tail remainder scale in the post-Feshbach protected directions.

Continues v13.324.  The finite buffer is eliminated first, then the exact
prime/cusp/arch leading 1/n channels are projected into the first effective
near-null directions.  Two cases are compared:

1. the computed 4D protected line annihilating all three leading channels;
2. the 3D quasi-protected direction carrying the smallest nonzero channel
   singular value.

For a low-coordinate vector q_m on m=1,3,...,19, the extracted remainders obey

 prime: O(n^-2),
 cusp:  O(n^-2),
 arch:  O(n^-3).

On the 4D protected line the leading 1/n contribution vanishes numerically by
construction, so the remote-tail norm is bounded only by these remainders.
For the 3D quasi-protected direction the leading-channel residual is retained
explicitly as sigma_min(C_3)*sqrt(sum_{odd n>=N}1/n^2).

The tail gap alpha_N is the same analytic coercive lower bound used in
v13.312--v13.322.  The Schur penalty beta_N^2/alpha_N is compared with the
formal post-Feshbach Rayleigh scales.

All displayed decimals are non-interval numerical evaluations.  In particular
the first three effective eigenvalue signs remain unresolved, and the 4D
protected-line Rayleigh value is a hybrid numerical scale rather than a
certified lower bound.  No exact zero mode, positivity, lambda_1=0, RH, or GRH
conclusion follows.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

from suzuki_post_feshbach_channel_geometry import channel_report, CORE
from suzuki_feshbach_buffer_anatomy import Aseq
from suzuki_arch_channel_and_third_tail_direction import H

QS=(2,3,4,5,7)
WEIGHTS=(
    math.log(2)/math.sqrt(2), math.log(3)/math.sqrt(3), math.log(2)/2,
    math.log(5)/math.sqrt(5), math.log(7)/math.sqrt(7),
)
W=sum(WEIGHTS)
PRIME_BOUND=2.044764260347282


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


def remainder_bounds(N: int, qcoord: np.ndarray, dps: int = 60):
    ms=np.array(CORE,dtype=float)
    Avec=np.array([Aseq(int(m)) for m in CORE],dtype=float)
    Sim=np.array([float(mp.si(int(m)*mp.pi)) for m in CORE],dtype=float)
    Hvec=np.array([float(H(int(m),dps=dps)) for m in CORE],dtype=float)
    den=1-(19/N)**2

    prime=(4/math.pi)/den*(
        float(np.sum(np.abs(qcoord)*np.abs(Avec)*ms**2))*math.sqrt(odd_sum6(N))
        + float(np.sum(np.abs(qcoord)*ms))*W*math.sqrt(odd_sum4(N))
    )
    cusp=(2/math.pi)/den*(
        float(np.sum(np.abs(qcoord)*np.abs(Sim)*ms**2))*math.sqrt(odd_sum6(N))
        + 2*float(np.sum(np.abs(qcoord)*ms))*math.sqrt(odd_sum4(N))
    )
    arch=(4/math.pi)/den*float(np.sum(
        np.abs(qcoord)*(np.abs(Hvec)*ms**2+ms/math.pi)
    ))*math.sqrt(odd_sum6(N))
    return prime,cusp,arch


def direction_data(max_buffer_n: int = 399, arch_order: int = 800,
                   dps: int = 70):
    r=channel_report(max_buffer_n=max_buffer_n,arch_order=arch_order,dps=dps)
    prot=r['rows'][4]
    quasi=r['rows'][3]
    return {
        'protected': {
            'coordinate_vector':np.array(prot['coordinate_vector'],dtype=float),
            'rayleigh':float(prot['formal_effective_rayleigh']),
            'leading_residual':float(np.linalg.norm(prot['channel_residual'])),
        },
        'quasi': {
            'coordinate_vector':np.array(quasi['coordinate_vector'],dtype=float),
            'rayleigh':float(quasi['formal_effective_rayleigh']),
            'leading_residual':float(quasi['channel_residual_norm']),
        },
    }


def bound_for_direction(N: int, info: dict, include_leading: bool = True):
    bp,bc,ba=remainder_bounds(N,info['coordinate_vector'])
    lead=(info['leading_residual']*math.sqrt(odd_sum2(N))) if include_leading else 0.0
    beta=lead+bp+bc+ba
    alpha=tail_gap(N)
    penalty=math.inf if alpha<=0 else beta*beta/alpha
    return {
        'N':N,'alpha':alpha,'leading':lead,'prime':bp,'cusp':bc,'arch':ba,
        'beta':beta,'penalty':penalty,'rayleigh':info['rayleigh'],
    }


def first_protected_crossover(start=151,stop=500001):
    d=direction_data()['protected']
    # By construction the protected line annihilates the three leading
    # channels; do not charge its floating roundoff residual as physical.
    for N in range(start if start%2 else start+1,stop+1,2):
        r=bound_for_direction(N,d,include_leading=False)
        if r['penalty'] < d['rayleigh']:
            return r
    return None


def report():
    d=direction_data()
    print('protected formal Rayleigh =',d['protected']['rayleigh'])
    print('protected numerical channel residual =',d['protected']['leading_residual'])
    print('quasi formal Rayleigh =',d['quasi']['rayleigh'])
    print('quasi leading residual =',d['quasi']['leading_residual'])
    for N in (401,1001,5001,10001,50001,100001,150001):
        rp=bound_for_direction(N,d['protected'],include_leading=False)
        rq=bound_for_direction(N,d['quasi'],include_leading=True)
        print('N',N,'protected',rp)
        print('N',N,'quasi',rq)
    print('first protected crossover =',first_protected_crossover())


if __name__ == '__main__':
    report()
