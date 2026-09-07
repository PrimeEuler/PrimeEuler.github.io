# Cone Derivation Ledger v13.290 — Semi-Analytic One-Dimensional Reduction and Cusp Subtraction

Date: 2026-09-07

Status: EXACT 2D-TO-1D TRANSLATION-KERNEL REDUCTION + SOURCE-KNOWN CUSP SUBTRACTION + PRIME-BREAKPOINT CONTROL — PREVIOUS NEGATIVE FLOOR IDENTIFIED AS QUADRATURE ARTIFACT — GRH NOT PROVED

> **v13.291 parity clarification:** the numerical odd/even index blocks in this entry are correct, but once the preconditioned matrix is interpreted in the direct Dirichlet `v` basis, differentiation reverses parity: odd mode number corresponds to even `v`, and even mode number to odd `v`. Any parity wording below that does not explicitly distinguish `u=Dv` from `v` is superseded by v13.291. The numerical values themselves are unchanged.

## 0. Synchronization and purpose

The v13.289 audit removed the numerically assembled compact denominator by diagonalizing `K_a=(-Delta_N)^(-1)` in the Neumann basis and cross-checked the resulting matrix against Suzuki's direct quadratic form. The two forms agreed to roundoff, but the lowest numerical values still drifted toward zero as the 2-D breakpoint-aware quadrature was refined.

The remaining target was therefore to isolate the integration error itself.

This entry adds

`research-notes/suzuki_semianalytic_neumann_matrix.py`.

The primary source remains Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, especially equations (1.3), (2.2), (8.6), and (8.7).

---

## 1. Exact reduction from two dimensions to one

Write the normalized Dirichlet modes on `[-a,a]` as

\[
\psi_n(x)=a^{-1/2}\sin(k_n(x+a)),
\qquad k_n=\frac{n\pi}{2a},
\]

so that

\[
\psi_n'(x)=q_n(x)=k_n a^{-1/2}\cos(k_n(x+a)).
\]

The direct quadratic-form matrix is

\[
A_{mn}=\int_{-a}^a\int_{-a}^a q_m(x)g(x-y)q_n(y)\,dy\,dx.
\]

Because `g` is an even difference kernel, set `t=x-y`. For `t>=0`, define

\[
C_{mn}(t)=\int_{-a+t}^a q_m(x)q_n(x-t)\,dx.
\]

Then exactly

\[
\boxed{
A_{mn}=\int_0^{2a}g(t)\,[C_{mn}(t)+C_{nm}(t)]\,dt.
}
\]

No approximation is used in this dimensional reduction.

The overlap integral itself is elementary. With `L=2a`, `A=k_m`, `B=k_n`,

\[
C_{mn}(t)=\frac{k_mk_n}{2a}
\left[
\int_t^L\cos((A-B)x+Bt)\,dx
+
\int_t^L\cos((A+B)x-Bt)\,dx
\right],
\]

and both terms have explicit sine antiderivatives, with the `A=B` zero-frequency case handled by its limiting linear expression.

This replaces the row-dependent 2-D kink geometry of v13.288-v13.289 by a fixed 1-D interval.

---

## 2. Prime-power breakpoints become fixed

In the 1-D representation, the prime-power part of Suzuki's equation (1.3) is piecewise affine in `t`, with breakpoints only at

\[
\boxed{t=\log(p^k)}
\]

inside `[0,2a]`.

For `a=1`, the entire matrix assembly can therefore be split once at the finite set of exact prime-power locations instead of recomputing row-wise crossing sets.

This is a substantial simplification and removes one whole source of frequency-dependent geometric quadrature error.

---

## 3. The dominant remaining difficulty is the universal t log t cusp

Suzuki equation (2.2) gives, near the origin,

\[
g(t)=\frac12 |t|\log|t|+A|t|+O(t^2),
\qquad
A=\frac12(\log(2\pi)+\gamma-1).
\]

The v13.289 2-D quadrature was breakpoint-aware, but ordinary Gauss-Legendre integration still had to approximate this nonanalytic endpoint behavior numerically.

A direct 1-D Gauss test without subtraction reproduces the same pathology: at 14 modes, increasing a single Gauss order gives lowest values of approximately

| order | lowest value |
|---:|---:|
| 8 | `-6.32e-3` |
| 12 | `-1.25e-3` |
| 16 | `-3.62e-4` |
| 24 | `-4.85e-5` |
| 32 | `-1.38e-5` |
| 48 | `-2.48e-6` |
| 64 | `-6.55e-7` |
| 80 | `-2.37e-7` |

This reproduces the same slow negative-to-zero drift seen in v13.289, now in a one-dimensional setting. Therefore the culprit is localized: the ordinary Gauss rule is converging slowly against the source-known cusp.

---

## 4. Cusp subtraction

Define the exact local model

\[
s(t)=\frac12 t\log t + At,
\qquad t>0.
\]

Then split

\[
g(t)=s(t)+r(t),
\qquad r(t)=O(t^2).
\]

The matrix becomes

\[
A_{mn}
=
\int_0^{2a}s(t)S_{mn}(t)\,dt
+
\int_0^{2a}r(t)S_{mn}(t)\,dt,
\]

where

\[
S_{mn}(t)=C_{mn}(t)+C_{nm}(t).
\]

The singular model integral is regularized with the change of variables

\[
t=2a\,u^2,
\]

which turns the endpoint cusp into a smooth enough integrand for high-order Gaussian evaluation. The remainder is then integrated separately on the exact prime-power subintervals.

