#!/usr/bin/env python3
"""Fail-closed gate for the M=16001 outward even index<=3 replay.

This file records exactly which pieces of the proposed shifted-nominal M16001
certificate are already certified and which executable outward backend is still
missing.  It deliberately refuses theorem promotion until source scalar
reconstruction is certified through the full M=16001 finite split.

Established inputs
------------------
* v13.357: for B=A0_[21,16001]-0.22 I, the exact-vs-high-precision-nominal
  operator target is ||B_exact-B_nominal||_2 < 2e-13.  The archimedean part is
  dimension-free (<=1.22e-13), while prime/cusp constants are to be reconstructed
  with certified scalar enclosures.
* shifted M16001 midpoint target:
      normalized Q lower block       > 0.67
      Q/N cross                      < 2.7e-7
      best unresolved scalar         > 9.1e-13
      six-plane Schur penalty        < 1.1e-13
      final seven-plane target       > 8.0e-13
* long-double replay on the same midpoint scalar payload:
      max solve-coefficient change   < 4e-15
      relevant Rayleigh change       < 2e-16

Open executable gate
--------------------
The currently committed exact-rational prime-trigonometric helper
suzuki_prime_trig_rational_certificate.py has RMAX=2000, matching the old
M=3999 split.  The M=16001 split requires certified recurrence propagation to
r=8000.  The current M16001 target helpers instead obtain their nominal source
payload from ordinary SciPy quadrature/special-function calls.  Those calls are
midpoint diagnostics, not outward intervals.

Therefore the four requested M16001 interval objects cannot yet be called
certified from the committed executable chain:
  1. shifted finite Schur block;
  2. Q/N cross block;
  3. remote Gram through 2M;
  4. blockwise analytic far tail, because its moment coefficients inherit the
     same uncertified M16001 nominal source payload.

This is a provenance/executable-certification gap, not evidence that the
numerical margin fails.
"""

REQUIRED_RMAX = 8000
COMMITTED_PRIME_CERT_RMAX = 2000

MIDPOINT_Q_LOWER = 0.67
MIDPOINT_QN_CROSS_UPPER = 2.7e-7
MIDPOINT_UNRESOLVED_LOWER = 9.1e-13
MIDPOINT_PENALTY_UPPER = 1.1e-13
MIDPOINT_FINAL_LOWER = 8.0e-13

LONGDOUBLE_SOLVE_COEFF_DIFF_UPPER = 4.0e-15
LONGDOUBLE_RAYLEIGH_DIFF_UPPER = 2.0e-16
SOURCE_OPERATOR_ENCLOSURE = 2.0e-13
ARCH_OPERATOR_ENCLOSURE = 1.22e-13

if __name__ == '__main__':
    print('required prime recurrence RMAX =', REQUIRED_RMAX)
    print('committed rational prime certificate RMAX =', COMMITTED_PRIME_CERT_RMAX)
    print('shifted midpoint Q lower >', MIDPOINT_Q_LOWER)
    print('shifted midpoint Q/N cross <', MIDPOINT_QN_CROSS_UPPER)
    print('shifted midpoint unresolved scalar >', MIDPOINT_UNRESOLVED_LOWER)
    print('shifted midpoint Schur penalty <', MIDPOINT_PENALTY_UPPER)
    print('shifted midpoint final margin >', MIDPOINT_FINAL_LOWER)
    print('long-double solve coefficient delta <', LONGDOUBLE_SOLVE_COEFF_DIFF_UPPER)
    print('long-double Rayleigh delta <', LONGDOUBLE_RAYLEIGH_DIFF_UPPER)
    print('certified exact-vs-high-precision-nominal operator target <', SOURCE_OPERATOR_ENCLOSURE)
    print('certified arch operator component <=', ARCH_OPERATOR_ENCLOSURE)

    if COMMITTED_PRIME_CERT_RMAX < REQUIRED_RMAX:
        raise RuntimeError(
            'FAIL CLOSED: M16001 certified scalar-generation backend is not yet '
            'extended through r=8000; no outward seven-plane theorem promotion.'
        )
