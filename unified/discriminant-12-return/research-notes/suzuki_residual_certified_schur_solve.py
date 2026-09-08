#!/usr/bin/env python3
"""Residual-certified Schur solve for the N=155 finite reduction.

Let X*=B^{-1} C^T and let X be a numerical approximate solve.  With
R=C^T-BX and B>=gamma I,

    ||X*-X|| <= ||R||/gamma,

and therefore

    ||C B^{-1} C^T - C X|| <= ||C|| ||R||/gamma.

This avoids constructing an interval inverse of the 67x67 buffer block.
"""
from __future__ import annotations

GAMMA=0.23848
C_NORM=0.76


def schur_error_from_residual(residual_norm: float) -> float:
    return C_NORM*residual_norm/GAMMA


def residual_target(schur_target: float) -> float:
    return schur_target*GAMMA/C_NORM


if __name__=='__main__':
    print('amplification ||C||/gamma =',C_NORM/GAMMA)
    for target in (1e-6,1e-9,1e-12,1e-15):
        print('Schur target',target,'requires residual <=',residual_target(target))
    print('guardrail: B,C and residual must themselves be outward-enclosed')
