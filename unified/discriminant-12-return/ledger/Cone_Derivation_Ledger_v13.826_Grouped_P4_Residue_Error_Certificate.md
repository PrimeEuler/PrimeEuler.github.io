# Cone Derivation Ledger v13.826 — Uniform Grouped-Residue Error Bound from the Certified Numerical \(P_4\) Basis

Date: 2026-09-26.

Lane: A.

Status: [C] uniform operator and Loewner-order error bound for the grouped residue matrix \(C(\delta)^*P_4C(\delta)\) over \(|\delta|\le0.02\); [C] source-faithful uniform coupling cap in both parity sectors; [G] no individual-residue decomposition or low-core zero count promoted yet.

Parents: v13.823–825.

Research artifact:

- research-notes/suzuki_grouped_residue_error_certificate.py
  - initial certificate commit 8caebed4975d040770ede22b8f0d4323e8d11021
  - smooth-bulk model-reserve hardening e34faa89a54f0a0d97f00f050a327cbe8e2aa1d5

External Audit Round 108, v13.825, independently replayed and confirmed the full v13.824 residual-certified \(P_4\) basis and the sharpened projector-error arithmetic used below.

No GitHub workflow/status run is attached to the present grouped-residue certificate.

## 1. Exact and numerical grouped residues

For one parity sector, define the exact grouped residue matrix

\[
G(\delta)
=
C(\delta)^*P_4C(\delta),
\]

where

\[
C(\delta)
=
B_T^{-1/2}F_{TC}(\delta),
\qquad
|\delta|\le0.02.
\]

Let

\[
\widehat P_4
\]

be the orthogonal projector onto the residual-certified numerical four-space of v13.824.

The corresponding numerical grouped residue is

\[
\widehat G(\delta)
=
C(\delta)^*\widehat P_4C(\delta).
\]

Because \(P_4\) and \(\widehat P_4\) have the same rank,

\[
\boxed{
\|P_4-\widehat P_4\|
=
\|\sin\Theta\|.
}
\]

The externally replayed sharpened v13.824 bounds are

\[
\boxed{
\|P_{4,e}-\widehat P_{4,e}\|<0.332,
}
\]

\[
\boxed{
\|P_{4,o}-\widehat P_{4,o}\|<0.361.
}
\]

## 2. Basic projector-to-residue inequality

The exact difference is

\[
G(\delta)-\widehat G(\delta)
=
C(\delta)^*
(P_4-\widehat P_4)
C(\delta).
\]

Since

\[
-\epsilon_P I
\preceq
P_4-\widehat P_4
\preceq
\epsilon_P I,
\]

one immediately obtains the stronger matrix inequality

\[
\boxed{
-\epsilon_P C(\delta)^*C(\delta)
\preceq
G(\delta)-\widehat G(\delta)
\preceq
\epsilon_P C(\delta)^*C(\delta).
}
\]

Therefore

\[
\boxed{
\|G(\delta)-\widehat G(\delta)\|
\le
\epsilon_P\|C(\delta)\|^2.
}
\]

Thus only a uniform coupling cap remains to be certified.

## 3. Uniform coupling reduction to the two endpoint values

The low-core/tail coupling is affine in the generalized spectral parameter:

\[
F_{TC}(\delta)
=
A_{TC}-\delta B_{TC}.
\]

Hence

\[
C(\delta)
=
B_T^{-1/2}
(A_{TC}-\delta B_{TC})
\]

is an affine operator-valued function of \(\delta\).

The operator norm of an affine map is convex. Therefore on the real interval

\[
[-0.02,0.02]
\]

one has

\[
\boxed{
\sup_{|\delta|\le0.02}\|C(\delta)\|
=
\max\{
\|C(-0.02)\|,
\|C(+0.02)\|
\}.
}
\]

Consequently only the two endpoint couplings need to be certified.

## 4. Finite \(B_T\)-energy solve

For the finite tail block

even-v:
\[
\{5,7,\ldots,3999\},
\]

