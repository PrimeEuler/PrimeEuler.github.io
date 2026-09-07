# Cone Derivation Ledger v13.289 — Neumann Preconditioning and Direct-Form Cross-Check

Date: 2026-09-07

Status: EXACT DENOMINATOR DIAGONALIZATION + DIRECT QUADRATIC-FORM CROSS-CHECK + FREQUENCY-AWARE QUADRATURE AUDIT — NO RELIABLE NEGATIVE GROUND STATE DETECTED — GRH NOT PROVED

## 0. Synchronization and purpose

The v13.288 audit superseded the v13.287 `~-1.3` Ritz table and showed that the raw compact generalized pair

\[
G_a u=\lambda K_a u,
\qquad K_a=(-\Delta_N)^{-1},
\]

is numerically delicate because the denominator is compact and becomes rapidly ill-conditioned in polynomial coordinates.

The preferred next target was therefore to remove the numerically assembled denominator altogether and cross-check the same spectral problem through Suzuki's direct quadratic form.

This entry adds

`research-notes/suzuki_neumann_preconditioned_audit.py`.

The primary source remains Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, especially equations (8.2), (8.6), and (8.7).

---

## 1. Exact Neumann diagonalization of the denominator

On `[-a,a]`, the normalized nonconstant Neumann eigenfunctions are

\[
\phi_n(x)=a^{-1/2}\cos\!\left(\frac{n\pi(x+a)}{2a}\right),
\qquad n\ge1,
\]

with

\[
-\Delta_N\phi_n=\mu_n\phi_n,
\qquad
\mu_n=\left(\frac{n\pi}{2a}\right)^2.
\]

Therefore

\[
K_a\phi_n=\mu_n^{-1}\phi_n.
\]

The mean-zero constraint is automatic because the constant Neumann mode `n=0` is omitted.

If `G` is the matrix of `G_a` in this basis, then the generalized eigenproblem is converted exactly into the ordinary symmetric problem

\[
\boxed{
A y=\lambda y,
\qquad
A=K^{-1/2}GK^{-1/2}
}
\]

with entries

\[
A_{mn}=\sqrt{\mu_m}\,G_{mn}\,\sqrt{\mu_n}.
\]

No Cholesky factorization of an increasingly small numerical `K_d` is required.

---

## 2. Exact parity split survives in the Neumann basis

Under reflection `x -> -x`, the Neumann modes alternate parity:

- `n` odd gives an odd function;
- `n` even gives an even function.

Thus the preconditioned matrix splits exactly into odd and even blocks just as the Legendre formulation did.

This gives a second coordinate system in which parity is structural rather than inferred numerically.

---

## 3. Direct quadratic-form identity

Let

\[
\psi_n(x)=a^{-1/2}\sin\!\left(\frac{n\pi(x+a)}{2a}\right)
\]

be the normalized Dirichlet eigenfunctions. Then

\[
\psi_n'(x)=\sqrt{\mu_n}\,\phi_n(x).
\]

Suzuki's equation (8.6) gives, for `v in H_0^1(-a,a)`,

\[
Q_W^a(v)=\langle G_a Dv,Dv\rangle.
\]

Therefore the matrix of the direct quadratic form in the Dirichlet basis is

\[
Q_{mn}
=
\langle G_a D\psi_n,D\psi_m\rangle
=
\sqrt{\mu_m}\,G_{mn}\,\sqrt{\mu_n}
=A_{mn}.
\]

This is an exact operator identity, but the audit assembles the two matrices through separate code paths:

1. assemble `G` in the Neumann basis and precondition analytically;
2. assemble the derivative-basis quadratic form directly.

At `a=1`, 10 modes and `23 x 24` breakpoint-aware quadrature, the local audit gives

\[
\|A_{\rm pre}-A_{\rm direct}\|_\infty
\approx 2.08\times10^{-15},
\]

with relative infinity-norm discrepancy about

\[
1.01\times10^{-15}.
\]

Thus the Neumann preconditioning and the direct quadratic-form assembly agree to roundoff.

---

## 4. Removing numerical K does not rescue the negative branch

The important question is whether the negative values seen in v13.288 were caused mainly by numerical conditioning of the compact denominator.

At fixed 10-mode Neumann/Dirichlet space, refine only the breakpoint-aware quadrature:

| outer x inner | odd minimum | even minimum | overall minimum |
|---:|---:|---:|---:|
| 7 x 8 | `-1.66685e-3` | `-1.96208e-3` | `-1.96208e-3` |
| 11 x 12 | `-3.47621e-4` | `-3.88135e-4` | `-3.88135e-4` |
| 15 x 16 | `-1.09235e-4` | `-1.12835e-4` | `-1.12835e-4` |
| 23 x 24 | `-1.83307e-5` | `-2.05503e-5` | `-2.05503e-5` |
| 31 x 32 | `-4.90160e-6` | `-6.45052e-6` | `-6.45052e-6` |
| 39 x 40 | `-1.89132e-6` | `-2.64426e-6` | `-2.64426e-6` |
| 47 x 48 | `-8.94109e-7` | `-1.27320e-6` | `-1.27320e-6` |

The apparent negative ground state again collapses rapidly toward zero as quadrature is refined.

This is decisive because the denominator is now exact and diagonal. Hence the instability seen in v13.288 was **not only** a Cholesky/conditioning artifact of the numerical `K_d` matrix. The dominant remaining issue is resolution of the twice-integrated screw kernel against increasingly oscillatory basis functions.

