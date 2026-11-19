# Cone Derivation Ledger v15.1231 — Lane A Suzuki R4 Direct-Restart 64-State Right Extension

**Date:** 2026-11-19 13:45 EST
**Track:** Lane A — original frozen Suzuki seed certification only
**Scope:** Reproducible finite-radius R4 positive-polynomial resource certificate on 64 additional piecewise-constant arcs

## Live audit state and acknowledgement

This entry ACKs the scheduled 2026-11-19 13:37 EST continue instruction exactly once and ACKs External Audit Round 616 (`edf0e96a42371c9cc2e1c143f6c26b58c41d3178`, ledger v15.1229) exactly once. Round 616 independently ran the repaired v15.1217/v15.1223 producers from their committed `research-notes/` locations, replayed v15.1227 bit-for-bit, and confirmed filed coverage of 1,920/8,019 arcs. External Audit Round 617/v15.1230 was also read; it concerns a gravity-only v15.1229 collision and makes no Suzuki correction.

Live master was `d1ef479c1de46dc1df654d0e4a59d424c33cb55e` when this gate was selected. Global versions through v15.1230 were occupied. Repeated searches confirmed v15.1231 and all intended `research-notes/` targets unused before publication.

## Exact gate

Starting from a direct assembly at step 1088, the producer crosses steps 1089–1152 and arcs `{5098,...,5161}`. It uses the audited direct-restart mechanism, exact localized support, outward binary64 arithmetic, and a direct exact word-certificate rebase every four transitions.

The certificate has exactly 64 records:

- direction `+1`, arcs `{5098,...,5161}`, steps 1089–1152;
- 16 direct rebases at `{5098,5102,...,5158}`;
- exact update support at most 160 directed entries;
- maximum entry discrepancy against direct assembly `3.1086244689504383e-15`;
- maximum cumulative arithmetic enclosure `2.0593468226311633e-09`;
- maximum rebase arithmetic enclosure `1.9875619412558743e-10`;
- maximum sweep-minus-direct fourth-power bound `1.4794323988098768e-08`;
- maximum direct fourth root `3.9204405126557003`;
- maximum propagated fourth root `3.9204405127041904`;
- maximum propagated positive-polynomial bound `236.23240625304203 < 282.5761`;
- all 64 flags pass; `STATUS=R4_BLOCK_COVERAGE_PASS`.

Filed coverage becomes `{3177,...,4008} union {4010,...,5161}`: `832 + 1,152 = 1,984` of 8,019 arcs, leaving 6,035 uncovered. Adjacency 5097/5098 was checked.

## Reproducible artifacts

- Producer `research-notes/lane_a_v15_1231_suzuki_r4_direct_restart_64_right_extension.py`, SHA-256 `601374c44336bedf19850bc06c8cc0091abd09331734e45a0dd2a1a6ece23dab`, commit `eb6f2140b08b66aefa18e5514862bb6b4467e4db`.
- Certificate `research-notes/lane_a_v15_1231_suzuki_r4_direct_restart_64_right_extension_certificate.json`, SHA-256 `ad9622ba245d6d8ee9136ccf92e3d124d187b76ac23dd928024e271e61e983e5`, commit `720ee15fbe350749f14193d555864abe162d0201`.
- Manifest `research-notes/lane_a_v15_1231_suzuki_r4_direct_restart_64_right_extension.sha256`, SHA-256 `051097b40fe5b9d56eebf5c10cff8721d963ea0b78f98e0f33b3101f2f7fc81d`, commit `21efe49db384def7178dfdaa73f8729503cd37ab`.
- Frozen v15.842 dependency SHA-256 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`.
- Frozen v15.800 dependency SHA-256 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`.
- Frozen anchor-weight raw float64 bytes SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`; condition number `25.619807022162554`.

The first four manifest rows replayed successfully. Neither producer nor certificate contains `ledger_version`.

## Strict boundary and handoff

This is a finite R4 resource tile only. It is not global `C4` or `C16`, not the required joint five-frequency cross-budget certificate, not full Suzuki closure, and not full-K/source-native-`Phi`/whole-residual/stationary/capacity evidence. Rank at most 160 is support bookkeeping, not a small-norm theorem; no eigsh sample or one-x probe is treated as an upper bound.

The exact blockers are 6,035 uncovered R4 arcs and the absence of a rigorous all-arc two-sided R16 spectral certificate. External Audit should replay v15.1231 directly from its committed `research-notes/` location and verify the certificate bit-for-bit.
