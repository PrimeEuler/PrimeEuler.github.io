# Cone Derivation Ledger v13.292 — Near-Null Ritz-Vector Convergence and Kernel Candidate

Date: 2026-09-07

Status: HIGH-PRECISION NESTED-RITZ VECTOR TRACKING + OFF-GRID SOURCE-KERNEL RESIDUAL + NO HIGH-FREQUENCY/BOUNDARY ESCAPE DETECTED — NUMERICAL KERNEL CANDIDATE EMERGES — NOT A PROOF OF NONTRIVIAL KERNEL, RH, OR GRH

## 0. Purpose

v13.291 established that the apparent negative finite-section values in ordinary floating point were sign loss caused by large cancellation among the pole, prime-ramp, and archimedean pieces. At arbitrary precision, the finite Ritz minima through 16 modes remained positive but collapsed rapidly toward zero.

That left two qualitatively different possibilities:

1. the Ritz minimizers could be escaping into increasingly oscillatory or boundary-localized directions, as one expects when a compact operator has a large near-kernel but no convergent kernel vector in the tested topology; or
2. the minimizers could converge to a genuine smooth vector `v`, with `u=Dv` approaching a nonzero element of `ker(G_a)`.

v13.292 therefore tracks the Ritz vectors themselves.

This entry adds

`research-notes/suzuki_near_null_vector_audit.py`.

The source-level framework remains Suzuki arXiv:2606.09096v2, especially equations (8.6) and (8.7), with the `lambda=0` case interpreted as an actual kernel condition for `G_a`.

---

## 1. Nested finite spaces and normalization

Use the normalized Dirichlet basis

\[
\psi_n(x)=a^{-1/2}\sin\!\left(\frac{n\pi(x+a)}{2a}\right),
\]

and let

\[
v_M(x)=\sum_{n=1}^M c_n^{(M)}\psi_n(x),
\qquad \|c^{(M)}\|_2=1.
\]

The corresponding differentiated Neumann representation is

\[
u_M=Dv_M,
\qquad
u_M\sim \sum_{n=1}^M k_n c_n^{(M)}\phi_n,
\qquad
k_n=\frac{n\pi}{2a}.
\]

The finite matrix is the same direct quadratic-form matrix audited at arbitrary precision in v13.291.

For nested dimensions `M < N`, compare

- the embedded `L2` overlap of `v_M` with `v_N`;
- the embedded normalized `L2` overlap of `u_M` with `u_N`;
- the norm of the newly introduced high-mode tail.

These diagnostics directly test whether the near-null sequence is escaping to higher frequencies.

---

## 2. The vectors do not escape to high frequency

For the numerically reliable nested sequence `M=6,8,10,12`, independently reproduced coefficient vectors give approximately

| transition | embedded overlap of `v` | normalized embedded overlap of `u=Dv` | new `v` tail norm |
|---:|---:|---:|---:|
| 6 -> 8 | `0.99687` | `0.98824` | `1.31e-2` |
| 8 -> 10 | `0.9999745` | `0.9999241` | `8.81e-7` |
| 10 -> 12 | `0.9994331` | `0.9982715` | `1.16e-4` |

The lowest vectors are therefore strongly aligned across nested spaces.

This is the opposite of a sequence whose mass migrates to the newly available highest modes.

The dominant even-`v` coefficient pattern is already visible at low dimension. Representative normalized coefficients are approximately

\[
M=6:\quad
(0.9011,0,-0.4269,0,0.0762,0),
\]

\[
M=10:\quad
(0.8673,0,-0.4792,0,0.1341,0,-0.0143,0,\text{tiny},0).
\]

The candidate is therefore a low-frequency even function of `v`; equivalently `u=Dv` is odd.

---

## 3. Frequency diagnostics remain bounded

Define the spectral centroid

\[
\bar n_M=\sum_{n=1}^M n|c_n^{(M)}|^2.
\]

For `M=6,8,10,12`, the reproduced values are approximately

| M | spectral centroid | `||u_M||_2` |
|---:|---:|---:|
| 6 | `1.388` | `2.532` |
| 8 | `1.519` | `2.816` |
| 10 | `1.532` | `2.844` |
| 12 | `1.597` | `2.979` |

Neither quantity exhibits rapid high-frequency growth.

In particular, the `H^1`-scale quantity `||Dv_M||_2=||u_M||_2` remains of order unity across the tested sequence rather than diverging with `M`.

This is an important compactness signal: the candidate is not buying a small quadratic form by pushing its energy into arbitrarily high basis frequencies over this range.

---

## 4. The candidate is not boundary localized

The normalized `L2` mass of `v_M` in the outer 20% of the interval,

\[
|x|>0.8a,
\]

falls sharply with dimension:

| M | boundary mass `|x|>0.8a` | central mass `|x|<0.2a` |
|---:|---:|---:|
| 6 | `4.42e-6` | `0.681` |
| 8 | `5.30e-7` | `0.736` |
| 10 | `3.67e-7` | `0.740` |
| 12 | `6.85e-8` | `0.762` |

Thus the near-null sequence becomes more concentrated in the interior rather than forming a boundary layer.

