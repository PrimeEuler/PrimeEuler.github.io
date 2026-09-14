#!/usr/bin/env python3
"""High-precision cutoff evolution of the first four even-v Suzuki eigenvectors.

This diagnostic extends ``suzuki_even_small_cutoff_highprecision_spectrum.py``.
For M=29,39,49,59,69 it diagonalizes the full source-faithful even-v finite
matrix at high precision, then studies only the first four eigenvectors.

Questions:
  * Are the tiny-eigenvalue vectors actually low-core objects?
  * Does their 4D low-core span stabilize with cutoff?
  * Does the stabilized span reproduce the frozen M=3999 unresolved complement?
  * Is the previously observed mod-12 residue profile stable independently of
    the frozen basis?

All subspace/overlap diagnostics are ordinary-double reductions of
high-precision eigenvectors.  This is diagnostic only: no exact kernel,
infinite-operator sign, RH, or GRH claim follows.
"""
from __future__ import annotations

import numpy as np
import mpmath as mp

from suzuki_even_small_cutoff_highprecision_spectrum import build
from suzuki_M3999_frozen_dyadic_Q_L0 import Q_HEX as FROZEN_Q_HEX

CUTOFFS=(29,39,49,59,69)
CORE=np.arange(1,20,2,dtype=int)


def frozen_complement():
    Q=np.array([[float.fromhex(x) for x in row] for row in FROZEN_Q_HEX],dtype=float)
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True)
    return vh[Q.shape[1]:].T


def unit_residue_basis():
    R=np.column_stack([(CORE%12==r).astype(float) for r in (1,5,7,11)])
    Q,_=np.linalg.qr(R)
    return Q


def low_fourplane(stop:int,dps:int=70):
    A=build(stop,dps)
    ev,E=mp.eigsy(A)
    V=np.array([[float(E[r,c]) for c in range(4)] for r in range(E.rows)],dtype=float)
    low=V[:10,:]
    U,_=np.linalg.qr(low)
    masses=np.array([np.linalg.norm(low[:,j]) for j in range(4)])
    vals=[ev[j] for j in range(4)]
    return vals,U,masses


def residue_exceptional(U,Rq):
    # smallest principal-cosine direction of U relative to the four unit-residue indicators
    left,s,_=np.linalg.svd(U.T@Rq)
    x=U@left[:,-1]
    x/=np.linalg.norm(x)
    return s,x


def report():
    Rq=unit_residue_basis()
    frozen=frozen_complement()
    prevU=None
    prevx=None
    lastU=None
    lastx=None

    for M in CUTOFFS:
        vals,U,masses=low_fourplane(M,70)
        s,x=residue_exceptional(U,Rq)
        print('M =',M)
        print('  lambda1..4 =',[mp.nstr(v,12) for v in vals])
        print('  low-core masses =',masses)
        print('  unit-residue principal cosines =',s)
        print('  exceptional |n=3 amplitude| =',abs(x[1]))
        if prevU is not None:
            ps=np.linalg.svd(prevU.T@U,compute_uv=False)
            print('  principal cosines vs previous four-plane =',ps)
            print('  exceptional overlap vs previous =',abs(prevx@x))
        prevU,prevx=U,x
        lastU,lastx=U,x

    pf=np.linalg.svd(frozen.T@lastU,compute_uv=False)
    sf,xf=residue_exceptional(frozen,Rq)
    print('M=69 principal cosines vs frozen M=3999 unresolved complement =',pf)
    print('frozen unit-residue principal cosines =',sf)
    print('M=69 exceptional overlap with frozen exceptional =',abs(lastx@xf))
    print('frozen exceptional |n=3 amplitude| =',abs(xf[1]))

    # broad qualitative guards only
    assert min(pf) > 0.999998
    assert abs(lastx@xf) > 0.999999
    assert abs(xf[1]) > 0.94
    assert min(masses) > 0.99999
    print('GUARDRAIL: high-precision finite-cutoff structural diagnostic only')


if __name__=='__main__':
    report()
