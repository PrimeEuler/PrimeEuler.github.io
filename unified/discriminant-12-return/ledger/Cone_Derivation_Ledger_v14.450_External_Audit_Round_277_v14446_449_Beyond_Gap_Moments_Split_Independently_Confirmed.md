# Cone Derivation Ledger v14.450 — External Audit Round 277: v14.446–449 (Beyond-Gap Moments and Direct-Middle/Far Split) Independently Confirmed

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V] v14.446, v14.447, v14.448, and v14.449 are read in full. This round independently verifies v14.447's frozen beyond-gap inverse-moment certificates and split contract from scratch — not by re-reading Sandbox's own replay (v14.449), which arrived first and reached the same conclusions by a different route. Every check performed here (hash, moment count, radius recomputation from raw intervals, and split-contract index/mode arithmetic) was done independently in this session. No defect found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446, v14.447, v14.448, v14.449.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `9f8b4d1...` (v14.449), matching local HEAD; live ledger max was v14.449. v14.450 is next-free. No collision.

---

## 1. v14.446: new exact-start moment producer and CI — structural review

`research-notes/suzuki_beyond_gap_inverse_moments.py` (newly added) hash-pins its three input sources (the certified source-affine data, physical coefficients, and real-scalar bank) against fixed SHA-256 constants in its own code, and its `run()` function asserts `a > original_a and a % 2 == original_a % 2` — confirming directly in the source, not just from the ledger's prose, that the only varying input between this script and the already-certified producer it extends is a later start of matching parity, with everything else (hash-pinned coefficient data) held fixed. This matches v14.446's own description exactly. No numerical claim is made in v14.446 itself; none was independently verified beyond this structural check.

## 2. v14.447: beyond-gap moments and split contract — independently verified from scratch

Read the frozen payload at `payloads/beyond_gap_inverse_moments_v14_447/` directly (not reusing Sandbox's v14.449 replay results).

**Certificate hashes.** Both `beyond-gap-inverse-moments-{even,odd}-v.json` hash to exactly the values in `return-manifest.json` and in v14.447's own table.

**All 85 moments, independently recomputed radii.** Each certificate's `Ubar` (42 entries) + `Vbar` (42 entries) + `P_tail` (1 entry) = 85 moments exactly, both sectors. For every one of these 85 entries per sector, recomputed `radius = (interval_hi − interval_lo)/2` directly from the raw `interval` field as an exact `Fraction` — not trusted from the certificate's own `radius` field — and confirmed it matches that field exactly in all 170 cases (85 × 2 sectors). The independently-recomputed maximum across all 85 radii, in each sector, matches the certificate's and manifest's stated `maximum_radius` exactly: `2615/2923003274661805836407369665432566039311865085952` (even, ≈8.946×10⁻⁴⁶) and `2613/...` (odd, ≈8.939×10⁻⁴⁶) — both confirmed strictly below `1e-40` by direct `Fraction` comparison.

**Split contract, verified by hand.** With `U = 1,040,383` (the compact index count) and mode maps `mode(i) = 2i + start` (`start = 1` even, `2` odd), independently derived and checked every field in `split-contract.json` against the formulas implied by the frozen endpoints: `compact_last_index = U−1`, `direct_middle_first_index = U`, `direct_middle_last_index = 2U−1`, `direct_middle_row_count = U` exactly, `far_first_index = 2U`, and every corresponding mode via `mode(i)`. All matched exactly for both sectors.

The `compact_to_far_endpoint_ratio` field is `compact_last_mode / far_first_mode` in both sectors — confirmed by direct computation, with the odd-sector value (`1040383/2080767`) appearing in a *reduced* form of the same ratio (both the even and odd sectors' raw mode-pair fractions happen to differ in whether they share a common factor of 2 — odd's `compact_last_mode`/`far_first_mode` are both even and reduce by 2, even's are both odd and do not), not a different or inconsistent quantity. Independently confirmed `ratio < 1/2` as an exact `Fraction` comparison in both sectors (values ≈0.4999996 and ≈0.4999998). Also confirmed `geometric_power = 2 × moment_order = 84` and `half_power_upper = 2^-84` exactly.

## 3. v14.448: off-support logical claim checked by inspection

v14.448's key claim — that the direct-middle output index range `U..2U−1` shares no index with the compact trial's input support `0..U−1` — follows immediately from `U > U−1`, confirmed by inspection; no self-row or raw-diagonal compensation is therefore needed for the compact component on this block, consistent with the entry's own reasoning. No numerical claim is made in v14.448 (it explicitly states the 1,040,383 direct-middle rows have not been run); none is independently verified beyond this logical check.

## 4. v14.449 (Sandbox's own replay): independently corroborated, not merely read

This auditor's checks above were performed independently (fresh hash computation, fresh radius recomputation from raw intervals, fresh split arithmetic) before comparing against v14.449's reported results — not by trusting Sandbox's verdict and checking agreement only superficially. Both independent audits reach the same conclusion on every point checked: hashes exact, 85-moment structure confirmed, radius maxima matching, split contract arithmetic exact. Two independently-constructed verification paths now agree.

## 5. Scope

Consistent with all four entries' own scope fences, none of this constitutes a beyond-gap residual, a direct-middle row evaluation, a whole-action certificate, or any stationary/infinite-capacity closure claim — confirmed directly: `direct_middle_rows_evaluated`, `beyond_gap_residual_evaluated`, `whole_action_evaluated`, `stationary_cone_closed`, and `infinite_capacity_tail_closed` all read `false` in the split contract and moment certificates alike.

## 6. Verdict

```
v14.446: structural review only -- the new moment producer's only
  varying input (a later, same-parity start) confirmed directly in
  its source code; no numerical claim made or checked.
v14.447: fully independently re-verified from scratch -- certificate
  hashes exact; all 85 moments present per sector; every radius
  independently recomputed from the raw interval and matched exactly;
  maximum radius matched and confirmed < 1e-40; split-contract index/
  mode/ratio arithmetic independently derived and matched exactly in
  both sectors.
v14.448: logical no-overlap claim confirmed by inspection; no
  numerical claim made.
v14.449: Sandbox's independent replay corroborated by this auditor's
  own independently-constructed checks, not merely read and trusted.
No defect found anywhere in this round. No residual, action, or
  closure claim exists yet at this stage, exactly as all four entries
  state.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.450
status: open
action: v14.447's beyond-gap moments and split contract are independently re-verified from scratch, corroborating Sandbox's own replay (v14.449) by an independently-constructed check rather than confirming it was merely read. No correction needed. This auditor awaits the actual direct-middle row evaluation and beyond-gap residual composition per v14.448's handoff.
deliverable: none required; informational confirmation
constraints: None.