odd-v:
\[
\{6,8,\ldots,4000\},
\]

let

\[
B_{FF}X_\delta
=
F_{FC}(\delta)
\]

be the finite smooth-bulk energy solve.

The observed endpoint data are:

### even-v

At \(\delta=-0.02\),

\[
\|X\|_2
\approx0.08424463,
\]

\[
\lambda_{\max}^{1/2}
(X^TB_{FF}X)
\approx0.04342827.
\]

At \(\delta=+0.02\),

\[
\|X\|_2
\approx0.27485285,
\]

\[
\lambda_{\max}^{1/2}
(X^TB_{FF}X)
\approx0.07154881.
\]

The widened caps are

\[
\boxed{
\|X\|_2<0.28,
\qquad
\lambda_{\max}^{1/2}(X^TB_{FF}X)<0.072.
}
\]

### odd-v

The two endpoint solves satisfy

\[
\|X\|_2<0.24,
\]

and

\[
\lambda_{\max}^{1/2}
(X^TB_{FF}X)
<
0.201.
\]

The outward long-double solve residual caps are

\[
\boxed{
r_{F,e}<1.0\times10^{-16},
}
\]

\[
\boxed{
r_{F,o}<1.5\times10^{-16}.
}
\]

## 5. Infinite remote residual

Embed the finite solution \(X\) by zero into the full parity tail.

The remote residual is

\[
r_R(\delta)
=
F_{RC}(\delta)-B_{RF}X.
\]

It is accumulated directly through \(16001/16000\), by a sixteen-level Hilbert inverse-power expansion through \(2,000,000\), and analytically beyond that cutoff.

The point residuals through two million remain below the widened caps

\[
\boxed{
\|r_{R,e,\le2M}\|<0.00770,
}
\]

\[
\boxed{
\|r_{R,o,\le2M}\|<0.01280.
}
\]

The sixteen-level Hilbert-expansion truncation error is below \(2\times10^{-15}\) and is negligible relative to these caps.

For the analytic far tail, the source-faithful coupling uses the already audited generator bound

\[
|Z_n|<8
\]

and the elementary rank-one pole decay

\[
|p_n|
\le
\frac{4g}{\pi n}.
\]

The resulting far residual caps are

\[
\boxed{
\|r_{R,e,>2M}\|<0.00460,
}
\]

\[
\boxed{
\|r_{R,o,>2M}\|<0.00100.
}
\]

After adding the inherited source/operator uncertainty and the v13.824 smooth-bulk entry/log reserve, the public total remote caps are

\[
\boxed{
\|r_{R,e}\|<0.0130,
}
\]

\[
\boxed{
\|r_{R,o}\|<0.0147.
}
\]

## 6. Full transformed coupling-energy identity

For the finite-support trial \(X\),

\[
F_{TC}
=
B_TX+r,
\]

so

\[
F_{CT}B_T^{-1}F_{TC}
=
X^TB_TX
+
X^Tr
+
r^TX
+
r^TB_T^{-1}r.
\]

But

\[
C(\delta)^*C(\delta)
=
F_{CT}(\delta)B_T^{-1}F_{TC}(\delta).
\]

Using the global v13.824 smooth-bulk floors

\[
B_{T,e}>0.00830I,
\]

\[
B_{T,o}>0.20500I,
\]

together with the widened finite-energy, solve-residual, model-reserve, and remote caps gives

\[
\boxed{
C_e(\delta)^*C_e(\delta)
\preceq
0.0256\,I_2
}
\]

uniformly for

\[
|\delta|\le0.02,
\]

and

\[
\boxed{
C_o(\delta)^*C_o(\delta)
\preceq
0.0416\,I_2.
}
\]

Equivalently,

\[
\boxed{
\|C_e(\delta)\|<0.160,
}
\]

\[
\boxed{
\|C_o(\delta)\|<0.204.
}
\]

These are uniform interval bounds, not point estimates.

