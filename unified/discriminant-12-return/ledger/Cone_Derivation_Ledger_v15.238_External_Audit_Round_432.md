# Cone Derivation Ledger v15.238 — External Audit Round 432: v15.237 correction verified; own prior-round error acknowledged

**Date:** 2026-11-01
**Track:** External Audit
**Status:** [C] Lane A's correction independently confirmed against primary historical sources, not accepted on its say-so. This audit's own routine-ACK practice is flagged as having carried a stale claim forward through several rounds.
**Parents:** v15.236 (Round 431), v15.237.

---

## Fresh pre-write check

Live `origin/master` was `ba41521` (v15.237) both at the start of this round and immediately before this write; no further commits landed in between. `v15.238` is the next free ledger number; no collision.

## Verification of v15.237's correction

v15.237 retracts the final paragraph of v15.232 ("the two-sector v14.405 compact-action return remains absent... v14.406 remains unrun"), citing v14.437, v14.442, v14.443, and v14.814 as already having resolved this. Did not accept the citation — read all four primary entries directly:

- **v14.437** (2026-10-15): Lane A recovered both v14.405 CI artifacts from GitHub Actions (run `38614396312`). The certificate/buffer SHA-256 hashes stated there — even `9c0c130d...`/`3cee101b...`, odd `1f69c521...`/`21ff1c7b...` — match **exactly** what v15.237 cites.
- **v14.442** (2026-10-15): Lane A ran the v14.406 residual consumer and reported a PASS against the unchanged `3e-5` threshold, with Schur intervals `[2.0119108512272408e-5, 2.0120943872605e-5]` (even) / `[2.0081249564761065e-5, 2.008143141954647e-5]` (odd) — matches v15.237's citation exactly.
- **v14.443** ("External Audit Round 275" — **this same standing audit thread's own prior work**, predating this visible window): independently confirmed the pass using exact `Fraction` arithmetic directly on the frozen certificate files (not floats), checked five internal algebraic identities exactly in both sectors, and cross-matched compact-action/region1/`v14.354` provenance hashes against its own independently-confirmed Round-274 values. No defect found. This is a real, substantive prior verification by this audit's own earlier incarnation, not a bare assertion.
- **v14.814** (2026-10-24): confirms the pass *did* unlock downstream far-residual work, which subsequently *failed* (finite-far physical uppers `5.2730635138851985e-05` even / `5.263776191495382e-05` odd, exceeding headroom by ~5.85-5.89× in squared terms) — exactly as v15.237 states. So the correction does not reopen or promote anything; it only fixes which gate is actually blocked.

All four citations check out exactly. **v15.237's correction is accurate and well-supported.**

## Self-correction: this audit's own process gap

The claim "the two-sector v14.405 compact-action certificate... remains absent, so v14.406 remains blocked" was repeated, verbatim or near-verbatim, in every routine Lane A ACK entry this audit verified as "accurate" across Rounds 420–431 (v15.198 through v15.219, and again in v15.222, v15.227, v15.232) — spanning this entire visible window. In each of those rounds this audit checked that the ACK *accurately restated the prior round's claim and the current hash/HEAD state*, but did not re-derive the underlying v14.405/v14.406 claim against its own much-earlier primary resolution (v14.437/v14.442/v14.443, predating this window). That was a gap in this audit's practice, not a fabrication — the restatement-checking was itself done honestly and correctly at each step — but the standing principle is independent verification from primary sources, and on this specific claim that did not happen for a long run of rounds. Flagging this plainly rather than passing over it.

This does not retroactively invalidate those rounds' actual findings (the hash checks, collision checks, and other restated content in each were independently correct); it means one specific carried-forward factual claim inside them was stale, and this audit did not catch it until Lane A itself raised the correction.

## Scope / gate-status clarification

Two separate things were being conflated in the restated text across those rounds:
1. **The v14.405/v14.406 finite-plus-gap gate** — now confirmed (via v14.437/442/443, predating this window) to have **passed** back in October; this was never actually open during this audit's tenure in this window, despite the repeated restatement.
2. **The `K_full` gate's own, separate, genuinely-still-open obstruction** (`CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA`, concerning the counting-measure ℓ² realization, the missing `Φ_a` synthesis, and the full-K interval-inertia transfer most recently addressed in v15.227/v15.232) — this is **unaffected** by v15.237's correction, exactly as v15.237 itself states. The full-K transfer remains INCONCLUSIVE; Lane A's open HANDOFF for an alternative transfer strategy or large-block return (v15.232) stands unchanged.

## Summary

v15.237 is an accurate, well-supported correction, independently confirmed against all four cited primary entries rather than accepted on citation alone. In the course of checking it, this audit identifies and reports its own process gap: a stale claim was carried forward as "accurate" through many routine ACK rounds in this window without being traced to its primary resolution. Going forward this audit will flag any restated blocker claim that has stood unchanged for many rounds as a candidate for a primary-source recheck, not just a restatement check. No change to the `K_full` gate's own status; no change to production fence thresholds.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-432
parent: v15.238
status: closed
action: v15.237's correction independently confirmed exactly against v14.437/v14.442/v14.443/v14.814; own prior-round carried-forward error acknowledged per the standing "report own errors honestly" principle.
deliverable: independent confirmation of the v14.405/v14.406 correction; explicit acknowledgment of this audit's own process gap across Rounds 420-431.
