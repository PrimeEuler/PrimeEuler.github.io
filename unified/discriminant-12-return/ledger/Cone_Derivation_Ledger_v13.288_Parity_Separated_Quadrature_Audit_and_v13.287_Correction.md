# Cone Derivation Ledger v13.288 — Parity-Separated Quadrature Audit and v13.287 Correction

Date: 2026-09-07

Status: REPRODUCTION AUDIT + PARITY BLOCK DIAGONALIZATION + QUADRATURE-REFINEMENT FAILURE DIAGNOSIS + OFF-GRID RESIDUAL CHECK — v13.287 NUMERICAL SCALE SUPERSEDED — GRH NOT PROVED

## 0. Synchronization and purpose

Immediately before this audit, `master` was re-fetched at

`b9729e70f38ef443c0f93e66710d92e5ecca3e63`,

the v13.287 checkpoint.

This entry adds

`research-notes/suzuki_generalized_eigenvalue_parity_audit.py`.

Primary source remains Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, especially equations (1.3), (2.2), (8.2), and (8.7).

The immediate goal was the audit requested at the end of v13.287:

1. separate the exact even/odd sectors;
2. refine polynomial degree and quadrature independently;
3. monitor the compact denominator `K_d`;
4. check the lowest computed eigenpair off-grid.

The first result is a correction: the numerical table recorded in v13.287 is not reproduced by the committed v13.287 script and is therefore superseded by this entry.

---

## 1. Source equation remains correct

Suzuki's equation (8.7) is

\[
\frac{Q_W^a(v)}{\|v\|_{L^2}^2}
=
\frac{\langle G_a u,u\rangle}{\langle K_a u,u\rangle},
\qquad u=Dv\in L_0^2(-a,a),
\]

with

\[
K_a=(-\Delta_N)^{-1}
\]

and continuous Neumann kernel

\[
N_a(x,y)=\frac{x^2+y^2}{4a}-\frac{|x-y|}{2}+\frac a6.
\]

This leads formally to

\[
G_a u=\lambda K_a u.
\]

Nothing in the present correction changes that source-level statement.

---

## 2. Exact parity decomposition

The trial basis remains

\[
P_1(x/a),P_2(x/a),\ldots,P_d(x/a),
\]

with `P_0` omitted so the mean-zero condition is exact.

Since

\[
P_n(-x)=(-1)^nP_n(x),
\]

and both kernels are invariant under simultaneous reflection `(x,y)->(-x,-y)`, the Galerkin pair splits exactly into two generalized eigenproblems:

- odd sector: `n=1,3,5,...`;
- even sector: `n=2,4,6,...`.

Numerically the off-block entries are at roundoff scale (`~10^-19` in the low-degree tests), confirming the exact symmetry rather than merely suggesting it.

---

## 3. Reproduction failure of the v13.287 table

The v13.287 ledger recorded, at `a=1`, outer order 7 and inner order 8,

\[
-1.25858924,-1.28368744,-1.29680983,-1.30456772
\]

for degrees `4,6,8,10`.

However, executing the formulas of the committed v13.287 script at those same settings gives instead:

| degree | odd-sector minimum | even-sector minimum | overall minimum |
|---:|---:|---:|---:|
| 4 | `+4.09415e-7` | `-1.56190e-4` | `-1.56190e-4` |
| 6 | `-9.55044e-5` | `-2.37183e-4` | `-2.37183e-4` |
| 8 | `-6.03816e-4` | `-8.32654e-4` | `-8.32654e-4` |
| 10 | `-6.96391e-4` | `-8.33563e-4` | `-8.33563e-4` |

Therefore the `~ -1.3` scale in v13.287 cannot be treated as a result of the committed source-faithful implementation.

The most likely explanation is that the table was produced by a stale or non-identical local computation. Since the exact origin of that discrepancy has not been reconstructed, the safe action is to withdraw the table rather than retrofit an explanation.

Accordingly:

\[
\boxed{\text{the v13.287 numerical Ritz table is superseded.}}
\]

The source equations and Rayleigh-Ritz guardrail in v13.287 remain valid; only the recorded numerical scale is withdrawn.

---

## 4. Fast source-equivalent archimedean evaluation for the audit

Direct high-precision Hurwitz-Lerch evaluation is expensive when quadrature order is pushed far beyond the v13.287 smoke test.

For `a=1`, every kernel argument satisfies

\[
|x-y|\le2<\pi.
\]

Suzuki's expansion immediately preceding equation (2.2), derived from the Hurwitz-Lerch expansion, can therefore be used safely throughout this control interval. The audit script evaluates the archimedean term through that convergent series and first compares it against the direct high-precision implementation.

At sample points

\[
10^{-4},10^{-2},0.1,0.5,1,2,
\]

the series and direct Lerch values agree to approximately machine precision in the local audit (the discrepancy at `t=2` is about `1.5e-13` with the finite series used).

This is an acceleration device, not a change of kernel.

---

## 5. Quadrature refinement destroys the apparent negative plateau

The decisive numerical diagnostic is to fix degree `d=10` and increase only the breakpoint-aware Gauss-Legendre orders.

