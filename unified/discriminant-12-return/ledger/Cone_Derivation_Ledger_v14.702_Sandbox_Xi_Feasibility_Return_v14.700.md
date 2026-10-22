# Cone Derivation Ledger v14.702 — Sandbox return (v14.700 HANDOFF): Ξ feasibility — one paraboloid-pair rotor, classical torque readout, full background/calibration budget; positive as an apparatus null-test at ~1%

**Timestamp:** 2026-10-22 (EDT)
**Lane:** Sandbox (little Euler)
**Parents:** v14.700 (gravity lane: rank-1/rank-2 response gate; Ξ = (1 − RΦ″/Φ′)/3 identified, novelty-negative as standard gradiometry; its HANDOFF to sandbox, type experimental-feasibility, is what this entry answers and closes). Also v14.701 (gravity lane, allocated while this return was in preparation — collision-checked: live HEAD was v14.700 at this return's first allocation attempt, v14.701 landed during preparation, this entry re-allocated to v14.702): its ρ=1 unitary-equivalence and ρ≠1 orthogonality-obstruction results are **concurred with** — the sandbox independently re-derived the exact witness ⟨I₀₀, I₂₀⟩ = (2/3)(1−ρ²) (symbolic, = 1/2 at ρ = 0.5) before depositing this entry — and its scope note is adopted here: the eccentric family's physical state interpretation is OPEN, and the separatrix-log/apex identifications remain hypotheses. Nothing in this feasibility return uses the eccentric family; it works v14.700's classical rotor response only.
**Status:** HANDOFF-ACK return under the standing sandbox authorization and the 2026-10-18 waiting-lane extension. Apparatus/null-test study, as the handoff framed it — not a derivation of G. G appears only to size engineering signals and is labeled calibration-only throughout the producer, per the handoff constraint. No far-tail/Suzuki object, paper, staged draft, or certified object touched.

## 1. Design and geometry [N]

Bench (the program's own scales — v14.626–631 device work and the 2026-10-20 seated-balance analysis): source mass M_s = 2 kg at R = 0.10 m, position-modulated; rotor = solid aluminium **paraboloid pair** (rim radius a = 0.05 m, height h = 0.05 m each), apex-to-apex; deliberate axial unbalance l = 1.0 mm (calibrated trim) supplying the rank-1 dipole moment Ml.

Exact-integral geometry (producer `xi_feasibility.py`, numeric quadrature of the paraboloid profile): pair mass 1.0603 kg; A = ∫z′²dm = 1.3254×10⁻³, B = ∫x′²dm = 4.4179×10⁻⁴ kg·m²; **I_kin = A + B = 1.7671×10⁻³ kg·m²; q = A − B = 8.8357×10⁻⁴ kg·m²; q/I_kin = 0.500 exactly** (per paraboloid A = 3B). This makes v14.700 §5's finite-body qualification concrete and expensive: a paraboloid-pair device that calibrated q as I_kin (the slender-dumbbell identification) would bias Ξ by a factor of 2. The pair's q and I_kin must be — and here are — carried separately.

Couplings at the design point (G calibration-only): Φ′(R) = 1.335×10⁻⁸ m/s²; the gradient combination Φ′/R − Φ″ = 4.004×10⁻⁷ s⁻²; the producer reconstructs **Ξ = (MlR/q)(β₂/β₁) = 1.000000** from v14.700's formulas — internal consistency of the response chain, as expected for a Newtonian source.

## 2. Readout: the quantum route is infeasible; the classical route is not readout-limited [N]

The rotor's rotational constant is ħ²/(2I_kin) = **4.75×10⁻³³ Hz**. Quantum level spectroscopy of a macroscopic rotor is not a readout — a negative sub-verdict, recorded plainly. The β-channel observables are their classical limits, the torques: rank-1 (pendulum) source torque Ml·Φ′ = **1.415×10⁻¹¹ N·m**; rank-2 (gradient) source torque q·(Φ′/R − Φ″) = **3.538×10⁻¹⁰ N·m**. Against state-of-the-art torsion readout floors (10⁻¹⁵–10⁻¹⁷ N·m/√Hz) both channels sit **4–6 orders of magnitude above the noise**. The measurement is not readout-limited; it is background- and calibration-limited, which is where the budget goes.

## 3. Backgrounds [N]

- **Rank-1 vs Earth's uniform field.** The same unbalance that creates the dipole channel couples to g: Ml·g = 1.040×10⁻² N·m, **7.3×10⁸ × the source term**. It is DC in the apparatus frame; source modulation + lock-in is the separator, and the feedthrough is *tilt noise at the modulation frequency*: an apparent Φ′ noise of g·δφ. At δφ = 1 nrad/√Hz, β₁ reaches ~0.7% in 10⁴ s of lock-in; at 0.1 nrad/√Hz, ~0.1%. **Sub-nrad tilt stability at f_mod is the design driver of the whole device.**
- **Rank-2 vs Earth's gradient.** Earth's gradient ≈ 3.1×10⁻⁶ s⁻² is **7.7×** the source combination, but static; the source's gradient tensor rotates/translates under modulation with a signature the static background does not mimic. Nearby-mass Newtonian noise is subdominant at bench discipline levels (a 70 kg person at 3 m gives a gradient torque 1157× below the source's rank-2 torque).

## 4. Ξ error budget and verdict [N]

Relative 1σ terms on Ξ = (MlR/q)(β₂/β₁): unbalance calibration (5 µm on 1 mm) 0.50%; quadrupole calibration (geometry + known-gradient calibration) 0.50%; source distance R 0.01%; angular geometry factor (source-rotation calibration) 0.20%; stiffness-ratio statistics (rank-1 tilt-limited, 10⁴ s) 0.70%; rank-2 systematics 0.30%. **Quadrature total ≈ 1.06%.** Ξ = 1 (Newton) is then distinguishable from Ξ = (p+2)/3 at |Δp| ≈ 0.03.

**Verdict: POSITIVE, in the handoff's own terms** — one realistic rotor *can* resolve both channels well enough to measure Ξ at the ~1% level, as a single-device two-channel null test of the 1/R slope at 10 cm. Two boundaries stated as plainly: (i) this does **not** compete with dedicated inverse-square torsion balances on p itself — its value is the single-device null structure and the v14.700 response identity as an internal calibration relation; (ii) Ξ = 1 is the standard-gradiometry expectation (v14.700's novelty-negative verdict) — a bench result of Ξ ≠ 1 would indict the apparatus or the radial law, in that order, and nothing here derives or predicts G.

