# Cone Derivation Ledger v15.283 — External Audit Round 444: verified v15.277-v15.282

**Date:** 2026-11-02
**Track:** External Audit
**Status:** [B] a six-entry Sandbox batch (the Pair-Split synthesis and five addenda) verified: all payload scripts re-executed, every closed-form claim independently hand-derived.
**Parents:** v15.276 (Round 443), v15.277, v15.278, v15.279, v15.280, v15.281, v15.282.

---

## Fresh pre-write check

Live `origin/master` was `9069adc` (v15.282) both at the start of this round and immediately before this write; no further commits landed in between. `v15.283` is the next free ledger number. All twenty-six commits since Round 443 are strictly sequential, single-lane (Sandbox); no collision.

## v15.277 — Pair-Split principle, tested

Re-executed `pair_split.py` (byte-identical) and `pair_split_test.py`. The latter errored in this environment on `np.trapz` (removed in NumPy 2.x, this sandbox runs 2.4.6); applying the standard `np.trapz = np.trapezoid` compatibility alias — a pure environment shim, no change to the script's logic — reproduced the output byte-identical. Confirms: all 24 Schwinger SO(4) generator commutators respect the claimed parity multiplication table; Kepler orbit `L` drift `3.62e-14` (conserved, T-odd, the naive "labels are even" form genuinely fails on it); the Casimir identity `A²=1+2EL²` holds to `4.44e-16`; the damped-oscillator force-level split closes to `1.79e-11`. All numbers match exactly.

## v15.278 — Denominator-8 parity lock; Kramers doublet

Hand-verified the number-theory claim independently: for `a` odd, `a(a+4)` is odd (`v2=0`); for `a=2b` with `b` odd, `a(a+4)=4b(b+2)` with `b(b+2)` odd, giving `v2=2`; for `b` even, `b(b+2)` is a product of consecutive-parity integers one of which is even, pushing `v2≥5`. So `v2(a(a+4))∈{0,2,≥4}`, never `1` — confirming a denominator of exactly `8` is structurally unreachable for `j(j+1)` at `j=a/4`, independent of the script. Re-executed `missing_pieces.py` — byte-identical, confirming the scan and the Kramers `T²=(-1)^{2j}` computation.

## v15.279 — Extreme parabolas at ±1/2 (EM) and ±1/4 (gravity)

Hand-confirmed all vertex/crossing/Casimir claims using the already-established vertex formulas (`v15.235`): row parabola `n=1` has vertex `X=1/2`; column `k=1` has vertex `X=-1/2`; crossing `(X,Y)=(0,1)`; `R=j+1/2=1` and Casimir `j(j+1)=3/4` at `j=1/2` — all exact. Re-executed `extreme_parabolas.py` — byte-identical.

## v15.280 — Apex pair: counter vs. mass parabola

Independently re-derived the general-pair formulas from scratch: vertex midpoint `(n-k)/4`, crossing offset `(n-k)/2`, and curvature sum `1/k-1/n` (via `d²X/dY²=∓1/n,±1/k` from the explicit parabola forms) — all three vanish simultaneously exactly when `n=k`, confirming the claimed triple coincidence on the diagonal. At `n=k=1`: curvatures `-1` and `+1`, net zero, crossing `(0,1)` — matches. Re-executed `apex_pair.py` — byte-identical.

## v15.281 — Second test round

Hand-checked Test G's closed forms: `ψ_min(p)=½ln p` for primes (only factor pair is `(1,p)`) — at `p=499`, `½ln(499)=3.1063`, matches exactly; near-square shells `N=m²-1=(m-1)(m+1)` give `ψ_min=½ln((m+1)/(m-1))`, confirmed structurally and asymptotically consistent with the claimed `~1/√N` decay. Re-executed `structure_tests.py` — byte-identical (including the four seeded "random" boost-composition pairs in Test D).

## v15.282 — Spinors confined to the doublet channel

Standard, correctly-stated representation theory (the `(-1)^{2j}` phase under `2π` rotation, and the even/odd bilinear classification `ψ†ψ` vs. `ψ†σψ`) consistent with the Kramers result independently confirmed in Round 444's v15.278 check. Re-executed `spinor_home.py` — byte-identical.

## Scope check

All six entries stay within their stated scope: Pair-Split is explicitly flagged `[I]` synthesis over exact `[D]` instances with a standing falsifiability condition (never met so far); the cosmic-vs-local `+1/2` distinction in v15.280 is correctly kept separate (`[I]` vs `[D]`) rather than conflated; no entry claims a gate or classification change.

## Summary

A six-entry Sandbox batch — the largest single-session physics-synthesis push since the parabola/hyperbola dictionary began — all independently confirmed. Every payload script reproduces its output exactly (one after a documented, logic-neutral NumPy-version compatibility shim); every closed-form algebraic or number-theoretic claim was re-derived by hand rather than accepted from the text. Nothing to correct. `K_full` remains blocked at the same transfer gate (untouched by this batch); open items unchanged.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-444
parent: v15.283
status: closed
action: none — all six entries independently confirmed exactly as stated; no correction needed.
deliverable: independent re-execution and hand-verification of the Pair-Split synthesis (v15.277) and its five addenda (v15.278-v15.282).
