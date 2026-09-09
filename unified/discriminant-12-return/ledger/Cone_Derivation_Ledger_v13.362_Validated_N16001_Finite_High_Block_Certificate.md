# Cone Derivation Ledger v13.362 — Validated N=16001 Finite High-Block Certificate

## Status

This checkpoint upgrades the pole-free finite high-block estimate from a numerical target to a validated computational certificate under the explicitly stated arithmetic model.

Target block:

\[
B=A_{0,[21,16001]}-0.22I,
\qquad \dim B=7991.
\]

The structured no-pivot LDL factorization uses the exact displacement-rank-two representation

\[
XA_0-A_0X=\frac{2}{\pi}(uv^T-vu^T),
\qquad X=\operatorname{diag}(n^2),
\qquad u_n=Z_n,
\qquad v_n=n,
\]

with

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n.
\]

## Provenance-clean scalar construction

All factorization midpoints are generated from the same high-precision formulas used to establish the scalar enclosures:

- prime/log/sqrt/trigonometric quantities from high-precision direct formulas;
- cusp quantities for all modes \(n\ge21\) from the asymptotic \(\operatorname{Si}/\operatorname{Ci}\) expansions with explicit first-omitted bounds;
- archimedean quantities from the exact rational degree-65 polynomial \(h_{32}\) and the exact \(I_p/J_p\) recurrence.

A 60-digit interval audit gives representative/worst scalar arithmetic radii

\[
\max_{21\le n\le16001}\operatorname{rad}(A_n)<2.15\times10^{-56},
\]

\[
\operatorname{rad}(\text{prime diagonal})<1.01\times10^{-56},
\]

\[
\operatorname{rad}(\operatorname{Si}/\operatorname{Ci}\text{ at }n=21)<7.0\times10^{-30},
\]

and arch polynomial arithmetic radius below \(5\times10^{-62}\).

The dominant exact-vs-polynomial uncertainty is therefore the already established dimension-free archimedean kernel remainder

\[
\boxed{\|\Delta K_{\rm arch}\|_2<1.2180332746458045\times10^{-13}}.
\]

## Validated structured LDL transcript

The structured recurrence was run in NumPy `longdouble` on a runtime reporting a 64-bit significand, with unit roundoff

\[
u=2^{-64}.
\]

Each Schur update was charged with the conservative local round-to-nearest error model developed in v13.359, and local Frobenius defects were composed globally.

Validated transcript:

\[
\boxed{\min_j d_j=0.25429962364429952527},
\]

attained at mode

\[
\boxed{n=29}.
\]

Factor-growth statistics:

\[
\boxed{\||L|\|_1=43.63817093391197109},
\]

\[
\boxed{\||L|\|_\infty=3.7433565044520330225}.
\]

Accumulated local Frobenius defect:

\[
\boxed{\sum_k\delta_k=2.2801510695454563477\times10^{-11}}.
\]

Crude global arithmetic residual bound:

\[
\boxed{\|E_{\rm arith}\|_2\le3.7247004439625295956\times10^{-9}}.
\]

The sharper prefix-weighted composition gives

\[
3.5190480723800255652\times10^{-9}.
\]

Adding the matrix-construction uncertainty gives the conservative total

\[
\boxed{\|E_{\rm total}\|_2<3.724822247289995\times10^{-9}}.
\]

## Positivity conclusion

The previously derived sufficient a-posteriori residual allowance was

\[
\|E_{\rm total}\|_2<3.15\times10^{-6}.
\]

The validated transcript also satisfies the stronger design guards

\[
\min_j d_j>0.25,
\qquad
\|E_{\rm arith}\|_2<10^{-8},
\qquad
\|E_{\rm matrix}\|_2<2\times10^{-13}.
\]

Hence, under the stated validated-arithmetic model,

\[
\boxed{B>0},
\]

and therefore

\[
\boxed{A_{0,[21,16001]}\succeq0.22I}.
\]

This closes the finite high-block component of the global high-complement argument.

## Remaining global high-complement obligations

To prove positivity of the entire infinite high complement

\[
\mathcal D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\text{ odd}\},
\]

we still need rigorous completion of both

\[
\boxed{\|A_{0,[21,16001],[16003,\infty)}\|<1}
\]

and the analytic tail gap at \(N=16003\), including a fully interval-certified proof of the robust prime-operator target

\[
\boxed{\|B_{\rm prime}\|<2.05}.
\]

Once those close, the Schur estimate gives a positive lower bound for \(A_0|_{\mathcal D}\), after which the PSD pole can be restored.

## Guardrail

This checkpoint does **not** prove positivity of the full infinite high complement by itself. It does **not** establish a global index bound, an exact zero, RH, or GRH. The remaining cross and infinite-tail inequalities must still be certified.
