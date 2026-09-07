# Cone Derivation Ledger v13.287 — Suzuki Generalized Eigenvalue Ritz Control

Date: 2026-09-07

Status: SOURCE-FAITHFUL EQUATION-(8.7) GALERKIN CONTROL + NUMERICAL RITZ DATA + ADMISSIBILITY GUARDRAIL — GRH NOT PROVED

> **Supersession notice (v13.288):** the numerical Ritz table and the associated `~ -1.3` spectral-scale interpretation in this entry are not reproduced by the committed v13.287 implementation and are superseded by `Cone_Derivation_Ledger_v13.288_Parity_Separated_Quadrature_Audit_and_v13.287_Correction.md`. The source equation (8.7), mean-zero Galerkin setup, and Rayleigh-Ritz admissibility guardrail below remain useful; the recorded numerical scale does not.

## 0. Synchronization

Immediately before this write, `master` was re-fetched at

`f8080105d9621b069e633c47bcc9c0f2b2671f60`,

whose parent is the v13.286 breakpoint-aware Riemann-control checkpoint.

This entry adds

`research-notes/suzuki_generalized_eigenvalue_control.py`.

The primary source remains Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, especially Section 8.5 and equation (8.7).

---

## 1. Source correction: what equation (8.7) actually gives

Suzuki writes, with `u=Dv` and `K_a=(-Delta_N)^(-1)`,

\[
\frac{Q_W^a(v)}{\|v\|_{L^2}^2}
=
\frac{\langle G_a u,u\rangle}{\langle K_a u,u\rangle},
\]

which leads to

\[
\boxed{G_a u=\lambda K_a u,\qquad u\in H(S_a).}
\]

Suzuki states that this generalized spectrum coincides with the spectrum of `A_a`, is discrete, bounded below, and accumulates only at `+infinity`.

The continuous kernel already used in the project is

\[
K_a(x,y)=N_a(x,y)
=\frac{x^2+y^2}{4a}-\frac{|x-y|}{2}+\frac a6,
\]

on the mean-zero subspace.

---

## 2. Exact mean-zero Galerkin space

For the control calculation at fixed `a`, use the nested polynomial spaces

\[
V_d=\operatorname{span}\{P_1(x/a),\ldots,P_d(x/a)\}\subset L^2_0(-a,a).
\]

The constant Legendre mode `P_0` is omitted, so the zero-mean constraint is exact rather than numerically projected.

The Galerkin matrices are

\[
(G_d)_{mn}=\int_{-a}^a\int_{-a}^a
P_m(x/a)\,g_\zeta(x-y)\,P_n(y/a)\,dy\,dx,
\]

\[
(K_d)_{mn}=\int_{-a}^a\int_{-a}^a
P_m(x/a)\,N_a(x,y)\,P_n(y/a)\,dy\,dx.
\]

The finite generalized eigenproblem is

\[
G_d c=\lambda K_d c.
\]

Because `K_d` is positive definite on the retained mean-zero trial space, the implementation reduces it by Cholesky to an ordinary symmetric eigenproblem.

---

## 3. Breakpoint-aware product integration retained

The v13.286 principle is retained.

For each fixed outer point `x`, the inner `y` integral is split at

\[
y=x
\]

and every prime-power crossing

\[
y=x\pm\log(p^k)
\]

inside `[-a,a]`.

The outer integral is also split where one of those inner breakpoints enters or leaves the interval, namely at

\[
\boxed{x=-a+\log(p^k),\qquad x=a-\log(p^k)}
\]

when these lie inside `[-a,a]`, together with `x=0`.

Thus both integration directions respect the exact nonsmooth geometry of the continuous screw kernel rather than asking a single global Gaussian rule to resolve prime-power kinks implicitly.

---

## 4. First source-faithful Ritz data at a=1

An independent local execution of the same formulas used in the committed script was made with

\[
a=1,
\]

7-point Gauss-Legendre outer integration on each exact outer segment, 8-point Gauss-Legendre inner integration on every row segment, and the exact Suzuki-v2 equation-(1.3) screw function with high-precision Hurwitz-Lerch evaluation.

The first Ritz values were:

| degree d | lowest Ritz value | next values (ascending) |
|---:|---:|---|
| 4 | -1.25858924 | -0.55943580, -0.13753369, 1.56437989 |
| 6 | -1.28368744 | -0.56226795, -0.14025807, 0.10226907, 0.36597818 |
| 8 | -1.29680983 | -0.57036244, -0.14824564, 0.09144945, 0.33015631 |
| 10 | -1.30456772 | -0.57460453, -0.15108765, 0.08285545, 0.31510761 |

The lowest Ritz value decreases monotonically over these nested trial spaces, as expected from the Rayleigh-Ritz principle.

