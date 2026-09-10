#!/usr/bin/env python3
"""Source-faithful finite-section regression targets for Suzuki S10.

This checkpoint follows v13.387, which resolved External Audit Round 20's
archimedean overlap mistake and restored the rank-two/source-faithful matrix.

Low core:
    C = {1,3,...,19}.
Finite high block at cutoff M:
    D_M = {21,23,...,M}.
The finite Schur complement is

    S10(M) = A_CC - A_C,D_M A_D_M,D_M^{-1} A_D_M,C,

with the full pole term included and the source-faithful arch formula

    K_arch(m,n)=-(4/pi)(n H_m-m H_n)/(n^2-m^2).

Fresh direct dense solves produced the regression table below.  These are
ordinary floating-point finite-section diagnostics, not certified infinite
Schur eigenvalues.

cutoff 99:
  [-1.69430801e-14, -2.39957530e-15, +2.50005003e-14,
   +1.74484630e-12, +4.47374662e-08, +2.69172458e-04,
   +8.68999223e-01, ...]

cutoff 199:
  [-1.69189836e-14, -2.36687531e-15, +2.49187458e-14,
   +1.46170560e-12, +4.28661882e-08, +2.49939429e-04,
   +8.20255652e-01, ...]

cutoff 399:
  [-1.69517481e-14, -2.35738306e-15, +2.54417780e-14,
   +1.43474376e-12, +4.13976030e-08, +2.34349019e-04,
   +7.95452258e-01, ...]

cutoff 799:
  [-1.69418372e-14, -2.56832248e-15, +2.48352148e-14,
   +1.39359190e-12, +4.00213430e-08, +2.24687386e-04,
   +7.82145931e-01, ...]

The first four directions are numerically indistinguishable from zero at this
precision and must NOT be called exact kernels.  The fifth remains small and
positive in every tested source-faithful finite section, while the sixth is
roughly four orders of magnitude larger.

The rank-four audit-detour matrix instead produced a fifth eigenvalue near
-1.65e-3.  That pattern is now a negative regression test: if it reappears, the
wrong derivative-overlap arch formula has entered the assembly.

No exact-zero, RH, GRH, or final inertia conclusion follows from this file.
"""

REGRESSION = {
    99:  (-1.69430801e-14, -2.39957530e-15, 2.50005003e-14,
          1.74484630e-12, 4.47374662e-08, 2.69172458e-04, 8.68999223e-01),
    199: (-1.69189836e-14, -2.36687531e-15, 2.49187458e-14,
          1.46170560e-12, 4.28661882e-08, 2.49939429e-04, 8.20255652e-01),
    399: (-1.69517481e-14, -2.35738306e-15, 2.54417780e-14,
          1.43474376e-12, 4.13976030e-08, 2.34349019e-04, 7.95452258e-01),
    799: (-1.69418372e-14, -2.56832248e-15, 2.48352148e-14,
          1.39359190e-12, 4.00213430e-08, 2.24687386e-04, 7.82145931e-01),
}

if __name__ == '__main__':
    for cutoff, vals in REGRESSION.items():
        print(cutoff, vals)
    print('guardrail: finite-section midpoint regression only')
