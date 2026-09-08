#!/usr/bin/env python3
"""Explicit error budget for certifying the N=155 finite Suzuki Schur reduction.

For F=A-C B^{-1} C^T with B >= gamma I, suppose interval/verified approximants
satisfy operator errors

    ||dA|| <= da, ||dB|| <= db, ||dC|| <= dc,

with db < gamma.  Then

 ||Ftilde-F|| <= da
   + (2||C|| dc + dc^2)/(gamma-db)
   + ||C||^2 db/[gamma(gamma-db)].

The last term follows from the resolvent identity
Btilde^{-1}-B^{-1}=-B^{-1} dB Btilde^{-1}.

This script records design tolerances for the v13.332 two-precision strategy.
The numerical constants are targeting data, not interval-certified facts.
"""
from __future__ import annotations

GAMMA_BUFFER = 0.23848      # pole-free numerical gap target from v13.331
C_NORM_BOUND = 0.76          # conservative core-buffer norm target
STIFF_GAP = 4.33e-8          # fifth effective scale from v13.332
BUFFER_DIM = 67
STIFF_DIM = 6


def schur_error(da: float, db: float, dc: float,
                gamma: float = GAMMA_BUFFER,
                cnorm: float = C_NORM_BOUND) -> float:
    if db >= gamma:
        return float('inf')
    return (da
            + (2*cnorm*dc + dc*dc)/(gamma-db)
            + cnorm*cnorm*db/(gamma*(gamma-db)))


def entrywise_half_gap_targets():
    # ||E||_2 <= d * max_ij |E_ij|
    buffer_entry = GAMMA_BUFFER/(2*BUFFER_DIM)
    stiff_entry = STIFF_GAP/(2*STIFF_DIM)
    return buffer_entry, stiff_entry


def report():
    eb, es = entrywise_half_gap_targets()
    print('buffer entrywise half-gap target =', eb)
    print('stiff 6D entrywise half-gap target =', es)
    print('example Schur budgets:')
    for db in (1e-4,1e-6,1e-8,1e-10):
        print('db',db,'with da=dc=1e-10 ->',schur_error(1e-10,db,1e-10))
    print('guardrail: design tolerances only; final proof requires outward enclosures')


if __name__ == '__main__':
    report()
