#!/usr/bin/env python3
"""Analytic perturbation budget for the frozen-8D normalized tail residual map.

This recovers the historical ||Delta Y||<7e-7 scale from already-audited
operator inputs rather than taking 7e-7 as a transcript constant.

Let
  R = A_TC - A_TF A_FF^{-1} A_FC,
  Y = R Q8 L0^{-T}.

Use
  ||Delta A|| <= eps_A = 2e-13             (v13.357 source envelope),
  A_FF >= mu I, mu=0.53                    (v13.434),
  ||A_TF|| < 1.015                          (v13.443),
  ||A_FC|| < 5.15                           (conservative component bound),
and the exact-dyadic frozen L0.

The inverse of L0 is formed exactly with Fraction arithmetic; its Frobenius
norm is an upper bound for ||L0^{-1}||_2.  A separate finite-solve residual
charge is included in the historical unnormalized-Q solve convention.

This closes only the analytic perturbation budget.  The nominal residual Gram
still needs its own outward replay before theorem promotion.
"""
from fractions import Fraction
from math import sqrt

from suzuki_odd_M4000_frozen_dyadic_Q8_L0 import L0_HEX

EPS_A=2.0e-13
MU=0.53
TF=1.015
FC=5.15
SOLVE_RESIDUAL=1.0e-12
FORMATION_ALLOWANCE=5.0e-8
TARGET=7.0e-7


def Fhex(x):
    n,d=float.fromhex(x).as_integer_ratio()
    return Fraction(n,d)


def inverse_exact_lower_triangular():
    L=[[Fhex(x) for x in row] for row in L0_HEX]
    n=len(L)
    X=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    for col in range(n):
        for i in range(n):
            rhs=Fraction(1 if i==col else 0)
            rhs-=sum(L[i][k]*X[k][col] for k in range(i))
            X[i][col]=rhs/L[i][i]
    return X


def report():
    X=inverse_exact_lower_triangular()
    fro2=sum(v*v for row in X for v in row)
    linv_fro=sqrt(float(fro2))
    assert linv_fro < 77409.0

    # Resolvent perturbation for R=A_TC-A_TF F^{-1}A_FC.
    # The nominal inverse uses ||Fhat^{-1}|| <= 1/(mu-eps).
    r_source=(EPS_A
              + EPS_A*FC/MU
              + TF*EPS_A*FC/(MU*(MU-EPS_A))
              + TF*EPS_A/(MU-EPS_A))
    y_source=r_source*77409.0

    # Historical solver forms the unnormalized Q8 finite solve first, then
    # applies L0^{-T}; propagate an outward 1e-12 solve residual accordingly.
    y_solve=(TF/MU)*SOLVE_RESIDUAL*77409.0
    total=y_source+y_solve+FORMATION_ALLOWANCE

    print('exact ||L0^{-1}||_F upper proxy =',linv_fro)
    print('residual-map source perturbation before normalization <',r_source)
    print('normalized source perturbation <',y_source)
    print('normalized solve perturbation <',y_solve)
    print('formation allowance =',FORMATION_ALLOWANCE)
    print('total normalized residual-map perturbation <',total)
    print('target =',TARGET)

    assert r_source < 6.249e-12
    assert y_source < 4.837e-7
    assert y_solve < 1.483e-7
    assert total < TARGET
    print('PASS: historical ||Delta Y||<7e-7 cap is recovered analytically')
    print('GUARDRAIL: nominal H Gram/far-tail outward replay remains separate')


if __name__=='__main__':
    report()
