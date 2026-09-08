#!/usr/bin/env python3
"""Two-tier buffer certification budget for Suzuki N=155 finite reduction.

Important separation:

1. A coarse enclosure of the 67x67 buffer B is used only to certify B>0.
   Entrywise radius ~1e-3 is enough because the observed pole-free gap is
   ~0.23848.

2. A distinct high-accuracy nominal matrix Bhat is used in the numerical solve
   Bhat X ~= C^T.  Rigour enters through an outward-rounded residual enclosure
   R=C^T-BX and the certified lower bound B>=gamma I.  One does NOT feed the
   coarse 1e-3 buffer radius into the Schur perturbation formula.

This avoids an artificial inverse-sensitivity catastrophe and is the intended
v13.338 certification architecture.
"""

BUFFER_DIM=67
GAMMA_CERT_TARGET=0.15   # deliberately weaker than observed ~0.2385
C_NORM_BOUND=0.80        # deliberately weaker than observed ~0.76
EFFECTIVE_TARGET=2.0e-8

# Example budget (operator norm):
CORE_ASSEMBLY_BUDGET=3.0e-9
C_ASSEMBLY_BUDGET=2.0e-9
SOLVE_SCHUR_BUDGET=5.0e-9
ROUNDING_MISC_BUDGET=2.0e-9
RESERVE=8.0e-9

# If ||R|| <= r, then ||C B^{-1} C^T - C X|| <= ||C|| r/gamma.
RESIDUAL_TARGET=SOLVE_SCHUR_BUDGET*GAMMA_CERT_TARGET/C_NORM_BOUND


def total_budget():
    return (CORE_ASSEMBLY_BUDGET+C_ASSEMBLY_BUDGET+SOLVE_SCHUR_BUDGET+
            ROUNDING_MISC_BUDGET+RESERVE)


if __name__=='__main__':
    print('target effective-core operator radius =',EFFECTIVE_TARGET)
    print('budget sum =',total_budget())
    print('certified residual target =',RESIDUAL_TARGET)
    print('guardrail: coarse B interval proves positivity only; fine Bhat enters residual solve')
