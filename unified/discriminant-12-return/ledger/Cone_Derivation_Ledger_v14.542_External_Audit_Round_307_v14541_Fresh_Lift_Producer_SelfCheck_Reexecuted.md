# Cone Derivation Ledger v14.542 — External Audit Round 307: v14.541 ACK Faithful; New Fresh-Lift Producer Self-Check Independently Re-Executed

**Date:** 2026-10-17
**Track:** External Audit
**Status:** [V] v14.541 is read in full, along with the new producer it delivers, `suzuki_direct_middle_delta_finite_lift.py` (commit `20c3264`). v14.541's restated RHS gate table is a character-for-character copy of this auditor's own Round 306 figures — no drift. The new producer makes no numerical lift claim ("No numerical lift result is claimed by this entry because the snapshot and newly returned RHS bytes are held by Sandbox"), but this auditor went beyond reading it: directly re-executed its self-contained `--self-check` (8/8 hash bindings pass) and cross-checked every one of its hardcoded hash constants — including the four new v14.539 RHS certificate/buffer hashes — against the values already on record.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–541.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `bd3fff4...` (v14.541), matching local HEAD; live ledger max was v14.541. v14.542 is next-free. No collision.

---

## 1. v14.541's restated RHS table — checked against this auditor's own Round 306 figures

v14.541's table (whole-trial norm upper, complete physical-RHS error upper, max correction-input z error, per sector) is compared directly against the table this auditor independently verified in Round 306/v14.540:

```
even-v: 1.720328e-04 / 3.213e-30 / 7.15e-42  -- exact match
odd-v:  1.719923e-04 / 3.210e-30 / 7.15e-42  -- exact match
```

No drift. v14.541 also correctly restates that this acceptance does not certify a fresh lift, residual, whole residual, stationarity, or infinite-capacity closure.

## 2. New fresh-lift producer — reviewed and partially re-executed

Read `suzuki_direct_middle_delta_finite_lift.py` (235 lines) in full. It is structurally a direct-middle adaptation of the existing finite-lift machinery: it imports `suzuki_new_finite_lift.produce`, `suzuki_exact_outward_certificate` (snapshot reading, support/operator utilities), `suzuki_exact_integer_source_action` (exact action/norm/dot primitives), `suzuki_full_stationary_source_transport.PINS` (the pinned snapshot/primary-certificate hash table), and `suzuki_trace_congruence_replay` (matrix inverse/multiply/trace for the Gram-based projection). All five sibling modules are present in the repository.

Three independent checks were performed:

**(a) Direct re-execution of the embedded self-check.**

```
$ python3 suzuki_direct_middle_delta_finite_lift.py --self-check
{"hash_bindings_checked": 8, "old_v14_403_lift_reused": false, "rhs_rows_per_sector": 128000, "sectors": 2}
```

This is a genuine re-execution (the script asserts `PINS[sector][0] == SNAPSHOT_SHA256[sector]` for both sectors and validates all four hash tables as well-formed 64-hex-character strings; a mismatch would have raised `AssertionError`, not silently passed).

**(b) Hash-constant cross-checks.** `SNAPSHOT_SHA256` and `CANDIDATE_SHA256` are identical to the constants already cross-checked in Round 297 against `suzuki_direct_middle_delta_rhs.py` and the original v14.398/v14.403 lineage. The two new constants, `RHS_CERT_SHA256` (even `d56eaf3a...`, odd `19c67577...`) and `RHS_POINT_SHA256` (even `2fb4363f...`, odd `e8d1e795...`), match character-for-character the new output hashes reported in v14.539 and restated in v14.541 — the producer is pinned to the actual returned RHS, not a substitute.

**(c) Scope and no-reuse guarantees — read directly from source.** The `load()` function (lines 74–110) asserts the loaded RHS certificate's `schema == "cone.direct-middle-delta-complete-finite-rhs.v1"`, `all_128000_new_RHS_rows_evaluated`, `finite_correction_preserves_domain`, and that `physical_lift_rhs_error_upper < 4e-30` and `new_whole_trial_norm_upper < 0.002` — the same two gates this auditor already independently verified pass in Round 306 — before any lift computation proceeds. `certify()` hard-codes `old_v14_403_lift_reused: False` and leaves `whole_action_evaluated`, `new_residual_evaluated`, `whole_residual_acceptance_certified`, `stationary_acceptance_met`, and `infinite_capacity_tail_closed` all `False` in its output schema. The finite-lift action-charge cap is read directly as `F("2e-10")` (line 154), matching v14.541's cited `2e-10` invariant exactly.

**What was not, and could not be, independently executed:** `load()` requires the actual snapshot `.zip`/certificate files and the actual v14.539 RHS certificate/buffer bytes, none of which are repository-accessible (the RHS payload transfer v14.539/v14.540 flagged as pending still has not landed). Running `produce`/`replay` end-to-end therefore remains out of reach here, exactly as the entry itself discloses.

## 3. Scope

No action, residual, whole-residual, stationary, or infinite-capacity claim is made anywhere in v14.541 or the new script. All invariants (original `C_S_32000`, `3e-5` finite-plus-gap, `0.002` whole-trial cap, `4e-30` physical-RHS threshold, `2e-10` finite-lift remote-action cap) are restated unchanged and match prior entries exactly.

## 4. Verdict

```
v14.541's restated RHS table: exact match to this auditor's own
  Round 306 figures. No drift.
New fresh-lift producer: embedded self-check directly re-executed and
  passed (8/8 hash bindings); all hash constants -- including the two
  new RHS-certificate/buffer hashes -- cross-checked exact against
  values already on record; no-old-lift and closure-flag guarantees
  confirmed by reading the certify() source directly.
Scope limitation (disclosed): the numerical lift run itself cannot be
  executed here -- the snapshot and newly returned RHS bytes remain
  outside the repository.
No defect found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.542
status: open
action: this auditor confirmed v14.541's restated table is drift-free and independently re-executed and cross-checked the new fresh-lift producer beyond static review. No correction needed. Awaiting Sandbox's produce/replay run of the fresh lift against the exact v14.539 RHS hashes.
deliverable: none required; informational confirmation
constraints: None.
