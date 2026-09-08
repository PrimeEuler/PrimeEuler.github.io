#!/usr/bin/env python3
"""Scalar-sequence reconstruction of the finite archimedean matrix.

For odd m != n,

  Karch_mn = -(4/pi) (n H_m - m H_n)/(n^2-m^2),
  H_j = int_0^2 h(t) sin(j*pi*t/2) dt.

Thus all off-diagonal entries are determined by the scalar sequence H_j.
For diagonal n,

  D_n = -int_0^2 h(t)[(2-t)cos(k_n t)+sin(k_n t)/k_n]dt.

At the N=155 finite scale there are 77 odd modes <=153, so the complete
77x77 smooth archimedean block is determined by 77 H-values plus 77 diagonal
D-values: 154 scalar integrals total.

The pole term is separately exact rank one with
c_n = 2 k_n cosh(1/2)/(k_n^2+1/4).
"""
from __future__ import annotations
import math

MODES=tuple(range(1,154,2))


def offdiag_from_H(m:int,n:int,Hm:float,Hn:float)->float:
    return -(4/math.pi)*(n*Hm-m*Hn)/(n*n-m*m)


def pole_c(n:int)->float:
    k=n*math.pi/2
    return 2*k*math.cosh(0.5)/(k*k+0.25)


if __name__=='__main__':
    print('odd finite modes =',len(MODES))
    print('scalar arch integrals required =',2*len(MODES))
    print('pairwise symmetric entries avoided =',len(MODES)*(len(MODES)+1)//2-2*len(MODES))
