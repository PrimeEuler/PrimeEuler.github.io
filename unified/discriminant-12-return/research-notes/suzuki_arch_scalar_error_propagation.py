#!/usr/bin/env python3
"""Error propagation from scalar archimedean sequences to the finite matrix.

For odd m != n,

  K_mn=-(4/pi)(n H_m-m H_n)/(n^2-m^2).

If every H_j has enclosure radius eps_H, then

  |delta K_mn| <= (4/pi)(n+m) eps_H/|n^2-m^2|
                 = (4/pi) eps_H/|n-m|
                 <= (2/pi) eps_H,

because distinct odd modes satisfy |n-m|>=2.

Diagonal entries are represented independently by D_n.  Thus if both H_n and
D_n are known to radius eps, every arch-matrix entry is known to radius at most
eps (since 2/pi<1).  For a d x d symmetric matrix the crude operator bound is
||E||_2 <= d eps.

At N=155 there are d=77 odd finite modes.  eps=1e-11 therefore gives a global
arch-block operator enclosure <=7.7e-10.
"""
import math

DIM=77
EPS=1e-11
OFFDIAG_FACTOR=2/math.pi
GLOBAL_OPERATOR_BOUND=DIM*EPS

if __name__=='__main__':
    print('offdiag scalar-error factor <=',OFFDIAG_FACTOR)
    print('77x77 arch operator error <=',GLOBAL_OPERATOR_BOUND)
