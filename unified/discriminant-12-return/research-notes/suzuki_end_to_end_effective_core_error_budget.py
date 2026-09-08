#!/usr/bin/env python3
"""End-to-end operator error budget for the finite effective-core certificate.

The goal is a rigorous bound ||F-Fhat|| well below the observed fifth effective
level ~4.3e-8, where

    F=A_CC-A_CB A_BB^{-1} A_BC.

Recommended analytic scalar targets:

  arch finite block operator radius: <=5e-11
  cusp Si/Ci scalar radius:          <=5e-13
  cusp whole-matrix operator radius: <=5e-11 (conservative design target)
  prime whole-matrix operator radius:<=1e-12
  pole whole-matrix operator radius: <=1e-12

Thus use a conservative full finite-matrix operator enclosure

    delta_full <= 1.1e-10.

For block perturbation with gamma>=0.15 and ||C||<=0.8,

 delta_schur_blocks <=
     delta_A
   + (2||C||delta_C+delta_C^2)/(gamma-delta_B)
   + ||C||^2 delta_B/(gamma(gamma-delta_B)).

Taking delta_A=delta_B=delta_C=1.1e-10 gives a block-assembly contribution
of only a few 1e-9.

For the verified solve, if X approximates B^{-1} C^T and
R=C^T-BX, then

    ||B^{-1}C^T-X|| <= ||R||/gamma,
    ||C B^{-1}C^T-CX|| <= ||C|| ||R||/gamma.

With ||R||<=8e-10, gamma>=0.15, ||C||<=0.8, the residual contribution is
<=4.27e-9.

Combining the two leaves a practical total target below about 7e-9, comfortably
inside the basis-free Weyl threshold needed to certify lambda_5(F)>0 from a
nominal lambda_5 near 4.3e-8.

This script records the algebraic budget only; the actual interval arithmetic
still has to instantiate each inequality.
"""

DELTA_FULL=1.1e-10
GAMMA=0.15
C_NORM=0.8
RESIDUAL=8e-10
NOMINAL_LAMBDA5=4.3e-8


def block_error(delta=DELTA_FULL,gamma=GAMMA,c=C_NORM):
    dA=dB=dC=delta
    return dA+(2*c*dC+dC*dC)/(gamma-dB)+(c*c*dB)/(gamma*(gamma-dB))


def solve_error(res=RESIDUAL,gamma=GAMMA,c=C_NORM):
    return c*res/gamma


if __name__=='__main__':
    b=block_error(); s=solve_error(); total=b+s
    print('block assembly contribution=',b)
    print('verified solve contribution=',s)
    print('total design enclosure=',total)
    print('lambda5 margin=',NOMINAL_LAMBDA5-total)