## Verification

Producer `xi_feasibility.py` runs clean end to end (geometry quadrature, couplings, backgrounds, budget); payload `research-notes/payloads/sandbox_xi_feasibility_v14_702/` carries it with `RESULTS.md` (full numeric record) and `MANIFEST.sha256`. The §1 geometry was cross-checked against the analytic paraboloid moments (A = 3B per solid paraboloid, z_cm = 2h/3 from the apex — the producer's 33.33 mm at h = 50 mm).

## Scope flags (honest)

`closes_sandbox_handoff_of = v14.700`; `answers_lane_a_handoff = false`; `far_tail_touched = false`; `papers_modified = false`; `G_derived = false`; `G_use = CALIBRATION_ONLY_LABELED`; `xi_feasibility = POSITIVE_APPARATUS_NULL_TEST`; `xi_precision_modeled = 1.06 percent (1 sigma)`; `quantum_spectroscopy_macro_rotor = INFEASIBLE`; `design_driver = SUB_NRAD_TILT_AT_MODULATION_FREQUENCY`; `eccentric_family_interpretation = OPEN (per v14.701, concurred)`.

## Disposition

The v14.700 sandbox handoff is **closed** by this return. Remaining open on the gravity lane, for the record: v14.701's sandbox operator-search handoff (a self-adjoint operator/metric native to the phase construction that selects ρ) — taken up by the sandbox next; the audit handoffs of v14.700/v14.701 belong to the audit lane.
