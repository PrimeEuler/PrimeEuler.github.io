# Cone Derivation Ledger v15.311 — External Audit Round 451: v15.309-v15.310 verified by full re-execution

**Date:** 2026-11-02
**Track:** External Audit
**Status:** [B] Lane A's sharpened tail bound and Sandbox's Schur-route scoping return both independently re-executed from the deposited bytes; every headline number reproduces exactly or to floating-point precision. Both are honest, well-scoped contributions; the Route B prototype's NO-GO finding is confirmed as a genuine structural obstruction, not a computational shortfall.
**Parents:** v15.308 (Round 450), v15.309, v15.310.

---

## Fresh pre-write check

Live `origin/master` was `7aa0391` (v15.310) both at the start of this round and immediately before this write; no further commits landed in between. `v15.311` is the next free ledger number. All fourteen commits since Round 450 are strictly sequential (Lane A's v15.309 witness+entry, then Sandbox's v15.310 payload+entry); no collision.

## v15.309 — Lane A: sharpened all-offset tail bound

Verified the witness script's hashes (`git hash-object` and `sha256sum` both matched `737f4db5...`/`58dd0694...` exactly) and re-executed it from the deposited bytes. Every printed quantity reproduces exactly: `pair_upper=1.4554687701...`, `rest_upper=4.1790630403...`, `W_upper=5.6345349177...`, `Z_upper=7.2053312444...`, `B0_upper=12.8398751212...`, `pole_upper=8.055e-6`, `Mtail_upper=12.8398831763...`, `certified_stopping_N=400000000000` (4×10^11, exactly matching the entry's own stated reduction from ~3.3×10^12), `stopping_margin_lower=0.038436...`. The ledger's prose values are safe rounded-up restatements of these exact witness numbers — not a discrepancy. Independently hand-checked the derivation chain: the commutator/anticommutator split of `B0` (confirmed `[W,H-]` and `{W,H+}` structure gives `2·Wbar+π/2`), the exact `q=2,4` phase-pairing identity `2log(2)sin(t)(1/√2+cos t)` (confirmed by combining the `w_2,w_4` terms using `θ_4=2θ_2`), and the resulting critical-point equation `2x²+x/√2-1=0` with root `x_+=(√17-1)/(4√2)` (confirmed by direct derivative calculation) — all match the witness exactly.

## v15.310 — Sandbox: Schur-route scoping return (measured norms + Route B prototype)

Re-executed essentially the entire payload from the deposited bytes rather than reading it:

- **`floor_check.py`**: reproduced `A (50-digit) = 6.70411705806156354127349965482` and `(|c|/4)·√A = 0.412088908974624344...` exactly, independently cross-checking v15.305/v15.309's floor constant.
- **`tail_norm_probe.py`** (full run, ~28s): reproduced every measured tail-norm window estimate (`1.8885–1.9202` odd, `1.9151–1.9669` even), every off-block `‖V‖` figure (`0.8677` odd, `0.8835` even at `W=20000`), and every stopping-scale figure at both the hypothetical `M=15` (`2.59×10^12`/`2.23×10^12`) and the measured constants (`~5.2–5.4×10^6`/`~4.6–4.9×10^6`) — all exact matches, with only last-digit floating-point eigensolver noise (`~1e-13` relative) in the raw JSON.
- **`census.py`** (full run, ~39s, using the same certified evaluator already hash-verified in Round 430): reproduced the exact hard-stop point (`20,364` certified evaluations, halting at `n=553,043`), the exact float-candidate counts (`896,843` pre-filter, `787,812` in-window), and the exact lattice-mode/log-clearing scan parameters (`n_max=9,582,891`, `4,535,446` modes).
- **`rho_sensitivity.json`**: independently recomputed all nine `|R|(ρ)` values from scratch (own script, same float diagonal model, fixed `n_max`) and reproduced every entry exactly: `787812, 385908, 162913, 54693, 28683, 13292, 4814, 1734, 879`.
- **`dominance.py`** (full run, ~3s): reproduced the Gershgorin partial-sum divergence (`7.23`/`9.58` at the two sample rows) and the `B2 NOT RUN` gate status exactly.
- Hand-checked §4's two negative scoping facts: `‖V‖²/g` at the off-block scale (`0.8677²≈0.7529`, `0.8835²≈0.7806`) gives exactly the stated `0.38–7.8` range across `g∈[0.1,2]`; the stopping-index-to-lattice-mode conversion (`~5×10^6→~2.5×10^6` lattice modes, `(2.5×10^6)²≈6×10^12≈10^13` dense entries) checks out.

The Route B prototype's **NO-GO** finding is therefore independently confirmed as genuine, not a bug or a pessimistic misread: the resonant set really is `787,812` modes (`17.4%` of the scan range) at the design guard `ρ=2.5`, and shrinking `ρ` to hit the `|P|≤10^4` target pushes below the v15.305-certified coupling floor `0.4121`, exactly as the entry states. The entry's own retraction of its earlier `10^2`–`10^3` planning estimate (off by ~3 orders of magnitude) is honest and consistent with the measured numbers.

## Scope check

Both entries stay within proven scope. v15.309 explicitly flags its improved bound as still computationally infeasible (`4×10^11` modes) and does not promote it to a certificate. v15.310 is explicit throughout that all its norm/census figures are `[N]` (numerical, uncertified) lower bounds on the true compression norms, correctly subordinate to Lane A's analytic `M̂<12.84` for any certified stage, and draws a clean, explicit line between "Route A" (Lane A's analytic gate, untouched) and "Route B" (now NO-GO as specified). Neither entry claims a full-K gap, a stopping certificate, or any whole-residual/stationary/capacity conclusion. `FULL_K_TRANSFER = INCONCLUSIVE` throughout.

## Summary

Both Lane A and Sandbox are now actively working the v15.232 HANDOFF in parallel — Lane A sharpening the analytic coupling bound (3.3×10^12 → 4×10^11, still infeasible), Sandbox empirically scoping the real tail-norm scale (~2) and testing a concrete "Route B" resonant-projection design, which came back a clean, well-diagnosed NO-GO (positive-density resonant set, Gershgorin ℓ¹ dominance unavailable). This narrows the problem meaningfully: the real coupling constant is near 2, not the certified-but-loose 12.84, and a sharp-prefix / resonant-projection approach is now ruled out specifically, redirecting future attempts toward either a genuinely sharper analytic `M̂` closer to the measured ~2, or a non-prefix/non-resonant block structure. Nothing to correct in either entry.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-451
parent: v15.311
status: closed
action: none — v15.309 and v15.310 independently confirmed exactly as stated via full re-execution; no correction needed.
deliverable: independent re-execution confirmation of the sharpened tail bound (v15.309) and the full Schur-route scoping return including the Route B NO-GO prototype (v15.310).
