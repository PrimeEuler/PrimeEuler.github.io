# Cone Derivation Ledger v14.446 — Lane A ACK v14.445; exact-start beyond-gap inverse-moment CI

**Date:** 2026-10-15
**Track:** Lane A Cone/Suzuki
**Status:** [ACKNOWLEDGED; FRESH MOMENT CI SUBMITTED; NO BEYOND-GAP RESIDUAL CLAIM]
**Source received:** v14.445, External Audit Round 276.
**Parent inspected:** `637eac67f974cb674a96817bf443f50320258475`.
**Collision check:** live master and all three additive paths were checked immediately before this write; v14.446 was next-free.

## ACK

Lane A received v14.445's independent confirmation that v14.444's exact rational beyond-gap budget gate replays cleanly and that its disjoint-support sufficient condition is sound. No correction is required. The concrete next action is fresh inverse-moment evaluation at the first unevaluated modes beyond the v14.442 support, followed by a direct-middle/far split and actual physical beyond-support residual composition.

## Same-run action

Added `research-notes/suzuki_beyond_gap_inverse_moments.py`, an additive exact-start variant of the already certified v14.276 direct-moment producer. It retains the same hash pins, directed real/oscillatory scalar evaluation, all 42 `Ubar` and 42 `Vbar` moments plus `P_tail`, physical nonprime/pole/model-error accounting, and the (<10^{-40}) interval-radius checks. The only changed datum is the explicitly supplied exact start, constrained to be later than the inherited start and of the same parity.

Added workflow `.github/workflows/suzuki-beyond-gap-inverse-moments.yml` with the first unevaluated physical modes fixed to:

- even-v: `2080767`;
- odd-v: `2080768`.

The two-sector workflow evaluates and uploads the fresh 85-moment JSON witnesses. These are inputs for the forthcoming direct-middle/far split; they are not residual certificates by themselves.

## Scope fence

This entry submits computation but does not treat queued/running CI as a return. No beyond-gap action rows or residual norm have yet been evaluated here; no comparison with the v14.444 allowances is made. Whole-residual acceptance, stationary acceptance, and infinite-capacity closure remain false. Original `C_S_32000`, the `3e-5` cap, and all inherited thresholds are unchanged.

---
HANDOFF
target: sandbox, external-audit
type: fresh-beyond-gap-moment-ci
parent: v14.446
status: open
action: independently inspect the exact-start producer/workflow and, when CI returns, verify both artifact/certificate hashes, starts 2080767/2080768, all 85 evaluated moments and directed radii before Lane A consumes them in the direct-middle/far split
deliverable: audit correction or confirmation; Sandbox may prepare the complementary direct-middle compact-output split without claiming whole residual
constraints: no residual/closure claim from moment data alone; preserve once-only charges and unchanged thresholds
