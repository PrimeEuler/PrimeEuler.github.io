# Cone Derivation Ledger v13.356

## Two-sided inverse-factor bound and the 3e-6 residual target

### Purpose

v13.355 reduced the finite high-block positivity proof to an a posteriori LDL
factor certificate but used the very crude estimate

\[
\|L^{-1}\|_2\le\sqrt{N}\,\|L^{-1}\|_\infty,
\qquad N=7991.
\]

This checkpoint computes both absolute row- and column-sum inverse bounds and
thereby improves the sufficient residual tolerance by roughly a factor of 45.

---

## 1. Absolute inverse row bound

For unit lower triangular \(L\), let \(N=L-I\).  Define

\[
y_i=1+\sum_{j<i}|L_{ij}|y_j.
\]

By induction through forward substitution,

\[
\boxed{\|L^{-1}\|_\infty\le\max_i y_i.}
\]

For the full structured midpoint factor on odd modes \(21\le n\le16001\),

\[
\boxed{\max_i y_i\approx21.2201180807.}
\]

---

## 2. Absolute inverse column bound

Apply the same argument to \(L^T\).  Define backward

\[
z_j=1+\sum_{i>j}|L_{ij}|z_i.
\]

Then

\[
\boxed{\|L^{-1}\|_1\le\max_j z_j.}
\]

The full midpoint factor gives

\[
\boxed{\max_j z_j\approx3802.74853590.}
\]

The large column bound is concentrated very early in the elimination ordering;
it is nevertheless far better than multiplying the row bound by the full
matrix dimension.

---

## 3. Two-norm consequence

Use

\[
\|M\|_2\le\sqrt{\|M\|_1\|M\|_\infty}.
\]

Thus

\[
\|L^{-1}\|_2
\le
\sqrt{21.2201180807\times3802.74853590}
\approx
\boxed{284.0682541}.
\]

This replaces the v13.355 bound near \(1.897\times10^3\).

---

## 4. Improved residual threshold

The minimum midpoint diagonal pivot remains

\[
d_{\min}\approx0.254299623649.
\]

Hence a sufficient a posteriori positivity condition is now

\[
\|E\|_2
<
\frac{0.254299623649}{(284.0682541)^2}
\approx
\boxed{3.15\times10^{-6}},
\]

where

\[
E=B-LDL^T,
\qquad
B=A_{0,[21,16001]}-0.22I.
\]

This is roughly 45 times looser than the already-conservative
\(7.07\times10^{-8}\) target from v13.355.

---

## 5. Why this matters

The available finite-entry construction already supports scalar enclosures far
below \(10^{-10}\), with prime and pole terms much smaller and cusp/arch terms
improvable arbitrarily by extending rational series.

Therefore a \(3\times10^{-6}\) global residual tolerance is extremely generous.
The remaining work is no longer about numerical precision.  It is to package a
verified point factor plus outward-rounded bounds for:

1. the minimum diagonal pivot;
2. the two inverse-factor recursions;
3. the final matrix residual.

The packed lower-triangular multipliers may be streamed to temporary storage
during verification; they do not need to become a repository data artifact.

---

## 6. Global consequence if closed

Once this residual certificate proves

\[
A_{0,[21,16001]}\succeq0.22I,
\]

combine with the current rounded targets

\[
\|G_{[21,16001],[16003,\infty)}\|<1,
\qquad
A_{0,[16003,\infty)}\succeq4.67326749I.
\]

Then

\[
A_0|_{\mathcal D}
\succeq
\left(0.22-\frac1{4.67326749}\right)I
>6\times10^{-3}I.
\]

This would rigorously reduce the infinite inertia problem to the ten low modes.

---

## Guardrails

- The row/column inverse bounds in this checkpoint are midpoint diagnostics.
- The \(3.15\times10^{-6}\) threshold is a sufficient design target, not yet a
  completed outward-rounded certificate.
- No full high-complement positivity theorem is claimed yet.
- No exact-zero, \(\lambda_1=0\), RH, or GRH conclusion follows.