This is the decisive numerical change.

---

## 5. The negative floor disappears

For `a=1`, 14 retained modes, and a fixed high-order evaluation of the subtracted model term, refining only the smooth remainder quadrature gives approximately

| remainder order | lowest eigenvalue |
|---:|---:|
| 8 | `-1.13e-4` |
| 10 | `-7.81e-10` |
| 12 | `+1.04e-15` |
| 16 | `-7.87e-16` |
| 20 | `+1.40e-16` |
| 24 | `-1.07e-16` |
| 32 | `+2.70e-15` |

Thus the negative branch that persisted at the `10^-7` to `10^-6` scale in v13.289 collapses to floating-point zero once the known `t log t` singularity is removed analytically from the numerical task.

The previous negative values were therefore not evidence for a negative `a=1` ground state. They were quadrature artifacts caused primarily by the endpoint cusp.

---

## 6. Mode-count audit after cusp removal

At the stabilized remainder order, the smallest parity-resolved values are approximately

| modes | odd-index block | even-index block | overall |
|---:|---:|---:|---:|
| 6 | `3.24e-11` | `2.12e-8` | `3.24e-11` |
| 8 | `1.42e-12` | `1.38e-10` | `1.42e-12` |
| 10 | `1.23e-13` | `8.15e-13` | `1.23e-13` |
| 12 | `2.00e-15` | `5.79e-14` | `2.00e-15` |
| 14 | `3.08e-16` | `-1.46e-16` | `-1.46e-16` |
| 16 | `2.91e-16` | `-3.96e-15` | `-3.96e-15` |
| 18 | `8.33e-17` | `-3.94e-15` | `-3.94e-15` |

At 14 modes and above, the sign is plainly below double-precision resolution and should not be interpreted. As clarified in v13.291, in the direct Dirichlet `v` basis the odd-index block is the even-`v` sector and the even-index block is the odd-`v` sector.

The correct statement is therefore not that the ground state has been shown to equal zero, but that the previously observed negative spectral floor has been removed down to machine precision.

---

## 7. Important source interpretation

Suzuki emphasizes that `G_a` is compact and its spectrum may accumulate at zero, while `A_a` is unbounded with discrete spectrum accumulating at `+infinity`. In the generalized equation (8.7), the case `lambda=0` is exceptional and corresponds to the kernel of `G_a`.

Therefore a near-zero finite calculation requires special care. Tiny eigenvalues of the direct or preconditioned finite matrix cannot automatically be identified with the ground state of `A_a`; one must distinguish genuine generalized spectral information from approximation to the compact operator's near-kernel. This source point is especially relevant now that the quadrature artifact has been pushed to machine zero.

---

## 8. Revised numerical conclusions

The v13.290 audit establishes numerically:

1. the direct quadratic-form matrix for a difference kernel reduces exactly from 2-D to 1-D;
2. the trigonometric overlap factor is elementary and can be evaluated analytically;
3. prime-power kinks become fixed one-dimensional breakpoints;
4. the slow negative drift seen in v13.289 is reproduced by ordinary 1-D Gauss quadrature;
5. subtracting Suzuki's exact `1/2 t log t + A t` local model removes that drift;
6. at 14 modes, the lowest computed value stabilizes at floating-point zero rather than at a negative `10^-7` scale;
7. the sign of the true `lambda_a` is still not established;
8. `lambda=-5 < lambda_a` remains uncertified.

This is a much stronger numerical diagnosis than v13.289 because it identifies the specific source of the false negative floor rather than merely observing its disappearance under brute-force refinement.

---

## 9. Exact, numerical, and open

Exact/source-established:

- Suzuki equations (1.3), (2.2), (8.6), and (8.7);
- even translation-kernel structure of `g(x-y)`;
- exact 2-D-to-1-D overlap reduction;
- elementary trigonometric overlap formula;
- exact prime-power breakpoint locations;
- exact leading cusp `1/2 |t| log|t| + A|t|`.

Numerically established:

- unsubtracted 1-D Gauss quadrature reproduces the previous negative drift;
- cusp subtraction removes that drift to approximately machine precision;
- no reliable negative spectral signal survives the corrected integration scheme.

Still open:

- distinguish an actual `lambda=0` generalized eigenvalue from finite-section approach to the near-kernel of compact `G_a`;
- obtain a stable positive or negative lower spectral branch, if present;
- produce a rigorous lower enclosure for `lambda_a`;
- certify an admissible Section-8 parameter `lambda<lambda_a`;
- return to the Fredholm differentiation-back test only after that certification issue is resolved;
- D12 transfer remains downstream;
- RH/GRH remains unproved.

---

## 10. Next target

The next audit should exploit the new 1-D representation to separate the matrix into its source components:

\[
A=A_{\rm pole}+A_{\rm prime}+A_{\rm arch}.
\]

The pole and prime-ramp contributions can be integrated to essentially analytic precision against the explicit overlap functions. The archimedean remainder can then be isolated and independently verified at higher precision.

At the same time, the near-zero directions should be inspected through their mode coefficients and through the generalized pair rather than interpreted directly as ordinary matrix eigenvalues.

The preferred v13.291 target is therefore

\[
\boxed{\text{componentwise 1-D matrix audit + high-precision near-kernel classification}.}
\]

That is the cleanest route to deciding whether the stabilized zero-scale signal is a genuine `lambda=0` phenomenon, an approximation-space artifact, or merely the expected compact near-kernel of `G_a`.
