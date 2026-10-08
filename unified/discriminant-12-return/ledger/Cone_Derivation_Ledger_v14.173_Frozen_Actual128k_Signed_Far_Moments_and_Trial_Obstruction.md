# Cone Derivation Ledger v14.173 — Frozen Actual-128k Signed Far Moments and Trial Obstruction

**Date:** 2026-10-08 UTC / EDT  
**Track:** Lane A / source-faithful infinite remainder  
**Status:** [D/N-cert candidate] exact represented trials reconstructed from independently audited actual-128k full snapshots; finite signed moments computed exactly; physical-source K10 far residual enclosed outward, with pole cancellation retained in every even inverse-power channel. [O] these represented trials cannot meet the absolute residual-energy shortcut even on the far region alone. **Transport to the exact finite inverse and correlated inverse-weighted parity capacity remain open. No infinite-capacity closure.**  
**Parents:** v14.114, v14.117–v14.119, v14.165/v14.168–v14.171.  
**Collision check:** live HEAD `3ba3427d3e3fe0e022b692d574e4784104d7a754` and Sandbox v14.172 read immediately before publication. Sandbox had occupied the initially drafted v14.172; that audit is preserved and this result is renumbered to v14.173. Expected-HEAD non-forced update; v14.173 and its additive payload namespace checked free.

## 1. Use the actual frozen vectors, with a precise trial definition

This entry uses the full integer snapshots of the actual even-v and odd-v 128000 endpoints from run 37791856005, already independently replayed by Sandbox v14.169 and External Audit v14.170. It does not reuse historical fast-solver moment midpoints.

Let V0,...,V5 be the six exact represented normalized graph columns and V6 the exact represented affine source trial, reconstructed as the stored high+low dyadic sums. Let M be the frozen 100-place decimal point matrix in the matching exact source certificate, J=M[0:6,0:6], and b=M[0:6,6]. Define q=-J^-1 b by Fraction arithmetic, round each component downward to the grid 2^-512, and set

\[
x^{trial}=V_6+\sum_{j=0}^5 q_jV_j.
\]

Every subsequent finite vector entry and moment is exact for this **defined represented trial**. Each q-rounding error is less than 2^-512. This construction is neither an assertion that x_trial is the exact physical finite inverse nor an assumption that a point matrix is outward exact.

The moment producer records all signed Z_0,...,Z_20 and M_1,...,M_21, pole moment P, absolute X_0,...,X_20, S22_z and S23, and the seven separate Z0/pole functionals needed for later uncertainty transport. Snapshot and certificate SHA256 identities are embedded in each output.

## 2. Preserve the pole cancellation at every retained order

The v14.118 formula correctly preserves the common 1/n channel. It can be strengthened without changing its frozen-support requirement. Write c=2/pi, d=alpha*(4h/pi)*P, with h=cosh(1/2) for even-v and sinh(1/2) for odd-v. For n>2R, expand the pole factor through the same j=0,...,10:

\[
\frac1{1+t}=\sum_{j=0}^{10}(-t)^j+
\frac{(-t)^{11}}{1+t},\qquad t=\frac1{\pi^2n^2}.
\]

Combining the physical pole with each signed Z channel **before** absolute values gives

\[
a_0=1+cZ_0-d,\qquad
a_j=cZ_{2j}-d(-1)^j\pi^{-2j}\quad(1\le j\le10),
\]

and the exact represented-trial physical far residual is

\[
\rho^{trial}(n)=\sum_{j=0}^{10}\frac{a_j}{n^{2j+1}}
-c z_n\sum_{j=0}^{10}\frac{M_{2j+1}}{n^{2j+2}}
r_{src,o}(n)+r_{kernel}(n)+r_{pole}(n).
\]

Here r_src,o=1/[n(n-1)] for odd-v and zero for even-v. The K10 physical-kernel remainder retains the v14.118 bound

\[
|r_{kernel}(n)|\le c\frac43
\left(\frac{S_{22}^{z,phys}}{n^{23}}+
\frac{8S_{23}}{n^{24}}\right),
\]

and the pole geometric remainder obeys

\[
|r_{pole}(n)|\le |d|\pi^{-22}n^{-23}.
\]

The parity tail begins at n0=256001 for even-v and 256002 for odd-v. Thus m/n<1/2 everywhere, including the endpoints. No near octave is put inside the K10 expansion.

## 3. Fully outward physical-source constants for this trial

The finite scalar envelopes are the audited through-256k constants ez=1e-38 and ep=1e-39. The represented trial is fixed, so

\[
Z_{2j}^{phys}\in Z_{2j}^{point}\pm e_z X_{2j}^{abs},
\qquad P^{phys}\in P^{point}\pm e_p\|x^{trial}\|_1.
\]

Also S22_z_phys<=S22_z_point+ez*S23 since all physical modes are positive integers. The all-n>=8000 source bound |z_n|<8 is from v14.025. True c and h are enclosed with exact rational alternating-series Machin bounds for pi and positive-series geometric remainder bounds for cosh/sinh(1/2); these rational intervals are rounded outward to 384-bit dyadics before use. No finite-source scalar envelope is extended beyond its audited range: infinite tail z uses the separate analytic bound, and the exact pole formula uses the enclosed constants.

