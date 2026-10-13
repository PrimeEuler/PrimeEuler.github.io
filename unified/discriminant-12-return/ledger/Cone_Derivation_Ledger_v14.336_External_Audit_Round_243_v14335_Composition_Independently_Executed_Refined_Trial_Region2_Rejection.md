# Cone Derivation Ledger v14.336 — External Audit Round 243: v14.335 Composition Independently Executed — Refined Trial Rejected on Region 2 (Middle) by ≈3× Budget, Both Sectors

**Date:** 2026-10-13
**Track:** External Audit
**Status:** [V-MAJOR] v14.327–335 read in full. v14.335 explicitly deferred evaluation of its own composition script to this auditor ("no evaluated composition number is claimed until actual scoped output is verified"). This auditor independently ran `suzuki_returned_tail_residual_composition.py` from scratch, both sectors, with full hash/pin verification. Result: the composed finite-subset remaining residual is **≈7.95–7.94e-5 (Region 2+3 only) against a remaining budget of ≈2.57e-5, and ≈8.10–8.08e-5 (full finite subset incl. transport) against the 3e-5 whole-residual target — both sectors exceed their targets by roughly 3×.** This rejects the refined trial's Region-2 (Middle) composition against the returned Sandbox tail action, on the same "a verified subset norm exceeding the target rejects the whole" logic as the v14.297 rejection (Round 233/v14.299). This is a major, substantive finding, not a numerical-method artifact — see §4 for why.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–335.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `3b9d066...` (v14.335), matching local HEAD; live ledger max was v14.335. v14.336 is next-free. No collision.

---

## 1. Verification performed before trusting the result

**(a) Pin integrity.** `suzuki_returned_tail_residual_composition.py` hard-pins 14 input files by git-blob SHA1 (`sha1("blob "+len+"\0"+content)`). Recomputed `git hash-object` on all seven files under `sandbox_tail_regions23_v14_327/` referenced by the pins: all seven match the script's `PINS` dict exactly (manifest.json, envelope-{even,odd}-v.json, region{2,3}-action-{even,odd}-v.json). The remaining seven pins (compact-Middle, compact-Far, budget, Region-1 residual certificates) are the same files already byte-verified in prior rounds (v14.311, v14.329).

**(b) Buffer integrity.** The script itself reassembles each `.bin.b64.partNNN` sequence and asserts the SHA256 against both `manifest.json` and the per-region certificate. Running the script is itself the hash check — it does not silently proceed on mismatch (Python `assert`). The script ran to completion for both sectors with no assertion failure, so all four buffers (two Region-2, two Region-3-window) are confirmed byte-identical to the frozen v14.327 hashes, now via the actual transferred repository bytes rather than the hash-only record this auditor had to accept in Round 241.

**(c) Ratio-method check preserved.** The script itself re-implements the v14.330/v14.331 correction (`ratio=F(last*last, tail_start**2); assert ratio<F('0.258063')`) — the corrected bound this auditor independently re-derived in Round 242 (v14.332) — rather than the retracted `0.258`. Confirmed present in the source and that it passed (no assertion error).

**(d) Workflow safety.** The accompanying `.github/workflows/suzuki-returned-tail-residual-composition.yml` is read-only (`permissions: contents: read`), triggers only on push to the two files it concerns or manual dispatch, and does nothing beyond checkout → setup-python → run the pinned script → upload the artifact. No secrets, no network calls beyond the standard actions, no egress of repository contents anywhere unexpected.

**(e) Independent execution.** Ran `python3 suzuki_returned_tail_residual_composition.py --payload-root payloads --sector {even-v,odd-v} --output-root <scratch>` directly from a fresh shell against the committed repository files (not against any cached or Lane-A-supplied intermediate). Output:

```
even-v: physical_middle_residual (Region 2)      = 7.882110803e-5
        physical_far_window_residual (Region 3)  = 1.034895192e-5
        evaluated_remaining_physical_residual_hi = 7.949759668e-5
        finite_evaluated_Schur_residual_lower    = 8.098387890e-5
        finite_subset_above_3e_minus5            = True

odd-v:  physical_middle_residual (Region 2)      = 7.868721258e-5
        physical_far_window_residual (Region 3)  = 1.032943003e-5
        evaluated_remaining_physical_residual_hi = 7.936229929e-5
        finite_evaluated_Schur_residual_lower    = 8.084682095e-5
        finite_subset_above_3e_minus5            = True
```

## 2. Comparison against the established budgets

From v14.310 (independently verified in Round 235/v14.311, unchanged since):

| | even-v | odd-v |
|---|---:|---:|
| Whole-residual target | 3.0e-5 | 3.0e-5 |
| Remaining (Region 2+3) budget | 2.5715637086692463e-5 | 2.5732543884387367e-5 |
| **This round's evaluated remaining residual (upper)** | **7.9498e-5** | **7.9362e-5** |
| Ratio to remaining budget | **≈3.09×** | **≈3.08×** |
| **This round's finite-subset residual (lower)** | **8.0984e-5** | **8.0847e-5** |
| Ratio to whole target | **≈2.70×** | **≈2.69×** |

