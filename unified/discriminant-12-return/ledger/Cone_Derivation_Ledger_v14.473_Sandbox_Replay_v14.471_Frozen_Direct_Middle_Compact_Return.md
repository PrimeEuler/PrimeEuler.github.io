# Cone Derivation Ledger v14.473 — Sandbox replay of the v14.471 frozen direct-middle compact return: all checks pass; v14.471 HANDOFF (sandbox arm) CLOSED

**Timestamp:** 2026-10-15 (EDT evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.471 (freeze + HANDOFF), v14.472 (Audit R284), v14.448, v14.452, v14.462, v14.465, v14.470.
**Status:** sandbox HANDOFF-ACK / independent replay. The frozen compact-only witness is byte-exact as recorded. No residual, seed-action, or closure value is asserted.

## What was done

In response to the v14.471 HANDOFF (target: external-audit, sandbox), the sandbox independently replayed the frozen return from primary sources, without trusting any ledger table: the frozen manifest was fetched from `unified/discriminant-12-return/payloads/direct_middle_compact_action_v14_471/return-manifest.json`, and all 40 artifact archives of workflow run 38802235441 were downloaded fresh from the GitHub Actions API and verified from raw bytes. Audit R284 (v14.472) has separately closed the audit arm of the same handoff; this entry closes the sandbox arm.

## Results — PASS on every check group, no defect

1. **Manifest integrity.** Fetched manifest is 34,070 bytes, SHA-256 `c914bed9d0b1bad8f57b46fb2bbaa2f324c3013100a0c7ae9944fa6fb46cb16a`; its recomputed git blob SHA-1 is `2a63ee15f14284e8e3457a8858414e8ed16d0754`, exactly the frozen blob id recorded in v14.471. Schema `cone.direct-middle-off-support-compact-action-return-manifest.v1`; header U = 1,040,383, bits = 256, width = 30, run id 38802235441; scope flags (direct-middle residual / whole action / infinite-capacity tail) all false.

2. **Per-shard verification, 40/40.** For every shard: archive SHA-256, certificate SHA-256, and buffer SHA-256 all equal the manifest; each archive contains exactly the certificate + buffer pair; certificate schema `cone.direct-middle-off-support-compact-action-shard.v1`; (sector, shard) unique with shards 0–19 per sector; bits = 256, width = 30, buffer bytes = rows × 30; certificate first/last indices equal the manifest; the v14.462 partition reproduces exactly (52,020 rows for shards 0–2, 52,019 for shards 3–19; first index = 1,040,383 + 52,019·shard + min(shard, 3)); the three input pins per certificate are uniform within each sector and identical to the six values recorded in v14.465; scope flags correct in every certificate (fresh output-z true, support disjoint true, artificial Hankel self-compensation false, raw physical diagonal false, pole pairing once true, original seed excluded false); all 12 sampled direct-component rows per shard match with output outside component support.

3. **Coverage and seams.** From the certificates themselves, each sector tiles output indices [1,040,383, 2,080,765] exactly: all 19 seams per sector satisfy last(s) + 1 = first(s+1); row sums 1,040,383 per sector; no gaps, no overlaps. The manifest's per-sector summary blocks match the recomputation.

4. **Stitched buffers.** Concatenating the raw buffers per sector in shard order 0…19 (31,211,490 bytes each) recomputes SHA-256 even-v `e9f4e532af901a8e5c2ed87f14b9b1b7fafa506c8d68b70bd5f8a486bf8e204e` and odd-v `1fb4be01c98d37b6e88a2097f0eadeb630556e6ed966f0bfe65e52f9acd0e0e7` — identical to the frozen manifest fields and to v14.471. The stitched buffers are retained in the sandbox workspace for the v14.448 composition stage.

5. **Producer error gate.** All 40 displayed complete error uppers are < 3e-11, and all 40 exact rational error uppers (parsed as Fractions from the certificates) are also < 3e-11; each displayed value equals the float of its exact rational (no understated display). True maximum 9.102720746208744e-22 (even-v shards 0–2), exactly the v14.471 claim, ~11 orders under the gate.

6. **Sequencing correction — confirmed from primary sources.** The 1,040,383-row return is not consumable by the v14.406 consumer: `research-notes/suzuki_gap_extended_residual_composition.py` sets COUNT = 392,192 + 520,191 = 912,383 and asserts `spec["count"] == COUNT` plus a `gap_extended_compact_output_rows_evaluated` certificate key that the direct-middle shard certificates do not carry; the v14.405 producer's block ends exactly at the 1,040,383 boundary where the direct-middle block begins (adjacent, disjoint row blocks); v14.448 specifies the direct-middle range as indices U..2U−1 with U = 1,040,383. Composition proceeds under the v14.448 contract: bare source − compact − original seed on the direct-middle range, with v14.354 and the v14.403 transport each charged exactly once in the prior budget and never re-charged.

## Scope

This replay verifies the compact-only freeze and the sequencing correction only. It asserts nothing about the original infinite-seed action on the direct-middle range, the direct-middle physical residual, the beyond-middle remainder, or any whole-residual/stationary/capacity closure — none was evaluated here. All thresholds unchanged.

## Handoff disposition

The v14.471 HANDOFF's sandbox arm is satisfied and CLOSED by this entry (the audit arm was closed by R284/v14.472). Sandbox next steps under the already-open v14.448 execution gate: certified original-seed action on the same 1,040,383-row range (bank/tail split at T2 = 8,323,063/8,323,064, moments already frozen), the beyond-middle far bound, and the residual composition against the v14.444 budgets.
