# Cone Derivation Ledger v13.198 — Normalized Log-Image Audit

Date: 2026-09-03

## Question

Test whether the globally normalized flat-circle image of the classical `n log n` region gives a systematically better approximation to the divisor summatory count `D(n)`.

From v13.196, the literal region

\[
E_n=\{(x,y):1\le x\le n,\ 0\le y\le n/x\}
\]

has factor-plane area

\[
\operatorname{Area}(E_n)=n\log n,
\]

and flat-circle image area

\[
W_L(n):=\operatorname{Area}(F(E_n))
=\frac23(n-1)\sqrt n.
\]

The complete anti-diagonal triangle has mean flat-area contraction factor `pi/4`, so a natural exploratory normalization is

\[
\widetilde W_L(n):=\frac4\pi W_L(n)
=\frac{8}{3\pi}(n-1)\sqrt n.
\]

The factor `4/pi` is exact for a complete triangle-to-half-disk map, but not for the subregion `E_n`; therefore `\widetilde W_L` is an exploratory normalized estimator, not an exact push-forward inverse.

## [N-cert] Finite-range test

Using exact divisor counts

\[
D(n)=\sum_{k=1}^n\left\lfloor\frac nk\right\rfloor,
\]

compare the absolute errors of

\[
L(n)=n\log n,
\qquad
\widetilde W_L(n)=\frac{8}{3\pi}(n-1)\sqrt n,
\]

and the standard two-term main approximation

\[
M(n)=n\log n+(2\gamma-1)n.
\]

Selected values:

| n | D(n) | n log n | W~_L(n) | M(n) |
|---:|---:|---:|---:|---:|
| 10 | 27 | 23.02585 | 24.15802 | 24.57016 |
| 11 | 29 | 26.37685 | 28.15239 | 28.07559 |
| 20 | 66 | 59.91465 | 72.12527 | 63.00327 |
| 50 | 207 | 195.60115 | 294.10333 | 203.32272 |
| 100 | 482 | 460.51702 | 840.33810 | 475.96015 |
| 1000 | 7069 | 6907.75528 | 26815.40421 | 7062.18661 |
| 10000 | 93668 | 92103.40372 | 848741.48052 | 93647.71702 |

For `n=11`,

\[
|D(11)-11\log11|\approx2.623152,
\]

whereas

\[
|D(11)-\widetilde W_L(11)|\approx0.847614.
\]

Thus the normalized log-image is indeed much closer at the `n=11` shell.

A direct scan over `2\le n\le200` finds that `\widetilde W_L(n)` beats `n\log n` only for

\[
8\le n\le16
\]

and at `n=18`.

## [D] Asymptotic obstruction

The improvement cannot persist asymptotically because

\[
\widetilde W_L(n)
=\frac{8}{3\pi}(n-1)\sqrt n
\sim\frac{8}{3\pi}n^{3/2},
\]

while

\[
D(n)\sim n\log n.
\]

Hence

\[
\frac{\widetilde W_L(n)}{D(n)}
\sim
\frac{8}{3\pi}\frac{\sqrt n}{\log n}
\to\infty.
\]

So the `n=11` closeness is a finite-shell phenomenon, not a candidate global approximation to the divisor summatory function.

The same obstruction is already visible before the `4/pi` renormalization:

\[
W_L(n)=\frac23(n-1)\sqrt n=\Theta(n^{3/2}).
\]

This scaling follows from the nonuniform Jacobian. The `n log n` region reaches the factor axes where the flat-area distortion grows like `T/(2Y)`, and its average distortion therefore grows with `n`; the complete-shell average `pi/4` cannot be reused as a scale-independent inverse on this subregion.

## [D] Correct geometric interpretation

The failure is informative rather than pathological. There are three distinct quantities:

1. `n log n`: ordinary factor-plane area of the classical continuous divisor region.
2. `W_L(n)`: exact flat-circle area of its image under the local Jacobian.
3. `\widetilde W_L(n)=(4/pi)W_L(n)`: complete-shell-normalized exploratory quantity.

Only item 2 is an exact transported area. Item 3 mixes a subregion-specific Jacobian with the global mean distortion of a different region, so its temporary accuracy near `n=11` has no asymptotic force.

## [N-cert] Discrete transformed staircase scaling

For comparison, v13.197 defines the exact flat-circle image area of the divisor staircase

\[
\mathcal W_D(n)
=\sum_{k=1}^n W_k\!\left(\left\lfloor\frac nk\right\rfloor\right).
\]

Numerically,

| n | W_D(n) | W_D(n)/n^(3/2) |
|---:|---:|---:|
| 100 | 893.81664 | 0.89382 |
| 200 | 2539.03767 | 0.89769 |
| 500 | 10067.36288 | 0.90045 |
| 1000 | 28517.03755 | 0.90179 |
| 2000 | 80720.64581 | 0.90248 |

Thus the exact transformed discrete staircase itself appears to live on an `n^(3/2)` flat-circle scale. This is consistent with the transformed continuous region and confirms that circle-area magnitudes should not be compared directly to the untransformed count scale without a region-dependent normalization.

No asymptotic constant for `\mathcal W_D(n)/n^{3/2}` is claimed here; the table is numerical evidence only.

## [Audit] Publication guardrail

Do not claim

\[
\widetilde W_L(n)=\frac{8}{3\pi}(n-1)\sqrt n
\]

is an improved asymptotic approximation to `D(n)`. It is better than `n log n` around the `n=11` example but has the wrong growth order.

Publication-safe wording:

> At the illustrative shell `n=11`, globally renormalizing the exact circle image of the `n log n` region by the whole-shell factor `4/pi` happens to reduce the numerical discrepancy with `D(11)`. This normalization does not survive an asymptotic audit: the transformed region grows like `n^(3/2)`, whereas `D(n)` grows like `n log n`. The coincidence is therefore local to small shells and is not used as an estimator.

## Next exact question

The productive next target is not a constant renormalization. It is to determine a natural **region-dependent inverse area weight** or normalized probability measure for the divisor staircase in circle coordinates, and then ask whether the Dirichlet error term has a simpler expression under that measure. The rapidity/angle relation

\[
d\theta=\operatorname{sech}s\,ds
\]

is the likely analytic coordinate for that normalization.
