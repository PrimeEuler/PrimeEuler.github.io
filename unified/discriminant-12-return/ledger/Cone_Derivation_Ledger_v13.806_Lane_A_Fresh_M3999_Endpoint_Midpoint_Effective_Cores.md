# Cone Derivation Ledger v13.806 — Fresh \(M=3999\) Endpoint Midpoint Effective Cores at \(\rho=0.10\)

Date: 2026-09-25

Lane: A.

Status: [D] source-faithful endpoint generator formulas; [N] fresh \(M=3999/4000\) structured midpoint Schur eliminations in both parity sectors; [N] effective-core inertia \((4,0,6)\) in both parities; [G] midpoint only, no infinite endpoint inertia theorem yet.

Parents: v13.799, v13.801, v13.804–805.

Research artifact:

- research-notes/suzuki_endpoint_M3999_midpoint_effective_core.py
- commit e266ddaf8b108b26b8da554ce48192c0b197799b.

No GitHub workflow/status run is attached to this research commit.

## 1. Requested endpoint and core/buffer layouts

Use the worst endpoint
\[
\boxed{
F^-_{0.10}
=
A-0.10B_{\rm sm},
\qquad
B_{\rm sm}=D_{\log}-H.
}
\]

The parity tail cores are fixed exactly as requested.

Even-v:
\[
\boxed{
C_+
=
\{5,7,9,11,13,15,17,19,21,23\},
}
\]
\[
\boxed{
F_+
=
\{25,27,\ldots,3999\},
}
\]
with buffer dimension \(1988\).

Odd-v:
\[
\boxed{
C_-
=
\{6,8,10,12,14,16,18,20,22,24\},
}
\]
\[
\boxed{
F_-
=
\{26,28,\ldots,4000\},
}
\]
again with buffer dimension \(1988\).

## 2. Source-faithful accelerated endpoint generator [D]

For the pole-free same-parity source-faithful form,
\[
A_{0,mn}
=
-\frac2\pi
\frac{nZ_m-mZ_n}{n^2-m^2},
\qquad m\ne n.
\]

The endpoint shift from v13.804 is
\[
\boxed{
Z_n\mapsto Z_n-\frac{0.10\pi}{2}.
}
\]

For either parity, the accelerated exact scalar sequence can be written
\[
\boxed{
Z_n
=
2A_n
+
\Im\psi\!\left(
\frac14+\frac{i n\pi}{4}
\right)
-
(-1)^n n\pi
\sum_{k\ge0}
\frac{e^{-2a_k}}
{a_k^2+(n\pi/2)^2},
}
\]
where
\[
a_k=2k+\frac12
\]
and \(A_n\) is the finite prime sine sequence.

For odd \(n\), the last term has the positive sign already used by the historical source-faithful \(M=3999\) verifier.

For even \(n\), the sign reverses because
\[
\cos(n\pi)=+1
\]
in the exponential sine integral. This is the corrected odd-v extension of the same accelerated formula.

The diagonal is assembled independently from
\[
C_{nn}+P_{nn}+K_{{\rm arch},nn}
-
0.10
\left(
\log(n/4)-\frac1{2n}
\right),
\]
where the smooth archimedean diagonal is evaluated by oscillatory-weight quadrature. This avoids the high-frequency adaptive-quadrature failure already documented in the historical branch.

## 3. Structured \(O(N^2)\) buffer elimination [D/N]

The pole-free high buffer retains the exact rank-two displacement representation. A no-pivot structured LDL factorization is generated using the restored v13.387 source-faithful recurrence.

The parity pole is then included as an exact rank-one update:

even-v:
\[
+2c_Fc_F^T,
\]

odd-v:
\[
-2d_Fd_F^T.
\]

The full buffer inverse is applied by Sherman-Morrison about the structured pole-free solve.

This gives the exact finite-dimensional effective core
\[
S
=
F_{CC}
-
F_{CF}F_{FF}^{-1}F_{FC}
\]
at midpoint arithmetic.

## 4. Independent implementation cross-check [N]

Before scaling to \(M=3999\), the same structured implementation was compared with an ordinary dense solve through \(N=256\).

The effective-core operator-norm differences were approximately
\[
\boxed{
2.27\times10^{-16}
\quad\text{(even-v)}
}
\]
and
\[
\boxed{
8.46\times10^{-17}
\quad\text{(odd-v)}.
}
\]

The same fast formulas also reproduce the v13.800 \(N=32\) effective-core levels from the \(10^{-10}\) scale upward essentially digit-for-digit; only the historical \(10^{-15}\) and smaller raw near-null values collapse to binary64 roundoff, as expected.

