# Cone Derivation Ledger v13.339 — Quadrature-Free Archimedean Finite Block and Explicit 4D Certificate Contract

## Scope

This checkpoint continues v13.338 and turns the finite-block certification architecture into an explicit proof contract.

The N=155 finite reduction is

\[
C=\{1,3,\ldots,19\},\qquad
B=\{21,23,\ldots,153\},
\]

with a 10-dimensional core and 67-dimensional buffer.

## Two-tier buffer certification

The buffer must be treated at two accuracies for two different purposes.

1. **Coarse interval enclosure** only to prove
   \[
   B\succeq \gamma I.
   \]
   A conservative target is \(\gamma=0.15\), well below the observed full-buffer gap ~0.272 and pole-free gap ~0.238.

2. **Fine nominal matrix** for the Schur solve.  One solves
   \[
   \widehat B X\approx C^T
   \]
   numerically and certifies the true residual
   \[
   R=C^T-BX.
   \]
   Since \(B\succeq\gamma I\),
   \[
   \|CB^{-1}C^T-CX\|
   \le\frac{\|C\|}{\gamma}\|R\|.
   \]

With conservative \(\|C\|\le0.8\), \(\gamma=0.15\), a residual norm below \(8\times10^{-10}\) contributes at most

\[
\frac{0.8}{0.15}(8\times10^{-10})
\approx4.27\times10^{-9}
\]

to the effective-core operator error.

## Explicit certificate contract

Let

\[
F=A_{CC}-CB^{-1}C^T.
\]

It is sufficient to verify:

- \(B\succeq0.15I\);
- \(\|C\|\le0.8\);
- \(\|R\|\le8\times10^{-10}\);
- a midpoint matrix \(\widehat F\) with
  \[
  \|F-\widehat F\|\le1.4267\times10^{-8};
  \]
- \(\lambda_5(\widehat F)\ge3.5\times10^{-8}\).

Then Weyl gives

\[
\lambda_5(F)
\ge3.5\times10^{-8}-1.4267\times10^{-8}
>2.07\times10^{-8}>0.
\]

Therefore the finite 10x10 effective core has at most four nonpositive eigenvalues.

This is a finite-core inertia statement only; it is not yet a theorem about the full infinite operator after remote-tail coupling.

## Quadrature-free archimedean block

Write

\[
h(t)=\frac14\left(\csch\frac t2+\sech\frac t2-\frac2t\right).
\]

After cancellation of the singular term, the Taylor coefficients are exact rational numbers.

Even coefficients:

\[
[t^{2r}]h
=\frac14\frac{E_{2r}}{(2r)!2^{2r}}.
\]

Odd coefficients:

\[
[t^{2r-1}]h
=\frac14\frac{2(1-2^{2r-1})B_{2r}}{(2r)!2^{2r-1}}.
\]

Using exact Euler-number and Bernoulli-number coefficient bounds, on \(0\le t\le2\) the truncation after \(N=32\) satisfies

\[
\|h-h_{32}\|_\infty<6.1\times10^{-14}.
\]

Hence

\[
|\delta H_n|<1.22\times10^{-13},
\qquad
|\delta D_n|<2.44\times10^{-13}.
\]

The associated crude 77x77 arch operator truncation is below about \(2\times10^{-11}\), far under the 1e-8 effective-core budget.

## Exact polynomial integration recurrence

For odd \(n\), set \(b=n\pi/2\) and

\[
I_p=\int_0^2t^p\cos(bt)dt,
\qquad
J_p=\int_0^2t^p\sin(bt)dt.
\]

Since \(\sin(2b)=0\), \(\cos(2b)=-1\),

\[
I_0=0,
\qquad
J_0=\frac2b,
\]

\[
I_p=-\frac p b J_{p-1},
\qquad
J_p=\frac{2^p}{b}+\frac p b I_{p-1}.
\]

Therefore the certified polynomial approximant \(h_{32}\) gives all scalar arch quantities by finite recurrence:

\[
H_n^{(32)}=\sum_pa_pJ_p,
\]

\[
D_n^{(32)}
=-\sum_pa_p\left(2I_p-I_{p+1}+\frac{J_p}{b}\right).
\]

All off-diagonal arch entries are then reconstructed from

\[
K^{arch}_{mn}
=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2}.
\]

Thus the finite archimedean block requires **no numerical quadrature** and **no special-function evaluation** after the Taylor coefficients are generated.  Only outward-rounded arithmetic in \(\pi\) remains.

## Exact pole block

For odd n, \(k_n=n\pi/2\),

\[
c_n=\frac{2k_n\cosh(1/2)}{k_n^2+1/4},
\]

and

\[
P_{pole}=2cc^T.
\]

Hence the pole block also requires no quadrature.

## Current bottleneck

After this reduction, the difficult proof-grade transcendental evaluation is concentrated in the cusp and prime formulas:

- \(\operatorname{Si}(n\pi)\), \(\operatorname{Ci}(n\pi)\);
- \(\log q\), \(\sin(n\pi\log q/2)\) for \(q\in\{2,3,4,5,7\}\);
- outward-rounded \(\pi\) and \(\cosh(1/2)\).

The archimedean integration problem has been removed entirely.

## Guardrails

- The nominal \(\lambda_5\approx4.32\times10^{-8}\) remains numerical until the stated enclosure contract is actually verified.
- The first four effective levels remain unresolved.
- No positivity, exact zero mode, \(\lambda_1=0\), RH, or GRH conclusion follows.

## Next target

Implement a proof-grade outward-rounded evaluator for the remaining finite transcendental scalars, then execute the residual-based Schur contract.  The first rigorous milestone is now precise:

> certify \(\lambda_5(F)>0\), hence finite effective nonpositive index \(\le4\).
