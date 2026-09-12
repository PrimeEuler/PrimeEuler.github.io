# Cone Derivation Ledger v13.405 — Quantitative Positive Schur Gaps After Parity Closure

Date: 2026-09-12

Status labels: **[D]** exact derived, **[N-cert]** validated computational, **[O]** open.

## 1. Purpose

v13.401–v13.404 certify positive frozen subspaces in both parity sectors at `a=1`:

- even-v sector: an exact six-dimensional positive subspace of the ten-mode Schur complement;
- odd-v sector: an exact eight-dimensional positive subspace of the ten-mode Schur complement.

The prior checkpoints used these only to bound nonpositive index.  Here we extract explicit lower Rayleigh margins for the first resolved positive Schur levels.

## 2. General normalized-to-raw conversion

Suppose on an exact frozen subspace we have

\[
B=L_0 C L_0^T,
\qquad
G=L_0 H L_0^T,
\]

and a positive tail floor

\[
T_{\rm eff}\succeq\delta I.
\]

Then the exact infinite Schur complement restricted to the frozen subspace obeys

\[
S_{\infty}|_Q
\succeq
B-\delta^{-1}G
=
L_0\left(C-\delta^{-1}H\right)L_0^T.
\]

Therefore

\[
\lambda_{\min}(S_{\infty}|_Q)
\ge
\lambda_{\min}(L_0L_0^T)
\left[
\lambda_{\min}(C)-\frac{\lambda_{\max}(H)}{\delta}
\right].
\]

This uses only the previously certified matrix inequalities.

## 3. Even-sector quantitative gap

From v13.401,

\[
\lambda_{\min}(C_{\rm even})
>0.9964577330113989,
\]

\[
\lambda_{\max}(H_{\rm even})
<0.1786106149943144,
\]

and

\[
\delta_{\rm even}>0.18225976374175623.
\]

Hence the normalized residual margin is

\[
0.9964577330113989
-
\frac{0.1786106149943144}{0.18225976374175623}
>
\boxed{0.0164794244}.
\]

The frozen preconditioner satisfies

\[
\lambda_{\min}(L_0L_0^T)
>3.8576494359\times10^{-8}.
\]

Therefore the exact infinite even-sector ten-mode Schur complement is bounded below on its exact six-dimensional frozen positive subspace by

\[
\boxed{
S_{10}^{\rm even}|_{Q_6}
\succeq
6.35\times10^{-10} I.
}
\]

By Courant–Fischer, a ten-dimensional symmetric matrix possessing a six-dimensional subspace with Rayleigh quotient at least `m` has fifth ordered eigenvalue at least `m`. Thus

\[
\boxed{
\lambda_5(S_{10}^{\rm even})>6.35\times10^{-10}.
}
\]

This is a quantitative strengthening of the v13.401/v13.402 statement `lambda_5>0`.

## 4. Odd-sector quantitative gap

From v13.404 retain the deliberately rounded bounds

\[
C_{\rm odd}\succeq0.80I,
\qquad
H_{\rm odd}\prec0.225I,
\qquad
\delta_{\rm odd}>0.6372304048.
\]

Then

\[
0.80-\frac{0.225}{0.6372304048}
>
\boxed{0.44690}.
\]

The frozen odd preconditioner has midpoint minimum square scale

\[
\lambda_{\min}(L_0L_0^T)
>1.6689\times10^{-10}
\]

after outward rounding.

Thus the exact infinite odd-sector ten-mode Schur complement satisfies on its exact eight-dimensional frozen subspace

\[
\boxed{
S_{10}^{\rm odd}|_{Q_8}
\succeq
7.45\times10^{-11}I.
}
\]

Since the positive subspace has dimension eight inside a ten-dimensional symmetric Schur complement, Courant–Fischer gives

\[
\boxed{
\lambda_3(S_{10}^{\rm odd})>7.45\times10^{-11}.
}
\]

## 5. Combined terminal-Schur statement

For the direct sum of the two ten-mode parity Schur complements,

\[
S_{20}=S_{10}^{\rm even}\oplus S_{10}^{\rm odd},
\]

there are at most six nonpositive eigenvalues and the seventh ordered eigenvalue satisfies the conservative bound

\[
\boxed{
\lambda_7(S_{20})>7.45\times10^{-11}.
}
\]

This statement concerns the finite terminal Schur complement.  Schur congruence preserves inertia but not eigenvalues, so this numerical lower bound is **not** transferred unchanged to the full infinite operator.

## 6. Current theorem-level parity picture

The strongest certified statements are now:

\[
\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,
\qquad
\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2,
\]

and therefore

\[
\boxed{
\operatorname{ind}_{\le0}(A_{a=1})\le6.
}
\]

At the terminal Schur level the first resolved positive eigenvalues have explicit margins:

\[
\lambda_5(S_{10}^{\rm even})>6.35\times10^{-10},
\qquad
\lambda_3(S_{10}^{\rm odd})>7.45\times10^{-11}.
\]

## 7. What remains genuinely unresolved

The only unresolved low-dimensional sign problem at `a=1` is now confined to

- four even-sector directions;
- two odd-sector directions.

No exact sign, zero, or kernel multiplicity is assigned to those six directions.

## 8. Guardrails

- The six unresolved directions are not asserted to be nonpositive; `index <= 6` is only an upper bound.
- Numerical-zero-scale finite levels are not exact kernels.
- The Schur eigenvalue lower bounds do not transfer directly as full-operator eigenvalue lower bounds because the Schur reduction is a congruence, not a unitary equivalence.
- No RH, GRH, exact-zero, or `lambda_1=0` conclusion follows.
