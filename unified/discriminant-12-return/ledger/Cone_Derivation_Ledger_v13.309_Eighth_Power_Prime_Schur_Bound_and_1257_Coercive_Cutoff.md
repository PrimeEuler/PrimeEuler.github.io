# Cone Derivation Ledger v13.309
## Eighth-Power Prime Schur Bound and 1257 Coercive Cutoff

### Scope
This checkpoint continues the Suzuki a=1 even-v tail coercivity audit. It sharpens only the joint prime-shift operator bound, using the same positive-kernel power-Schur mechanism as v13.307-v13.308.

No RH/GRH, kernel, or lambda_1=0 conclusion is made.

---

## 1. Joint prime operator
Write

\[
A=-B_{\rm prime}=\sum_{q\in\{2,3,4,5,7\}} a_q S_{\log q},
\qquad
 a_q=\frac{\Lambda(q)}{\sqrt q},
\]

where

\[
(S_\ell f)(x)=f(x-\ell)+f(x+\ell)
\]

with zero extension outside \([-1,1]\).

The kernel of \(A\) is nonnegative and symmetric. Therefore, for every positive integer \(k\),

\[
\|B_{\rm prime}\|=\|A\|
\le
\left(\sup_{x\in[-1,1]} (A^k\mathbf 1)(x)\right)^{1/k}.
\]

For piecewise-constant inputs, \(A\) preserves piecewise constancy. The breakpoint set at each iterate is generated exactly by shifting the previous breakpoint set by \(\pm\log q\) and retaining points inside \([-1,1]\). Thus each power bound reduces to a finite exhaustive interval sweep.

---

## 2. Power-Schur sequence through k=8
The computed finite breakpoint sequence is:

| k | intervals | sup_x A^k 1 | kth-root bound |
|---:|---:|---:|---:|
| 1 | 11 | 2.9262341821764086 | 2.9262341821764086 |
| 2 | 31 | 6.054238008078117 | 2.460536122083583 |
| 3 | 59 | 12.692957889252241 | 2.3326752407353215 |
| 4 | 101 | 25.69449057762533 | 2.2514380572859216 |
| 5 | 161 | 51.72258347500741 | 2.201587961706689 |
| 6 | 237 | 103.36341219971001 | 2.1663459236634086 |
| 7 | 347 | 205.58079715675115 | 2.1400606322376294 |
| 8 | 491 | 408.10917852814157 | 2.120054596948403 |

Hence the eighth-power bound is

\[
\boxed{
\|B_{\rm prime}\|
\le
408.10917852814157^{1/8}
\approx
2.120054596948403.
}
\]

The finite-breakpoint reduction is exact. The displayed decimal values are ordinary floating-point evaluations rather than interval-certified enclosures.

This improves the v13.308 fourth-power value

\[
2.251438057285922.
\]

The sequence continues to move toward the exploratory odd-mode Galerkin spectral edge near 1.94, but that numerical edge remains non-certified and is not used in any theorem-level cutoff.

---

## 3. Tail coercivity update
Retain the established decomposition

\[
A_{\rm even}
=
D_{\log}-H_{\rm odd}+K_{\rm cusp}+B_{\rm prime}+K_{\rm smooth}.
\]

Use:

\[
\|H_{\rm odd}\|=\frac\pi2,
\]

the v13.304 analytic archimedean-remainder bound

\[
\|K_{\rm arch\,rem}\|\le 2.0563386856144006,
\]

plus the explicit tail-localized cusp and rank-one pole bounds from v13.304.

With the eighth-power prime constant, for odd-mode vectors supported on \(n\ge N\),

\[
\langle A_{\rm even}c,c\rangle
\ge
\left[
\log(N/4)
-
C_{\rm tail}(N)
\right]\|c\|_2^2.
\]

The first odd cutoff found by the explicit bound is

\[
\boxed{N=1257}.
\]

At this cutoff:

\[
\|P_NK_{\rm cusp}P_N\|
\lesssim
8.355623150544087\times10^{-5},
\]

\[
\|P_NK_{\rm pole}P_N\|
\lesssim
1.6425006388125518\times10^{-3},
\]

and

\[
C_{\rm tail}(1257)
\approx
5.748915666228018.
\]

The coercivity margin is

\[
\log(1257/4)-C_{\rm tail}(1257)
\approx
1.2731812423387723\times10^{-3}>0.
\]

So the explicit sufficient tail threshold progresses as

\[
5.56\times10^6
\to 52363
\to 3441
\to 2809
\to 1765
\to 1433
\to
\boxed{1257}.
\]

---

## 4. Interpretation and guardrails
1. This is an infinite-tail coercivity statement in the a=1 even-v sector only.
2. It does not prove \(\ker G_1\neq\{0\}\), \(\lambda_1=0\), RH, or GRH.
3. The eighth-power breakpoint reduction is finite and exhaustive, but the reported decimal bound is not interval-certified.
4. The compact cusp/pole tails are now numerically negligible at the coercive cutoff. The remaining dominant constants are the Hilbert term, the joint prime operator, and the analytic archimedean-remainder envelope.
5. Power-Schur gains are beginning to taper. A k=16 checkpoint is still reasonable, but after that a sharper analytic archimedean bound may be more productive.

---

## Reproducibility
Script:

`research-notes/suzuki_joint_prime_eighth_power_schur.py`

The script reproduces the k=1..8 power-Schur sequence, the k=8 joint-prime bound, and the updated N=1257 tail-coercivity cutoff.
