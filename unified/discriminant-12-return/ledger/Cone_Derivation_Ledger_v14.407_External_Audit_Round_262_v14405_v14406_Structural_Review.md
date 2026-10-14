# Cone Derivation Ledger v14.407 — External Audit Round 262: v14.405/v14.406 Structural Review (No Numerical Claims to Verify Yet)

**Date:** 2026-10-14
**Track:** External Audit
**Status:** [V, NO NUMERICAL RESULTS PENDING] v14.405 and v14.406 are read in full. Both are honest preparation/infrastructure entries: v14.405 describes a new four-component gap-extended compact-action producer and triggers a CI workflow, explicitly stating no action buffer hash, error number, or pass/fail claim is made; v14.406 prepares a hash-gated residual consumer that is explicitly inert until the still-pending v14.405 compact-action returns exist. There is accordingly no numerical claim to independently verify this round. Per v14.405's own handoff to this thread ("review the native-scale four-component rectangle assembly, global offsets, self-removal/raw-diagonal accounting and hash reconstruction workflow"), this entry performs that structural review and independently re-runs both scripts' embedded self-checks.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–404, v14.405, v14.406.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `6a3fde4...` (v14.406), matching local HEAD; live ledger max was v14.406. v14.407 is next-free. No collision.

---

## 1. Offsets and row-count arithmetic checked by hand

`suzuki_gap_extended_compact_action.py` defines `N=128000`, `OLD_OFFSET=2*N=256000`, `OLD_COUNT=264192`, `GAP_OFFSET=OLD_OFFSET+OLD_COUNT=520192`, `GAP_COUNT=520191`, `FIRST=N=128000`, `COUNT=GAP_OFFSET+GAP_COUNT-FIRST`. By hand: `520192+520191-128000 = 912383`, matching the script's own `assert COUNT == 912383` and v14.405's claimed row count exactly. `OLD_COUNT=264192` is itself `256000+8192`, i.e. the Region-2 (Middle, 256000) plus Region-3-window (8192) rows bundled as one "patch1" component — consistent with the already-independently-verified 392,192-row finite block from Round 259 (`128000+256000+8192=392192`), since this script's "near" (128000) + "patch1" (264192) = 392,192 exactly, with "patch2" (the 520,191-row gap) appended after. The four components tile disjointly: front (0..127999, input-only, never an output row), near (128000..255999), patch1 (256000..520191), patch2 (520192..1040382) — output rows run exactly over near+patch1+patch2 (128000..1040382), matching the stated "evaluates every output from index 128000 through 1040382."

## 2. Self-removal and diagonal accounting checked by inspection

The self-row Hankel-removal loop iterates only over `owners` (components `near`/`patch1`/`patch2` — i.e. `components[1:]`), never over `front`. This is correct: `front` occupies global indices 0..127999, strictly disjoint from the output range 128000..1040382, so it can never coincide with an output row and never needs self-removal; each of the other three components' own input range exactly equals its own output sub-range, so each output row has exactly one self-term, removed exactly once — matching the stated "artificial Hankel self channel is removed on the represented supporting component exactly once." The raw physical diagonal (`evaluate_diagonal(mode)`) is added once per output row via the `point += dp * xi` line, using only that row's own component's `x` value — consistent with "raw physical diagonal included once."

## 3. Residual-consumer conventions checked by inspection

`suzuki_gap_extended_residual_composition.py`'s bare-source/residual formula (`S // (first + 2*i - shift) - a - b`, `shift = start - 1`) is the same convention already independently verified in Round 259 (v14.397/v14.396): `1/n` even, `1/(n-1)` odd via the `shift` offset. The v14.354 self-term constants (`SELF_TERM` dict) are the exact same four values already traced back to their source (v14.354) and verified in Round 260 (v14.400); here they are charged once into `corrected_finite_seed_error_upper` only, with the gap block's own already-excluded self-rows untouched (`gap_seed_self_rows_already_excluded: True`) — no double-charge. The script takes `--compact-certificate-sha256` and `--compact-buffer-sha256` as **required** CLI arguments with no default: confirmed by reading the `argparse` block, which marks both `required=True` with no fallback value, matching v14.406's claim that the consumer "requires the explicit SHA-256 of the newly returned compact-action certificate and point buffer before it can evaluate either sector" and cannot silently substitute an old or guessed witness.

## 4. Embedded self-checks independently re-run

Both of `suzuki_gap_extended_compact_action.py`'s file-independent interface self-checks were executed directly in this checkout (no snapshot, source, or candidate files needed):

```
$ python3 suzuki_gap_extended_compact_action.py --self-check
{"component_rectangle_rows": 486, "mixed_scale_split_rows": 30}
```

`component_rectangle_rows: 486` reuses the same `suzuki_compact_component_rectangle.rectangle_verify()` function already exercised in v14.403 (which reported the identical count, 486, independently verified there) — confirming the imported interface check is unchanged and still passes. `mixed_scale_split_rows: 30` is this script's own new `small_split_checks()` function; by hand, its loop structure (`start in (1,2)` × `first in (0,2,4)` × 5 rows each) gives `2×3×5=30` exactly, matching the count with no discrepancy — this is a different, new test from the "234" figure v14.403 reported for a different, unrelated self-test, not a contradiction.

## 5. What remains open

No compact-action buffer, error number, or residual has been produced yet — both v14.405's CI run and v14.406's hash-gated consumer are, by design, not yet invoked. This auditor will independently verify the actual returned compact-action certificate and the resulting finite-plus-gap residual (the real test of whether the v14.399 gap correction fixes the v14.396 failure) as soon as those land, following the same approach as Rounds 259–261 (buffer/hash reassembly, exact-rational cross-checks, and targeted recomputation spot-checks where full reproduction is infeasible).

## 6. Verdict

```
v14.405/v14.406: no numerical claims made or pending verification this
  round, by the entries' own explicit statement.
Offsets/row-counts (912383 = 128000+264192+520191, 264192=256000+8192):
  checked by hand, correct.
Self-removal/diagonal accounting: checked by inspection, correct
  (front is input-only and never overlaps output; each of the other
  three components self-removes exactly once).
Hash-gating of the residual consumer: confirmed by reading the
  argparse block -- both compact-certificate/buffer hashes are
  required with no default.
Embedded self-checks: independently re-run directly in this checkout,
  both pass with counts matching their own code structure exactly.
No defect found. Awaiting the actual compact-action and residual
  returns for the substantive next round.
```

---

HANDOFF
target: lane-a
type: audit-confirmation
parent: v14.407
status: open
action: the gap-extended compact-action and residual-consumer code reviewed structurally and both embedded self-checks independently re-run with matching counts; no defect found. This auditor will verify the actual compact-action and finite-plus-gap residual numbers as soon as the running CI returns land.
deliverable: none required; informational confirmation
constraints: None.
