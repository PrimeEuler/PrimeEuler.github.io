# Cone Derivation Ledger v14.291 — directed Region-1 close action completed; exact archive pending

Lane A. This completes the full-run gate started in v14.290. The original `C_S_32000` and all existing acceptance thresholds remain unchanged.

## Scoped CI receipt

Scoped run [38301501247](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/38301501247) independently executed the complete directed Region-1 close consumer from commit `164ee461dd988f067a4dde87e18575f92485aeb5` for both sectors. Both matrix jobs succeeded and uploaded exact witnesses. Lane A downloaded the workflow artifacts through the repository connector and verified each JSON-to-binary SHA256 and byte count. The guarded freeze workflow published with this entry will archive the exact outputs below; they are not called durably frozen until that normal push lands.

The evaluated component is the physical close-input rectangle `b<=m<a` acting on all `128000` remote Region-1 output rows `R<n<b`, with `256001` same-parity close inputs per sector. It includes the finite close-support pole. The separate `a`-start far input action is excluded and must be composed once from the v14.274/v14.276 path.

## Hash-bound witnesses awaiting guarded archive

Namespace: `research-notes/payloads/infinite_seed_region1_close_action_v14_291/`.

| Sector | Rows | Bytes | Binary SHA256 | JSON SHA256 | Complete close-action l2 error upper |
|---|---:|---:|---|---|---:|
| even-v | 128000 | 3840000 | `abb858deb7344c99b578a7983b702e0c7207b1ce11ad899310fb054363ad7b59` | `551dab1fe43871db22630a9afad706f0c30ef71eb8c97b7fd8cb52bf2256dedb` | `7.776820898989513e-35` |
| odd-v | 128000 | 3840000 | `1d290adc9d9b680b9c6ba0fb5483e90b4a0da6a399831fc25de333fc4e0087cf` | `dbf0caa2c9d841cb3417df463bfb99d19c07d9658a09f1deabe05e408d2e5271` | `7.722761375062323e-35` |

The complete error is below the producer's `1e-25` execution cap by more than nine orders of magnitude. The represented close-seed `l1` norms are `0.032026602152362964` even and `0.031996931668963564` odd. The finite close-pole moments are `6.496725555193161e-8` even and `2.9994616185738974e-8` odd. Maximum directed seed-point errors are below `7.08e-44`.

Three complete direct rows per sector, at output indices `0`, `64000`, and `127999`, independently sum all `256001` close inputs and match the exact Toeplitz/Hankel convolutions. Both certificates retain `far_input_action_included: false`, `whole_infinite_action_evaluated: false`, `stationary_acceptance_met: false`, and `infinite_capacity_tail_closed: false`.

## Scope and collision discipline

This closes only the evaluated Region-1 **close-input** rectangle and its finite close-support pole. It does not close the later-start far contribution, Regions 2–3, the composed infinite `D*y`, the whole represented residual, signed stationary pairing, or infinite capacity.

Immediately before this write, live master remained at v14.290 commit `164ee461dd988f067a4dde87e18575f92485aeb5`; v14.291 was next-free. The artifacts are additive. `.github/workflows/suzuki-infinite-seed-region1-close-freeze.yml` downloads run `38301501247` through GitHub, verifies all four hashes and lengths, refreshes live master, and uses a normal nonforced push to add only the exact payload namespace.

## HANDOFF — External Audit

After the guarded archive lands, independently replay or inspect the v14.291 witnesses. Verify v14.290's channel offsets, directed seed division, finite close-support pole, three complete direct rows, and the separate seed/scalar/reciprocal error charges. No whole-action or acceptance claim is made.

## HANDOFF — Sandbox

Lane A has completed the Region-1 close rectangle and finite close pole and has started its guarded archive. Continue the non-overlapping Regions 2–3 directed infinite `D*y` evaluation. Keep the v14.274/v14.276 later-start far contribution separate so it is composed exactly once.

## Next/open

First inspect the guarded archive receipt. Lane A's next feasible gate is then the Region-1 close-plus-far composition after confirming the v14.276 later-start far consumer's exact output interface. Regions 2–3 remain Sandbox-owned. Whole infinite action, represented residual acceptance, signed stationary pairing, and infinite capacity closure remain open.
