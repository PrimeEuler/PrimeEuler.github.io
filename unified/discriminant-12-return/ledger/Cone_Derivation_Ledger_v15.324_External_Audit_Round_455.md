# Cone Derivation Ledger v15.324 — External Audit Round 455: q=3,5,7 multiplier-sup route NO-GO verified

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's q=3,5,7 lumped-multiplier sup-norm route independently re-executed and its Kronecker-density argument hand-checked; correctly closed as worse than the existing v15.315 bound, not promoted as new progress.
**Parents:** v15.320 (Round 454), v15.321, v15.322, v15.323.

---

## Fresh pre-write check

Live `origin/master` was `77d5088` (v15.323) both at the start of this round and immediately before this write; no further commits landed in between. `v15.324` is the next free ledger number; no collisions (two sequential Lane A commits after Round 454).

## Verification

Checked the rational-independence argument for `1, log(3)/2, log(5)/2, log(7)/2` by hand: a nonzero integer relation after clearing denominators gives `e^{m_0}=3^{-c_1}5^{-c_2}7^{-c_3}` for some integer `m_0`; if `m_0≠0`, Lindemann–Weierstrass makes the left side transcendental while the right side is rational — contradiction; if `m_0=0`, unique factorization over the distinct primes `3,5,7` forces `c_1=c_2=c_3=0`. This is a correct, standard argument, and the resulting Kronecker-density conclusion (the three phases are simultaneously dense on the torus, so the sup of the multiplier sum equals the sum of individual amplitudes) is the standard consequence.

Verified the witness script's hashes (`2e491a92...`/`9127014e...`) match the repo file exactly, and re-executed it: `q357_amplitude_sum_lower=q357_amplitude_sum_upper=4.179063040324325406515981740085`, confirming `4.179<‖Z_357‖_∞<4.180` exactly. Noted this is the **identical value**, digit-for-digit, to v15.309's independently-verified `rest_upper` (`2·Σ log(q)/√q` for `q∈{3,5,7}`) from Round 450 — the same quantity correctly reused rather than recomputed differently, a good internal-consistency sign.

## Scope check

The entry draws the correct and only defensible conclusion: this lumped-multiplier-then-generic-commutator-inequality route (`~4.179`) is strictly **worse** than the already-established exact frequencywise commutator sum for the same three frequencies (`3.286432927...`, from v15.315/Round 453), so it is correctly closed as a dead end rather than presented as progress. It explicitly does not claim a lower bound on the physical commutator and does not foreclose an operator-specific (shifted-sawtooth or joint commutator–Hankel) argument. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

A quick, correctly-reasoned negative result: before trying anything more elaborate, Lane A checked whether simply lumping the three remaining frequencies into one multiplier and reusing the generic commutator inequality could beat the existing exact per-frequency sum — it cannot (4.179 vs. 3.286) — so that specific shortcut is closed. This keeps the search space honestly narrowed without wasted effort elsewhere. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-455
parent: v15.324
status: closed
action: none — v15.323's rational-independence argument and sup-norm witness independently confirmed exactly; no correction needed.
deliverable: independent confirmation of the Kronecker-density argument, the exact sup-norm value (matching v15.309's reused constant), and the correct comparison against v15.315.
