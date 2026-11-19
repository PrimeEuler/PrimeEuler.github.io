# Cone Derivation Ledger v15.1227 — Lane A Suzuki R4 Placement Repair and 64-State Right Extension

**Date:** 2026-11-19 12:20 EST
**Track:** Lane A — original frozen Suzuki seed certification only
**Scope:** Additive deployment repair for v15.1217/v15.1223 plus a reproducible finite-radius R4 positive-polynomial certificate on 64 additional arcs

## Live state and audit acknowledgement

This entry ACKs the scheduled 2026-11-19 12:12 EST continue instruction exactly once and ACKs External Audit Round 615 (`5eba16e4002c2980e50dae70c12588c0cc8db183`, ledger v15.1225) exactly once. Live master was `f32fbcb3a0863326cdbf6d34ed5475b3259a97b8` when this gate was selected. Round 615 is the latest Suzuki audit; later commits were gravity-only and excluded. Global versions through v15.1226 were occupied, and repeated searches confirmed v15.1227 unused before the additive writes.

Round 615 independently replayed v15.1217 and v15.1223 bit-for-bit and confirmed their mathematics and union arithmetic, but flagged a deployment defect: their triplets were filed at `unified/discriminant-12-return/` rather than `unified/discriminant-12-return/research-notes/`, so the committed producers could not resolve their frozen dependency from a clean checkout.

## Additive placement repair

The original root-level files are untouched. Byte-identical copies of each producer, certificate, and manifest were added under `research-notes/`, where the producer's existing `HERE / SOURCE_NAME` lookup resolves the frozen v15.842 dependency and each manifest's relative paths resolve in place.

v15.1217 repair commits:

- producer `589e7e88d1706fc0c7b7c00651b2554e6d2e4d75`;
- certificate `f33e02edbac82fdeea65ddb5f4439f2acea5bd4b`;
- manifest `b31a00e575a20b22f5f3101e43659d4f75a07b4a`.

Their hashes remain producer `19c36118420c69d701fdce4e63daebce6780e720d11cee4964cecfda03943afb`, certificate `3f7b20f2720920dfb2538a6d2735757aeb0c7c0a5e1c4d046763b17ec1f8a2bb`, and manifest `62a07cfc061686fa4dd91a0361affc9b3431bea90d912bec02957d15acae07ef`.

v15.1223 repair commits:

- producer `4a936049c1ed111afdbdf7866b1781591ff140ba`;
- certificate `4c7661e0975d4e19d1fbd85e9101ebf00c1006c9`;
- manifest `8e83c1ec0b1f383474b25cb172ee967f641d8c46`.

Their hashes remain producer `e7372582460ca26803d4855a6834451e5a765d59823375b4578671b7c07e19d3`, certificate `e806d457b3188da237832e9f23592fb062f7ab58e2095cc8fa4462eb8e8bf30d`, and manifest `9bfd0cc9820b3ceefb652e820b279ed35a05ed95c8cd4e834c449cede367b0d8`.

## New exact gate

The new producer was filed correctly under `research-notes/` from the outset. Starting from a direct assembly at step 1024, it crosses steps 1025–1088 and arcs `{5034,...,5097}`, using exact localized support, outward binary64 arithmetic, and direct word-certificate rebasing every four transitions.

The certificate contains exactly 64 records:

- direction `+1`, arcs `{5034,...,5097}`, steps 1025–1088;
- 16 direct rebases at `{5034,5038,...,5094}`;
- exact update support at most 160 directed entries;
- maximum entry discrepancy against direct assembly `3.1086244689504383e-15`;
- maximum cumulative arithmetic enclosure `2.0840967156485934e-09`;
- maximum rebase arithmetic enclosure `1.9968089732525742e-10`;
- maximum sweep-minus-direct fourth-power bound `1.4511869039779413e-08`;
- maximum direct fourth root `3.920055647481403`;
- maximum propagated fourth root `3.9200556475097437`;
- maximum propagated positive-polynomial bound `236.139657243202 < 282.5761`;
- all 64 flags pass; `STATUS=R4_BLOCK_COVERAGE_PASS`.

Filed coverage is now `{3177,...,4008} union {4010,...,5097}`: `832 + 1,088 = 1,920` of 8,019 arcs, leaving 6,099 uncovered. Adjacency 5033/5034 was checked.

New artifacts:

- producer `lane_a_v15_1227_suzuki_r4_direct_restart_64_right_extension.py`, SHA-256 `571a89d54d8894b0095c9ae0324652685bc8dce4f761113850cda20afce19b04`, commit `5b6baf1c3c95955f1f5d0584113501a2d722df37`;
- certificate `lane_a_v15_1227_suzuki_r4_direct_restart_64_right_extension_certificate.json`, SHA-256 `ff5095b23b82edde937645d6df6d6992dd019b1cc0c255a3b828f846963ffb5b`, commit `738a8872c940a07388e3021ee144b71b0707fb6d`;
- manifest `lane_a_v15_1227_suzuki_r4_direct_restart_64_right_extension.sha256`, SHA-256 `18648f563e28274ac673b30d244764a9d5b1a60093346838d3f75d469c7ae9d0`, commit `f69aec20f9d2e9462544e2685acd5751039ce35f`.

Frozen dependency hashes remain v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`, v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`, and anchor-weight raw float64 bytes `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`. The first four manifest rows replayed successfully; neither producer nor certificate contains `ledger_version`.

## Strict boundary and audit handoff

This is a finite R4 resource tile and deployment correction only. It is not global `C4` or `C16`, not the required joint five-frequency cross-budget certificate, not full Suzuki closure, and not a full-K/source-native-`Phi`/whole-residual/stationary/capacity claim. Rank at most 160 is support bookkeeping, not a small-norm theorem; no eigsh sample or one-x probe is treated as an upper bound.

The exact blockers remain 6,099 uncovered R4 arcs and the absence of a rigorous all-arc two-sided R16 spectral certificate. External Audit should verify that the repaired v15.1217/v15.1223 triplets now replay from their committed `research-notes/` locations and replay v15.1227 bit-for-bit.
