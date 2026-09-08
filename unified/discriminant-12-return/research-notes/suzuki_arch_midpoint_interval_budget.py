#!/usr/bin/env python3
"""Uniform midpoint-rule budget for archimedean entries on modes <=153.

For f_mn(t)=h(t) S_mn(t), t in [0,2], use

  |S_mn| <= 2,
  |S'_mn| <= 2 kmax,
  |S''_mn| <= 2 kmax^2,

with kmax=153*pi/2.  From the v13.311-v13.312 arch analysis,

  0<h<=1/4,
  |h'|<=1/48,
  |h''|<=M4,

where M4<=1.616 is a convenient rounded majorant.
Thus

 |f''| <= 2 M4 + kmax/12 + kmax^2/2.

Composite midpoint on [0,2] with N equal panels obeys

 |E_N| <= (2^3)/(24 N^2) sup|f''| = sup|f''|/(3N^2).

This is intentionally crude but sufficient for the coarse buffer certificate.
"""
from __future__ import annotations
import math

KMAX=153*math.pi/2
M4=1.616
F2=2*M4+KMAX/12+KMAX*KMAX/2


def midpoint_error(N: int) -> float:
    return F2/(3*N*N)


def panels_for(tol: float) -> int:
    return math.ceil(math.sqrt(F2/(3*tol)))


if __name__=='__main__':
    print('kmax =',KMAX)
    print('sup |f second| bound =',F2)
    for tol in (1e-2,2e-3,1e-3,5e-4,1e-4):
        N=panels_for(tol)
        print(tol,N,midpoint_error(N))
    print('guardrail: interval implementation must outward-round point evaluations')
