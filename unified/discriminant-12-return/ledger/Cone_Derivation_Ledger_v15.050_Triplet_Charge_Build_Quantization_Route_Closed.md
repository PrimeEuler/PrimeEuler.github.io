# Cone Derivation Ledger v15.050 — The Triplet-Charge Build: Rotating Labels, the B Fork, and the Quantization Route Closed (Sandbox Return)

**Entry ID:** v15.050 (sandbox return; lane-request mode)
**Date:** 2026-10-28
**Author:** Sandbox (little Euler)
**Parents:** v15.048 (composite-triplet test, route closed; park sharpened to "slave an action coefficient"), v14.731 (the dyon quarter — the record's one coefficient derived via charge quantization), v14.989/v14.992 (the AM triplet source), v14.996 (SVT certificate, static labels).
**Payload:** `payloads/triplet_charge_build_v15_050/` — `NOTE.md`, `triplet_charge.py` (sympy reproducer).

## Question

The Wald/Noether discussion isolated one loophole in the charge framework: charges measure coefficient × state and never derive a coefficient — *except* under a quantization or periodicity condition, the mechanism that derived the quarter at v14.731. This build constructs the configuration that loophole requires for the triplet — rotating labels φ^I(t, z) = R^I_J(ωt) z^J on the coasting background — and tests whether a quantization condition on its internal Noether charge can pin κC.

## Results

1. **Building the configuration forces a fork the record never needed** (all deposited labels are time-independent): (R1) B = spatial strain a⁻²FF^T, the reading of the deposited work (F = deformation gradient, v14.989); (R2) B = full spacetime contraction. [D]
2. **(R1) The rotation is invisible and chargeless.** B = a⁻²I exactly; A_B = 1/a²; the background stress-energy is unchanged (a degenerate background class). The internal-rotation Noether charge density is **exactly zero**: W contains no φ̇, so the canonical momentum vanishes and J^t ≡ 0. The rotation is a flat direction with a spatial flux and no charge — nothing to quantize. [D, sympy-verified]
3. **(R2) The charge exists but is a moment, hence state-laden.** A_B = 1/a² − ω²((z¹)² + (z²)²)/3 (matched normalization); charge density q₃ = (2C/3)ω((z¹)² + (z²)²) ∝ C but weighted by squared distance to the axis; total over a ball ~ C·ω·R⁵. ω and R are state data; the homogeneous cosmology has no finite total. Quantization would pin C × state, not C. [D, sympy-verified]
4. **No finite carrier exists in the action as deposited.** Derrick scaling E(λ) = λE(1) is monotone; W has no potential term (no Q-ball); a cut-out lump is the medium, not a soliton. [D scaling]
5. **Checklist against the one success.** The quarter was pinned because Taub–NUT supplies (i) a finite total charge, (ii) a period fixed by regularity (Misner 8πn) making the conjugate angle compact with fixed range, (iii) a charge isolating the coefficient at the self-dual point. The triplet fails all three: zero/extensive charge, no periodic direction, state data surviving. [I as criterion, abstracted from v14.731]

## Verdict

**The quantization route is CLOSED NEGATIVE for the triplet action as deposited.** Instantiating it requires adding structure (a potential, a compact label direction, a solitonic carrier) — new chosen constants, the species a derivation was meant to avoid. With v15.048 (compositeness: category failure) and the background-charge analysis (Komar/Wald charges vanish or merely measure on this background), all three mechanism species for deriving κC are now closed with exact obstructions. The park specification is complete: a future mechanism must arrive carrying a finite system, a regularity-fixed period, and a charge that isolates the coefficient. κC = 1 remains a matching; `G_derived = false`; the Suzuki quarter remains PARKED (v14.916).

## By-products

- **The B fork**, invisible on every deposited (static-label) background, decides time-dependent-label physics; R1 is the reading consistent with the deposited F/strain usage. Flagged for the gravity lane; no deposited result is affected.
- Under R1 the rotating-label background is stress-energy-degenerate with the static one but is a **different background for perturbations**: the v14.996 SVT certificate covers static labels only. Flagged, not computed.

## Handoff

To the gravity lane: the B-fork disambiguation and the rotating-label perturbation caveat, for whenever time-dependent labels enter their program. To Lane A / Audit: verification of the charge computations as desired; the three-route classification is offered as the door's closing summary. Production thresholds and charges remain unspent; the far/K_full gate is untouched.
