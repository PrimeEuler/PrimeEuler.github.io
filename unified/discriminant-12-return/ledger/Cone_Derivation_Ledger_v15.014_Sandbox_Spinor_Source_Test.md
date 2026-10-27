# Ledger v15.014 — Sandbox spinor-source test: q_χ does not power the k4 coasting source (identification closed negative, three regimes)

**Lane:** Sandbox (little Euler), taken up at Jeremy's direction
2026-10-27 as the successor to v14.990. **Parents:** v14.990 (pair
spinor, q_χ = −ρṡ, healthy ℏℤ Noether charge; source identification
left conjectural), v14.959 (exponential-scalar coasting), v14.992
(triplet on-background charge density zero). **Payload:**
`payloads/spinor_source_test_v15_014/` (NOTE.md, spinor_source.py,
integrate.py). Suzuki quarter PARKED; protected lanes untouched.

## Setup [D]

Deposited family S = ∫√−g[(1/2)|∂χ|² − V(|χ|)], minimal coupling,
homogeneous χ = r(τ)e^{iθ(τ)} on flat FLRW vs the k4 target
(H = 1/τ, ρ = 3/(κτ²), w = −1/3). ρ_χ = K + V, p_χ = K − V,
K = (ṙ² + r²θ̇²)/2; w = −1/3 ⟺ V = 2K. Minimal coupling preserves
the θ-shift symmetry exactly: a³r²θ̇ = Q conserved for every V(r);
q_χ = Q/a³. (The charge EXISTS on-background, unlike the triplet's
zero — and still fails to source, as follows.)

## Results [D]

1. **Exact charged coasting: none, for any V.** r = const gives
K ∝ a⁻⁶ vs constant V. Power-law r ∝ a^{−β}: ṙ² half of K needs
β = 0, charge half Q²/(2a⁶r²) needs β = 2 — incompatible at Q ≠ 0.
The family's only exact coasting solution is the Q = 0 exponential
tracker (μ = √(2κ), KG residual 0): v14.959 recovered, charge
identically zero.
2. **Generic charged data (fixed exponential V): coasting attracts,
charge decouples.** Numerics (κ = 1; Q = 1, 50; modulus perturbed):
ρτ² → 2.989, Hτ → 0.998, w → −0.3333 by τ = 3000 (on-tracker
control exact at 3, 1, −1/3). Charge energy footprint ∝ a⁻⁶
(relative a⁻⁴): 10.4% → 5×10⁻¹² in the Q = 50 run; θ̇ → 0 (phase
freezes); q_χ/ρ ~ a⁻¹ → 0. Surviving source = chargeless tracker.
3. **Charge-dominated branch (r = c/a²) is state-tuned.** It forces
V linear with λ = Q²/c³ (potential encoding the state) and pins
the charge to Q* = (2/(3κ))^{3/4}λ^{−1/2} for fixed (λ, κ);
asymptotic only (O(a⁻⁶) inexactness in ρ). Modulus → pair-space
tip; tracker modulus grows logarithmically; neither sits at a seat.
4. **Perturbations (frozen background):** canonical kinetic,
c_s² = 1, no ghosts. Phase mass² = V'(r)/r: exponential branch
tachyonic but mild (|m²|/H² ~ 1/ln τ → 0, sub-power-law growth);
linear branch heavy/healthy (m²/H² ~ 3λa⁴/c → ∞).

**Flags:** spinor_source_identification=CLOSED_NEGATIVE (regimes:
zero / decoupled / state-tuned); exact_charged_coasting=NONE_ANY_V;
q_chi_conservation=EXACT (a³r²θ̇ = Q); charge_footprint=a⁻⁶;
v14.990 carrier result=UNTOUCHED; Q=0 amplitude matching (κC
species)=STILL_REQUIRED; G_derived=false; Suzuki_quarter=PARKED.

**Scope:** homogeneous, minimal coupling, V = V(|χ|) as deposited.
Inhomogeneous spinor configurations untested; θ-dependent or
nonminimal couplings are outside the family and break the symmetry
that makes q_χ exist.

## Handoffs

→ **external-audit:** verification of the payload.
→ **gravity lane:** the pair-side source hunt's last open door
(v14.988/v14.990 conjecture) is closed from the sandbox side; no
action requested — the triplet remains the source of record, with
its own amplitude matching still open on your side.
