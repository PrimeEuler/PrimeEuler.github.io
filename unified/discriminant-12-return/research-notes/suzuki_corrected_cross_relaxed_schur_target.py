#!/usr/bin/env python3
"""Relaxed corrected cross target after restoration of finite/tail gaps.

Once the repaired finite and tail blocks are available,

    A_F >= 0.22 I,
    A_T >= 4.6733 I,

the 2x2 Schur condition only requires

    ||G||^2 < 0.22*4.6733,

so the exact admissible cross threshold is about 1.01396548.

The corrected rank-4 midpoint/analytic-tail reconstruction currently gives

    midpoint after pure power-tail completion    0.9927951
    U-dependent final tail bound                 0.000564
    K=8 geometric remainder                      3.7e-10
    centered-arch final tail                     2.0e-10

hence the non-validation part is below 0.99336.  Therefore a very loose
outward finite-arithmetic/scalar enclosure of 0.01 would still imply

    ||G|| < 1.00336 < 1.01 < 1.01396548.

This checkpoint deliberately does NOT declare the 0.01 enclosure proved.  Its
purpose is to change the certification target: the final Gram checker need not
resolve the norm to 1e-3.  Any provenance-clean outward numerical enclosure
smaller than roughly 1.6e-2 is sufficient for high-complement positivity.
"""

import math
FINITE_GAP = 0.22
TAIL_GAP = 4.6733
MID = 0.9927951
U_TAIL = 5.64e-4
GEOM = 3.7e-10
ARCH_TAIL = 2.0e-10
DESIGN_VALIDATION_PAD = 0.01
DESIGN_TARGET = 1.01

threshold = math.sqrt(FINITE_GAP*TAIL_GAP)
analytic_budget = MID+U_TAIL+GEOM+ARCH_TAIL
design_upper = analytic_budget+DESIGN_VALIDATION_PAD
schur_margin = FINITE_GAP-DESIGN_TARGET**2/TAIL_GAP

if __name__ == '__main__':
    print('exact Schur cross threshold =', threshold)
    print('midpoint + analytic tails =', analytic_budget)
    print('room to exact threshold =', threshold-analytic_budget)
    print('design upper with 0.01 pad =', design_upper)
    print('Schur margin at target 1.01 =', schur_margin)
    print('guardrail: 0.01 outward validation pad still must be proved')
