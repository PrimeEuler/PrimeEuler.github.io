# Cone Derivation Ledger v13.345 — Six-Dimensional Full Infinite-Tail Bridge and Rational Protected Subspace

## Why this checkpoint matters

The earlier finite certificate architecture established a plausible route to a six-dimensional positive subspace of the N=155 finite effective block, but that alone does not control the infinite tail Schur correction.  This checkpoint addresses that structural gap directly.

Work with the pole-free operator

\[
A_0=C_{\rm cusp}+B_{\rm prime}+K_{\rm arch},
\]

and add the positive rank-one pole term only after the lower-bound argument.

## Eleven positive directions, five tail constraints, six protected directions

At the N=155 finite split, take an 11-dimensional positive finite eigenspace of the pole-free finite block and impose the five linear conditions

\[
p=0,\qquad s=0,\qquad t=0,\qquad M_1=0,\qquad J_2^{\rm total}=0.
\]

The constraint matrix has numerical rank five, leaving a six-dimensional subspace.

Its pole-free finite projected spectrum is

\[
\boxed{
0.187445591521,
0.596095813648,
0.757640642020,
0.987845006116,
1.231918326130,
1.483930923314.
}
\]

Thus the weakest finite protected level is of order 1.9e-1, not 1e-8.

## Finite intermediate tail 155..3001

Project the exact pole-free finite-to-tail matrix onto this six-plane for odd tail modes 155<=n<=3001.  Midpoint diagnostics give

\[
\|G_{155:3001}\|_2\approx8.675737398204\times10^{-3},
\]

and

\[
\boxed{
\|G_{155:3001}\|_F\approx8.730696686245\times10^{-3}.
}
\]

The Frobenius norm is the preferred proof quantity: once the matrix entries are rationally enclosed, it is certified by a finite sum of squares and requires no singular-value routine.

## Analytic tail beyond 3001

For n>=3003, the exact prime/cusp/arch formulas plus the leading-channel and first-moment cancellations give a conservative remainder bound

\[
\beta_{\rm prime}\lesssim7.7139\times10^{-5},
\]

\[
\beta_{\rm cusp}\lesssim6.2694\times10^{-5},
\]

\[
\beta_{\rm arch}\lesssim1.526\times10^{-7}.
\]

Hence

\[
\boxed{
\beta_{\ge3003}\lesssim1.400\times10^{-4}.
}
\]

The fifth constraint J2_total=0 was not even needed to obtain this coarse bound; it provides additional slack.

Combining the finite intermediate tail and the analytic remainder gives

\[
\beta_{\rm total}\lesssim8.871\times10^{-3}.
\]

Using the existing analytic tail coercivity scale

\[
\alpha_{155}\approx0.0301854,
\]

the adverse Schur correction satisfies at the design level

\[
\frac{\beta_{\rm total}^2}{\alpha_{155}}
\approx2.61\times10^{-3}.
\]

Therefore the weakest protected finite level retains approximately

\[
\boxed{
0.18745-0.00261\approx0.18484
}
\]

of positive margin after the full infinite-tail elimination.

This is the first numerically strong finite-to-infinite bridge in the Suzuki thread.

## Rational protected basis

There is no need to certify the SVD/nullspace construction itself.  Round the six protected basis vectors to 12 decimal places and treat the resulting 77x6 matrix W as a fixed rational proof object.

For this rounded W:

\[
\lambda_{\min}(W^T A_{0,FF}W)\approx0.187445591522,
\]

and

\[
\|W^T W-I\|_2\approx2.10\times10^{-12}.
\]

The five constraint residual norms are approximately

\[
8.93\times10^{-12},
8.75\times10^{-12},
3.11\times10^{-13},
5.91\times10^{-10},
9.25\times10^{-8}.
\]

When weighted by their actual n^{-1}, n^{-2}, and n^{-3} tail orders at N=3003, the combined additional tail norm caused by these rounding residuals is only

\[
\boxed{2.4\times10^{-13}}.
\]

Thus exact constraint satisfaction is unnecessary.  The final proof can work directly with a fixed rational W and explicitly charge its tiny constraint residuals.

## Resulting proof object

A full certificate can now be reduced to the following finite checks:

1. certify a rational 77x6 matrix W has rank six;
2. certify W^T A_{0,FF} W is positive definite with a lower bound comfortably above 0.18;
3. certify the finite Frobenius coupling to modes 155..3001 is below roughly 0.009;
4. use the analytic >=3003 remainder bound below roughly 1.5e-4;
5. combine with alpha_155>0 to retain a positive margin above roughly 0.18;
6. add back P_pole>=0.

This route bypasses the ultra-near-null four-dimensional finite sector entirely when the goal is only to exhibit six positive full-operator directions.

## Guardrails

The finite 155..3001 coupling and the 77x6 finite projected matrix are still midpoint data awaiting rational interval instantiation.  Therefore this checkpoint is not yet a proof that the full operator has nonpositive index <=4.  No exact zero, lambda_1=0, RH, or GRH conclusion follows.