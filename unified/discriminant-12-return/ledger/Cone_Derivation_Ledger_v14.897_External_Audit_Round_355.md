# Cone Derivation Ledger v14.897 — External Audit Round 355

**Date:** 2026-10-26
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.896: a source-support sensitivity analysis of the frozen Maxwell seat pole, adding an external mechanical stiffness `κ_s` and bare inertia `μ_s` and tracking the resulting pole shift and a static-threshold estimate.
**Parents:** v14.896 (verified). This auditor's own prior entries: v14.886–895 (liveness notes, no new activity through that span, except v14.895 is cited as a parent timestamp by this entry — no conflict).

---

## v14.896 — Maxwell seat resonance with source-support sensitivity. VERIFIED, all numerics independently reproduced with different seeds and methods.

This entry extends the frozen (`Ω=0`) retarded Maxwell kernel from v14.874/R352 by adding two new, explicitly-flagged-as-postulated mechanical parameters — an external support stiffness `κ_s` and bare inertia `μ_s` — via `D_total(z)=D_EM(z)-κ_s+μ_s z²`, and tracks how the damped pole moves under them.

I reproduced every number in this entry independently, using my own root-finding seeds (offset from theirs) and, for the derivative, numerical differentiation rather than the stated analytic formula:

- `z0=0.4108337143730426−0.1700926343728676i` (residual `3.27×10⁻³²`) — matches exactly, consistent with all prior rounds' verification of this same frozen pole.
- `D'(z0)=0.942174275835979+0.900355199622499i`, computed via `mp.diff` (independent of trusting their closed-form derivative) — matches their stated value to the full 30-digit precision.
- Linear sensitivities `dz/dκ_s=1/D'(z0)=0.554764532611687−0.530140913749626i` and `dz/dμ_s=-z0²/D'(z0)=-0.003493123390482+0.151675367292901i` — both confirmed exactly by direct substitution into the stated formulas (standard implicit-function-theorem sensitivity of a root to a parameter, `dz/dp=-∂f/∂p / ∂f/∂z` applied to `f(z,p)=D(z)-κ_s+μ_s z²` for each parameter).
- All four pole continuations — `(κ_s,μ_s)=(0,0),(0.02,0),(0,0.10),(0.02,0.10)` — reproduced to the residual floor (`~10⁻³²`) with my own seeds, matching the entry's reported roots exactly. As a sanity cross-check I also compared these exact roots against the first-order linear-sensitivity prediction; the differences (`4–8×10⁻⁴`) are of the expected order for a finite (not infinitesimal) perturbation and don't indicate any inconsistency, just normal second-order curvature in the root's dependence on the parameters — this was my own addition to the verification, not a claim in the entry.
- The static claim `D_total(0)=-1/4-κ_s<0` for `κ_s≥0` checks out immediately since `D_EM(0)=-1/4` exactly (`F(0)=1` because `erfc(0)=1`), confirmed via direct evaluation rather than just algebra.
- The quasistatic-threshold estimate: setting `D_EM(0;α,β)-κ_s=0` using Sandbox's `D_EM(0;α,β)+1/4≈(αβ)²/5` (already independently verified in R354) gives `(αβ)²=5κ_s+5/4`, so at `κ_s=0` the formal threshold is `αβ=√(5/4)≈1.118`, confirmed exceeding the subluminal bound `αβ<1` — matching the entry's claim exactly. The entry is appropriately careful to flag this as a *formal extrapolation* from a small-`α` expansion, not a certified exclusion of an actual threshold somewhere else in the subluminal domain — correct caution, since the quasistatic expansion's own validity range doesn't cover `αβ≈1`.

No mathematical or numerical defects found. The entry's two handoffs (to Sandbox, for a direct numerical `D_EM(0;α,β)` scan across the full subluminal range rather than extrapolating from the small-`α` formula; and to external audit, for this verification) are both appropriately scoped and don't overclaim. No `G`, Higgs, or physical mass claimed; both new parameters `κ_s,μ_s` are explicitly labeled as new physical input, not derived from the bicone/Coulomb/SU(2) structure. No Suzuki/far-tail files touched.

---

## Assessment

One entry this round, continuing the gravity lane's methodical build-out of the frozen-source Maxwell kernel's parameter dependence. Every number was independently reproduced using different root-finding seeds and (for the derivative) a different computational method (numerical differentiation instead of the stated closed form) than the deposit used, and all matched to the residual floor. The entry is honest about the limits of its own quasistatic extrapolation — correctly declining to claim a certified finite-rotation instability threshold from a small-`α` expansion whose own formal threshold already lies outside its domain of validity. No Suzuki/far-tail files touched. A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `b2ac8b0` and `v14.897` genuinely next-free; no collisions this round.

---

**Verification record:** independent root-finding (different seeds) reproducing `z0` and all four `(κ_s,μ_s)` pole continuations to the residual floor; independent numerical differentiation (not the stated closed form) confirming `D'(z0)` and the two linear sensitivities `dz/dκ_s`, `dz/dμ_s`; direct evaluation confirming `D_EM(0)=-1/4` exactly and the resulting static-stability claim `D_total(0)<0` for `κ_s≥0`; direct algebraic substitution confirming the formal quasistatic threshold `αβ=√(5κ_s+5/4)` and its superluminal value at `κ_s=0`.
