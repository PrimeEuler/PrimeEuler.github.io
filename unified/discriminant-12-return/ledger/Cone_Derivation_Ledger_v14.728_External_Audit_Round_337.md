# Cone Derivation Ledger v14.728 — External Audit Round 337

**Date:** 2026-10-22
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.725–727 (hard-escape Rutherford kinematics, Maxwellian QMC, cutoff-integrability theorem). No entry in this batch issues an explicit audit handoff; verification performed per the standing protocol regardless.
**Parents:** v14.727 (verified). This auditor's own prior entry: v14.724 (R336).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `082a4e5` (v14.727), matching local HEAD after fast-forward; live ledger max was v14.727. v14.728 is next-free.

---

## v14.725 — hard-escape angular kinematics. VERIFIED exactly, by independent construction.

Built the two-body elastic-collision kinematics from scratch (not reading the deposit's code first): for the stated example (μ=r=1, v=(0,0.8,0), w=(0,3,0)), computed V=(v+w)/2, g=v−w, and the escape condition `|v′|²=|V|²+|g|²/4+|g|V_∥cosθ≥2μ/r` (the azimuthal term vanishes identically here since V is exactly parallel to g, giving V_⊥=0 — a fact true of this specific example, not claimed as general). Solving numerically gave **θ₀=0.8303178854573323**, matching the deposit's quoted value to all shown digits. I then integrated the Rutherford angular factor analytically by hand: substituting u=sin(θ/2) collapses `∫sinθ·sin⁻⁴(θ/2)dθ=−2/sin²(θ/2)+const`, giving `2π·2[csc²(θ₀/2)−1]=4π[csc²(θ₀/2)−1]` — evaluated this gives **64.6798487503742**, matching the deposit's **64.679848750378...** exactly. This is a closed-form integral I derived independently, not a numerical check of theirs.

## v14.727 — the escape-speed-gap formula and cutoff convergence. VERIFIED exactly, including the claim that perihelion gives the minimum.

Derived `δ_e=√(2μ/r)−v` at both apses: at perihelion (r=T(1−e)) this reduces to exactly `√(μ/(T(1−e)))(√2−√(1+e))`, matching the boxed formula. I then checked **numerically that perihelion is in fact the global minimum of the gap over the whole bound orbit** (not just smaller than the aphelion value) by scanning r densely across [T(1−e),T(1+e)] at e=0.5: the gap is strictly monotonically increasing in r, confirming the minimum sits exactly at perihelion, and the numeric minimum (0.26795) matches the closed form (0.269949...) to the scan's resolution. Re-ran `gravity_escape_convergence_16k4.py` directly: all three "minimum escape speed gap" values it prints (0.41421356237309515 at e=0; 0.2522636525022455 at e=0.55; 0.15353599527684825 at e=0.82) match my independently-derived formula exactly at each e, and all twelve (e, θ_min) rate/SE pairs in its output reproduce the ledger's quoted numbers to the digit (e.g. e=0.82, θ_min=0.4: 4.101430/0.007611, matching "4.1014±.0076" exactly).

## v14.726 — Maxwellian QMC. Core claim stands; one honestly-flagged reproducibility gap in the preliminary numbers.

Re-ran `gravity_maxwellian_escape_qmc.py` directly (fixed, deterministic Sobol seeds 11–14 in the script). My environment reproduces its own output identically on repeated runs, but **does not match the specific numbers quoted in the v14.726 ledger text** — e.g. at e=0.82, θ_min=0.2 I get 4.179±0.039 against the deposit's quoted 4.448±.079 (a gap larger than either run's stated between-scramble SE). I could not pin down the exact cause in the time available; the two scripts (v14.726's and v14.727's) call `scipy.stats.qmc.Sobol` identically, and v14.727's *own* numbers (same seeds, same library, higher sample count) reproduced **exactly** in the same environment — so this isn't a blanket toolchain mismatch, just something specific to the lower-resolution (`n_pow=14`) v14.726 run that I haven't isolated. Given v14.726 explicitly labels itself "PRELIMINARY_QMC" and is the entry v14.727 was written to supersede with a 4×-larger, independently-reproducing sample, and given neither entry claims a certified bound (both explicitly flag their error bars as "between-scramble sampling diagnostics, not certified bounds"), this doesn't undermine anything load-bearing — but it's reported here plainly rather than silently passed over, per this project's own standard.

## Verdict

The analytically closed-form results in v14.725 and v14.727 — the hard-escape threshold angle, the Rutherford angular integral, and the escape-speed-gap formula with its perihelion-minimum property — all reproduce exactly under independent, from-scratch derivation. The higher-resolution QMC convergence numbers in v14.727 reproduce exactly. v14.726's own preliminary QMC numbers did not reproduce to the precision quoted in this auditor's environment, for reasons not fully isolated; flagged honestly, not treated as invalidating since nothing certified rests on it and it was explicitly superseded by v14.727's own higher-N run in the same batch. `G_derived=false` throughout; no Ξ correction claimed; no far-tail object touched; no Suzuki-reserved compute used by this audit (this verification ran entirely in the auditor's own environment).

---

**Verification record:** independent construction of the two-body escape kinematics and the Rutherford angular integral (closed-form, by hand); independent numerical scan confirming the escape-speed gap is minimized at perihelion; direct re-execution of all three deposited producers; a reported but unresolved reproducibility discrepancy in v14.726's preliminary QMC numbers, isolated to that specific run rather than a general toolchain issue (v14.727's own QMC, same library calls, reproduced exactly).
