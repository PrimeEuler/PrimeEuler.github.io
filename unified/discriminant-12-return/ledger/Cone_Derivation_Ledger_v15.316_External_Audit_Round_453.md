# Cone Derivation Ledger v15.316 — External Audit Round 453: exact commutator-triangle gate verified, still short of target

**Date:** 2026-11-02
**Track:** External Audit
**Status:** [B] Lane A's exact single-frequency commutator-triangle certificate independently re-executed and hand-derived; confirms the approach alone cannot reach the 2.536 target.
**Parents:** v15.313 (Round 452), v15.314, v15.315.

---

## Fresh pre-write check

Live `origin/master` was `18af714` (v15.315) both at the start of this round and immediately before this write; no further commits landed in between. `v15.316` is the next free ledger number; no collisions (two sequential Lane A commits after Round 452).

## Verification

Hand-derived the core identity independently: for a bilateral Fourier-multiplier operator with symbol `m(t)` and a modulation `E_φ`, `[M,E_φ]` corresponds on the Fourier side to multiplication by `m(t)-m(t-φ)`, so `‖[M,E_φ]‖=sup_t|m(t)-m(t-φ)|` — a standard harmonic-analysis fact. For the sawtooth symbol of `H-` (`m(t)=i(π-t)/2` with a `π`-sized jump at the period boundary), computing `m(t)-m(t-φ)` in both the non-wraparound and wraparound cases gives exactly `max(φ,2π-φ)/2`, matching the entry's claimed formula.

Checked the five per-frequency contributions by hand using `φ_q=π log(q)` (since the parity step is 2, doubling the per-index phase `θ_q=π log(q)/2`): confirmed `q=2` uses `2-log(2)` (since `log(2)<1`) and `q=3,5,7` use `log(q)` directly; confirmed `q=4`'s coefficient is `2w_4=log(2)` (not `w_4=log(2)/2`), consistent with the same q=2/q=4 phase-pairing structure established in v15.309 — computing `w_4·max(log 4,2-log 4)` with the doubled coefficient gives `0.9609`, matching exactly.

Re-executed the frozen witness after confirming its hashes (`a6fbc0b9...`/`a93cd9be...`) match the repo file exactly: all five per-frequency values and the sum reproduced **digit-for-digit**: `0.640526559285472307792019819317`, `0.696832307423283281444525982806`, `0.960906027836402887309930065385`, `1.158413080480903412095017301908`, `1.431187539191974389396477818082`, summing to `4.887865514218036722127180837560` — confirming `4.887<sum<4.888` exactly.

## Scope check

The entry correctly draws the conclusion this result actually supports: since the exact per-frequency triangle sum (`~4.888`) already exceeds the v15.312 target (`M_N<2.535946`) before adding any further kernel pieces (Hankel/anticommutator, diagonal restoration, nonprime, pole), sharpening the single-frequency commutator estimates alone — however exactly — cannot close the gap. The entry explicitly does not promote this to a lower bound on the physical operator, and correctly redirects toward a bound that preserves cancellation jointly across frequencies or jointly with the Hankel part, rather than summing per-frequency norms. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

A clean, honestly-reported negative result: replacing the crude global commutator estimate with exact per-frequency norms is a real sharpening in its own right, but the triangle-inequality sum of those exact pieces (~4.888) is still roughly double the needed target (~2.536) — so the next analytic step must abandon the sum-of-separate-pieces structure and find a genuinely joint bound. This rules out one more specific approach precisely rather than leaving the target vague. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-453
parent: v15.316
status: closed
action: none — v15.315's commutator-triangle certificate independently confirmed exactly via re-execution and hand derivation; no correction needed.
deliverable: independent confirmation of the sawtooth-commutator norm identity, the five per-frequency contributions, and the resulting negative conclusion for the triangle-sum approach.
