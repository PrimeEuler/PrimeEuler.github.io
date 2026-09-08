# Cone Derivation Ledger v13.335 — Residual-Certified Schur Solve and No Interval Inverse

## Main reduction

For the finite Feshbach problem at N=155, write

\[
F=A_{CC}-CB^{-1}C^T,
\]

with buffer block \(B\) on odd modes \(21,23,\ldots,153\).

There is no need to construct a verified inverse of \(B\).

Let \(X\) be a numerical approximation to

\[
X_*=B^{-1}C^T,
\]

and define the residual

\[
R=C^T-BX.
\]

If

\[
B\succeq\gamma I,
\]

then

\[
X_*-X=B^{-1}R,
\]

so

\[
\boxed{
\|X_*-X\|\le\frac{\|R\|}{\gamma}.
}
\]

Consequently

\[
\boxed{
\|CB^{-1}C^T-CX\|
\le
\frac{\|C\|}{\gamma}\,\|R\|.
}
\]

## Numerical design scale

Using the current targeting values

\[
\gamma\approx0.23848,
\qquad
\|C\|\lesssim0.76,
\]

the amplification factor is only

\[
\frac{\|C\|}{\gamma}\lesssim3.19.
\]

Therefore a Schur-correction solve error below \(10^{-9}\) only requires a certified residual norm roughly

\[
\boxed{
\|R\|\lesssim3.1\times10^{-10}.
}
\]

Similarly:

- \(10^{-12}\) Schur accuracy requires residual \(\sim3\times10^{-13}\);
- \(10^{-15}\) Schur accuracy requires residual \(\sim3\times10^{-16}\).

These are straightforward targets for multiprecision numerical solves, provided the residual itself is evaluated with outward-rounded enclosures.

## Why this matters

The 67-dimensional buffer now has two completely separate tasks:

1. coarse interval enclosure to prove \(B>0\);
2. high-accuracy numerical solve followed by a verified residual bound.

The second task does **not** require high-accuracy interval enclosure of every entry of \(B^{-1}\).  It only requires verification of the residual of 10 right-hand sides.

Thus the rigorous pipeline becomes

\[
\boxed{
\text{coarse buffer positivity}
\;\to\;
\text{multiprecision solve}
\;\to\;
\text{interval residual}
\;\to\;
\text{10x10 Schur enclosure}.
}
\]

## Next simplification

Once the 10x10 effective core is enclosed in operator norm by \(\eta\), one does not need to construct an exact six-dimensional stiff basis.  If the fifth approximate eigenvalue satisfies

\[
\widehat\lambda_5>\eta,
\]

then Weyl's inequality certifies

\[
\lambda_5(F)>0,
\]

and hence **at most four eigenvalues of F can be nonpositive**.  This gives a basis-free route to the rigorous four-dimensional terminal obstruction.

## Guardrails

The numerical constants are non-interval design data.  Final certification requires outward enclosures of the buffer lower bound, matrix entries, and residual norm.  No exact zero, positivity theorem, lambda_1=0, RH, or GRH conclusion follows.
