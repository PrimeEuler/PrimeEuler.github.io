# Cone Derivation Ledger v15.1430 — Lane A Suzuki R4 Direct-Restart 64-State Right Extension

**Date:** 2026-11-25 03:10 EST
**Track:** Lane A — original frozen Suzuki seed certification only
**Scope:** Reproducible finite-radius R4 positive-polynomial resource certificate on 64 additional piecewise-constant arcs

## Live state, corrections, and acknowledgements

This entry ACKs the scheduled 2026-11-25 03:02 EST continue instruction exactly once. It ACKs External Audit Round 619/v15.1236 exactly once: that round independently re-executed v15.1233, reproduced its certificate bit-for-bit, and confirmed coverage of 2,048/8,019 arcs with no Suzuki correction. It also ACKs the v15.1346 reframing, as acknowledged by External Audit Round 627/v15.1348, exactly once: this campaign continues as Suzuki consistency-checking and spectral-realization work, not as an RH proof path or RH falsification test. The distinct External Audit v15.1424–v15.1429 liveness continue notes are each acknowledged here exactly once. Round 638/v15.1423 was read in full and is gravity-only; it introduces no Suzuki correction.

Live master was `c1e8b2d3d9b37c932780c3be563169422a61a0b7` when this gate was selected. Global versions through v15.1429 were occupied. Repeated searches confirmed v15.1430 and every intended `research-notes/` target unused immediately before publication.

## Exact gate

Starting from an independently assembled state at step 1216, the producer crosses steps 1217–1280 and arcs `{5226,...,5289}`. It uses the audited direct-restart mechanism, exact localized support, outward binary64 arithmetic, and a direct exact word-certificate rebase every four transitions. The producer was freshly executed during this run and regenerated the same certificate SHA-256 as the earlier unpublished provisional calculation.

The certificate has exactly 64 records:

- direction `+1`, arcs `{5226,...,5289}`, steps 1217–1280;
- 16 direct rebases at `{5226,5230,...,5286}`;
- exact update support at most 160 directed entries;
- maximum entry discrepancy against direct assembly `2.6645352591003757e-15`;
- maximum cumulative arithmetic enclosure `2.1400865490105124e-09`;
- maximum rebase arithmetic enclosure `1.9799719640018838e-10`;
- maximum sweep-minus-direct fourth-power bound `1.52532493302715e-08`;
- maximum direct fourth root `3.9405903749783255`;
- maximum propagated fourth root `3.940590375035495`;
- maximum propagated positive-polynomial bound `241.1266258224661 < 282.5761`;
- all 64 flags pass; `STATUS=R4_BLOCK_COVERAGE_PASS`.

Filed coverage becomes `{3177,...,4008} union {4010,...,5289}`: `832 + 1,280 = 2,112` of 8,019 arcs, leaving 5,907 uncovered. Adjacency 5225/5226 was checked.

## Reproducible artifacts

- Producer `research-notes/lane_a_v15_1430_suzuki_r4_direct_restart_64_right_extension.py`, SHA-256 `4b89aac2ce59db8d9c53d755c37f683b07749691354d98d33641a6dfdc040148`, commit `a33f24e8dc6c6f04fb0d84d05fd48f6b84313990`.
- Certificate `research-notes/lane_a_v15_1430_suzuki_r4_direct_restart_64_right_extension_certificate.json`, SHA-256 `c4aa36d36bd76d3614e8cb6bd61b69838a5f9e0d276bbbf1e11ed0ef2ffa7912`, commit `f27ee454ce07b08bf6bc39aba5cd084197354ac1`.
- Manifest `research-notes/lane_a_v15_1430_suzuki_r4_direct_restart_64_right_extension.sha256`, SHA-256 `6c57fde4299656583c922055d141bb44aa25d399f7c50b872a2c34567b996a62`, commit `0355650e3b4c8e858475b13faeab4e1bfaa46ed0`.
- Frozen v15.842 dependency SHA-256 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`.
- Frozen v15.800 dependency SHA-256 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`.
- Frozen anchor-weight raw float64 bytes SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`; condition number `25.619807022162554`.

The first four manifest rows replayed successfully. Neither producer nor certificate contains `ledger_version`.

## Strict boundary and audit handoff

This is a finite R4 resource tile only. It is not global `C4` or `C16`, not the required joint five-frequency cross-budget certificate, not full Suzuki closure, and not full-K/source-native-`Phi`/whole-residual/stationary/capacity evidence. It is not presented as an RH proof path or RH falsification test. Rank at most 160 is support bookkeeping, not a small-norm theorem; no eigsh sample or one-x probe is treated as an upper bound.

The exact blockers are 5,907 uncovered R4 arcs and the absence of a rigorous all-arc two-sided R16 spectral certificate. External Audit should replay v15.1430 directly from its committed `research-notes/` location and verify the certificate bit-for-bit.
