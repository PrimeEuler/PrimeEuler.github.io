# Cone Derivation Ledger v13.814 — Independent Audit of v13.813 Four-Negative Endpoint Certificate

Date: 2026-09-25 local / 2026-09-26 UTC.

Lane: A.

Status: [A] independent source-thread audit completed; [P] v13.813 four-negative certificate passes; [H] brittle caps widened and payload checks made fail-closed before final inertia use.

Parents: v13.357, v13.809, v13.812–813.

Hardening commits:

- 022a68cc9338b0cb19a7018c8cda4a1d5813395f — widen brittle caps and make hash/rank checks fail closed in the four-negative verifier;
- 53ace85d1b18b008d0f6dd830d43099eddddbb73 — update v13.813 to the hardened safe margins.

No GitHub workflow/status run is attached.

## 0. Audit method

The four-negative theorem was treated as untrusted.

The audit did not call the v13.813 certificate routine to obtain its target values. Instead it independently:

1. parsed the frozen hexadecimal dyadics;
2. recomputed the canonical SHA-256 payload hashes;
3. evaluated the first \(4\times4\) determinants as exact rational dyadics;
4. rebuilt the current source-faithful \(\rho=0.10\) M3999/4000 endpoint matrices from the midpoint formulas;
5. reconstructed the structured buffer solves;
6. recomputed the four-RHS residual envelopes;
7. recomputed the reference defects and fixed-\(Q\) Schur perturbation budgets;
8. compared the one-sided Schur restriction against the full finite graph quadratic form;
9. tested every hard-coded numerical cap and final assertion;
10. independently checked the explicit endpoint-shift and pole-scalar rounding scale against the \(10^{-14}\) extra endpoint reserve.

A separate clean repository clone was attempted first, but the execution runtime has no outbound DNS. The numerical audit was therefore performed in a clean local notebook from the committed literal payloads and formulas, rather than by invoking the certificate script itself.

## 1. Payload hashes [PASS]

Even-v recomputed SHA-256:

\[
\boxed{
\texttt{40e43622bce7044f9e5bc39a682399d39acaccab2835a68ca2eec892af2cf309}.
}
\]

Odd-v recomputed SHA-256:

\[
\boxed{
\texttt{798cbbcd88c2c035854d5b67432e5b12cf1c04dedac7399873a1bd27211a2395}.
}
\]

Both agree exactly with the frozen input file and v13.813.

The hardened verifier now recomputes these hashes at runtime and fails closed on mismatch.

## 2. Exact rank tests [PASS]

The exact rational determinant of the first four rows of the even-v \(10\times4\) payload is nonzero:

\[
\det Q_{4,e}[1:4]
\approx
-1.1303249120999483\times10^{-3}.
\]

For odd-v:

\[
\det Q_{4,o}[1:4]
\approx
8.598312917723064\times10^{-2}.
\]

Hence both frozen payloads have rank four exactly.

Independent numerical full-matrix checks give

\[
\operatorname{rank}(Q_{4,e})=4,
\qquad
\|Q_{4,e}^TQ_{4,e}-I\|_2
\approx1.4604\times10^{-15},
\]

\[
\operatorname{rank}(Q_{4,o})=4,
\qquad
\|Q_{4,o}^TQ_{4,o}-I\|_2
\approx7.0495\times10^{-16}.
\]

The hardened verifier now checks the exact first-four determinant at runtime.

## 3. Independent M3999/4000 reconstruction [PASS]

The endpoint

\[
F^-_{0.10}=A-0.10B_{\rm sm}
\]

was rebuilt independently on the current corrected source-faithful branch.

The independently reconstructed negative restricted spectra are

even-v:
\[
-0.15621555,\ 
-0.10452099,\ 
-0.06088816,\ 
-0.02924936,
\]

odd-v:
\[
-0.14850813,\ 
-0.10581543,\ 
-0.06627575,\ 
-0.03002246.
\]

These reproduce the v13.806/v13.813 midpoint sign pattern.

## 4. Structured factor and conditioning data [PASS]

Even-v:

\[
\|A_0-LDL^T\|_2
\le
\|A_0-LDL^T\|_F
<
5.46527249\times10^{-11}.
\]

The independently recomputed inverse-factor bounds are

\[
\|L^{-1}\|_\infty<4.614605,
\]

