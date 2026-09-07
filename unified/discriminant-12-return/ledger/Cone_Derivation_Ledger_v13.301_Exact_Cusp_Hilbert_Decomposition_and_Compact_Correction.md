# Cone Derivation Ledger v13.301 — Exact Cusp Hilbert Decomposition and Compact-Correction Audit

**Status:** EXACT Si/Ci CUSP MATRIX FORMULA DERIVED — v13.300 COMPACTNESS INTERPRETATION CORRECTED — NONCOMPACT PART IDENTIFIED AS ONE-HALF HILBERT MATRIX — REMAINING CORRECTION NUMERICALLY HILBERT-SCHMIDT-LIKE — RH/GRH NOT PROVED.

## 1. Purpose

v13.300 found that finite high-mode compressions of

\[
C-D_{\log},
\qquad
(D_{\log})_{nn}=\log(n/4),
\]

shrank rapidly and tentatively interpreted the cusp remainder as compact. v13.301 derives the cusp entries exactly and shows that this interpretation was incomplete: the residual contains an explicit bounded but noncompact Hilbert/Hankel operator.

The corrected goal is to write

\[
C=D_{\log}-H_{\rm odd}+K
\]

with the noncompact term explicit and the remaining correction \(K\) small enough to be compact or Hilbert-Schmidt.

## 2. Exact odd-mode overlap

Let

\[
a=\frac{m\pi}{2},\qquad b=\frac{n\pi}{2},
\]

with distinct odd positive integers \(m,n\). For the even-v sector the symmetric overlap from the one-dimensional reduction simplifies exactly to

\[
S_{mn}(t)
=
\frac{2ab}{a^2-b^2}
\left[b\sin(bt)-a\sin(at)\right].
\]

The linear part \(At\) of the cusp is already known from v13.300 to be exactly diagonal, so off-diagonal entries come solely from

\[
\frac12 t\log t.
\]

## 3. Exact sine-integral formula off the diagonal

The elementary special-function integral

\[
J(k)=\int_0^2 t\log t\,\sin(kt)\,dt
\]

has the closed form

\[
J(k)
=
\frac{-(2k\cos2k-\sin2k)\log2+\sin2k-\operatorname{Si}(2k)}{k^2}.
\]

For odd Dirichlet frequencies \(k=n\pi/2\),

\[
\sin(2k)=0,\qquad \cos(2k)=-1,
\]

and therefore

\[
J(k)=\frac{2\log2}{k}-\frac{\operatorname{Si}(2k)}{k^2}.
\]

Substitution into the overlap formula yields, for \(m\ne n\),

\[
\boxed{
C_{mn}
=
\frac{2}{\pi}
\frac{n\,\operatorname{Si}(m\pi)-m\,\operatorname{Si}(n\pi)}{m^2-n^2}.
}
\]

This is an exact formula, not a numerical fit.

## 4. Exact diagonal formula

For \(m=n\), the exact self-overlap is

\[
S_{nn}(t)
=
k_n^2(2-t)\cos(k_nt)-k_n\sin(k_nt),
\qquad
k_n=\frac{n\pi}{2}.
\]

Integrating the singular part and then adding the exact diagonal contribution \(-2A\) from the linear term gives

\[
\boxed{
C_{nn}
=
\log\frac n4
-\operatorname{Ci}(n\pi)
-rac{\operatorname{Si}(n\pi)}{n\pi}.
}
\]

Hence

\[
C_{nn}-\log(n/4)
=
-\operatorname{Ci}(n\pi)
-rac{\operatorname{Si}(n\pi)}{n\pi}.
\]

For odd \(n\), the standard large-argument asymptotics give

\[
\operatorname{Si}(n\pi)
=
\frac\pi2+\frac1{n\pi}+O(n^{-3}),
\]

so

\[
C_{nn}-\log(n/4)
=
-\frac1{2n}+O(n^{-2}).
\]

This exactly matches the leading diagonal of the Hankel kernel \(-1/(m+n)\).

## 5. The missing noncompact term

For \(m\ne n\), insert

\[
\operatorname{Si}(n\pi)=\frac\pi2+\delta_n.
\]

The constant \(\pi/2\) contribution gives

\[
\frac{2}{\pi}
\frac{(\pi/2)(n-m)}{m^2-n^2}
=-\frac1{m+n}.
\]

Therefore

\[
\boxed{
C=D_{\log}-H_{\rm odd}+K,
}
\]

where

\[
(H_{\rm odd})_{mn}=\frac1{m+n}.
\]

Reindexing odd modes by

\[
m=2j+1,\qquad n=2k+1
\]

gives

\[
(H_{\rm odd})_{jk}
=
\frac1{2(j+k+1)}.
\]

Thus \(H_{\rm odd}\) is exactly one-half of the classical Hilbert matrix. Its \(\ell^2\) operator norm is

\[
\boxed{\|H_{\rm odd}\|=\frac\pi2.}
\]

