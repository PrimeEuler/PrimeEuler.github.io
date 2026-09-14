# Cone Derivation Ledger v13.424 — Odd Pole-Free Finite-High Arithmetic Budget

Date: 2026-09-14

Status labels: **[N]** midpoint numerical; **[N-cert]** conservative floating-point verification conditional on the nominal matrix; **[Audit]** guardrail.

## 0. Purpose

The active target is

\[
A_{FF}^{(0)}\succeq0.53I,
\qquad F=\{22,24,\ldots,4000\},
\]

which is sufficient for the full odd finite-high block because the removed sinh-pole is PSD.

v13.417 established the pole-free midpoint shifted minimum

\[
\lambda_{\min}(A_{FF}^{(0)}-0.53I)\approx0.002842383786.
\]

The present checkpoint isolates the **finite floating-point factor/inverse arithmetic** from the still-separate exact-source-vs-nominal enclosure.

## 1. Cholesky reconstruction [N]

For the midpoint nominal shifted matrix

\[
B=A_{FF}^{(0)}-0.53I
\]

of dimension N=1990, binary64 Cholesky gives L with point residual

\[
\|B-LL^T\|_F\approx4.01\times10^{-14}.
\]

With unit roundoff

\[
u=2^{-53},
\]

the standard dot-product factor is

\[
\gamma_N=\frac{Nu}{1-Nu}\approx2.2094\times10^{-13}.
\]

The computed scale

\[
\||L||L|^T\|_F\approx249.66
\]

gives a dot-product envelope about

\[
5.52\times10^{-11}.
\]

Including the final subtraction, a deliberately rounded conditional reconstruction budget is

\[
\boxed{\|B-LL^T\|_F<6\times10^{-11}}
\]

for the supplied nominal B.

## 2. Verified-inverse route [N/N-cert]

Let X be the computed triangular solve approximation to L^{-1}.  Midpoint diagnostics give

\[
\|X\|_F\approx27.65454,
\]

and

\[
\|I-LX\|_F\approx5.4\times10^{-15}.
\]

The same gamma_N product accounting gives an arithmetic envelope about

\[
2.14\times10^{-11}
\]

for the LX product.  Thus the relaxed verification targets

\[
\boxed{\|X\|_F<28,}
\qquad
\boxed{\|I-LX\|_2<10^{-8}}
\]

have enormous numerical slack.

If these outward inequalities are used, the Neumann argument gives

\[
\|L^{-1}\|_2
\le
\frac{\|X\|_2}{1-\|I-LX\|_2}
<\frac{28}{1-10^{-8}}.
\]

Therefore

\[
\lambda_{\min}(LL^T)
=\frac1{\|L^{-1}\|_2^2}
>
\frac{(1-10^{-8})^2}{28^2}
>0.0012755.
\]

This lower scale is intentionally much weaker than the midpoint shifted eigenvalue 0.00284238, but it is more than sufficient for a robust certificate.

## 3. Comparison with arithmetic reconstruction error [N-cert conditional]

The relaxed factor floor

\[
0.0012755
\]

is over seven orders of magnitude larger than the reconstruction budget

\[
6\times10^{-11}.
\]

Thus finite Cholesky/inverse arithmetic is not the bottleneck.

Even after allocating a source-operator uncertainty on the order of v13.357's

\[
2\times10^{-13},
\]

the arithmetic/source budget remains negligible relative to this deliberately weakened factor floor.

## 4. Logical separation [Audit]

This checkpoint does **not** yet promote

\[
A_{FF}^{(0)}\succeq0.53I.
\]

The remaining proof obligation is to replace the scipy/adaptive nominal scalar construction by an outward-enclosed source-faithful generator:

1. certified h_32 polynomial plus the parity-correct even-mode recurrence from v13.423;
2. outward prime logarithm/trigonometric constants;
3. outward cusp Si/Ci evaluation or certified asymptotic series;
4. outward finite matrix assembly relative to the nominal B.

Once the exact-source-vs-nominal operator error is bounded well below approximately 0.00127, the verified-factor route closes positivity.  The inherited target 2e-13 is far stronger than actually required.

## 5. Consequence for proof strategy

The available margin means there is no need to reproduce an ultra-tight historical high-block implementation.  A much looser, transparent source enclosure suffices:

\[
\boxed{
\text{source enclosure }<10^{-4}
\quad\text{would already leave more than an order of magnitude of safety.}
}
\]

This substantially simplifies the outward finite-high task.

The arithmetic replay helper is

`research-notes/suzuki_odd_M4000_pole_free_arithmetic_residual_budget.py`.

---

**Checkpoint conclusion.** The odd pole-free finite-high proof is no longer limited by floating-point factorization.  A coarse verified inverse gives a factor floor above 0.0012755 while reconstruction arithmetic is at the 1e-10 scale.  The only substantive finite-high task left is an outward scalar/source generator; importantly, that generator may be conservative by many orders of magnitude and still close A_FF >= 0.53 I.