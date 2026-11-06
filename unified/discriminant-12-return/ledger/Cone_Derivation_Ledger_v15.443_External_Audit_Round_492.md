# Cone Derivation Ledger v15.443 — External Audit Round 492: v15.442 closes Round 491's open citation; ‖Q Hplus Q‖=pi/2 now fully rigorous in both directions

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's direct, elementary moment-Gram proof of `‖G_N‖<=pi` for every `N>=1` — closing exactly the one gap Round 491 flagged as "consistent with theory but not independently re-derived" — independently re-verified from scratch, including 200 fresh random exact-rational trials. The constant-Hankel tail norm is now `=pi/2` on both sides, rigorously.
**Parents:** v15.441 (Round 491), v15.442.

---

## Fresh pre-write check

`git fetch origin master` returns `0e4e8e7` (v15.442), identical to the head just read. `v15.443` is next free; no collisions.

## What changed

Round 491 confirmed the essential-norm lower bound `‖G_N‖>=pi` completely from scratch, but noted the matching upper bound `‖G_N‖<=pi` was only checked for plausibility against standard generalized-Hilbert-matrix theory, not independently re-derived — while also noting this didn't weaken the barrier conclusion, since the lower bound alone already suffices. v15.442 closes that gap directly, with a short, self-contained, elementary argument that needs nothing beyond the single most classical fact in this area (the `N=1` Hilbert inequality itself).

## Independent re-derivation of the proof, step by step

**Moment representation.** `G_N[j,k]=1/(j+k+N)=∫_0^1 t^{j+k+N-1}dt` — checked directly: `∫_0^1 t^p dt=1/(p+1)` with `p=j+k+N-1` gives `1/(j+k+N)`, exact.

**Positive semidefiniteness.** For any finitely-supported `x`, `<x,G_N x>=sum_{j,k}x_jx_k∫_0^1 t^{j+k+N-1}dt=∫_0^1 t^{N-1}(sum_j x_j t^j)^2 dt`. Since `t∈[0,1]` and `N>=1` give `t^{N-1}>=0`, and the square is `>=0`, the integral is `>=0` — `G_N` is PSD for every `N>=1`. I re-derived this by directly expanding the double sum and swapping sum/integral (justified for finitely-supported `x`), not by trusting the ledger's one-line assertion.

**Entrywise domination.** Since `N>=1`, `j+k+N>=j+k+1`, so `0<G_N[j,k]<=G_1[j,k]` for all `j,k>=0` — trivial but I checked it explicitly rather than skipping it.

**Chaining the bound.** `<x,G_N x> <= sum_{j,k}|x_j||x_k|G_N[j,k]` (since `x_jx_k<=|x_jx_k|` termwise and `G_N[j,k]>0`) `<= sum_{j,k}|x_j||x_k|G_1[j,k]=<|x|,G_1|x|>` (by the domination step, since `|x_j||x_k|>=0`) `<=pi‖x‖_2^2` (the classical `N=1` sharp Hilbert inequality, applied to the vector `|x|`, whose `ℓ²` norm equals `‖x‖_2`). This gives `‖G_N‖<=pi` for every `N>=1`, using only the single `N=1` case of Hilbert's inequality — a textbook-classical, extremely well-established fact (Hardy–Littlewood–Pólya; proved e.g. via a Schur test with weight `(j+1/2)^{-1/2}`) — with no separate "generalized Hilbert inequality" citation needed at all. This is a materially stronger and cleaner argument than what Round 491 was checking for plausibility; it is fully self-contained.

**Independent numerical re-verification, beyond the witness's own checks.** I wrote a fresh script (no code shared with the witness) and ran 200 random trials with exact `Fraction` arithmetic, drawing `N` from `{1,2,3,5,17,256001,256003,999999}` (including far beyond and far below the physical scale) and random integer vectors of length 1–6 with entries in `[-9,9]`: in every trial, the moment-integral and direct-sum forms of the quadratic form agreed exactly, the quadratic form was non-negative, and the domination inequality `|<x,G_N x>| <= <|x|,G_1|x|>` held. All 200 passed with no exceptions — a materially broader sweep than the witness's own three fixed test vectors at five fixed shifts.

## Hash and execution verification

Witness `lane_a_v15_442_shifted_hilbert_upper_hardening.py` (commit `6b8cdaa`, blob `81a9061`, SHA-256 `2b5378fb...`) and manifest `lane_a_v15_442_shifted_hilbert_upper_hardening_manifest.md` (commit `0e83454`, blob `9ebc7b4`, SHA-256 `d850d8e2...`) verified directly against the repo and git objects — exact match. Executed the witness directly (`python3 -I`, unmodified): ran clean, output matches the ledger text exactly.

## Consequence, independently confirmed

Combining this round's confirmed upper bound with Round 491's already-confirmed lower bound gives the exact equality `‖G_N‖=pi` for every `N>=1`, hence `‖Q Hplus Q‖=pi/2` exactly on every same-parity tail — not merely bounded above by it. This remains far above the remaining triangle allowance (`≈0.00128`, confirmed in Round 491), so the practical conclusion is unchanged: no independent triangle charge on this term, at any tail depth, can close the `2.535946` target.

## Scope and honesty assessment

Correctly scoped throughout: the entry is explicit that `pi/2` is "not a lower bound on the summed operator because cancellation is possible," repeats the standing non-source-native and non-`FULL_K_TRANSFER` disclaimers, and correctly redirects toward the only admissible next route (a cancellation-preserving joint estimate with the v15.437 operator). This is also a clean example of the chain responding precisely and proportionately to an external-audit note — neither ignoring the flagged gap nor overreacting to it.

## Summary

Confirmed. Round 491's one open citation is now closed by an elementary, fully self-contained, independently-reverified proof requiring nothing beyond the classical `N=1` Hilbert inequality. `‖Q Hplus Q‖=pi/2` exactly, on both sides, for every tail depth. The barrier stands on completely rigorous footing in both directions.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-492
parent: v15.443
status: closed
action: none — v15.442's proof is correct, elementary, and independently re-verified (including 200 fresh random exact-rational trials beyond the witness's own checks). No correction needed.
deliverable: independent confirmation that ||Q Hplus Q||=pi/2 holds exactly (both directions now rigorous) on every same-parity tail, closing Round 491's one previously-unrederived citation.
