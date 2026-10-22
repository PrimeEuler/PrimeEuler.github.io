# Cone Derivation Ledger v14.710 — Sandbox return (v14.708 HANDOFF): the hot-limit drift coefficients derived from the v3.4 collision operator — (3q²−1) is derived twice over, not protected; no Ξ alteration

**Timestamp:** 2026-10-22 (EDT)
**Lane:** Sandbox (little Euler)
**Parents:** v14.708 (gravity lane: bath/phase coordinate gate; its HANDOFF to sandbox — derive the hot-limit drift coefficients from the deposited EFT v3.4's bath/collision operator without a hand-fit fixed point, test physically motivated perturbations of distribution and coefficients, and check whether any independently derived interaction alters the rank-1/rank-2 Ξ response beyond standard gradiometry — is what this entry answers and closes). Also v14.705 (the expansion that first carried the fixed point), v14.707/v14.709 (the v3.4 deposit and corpus record).
**Status:** HANDOFF-ACK return under the standing sandbox authorization and the 2026-10-18 waiting-lane extension. Producer re-run clean from the deposited file at deposit time. No far-tail/Suzuki object, paper, or certified object touched; no measured G inserted.

## 1. The coefficients are derived, not fit [D]

Starting from v3.4's own generator data in the hot limit (isotropic velocity diffusion, per-component kick variance rate 2D₀): energy drift A_h = 3D₀, covariances C_hh = 2D₀v², C_hL = 2D₀L, and the angular-momentum drift A_L = D₀r²/L (the Itô curvature of L = |**r**×**v**| — the term the draft's abstract names). Applying the generator to the jump-safe shape coordinate s = 1 − q and inserting the exact Kepler time averages ⟨v²⟩ = μ/T, ⟨r²⟩ = (T²/2)(5 − 3q²), with L² = μTq² and h = −μ/(2T), assembles **symbolically and exactly** to the draft's boxed result,

\[
\langle\mathcal Ls\rangle = \frac{5D_0T}{2\mu q}\,(3q^2-1),\qquad q_0^2=\tfrac13,\quad e_0^2=\tfrac23 .
\]

**Attribution** (numerator 15q² − 5, in units of T/(2μq²)): the energy drift + cross-covariance channel contributes **+10q²**; the energy Itô term (½C_hh s_hh through ⟨v²⟩) **+2q²**; the L-curvature channel (s_L A_L through ⟨r²⟩) **−5 + 3q²**. So the "−1" of (3q²−1) comes entirely from the constant part of ⟨r²⟩ flowing through the L-curvature drift, and the "3" is the mixed total (10+2+3)/5 — a channel balance, each channel fixed by the bath operator, none chosen to place the zero.

**Second, independent route [D]:** Hamilton & Modak's encounter-theory coefficients A_ε = C(1−2ε), D_ε = 2Cε(1−ε) (ε = e²), carried through Itô's formula to s = 1 − √(1−ε), give A_s = (C/4q)(3q²−1) symbolically; identifying C = (5T/3μ)·⟨|Δ**v**|²⟩/Δt = 10D₀T/μ makes the **absolute** coefficient identical to the generator route. Two derivations that share no algebra agree on the polynomial and its normalization — the fixed point is a theorem of the stated bath model, not a fit.

## 2. The value is not protected [D/N]

Concurring with v14.708's general-drift observation (q̇ = −C(aq²−b)/q selects e² = 1 − b/a) and localizing it in the channels: weighting the generator's channels — the reproducible stand-in for changing the bath's distribution, which redistributes exactly these channel strengths — moves the zero **continuously**: L-channel ×1.5 → q² = 5/11 (e² = 0.5455); L-channel ×0.5 → q² = 5/27 (e² = 0.8148); energy channels ×1.25 → q² = 5/18 (e² = 0.7222). The draft's own physical perturbations point the same way [N, as reported in v3.4]: restoring finite temperature moves the zero along the drift-zero curve F_s(q,Θ) = 0 until it annihilates at the fold (q_c, Θ_c) = (0.59618619, 0.32464127), and the draft's planar sector has a different response structure outright. **Verdict on the fixed point: exactly derived within the Maxwellian hot limit; a property of that bath's channel balance; not forced by, and not protected by, cone geometry.** This is the precise content of v14.705's "template, not a fundamental constant," now shown at the coefficient level.

## 3. Ξ alteration test [D, negative]

The bath drift is a stochastic process on a Kepler orbit's (h, L) statistics. Ξ (v14.700) is the *static* rank-1/rank-2 response of a rotor to an external field's Φ′(R), Φ″(R) — the coefficients β₁, β₂ are properties of the rotor–field coupling, not of any orbital relaxation process. No term derived from the bath operator enters β₁ or β₂; the objects are disjoint. The only physical bridge — a source mass granular enough for its own encounters to matter — contributes *noise* to a Ξ measurement (already the regime of v14.702's error budget), not a correction to the mean response ratio. **No independently derived bath interaction alters the Ξ response beyond standard gradiometry.** Together with v14.708 (inserting the bath point into the phase Gram overlap generates no e-dependent Ξ correction), the bath↔response connection is closed from both sides: exact conditional algebra, no physical coupling.

## Verification

Producer `drift_coefficients.py` (symbolic assembly, attribution, Hamilton–Modak route, perturbation roots) runs clean end to end; payload `research-notes/payloads/sandbox_drift_coefficients_v14_710/` carries it with `RESULTS.md` and `MANIFEST.sha256`.

## Scope flags (honest)

`closes_sandbox_handoff_of = v14.708`; `answers_lane_a_handoff = false`; `far_tail_touched = false`; `papers_modified = false`; `G_derived = false`; `drift_coefficients = DERIVED_TWICE (generator + Hamilton-Modak, absolute agreement)`; `fixed_point_protected = false (channel-balance property of the Maxwellian hot limit)`; `xi_alteration_by_bath = NONE [negative]`.

## Disposition

The v14.708 sandbox handoff is **closed**. Open from v14.708: its audit handoff (coordinate-distinction verification; whether the archive bath's e and the phase family's e are the same geometrical object or a notational correspondence; source-level check of the fixed-point coefficients — the sandbox's §1 above is offered as input to that check). The far gate (v14.585 actions 3–4) continues independently.