Again this runs against the most obvious finite-section artifact scenario.

---

## 5. Independent off-grid kernel residual

A finite Ritz eigen-equation is not by itself enough to identify a kernel element, because the residual vanishes only after projection back into the same trial space.

The new audit therefore evaluates

\[
P_aG_a u_M
\]

independently on an off-grid Gauss set using the original source screw kernel `g_fast`, with row-dependent prime-power breakpoints. This code path does not reuse the one-dimensional Ritz matrix.

The normalized residual

\[
\rho_M=
\frac{\|P_aG_a u_M\|_{L^2}}{\|u_M\|_{L^2}}
\]

is approximately

| M | `||P_a G_a u_M||_2` | normalized residual `rho_M` |
|---:|---:|---:|
| 6 | `2.86e-7` | `1.13e-7` |
| 8 | `1.06e-7` | `3.77e-8` |
| 10 | `1.29e-8` | `4.53e-9` |
| 12 | `1.57e-9` | `5.27e-10` |

The residual decreases by more than two orders of magnitude across the sequence.

The mean removed by `P_a` is at numerical roundoff scale in these tests, so the decay is not being manufactured by a large constant-mode subtraction.

---

## 6. Joint interpretation with v13.291

v13.291 found high-precision positive finite Ritz values

\[
3.24\times10^{-11},
1.42\times10^{-12},
1.23\times10^{-13},
1.82\times10^{-15},
4.52\times10^{-17},
8.32\times10^{-19}
\]

for `M=6,8,10,12,14,16` respectively.

By themselves, values collapsing toward zero could have represented mere compact near-kernel behavior.

v13.292 adds three independent structural facts:

1. the nested Ritz vectors are strongly aligned;
2. their frequency scale remains bounded and their new high-mode tails remain small;
3. an off-grid source-kernel residual `||P_aG_a u_M||/||u_M||` decreases rapidly toward zero.

Together, these observations provide positive numerical evidence that the sequence is converging toward a smooth nonzero kernel candidate for `G_a` at `a=1`.

This is materially stronger than merely observing small singular/eigenvalues of finite matrices.

---

## 7. What this does NOT establish

The present evidence is still numerical.

It does **not** yet establish that

\[
\ker G_1\neq\{0\}.
\]

To promote the candidate to a theorem, one would need controlled statements such as:

- a rigorously convergent sequence `u_M -> u` in a topology strong enough for `G_a u_M -> G_a u`;
- a proof that the limit is nonzero;
- a certified residual bound tending to zero;
- or an analytic construction of the limiting candidate satisfying the integral equation exactly.

Accordingly, this audit does not establish `lambda_1=0`, does not establish the sign of the generalized spectral bottom in any theorem-level sense, and does not prove RH or GRH.

The Section-8 admissibility statement `lambda=-5 < lambda_a` also remains uncertified by the current finite Ritz evidence alone.

---

## 8. Parity interpretation

The converging candidate lies in the odd-index Dirichlet sector.

Because

\[
\psi_n(-x)=(-1)^{n+1}\psi_n(x),
\]

odd `n` corresponds to **even `v`**.

Differentiation reverses parity, so

\[
u=Dv
\]

is **odd**.

This parity convention is now fixed throughout the Suzuki control ledger.

---

## 9. Revised status

Numerically established in the present audit:

- no observed migration of the near-null Ritz vector toward the highest available modes through `M=12`;
- strong nested-space alignment of both `v_M` and normalized `u_M`;
- bounded low spectral centroid and `||u_M||_2` over the tested range;
- rapidly vanishing boundary mass and increasing central mass;
- independently evaluated off-grid normalized kernel residual decreasing from about `1.1e-7` to `5.3e-10`;
- a coherent smooth even-`v` / odd-`u` kernel candidate.

Still open:

- rigorous convergence of the candidate;
- analytic identification of its limiting shape;
- proof or disproof of `ker G_1 != {0}`;
- theorem-level classification of the exceptional `lambda=0` case;
- rigorous lower enclosure for the nonzero generalized spectrum;
- certification of a Section-8 `lambda<lambda_a`;
- D12 transfer;
- RH/GRH.

---

## 10. Next target

The numerical candidate is now coherent enough that the next step should no longer be another brute-force eigenvalue refinement.

The highest-value v13.293 target is to identify the limiting function itself.

Two complementary routes are suggested:

1. **coefficient recognition / analytic ansatz** — extend the high-precision odd-index coefficient sequence and test whether it matches a simple cosine/hyperbolic/special-function expansion;
2. **direct integral-equation reconstruction** — interpolate the converged `u(x)` candidate and test the equation

\[
P_aG_a u=0
\]

componentwise in the pole, prime-ramp, and archimedean pieces, looking for an analytic cancellation identity.

A successful identification would convert the present numerical kernel candidate into a mathematically structured object and would determine whether the near-zero branch is genuinely exceptional or merely an extraordinarily well-conditioned approximation.

The preferred next checkpoint is

\[
\boxed{\text{high-precision kernel-candidate reconstruction + coefficient/functional identification}.}
\]
