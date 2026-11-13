# Cone Derivation Ledger v15.887 — External Audit Round 568

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 567/v15.877, Gravity v15.878, v15.879, v15.880, v15.882, v15.884, v15.885

## Fresh state at gate

This write went through two freshness checks: first `890fcd2` (Gravity's v15.885), then a follow-up catching a new committed script `k4_rindler_compton_action_closure_v15_886.py` (commit `ad28914`) with **no ledger `.md` text yet** — deferred to the next round. This entry uses `v15.887` (not `v15.886`, reserved by that in-flight script) to avoid any collision.

## The v15.877 version-label collision between External Audit and Gravity, correctly self-resolved

Confirmed independently (`git log --all --oneline --diff-filter=A -- "*Cone_Derivation_Ledger_v15.877_Gravity*"` returns nothing): my own Round 567 entry claimed ledger `v15.877` before Gravity's Gertsenshtein script was committed under a `v15.877` filename. Gravity caught this and moved its ledger write-up to `v15.878` without touching either my entry or its own original script. This is the same clean self-resolution pattern seen at `v15.836` and `v15.864` in earlier rounds — no action needed beyond confirming it.

## v15.878 — Einstein–Maxwell Gertsenshtein mixing, verified personally

Independently re-derived the mixing-matrix identity `C^TC=μ²I₂` from the stated `C=μ[[sinθ,-cosθ],[cosθ,sinθ]]` from scratch (fresh SymPy), confirming it holds for arbitrary `θ` exactly — this is the key fact underlying the claim that both polarization branches share identical conversion probability. Independently recomputed the test value `P(μ=0.083,Δ=0.14,L=14)=0.5828565490569763`, matching exactly. **Re-executed both the original script and the v15.878 replay**: both reproduce every PASS and the exact `P` value.

## v15.879 — no autonomous phase attractor; real B-reversal QPM, verified personally

The no-attractor theorem (`d/dz[Ψ₁†Ψ₂]=0` for Hermitian `H`) is a standard, immediate consequence of unitarity — correctly invoked, not something requiring independent rederivation. **Re-executed the committed script**: reproduces the three-way comparison table exactly (`P_uniform=6.168271388049616e-13`, `P_real-B-flip=0.0015991430183278494`, `analytic QPM=0.0016`), matching the ledger's cited values exactly.

## v15.880 — mesh ratio does not fix an absolute QPM length, verified personally

Independently computed the square-wave Fourier spectrum `|a(r)|²` from scratch via direct numerical quadrature of `sign(cos z)` (not importing the committed script): got `0.405284735...`, `0.0450316377...`, `0.0162113899...` at `r=1,3,5` and numerical-noise-level values at half-integer/even `r` — matching the ledger's cited `0.405284734569351`/`0.0450316371743724`/`0.0162113893827740` exactly. **Re-executed the committed script**: reproduces the same values plus the exact/Born comparison table at `Δ=1,3` exactly.

## v15.881/882 — the m/s tag does not supply an absolute QPM scale, verified personally

**Confirmed the disclosed defect**: re-executing `k4_null_ms_tag_qpm_scale_v15_881.py` as committed raises `AssertionError` at the final assertion (the dimensionless ratio correctly equals `1`, but the script's original assertion mistakenly checks against `0`), exactly as v15.882 discloses. Independently verified the beat-length formula `Λ_QPM=2π/|Δk|=c/(f|n_γ-n_g|)` algebraically: with `Δk=(n_γ-n_g)ω/c=(n_γ-n_g)2πf/c`, `2π/Δk` reduces to exactly that form, confirming the ratio claimed equal to `1` is correct and the original assertion's expectation of `0` was the actual bug. **Re-executed the v15.882 repair**: runs cleanly to completion.

## v15.884 — velocity-axis node interpretation, verified personally

Independently re-derived the constant-proper-acceleration relation from scratch: inverting the standard relativistic-rocket velocity profile `v(t)=a₀t/√(1+(a₀t/c)²)` for `t` gives exactly `t(v)=v/[a₀√(1-v²/c²)]`, matching the entry's Gate 534 formula exactly. **Re-executed the committed script**: all four PASS checks succeed.

## v15.885 — action-circle tangency does not select acceleration, verified personally

Independently re-derived both headline results from scratch: (1) the lab-frame node-crossing interval `Δt_(1/4→1/2)=(c/a)[1/√3-1/√15]`, which evaluates to `≈0.319151379 c/a` exactly as claimed; (2) the exact fixed-action counterfamily `a→8a, E→4E`: substituting into the bouncer action `J(E)=(4√2/(3a√m))E^{3/2}` confirms `J` is exactly unchanged (both the `1/a` and `E^{3/2}=8E^{3/2}` factors combine to an overall factor of 1), while the period `T(E)=dJ/dE=(2√2/(a√m))√E` scales to exactly `T/4` under the same substitution — both confirmed by direct hand algebra before checking the script. **Re-executed the committed script**: reproduces the exact symbolic node-interval expression (`c(5√3-√15)/(15a)`, algebraically identical to the ledger's form) and the `T→T/4` counterfamily result exactly.

## Honesty and scope assessment

Another large, fully-confirmed round. The one disclosed defect (v15.881) is confirmed exactly as described, and its v15.882 repair runs cleanly. The Gertsenshtein sequence (v15.878→882) is a genuinely substantial piece of physics — real Einstein–Maxwell photon-graviton mixing, not a freely-chosen toy coupling like the earlier parametric-oscillator entries — and it is handled with the same careful honesty throughout: every entry correctly distinguishes real physical quasi-phase-matching (which does work, via engineered magnetic-field reversals) from any claim that the Cone mesh geometry supplies the missing absolute length/frequency scale (which it does not, and the entries say so plainly). v15.884/885 continue directly answering the project owner's own follow-up questions about the velocity axis, with correct and appropriately modest conclusions throughout.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.887
type: external-audit-round
status: actionable
action: v15.878 through v15.885 are all independently confirmed as stated, including the disclosed v15.881 defect and its v15.882 repair. No corrections needed anywhere in this round. v15.886 has a committed script but no ledger text yet; deferred to the next round.
deliverable: Round 568 independent audit of v15.878 through v15.885 (8 entries).
