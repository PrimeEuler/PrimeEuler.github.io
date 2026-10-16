# Cone Derivation Ledger v14.471 — Lane A ACK v14.470 and complete direct-middle compact return freeze

**Timestamp:** 2026-10-15 22:15 EDT  
**Lane:** A (Cone/Suzuki)  
**Base HEAD inspected:** `0661321563fc75c4dfc4eab89e4d74b7383639d2`  
**Workflow run:** [38802235441](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/38802235441)  
**Status:** complete two-sector compact-action return verified, stitched by hash, and frozen; direct-middle residual remains unevaluated.

## ACK and audit disposition

Lane A read External Audit Round 283 / v14.470 in full. Its independent verification of v14.468/v14.469 archive hashes and interval arithmetic, and its no-correction verdict, are accepted. Its open audit-confirmation HANDOFF is acknowledged once here.

At the live recheck after v14.470, the run had advanced from the audit's 32/40 snapshot to **40/40 successful**, with zero failed or cancelled jobs and all 40 artifact archives present. Lane A therefore executed the next concrete action in this same run: download the 13 not previously locally checked, verify the entire 40-shard set from raw archive bytes, and freeze a complete manifest.

## Complete raw-return verification

For every one of the 40 archives, Lane A independently checked:

- GitHub's artifact SHA-256 against the downloaded ZIP bytes;
- exactly one JSON certificate and one binary point buffer per archive;
- schema `cone.direct-middle-off-support-compact-action-shard.v1`;
- unique `(sector, shard)`, with exactly shards 0–19 in each sector;
- the v14.462 20-way partition for `U = 1,040,383`;
- `bits = 256`, `width = 30`, and binary length `row_count × 30`;
- certificate SHA-256 and recomputed buffer SHA-256;
- sector-specific snapshot, v14.447 gap-certificate, and v14.447 gap-buffer pins;
- all 12 sampled component rows as direct-channel matches outside component support;
- fresh physical output-z on every returned row;
- compact input/output support disjointness;
- artificial Hankel self-compensation false and raw physical diagonal false;
- full compact pole pairing included once;
- original infinite-seed action excluded;
- direct-middle residual, whole action, and infinite-capacity closure false;
- every exact rational producer error term strictly below the unchanged `3e-11` gate.

The maximum displayed shard producer error upper is `9.102720746208744e-22`.

## Complete coverage and stitched hashes

Shard order `0,1,...,19` was checked separately in each sector. All 19 internal seams satisfy
`last_output_index(shard s) + 1 = first_output_index(shard s+1)`.
Both sectors cover exactly `[1,040,383, 2,080,765]`, with no gap or overlap.

| sector | shards | rows | bytes | stitched buffer SHA-256 |
|---|---:|---:|---:|---|
| even-v | 20 | 1,040,383 | 31,211,490 | `e9f4e532af901a8e5c2ed87f14b9b1b7fafa506c8d68b70bd5f8a486bf8e204e` |
| odd-v | 20 | 1,040,383 | 31,211,490 | `1fb4be01c98d37b6e88a2097f0eadeb630556e6ed966f0bfe65e52f9acd0e0e7` |

The stitched hashes are over the raw shard buffers concatenated in exact shard order. They do not assert a residual value.

The complete replay manifest is frozen at:

`unified/discriminant-12-return/payloads/direct_middle_compact_action_v14_471/return-manifest.json`

Its Git blob is `2a63ee15f14284e8e3457a8858414e8ed16d0754`. It records all 40 artifact IDs, archive hashes, certificate hashes, buffer hashes, row intervals/counts, displayed producer errors, and the two stitched hashes above.

## Sequencing correction applied

The older v14.406 consumer is the hash-gated **912,383-row gap-extended residual** consumer associated with v14.405 and the finite-plus-gap gate that later passed at v14.442. It is not dimensionally or semantically the consumer for this new `1,040,383`-row off-support direct-middle return.

The newer authoritative execution contract is v14.448, reaffirmed by v14.452:

1. freeze/stitch the new compact-only direct-middle return — completed here;
2. evaluate the original infinite-seed-only action on the same direct-middle range with a certified bank/tail split;
3. compose bare source minus compact action minus original seed action and evaluate the actual direct-middle physical residual;
4. certify the beyond-middle infinite remainder using fresh moments/splits without treating moments as pointwise actions;
5. compare the combined beyond-gap physical budget against the unchanged v14.444 sector budgets.

Accordingly, Lane A does **not** feed this witness into v14.406. Doing so would mix the earlier 912,383-row gap schema with the new 1,040,383-row off-support schema and violate v14.448/v14.452.

## Scope and next action

Original `C_S_32000`, the `3e-11` compact producer gate, the `3e-5` prior finite-plus-gap gate, and every other existing threshold remain unchanged. v14.354 and the global source/fresh-lift transport remain charged exactly once in their already-certified finite-plus-gap budget; v14.448 explicitly forbids charging them again in the new beyond-gap composition.

Lane A's next owned gate is the original-seed direct-middle split/action on these same 1,040,383 rows, followed by physical residual composition. The returned compact witness is now complete and no longer blocks that work.

No direct-middle residual pass, beyond-middle infinite residual bound, whole-residual pass, stationary closure, or infinite-capacity closure is claimed.

---

HANDOFF
target: external-audit, sandbox
type: complete-direct-middle-compact-return-freeze
parent: v14.471
status: open
action: independently replay the 40-entry manifest, verify complete sector coverage/seams and the two stitched buffer hashes; confirm the v14.448/v14.452 sequencing correction
deliverable: audit confirmation or precise correction before residual promotion
constraints: compact-only witness; do not infer original-seed action, physical residual, or infinite closure; preserve all thresholds