## 7. Grouped-residue error certificate

Combining the coupling caps with the externally replayed projector errors gives

### even-v

\[
\|G_e(\delta)-\widehat G_e(\delta)\|
<
0.332\times0.0256
=
0.0084992.
\]

The public fail-closed cap is

\[
\boxed{
\|G_e(\delta)-\widehat G_e(\delta)\|
<
0.0086
\qquad
(|\delta|\le0.02).
}
\]

### odd-v

\[
\|G_o(\delta)-\widehat G_o(\delta)\|
<
0.361\times0.0416
=
0.0150176.
\]

The public fail-closed cap is

\[
\boxed{
\|G_o(\delta)-\widehat G_o(\delta)\|
<
0.0152
\qquad
(|\delta|\le0.02).
}
\]

## 8. Loewner-order form

The stronger sector-wise matrix enclosures are

### even-v

\[
\boxed{
-0.332\,C_e(\delta)^*C_e(\delta)
\preceq
G_e(\delta)-\widehat G_e(\delta)
\preceq
0.332\,C_e(\delta)^*C_e(\delta),
}
\]

and therefore

\[
\boxed{
-0.0086I_2
\prec
G_e(\delta)-\widehat G_e(\delta)
\prec
0.0086I_2.
}
\]

### odd-v

\[
\boxed{
-0.361\,C_o(\delta)^*C_o(\delta)
\preceq
G_o(\delta)-\widehat G_o(\delta)
\preceq
0.361\,C_o(\delta)^*C_o(\delta),
}
\]

hence

\[
\boxed{
-0.0152I_2
\prec
G_o(\delta)-\widehat G_o(\delta)
\prec
0.0152I_2.
}
\]

These inequalities hold uniformly throughout the entire certified inner window.

## 9. Consequences for the next low-core gate

Because both grouped residue matrices are positive semidefinite,

\[
G(\delta)\succeq0,
\qquad
\widehat G(\delta)\succeq0.
\]

The present certificate therefore allows any numerical grouped residue computed with \(\widehat P_4\) to be inserted into the two-mode Feshbach map with a rigorous additive symmetric-matrix uncertainty:

\[
\boxed{
\Delta G_e(\delta)
\in
[-0.0086I_2,\,+0.0086I_2],
}
\]

\[
\boxed{
\Delta G_o(\delta)
\in
[-0.0152I_2,\,+0.0152I_2].
}
\]

In particular, every eigenvalue of the exact grouped residue differs from the corresponding numerical grouped-residue eigenvalue by at most the sector cap.

The trace errors obey the immediate bounds

\[
|\operatorname{tr}G_e-\operatorname{tr}\widehat G_e|
<0.0172,
\]

\[
|\operatorname{tr}G_o-\operatorname{tr}\widehat G_o|
<0.0304.
\]

No determinant bound is promoted here because the determinant error is better handled after the actual \(2\times2\) numerical residue matrices are evaluated.

## 10. Guardrails

This entry certifies the grouped spectral projector residue only.

It does not:

- separate the four nearly degenerate tail channels into individually certified residues;
- assert simplicity of the cluster eigenvalues;
- prove the four infinite tail eigenvalues are positive;
- certify the full low-core Schur determinant;
- prove convergence of \(\kappa_0\);
- unblock \(\kappa_1\);
- imply RH or GRH.

## Result

For all real

\[
|\delta|\le0.02,
\]

the numerical grouped residue based on the residual-certified four-space obeys

\[
\boxed{
\|C_e(\delta)^*P_{4,e}C_e(\delta)
-
C_e(\delta)^*\widehat P_{4,e}C_e(\delta)\|
<
0.0086,
}
\]

and

\[
\boxed{
\|C_o(\delta)^*P_{4,o}C_o(\delta)
-
C_o(\delta)^*\widehat P_{4,o}C_o(\delta)\|
<
0.0152.
}
\]

The stronger Loewner enclosures in Section 8 hold simultaneously.
