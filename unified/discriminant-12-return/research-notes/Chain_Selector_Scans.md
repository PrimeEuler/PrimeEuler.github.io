# The chain-selector scans: no arithmetic selector for ψ_D

*Sandbox note (little Euler), 2026-10-19. Companion to v14.621
(the G ingredients assembled) and v14.626 (the rotor anatomy).
Target: ψ_D = ½ ln(Dirac) = 45.310004305. Hit window ±1.1×10⁻⁵
in ψ — the Dirac ratio's five meaningful figures (v14.616).
Producers: `chain_selector.py`, `em_steps.py`,
`regulator_chains.py`. Every scan declares its candidate set in
advance and carries its chance accounting. All results negative.*

## 1. Uniform chains (one repeated ratio) — negative

m·(½ ln r) vs ψ_D for r ∈ {(n+1)/n, n = 1..11} ∪ {p/1 : p ∈
{2,3,5,7,11}} ∪ {12/1}: no hit. Best: r = 4/3, m = 315, residual
7.8×10⁻⁵ — 7× outside the window, its implied ratio off by
1.6×10⁻⁴ (beyond G's own uncertainty, so physically excluded);
luck of that near-miss under the scan ≈ 2%. Expected chance hits
overall: 0.0034. Next best: (6/5)⁴⁹⁷ at 3.1×10⁻³. A single
repeated action does not select the chain.

## 2. EM steps — negative as numbers

(Jeremy's direction: the selector from EM.) Uniform chains on
−ln α (m = 9), −(½)ln α (m = 18), −ln α/(2π) (m = 58):
residuals 1.028, 1.028, 0.109. α-step repairs of (4/3)³¹⁵,
k·(−ln α) for k ∈ [−3, 3]: k = 0 stays best by four orders.
Pure α-power reading: ln α_G/ln α = 17.890344 — not an integer
(0.6% from 18; the classic Eddington near-miss zone).
Totient-restricted consecutive ladder (units of 12; block step
0.54800575): 83 blocks, residual 0.175. EM does not select
through α-sized steps or powers.

## 3. Prime chain of the nearest integer — exists, unselected

M₀ = 226866143917643529×10²¹ (nearest integer to the v14.616
central value) = 2²¹·3·5²¹·13·31·12537181·14967301. The 2²¹5²¹
is the decimal shift; the lead's largest prime is 14967301, i.e.
the "chain" contains two ~10⁷ prime steps (rapidity ≈ 8.2 each).
Lead smoothness is Dickman-chance (ρ(2.5) ≈ 13%). Recorded
methodological catch: a first attempt factored the float64
nearest the ratio and "found" 2⁸⁰ — the double's ulp, not
physics; redone on the exact decimal integer. Structural point:
G's uncertainty window holds ~10³⁵ integers; one integer's
factorisation is representation noise without a principle to
pick it.

## 4. Regulator orbits — negative

Each real quadratic channel field acts on its hyperbolas by its
fundamental unit ε_d; orbit step = regulator ln ε_d. Uniform
chains for d ∈ {5, 2, 3, 13, 21, 6} (steps 0.4812…2.2924):
residuals 0.076–0.54. Two-field mixes a·ln ε_{d₁} + b·ln ε_{d₂},
all 15 pairs, a,b ≤ 300: best 1.3×10⁻⁴ (85 ln φ + 5 ln(1+√2)),
3.4×10⁻⁴, 4.1×10⁻⁴ — all ≥ 12× outside the window, in-band
counts at generic Diophantine density.

## 5. Summary and the live reading [O]

Near-misses across all four constructions cluster at ~10⁻⁴, one
order above the window — the signature of chance density, not of
a mechanism approached. **The selector is not in the step
arithmetic**: not repetition, not α, not factorisation, not the
fields' own unit orbits. What EM actually contributed in this
project's one completed elimination (the α note) was not a
number but **selection rules** — a coupling whose Wigner factors
decide which transitions exist. The remaining form of the
hierarchy item is therefore a construction problem (specify the
coupling, as the parabolic dipole was specified for α), and its
natural arena is the rotor system of v14.626 — whose coupling,
computed there, also selects no finite chain (democratic
weights, Wallis × 2^{−J} climb). Both G items remain open;
`G_derived = false`.

## Scope

[I]/[O] sandbox note; exact scan outputs are [D] as computed.
No paper, staged draft, or certified object modified.
