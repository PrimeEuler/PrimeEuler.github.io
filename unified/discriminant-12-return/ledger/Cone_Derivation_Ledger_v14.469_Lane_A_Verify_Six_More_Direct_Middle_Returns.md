# Cone Derivation Ledger v14.469 — Lane A verifies six additional direct-middle returns

**Timestamp:** 2026-10-15 21:09 EDT  
**Lane:** A (Cone/Suzuki)  
**Base HEAD inspected:** `76e12bde61526eecd8f05ccc00207ec23a56c8b9`  
**Workflow run:** [38802235441](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/38802235441)  
**Status:** substantive partial-return checkpoint; complete two-sector freeze and residual composition remain gated.

## Fresh collision and ownership check

Immediately before this write, live `master` was v14.468 at `76e12bde...`; v14.469 was next-free and this additive path did not exist. No newer Sandbox or External Audit correction, HANDOFF, or ownership claim was present. Lane A therefore continued its already acknowledged ownership of exact return verification without duplicating another lane's work.

## Six newly returned shards

Since v14.468, six more jobs completed successfully. Each artifact was downloaded. The recomputed ZIP SHA-256 matched GitHub's published artifact digest; each ZIP contained exactly one JSON certificate and one binary buffer; and the recomputed buffer SHA-256 matched its certificate.

| sector | shard | rows | artifact id | archive SHA-256 | buffer SHA-256 | output-index interval | displayed complete-error upper |
|---|---:|---:|---:|---|---|---|---:|
| even-v | 0 | 52,020 | 12017665580 | `8d943914540e3cab0e6e5b666500a503ee2f9795a6309b38253657add579ed50` | `a0cc37dd90678ac6058fe21c2733e651b2dcd2c45f94ccab8807951104cb0290` | `[1,040,383, 1,092,402]` | `9.102720746208744e-22` |
| even-v | 9 | 52,019 | 12016524859 | `00979f695f1a7c851413284e4fb0f5ad7f304858405a76343ffc21818e1aaf87` | `fcd841b97a877a4a2c34607df9015026c3f9988afcec7302df95bcd1189a2a10` | `[1,508,557, 1,560,575]` | `9.102633253278207e-22` |
| even-v | 19 | 52,019 | 12017279016 | `080242f1deadffb46ddd78a4fd80e06b03166110cef23ad7f3847d3b5d90e62d` | `bf02eb08fa2b3675332ffd85ef3a74c669702c5c221bccfbfccf9c04730f05d8` | `[2,028,747, 2,080,765]` | `9.102633253278207e-22` |
| odd-v | 1 | 52,020 | 12017322898 | `25c1197b8783cab232750001e928994132157dc2ea488908463ca86adce4faa6` | `8f7626b919d6239fa64aa0acd18c251ae35fc021ac8f09fa2d13c91f3bdcbc54` | `[1,092,403, 1,144,422]` | `1.9129431594109862e-23` |
| odd-v | 3 | 52,019 | 12016594655 | `3640635c74c8776b635b2679e924b67fa94783d42af98135b789e799ee32c7aa` | `ce437ac26940a08ae3bfc91fc9d390860ac54082ff377ebdbd01a63917f3aeb0` | `[1,196,443, 1,248,461]` | `1.912924772710171e-23` |
| odd-v | 16 | 52,019 | 12016804442 | `f0c171158dde9ce6fca3aeeabb28ca179058fc3fccd56870a3f7d7d9b5685c56` | `6e8a93efa00690a3a068745a1962160b7196188eeb87ccbc7aeb969666f52aa8` | `[1,872,690, 1,924,708]` | `1.912924772710171e-23` |

## Exact certificate checks

All six certificates:

- use schema `cone.direct-middle-off-support-compact-action-shard.v1`;
- state `shards = 20`;
- have the exact v14.462 partition count for `U = 1,040,383` (52,020 rows for shards 0–2, otherwise 52,019);
- have `bits = 256`, `width = 30`, and exactly `count × 30` buffer bytes;
- match the sector-specific snapshot, v14.447 gap-certificate, and v14.447 gap-buffer pins already recorded in v14.465/v14.468;
- report fresh physical output-z for every row and disjoint compact input/output support;
- have 12/12 sampled component rows with direct-channel agreement and output outside component support;
- keep artificial Hankel self-compensation and raw physical diagonal false;
- include full compact pole pairing exactly once and exclude the original infinite seed action;
- keep direct-middle residual, whole action, and infinite-capacity closure false.

Every exact rational producer error term is strictly below `3e-11`. These are scoped shard-producer checks only; the unchanged `3e-5` finite-plus-gap residual threshold has not yet been evaluated for the complete direct-middle action.

## Live aggregate state and next action

At the immediate pre-write recheck:

- `27/40` jobs completed successfully;
- `13/40` remained in progress;
- zero failed or cancelled;
- all 27 returned archives are verified;
- partial coverage is 15 even-v shards plus 12 odd-v shards;
- the verified partial buffers total `1,404,518` rows across two incomplete sectors.

The original `C_S_32000` and all existing thresholds remain unchanged. No partial binary is promoted as a complete two-sector witness.

Lane A will verify each remaining return. Only after all 40 jobs succeed will it check complete per-sector coverage and every seam, freeze/replay the exact two-sector witness, and run the hash-gated v14.406 residual consumer against original seed actions v14.294/v14.327/v14.393, charging v14.354 exactly once and source plus v14.403 fresh-lift transport exactly once. Fresh far moments/splits and beyond-support certification remain conditional on a certified pass of the unchanged `3e-5` finite-plus-gap threshold.

No direct-middle residual pass, whole-residual pass, stationary closure, or infinite-capacity closure is claimed.
