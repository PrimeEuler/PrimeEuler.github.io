#!/usr/bin/env python3
"""Six-dimensional finite-to-infinite bridge audit for the pole-free operator.

This checkpoint addresses the structural gap between a finite effective-core
index bound and the full infinite operator.

Work with the pole-free operator

    A0 = C_cusp + B_prime + K_arch,

because P_pole >= 0 can be added back only after the lower-bound argument.

At the N=155 finite split, take the 11-dimensional positive finite eigenspace
corresponding numerically to positive levels 5 through 15 and impose five
linear tail-cancellation constraints:

  prime 1/n channel = 0,
  cusp 1/n channel = 0,
  arch 1/n channel = 0,
  M1 = sum m q_m = 0,
  J2_total = 0.

The resulting constrained space has dimension 6.  Its midpoint finite spectrum
is approximately

  0.187445591521,
  0.596095813648,
  0.757640642020,
  0.987845006116,
  1.231918326130,
  1.483930923314.

Thus the weakest finite Rayleigh margin is ~1.87e-1, dramatically larger than
the old 4.3e-8 stiff-core level.

For the exact pole-free finite-to-tail formulas, direct midpoint projection on
155 <= n <= 3001 gives

  ||G_155:3001||_2   ~= 8.675737398204e-3,
  ||G_155:3001||_F   ~= 8.730696686245e-3.

The Frobenius norm is the preferred future certificate because it can be
verified by a finite rational interval sum of squares; no tail singular-value
routine is needed.

For n >= N=3003, using only the three leading-channel cancellations and M1=0
(the J2 cancellation is not even needed for this coarse remainder bound),
Cauchy-Schwarz plus the exact prime/cusp/arch formulas gives the conservative
midpoint targeting bounds

  beta_prime >=3003 ~= 7.7138941231e-5,
  beta_cusp  >=3003 ~= 6.2693693491e-5,
  beta_arch  >=3003 ~= 1.5255604579e-7,

hence

  beta_remainder <= 1.3998519077e-4.

Combining finite and infinite tail pieces by triangle inequality gives

  beta_total <= 8.8706818770e-3.

Using the existing analytic N=155 tail gap

  alpha_155 ~= 3.01854e-2,

one obtains the design Schur penalty

  beta_total^2 / alpha_155 ~= 2.6068562e-3.

Against the weakest finite constrained level ~1.8744559e-1, the remaining
positive margin is about

  1.8483874e-1.

This is a midpoint/analytic hybrid audit, NOT yet the final proof.  The finite
155..3001 Frobenius block and the six-dimensional finite constrained matrix
still need rational interval instantiation.  The infinite >=3003 remainder is
already in analytic-bound form.

If the finite interval implementation preserves even a small fraction of the
~0.18 margin, this will bridge the finite positive-subspace certificate to the
full pole-free infinite operator; adding P_pole >= 0 then preserves positivity.
No exact-zero, lambda_1=0, RH, or GRH claim follows.
"""

FINITE_CONSTRAINED_EIGS=(
    0.187445591521,
    0.596095813648,
    0.757640642020,
    0.987845006116,
    1.231918326130,
    1.483930923314,
)
TAIL_155_3001_NORM2=8.675737398204e-3
TAIL_155_3001_FRO=8.730696686245e-3
TAIL_GE3003_PRIME=7.7138941231e-5
TAIL_GE3003_CUSP=6.2693693491e-5
TAIL_GE3003_ARCH=1.5255604579e-7
TAIL_GE3003_TOTAL=1.3998519077e-4
TAIL_TOTAL=8.8706818770e-3
ALPHA_155=3.01854e-2
SCHUR_PENALTY=2.6068562e-3
POSITIVE_MARGIN_AFTER_TAIL=1.8483874e-1

if __name__=='__main__':
    print('finite min',FINITE_CONSTRAINED_EIGS[0])
    print('finite-tail Frobenius',TAIL_155_3001_FRO)
    print('analytic tail remainder',TAIL_GE3003_TOTAL)
    print('Schur penalty',SCHUR_PENALTY)
    print('remaining margin',POSITIVE_MARGIN_AFTER_TAIL)
    print('guardrail: finite interval instantiation still pending')