\[
\|L^{-1}\|_1<44.506232,
\]

\[
\|L^{-1}\|_2<14.331038.
\]

This gives

\[
\mu_e^{\rm nominal}
>
0.0022693778644627.
\]

Odd-v:

\[
\|A_0-LDL^T\|_F
<
5.46837029\times10^{-11},
\]

\[
\|L^{-1}\|_\infty<5.015670,
\]

\[
\|L^{-1}\|_1<55.947633,
\]

\[
\|L^{-1}\|_2<16.751562.
\]

The corrected negative-pole denominator is independently reproduced as

\[
\boxed{
1-2d_F^T(A_0)^{-1}d_F
>
0.987009107376726.
}
\]

Hence

\[
\mu_o^{\rm nominal}
>
0.0018214088932311.
\]

Subtracting the common exact-vs-nominal budget

\[
\epsilon_F=2.1\times10^{-13}
\]

leaves positive exact buffer floors in both sectors.

## 5. Original hard-coded cap audit [PASS, but brittle]

The original v13.813 caps all pass.

### Even-v

Frozen coupling:
\[
\|F_{FC}Q_{4,e}\|_F
=
0.668899957380299
<
0.670.
\]

Headroom: approximately \(0.164\%\).

Four-RHS outward residual:
\[
8.157032524651205\times10^{-16}
<
8.20\times10^{-16}.
\]

Headroom: approximately \(0.524\%\).

Reference defect:
\[
2.655197910063368\times10^{-16}
<
2.70\times10^{-16}.
\]

Headroom: approximately \(1.66\%\).

### Odd-v

Frozen coupling:
\[
0.244099127776522
<
0.245.
\]

Headroom: approximately \(0.368\%\).

Four-RHS outward residual:
\[
2.267064235953721\times10^{-16}
<
2.30\times10^{-16}.
\]

Headroom: approximately \(1.43\%\).

Reference defect:
\[
1.242557451366109\times10^{-16}
<
1.30\times10^{-16}.
\]

Headroom: approximately \(4.42\%\).

Conclusion:

\[
\boxed{
\text{the original certificate passes, but several caps are unnecessarily close to platform-level arithmetic variation.}
}
\]

## 6. Hardened fail-closed caps

Commit 022a68cc9338b0cb19a7018c8cda4a1d5813395f replaces the brittle caps by

even-v:
\[
K_Q<0.680,
\qquad
r_{\rm solve}<9.00\times10^{-16},
\qquad
\epsilon_{\rm ref}<3.20\times10^{-16},
\]

odd-v:
\[
K_Q<0.255,
\qquad
r_{\rm solve}<2.60\times10^{-16},
\qquad
\epsilon_{\rm ref}<1.60\times10^{-16}.
\]

The exact rank/hash checks are also executed inside the theorem verifier.

Recomputing the full scalar perturbation budget with these wider caps gives

even-v:
\[
\epsilon_{{\rm neg},e}
<
1.89812\times10^{-8},
\]

odd-v:
\[
\epsilon_{{\rm neg},o}
<
4.17514\times10^{-9}.
\]

Therefore the recommended hardened margins are

\[
\boxed{
-Q_{4,e}^TS_{e,\rm exact}Q_{4,e}
>
0.0292493433\,I,
}
\]

\[
\boxed{
-Q_{4,o}^TS_{o,\rm exact}Q_{4,o}
>
0.0300224607\,I.
}
\]

Normalized:

\[
\boxed{
>0.99999935\,I
\quad\text{(even-v)},
}
\]

\[
\boxed{
>0.99999986\,I
\quad\text{(odd-v)}.
}
\]

The sign theorem is unchanged.

## 7. Schur-versus-full finite graph form [PASS]

This check was performed by a second algebraic path.

For the dressed graph vector

\[
W=
\begin{pmatrix}
Q_4\\
-Y
\end{pmatrix},
\]

the full finite block quadratic form

\[
W^T
\begin{pmatrix}
F_{CC}&F_{CF}\\
F_{FC}&F_{FF}
\end{pmatrix}
W
\]

was evaluated independently and compared with

\[
Q_4^TF_{CC}Q_4
-
(F_{FC}Q_4)^TY.
\]

The operator-norm discrepancies are