This term is bounded but noncompact. Consequently the v13.300 inference that \(C-D_{\log}\) itself may be compact is false and has been explicitly superseded in that ledger entry.

## 6. Compact/Hilbert-Schmidt candidate after subtracting the Hilbert term

Define

\[
K_{mn}
=
C_{mn}
-\delta_{mn}\log(n/4)
+\frac1{m+n}.
\]

The next term in the odd-integer sine-integral asymptotic gives

\[
K_{mn}\sim -\frac{2}{\pi^2mn}.
\]

This leading correction is rank-one at the level of its asymptotic model and is Hilbert-Schmidt because

\[
\sum_{m,n\ \mathrm{odd}}\frac1{m^2n^2}<\infty.
\]

A full rigorous Hilbert-Schmidt conclusion still requires a uniform remainder estimate for the exact Si/Ci expressions. v13.301 therefore records the global HS property as a theorem target, not as completed proof.

## 7. Numerical Hilbert-Schmidt stabilization

Using the exact formulas above, the Frobenius/Hilbert-Schmidt norm of finite principal sections of \(K\) stabilizes rapidly:

\[
N=10:\quad \|K_N\|_{\rm HS}\approx0.2036223,
\]

\[
N=20:\quad 0.2060975,
\]

\[
N=40:\quad 0.2073373,
\]

\[
N=80:\quad 0.2079576,
\]

\[
N=160:\quad 0.2082677,
\]

\[
N=320:\quad 0.2084228.
\]

This is strongly consistent with a finite Hilbert-Schmidt limit near \(0.2085\).

High-mode partial HS tails, computed out through odd mode 999, fall rapidly:

\[
\|K_{m,n\ge11}\|_{\rm HS}\approx9.98\times10^{-3},
\]

\[
\|K_{m,n\ge21}\|_{\rm HS}\approx4.96\times10^{-3},
\]

\[
\|K_{m,n\ge41}\|_{\rm HS}\approx2.43\times10^{-3},
\]

\[
\|K_{m,n\ge81}\|_{\rm HS}\approx1.17\times10^{-3}.
\]

These are numerical finite-window diagnostics, but unlike the v13.300 compression test they are now applied to the correctly renormalized residual after subtraction of the noncompact Hilbert term.

## 8. Corrected cumulative operator picture

Combining v13.298-v13.301 gives the refined even-v structural model

\[
\boxed{
A_{\rm even}
=
D_{\log}
-H_{\rm odd}
+K_{\rm cusp}
+B_{\rm prime}
+K_{\rm smooth}.
}
\]

Here:

- \(D_{\log}=\operatorname{diag}(\log(n/4))\) is unbounded upward;
- \(H_{\rm odd}\) is explicit, bounded, noncompact, with exact norm \(\pi/2\);
- \(K_{\rm cusp}\) is numerically Hilbert-Schmidt-like and has leading asymptotic \(-2/(\pi^2mn)\);
- \(B_{\rm prime}\) is bounded by the exact finite-shift argument of v13.298;
- \(K_{\rm smooth}\) is bounded by the remainder/pole argument of v13.299.

This is enough to preserve the tail-coercivity strategy: an unbounded diagonal dominates any fixed bounded perturbation. What remains is to turn the cusp correction and smooth-series bounds into fully rigorous constants.

## 9. What is established and what is not

Established exactly:

- the odd-mode overlap simplification;
- the off-diagonal Si formula;
- the diagonal Si/Ci formula;
- the decomposition of the leading noncompact cusp residual as \(-H_{\rm odd}\);
- \(\|H_{\rm odd}\|=\pi/2\).

Strong numerical/asymptotic evidence:

- after subtracting \(D_{\log}-H_{\rm odd}\), the remaining cusp correction is Hilbert-Schmidt;
- its finite HS norm appears to converge near 0.2085;
- its high-mode HS tails decay rapidly.

Not established:

- a uniform analytic Si/Ci remainder estimate sufficient to certify the full HS norm;
- a certified infinite-tail coercivity threshold for the complete Suzuki operator;
- \(\ker G_1\neq\{0\}\), \(\lambda_1=0\), RH, or GRH.

## 10. Next checkpoint

v13.302 should make the Si/Ci remainder estimate quantitative. A clean route is to use the integral/asymptotic remainder representation for \(\operatorname{Si}(x)\) and \(\operatorname{Ci}(x)\) at \(x=n\pi\), derive a uniform bound on

\[
K_{mn}+\frac{2}{\pi^2mn},
\]

and sum its square over odd \(m,n\). Even a conservative analytic constant would convert the cusp correction from a numerical compactness candidate into a rigorous Hilbert-Schmidt operator.

## 11. Files

- `research-notes/suzuki_cusp_exact_hilbert_decomposition.py`
- corrected predecessor: `ledger/Cone_Derivation_Ledger_v13.300_Cusp_Logarithmic_Diagonal_and_Compact_Remainder_Audit.md`
- this ledger entry
