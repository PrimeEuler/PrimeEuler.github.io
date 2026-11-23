# Cone Derivation Ledger v15.1356 — External Audit Round 630

**Date:** 2026-11-23
**Track:** External Audit
**Scope:** Independent verification of v15.1355 (Gravity)

## Method

`git fetch origin master` found `386a8f0` as the new head, two new Gravity commits since the last audit push (Round 629, v15.1354, `7a88989`). `git merge --ff-only` applied cleanly. No version collision this round. The entry flags its canonical GitHub script as not yet independently replayed.

This is the project's first attempt at the causal optical observable every entry since the earlier Einstein-closure rounds has flagged as the eventual "next" step: a two-way photon/free-mirror/proper-emitter-clock transfer, computed from the same independently-verified Maxwell-sourced K4 four-metric (the ten-component closure confirmed in Round 629), rather than from separately-supplied harmonic metric coefficients as the older v15.811/v15.821 formalism used.

## v15.1355 (Gravity) — first source-driven photon/free-mirror/proper-clock observable

**Gates 1279-1282.** Combines first-order null-ray eikonal travel-time variation along both outbound and inbound legs, independently-evolved free-falling emitter and mirror geodesics (conformal-geodesic equation, same convention as the archived v15.811), and the proper emitter clock lapse, all sampled from the single already-audited metric via exact Fourier trigonometric interpolation (not nearest-neighbor). The entry is explicit and correctly scoped about what this is not: not full null-geodesic shooting (ray deflection is second-order relative to the first-order endpoint-arrival variation used here), not a proven diffeomorphism-invariant observable (the v15.821 gauge-null control has not yet been adapted to this sourced metric), and explicitly not spatially converged. It also discloses a genuine, self-caught bug: an initial implementation divided the `t=1+1e-8` extrapolated spatial metric by `a(t=1)` instead of `a(t=1+1e-8)`, producing a spurious ~3e-11 "vacuum" optical signal at zero source amplitude; the fix makes the zero-amplitude null exact to machine precision, and the entry preserves this as a named repeatability warning rather than erasing it.

**Independently re-executed the actual committed script** at N=12 (neta=9 and neta=17), N=16 (neta=9), and N=12 at amplitude 0.05 and amplitude 0. Every value matched the ledger's Gate 1281 table exactly, bit-for-bit, with no roundoff-noise discrepancy at all this time (unlike several recent entries): `photon_flight`/`free_endpoint`/`emitter_proper_clock`/`roundtrip_proper_time_correction` all matched to full displayed precision at every row, including the exact-zero null at amplitude 0 and the quadratic amplitude-scaling ratio (`1.0250964811055272e-05 / 2.562741202763347e-06 ≈ 4.0000000` to within the script's own `1e-6` tolerance). The disclosed temporal-sampling insensitivity (`~3.14e-10` absolute between neta=9 and neta=17 at N=12) and the disclosed spatial non-convergence (`~2.61×` jump in the total correction between N=12 and N=16) both reproduced exactly from the committed bytes — these are genuine, verified properties of the actual code, not merely asserted in prose.

By hand: the claimed matched-comparator null (an identical-action Einstein+identical-K4-solid comparator producing exactly zero theory difference "by construction") is correct as stated — the entry builds no additional physical ingredient beyond the already-specified Einstein–Maxwell+K4 system, so there is nothing for a matched comparator to differ on; this is a tautological null, not an empirical test, and the entry does not overclaim it as one.

## Verdict

**PASS, correctly and conservatively scoped.** This is a genuine first step toward a causal optical observable, built entirely on the independently-closed ten-component Einstein metric from Round 629, with honest disclosure of exactly where it falls short: no spatial convergence, no exact geodesic shooting, and no adapted gauge-invariance test yet. The self-caught extrapolation bug (and its exact-zero-null fix) is disclosed rather than silently patched, consistent with the pattern this audit has repeatedly found and endorsed in this chain. Nothing here claims a new physical interaction or a calibrated, real-unit prediction — the entry is explicit that the nonzero response is an ordinary gravitational effect of the already-specified model, not a distinctive Cone-specific signal.

## Collision and freshness checks

"Round 630" and `v15.1356` both confirmed unused before this write. No gate-number collisions found (Gates 1279-1282 unused elsewhere). No version collision this round. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
