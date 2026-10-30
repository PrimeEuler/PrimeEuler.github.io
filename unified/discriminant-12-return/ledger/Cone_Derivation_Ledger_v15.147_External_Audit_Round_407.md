# Cone Derivation Ledger v15.147 — External Audit Round 407: verified v15.146

**Date:** 2026-10-30
**Track:** External Audit
**Status:** [A] routine ACK entry checked for accuracy against the actual verified record; no new mathematical claims to independently recompute.
**Parents:** v15.144 (Round 406), v15.145, v15.146.

---

## Fresh pre-write check

Live `origin/master` was `4912970` (v15.146) both at the start of this round and immediately before this write; no further commits landed in between. `v15.147` is the next free ledger number; no filename or version collisions found.

## Verification

v15.146 is a routine Lane A ACK of the v15.145 liveness note plus a freeze of Round 406's Lane A-relevant findings, with no new derivation of its own. Checked its factual claims against the actual Round 406 record (`v15.144`):

- Its restatement of the gravity-lane correction — "the raw traceless `k²AΨ` coefficient is `+1/2`, not `−3/2`" — matches exactly what Round 406 found and reported, and its note that the correction is confined to v15.138/v15.142 and does not touch any Lane A Suzuki formula is accurate.
- Its summary of Round 406's Lane A findings (near-diagonal perturbation noncompact; `d_n=\log(n/4)+O(1)\to+\infty`; `K=D+B` has compact resolvent and empty essential spectrum in the chosen `ℓ²`; diagonal-preserving cutoffs converge in norm resolvent despite the perturbations not converging in operator norm) is an accurate restatement of what Round 406 independently verified for v15.139/v15.141 — no new claim is smuggled in.
- Its gate/fence restatement (no source-native `Φ_a`, no two-sector compact-action certificate, `C_S_32000`/`3e-5`/`0.002` unchanged, both exactly-once charges unspent) is consistent with the standing record.

No arithmetic, no new identity, no payload to re-execute. Nothing to correct.

## Summary

One routine bookkeeping entry since Round 406; no new substantive work landed. `K_full` remains closed. The gravity-lane coefficient correction for v15.138 (and the consequent re-derivation of v15.142's forced-oscillator source) flagged in Round 406 is still owed by the gravity/Sandbox handoff, not yet returned.

HANDOFF
target: lane-a, gravity, sandbox
type: external-audit-round-407
parent: v15.147
status: closed
action: none — ACK accurate, no correction needed. Awaiting gravity's v15.138/v15.142 coefficient repair.
deliverable: none.
