# Cone Derivation Ledger v13.298

## Asymptotic matrix anatomy and bounded prime-shift structure

**Status:** ASYMPTOTIC HIGH-MODE STRUCTURE IDENTIFIED — GROWING ARCHIMEDEAN DIAGONAL + BOUNDED PRIME SHIFT OPERATOR + LOWER-ORDER SMOOTH REMAINDER. INFINITE-TAIL COERCIVITY NOT YET CERTIFIED. RH/GRH NOT PROVED.

This checkpoint continues v13.297. The goal is to understand why the high-mode even-v block becomes increasingly invertible and whether that behavior can be promoted from a finite-section observation to an infinite-tail estimate.

## 1. Even-v high-mode basis

At a=1, even v corresponds to odd Dirichlet indices n=1,3,5,... with

\[
\psi_n(x)=\sin\!\left(\frac{n\pi(x+1)}2\right),\qquad
k_n=\frac{n\pi}{2}.
\]

For the derivative modes, the exact symmetric self-overlap used in the 1-D kernel reduction is

\[
S_{nn}(t)=k_n^2(2-t)\cos(k_nt)-k_n\sin(k_nt).
\]

## 2. Local cusp produces the growing diagonal

Suzuki's local expansion is

\[
g(t)=\frac12 |t|\log|t|+A|t|+O(t^2),\qquad
A=\frac12(\log(2\pi)+\gamma-1).
\]

Define

\[
s(t)=\frac12 t\log t+At,\qquad t>0.
\]

High-precision evaluation of

\[
A^{\rm cusp}_{nn}=\int_0^2 s(t)S_{nn}(t)\,dt
\]

shows

\[
A^{\rm cusp}_{nn}=\log n-\log4+o(1)
\]

for odd n. Representative errors in
\(A^{\rm cusp}_{nn}-(\log n-\log4)\) are approximately

- n=21: -2.43e-2,
- n=31: -1.63e-2,
- n=41: -1.23e-2,
- n=61: -8.25e-3.

Thus the archimedean cusp provides the only observed logarithmically growing diagonal term.

The full archimedean diagonal approaches the cusp diagonal, while the pole contribution decays. For example at n=31,

\[
A^{\rm arch}_{31,31}\approx2.03102,\qquad
A^{\rm cusp}_{31,31}\approx2.03135,\qquad
A^{\rm pole}_{31,31}\approx0.00429.
\]

## 3. Exact prime-ramp diagonal formula

For one ramp

\[
h_\ell(t)=(t-\ell)_+,
\]

direct integration gives, for odd n,

\[
\boxed{
\int_\ell^2 h_\ell(t)S_{nn}(t)\,dt
=(\ell-2)\cos(k_n\ell)-\frac{\sin(k_n\ell)}{k_n}
}
\]

with \(k_n=n\pi/2\).

Therefore each prime-power ramp contributes only an O(1) oscillatory term to the diagonal. At a=1 the only prime-power breakpoints are

\[
\log2,\ \log3,\ \log4,\ \log5,\ \log7.
\]

The prime diagonal is consequently a finite bounded oscillatory sum. This explains features such as the n=11 shoulder seen in v13.297: the anomalously small full diagonal there comes from cancellation between the growing archimedean term and a negative prime oscillation, not from loss of the archimedean asymptotic.

Representative decomposition:

- n=11: pole +0.0340, prime -0.9288, arch +0.9618, full +0.0670;
- n=13: pole +0.0244, prime +0.6467, arch +1.1371, full +1.8081;
- n=31: pole +0.00429, prime +1.2553, arch +2.0310, full +3.2906.

## 4. Prime ramps are bounded shift operators

The diagonal formula is part of a stronger operator identity. For the even kernel

\[
r_\ell(t)=(|t|-\ell)_+,
\]

distributionally

\[
r_\ell''(t)=\delta(t-\ell)+\delta(t+\ell).
\]

For v in H_0^1(-1,1), two integrations by parts give

\[
Q_\ell(v)
=\iint v'(x)r_\ell(x-y)v'(y)\,dx\,dy
=-\int v(x)\,[v(x-\ell)+v(x+\ell)]\,dx,
\]

where the shifted functions are understood as zero outside [-1,1].

Hence each ramp defines a truncated-shift operator with

\[
\|B_\ell\|_{L^2\to L^2}\le2.
\]

For Suzuki's a=1 prime term,

\[
B_{\rm prime}=\sum_{q\in\{2,3,4,5,7\}}
\frac{\Lambda(q)}{\sqrt q}\,B_{\log q},
\]

so the triangle inequality gives the explicit crude bound

\[
\boxed{
\|B_{\rm prime}\|\le
2\sum_{q\in\{2,3,4,5,7\}}\frac{\Lambda(q)}{\sqrt q}
\approx5.85247.
}
\]

This is an actual operator bound for the prime part, not a finite-matrix fit.

## 5. Emerging high-mode operator model

The evidence now supports the decomposition

\[
\boxed{
A_{\rm even}
=D_{\log}+B_{\rm prime}+K_{\rm lower},
}
\]

with

\[
(D_{\log}c)_n=(\log n-\log4)c_n,
\]

where

- \(D_{\log}\) is an unbounded positive diagonal operator;
- \(B_{\rm prime}\) is bounded by the shift-operator argument above;
- \(K_{\rm lower}\) consists of the smooth pole contribution plus the difference between the full archimedean term and the local cusp model.

Numerically, the latter pieces decay in the diagonal and appear lower order off-diagonal.

If one can prove a uniform bound

\[
\|K_{\rm lower}\|\le C_K<\infty,
\]

then for sufficiently large odd cutoff N,

\[
\log N-\log4>\|B_{\rm prime}\|+C_K
\]

would imply coercivity of the infinite tail by a direct perturbative estimate.

This would be the infinite-dimensional counterpart of the finite tail-resolvent behavior observed in v13.297.

## 6. What is established vs not established

Established here:

1. exact single-ramp diagonal formula;
2. exact truncated-shift representation of each prime ramp on H_0^1;
3. explicit bounded-operator estimate for the full prime-ramp sum at a=1;
4. high-precision evidence that the archimedean cusp diagonal follows \(\log n-\log4\);
5. high-precision evidence that the pole and archimedean remainder are lower order.

Not established:

- a rigorous asymptotic formula with error bound for every matrix entry;
- a certified operator norm bound for the full archimedean remainder;
- infinite-tail coercivity;
- nontriviality of ker(G_1);
- \(\lambda_1=0\);
- RH or GRH.

## 7. Next target: v13.299

The next checkpoint should isolate the archimedean remainder

\[
r(t)=g_{\rm arch}(t)-\left(\frac12 t\log t+At\right)
\]

and prove or numerically calibrate derivative regularity sufficient to bound the associated matrix/operator. Since r(t)=O(t^2) at the origin and is smooth on [0,2], repeated integration by parts should yield quantitative Fourier decay. The aim is to turn K_lower from a numerically lower-order remainder into a rigorously bounded (ideally compact) perturbation.

Only after that step should the logarithmic diagonal dominance be promoted into a genuine infinite-tail coercivity statement.