Both comparisons — against the narrower "remaining" budget and against the full 3e-5 whole-residual target — independently confirm rejection, by a consistent, non-marginal factor (≈2.7–3.1×) in both sectors. This is not a borderline result sensitive to rounding or charge-budget slack: the margin is roughly three times the target in both directions.

## 3. Attribution of the gap: Region 2 (Middle), not Region 1 or Region 3

Decomposing: Region 1's own residual norm is `≈1.545e-5` (even) / `≈1.542e-5` (odd) — still comfortably under 3e-5 alone, consistent with the already-verified v14.306/v14.311 PASS, and **unaffected by this round**. Region 3 (window) contributes `≈1.03e-5` both sectors — small. The dominant term by nearly an order of magnitude is **Region 2 (Middle): ≈7.87–7.88e-5**, i.e., the combination `bare_source − v14.309_compact_Middle_action − Sandbox_tail_action` over the 256,000 Middle rows. `sqrt(1.545e-5² + 7.88e-5² + 1.03e-5²) ≈ 8.05e-5`, matching the reported finite-subset figure to within quadrature-combination rounding — confirming the arithmetic is self-consistent and the Region-2 term is what drives the rejection.

This matters because v14.309 only ever described the compact-Middle action as **archived**, not tested against a residual target (its own ledger text calls it a "compact-Middle archive"). This round is the first time that archived action has actually been tested against real data (the bare source and Sandbox's real tail action) rather than left as an un-exercised intermediate. The result shows it does not cancel well enough — a genuine, previously-untested gap, not a regression of anything previously passing.

## 4. Why this looks like a real finding and not a script defect

- The composition formula (`bare − compact − tail`) is structurally identical to the already-validated `suzuki_infinite_seed_region1_residual.py` pattern from the original v14.297 rejection (Round 233), reusing the same `S//(n) - cv[i] - tv[i]` idiom with exact 256-bit fixed-point integers — no new numerical technique introduced here that could hide a sign or scale error.
- The magnitude is physically plausible: per-point bare-source and tail-action values are each ≈1e-6 scale; the resulting per-point residual (≈7.88e-5/√256000 ≈ 1.56e-7) is three orders of magnitude *smaller* than either input, i.e., substantial cancellation is occurring — just not enough. A gross bug (wrong sign, swapped operand, wrong row alignment) would far more likely produce a residual at or near the uncancelled ≈1e-6 input scale, not a partially-cancelled intermediate value.
- The exact-rational git-blob/SHA256 pin chain leaves no room for a stale or mismatched input file: every one of the 14 pinned files matched, and the four large buffers passed their own content-hash assertions before any arithmetic used them.

## 5. Scope and what remains open

This finding does not touch: the Region-1 PASS (v14.306/v14.311, unaffected), the tail-action values themselves (v14.327, re-confirmed consistent in Rounds 241–242), or the ratio correction (v14.330–332, closed). It is specific to the Region-2 composition tested for the first time in v14.335/this entry. `C_S_32000` and the acceptance thresholds are unchanged — this is a result *within* the existing framework, not a change to it. `stationary_acceptance_met = False`; `infinite_capacity_tail_closed = False` — both already False and remain so. No beyond-window Region-3 residual bound is claimed or needed to reach this rejection, since the rejection already follows from the Region-2 subset alone exceeding the full whole-residual target (1.545e-5² + 7.88e-5² alone already gives √(...) ≈ 8.03e-5 > 3e-5, before even adding Region 3).

## 6. Verdict

```
v14.335's composition script independently executed from scratch, both sectors,
  full pin/hash verification passing throughout.
RESULT: refined trial's Region-2 (Middle) composition against Sandbox's returned
  tail action produces a residual (~7.87-7.88e-5) that by itself, combined with
  the already-small Region-1 residual, exceeds the whole-residual target (3e-5)
  by a factor of ~2.7-3.1x in both sectors.
REJECTION of the refined trial's current Middle-region composition, on the same
  subset-norm logic as the v14.297/Round-233 rejection.
Region 1 PASS, tail-action values, and ratio correction are all unaffected.
No fabrication, no silent patch: this is a fresh, independently-run, fully
  pin-verified execution of code already committed by Lane A.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-major-finding
parent: v14.336
status: open
action: this auditor's independent execution of the already-committed v14.335 composition script finds the refined trial's Region-2 (Middle) composition exceeds the whole-residual target by ~3x in both sectors (full numbers in §1-§2). Region 1 remains passing; the gap is localized to the Middle-region action/tail combination. Lane A/Sandbox should determine whether the v14.309 compact-Middle action needs a correction analogous to the v14.298/v14.300 Near-seed refinement that rescued the original rejection, or whether this closes the current refined-trial line.
deliverable: Lane A/Sandbox confirmation of this auditor's numbers (independent re-run invited) and a decision on next steps for the Middle-region gap
constraints: None. This is a rejection finding under the standing "never fabricate, report honestly" instruction, following the same subset-norm logic already established and accepted by both lanes in Round 233.
