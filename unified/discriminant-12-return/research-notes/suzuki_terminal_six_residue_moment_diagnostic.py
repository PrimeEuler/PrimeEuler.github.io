#!/usr/bin/env python3
"""Numerical structural diagnostic for the six unresolved Suzuki directions.

This script uses only the already-frozen exact-dyadic positive subspaces:
  * even-v core {1,3,...,19}: frozen 10x6 Q, unresolved complement dimension 4;
  * odd-v core  {2,4,...,20}: frozen 10x8 Q8, unresolved complement dimension 2.

It asks whether the unresolved complements look like low-order polynomial moments
or like mod-12 / unit-core residue channels.  The complements themselves are
constructed numerically by SVD, so all outputs here are diagnostic only.

No exact kernel, sign, RH, or GRH claim follows.
"""
from __future__ import annotations

import math
import numpy as np

from suzuki_M3999_frozen_dyadic_Q_L0 import Q_HEX as EVEN_Q_HEX
from suzuki_odd_M4000_frozen_dyadic_Q8_L0 import Q_HEX as ODD_Q_HEX


def fmat(H):
    return np.array([[float.fromhex(x) for x in row] for row in H], dtype=float)


def complement(Q):
    # Columns of N span ker(Q^T).  Frozen Q is numerically nearly orthonormal.
    _, _, vh = np.linalg.svd(Q.T, full_matrices=True)
    return vh[Q.shape[1]:].T


def unitcore(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n % 12


def chi12(n: int) -> int:
    r=n%12
    return 1 if r in (1,11) else (-1 if r in (5,7) else 0)


def chi4(n: int) -> int:
    return 1 if n%4==1 else (-1 if n%4==3 else 0)


def chi3(n: int) -> int:
    return 1 if n%3==1 else (-1 if n%3==2 else 0)


def unresolved_fraction(N, v):
    v=np.asarray(v,dtype=float)
    nv=np.linalg.norm(v)
    if nv == 0: return 0.0
    return float(np.linalg.norm(N.T@(v/nv)))


def report():
    Q=fmat(EVEN_Q_HEX)
    Q8=fmat(ODD_Q_HEX)
    Ne=complement(Q)
    No=complement(Q8)
    me=np.arange(1,20,2,dtype=int)
    mo=np.arange(2,21,2,dtype=int)

    print('even unresolved dimension =',Ne.shape[1])
    for p in range(6):
        print(f'even unresolved fraction n^{p} =',unresolved_fraction(Ne,me.astype(float)**p))
    for name,f in [('chi12',chi12),('chi_-4',chi4),('chi_-3',chi3),
                   ('unit-indicator',lambda n: int(math.gcd(n,6)==1)),
                   ('3-divisible',lambda n: int(n%3==0))]:
        print('even unresolved fraction',name,'=',unresolved_fraction(Ne,[f(int(n)) for n in me]))

    # Four unit residue channels on the even-v odd-index core.
    R=np.column_stack([(me%12==r).astype(float) for r in (1,5,7,11)])
    V,_=np.linalg.qr(R)
    pc=np.linalg.svd(Ne.T@V,compute_uv=False)
    print('even principal cosines vs unit residue span {1,5,7,11} =',pc)

    print('odd unresolved dimension =',No.shape[1])
    for p in range(6):
        print(f'odd unresolved fraction n^{p} =',unresolved_fraction(No,mo.astype(float)**p))
    for r in (1,5,7,11):
        print('odd unresolved fraction unit-core',r,'=',
              unresolved_fraction(No,[int(unitcore(int(n))==r) for n in mo]))
    print('odd unit cores in core =',[(int(n),unitcore(int(n))) for n in mo])

    # Broad regression guards for the qualitative pattern.
    assert unresolved_fraction(Ne,me.astype(float)) < 0.004
    assert unresolved_fraction(No,mo.astype(float)) < 0.001
    assert pc[0] > 0.93 and pc[1] > 0.70 and pc[2] > 0.69 and pc[3] < 0.25
    print('GUARDRAIL: numerical structural diagnostic only; no theorem promotion')


if __name__=='__main__':
    report()
