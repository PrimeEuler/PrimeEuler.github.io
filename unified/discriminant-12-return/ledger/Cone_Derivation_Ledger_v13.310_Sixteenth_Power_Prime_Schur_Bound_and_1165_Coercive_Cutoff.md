# Cone Derivation Ledger v13.310 — Sixteenth-Power Prime Schur Bound and 1165 Coercive Cutoff

## Status
Continuation of the Suzuki/Weil quadratic-form audit at `a=1`, even-v / odd-Dirichlet sector. This checkpoint extends the positive-kernel power-Schur calculation from k=8 to k=16. It does **not** assert RH/GRH, a kernel, or lambda_1=0.

## Joint prime operator
Write
\[
A=-B_{\rm prime}=\sum_{q\in\{2,3,4,5,7\}} \frac{\Lambda(q)}{\sqrt q}S_{\log q}.
\]
The truncated-shift kernel of A is nonnegative and symmetric. Therefore for every positive integer k,
\[
\|B_{\rm prime}\|=\|A\|\le \bigl\|A^k\mathbf 1\bigr\|_\infty^{1/k}.
\]
Starting from the constant function on [-1,1], every iterate is piecewise constant. Its breakpoints are generated exactly by translating the previous breakpoints by ±log(q) and retaining points in [-1,1]. Hence the reduction to a finite interval sweep is exact.

## k=16 checkpoint
The k=16 sweep contains 3345 constant intervals. Ordinary floating-point evaluation gives
\[
\sup_x(A^{16}\mathbf1)(x)=93388.18411213082,
\]
and therefore
\[
\boxed{\|B_{\rm prime}\|\lesssim 2.044764260347282.}
\]
The finite combinatorial reduction is exact; this displayed decimal is not an interval-certified enclosure.

The late power-Schur roots are

| k | root bound |
|---:|---:|
| 8 | 2.120054596948403 |
| 9 | 2.103882903225684 |
| 10 | 2.090916526906261 |
| 11 | 2.079956678517087 |
| 12 | 2.070829709369812 |
| 13 | 2.062890150593749 |
| 14 | 2.056087864009624 |
| 15 | 2.050050622466240 |
| 16 | 2.044764260347282 |

The sequence continues to improve, but the gain per doubling is tapering. The numerical Galerkin edge near 1.94 remains exploratory and is not substituted for this bound.

## Updated tail coercivity
Retaining the existing terms
\[
\|H_{\rm odd}\|=\pi/2,
\]
the analytic archimedean-remainder bound
\[
C_{\rm arch}=1+2\log\Gamma(1-2/\pi)-4\gamma/\pi\approx2.056338685614401,
\]
and the v13.302-v13.304 localized cusp/pole estimates, use
\[
C_{\rm tail}(N)=\pi/2+2.044764260347282+C_{\rm arch}+C_{\rm cusp}(N)+C_{\rm pole}(N).
\]
The first odd N for which
\[
\log(N/4)-C_{\rm tail}(N)>0
\]
is
\[
\boxed{N=1165.}
\]
At N=1165 the ordinary floating-point evaluation is
\[
C_{\rm cusp}(1165)\lesssim9.0284\times10^{-5},
\qquad
C_{\rm pole}(1165)\lesssim1.77243\times10^{-3},
\]
with total tail constant about 5.67376198814 and positive margin about
\[
4.20\times10^{-4}.
\]

Thus the sufficient cutoff progression is now
\[
5.56\times10^6\to52363\to3441\to2809\to1765\to1433\to1257\to\boxed{1165}.
\]

## Audit synchronization
The external round-15 objection to the v13.302 off-diagonal Hilbert-Schmidt estimate was explicitly addressed by the revised v13.303 estimate and independently confirmed closed in external audit round 16. This checkpoint therefore uses the localized cusp control only with that corrected audit status in force.

## Interpretation / next move
Power-Schur has not fully saturated, but the k=8→16 improvement changes the prime constant by only about 0.0753 and the cutoff by 92 modes. The archimedean remainder constant 2.05634 is now slightly larger than the k=16 prime constant 2.04476. This is the natural pivot point: preserve the k=16 prime bound and next sharpen the **lower spectral cost** of the smooth archimedean remainder rather than continuing blind power doubling.

A particularly important sign check should accompany that audit: in the even-v sector the pole contribution is positive semidefinite rank one, so a lower-coercivity estimate should not need to subtract its norm. Removing that conservative cost is exact if the sign bookkeeping is reconfirmed in the full decomposition.

## Reproducibility
Script: `research-notes/suzuki_joint_prime_sixteenth_power_schur.py`.
