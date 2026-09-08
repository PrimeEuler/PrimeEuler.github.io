#!/usr/bin/env python3
"""Joint prime+cusp remote-tail bound on the post-Feshbach protected line.

Continues v13.325.  The key improvement is to project the prime and cusp
remainders onto the protected low-coordinate vector before taking absolute
values.  This preserves the signed first moment

    M = sum_m m q_m,

which is numerically small on the computed post-Feshbach protected line.

For odd n>N>19, after the leading 1/n channels have been annihilated, the
projected prime+cusp remainder can be bounded by

  |M| * (4/pi)(W+1) / n^2

plus n^-3 and n^-4 correction terms.  Consequently

  ||r_{p+c}||_{ell^2(n>=N)}
   <= |M|(4/pi)(W+1) sqrt(S4)
      + [(4/pi)Bp+(2/pi)Bc]/d_N * sqrt(S6)
      + [4(W+1)M3/(pi d_N)] * sqrt(S8),

where

  Bp = sum |q_m A_m| m^2,
  Bc = sum |q_m Si(m pi)| m^2,
  M3 = sum |q_m| m^3,
  d_N = 1-(19/N)^2,

and S4,S6,S8 are elementary odd-tail zeta bounds.

The archimedean remainder is then added using the v13.321 O(N^-5/2) bound.
The resulting Schur penalty is compared with the formal post-Feshbach
protected-line Rayleigh scale.

All decimals are non-interval numerical evaluations.  The protected line and
its Rayleigh scale remain hybrid numerical quantities.  This is not a proof of
positivity, an exact zero mode, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

from suzuki_post_feshbach_protected_tail_scale import (
    direction_data, tail_gap, odd_sum6,
)
from suzuki_feshbach_buffer_anatomy import Aseq
from suzuki_arch_channel_and_third_tail_direction import H
from suzuki_post_feshbach_channel_geometry import CORE

QS=(2,3,4,5,7)
WEIGHTS=(
    math.log(2)/math.sqrt(2), math.log(3)/math.sqrt(3), math.log(2)/2,
    math.log(5)/math.sqrt(5), math.log(7)/math.sqrt(7),
)
W=sum(WEIGHTS)


def S4(N): return 1/N**4 + 1/(6*N**3)
def S6(N): return 1/N**6 + 1/(10*N**5)
def S8(N): return 1/N**8 + 1/(14*N**7)


def joint_prime_cusp_bound(N: int, qcoord: np.ndarray):
    ms=np.array(CORE,dtype=float)
    Avec=np.array([Aseq(int(m)) for m in CORE],dtype=float)
    Sim=np.array([float(mp.si(int(m)*mp.pi)) for m in CORE],dtype=float)
    d=1-(19/N)**2

    M=float(np.dot(qcoord,ms))
    Bp=float(np.sum(np.abs(qcoord*Avec)*ms**2))
    Bc=float(np.sum(np.abs(qcoord*Sim)*ms**2))
    M3=float(np.sum(np.abs(qcoord)*ms**3))

    lead=abs(M)*(4/math.pi)*(W+1)*math.sqrt(S4(N))
    cubic=((4/math.pi)*Bp+(2/math.pi)*Bc)/d*math.sqrt(S6(N))
    quartic=(4/math.pi)*(W+1)*M3/d*math.sqrt(S8(N))
    return {
        'M':M,'Bp':Bp,'Bc':Bc,'M3':M3,
        'lead_n2':lead,'n3':cubic,'n4':quartic,
        'joint_bound':lead+cubic+quartic,
    }


def arch_bound(N: int, qcoord: np.ndarray, dps: int = 60):
    ms=np.array(CORE,dtype=float)
    Hvec=np.array([float(H(int(m),dps=dps)) for m in CORE],dtype=float)
    d=1-(19/N)**2
    coeff=float(np.sum(np.abs(qcoord)*(np.abs(Hvec)*ms**2+ms/math.pi)))
    return (4/math.pi)/d*coeff*math.sqrt(S6(N))


def protected_bound(N: int):
    info=direction_data()['protected']
    q=np.array(info['coordinate_vector'],dtype=float)
    j=joint_prime_cusp_bound(N,q)
    a=arch_bound(N,q)
    beta=j['joint_bound']+a
    alpha=tail_gap(N)
    penalty=math.inf if alpha<=0 else beta*beta/alpha
    return {
        'N':N,'alpha':alpha,'beta':beta,'penalty':penalty,
        'rayleigh':info['rayleigh'],'arch':a,**j,
    }


def first_crossover(start=151,stop=200001):
    for N in range(start if start%2 else start+1,stop+1,2):
        r=protected_bound(N)
        if r['penalty'] < r['rayleigh']:
            return r
    return None


def report():
    base=protected_bound(5001)
    print('protected signed first moment M =',base['M'])
    print('Bp Bc M3 =',base['Bp'],base['Bc'],base['M3'])
    for N in (1001,2001,3001,3149,4001,5001,10001):
        print(protected_bound(N))
    print('first crossover =',first_crossover())


if __name__ == '__main__':
    report()