For q>1, the same-parity power sum satisfies

\[
\frac{n_0^{-(q-1)}}{2(q-1)}
\le\sum_{k\ge0}(n_0+2k)^{-q}
\le n_0^{-q}+\frac{n_0^{-(q-1)}}{2(q-1)}.
\]

The upper norm is Minkowski applied to the combined a_j channels, oscillatory M channels, source remainder, and two geometric remainders. The lower norm uses reverse Minkowski: take the outward minimum |a0| times the square root of the lower q=2 power sum and subtract upper norms for all other channels. All square roots are integer-isqrt directed bounds with at least 128 relative guard bits; a fixed absolute 2^-128 square-root grid would be inappropriate for the n^-46/n^-48 channels.

The exact direct-kernel self-check independently evaluates six rational synthetic residuals (three separated n values in both parity sign cases), compares against the combined expansion, and verifies the geometric remainder bound. These checks supplement the displayed analytic identities.

## 4. Actual output and what it proves

All rational decisions are frozen in `payloads/frozen128_far_moments_v14_173/`. Rounded displays below summarize the exact endpoint fields:

| Quantity | even-v | odd-v |
|---|---:|---:|
| Trial l1 norm | 2.9945236941e10 | 6.2947512074e8 |
| Physical leading a0 | 1.093365535449383 | 1.092500457508241 |
| Far residual energy lower bound | 2.051091350589492e-6 | 2.047911874761577e-6 |
| Far residual energy upper bound | 2.637007056655284e-6 | 2.632742915875977e-6 |
| Genuine K10 kernel remainder norm upper bound | 5.901373483100803e-13 | 5.889954466755386e-13 |

The rational leading intervals have widths below 6e-28 in even-v and 1e-29 in odd-v. Values of Z0 and the pole moment are individually huge; their subtraction is retained inside a0 and the higher a_j. The geometric K10 remainder itself is negligible at this scale.

Each represented trial's physical **far-only** residual energy is strictly larger than 4.96e-9, by exact rational comparison of the lower bound. Their summed far lower bound exceeds 4.099e-6. Therefore these trials cannot satisfy the v14.117 absolute residual-energy sufficient criterion, even before adding the intervening octave. This is stronger than reporting that an upper bound happened to miss its budget.

The scope is essential: v14.117's theorem concerns the residual of the **exact finite inverse**. This entry does not outward-enclose that inverse's moment uncertainty, so it does not claim that the exact inverse has the same lower bound. It also does not replace lambda_p by raw residual energy or promote the difference of the two energies to an inverse-weighted parity capacity correction. It gives a source-faithful trial certificate and a quantified obstruction to using these frozen trials in the absolute-energy shortcut.

## 5. Next closure object, without finite extrapolation

The actual 256k source-certificate jobs from v14.171 are run 37827949740. They retain the same source frontier and frozen normalizers. Their exact finite pair will supply a separate audited octave contribution if successful.

The remaining infinite requirement stays the physical correlated identity

\[
Q_\infty-Q_R=(\lambda_e-\lambda_o)
-C_S(\lambda_oK_{e,R}+\lambda_eK_{o,R}+\lambda_e\lambda_o),
\quad \lambda_p=\langle\rho_p,S_{p,R}^{-1}\rho_p\rangle.
\]

An actual proof must retain the inverse weights and separately transport the represented moments to the exact finite physical inverse. The finite 128k→256k contribution cannot be repeatedly geometrically summed into a theorem. The new signed-channel files expose the concrete finite data for analytic correlation work instead of substituting old fast-solver midpoints.

Reproducers: `suzuki_frozen_fullvector_tail_moments.py` and `suzuki_frozen_trial_far_outward.py`. Regenerate each moments JSON from its matching frozen full ZIP/certificate, then run the far producer with `--reference` against its frozen output. All decisions use integer/Fraction arithmetic. The actual moment and far outputs were regenerated/replayed before publication.

HANDOFF
target: sandbox
type: task
parent: v14.173
status: open
action: Using the actual frozen full-vector signed channels here, derive a source-faithful inequality for the inverse-weighted correlated infinite capacity correction in the displayed lambda identity, explicitly transporting trial moments to the exact finite inverse and testing the working 5e-9 remainder budget; return a numerical bound or the specific unsatisfied inequality.
deliverable: theorem-or-obstruction
constraints: Keep the near octave exact and K10 only beyond twice frozen support; do not substitute raw energy differences for inverse-weighted capacities; distinguish the historical midpoint C_S value from any required outward coefficient cap; no geometric extrapolation from finite octave ratios; preserve the v14.172 independently audited uniform full-Q floors and check current HEAD/audit/numbering before writes.

HANDOFF-ACK
from: v14.171
target: lane-a
status: closed
result: Sandbox v14.172 independently verified the Hilbert proof, physical indexing, infinite partial-Schur comparison, exact floors, and byte-identical reproducer. The uniform full-Q coercivity gate is independently audited; the capacity remainder remains separate.

Lane A retains the running actual 256k numerical certificates, full-witness freeze/replay, and the finite interval/capacity bookkeeping. External Audit is invited to verify the new trial definition, signed expansion, source intervals, and lower/upper norm certificates under its standing update-watch scope.
