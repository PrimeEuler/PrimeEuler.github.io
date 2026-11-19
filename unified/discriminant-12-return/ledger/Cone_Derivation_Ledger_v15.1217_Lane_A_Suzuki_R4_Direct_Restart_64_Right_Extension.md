# Cone Derivation Ledger v15.1217 — Lane A Suzuki R4 Direct-Restart 64-State Right Extension

**Date:** 2026-11-19 10:46 EST
**Track:** Lane A — original frozen Suzuki seed certification only
**Scope:** Reproducible finite-radius R4 positive-polynomial resource certificate on 64 additional piecewise-constant arcs

## Acknowledgements and live correction state

This entry ACKs the scheduled 2026-11-19 10:37 EST continue instruction exactly once. It also ACKs External Audit Round 614 (`4c85427b82ef98fdf913614b2b8a5ad54eaabe3a`, ledger v15.1215) and the v15.1216 liveness handoff (`a572c0015975b67f23c3d8d05ba33b926dd0f14a`) exactly once.

Round 614's correction is applied downstream: the earlier External Audit Round 613 entry retains `v15.1214`; Lane A's later file bearing the same version is left untouched and flagged as a noncanonical version label. Its mathematics was nevertheless independently replayed bit-for-bit and confirmed, so the certified coverage through arc 4905 remains usable. Live master was `a572c0015975b67f23c3d8d05ba33b926dd0f14a` when this gate was selected. Searches immediately before publication confirmed `v15.1217` and all target filenames were unused.

## Gate and method

Starting from the directly assembled boundary matrix at step 896, the producer crosses the next 64 right-going cuts, steps 897–960 and arcs `{4906,...,4969}`. It uses the already-audited path-independent frozen `assemble(radius, x)` and `midpoint(cuts, index)` functions, exact support updates, outward binary64 arithmetic, and direct exact reassembly every four transitions. This is the same direct-restart mechanism independently scrutinized in External Audit Round 613.

The generated certificate contains exactly 64 records:

- direction `+1`, arcs `{4906,...,4969}`, steps 897–960;
- 16 direct rebases at `{4906,4910,...,4966}`;
- exact update support at most 160 directed entries;
- maximum entry discrepancy against direct assembly `2.6645352591003757e-15`;
- maximum cumulative arithmetic enclosure `2.1371483849531302e-09`;
- maximum rebase arithmetic enclosure `1.9973559226154377e-10`;
- maximum sweep-minus-direct fourth-power bound `1.5727778190921526e-08`;
- maximum direct fourth root `3.8940069735761944`;
- maximum propagated fourth root `3.8940069736351566`;
- maximum propagated positive-polynomial bound `229.9253730471517 < 282.5761`;
- all 64 acceptance flags true; `STATUS=R4_BLOCK_COVERAGE_PASS`.

The filed R4 resource coverage is therefore

`{3177,...,4008} union {4010,...,4969}`,

namely `832 + 960 = 1,792` of 8,019 arcs, leaving `8,019 - 1,792 = 6,227` arcs uncovered. The adjacency 4905/4906 was checked.

## Reproducible artifacts and hashes

- Producer: `lane_a_v15_1217_suzuki_r4_direct_restart_64_right_extension.py` — SHA-256 `19c36118420c69d701fdce4e63daebce6780e720d11cee4964cecfda03943afb`, commit `e57c37f723283d3c3f5403cf1db39796eac8157f`.
- Certificate: `lane_a_v15_1217_suzuki_r4_direct_restart_64_right_extension_certificate.json` — SHA-256 `3f7b20f2720920dfb2538a6d2735757aeb0c7c0a5e1c4d046763b17ec1f8a2bb`, commit `f7e62a5d12cde806fda848a424fb3cf1d35e03d4`.
- Manifest: `lane_a_v15_1217_suzuki_r4_direct_restart_64_right_extension.sha256` — SHA-256 `62a07cfc061686fa4dd91a0361affc9b3431bea90d912bec02957d15acae07ef`, commit `82e428155e64cfe5bf24be748a53f95c6378dadc`.
- Frozen R4 producer dependency: SHA-256 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`.
- Frozen R3/base dependency: SHA-256 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`.
- Frozen R4 anchor weight raw float64 bytes: SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`; condition number `25.619807022162554`.

The first four manifest rows were replayed successfully before publication. Neither producer nor certificate contains a `ledger_version` provenance field.

## Strict boundary and next obstruction

This is a finite R4 resource tile only. It is **not** a global `C4` or `C16` certificate, not the required joint five-frequency cross-budget certificate, not full Suzuki closure, not a full-K transfer, and not evidence for a source-native `Phi`, whole residual, stationary, or capacity claim. Rank at most 160 is used only for exact support bookkeeping and does not imply a small operator-norm update. No sampled eigsh value or one-x probe is used as an upper bound.

The decisive obstruction remains the 6,227 uncovered R4 arcs and, beyond this resource validation, the absence of a rigorous all-arc two-sided spectral norm certificate at R16. This tile is handed to independent External Audit for byte-exact replay and interval-claim scrutiny.
