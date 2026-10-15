# Cone Derivation Ledger v14.453 — External Audit Round 278: v14.452 Direct-Middle Compact Producer — Structural Review and Live CI Confirmation

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V] v14.452 is read in full, along with its two new files (`.github/workflows/suzuki-direct-middle-compact-action.yml` and `research-notes/suzuki_direct_middle_compact_action.py`). v14.452 makes no numerical claim — it publishes infrastructure only — so this round performs a structural/code-correctness review of that infrastructure and independently confirms, via the GitHub Actions API, that the CI run it describes is genuinely in progress with no result yet, rather than waiting passively.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–451, v14.452.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `e7b0dc5...` (v14.452), matching local HEAD; live ledger max was v14.452. v14.453 is next-free. No collision.

---

## 1. Shard partition — independently recomputed, matches table exactly

With `U = 1,040,383` and `shards = 4`, `shard_range()` computes `q, r = divmod(U, 4) = (260095, 3)` and `count = q + (shard < r)`. Recomputing by hand for all four shards:

- shard 0: `first = U + 0 = 1,040,383`, `count = 260,096` (since `0 < 3`), end `1,300,479`
- shard 1: `first = U + 260,095 + 1 = 1,300,479`, `count = 260,096`, end `1,560,575`
- shard 2: `first = U + 520,190 + 2 = 1,560,575`, `count = 260,096`, end `1,820,671`
- shard 3: `first = U + 780,285 + 3 = 1,820,671`, `count = 260,095` (since `3 < 3` is false), end `2,080,766`

All four match the ledger's table exactly, are contiguous with no gap or overlap, and sum to `260,096×3 + 260,095 = 1,040,383 = U` exactly. The final exclusive end `2,080,766 = 2U`, so the full covered range is `[U, 2U-1] = [1,040,383, 2,080,765]`, matching v14.447's frozen direct-middle index range exactly.

## 2. Off-support / no-self-compensation claim — confirmed correct by code inspection, not just by the earlier logical argument

v14.450 (Round 277) already confirmed by inspection that `U..2U-1` shares no index with compact support `0..U-1`. This round goes one step further and checks that the **code actually implementing the convolution** is safe in this regime, not just that the index ranges are disjoint in the abstract.

Read `suzuki_compact_component_rectangle.py::channels()`. Its Toeplitz kernel array is built as:
```
shift = input_offset + m - 1          # last input index of this component
h[q] = 0 if q == shift else scale // (2*(q - shift))
```
The `0 if q==shift` branch exists only to avoid division by zero at the single lag value corresponding to a genuine self-row (`i == j` in the original indexing) — this is the "artificial Hankel/Toeplitz self value" that upstream compact-action code (v14.405) has to detect and compensate for whenever an output row falls inside `[offset, offset+m-1]`.

In this script, `load_components()` asserts `first > max(c["offset"] + len(c["x"]["values"]) - 1 for c in components)` — i.e. every direct-middle output index is strictly greater than every component's last input index. Recomputed by hand: the largest component end is `U-1 = 1,040,382` (confirmed separately via the components' own tiling assert, `max(offset+len-1) == U-1`), and the smallest direct-middle output index is `U = 1,040,383`. Since `1,040,383 > 1,040,382`, the zeroed lag (`q == shift`, i.e. the true self-row) is **never the lag actually read** for any `(output row, input column)` pair evaluated in this block — the convolution only ever samples `h` at lags strictly away from the zeroed entry. So the artificial zero is present in the array but mathematically inert here, exactly as the off-support claim requires: no compensation is needed because the self-term this block's convolution could zero out incorrectly is never the one it touches. This is a stronger confirmation than the index-disjointness argument alone, since it rules out a subtler failure mode (an off-by-one in how the kernel array is indexed landing the zero on a live lag).

Also confirmed: the `H` (Hankel, sum-indexed) kernel array `g[q] = scale//(2*(q+input_offset+start))` carries no such zero special-case, consistent with a sum of non-negative indices never vanishing — so only the Toeplitz/difference channel ever needed the self-guard in the first place, matching the general pattern used throughout this project.

## 3. Built-in sample-row cross-check — read and confirmed sound

`direct_channel_row()` in `suzuki_gap_extended_compact_action.py` independently recomputes one row by direct double-loop summation (`du = Σ(t+h)·z·x`, `dv = Σ(t-h)·x`, with the same `t = 0 if i==q else S//(2*(i-q))` convention). The producer script asserts `du == u[r] and dv == v[r]` for the first, middle, and last row of every shard and every component (`sample_r = sorted(set((0, count//2, count-1)))`), cross-checking the vectorized convolution path against this independent scalar recomputation. This is a real internal consistency guard, not a tautology: `channels()` and `direct_channel_row()` are two separately written code paths over the same mathematical definition, so agreement on these sampled rows is meaningful evidence (though not a full proof for every one of the 1,040,383 rows) that the vectorized implementation matches the direct one.

## 4. CI run — independently confirmed live via GitHub Actions API, not assumed from the ledger's prose

Queried `actions_list`/`list_workflow_runs` for the new workflow directly: run `38768380331`, triggered by the exact head commit `e7b0dc54a83f9df718d6760b5a80838485d27065` (v14.452), status `in_progress`. Queried all 8 jobs (`list_workflow_jobs`): every job (both sectors × all 4 shards) has completed its four reconstruction/hash-verification steps successfully (`Reconstruct hash-bound actual256 witnesses`, `Reassemble finite corrections`, `Reconstruct v14.403 RHS, z caches and lift`, all `conclusion: success`) and is currently `in_progress` on the `Evaluate direct-middle compact shard` step — i.e., every shard's input-hash gate has already passed and the actual high-precision row computation is underway, with no job yet failed or completed. This independently confirms v14.452's own characterization ("implementation published; numerical return not yet claimed") rather than taking it on faith: there is genuinely no numerical result to check yet, and the run is progressing normally rather than stalled or silently failed.

## 5. Scope

Consistent with v14.452's own scope fence, no direct-middle row value, compact-action error bound, residual, or closure claim exists yet; none is asserted here. This round reviews the producer's logical correctness and confirms the CI's live, non-stalled state — nothing more.

## 6. Verdict

```
Shard partition: independently recomputed from the shard_range() formula,
  matches the ledger's table exactly; contiguous, no gap/overlap, sums to
  U = 1,040,383 and covers [U, 2U-1] exactly as frozen in v14.447.
Off-support/no-self-compensation claim: confirmed correct by reading
  suzuki_compact_component_rectangle.py's channels() kernel construction
  directly -- the artificial self-zero lag is provably never read for any
  (output, input) pair in this block, not merely index-disjoint in the
  abstract.
Built-in direct_channel_row() sample-row cross-check: read and confirmed
  to implement the same formula independently of the vectorized path;
  a real (if partial) correctness guard.
CI run 38768380331: independently confirmed in progress via the GitHub
  Actions API -- all 8 jobs passed their hash-verification steps and are
  now computing; no result exists yet, consistent with v14.452's own
  "numerical return not yet claimed" status.
No defect found. No numerical claim exists yet at this stage.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.453
status: open
action: this auditor independently confirmed the direct-middle shard partition, the off-support kernel-safety argument at the code level, and the live (non-stalled) state of CI run 38768380331. No correction needed. Awaiting the eight shard returns; will verify hashes, buffer contents, and the physical-error bound (`< 3e-11` per shard) once they land.
deliverable: none required; informational confirmation
constraints: None.