---

## 5. Fixed quadrature is not a valid degree-convergence test

At `47 x 48` quadrature, increasing the number of retained modes gives:

| modes | odd minimum | even minimum | overall minimum |
|---:|---:|---:|---:|
| 4 | `-5.85815e-8` | `+4.02731e-6` | `-5.85815e-8` |
| 6 | `-1.93001e-7` | `-3.60656e-7` | `-3.60656e-7` |
| 8 | `-8.92899e-7` | `-5.58372e-7` | `-8.92899e-7` |
| 10 | `-8.94109e-7` | `-1.27320e-6` | `-1.27320e-6` |
| 12 | `-1.26775e-6` | `-1.55209e-6` | `-1.55209e-6` |
| 14 | `-1.71699e-6` | `-2.04473e-6` | `-2.04473e-6` |

Taken alone, this would look like a worsening negative spectral branch. But the basis frequency is increasing while quadrature is held fixed.

The 14-mode calculation was therefore repeated with increasing quadrature:

| outer x inner | lowest eigenvalue |
|---:|---:|
| 47 x 48 | `-2.04473e-6` |
| 55 x 56 | `-1.03460e-6` |
| 63 x 64 | `-5.63977e-7` |
| 79 x 80 | `-2.10237e-7` |

At `79 x 80`, the parity minima are

\[
\lambda_{\rm odd}\approx-2.10237\times10^{-7},
\qquad
\lambda_{\rm even}\approx-2.07530\times10^{-7}.
\]

So the degree drift at fixed quadrature is itself a resolution artifact: quadrature order must scale with the maximum resolved basis frequency.

---

## 6. Revised numerical interpretation

The v13.289 audit supports the following conclusions.

1. The generalized denominator `K_a=(-Delta_N)^(-1)` can be removed exactly by working in the Neumann eigenbasis.
2. The resulting standard symmetric matrix is identical, to roundoff, to the independently assembled direct quadratic-form matrix on the Dirichlet basis.
3. The apparent small negative eigenvalues continue to collapse toward zero as breakpoint-aware quadrature is refined.
4. Therefore the negative branch is not evidence for a negative `a=1` ground state.
5. Fixed quadrature cannot be used to assess convergence in mode count; the integration order must increase with basis frequency.
6. No stable ground-state parity has emerged. At the highest present resolution the two parity minima are nearly tied at the `2e-7` scale.
7. No reliable numerical value or sign of `lambda_a` has yet been extracted from these finite calculations.
8. In particular, `lambda=-5 < lambda_a` remains uncertified.

The important improvement over v13.288 is that denominator conditioning has now been factored out analytically. The remaining error can be localized primarily to kernel integration / high-frequency resolution.

---

## 7. Relation to Suzuki's source

The present formulation is not a new spectral problem. It is the same source-level object in three equivalent coordinate forms:

\[
\frac{\langle G_a u,u\rangle}{\langle K_a u,u\rangle},
\]

\[
K^{-1/2}GK^{-1/2},
\]

and

\[
Q_W^a(v)=\langle G_aDv,Dv\rangle,
\qquad \|v\|_{L^2}=1.
\]

The second and third forms are numerically preferable because they avoid division by a separately discretized compact denominator.

---

## 8. What is exact, numerical, and still open

Exact/source-established:

- Suzuki equations (8.2), (8.6), and (8.7);
- Neumann spectrum of `-Delta_N` on `[-a,a]`;
- exact diagonal form of `K_a` in that basis;
- exact equivalence between Neumann preconditioning and the Dirichlet direct quadratic form;
- exact parity decomposition.

Numerically established in this audit:

- preconditioned and direct-form matrices agree to about `1e-15` relative scale in the 10-mode `23 x 24` control;
- the 10-mode negative minimum collapses from about `-2e-3` to `-1.3e-6` as quadrature rises from `7 x 8` to `47 x 48`;
- the 14-mode minimum collapses from about `-2.0e-6` at `47 x 48` to `-2.1e-7` at `79 x 80`;
- odd/even minima remain close and no stable parity winner is established.

Open:

- obtain a controlled quadrature-error estimate uniform in retained mode number;
- determine whether the limiting `a=1` ground state is strictly positive, zero, or negative;
- obtain a rigorous lower enclosure for `lambda_a`;
- certify an admissible `lambda<lambda_a` for the Section-8 deficiency calculation;
- resume the differentiation-back Fredholm consistency test only after admissibility is controlled;
- D12 transfer remains downstream;
- RH/GRH remains unproved.

---

## 9. Next target

The next step should be a **frequency-aware integration audit with an analytic/semi-analytic matrix-element control**.

The highest-value route is to exploit the piecewise structure of the screw kernel:

- the Neumann/Dirichlet trigonometric factors are explicit;
- the prime-power ramp terms are piecewise affine between exact breakpoints;
- the pole term is elementary;
- only the archimedean term requires non-elementary treatment.

Therefore the prime-ramp and polynomial/Neumann pieces can be integrated analytically, leaving only a smooth archimedean remainder for numerical quadrature. This should sharply reduce the error that is currently masquerading as `10^-7`–`10^-6` negative eigenvalues.

The preferred v13.290 target is

\[
\boxed{\text{semi-analytic Neumann-basis matrix elements + certified frequency-scaled quadrature control}.}
\]

Only after that error floor is pushed below the observed near-zero spectral scale should the project assign a sign to the `a=1` ground state or return to the admissible-`lambda` question.
