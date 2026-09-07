# Cone Derivation Ledger v13.291 — Componentwise High Precision and Near-Zero Classification

Date: 2026-09-07

Status: SOURCE-TERM DECOMPOSITION + ARBITRARY-PRECISION FINITE-SECTION AUDIT + PARITY-LABEL CORRECTION — FINITE RITZ SECTIONS POSITIVE THROUGH 16 MODES, BUT INFINITE-PROBLEM GAP REMAINS UNRESOLVED — RH/GRH NOT PROVED

## 0. Synchronization and purpose

Immediately before this write, `master` was re-fetched at

`025fb9542c07d206018c516b1d80cc9e6303533a`,

the v13.290 checkpoint.

This entry adds

`research-notes/suzuki_componentwise_high_precision_audit.py`.

The primary source remains Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2. The source facts used here are especially:

- equation (1.3), the exact pole + prime-power ramp + archimedean decomposition of `g`;
- Theorem 1.1, identifying `A_a` as the Friedrichs extension of `B_a=D^*G_aD`;
- Corollary 1.2, allowing the bottom `lambda_a` to be approached through compactly supported smooth / `H_0^1` test functions;
- equation (8.7), the generalized problem `G_a u=lambda K_a u`;
- the statement following (8.7) that `lambda=0` is exceptional and corresponds to the kernel of `G_a`.

The purpose of v13.291 is to determine whether the near-zero values left after the v13.290 cusp subtraction are genuine zero modes or merely finite-precision cancellation artifacts.

---

## 1. Source-level component split

Suzuki equation (1.3) is retained term by term:

\[
g(t)=g_{\rm pole}(t)+g_{\rm prime}(t)+g_{\rm arch}(t),
\]

with

\[
g_{\rm pole}(t)=-4\left(e^{|t|/2}+e^{-|t|/2}-2\right),
\]

\[
g_{\rm prime}(t)=\sum_{p^k\le e^{|t|}}
\frac{\log p}{\sqrt{p^k}}\bigl(|t|-\log p^k\bigr),
\]

and the remaining Hurwitz-Lerch / gamma contribution denoted by `g_arch`.

Using the exact one-dimensional reduction of v13.290, the direct quadratic-form matrix is decomposed as

\[
\boxed{A=A_{\rm pole}+A_{\rm prime}+A_{\rm arch}.}
\]

Each component is integrated independently against the exact analytic trigonometric overlap.

For `a=1`, the prime-power breakpoints are exactly

\[
\log 2,\log 3,\log 4,\log 5,\log 7.
\]

The archimedean contribution is evaluated from Suzuki's convergent local series on `0<=t<=2<pi`, now at arbitrary precision.

---

## 2. Parity-label correction

The previous Neumann-basis statements about the parity of `u=Dv` were correct:

- Neumann mode number `n` odd -> `u` odd;
- Neumann mode number `n` even -> `u` even.

However, after preconditioning, the same index labels the direct Dirichlet basis

\[
\psi_n(x)=a^{-1/2}\sin\left(\frac{n\pi(x+a)}{2a}\right).
\]

Here differentiation reverses parity. Therefore

\[
\boxed{n\text{ odd }\Longleftrightarrow v\text{ even}},
\qquad
\boxed{n\text{ even }\Longleftrightarrow v\text{ odd}}.
\]

Thus any prior language calling the odd-index block the "odd ground-state sector" without specifying whether parity referred to `u` or `v` is ambiguous and is superseded by this convention.

The numerical block decomposition itself was not wrong; only the physical parity label attached to the direct `v` basis required correction.

---

## 3. Why double precision could not classify the smallest modes

At 14 modes, the component matrices have order-one scale, while the lowest combined eigenvalues are many orders of magnitude smaller.

For the first four high-precision eigenvectors, representative Rayleigh contributions are:

| finite eigenvalue | pole contribution | prime contribution | arch contribution |
|---:|---:|---:|---:|
| `4.52e-17` | `+1.62982` | `-0.0936782` | `-1.53614` |
| `3.94e-15` | `-0.0409964` | `+0.394193` | `-0.353197` |
| `3.53e-12` | `+0.880076` | `-0.407277` | `-0.472799` |
| `6.54e-11` | `-0.0662707` | `+0.135619` | `-0.0693487` |

Hence the near-zero spectrum is produced by severe arithmetic cancellation among source terms whose individual magnitudes are `10^-1` to `1`.

This explains why ordinary double precision sometimes returned tiny negative values at the `10^-15` level even after the v13.290 quadrature error had been removed.

Those negative signs were not spectral information.

---

## 4. Arbitrary-precision finite Ritz values

The component matrices were recomputed directly using `mpmath` arbitrary precision, including the exact prime-power weights `log(p)/sqrt(p^k)` rather than promoting double-precision weights afterward.

The lowest finite Ritz values at `a=1` are:

| Dirichlet modes | lowest Ritz value |
|---:|---:|
| 6 | `3.237654258905437e-11` |
| 8 | `1.416731657079581e-12` |
| 10 | `1.232158117461267e-13` |
| 12 | `1.822752686729973e-15` |
| 14 | `4.522349906886357e-17` |
| 16 | `8.3157917635506e-19` |

All of these finite-section minima are positive at the working precision.

This is the first clean resolution of the previous sign ambiguity:

