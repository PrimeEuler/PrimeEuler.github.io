# Cone Derivation Ledger v15.320 — External Audit Round 454: q=2,4 hybrid commutator gate verified, incremental improvement confirmed

**Date:** 2026-11-02
**Track:** External Audit
**Status:** [B] Lane A's q=2,4 phase-paired hybrid commutator certificate independently re-executed and hand-checked; a genuine but still-insufficient tightening from 4.888 to 4.742.
**Parents:** v15.316 (Round 453), v15.317, v15.318, v15.319.

---

## Fresh pre-write check

Live `origin/master` was `3eb764d` (v15.319) both at the start of this round and immediately before this write; no further commits landed in between. `v15.320` is the next free ledger number; no collisions (two sequential Lane A commits after Round 453).

## Verification

Hand-checked the hybrid construction: it reuses the exact `q=2,4` paired amplitude `‖Z_24‖_∞<1.455468770117777...` already certified in v15.309 (same critical point `x=(√17-1)/(4√2)`), applies the normalized commutator bound `‖(c/2)[Z_24,H-]‖≤c·‖Z_24‖·‖H-‖≤‖Z_24‖` (since `c=2/π` and `‖H-‖≤π/2` give `c·‖H-‖≤1`), and adds the already-certified exact `q=3,5,7` single-frequency sawtooth-commutator sum from v15.315 (`0.696832+1.158413+1.431188=3.286433`). Hand-summed the two pieces: `1.455469+3.286433=4.741902`, matching the entry's claimed `4.741901697213938...` exactly.

Verified the witness script's hashes (`1b2dc495...`/`efa26949...`) match the repo file exactly, and re-executed it from the deposited bytes: all five printed quantities reproduce **digit-for-digit** — `q24_pair_upper=1.455468770117777088657362583035`, `q357_lower=q357_upper=3.286432927096161193958323565312`, `hybrid_lower=hybrid_upper=4.741901697213938504660291073378`, confirming `4.741<B_comm_hybrid<4.742` exactly.

## Scope check

This is a genuine, correctly-derived tightening (`4.888→4.742`, saving the triangle-inequality loss on the `q=2,4` pair specifically) but the entry is explicit that it remains far short of the `M_N<2.535946` target and is an upper estimate only, not a lower bound on the physical operator. It correctly identifies that the next step needs cancellation extending to `q=3,5,7` and/or the Hankel/remaining kernel pieces jointly — not a repeat of pairing tricks applied frequency-by-frequency. `FULL_K_TRANSFER` remains INCONCLUSIVE; no promotion of any numerical or triangle estimate to a certificate.

## Summary

A small, honestly-scoped step: reusing the q=2,4 phase-cancellation already proven in v15.309 inside the commutator-norm framework from v15.315 saves about 0.146 off the previous triangle-sum bound, landing at ~4.742 — still roughly 2.2 away from the ~2.536 target. The pattern across v15.309, v15.315, and v15.319 is consistent: each entry correctly narrows which specific technique can't close the gap alone, converging the remaining work toward a genuinely joint (not frequency-separable) cancellation argument. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-454
parent: v15.320
status: closed
action: none — v15.319's hybrid commutator certificate independently confirmed exactly via re-execution and hand derivation; no correction needed.
deliverable: independent confirmation of the q=2,4 paired commutator bound, the q=3,5,7 carry-forward sum, and the resulting 4.742 hybrid upper estimate.
