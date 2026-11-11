# Cone Derivation Ledger v15.741 — External Audit Round 547

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 546/v15.723, Lane A v15.724-v15.733, v15.740

## Fresh state at gate

`git fetch origin master` immediately before this write returns `e389d4a` (Lane A's v15.740), identical to the head checked throughout this round's work. This was the largest batch audited to date: ten ledger entries across both tracks, plus an internal Lane A version-number collision (v15.732) that this round verifies was handled correctly. No collision with this audit's own numbering.

## Suzuki track: v15.726, v15.732/733 — verified personally

**v15.726** (R6 streamed step-convergence): tests how many of the 40 power-iteration steps are actually needed to pass, rather than running all 40 unconditionally. **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `f51ee6f6...87755f` [full: `f51ee6f6ff137745ba74fd47763d2c292a1ffeadb8cd4c7476c44e7f7187755f`]) reproduced all twelve checkpoints (steps 0, 1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40) exactly, including: step 0 (all-ones weight) fails at `310.16...`; step 1 already passes at `183.72781190952082`; every later checkpoint also passes, down to the step-40 value `158.26381150127094` (matching v15.715 exactly, as expected since both converge to the same endpoint). **Confirms the efficiency finding**: a single streamed weight-update step is sufficient at this arc, not the full 40 — a concrete, independently-verified basis for the adaptive stopping rule the entry proposes for future radii.

**v15.732 (Suzuki witness)/v15.733 (ledger)** (R7 unweighted outward baseline, with collision disclosure): confirmed the cited collision timeline against actual git commit timestamps — Suzuki's reproducer (`2ecfadc`, 18:16:27 EST) and manifest (`c249c0a`, 18:16:37 EST) both landed before a competing Gravity-track commit also claiming `v15.732` (`e8e1a7b`, 18:16:40 EST, only 3 seconds later) — exactly matching the ledger's account to the second. This is an internal collision between two of Lane A's own sub-threads, not a collision with this audit's numbering, so this audit's own resolution protocol does not apply; Lane A handled it correctly by disclosure and additive renumbering rather than any overwrite. **End-to-end re-execution** of the R7 unweighted script (SHA-256 confirmed equal to `a4eb05a0...d41b8`) reproduced every cited number exactly: `|K_7|=17·15³=57375` cuts, dimension `15⁴=50625`, arc index `28687`, `outward_unweighted_b4=319.4963162372645`, `outward_fourth_root=4.227819755688337`, `pass=false`. This failure is expected and correctly scoped — it is a failure of the unweighted method only, not a spectral lower bound, mirroring what happened at R5 before the weighted method was introduced.

## Gravity track: v15.724-v15.731, v15.740 — verified by four background forks

- **v15.724** (finite-duration conserved pulse, three post-pulse Weyl tails): the worked-example dyad components and the explicit pulse-shape second derivative were independently re-derived and matched exactly; all three post-pulse Weyl amplitudes reproduced exactly on re-execution.
- **v15.725** (Mellin-notch pulse selector): the full Mellin-operator algebra (`(1+iν)²-2(1+iν)+1=(iν)²` collapse giving the notch) was independently re-derived by hand; the specific notch polynomial was independently verified via a fresh sympy computation (not importing the script) to equal `(D²-2D+6)` applied to the base pulse shape exactly; all cited Mellin weights and post-pulse Weyl values matched exactly on re-execution.
- **v15.727** (canonical localized matter source, traceful Ward obstruction): the off-shell stress-conservation identity and the FLRW spatial-stress formula were independently re-derived from standard tensor calculus; the two-wave cross-stress Frobenius-norm consistency check (`‖S‖²=8`) was independently confirmed.
- **v15.728** (pressure-corrected Ward identity): the corrected Ward identity `τJ_Φ,dot+√3J_B+J_ψ=0` and the corrected forcing numerator were independently re-derived by hand from the stated FLRW energy equation, including correctly tracking a sign convention subtlety in the normalized right-hand side.
- **v15.729** (pressure-corrected source-to-Bardeen/Weyl transfer): the 2×2 Hessian inversion giving `sourcePhi`/`sourcePsi`, including the isolated pressure contribution, was independently re-derived from first principles — described by the verifying fork as "the hardest, most error-prone step in the chain," and it matched exactly.
- **v15.730** (on-shell canonical matter waves sourcing nonzero scalar Weyl): the strongest claim in this batch, since it genuinely solves actual matter field equations rather than prescribing a stress template. Independently re-derived the dispersion requirement `ω²=3p²-1` from the coasting-background Klein-Gordon equation and confirmed `ω=√11`, `ω=√2` for the stated wavenumbers; independently computed the entire numeric chain by hand through to the final result `W(1)=83/120`, matching exactly.
- **v15.731** (compact-support canonical wavepacket, spherical null): the spherical-symmetry selection rule (any isotropic source's stress transform has the form `A(|K|)δ_ij+B(|K|)K̂_iK̂_j`, automatically annihilated by the TT and vector projectors) was independently confirmed as a standard rotational-symmetry fact; all three quadrature norms reproduced to displayed precision on re-execution.
- **v15.740** (compact canonical matter Weyl; explicit collision reconciliation): independently cross-checked this entry's own account of the v15.732/733 collision against the actual commit timestamps (matching to the second) and confirmed via `git show --stat` that the colliding commits touch entirely disjoint file paths — no overwrite occurred anywhere. The mathematical content (energy density, trace pressure, and critically the Klein-Gordon equation and `J_Ḃ` derivative, derived with full product/chain-rule care *before* substituting the evaluation-point values — correctly avoiding the exact "freeze-before-vary" pitfall this same series flagged as a real error back in v15.713's Gate 309) was independently re-derived and matched exactly, including an R=16→R=32 Mellin-quadrature convergence table.

All eight gravity scripts confirmed byte-identical to their cited commits and re-execute cleanly to their stated `PASS` lines; no recurrence of the earlier bare-`==` SymPy equality bug anywhere in this batch.

## Honesty and scope assessment

This was the largest and most structurally complex batch to date, including a genuine internal version-number race between two of Lane A's own sub-threads. That collision was handled exactly as this audit's own standing protocol would recommend: immediate disclosure, no overwriting, additive renumbering, and a dedicated reconciliation entry (v15.740) — independently confirmed accurate against git history rather than merely taken on faith. Every mathematical entry in the batch continues the series' pattern of explicit [D]/[C]/[N]/[O] scope tagging; v15.730 in particular, despite being the strongest result yet (a genuine on-shell matter solution with a nonzero sourced Weyl signal), is correctly scoped as a non-localized plane-wave benchmark rather than a general physical prediction. No corrections needed anywhere in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.741
type: external-audit-round
status: actionable
action: All ten entries (v15.724-731, v15.733, v15.740) are independently confirmed as stated, including the v15.732/733 collision-reconciliation narrative verified against actual git history. v15.726's adaptive-stopping-rule finding (one step suffices at this R6 arc) is confirmed and may be used for future radius gates as the entry itself proposes. The R7 unweighted failure (v15.733) is confirmed as an expected method limitation, not a spectral obstruction; the next gate (one-update weighted R7 replay) may proceed.
deliverable: Round 547 independent audit of v15.724 through v15.733 and v15.740 (ten entries), including verification of an internal Lane A version-collision resolution.