Thus the fresh M3999 run is on the same corrected source-faithful branch as v13.799–805.

## 5. Even-v \(M=3999\) endpoint core [N]

The pole-free structured buffer has minimum scalar LDL pivot
\[
\boxed{
0.46608173927253421
}
\]
attained at mode
\[
\boxed{n=29}.
\]

The positive-pole Sherman-Morrison denominator is
\[
\boxed{
1.0751351527236084.
}
\]

Hence the finite high buffer is safely invertible at midpoint.

The ten effective-core eigenvalues are
\[
\boxed{
\begin{aligned}
-0.156215549746995,&\\
-0.104520990309778,&\\
-0.0608881633519161,&\\
-0.0292493622873678,&\\
+0.0321649112671556,&\\
+0.925993596010909,&\\
+1.57864148612152,&\\
+1.92030738814565,&\\
+2.30775820778586,&\\
+2.45861549009120.&
\end{aligned}
}
\]

Therefore
\[
\boxed{
\operatorname{inertia}(S_+)
=
(4,0,6).
}
\]

The nearest sign margins are
\[
-0.02924936
\qquad\text{and}\qquad
+0.03216491,
\]
so the midpoint split is not numerically borderline.

## 6. Odd-v \(M=4000\) endpoint core [N]

The corrected odd-v pole-free buffer has minimum scalar LDL pivot
\[
\boxed{
0.51112941830003888
}
\]
attained at mode
\[
\boxed{n=40}.
\]

For the adverse corrected pole term
\[
-2d_Fd_F^T,
\]
the Sherman-Morrison denominator is
\[
\boxed{
0.98700910737674274>0.
}
\]

Thus the negative rank-one pole update does not destroy buffer positivity at midpoint.

The ten effective-core eigenvalues are
\[
\boxed{
\begin{aligned}
-0.148508134494624,&\\
-0.105815425299754,&\\
-0.0662757507718400,&\\
-0.0300224649388448,&\\
+0.659813715712898,&\\
+1.36984099586045,&\\
+1.71006808682916,&\\
+1.91977422748237,&\\
+2.30998613561652,&\\
+2.49050217447450.&
\end{aligned}
}
\]

Therefore
\[
\boxed{
\operatorname{inertia}(S_-)
=
(4,0,6).
}
\]

The fifth level is already
\[
\boxed{
+0.6598137157,
}
\]
so the odd-v positive sector has a particularly large midpoint separation.

## 7. Main conclusion

The fresh theorem-scale midpoint problem lands exactly on the certification architecture anticipated in v13.805:

\[
\boxed{
4\ \text{negative effective-core directions}
+
6\ \text{positive effective-core directions}
}
\]
in **both** parity sectors for
\[
F^-_{0.10}=A-0.10B_{\rm sm}.
\]

Equivalently,
\[
\boxed{
\operatorname{inertia}(S_+)
=
\operatorname{inertia}(S_-)
=
(4,0,6).
}
\]

This is substantially stronger midpoint evidence than the smaller-cutoff resonance plots because the full finite buffers through \(3999/4000\) have now been eliminated on the source-faithful structured branch.

## 8. Certification consequence

The next gate is no longer to search for the correct protected dimension.

It is now to certify the six positive effective-core directions against the infinite remote tails.

For each parity:

1. freeze a fresh six-dimensional basis \(Q_{\rho,\pm}\) spanning the positive effective-core directions;
2. freeze a corresponding preconditioner \(L_{0,\rho,\pm}\);
3. accumulate the normalized remote residual Gram from modes \(4001+\) / \(4002+\);
4. use the exact endpoint large-\(n\) coefficient shift from v13.805;
5. bound the inverse-power remainder analytically;
6. outward-certify
   \[
   H_{\rho,\pm}
   <
   \delta_{\rho,\pm}C_{\rho,\pm}.
   \]

The four negative directions then remain isolated as the only candidates contributing to
\[
\operatorname{ind}_-(F^-_{0.10}).
\]

A separate \(F^+_{0.10}\) replay is still needed to certify zero negative directions at the positive endpoint.

## Guardrail

This entry is a **fresh midpoint M3999 result**, not an interval theorem.

It does not yet certify
\[
\operatorname{ind}_-(F^-_{0.10})=4
\]
for the infinite operator.

No exact-zero, RH, GRH, or \(\kappa_1\) claim follows.

## Result

\[
\boxed{
\textbf{Fresh }M=3999/4000\textbf{ endpoint midpoint cores give inertia }(4,0,6)\textbf{ in both parity sectors.}
}