The data strongly suggest that the bottom of the `a=1` generalized spectrum is of order `-1.3`, not of order `-5`.

---

## 5. Important audit correction: Ritz data do NOT certify lambda=-5 < lambda_a

This is the key correction to the wording of the v13.286 next target.

For a lower-bounded self-adjoint generalized problem, the smallest Ritz value on a finite trial space satisfies

\[
\boxed{\lambda_a\le \lambda_{\min}^{(d)}}.
\]

Therefore the observed value near `-1.30` is an **upper bound** on the true spectral bottom `lambda_a`, not a lower bound.

Consequently,

\[
-5 < -1.30
\]

does **not** by itself prove

\[
-5<\lambda_a.
\]

The true bottom could in principle lie below the finite Ritz values. The numerical trend makes `lambda=-5` look very conservative, but a finite-dimensional Ritz calculation alone cannot certify admissibility.

Accordingly, the v13.286 phrase that a numerical estimate of `lambda_a` would by itself permit a "genuinely admissible" choice of `lambda<lambda_a` is too strong and is superseded by this guardrail.

---

## 6. What the generalized control *does* establish numerically

The new calculation is still highly useful.

1. It verifies that the exact equation-(8.7) generalized problem can be discretized directly using the same continuous-kernel machinery as the deficiency calculation.
2. It preserves the exact mean-zero constraint at the basis level.
3. It produces a stable low-degree spectral scale near `-1.3` for `a=1`.
4. It provides a second numerical object, independent of the first-kind Fredholm deficiency solve, against which parity, phase, and convergence behavior can be compared.
5. It gives a natural route to compute approximate eigenfunctions and parity sectors before returning to the deficiency equations.

The committed implementation is

`research-notes/suzuki_generalized_eigenvalue_control.py`.

---

## 7. How to obtain an actual admissibility certificate

To prove numerically or rigorously that a chosen `lambda` lies below `lambda_a`, one needs a **lower bound** for the generalized Rayleigh quotient, not merely Ritz upper bounds.

Promising routes include:

- a complement-space residual bound / Lehmann-Goerisch or Temple-type enclosure adapted to the generalized compact pair;
- interval-arithmetic enclosure of a finite section plus a rigorous tail bound;
- an operator inequality of the form
  \[
  G_a-\lambda K_a\ge cI
  \]
  on the mean-zero space for some explicit `c>0`;
- certified comparison with the original lower-bounded operator `A_a`.

Until one of these is implemented, `lambda=-5` should remain labelled **numerically plausible but uncertified**.

---

## 8. Immediate next numerical checks

Before attempting a rigorous lower bound, the generalized control should be hardened numerically in four directions:

1. separate even and odd Legendre sectors and identify which parity carries the ground state;
2. increase polynomial degree while independently increasing inner and outer quadrature order;
3. monitor the smallest eigenvalue of `K_d` and the conditioning of the Cholesky reduction to detect compact-denominator spectral pollution;
4. reconstruct the lowest Ritz eigenfunction and verify its generalized residual against off-grid breakpoint-aware quadrature.

These checks will tell us whether the observed `~ -1.3` scale is a true convergent ground-state signal or a low-degree pre-asymptotic plateau.

---

## 9. Exact, numerical, and open

Exact/source-established:

- Suzuki equation (8.7) and the generalized eigenproblem `G_a u=lambda K_a u`;
- equality of that generalized spectrum with the spectrum of `A_a`;
- discreteness, lower boundedness, and accumulation only at `+infinity`;
- the mean-zero setting and Neumann inverse kernel;
- Rayleigh-Ritz gives finite-subspace upper bounds for the spectral bottom.

Numerical in this entry:

- breakpoint-aware Galerkin matrices for `a=1`;
- low-degree lowest Ritz sequence
  \[
  -1.25859,-1.28369,-1.29681,-1.30457;
  \]
- apparent ground-state scale near `-1.3`.

Open:

- convergence of the Ritz sequence at higher degree;
- parity of the true ground state;
- rigorous lower enclosure of `lambda_a`;
- certified admissibility of `lambda=-5`;
- differentiation-back test for the deficiency solution;
- finite-to-infinite phase normalization;
- D12 transfer after the Riemann control is fully hardened;
- RH/GRH remains unproved.

---

## 10. Next target

The next highest-value step is a **parity-separated, quadrature-refined Ritz audit** of equation (8.7), including off-grid residuals and conditioning diagnostics.

Only after that numerical spectrum is demonstrably stable should we invest in a rigorous lower-bound enclosure for `lambda_a`. That enclosure, rather than the Ritz estimate alone, is what can finally certify a parameter `lambda<lambda_a` for the Section-8 deficiency computation.
