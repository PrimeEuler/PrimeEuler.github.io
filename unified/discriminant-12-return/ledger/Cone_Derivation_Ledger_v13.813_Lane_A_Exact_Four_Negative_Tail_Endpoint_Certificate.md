# Cone Derivation Ledger v13.813 — Exact Four-Negative Tail Endpoint Certificate at \(\rho=0.10\)

Date: 2026-09-26

Lane: A.

Status: [D] exact-dyadic four-direction freezes; [C] outward finite-buffer negativity certificates in both parity tails; [C] together with v13.812, exact minus-tail endpoint inertia four in both parities; [G] plus endpoint and \(\rho=0.02\) pair remain separate gates; [G] two-mode low-core Feshbach problem remains separate from this tail theorem.

Parents: v13.806–812.

Research artifacts:

- research-notes/suzuki_endpoint_M3999_frozen_four_negative_inputs.py
- commit 2b60156b8fbdafaa41bf788332a9d6e12b50f634

- research-notes/suzuki_endpoint_M3999_four_negative_certificate.py
- commit bcbdd498a03da33c491bf53dd31af68583fe3819

Additional script-hygiene hardening:

- commit 5278103abfbb8d4be4791c2c926903dc19200c95 adds fail-closed runtime checks of the frozen \(L_0^{-1}\) and normalized dressed-plane norm caps used by the v13.812 terminal remote-Gram verifier.

No GitHub workflow/status run is attached.

## 1. Scope

The operator certified here is the bulk-subtracted parity-tail minus endpoint

\[
F^-_{0.10}=A-0.10B_{\rm sm}
\]

on the tails

\[
n=5,7,9,\ldots
\quad\text{(even-v)}
\]

and

\[
n=6,8,10,\ldots
\quad\text{(odd-v)}.
\]

The first two parity modes retained in the separate low-core Feshbach problem are not part of this theorem.

The target is the four-dimensional complement of the six positive frozen directions certified in v13.812.

## 2. Independent midpoint reconstruction

Before freezing any negative direction, the fresh source-faithful M3999/4000 midpoint problem was reconstructed independently from the current corrected formulas.

The ten effective-core eigenvalues agree with v13.806 digit-for-digit at the displayed precision.

Even-v:

\[
-0.156215549747,\ 
-0.104520990310,\ 
-0.060888163352,\ 
-0.029249362287,
\]

followed by six positive values.

Odd-v:

\[
-0.148508134495,\ 
-0.105815425300,\ 
-0.066275750772,\ 
-0.030022464939,
\]

followed by six positive values.

Thus the negative freezes below are generated from the current corrected source-faithful branch, not from an archived payload.

## 3. Exact-dyadic four-direction freezes [D]

Column signs are canonicalized by requiring the largest-magnitude component to be positive.

The frozen \(10\times4\) negative bases and \(4\times4\) Cholesky factors of

\[
-Q_4^TS_{\rm mid}Q_4
\]

are stored as exact IEEE-754 hexadecimal dyadics.

Even-v payload SHA-256:

\[
\boxed{
\texttt{40e43622bce7044f9e5bc39a682399d39acaccab2835a68ca2eec892af2cf309}.
}
\]

Odd-v payload SHA-256:

\[
\boxed{
\texttt{798cbbcd88c2c035854d5b67432e5b12cf1c04dedac7399873a1bd27211a2395}.
}
\]

The exact rational determinants of the first \(4\times4\) row minors are nonzero.

Decimal diagnostics:

\[
\det Q_{4,e}[1:4]\approx-1.13032491210\times10^{-3},
\]

\[
\det Q_{4,o}[1:4]\approx8.59831291772\times10^{-2}.
\]

Hence both frozen bases have rank four exactly.

## 4. Fresh four-RHS buffer solves [C]

The finite buffers are the same positive blocks certified in v13.809:

even-v:
\[
\{25,27,\ldots,3999\},
\]

odd-v:
\[
\{26,28,\ldots,4000\}.
\]

The exact-vs-nominal endpoint operator budget remains

\[
\epsilon_F=2.1\times10^{-13}.
\]

The fresh four-direction coupling norms are

\[
\|F_{FC}Q_{4,e}\|_2
<
0.670,
\]

\[
\|F_{FC}Q_{4,o}\|_2
<
0.245.
\]

The outward long-double four-RHS residuals satisfy

\[
\boxed{
\|B_{Q,e}-F_{FF,e}\widehat Y_e\|_2
<
8.20\times10^{-16},
}
\]

\[
\boxed{
\|B_{Q,o}-F_{FF,o}\widehat Y_o\|_2
<
2.30\times10^{-16}.
}
\]

The same independently certified buffer floors from v13.809 are used:

\[
\mu_e>0.00226937786425,
\]

\[
\mu_o>0.00182140889302.
\]

For odd-v the corrected negative-pole Sherman-Morrison denominator remains

\[
\boxed{
>0.9870091073767.
}
\]

## 5. Frozen reference checks [C]

