# Cone Derivation Ledger v15.840 — Gravity: an isolated sourced TT tensor gives a spurious remote initial tidal acceleration unless full gravitational constraints are completed

**Date:** 2026-11-12 US Eastern. **Parents:** v14.935 fixed EH+relativistic-solid K4 action; v15.727 canonical positive local-energy matter; v15.750 and v15.818 source-first K4 metric evolution, v15.787 complete local full-Riemann formula; v15.838 compact canonical source with nonlocal TT stress outside support; v15.839 full-spectrum *local canonical field* obeying finite domain of dependence at separated receiver. **Live HEAD immediately prewrite:** 17eaa09fda37291344781e21278eaa66f2ec0d13, target path absent. Additive-only; historical/audited and Suzuki assets untouched.

**Status:** [D] exact initial tensor-sector equation-to-Riemann contact formula under zero dynamical tensor displacement/velocity; [N] refined numerical nonzero remote *isolated tensor sector* electric-Riemann from nonlocal TT-projected compact canonical stress; [N] this is **not a physical acausal gravitational signal** and must not be called a complete local curvature result; [O] full constrained Einstein+solid scalar/vector/tensor initial data and their physical complete Riemann cancellation/causal comparison.

## Gate 480 — the limitation of imposing zero tensor displacement independently

The v15.838 canonical scalar source is compact in a sphere radius 2.5 centered at (6,0,0) on τ=1 in coasting FLRW. At a receiver at the origin, the local matter stress is exactly zero, but the Fourier rank-two TT projection of its anisotropic spatial gradient stress **S_ij=∂iχ∂jχ** is nonzero by the nonlocal action of inverse-Laplacian projectors. Its physical orthonormal stress on this initial coasting slice is **Π^TT_ij=a(1)^{-2} S^TT_ij=3 S^TT_ij**, using a(1)=1/sqrt3.

The archived K4 tensor equation for each TT tensor component with scalar amplitude normalization consistent with v15.750/818 is

**γ̈_TT+3γ̇_TT/τ + [3|k|²+8η_s/3]γ_TT/τ²=−2 Π^TT**,

with η_s the solid elasticity parameter. The directly metric-derived full tensor-sector electric Riemann on the coasting background is

**R^i_(0j0)|TT=−(γ̈_TT+2γ̇_TT/τ)/2**.

At τ0=1, impose the common zero **propagating tensor** initial conditions **γ_TT(1)=γ̇_TT(1)=0** *at every Fourier k*. Then the actual sourced Euler equation instantaneously fixes

**γ̈_TT(1,x)=−2Π^TT(1,x)**,

and the isolated TT-sector curvature is therefore **R^i_(0j0)|TT(1,x)=Π^TT(1,x)**.

Since the TT projection is spatially nonlocal, its value can be nonzero outside the compact **local** matter support. This identity is an exact conditional result for the tensor-sector variables; it is not, by itself, a complete solution of the gravitational Hamiltonian/momentum constraints or the optical detector.

## Gate 481 — quantified remote tensor-only false-front amplitude

Apply the same C7 compact canonical stress and receiver as v15.838, and calculate the conditional initial full tensor-sector electric Riemann **under the above zero tensor displacement/velocity preparation**, with the exact Fourier TT projector and its k=0-zero convention, across 96³,112³,128³ periodic grids (L=24):

| Grid | raw local stress S_ij(receiver) | isolated tensor-sector |R^i_(0j0)|TT, Frobenius |
|---|---:|---:|
| 96³ | exactly 0 | **0.00469661089986996** |
| 112³ | exactly 0 | **0.00469682397433449** |
| 128³ | exactly 0 | **0.00469703904076650** |

The result is exactly **3 × the spatially TT-projected source norm** from v15.838, via the algebraic Euler equation at the initial slice. Its refinement range is ~4.28×10^-7 while amplitude ~4.70×10^-3. It is therefore not numerical pollution from the originally compact local source. The associated source decomposition is deliberately nonlocal; these are *tensor-only metric-sector amplitudes* and are not an independent observation of gravity arriving at a receiver.

**Reproducer:** research-notes/k4_sourced_tensor_initial_remote_projection_v15_840.py, commit **17eaa09fda37291344781e21278eaa66f2ec0d13**. It imports the unchanged v15.838 compact source/TT projector, verifies the tensor Euler equation-to-curvature relation with exact SymPy algebra and reuses 96³,112³,128³ independent Fourier stresses for the remote 3× norm check. The Euler-to-Riemann identity was independently locally checked; exact committed file reexecution awaits audit. No image generator or certified overwrite.

## Gate 482 — do not confuse nonlocal projection, constraint data and superluminal physical signals

The fact that the isolated TT-sector Riemann contribution is nonzero at the remote receiver on the initial slice does **not** establish an acausal physical change. A source with nonzero total energy generally imposes *nonlocal* gravitational constraint data outside its own support on any spacelike slice; setting **all** gravitational perturbations to zero initially while retaining compact matter may violate constraints. Even with valid global initial data, an SVT-decomposed piece need not have the locality properties of a complete gauge-invariant curvature or a true causal difference of two physical solutions with matching initial exterior geometry.

The correct physical comparison must solve the *full* Einstein+solid Hamiltonian and momentum constraints with the canonical matter field on τ=1, determine all scalar/vector/tensor metric data and elastic material displacements, and compute **the full local Riemann curvature** and clock/photon/mirror observable at the receiver. Distinguish preexisting exterior curvature from a *new* signal reaching it. Compare two matched-constraint physical solutions with identical receiver past to test causal onset. Only after such complete data are supplied is an early tensor-sector term meaningfully classified as canceled, compensated or part of a physically preexisting exterior field.

**Negative/originality:** this projection artifact is standard constrained-gravity/SVT physics, not evidence for a new Cone force, light-speed violation, 1/4 Casimir mass gap, nor new value of measured G. The frozen K4 action remains exactly ordinary Einstein–Hilbert + isotropic solid, so matched conventional GR+solid produces identical results.

**HANDOFF — external audit:** independently rederive the exact tensor Euler and Riemann contact and audit the 3× physical anisotropic-stress normalization, 3-grid remote TT amplitudes and k=0 prescription; verify this cannot be interpreted as a complete causal observable. Confirm v15.838/839 complete field and projector claims first.

**NEXT:** derive the full K4 Hamiltonian/momentum constraint solution for an explicitly localized canonical stress distribution on the coasting background, reconstruct **all** gauge and solid contributions to the remote electric Riemann, and contrast causally changing source perturbations with identical incoming/exterior gravitational initial data. A truly remote five-helicity photon/clock/gradiometer detector remains the next major physical implementation; no new Cone-specific residual is claimed.