\[
\boxed{
7.88499\times10^{-16}
\quad\text{(even-v)},
}
\]

\[
\boxed{
6.33003\times10^{-17}
\quad\text{(odd-v)}.
}
\]

The verifier's conservative graph consistency bounds after hardening are approximately

\[
5.7243\times10^{-15}
\quad\text{and}\quad
5.0478\times10^{-15}.
\]

Thus the independent full-form check is safely inside the residual envelope.

The independently evaluated full graph spectra remain strictly negative with the same four midpoint eigenvalues.

## 8. Residual envelope decomposition [PASS]

The outward four-RHS residual decomposes into point residual plus long-double rounding envelope.

Even-v:

\[
r_{\rm point}
\approx5.93917\times10^{-16},
\]

\[
r_{\rm round}
\approx2.21787\times10^{-16},
\]

\[
r_{\rm total}
\approx8.15703\times10^{-16}.
\]

Odd-v:

\[
r_{\rm point}
\approx1.67407\times10^{-16},
\]

\[
r_{\rm round}
\approx5.92991\times10^{-17},
\]

\[
r_{\rm total}
\approx2.26706\times10^{-16}.
\]

The reference-defect envelopes likewise reproduce:

even-v:
\[
2.15045\times10^{-16}
+
5.04750\times10^{-17}
=
2.65520\times10^{-16},
\]

odd-v:
\[
1.18587\times10^{-16}
+
5.66864\times10^{-18}
=
1.24256\times10^{-16}.
\]

No hidden cancellation is being used in the outward caps.

## 9. Audit of \(\epsilon_F=2.1\times10^{-13}\)

The inherited source/operator budget

\[
2.0\times10^{-13}
\]

was traced back to v13.357, where the dominant archimedean operator uncertainty is bounded dimension-freely and the prime/cusp scalar data are allowed to be over-resolved.

The endpoint certificate adds the explicit reserve

\[
10^{-14}.
\]

An independent 100-digit comparison of the explicit endpoint modification on the actual M3999/4000 parity blocks gives observed errors far below this reserve.

For the \(0.10B_{\rm sm}\) shift, the maximum absolute row-sum error is below

\[
1.78\times10^{-16}
\]

in even-v and

\[
1.74\times10^{-16}
\]

in odd-v.

For the rank-one pole reconstruction, a direct high-precision vector comparison gives operator-error bounds below

\[
1.39\times10^{-16}
\quad\text{(even-v)},
\]

\[
1.38\times10^{-17}
\quad\text{(odd-v)}.
\]

Thus the extra \(10^{-14}\) endpoint/pole reserve has more than thirtyfold slack relative to the observed explicit additions.

The \(2\times10^{-13}\) source budget remains an inherited validated input from v13.357 rather than being re-proved from first principles in this audit.

## 10. Platform arithmetic assumption [PASS]

The replay platform reports

\[
\epsilon_{\rm longdouble}
=
1.084202172485504434\times10^{-19}
=
2^{-63},
\]

i.e. a 64-bit significand.

Thus the use of

\[
u_{\rm LD}
=
\epsilon_{\rm longdouble}/2
\]

in the \(\gamma_n\) dot-product envelopes matches the intended arithmetic model.

## 11. Final audit verdict

No hash, rank, sign, transpose, residual, conditioning, or cap failure was found.

The only issue found was proof-engineering brittleness in the original hard-coded caps. That issue is now removed by the widened fail-closed constants and runtime hash/rank checks.

Therefore the audited four-negative theorem may be used with the hardened margins

\[
\boxed{
-Q_{4,e}^TS_{e,\rm exact}Q_{4,e}
>
0.0292493433\,I,
}
\]

\[
\boxed{
-Q_{4,o}^TS_{o,\rm exact}Q_{4,o}
>
0.0300224607\,I.
}
\]

Together with the independent codimension-four positive certificate of v13.812, this supports

\[
\boxed{
\operatorname{ind}_{-}(F^-_{0.10,e,\rm tail})
=
\operatorname{ind}_{-}(F^-_{0.10,o,\rm tail})
=
4,
}
\]

with zero kernel at the minus tail endpoint.

The theorem remains scoped to the bulk-subtracted parity tail. The separate two-mode low-core Feshbach problem and the plus endpoint remain outside this claim.