\[
\boxed{\text{the negative }10^{-15}\text{-scale signs were floating-point cancellation artifacts.}}
\]

The higher finite eigenvalues also reproduce the earlier cusp-subtracted values. For example, at 14 modes the first several values are approximately

\[
4.52\times10^{-17},
3.94\times10^{-15},
3.53\times10^{-12},
6.54\times10^{-11},
3.19\times10^{-8},
3.95\times10^{-7},
1.04\times10^{-4},
1.46\times10^{-4}.
\]

---

## 5. What the positivity does and does not mean

The positivity of every finite section tested is useful, but it does **not** establish

\[
\lambda_{a=1}>0.
\]

The lowest Ritz value is collapsing extremely rapidly as the trial space grows:

\[
3.2\times10^{-11}
\to1.4\times10^{-12}
\to1.2\times10^{-13}
\to1.8\times10^{-15}
\to4.5\times10^{-17}
\to8.3\times10^{-19}.
\]

Rayleigh-Ritz supplies upper bounds on the true bottom. A decreasing sequence of positive upper bounds is compatible with either

1. a very small positive ground-state eigenvalue not yet resolved, or
2. a true limiting value `lambda_a=0`.

Distinguishing these possibilities is mathematically decisive and cannot be done by finite positivity alone.

In particular, Suzuki states after equation (8.7) that `lambda=0` is exceptional: the `K_a` term disappears and one is looking at the `0`-eigenspace of `G_a`. An actual proof that `lambda_{a=1}=0` would therefore be a major statement about degeneracy of the localized Weil form and must not be inferred from numerical decay.

---

## 6. Relation to the source discreteness statement

Suzuki states that the generalized spectrum coincides with that of `A_a`, is bounded below and discrete, and accumulates only at `+infinity`.

Therefore the rapidly collapsing Ritz sequence should not be casually interpreted as ordinary compact-operator eigenvalue accumulation at zero in the `A_a` problem.

The correct distinction is:

- `G_a` itself is compact and has spectral accumulation at zero;
- the generalized pair `(G_a,K_a)` represents the unbounded `A_a` spectrum;
- `lambda=0` is a special kernel question for `G_a`;
- finite trial spaces can contain directions with extremely strong pole/prime/arch cancellation without those directions converging to an actual element of `ker G_a`.

This is precisely why a residual / compactness test on the near-null vectors is now more informative than simply adding more modes.

---

## 7. Revised parity statement at a=1

At 14 modes, when parity is stated for the direct `v` basis:

- the odd-index block is the **even-`v`** sector;
- the even-index block is the **odd-`v`** sector.

The very smallest high-precision value lies in the even-`v` sector at this truncation.

This is numerically consistent with the small-`a` theorem that the ground state is even for sufficiently small `a`, but `a=1` is not covered by that asymptotic theorem, and no parity conclusion for the true `a=1` ground state is claimed here.

---

## 8. Exact, numerical, and open

Exact/source-established:

- Suzuki's decomposition (1.3);
- `A_a` is the Friedrichs extension of `D^*G_aD`;
- the bottom can be approached through the form core;
- equation (8.7) and the generalized compact pair;
- `lambda=0` corresponds exceptionally to the kernel of `G_a`;
- `A_a` has discrete lower-bounded spectrum with only `+infinity` as accumulation point.

Exact elementary geometry in this project:

- one-dimensional translation-kernel reduction;
- analytic trigonometric overlap;
- parity reversal under `u=Dv`.

Numerically established in v13.291:

- source components individually have order-one Rayleigh contributions in the near-null directions;
- double-precision negative signs at `~10^-15` are cancellation artifacts;
- high-precision finite Ritz minima are positive through 16 modes;
- the smallest finite Ritz value nevertheless decays from `~3e-11` at 6 modes to `~8e-19` at 16 modes.

Open:

- whether `lambda_{a=1}` is strictly positive or zero;
- whether the near-null Ritz vectors converge in the form/operator topology to an actual zero mode;
- a rigorous positive lower bound for `lambda_a`;
- certification that `lambda=-5<lambda_a`;
- return to the Section-8 Fredholm deficiency computation;
- D12 transfer;
- RH/GRH remains unproved.

---

## 9. Next target

The next calculation should classify the *vectors*, not just their tiny eigenvalues.

For the lowest high-precision Ritz vector `v_M`, compute independently:

1. its `L2` normalization and boundary-layer concentration as `M` grows;
2. the corresponding `u_M=Dv_M` and its `K_a` norm;
3. the off-grid action `G_a u_M` using the cusp-subtracted one-dimensional / row-wise control;
4. a residual normalized in a topology that does not divide by the vanishing Ritz value;
5. overlaps `|<v_M,v_{M+2}>|` after embedding into the larger basis;
6. weak/strong convergence diagnostics.

If the near-null vectors stabilize and `G_a u_M -> 0` in a controlled norm, the zero-kernel hypothesis becomes a concrete numerical conjecture. If instead the vectors run to higher frequencies or boundary layers while overlaps collapse, then the falling Ritz values are a variational escape phenomenon rather than evidence for a true kernel element.

The preferred v13.292 target is therefore

\[
\boxed{\text{near-null Ritz-vector compactness, overlap, and operator-residual audit}.}
\]

Only after this vector-level audit should the project revisit the sign of `lambda_{a=1}` or the admissible-`lambda` question.
