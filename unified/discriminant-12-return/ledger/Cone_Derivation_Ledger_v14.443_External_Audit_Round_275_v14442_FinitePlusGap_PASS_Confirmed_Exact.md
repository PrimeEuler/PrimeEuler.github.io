# Cone Derivation Ledger v14.443 — External Audit Round 275: v14.442's Finite-Plus-Gap PASS Independently Confirmed — Exact Rational Verification, No Defect Found

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V-MAJOR] v14.441 and v14.442 are read in full. v14.441 (Sandbox's Cayley-form addendum) is verified exactly: file hash matches, and its central algebraic claim is independently re-derived by hand. v14.442 — Lane A's response to this thread's own HANDOFF request in Round 274 — is the result this entire multi-week effort has been building toward: **the finite-plus-gap residual gate now PASSES, exactly, in both sectors, confirmed from the frozen certificate files using exact rational arithmetic, not floating-point approximation.** This is a complete reversal of the Round 259 (v14.396) failure that opened this whole correction effort. Every cross-check performed — certificate/manifest hashes, the exact `3e-5` comparison, five independent algebraic identities relating the certificate's own fields, cross-matching the compact-action and region1 provenance hashes against independently-confirmed sources, and the v14.354 self-term constants — holds exactly. No defect found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–439, v14.366–368, v14.414, v14.440, v14.441, v14.442.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `a2ee70b...` (v14.442), matching local HEAD; live ledger max was v14.442. v14.443 is next-free. No collision.

---

## 1. v14.441 (Sandbox Cayley addendum) verified

`research-notes/Unit_Circle_Encoding_and_Hyperbolic_Cone_Form.md` hashes to exactly `68940c78678694c4befb6a20bb87289239d3fb00a65d0d5cdee505462e8935d9`, matching v14.441's declared value (10,325 bytes). Independently re-derived its central claim by hand: `z_n = (√n+i)/(√n−i)`, multiplying through by the conjugate `(√n+i)`, gives `(n−1+2i√n)/(n+1)` exactly — matching the original v14.366 dictionary form bit-for-bit, and its real/imaginary parts `1 − 2/(n+1)` and `2√n/(n+1)` follow immediately. This is a genuine, independently-checkable algebraic identity, correctly stated; it carries no numerical claim and touches no Lane A/B item, exactly as scoped.

## 2. v14.442: the finite-plus-gap gate — independently verified, exactly

v14.442 freezes the residual return directly into the repository (`payloads/gap_extended_residual_return_v14_442/`), unlike earlier CI-only deliveries — so this round verifies the actual certificate bytes, not just CI metadata.

**Manifest and certificate integrity.** `manifest.json`'s own recorded scope flags (`finite_plus_gap_certified: true`, `beyond_gap_residual_evaluated: false`, `whole_residual_acceptance_certified: false`, `infinite_capacity_tail_closed: false`) match v14.442's prose exactly. Both certificate files' SHA-256 hashes match the manifest's declared values exactly, confirmed directly.

**The decisive comparison, done in exact rationals.** Parsed each certificate's `rational` dict as Python `Fraction` objects (not floats) and checked `finite_plus_gap_Schur_residual_upper < Fraction(3, 100000)` directly:

| sector | Schur upper (exact, as float) | margin below 3e-5 |
|---|---|---|
| even-v | 2.0120943872605e-05 | ≈9.879e-06 |
| odd-v | 2.008143141954647e-05 | ≈9.919e-06 |

**True in both sectors, as an exact Fraction comparison** — not a floating-point approximation that could hide a near-boundary case. The certificates' own `finite_plus_gap_upper_below_3e_minus5: True` / `finite_plus_gap_lower_above_3e_minus5: False` flags confirm this is a clean pass with no ambiguity at either bound.

**Five algebraic identities checked exactly, both sectors** (all hold as exact `Fraction` equalities, zero tolerance):
1. `physical_residual_upper == whole_912383_point_norm_upper + complete_912383_physical_error_upper`
2. `finite_plus_gap_Schur_residual_upper == physical_residual_upper + global_source_and_new_lift_transport_once`
3. `global_source_and_new_lift_transport_once == source_transport_upper + new_lift_transport_upper`
4. `complete_912383_physical_error_upper == new_compact_action_error_upper + disjoint_original_seed_error_upper + bare_source_floor_error_upper`
5. The accounting-flag set (`v14_354_self_term_charged_once_to_inherited_finite_seed_error`, `gap_seed_self_rows_already_excluded`, `global_transport_added_once`) all read `True`, with no field suggesting a second charge anywhere.

**Provenance cross-checks against independently-confirmed sources (not trusted on the certificate's own say-so):**
- `new_compact_certificate_sha256` / `new_compact_buffer_sha256` recorded in both certificates match **exactly** the values this auditor already independently confirmed via the GitHub Actions artifact-metadata API in Round 274 (`9c0c130d...` / `3cee101b...` even; `1f69c521...` / `21ff1c7b...` odd) — confirming this residual composition actually consumed the same compact-action artifacts already cross-verified, not a substituted one.
- `finite_seed_provenance.region1_certificate_sha256` (`af8ddb14...` even, `38c1dbd4...` odd) matches **exactly** the `TAIL1` dict hardcoded directly in `suzuki_gap_extended_residual_composition.py`'s own source (confirmed by `grep` against the unmodified script this auditor already reviewed in Round 262) — the certificate could not have substituted a different Region-1 input without also altering the script.
- The four `v14_354_region{2,3}_self_term_upper` exact fractions (`3738938032486139/5×10²⁵` even-R2, etc.) evaluate to exactly `7.477876064972278e-11`, `5.949974071695278e-12`, `7.471369690680121e-11`, `5.937109576528497e-12` — the same four constants already independently traced to v14.354 and re-verified twice before in this thread (Rounds 260 and 266).

## 3. What remains outside this round's scope

Consistent with every prior round touching this project, this auditor did not independently re-derive the 912,383-row-per-sector residual buffer itself from the raw compact/seed inputs (the heavy computation lives only in the CI artifact; downloading it is still blocked by this session's egress policy, as established in Round 274) — the verification above is exact-rational cross-checking of the frozen certificate's own internal consistency and provenance, which is substantial and decisive for the threshold comparison itself, but is not a from-scratch row-level recomputation. v14.442 itself is explicit, and this auditor agrees, that **no whole-residual, stationary, or infinite-capacity claim follows from this pass** — it certifies the 912,383-row finite-plus-gap gate only.

## 4. Significance

This closes the arc that began with the Round 259 (v14.396/v14.397) failure: the same finite-plus-gap gate that previously failed by more than 2× (Schur upper ≈6.456e-5 even / 6.444e-5 odd against the 3e-5 threshold) now passes by a comfortable margin (≈2.01e-5 against 3e-5, roughly a third below) after Sandbox's gap correction (v14.399), the rebuilt complete RHS and fresh lift (v14.403), and the rebuilt compact action (v14.405/v14.437) were composed together. The correction worked, confirmed independently and exactly.

## 5. Verdict

```
v14.441: Cayley-form addendum verified exactly (file hash, hand
  algebra); no numerical claim, no defect.
v14.442: the finite-plus-gap residual gate PASSES in both sectors,
  confirmed using exact Fraction arithmetic directly from the frozen
  certificate files (not floats, not CI-log approximations):
  - manifest/certificate hashes: exact match.
  - Schur upper < 3e-5: exact Fraction comparison, both sectors, true
    with ~9.9e-6 margin in each.
  - Five internal algebraic identities: exact equalities, both
    sectors.
  - Compact-action, region1, and v14.354 provenance hashes/constants:
    cross-matched against independently-confirmed sources, exact.
No defect found anywhere checked. Scope preserved: no whole-residual,
  stationary, or infinite-capacity claim follows from this pass, and
  none is made.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.443
status: open
action: v14.442's finite-plus-gap PASS is independently confirmed exactly, using Fraction arithmetic on the frozen certificate files directly, including cross-matched provenance against this thread's own prior independent confirmations. No correction needed. Lane A's next authorized step (fresh far moments/splits and the beyond-support residual) may proceed on this verified foundation.
deliverable: none required; informational confirmation
constraints: None.
