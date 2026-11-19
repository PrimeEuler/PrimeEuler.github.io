# Cone Derivation Ledger v15.1233 — Lane A Suzuki R4 Direct-Restart 64-State Right Extension

**Date:** 2026-11-19 14:45 EST
**Track:** Lane A — original frozen Suzuki seed certification only
**Scope:** Reproducible finite-radius R4 positive-polynomial resource certificate on 64 additional piecewise-constant arcs

## Live audit state and acknowledgement

This entry ACKs the scheduled 2026-11-19 14:36 EST continue instruction exactly once and ACKs External Audit Round 618 (`992f505a03f7770bf958d0b51c93d86640cc8e5f`, ledger v15.1232) exactly once. Round 618 independently re-executed the correctly filed v15.1231 producer, reproduced its certificate bit-for-bit, and confirmed the coverage union `{3177,...,4008} union {4010,...,5161}` has 1,984 arcs and 6,035 uncovered. It makes no correction to the Suzuki argument.

Live master was `992f505a03f7770bf958d0b51c93d86640cc8e5f` when this gate was selected. Global versions through v15.1232 were occupied. Repeated searches confirmed v15.1233 and every intended `research-notes/` target unused immediately before publication.

## Exact gate

Starting from an independently assembled state at step 1152, the producer crosses steps 1153–1216 and arcs `{5162,...,5225}`. It uses the audited direct-restart mechanism, exact localized support, outward binary64 arithmetic, and a direct exact word-certificate rebase every four transitions.

The certificate has exactly 64 records:

- direction `+1`, arcs `{5162,...,5225}`, steps 1153–1216;
- 16 direct rebases at `{5162,5166,...,5222}`;
- exact update support at most 160 directed entries;
- maximum entry discrepancy against direct assembly `3.1086244689504383e-15`;
- maximum cumulative arithmetic enclosure `2.0410489163709794e-09`;
- maximum rebase arithmetic enclosure `1.997355922615438e-10`;
- maximum sweep-minus-direct fourth-power bound `1.4986682117523742e-08`;
- maximum direct fourth root `3.9162621301155625`;
- maximum propagated fourth root `3.916262130161367`;
- maximum propagated positive-polynomial bound `235.22691469059788 < 282.5761`;
- all 64 flags pass; `STATUS=R4_BLOCK_COVERAGE_PASS`.

Filed coverage becomes `{3177,...,4008} union {4010,...,5225}`: `832 + 1,216 = 2,048` of 8,019 arcs, leaving 5,971 uncovered. Adjacency 5161/5162 was checked.

## Reproducible artifacts

- Producer `research-notes/lane_a_v15_1233_suzuki_r4_direct_restart_64_right_extension.py`, SHA-256 `94ebb1800748960ca9f570712f238397a39412a136f2b9c7328be1ef9ea0bec6`, commit `d51d4c694d18020ef2d0ae65571870769fad08fd`.
- Certificate `research-notes/lane_a_v15_1233_suzuki_r4_direct_restart_64_right_extension_certificate.json`, SHA-256 `bf10e8ad7d09b93f835e1ffad0669e00c03239452cc426e5676299521d1fe5e5`, commit `29a62e18bd9fd7b45599ccbcc67ad353c7d763cb`.
- Manifest `research-notes/lane_a_v15_1233_suzuki_r4_direct_restart_64_right_extension.sha256`, SHA-256 `6629963b8ab6dc12f2dc15577918d008375eb6fd492b249fb59be0a5a370ad06`, commit `a64d75581036bf29bea49a895dfb2938f2041633`.
- Frozen v15.842 dependency SHA-256 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`.
- Frozen v15.800 dependency SHA-256 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`.
- Frozen anchor-weight raw float64 bytes SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`; condition number `25.619807022162554`.

The first four manifest rows replayed successfully. Neither producer nor certificate contains `ledger_version`.

## Strict boundary and handoff

This is a finite R4 resource tile only. It is not global `C4` or `C16`, not the required joint five-frequency cross-budget certificate, not full Suzuki closure, and not full-K/source-native-`Phi`/whole-residual/stationary/capacity evidence. Rank at most 160 is support bookkeeping, not a small-norm theorem; no eigsh sample or one-x probe is treated as an upper bound.

The exact blockers are 5,971 uncovered R4 arcs and the absence of a rigorous all-arc two-sided R16 spectral certificate. External Audit should replay v15.1233 directly from its committed `research-notes/` location and verify the certificate bit-for-bit.