| outer x inner | odd minimum | even minimum | overall minimum |
|---:|---:|---:|---:|
| 7 x 8 | `-6.96391e-4` | `-8.33563e-4` | `-8.33563e-4` |
| 11 x 12 | `-1.42019e-4` | `-1.64960e-4` | `-1.64960e-4` |
| 15 x 16 | `-4.61633e-5` | `-4.55228e-5` | `-4.61633e-5` |
| 19 x 20 | `-1.91694e-5` | `-1.51149e-5` | `-1.91694e-5` |
| 23 x 24 | `-9.25911e-6` | `-6.38305e-6` | `-9.25911e-6` |
| 27 x 28 | `-4.94354e-6` | `-3.25268e-6` | `-4.94354e-6` |
| 31 x 32 | `-2.82534e-6` | `-1.86010e-6` | `-2.82534e-6` |
| 39 x 40 | `-1.03956e-6` | `-7.49794e-7` | `-1.03956e-6` |

The negative value shrinks by almost three orders of magnitude as quadrature alone is refined.

Hence the low-order negative branch is not a stable approximation of a ground-state eigenvalue. It is dominated by quadrature error amplified by the compact generalized denominator.

The parity label also changes during refinement: the even sector is lower at low order, while the odd sector becomes slightly lower at higher order. Therefore no reliable ground-state parity has yet been identified.

---

## 6. Compact-denominator conditioning explains the sensitivity

For the degree sequence at `a=1`, the denominator matrix remains positive but becomes rapidly more ill-conditioned.

Representative values at the source-faithful 7 x 8 integration are:

| degree | `cond(K_d)` | smallest eigenvalue of `K_d` |
|---:|---:|---:|
| 4 | `5.87e1` | `4.57e-3` |
| 6 | `2.28e2` | `1.18e-3` |
| 8 | `6.46e2` | `4.15e-4` |
| 10 | `1.52e3` | `1.76e-4` |
| 12 | `3.16e3` | `8.47e-5` |

This is exactly the regime in which a small absolute error in `G_d` can create a much larger error in the generalized eigenvalue after division by a very small denominator direction.

The observed behavior is therefore consistent with compact-denominator spectral pollution / amplification rather than convergence to a negative eigenvalue near `-1.3`.

---

## 7. Independent off-grid residual rejects the current lowest pair

A stronger check was performed on the degree-10 lowest Ritz pair assembled with the much finer `39 x 40` breakpoint-aware quadrature.

The resulting lowest finite generalized eigenvalue is approximately

\[
\lambda_{10}^{(39,40)}\approx -1.03956\times10^{-6}.
\]

The eigenfunction was reconstructed from its Legendre coefficients and tested on an independent 61-point Gauss-Legendre x-grid, with fresh 50-point row-wise breakpoint-aware integration in `y`.

For the projected residual

\[
r(x)=P_aG u(x)-\lambda K_a u(x),
\]

the audit gives approximately

\[
\|r\|_{L^2}\approx1.89\times10^{-5},
\]

with relative residual

\[
\frac{\|r\|}{\|P_aGu\|+|\lambda|\|K_au\|}
\approx0.989.
\]

This is not a converged eigenpair. The small finite generalized eigenvalue is therefore not supported by an off-grid operator residual.

This residual test is more informative than the machine-precision algebraic residual of the finite matrix problem.

---

## 8. Revised interpretation

The correct numerical conclusion is now much weaker, but substantially safer:

1. The parity decomposition is exact and implemented correctly.
2. The v13.287 `~ -1.3` numerical scale is invalid and superseded.
3. At `a=1`, low-order breakpoint-aware Galerkin discretizations produce tiny negative generalized eigenvalues, but those values collapse toward zero under quadrature refinement.
4. The compact denominator `K_a` strongly amplifies integration error as degree grows.
5. The current lowest Ritz pair fails an independent off-grid residual test.
6. No reliable numerical estimate of `lambda_a` has yet been obtained from this formulation.
7. Consequently there is still no numerical or rigorous certification that `lambda=-5 < lambda_a`.

The useful gain from v13.288 is not a new spectral number; it is the elimination of a false one.

---

## 9. What remains exact/source-established

Exact/source-established:

- Suzuki equation (8.7);
- `K_a=(-Delta_N)^(-1)` and its continuous kernel;
- mean-zero generalized setting;
- exact Legendre parity split;
- Rayleigh-Ritz upper-bound principle when the discretized pair genuinely approximates the intended self-adjoint generalized problem.

Numerically established in this audit:

- committed v13.287 code does not reproduce the v13.287 table;
- parity off-blocks are at roundoff scale;
- degree-10 low-order negative values collapse strongly under quadrature refinement;
- `K_d` condition number grows rapidly with degree;
- the refined lowest Ritz pair has an order-one relative off-grid residual.

Not established:

- sign or reliable value of the true `a=1` ground state `lambda_a`;
- ground-state parity;
- admissibility of `lambda=-5`;
- any RH/GRH conclusion.

---

## 10. Next target

The next step should not be a still-higher-degree generalized eigensolve using the same raw compact pair.

The audit suggests two higher-value routes:

1. **Change the numerical formulation** so the small denominator is treated analytically or preconditioned, for example by expanding in the known Neumann-Laplacian eigenbasis where `K_a=(-Delta_N)^(-1)` is diagonal. The generalized problem can then be rescaled into a standard problem involving the square-root denominator and conditioning can be audited directly.

2. **Cross-check against Suzuki's original Rayleigh quotient / quadratic-form representation** before returning to the generalized compact pair. This gives an independent route to the lowest spectral scale without dividing two separately small compact forms.

The preferred v13.289 target is therefore:

\[
\boxed{\text{Neumann-eigenbasis preconditioning and direct-form cross-check of }\lambda_a.}
\]

Only once that formulation produces stable parity-resolved eigenpairs with small off-grid residual should the project revisit an admissible `lambda` for the Section-8 Fredholm deficiency computation.
