# Cone Derivation Ledger v13.380

## Global centered corrected-arch decay

This checkpoint closes the provisional centered-arch decay target left open in
v13.379.

For odd positive `n`, define

\[
H_n=\int_0^2 h(t)\sin\frac{n\pi t}{2}\,dt,
\qquad
Y_n=nH_n,
\]

and

\[
c_\infty
=\frac2\pi\bigl(h(0)+h(2)\bigr)
=\frac2\pi\frac{e^{-1}}{1-e^{-4}}.
\]

Then

\[
\widetilde Y_n=Y_n-c_\infty.
\]

Two integrations by parts give the exact identity

\[
\widetilde Y_n
=-\frac{8}{\pi^3n^2}
\left[
 h''(0)+h''(2)
 +\int_0^2 h'''(t)\cos\frac{n\pi t}{2}\,dt
\right].
\]

Therefore

\[
|\widetilde Y_n|
\le
\frac{8}{\pi^3n^2}
\left(
 |h''(0)|+|h''(2)|+\int_0^2|h'''(t)|dt
\right).
\]

Using the exact rational degree-65 polynomial `h_32`, termwise absolute
coefficient sums on `[0,2]` give

\[
\sup|h_{32}''|<0.687343597681,
\]

and

\[
\int_0^2|h_{32}'''(t)|dt<3.541154722978.
\]

Thus the polynomial contribution to the bracket is below

\[
2(0.687343597681)+3.541154722978
<4.915841919.
\]

For the omitted sech tail, use the coefficient majorant

\[
|T_r(2)|\le \frac1\pi\left(\frac2\pi\right)^{2r},
\qquad r\ge33.
\]

For the omitted regular-csch tail, the coarser bound

\[
|T_r(2)|\le \pi^{-2r},
\qquad r\ge34
\]

is sufficient.  Differentiating termwise multiplies the endpoint magnitudes by
`p(p-1)/4` for the second derivative and by `p(p-1)(p-2)/8` for the third
derivative.  Summing the resulting geometric tails gives an additional
contribution below

\[
4.60\times10^{-9}.
\]

Hence

\[
C_h<4.915841924,
\qquad
\frac8{\pi^3}C_h<1.268348.
\]

We record the rounded global estimate

\[
\boxed{
|\widetilde Y_n|<\frac{1.27}{n^2}
}
\]

for every odd positive `n`.

### Consequence for the corrected remote cross

The final `n>2,000,005` variable centered-arch channel in v13.379 is then below
about `2e-10` in Hilbert-Schmidt norm, replacing the provisional `1.5e-9`
budget based on the much weaker target `10/n^2`.

This result comes directly from the defining sine transform and is independent
of the superseded legacy arch off-diagonal formula.

## Status

This closes the centered-arch decay ingredient of the repaired cross
certificate.  The finite projected Gram arithmetic and corrected finite-block
LDL replay remain to be outward certified before restoring global
high-complement positivity.  No exact-zero, RH, or GRH conclusion follows.
