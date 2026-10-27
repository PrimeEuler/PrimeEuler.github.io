# Spinor-source test: can the pair spinor's charge power the k4 coasting source? (Sandbox)

**Successor to v14.990**, which left the identification "source = q_χ"
as a conjecture with a healthy model attached. Test: the deposited
action family S = ∫√−g[(1/2)|∂χ|² − V(|χ|)] (minimal coupling, V any
function of the modulus r = |χ| = √(2T)), homogeneous χ = r(τ)e^{iθ(τ)}
on flat FLRW, against the k4 target: coasting history H = 1/τ,
ρ = 3/(κτ²), w = −1/3 (a = τ/√3 in the triplet's normalization).
Facts used throughout [D]: ρ_χ = K + V, p_χ = K − V with
K = (ṙ² + r²θ̇²)/2; w = −1/3 ⟺ V = 2K on the solution; the θ-shift
symmetry survives minimal coupling exactly, so the comoving charge
a³r²θ̇ = Q is conserved for every V(r), and q_χ = r²θ̇ = Q/a³.

## Verdict: the identification is CLOSED NEGATIVE — in every regime the charge is zero, decoupled, or tuned into the potential

**(1) Exact charged coasting does not exist for any V [D].**
r = const: K = Q²/(2a⁶r₀²) ∝ a⁻⁶ against constant V — never ∝ a⁻².
Power-law scaling r ∝ a^{−β}: the ṙ² half of K scales as a^{−2−2β}
(needs β = 0), the charge half Q²/(2a⁶r²) as a^{−6+2β} (needs
β = 2) — incompatible for Q ≠ 0. The family's only exact coasting
solution is the Q = 0 exponential tracker (μ = √(2κ), KG residual
exactly 0 — v14.959's solution, recovered), where the phase is
frozen and the charge is identically zero.

**(2) Generic charged data coasts only by decoupling the charge
[D asymptotics + numeric].** With the theory-fixed exponential V,
charged initial data is attracted to the tracker: numerical
integration (κ = 1, Q = 1 and Q = 50, modulus perturbed off-tracker)
gives ρτ² → 2.989, Hτ → 0.998, w → −0.3333 by τ = 3000 (control
on-tracker run sits at exactly 3, 1, −1/3). But the charge's energy
footprint (1/2)r²θ̇² ∝ a⁻⁶ (relative a⁻⁴) collapses — 10.4% →
5×10⁻¹² over the Q = 50 run — θ̇ → 0 (phase freezes), and
q_χ = Q/a³ dilutes against ρ ~ a⁻² (ratio ~ a⁻¹ → 0). The surviving
source is the chargeless tracker in spinor dress.

**(3) The charge-dominated branch is state-tuned [D].** The ansatz
r = c/a² makes the charge term ∝ a⁻², but the r-equation then forces
V linear with slope λ = Q²/c³ — the potential must know the state
(Q, c) in advance — and Friedmann's amplitude forces
3Q²/(2c²) = 1/κ: for fixed theory (λ, κ) the charge is pinned to
the single value Q* = (2/(3κ))^{3/4} λ^{−1/2}. Codimension-1 in the
state, and still only asymptotic: ρ carries an O(a⁻⁶) inexact piece
(2c²/(3a⁶)) from (1/2)ṙ². On this branch the modulus collapses to
the pair-space tip (r → 0); on the tracker branch it grows
logarithmically. Neither sits at a seat.

**Perturbations (frozen background, matter sector) [D]:** kinetic
term canonical, c_s² = 1, no ghosts on either branch. Phase-mode
mass² = V'(r)/r: exponential branch NEGATIVE (tachyonic) but mild —
|m²|/H² = 2μ/(κr(τ)) ~ 1/ln τ → 0, growth ~ e^{2√(ln τ)},
sub-power-law; radial mass² = V'' = μ²V > 0. Linear branch:
V'/r = λ/r > 0 with m²/H² = 3λa⁴/c → ∞ (heavy, healthy sign).

**Scope:** homogeneous configurations, minimal coupling, V = V(|χ|)
as deposited in v14.990. Inhomogeneous spinor configurations are
not tested; nonminimal or θ-dependent couplings lie outside the
deposited family and would break the shift symmetry that makes
q_χ a Noether charge at all. v14.990's positive result is untouched:
χ remains the healthy ℏℤ pair-side charge carrier. What closes is
only its identification with the k4 source. The Q = 0 sector still
needs its amplitude matching (V₀e^{−μB} = 2, the κC = 1 species).
G not derived. Suzuki weld parked.

**Payload:** spinor_source.py (regimes 1, 3, perturbation masses),
integrate.py (regime 2 numerics), this NOTE.