The exact dyadic Gram/Gershgorin lower bounds for the negative midpoint references are

\[
\lambda_{\min}
(L_{{\rm neg},e}L_{{\rm neg},e}^T)
>
0.02924936228736769,
\]

\[
\lambda_{\min}
(L_{{\rm neg},o}L_{{\rm neg},o}^T)
>
0.03002246493884458.
\]

The outward reference-formation defects satisfy

\[
\epsilon_{{\rm ref},e}
<
2.70\times10^{-16},
\]

\[
\epsilon_{{\rm ref},o}
<
1.30\times10^{-16}.
\]

The source/operator Schur perturbation bounds are

\[
\epsilon_{{\rm source},e}
<
1.843\times10^{-8},
\]

\[
\epsilon_{{\rm source},o}
<
3.857\times10^{-9}.
\]

The finite-solve contributions are below

\[
2.43\times10^{-13}
\quad\text{and}\quad
3.10\times10^{-14}.
\]

## 6. Independent graph-form consistency check

The certificate does not rely on only one algebraic implementation.

Let

\[
Y\approx F_{FF}^{-1}F_{FC}Q_4.
\]

The one-sided Schur expression

\[
Q_4^TF_{CC}Q_4
-
(F_{FC}Q_4)^TY
\]

is compared independently against the full graph quadratic form of

\[
\begin{pmatrix}
Q_4\\
-Y
\end{pmatrix}.
\]

The discrepancies are

\[
7.26\times10^{-16}
\quad\text{(even-v)},
\]

\[
4.58\times10^{-17}
\quad\text{(odd-v)},
\]

well below conservative residual-based envelopes of approximately

\[
5.66\times10^{-15},
\qquad
5.05\times10^{-15}.
\]

This independently checks the signs, transposes, and graph convention used by the Schur calculation.

## 7. Rigorous four-direction negativity [C]

Combining all finite-side charges gives

\[
\epsilon_{{\rm neg},e}
<
1.843\times10^{-8},
\]

\[
\epsilon_{{\rm neg},o}
<
3.857\times10^{-9}.
\]

Therefore

\[
\boxed{
-Q_{4,e}^TS_{e,\rm exact}Q_{4,e}
>
0.0292493438\,I,
}
\]

\[
\boxed{
-Q_{4,o}^TS_{o,\rm exact}Q_{4,o}
>
0.0300224610\,I.
}
\]

In normalized frozen coordinates,

\[
\boxed{
L_{{\rm neg},e}^{-1}
(-Q_{4,e}^TS_{e,\rm exact}Q_{4,e})
L_{{\rm neg},e}^{-T}
>
0.99999936\,I,
}
\]

\[
\boxed{
L_{{\rm neg},o}^{-1}
(-Q_{4,o}^TS_{o,\rm exact}Q_{4,o})
L_{{\rm neg},o}^{-T}
>
0.99999987\,I.
}
\]

Thus each parity tail has an exact four-dimensional negative graph subspace.

The remote coordinate of these trial vectors is chosen identically zero, so no remote-tail estimate enters this lower-index argument.

## 8. Exact minus-tail endpoint inertia [C]

v13.812 certifies an infinite remote-corrected positive subspace of codimension four in each parity tail. Hence

\[
\operatorname{ind}_{\le0}(F^-_{0.10,\rm tail})
\le4.
\]

The present four-dimensional strict negative subspaces give

\[
\operatorname{ind}_{-}(F^-_{0.10,\rm tail})
\ge4.
\]

Therefore

\[
\boxed{
\operatorname{ind}_{-}(F^-_{0.10,e,\rm tail})=4,
\qquad
\ker F^-_{0.10,e,\rm tail}=\{0\},
}
\]

and

\[
\boxed{
\operatorname{ind}_{-}(F^-_{0.10,o,\rm tail})=4,
\qquad
\ker F^-_{0.10,o,\rm tail}=\{0\}.
}
\]

Equivalently,

\[
\boxed{
\operatorname{ind}_{-}(F^-_{0.10,\rm tail})=4
}
\]

in each parity sector, with no endpoint zero mode.

## 9. Resonance consequence and remaining gates

For the compact relative tail operator

\[
J=I+K,
\]

the minus endpoint is

\[
F^-_{0.10}\sim J-0.10I.
\]

Thus the certified tail inertia gives four generalized eigenvalues below \(+0.10\) in each parity tail.

To turn this into the full fifth-exclusion statement

\[
N(0.10)=4,
\]

the plus endpoint

\[
F^+_{0.10}\sim J+0.10I
\]

still must be certified to have zero negative directions.

The tighter cluster statement

\[
N(0.02)=4
\]

also requires the corresponding plus/minus endpoint pair at \(\rho=0.02\).

The separate two-mode low-core Feshbach problem remains outside this tail theorem.

## Result

\[
\boxed{
\textbf{The four complementary tail directions are rigorously negative in both parity sectors.}
}
\]

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

This closes the \(\rho=0.10\) minus endpoint of the four-resonance certification.
