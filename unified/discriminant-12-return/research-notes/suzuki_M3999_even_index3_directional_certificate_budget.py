#!/usr/bin/env python3
"""Fail-closed budget for a possible even-sector index<=3 strengthening.

The frozen M3999 unresolved four-plane contains one midpoint direction v_* with
finite Schur Rayleigh value about 1.34627e-12.  The M3999 residual-Gram replay
shows that its infinite-tail residual norm is only about 3.48e-7.

This script records deliberately rounded targets which, *if independently
outward-certified*, imply that this one direction stays positive for the exact
source-faithful infinite operator.

No theorem is promoted by this file.  The two nominal inequalities

    s_F,nom(v_*) > 1.34e-12
    ||R_nom v_*||^2 < 1.23e-13

are currently midpoint/certification targets.  All remaining inequalities in
this file are analytic consequences of already-certified source/high-block
bounds plus elementary perturbation estimates.
"""
from __future__ import annotations
import math

# Certification targets from the M3999 replay.
NOMINAL_FINITE_RAYLEIGH_LOWER_TARGET = 1.34e-12
NOMINAL_RESIDUAL_GRAM_UPPER_TARGET = 1.23e-13
NOMINAL_FINITE_SOLVE_NORM_UPPER = 0.0040
NOMINAL_FC_DIRECTION_NORM_UPPER = 0.00425

# Previously certified/operator-level inputs.
SOURCE_OPERATOR_ERROR = 2.0e-13
FINITE_HIGH_FLOOR_EXACT = 0.22
EFFECTIVE_TAIL_FLOOR_EXACT = 0.18225976374175623

# Crude source-faithful F->T cross norm for F=21..3999, T>=4001.
# With |Z_n|<8,
#   |A0_mn| <= (16/pi)/(n-m),  n>m,
# and the cross Frobenius square is bounded by the harmonic sums below.
R = 1990
H1 = sum(1.0/r for r in range(1,R+1))
H2 = sum(1.0/(r*r) for r in range(1,R+1))
POLEFREE_CROSS_FROB = (16.0/math.pi)*math.sqrt(0.25*(H1+H2))
K_C = 4.0*math.cosh(0.5)/math.pi
SUM_F_INV2 = sum(1.0/(n*n) for n in range(21,4000,2))
SUM_T_INV2_UPPER = 1.0/4001.0**2 + 1.0/(2.0*4001.0)
POLE_CROSS_NORM = 2.0*K_C*K_C*math.sqrt(SUM_F_INV2*SUM_T_INV2_UPPER)
CROSS_NORM_UPPER = POLEFREE_CROSS_FROB + POLE_CROSS_NORM

EPS = SOURCE_OPERATOR_ERROR

# Finite Schur directional perturbation.
# Exact A >= nominal A - eps I.  The nominal finite-high block has floor at
# least 0.22-eps because the exact finite-high block has floor 0.22.
MU_NOM = FINITE_HIGH_FLOOR_EXACT - EPS
FINITE_SOURCE_COST = (
    EPS
    + EPS*NOMINAL_FC_DIRECTION_NORM_UPPER**2/(MU_NOM*(MU_NOM-EPS))
)
EXACT_FINITE_RAYLEIGH_LOWER = (
    NOMINAL_FINITE_RAYLEIGH_LOWER_TARGET - FINITE_SOURCE_COST
)

# Exact-vs-nominal finite-solve vector.
DX_UPPER = (
    EPS*math.sqrt(1.0+NOMINAL_FINITE_SOLVE_NORM_UPPER**2)
    / FINITE_HIGH_FLOOR_EXACT
)

# Residual perturbation:
#   Delta r = E_T,[C,F](v,-x_nom) - (A_TF+E_TF) Delta x.
RESIDUAL_VECTOR_PERTURB_UPPER = (
    EPS*math.sqrt(1.0+NOMINAL_FINITE_SOLVE_NORM_UPPER**2)
    +(CROSS_NORM_UPPER+EPS)*DX_UPPER
)

NOMINAL_RESIDUAL_NORM_UPPER = math.sqrt(NOMINAL_RESIDUAL_GRAM_UPPER_TARGET)
EXACT_RESIDUAL_NORM_UPPER = (
    NOMINAL_RESIDUAL_NORM_UPPER + RESIDUAL_VECTOR_PERTURB_UPPER
)
EXACT_RESIDUAL_GRAM_UPPER = EXACT_RESIDUAL_NORM_UPPER**2
EXACT_TAIL_SELF_ENERGY_UPPER = (
    EXACT_RESIDUAL_GRAM_UPPER/EFFECTIVE_TAIL_FLOOR_EXACT
)

FINAL_DIRECTIONAL_MARGIN_LOWER = (
    EXACT_FINITE_RAYLEIGH_LOWER - EXACT_TAIL_SELF_ENERGY_UPPER
)

if __name__ == '__main__':
    print('pole-free crude cross Frobenius <',POLEFREE_CROSS_FROB)
    print('pole cross norm <',POLE_CROSS_NORM)
    print('total F->T cross norm <',CROSS_NORM_UPPER)
    print('finite source cost <',FINITE_SOURCE_COST)
    print('exact finite Rayleigh lower target >',EXACT_FINITE_RAYLEIGH_LOWER)
    print('finite-solve vector perturbation <',DX_UPPER)
    print('residual-vector perturbation <',RESIDUAL_VECTOR_PERTURB_UPPER)
    print('exact residual Gram upper target <',EXACT_RESIDUAL_GRAM_UPPER)
    print('exact tail self-energy upper target <',EXACT_TAIL_SELF_ENERGY_UPPER)
    print('conditional final directional margin >',FINAL_DIRECTIONAL_MARGIN_LOWER)

    assert CROSS_NORM_UPPER < 8.0
    assert FINITE_SOURCE_COST < 2.01e-13
    assert DX_UPPER < 9.1e-13
    assert RESIDUAL_VECTOR_PERTURB_UPPER < 7.5e-12
    assert EXACT_TAIL_SELF_ENERGY_UPPER < 6.8e-13
    assert FINAL_DIRECTIONAL_MARGIN_LOWER > 4.0e-13

    print('PASS: rounded index-3 budget closes CONDITIONALLY on the two nominal outward targets')
    print('OPEN TARGET 1: certify s_F,nom(v_*) > 1.34e-12')
    print('OPEN TARGET 2: certify ||R_nom v_*||^2 < 1.23e-13')
    print('GUARDRAIL: no index<=3 theorem until both nominal targets are outward-certified')
