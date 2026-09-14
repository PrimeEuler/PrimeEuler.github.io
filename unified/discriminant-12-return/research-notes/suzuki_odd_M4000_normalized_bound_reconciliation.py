#!/usr/bin/env python3
"""Reconcile the historical frozen-8D C/H scalar bounds.

This helper separates exact algebra/audited source budgets from the two pieces
that still require independent outward replay.  It does NOT promote the odd
index theorem by itself.

Closed/re-derived here:
  * exact-dyadic Gershgorin floor for L0 L0^T;
  * finite-Schur source perturbation formula from eps_A, ||A_CF|| and mu_F;
  * solve-residual propagation formula;
  * historical C scalar arithmetic;
  * historical H terminal scalar arithmetic.

Still external inputs:
  * a proof-grade frozen-nominal lower mismatch allowance;
  * proof-grade explicit residual-Gram and normalized residual-operator error.
"""
from fractions import Fraction
from math import sqrt

from suzuki_odd_M4000_frozen_dyadic_Q8_L0 import L0_HEX

EPS_A=2.0e-13          # audited v13.357 exact-vs-high-precision nominal target
MU_F=0.53              # closed v13.434
CF_BOUND=5.15
SOLVE_RESIDUAL=1.0e-12
SCHUR_FORMATION=1.0e-15

# Historical transcript charges retained only as comparison targets.
H_EXPLICIT_HIST=0.22441479153402388
H_TAIL_HIST=0.000482
Y_ERROR_HIST=7.0e-7


def Fhex(x):
    n,d=float.fromhex(x).as_integer_ratio()
    return Fraction(n,d)


def exact_l0_gershgorin_floor():
    L=[[Fhex(x) for x in row] for row in L0_HEX]
    n=len(L)
    G=[[sum(L[i][k]*L[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    floors=[]
    for i in range(n):
        floors.append(G[i][i]-sum(abs(G[i][j]) for j in range(n) if j!=i))
    return min(floors)


def schur_source_error(eps=EPS_A,b=CF_BOUND,mu=MU_F):
    # Exact and nominal blocks differ by <=eps in operator norm.  Use
    # ||F_exact^{-1}||<=1/mu and ||F_nom^{-1}||<=1/(mu-eps), together with
    # the resolvent identity for the inverse perturbation.
    return (eps
            + eps*b/mu
            + b*(eps/(mu*(mu-eps)))*b
            + b*eps/(mu-eps))


def report():
    floor=exact_l0_gershgorin_floor()
    es=schur_source_error()
    solve=CF_BOUND/MU_F*SOLVE_RESIDUAL
    finite=es+solve+SCHUR_FORMATION

    # The old verifier used 2e-8 here.  Keep it only as a comparison target;
    # the independent replay must justify whichever final frozen-nominal loss
    # is used for theorem promotion.
    old_precond_loss=2.0e-8
    c_old=1.0-finite/float(floor)-old_precond_loss

    hbase=H_EXPLICIT_HIST+H_TAIL_HIST
    hout=hbase+2.0*sqrt(hbase)*Y_ERROR_HIST+Y_ERROR_HIST**2

    print('exact Gershgorin floor lambda_min(L0 L0^T) >',float(floor))
    print('source Schur perturbation <',es)
    print('solve Schur perturbation <',solve)
    print('total finite Schur error <',finite)
    print('historical-comparison C lower raw =',c_old)
    print('historical H outward raw =',hout)
    print('guardrail: old preconditioner/Y/Gram charges remain replay targets')

    assert float(floor)>1.6689e-10
    assert es<2.298e-11
    assert finite<3.269e-11
    assert c_old>0.804
    assert hout<0.225


if __name__=='__main__':
    report()
