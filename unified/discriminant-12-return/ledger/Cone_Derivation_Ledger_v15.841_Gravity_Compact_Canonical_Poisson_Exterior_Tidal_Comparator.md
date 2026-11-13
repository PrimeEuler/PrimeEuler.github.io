# Cone Derivation Ledger v15.841 — Gravity: exact compact positive-energy canonical matter yields a pre-existing exterior elliptic-constraint tidal field in the ordinary Poisson comparator

**Date:** 2026-11-12 US Eastern. **Parents:** v15.727 canonically derived positive local scalar energy, v15.835 spatial Fourier nonlocality, v15.838 TT projection of compact stress is nonlocal, v15.839 causal physical KG matter front, v15.840 zero-initial-tensor-velocity conditional remote TT curvature. **Immediately prewrite live HEAD:** c3a1f8ca830a7264df91e4a102663f31a03164b3. Target absent; additive only, certified Suzuki and earlier K4 payloads untouched.

**Classification:** [D] exact canonical scalar initial energy integral and an analytic ordinary elliptic Poisson exterior-field solution with symbolic coupling; [N] that a pre-existing exterior constraint field is not evidence of causal source transmission, and neither this benchmark nor the isolated tensor-only v15.840 term is a complete K4 receiver result; [O] K4 action-derived full Hamiltonian/momentum constraints, their consistent exterior initial data and physically sourced/causally varied remote detector.

## Gate 483 — compact matter does not imply compact gravitational constraint data

Take a **different** C7 compact, spherically symmetric canonical scalar initial condition on the same coasting scalar background at cosmic tau=1:

**χ(r)=[1−(r/R)²]^8** for r<R, and zero outside; **χdot=−χ**.

Since a(1)=1/sqrt3, the **actual local canonical energy density** inside the support is

**ρ(r)=1/2[χ(r)²+3(dχ/dr)²] ≥0**, and zero for r≥R. The integrated initial energy is

**M=4π∫_0^R ρ(r)r²dr**

**=π R³[B(3/2,17)+(768/R²)B(5/2,15)] >0**,

where B is the Euler beta function. This is an **exact** finite-energy integral derived from the canonical field and its cutoff derivative, not an inserted point-mass ansatz.

For a *separate ordinary weak-field elliptic-constraint comparator*, let a scalar Newtonian potential obey **∇²Φ=λρ** on infinite flat space, with Φ→0 at infinity. Keep λ symbolic (no measured G, no proposed Cone identification). For a spherically symmetric compact positive density, Gauss's law gives outside its support (at d>R)

**Φ(d)=−λ M/(4πd)**.

The receiver's local matter stress and density vanish there, but the elliptic gravitational potential is already nonzero on the same initial slice. This is not acausal signal propagation: the gravitational constraint must hold for the entire set of initial data, and cannot be prepared independently of the source.

## Gate 484 — exact exterior tidal eigenvalue ratio, no novel scale

The exterior spatial tidal Hessian **H_ij=∂i∂j Φ** in a radial orthonormal frame has transverse eigenvalues **H_⊥=+λM/(4πd³)** (multiplicity two) and radial eigenvalue **H_r=−2λM/(4πd³)**. Its trace is zero outside the matter source, its squared norm is **6[λM/(4πd³)]²**, and

**H_r/H_⊥ = −2**

independently of λ, M and distance d for this spherical exterior Laplace solution. This is the familiar Newtonian monopole tidal ratio, **not** a Cone-specific force, 2/3 Casimir selector or measurement of G. The signal amplitude is proportional to the unspecified λM: no gravitational coupling has been predicted.

For **R=5/2,d=6**, exact beta integration numerically gives

**M≈8.770258719877843**,

**Φ(d)/λ≈−0.11631916895528**,

**H_⊥/λ≈+0.003231088026535548**,

**H_r/λ≈−0.006462176053071097**.

All are **pre-existing initial constraint** quantities in the ordinary comparator, not distant-photon readings or radiative fronts. Their radial/transverse ratio is a standard geometry consequence of ∆Φ=0 in the exterior.

## Gate 485 — how to falsify an apparent remote arrival

The prior v15.840 isolated K4 TT curvature term can be nonzero outside the compact canonical material support because its SVT projector is nonlocal; the present ordinary Poisson comparator can also have genuine nonzero exterior gravitational curvature on an initial slice even when *local* matter density vanishes there. These must not be conflated. In a fully constrained Einstein+solid calculation one must decide, from **the original action-derived Hamiltonian/momentum constraints**, which part of the exterior metric/curvature is genuine physical initial data and which is a nonlocal sector decomposition compensated by other sectors.

An actual causality test should compare **two physical solutions with identical initial data in the receiver's causal past**, including gravitational field/solid data and constraints, and ask whether their receiver **difference** remains zero until their causally differing data reach it. It must not ask whether the *absolute* remote curvature is initially zero. A nontrivial canonical spectator cannot simply switch on from exactly zero Cauchy data without a physical dynamical production process, as already warned in v15.727.

**Reproducer:** research-notes/k4_constraint_comparator_v15_841.py, additive commit **c3a1f8ca830a7264df91e4a102663f31a03164b3**. Locally executed exact SymPy integration of canonical energy and beta identity, exterior Poisson solution, Hessian eigenvalues, trace, Frobenius norm, and exact ratio. New committed file awaits external audit.

**HANDOFF — independent audit:** check canonical ρ and beta integral, Hessian signs and λ normalization, and that the example is **explicitly a comparator** not a claimed original K4 Poisson constraint; audit v15.838–840 separately and prioritize the complete first-class constrained K4 scalar/vector/tensor reconstruction.

**NEXT:** formulate the *linearized full K4 initial-constraint problem* for a compact canonical scalar source, including the nonzero elastic-solid background; identify admissible exterior initial field data and compare causally differing solutions at a distant observer. Proceed to five-helicity full-spectrum optical receiver only after constraint-compatibility and initial-event identification are under control. The matched EH+relativistic-solid model still has exactly zero Cone-specific subtraction.
