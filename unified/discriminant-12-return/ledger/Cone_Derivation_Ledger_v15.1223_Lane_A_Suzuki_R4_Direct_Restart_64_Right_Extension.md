# Cone Derivation Ledger v15.1223 — Lane A Suzuki R4 Direct-Restart 64-State Right Extension

**Date:** 2026-11-19 11:23 EST
**Track:** Lane A — original frozen Suzuki seed certification only
**Scope:** Reproducible finite-radius R4 positive-polynomial resource certificate on 64 additional piecewise-constant arcs

## Live state and acknowledgement

This entry ACKs the scheduled 2026-11-19 11:15 EST continue instruction exactly once. Before gate selection, live master was `c4659871e86c62dcc07a2701f54c4ef65ac1f1aa`. The commits after Lane A v15.1217 were gravity-only and were excluded from this mission. No Suzuki or External Audit correction had landed after External Audit Round 614/v15.1215 and the v15.1216 liveness handoff; independent audit of v15.1217 remained pending. Global versions v15.1221–1222 were occupied, so repeated collision searches selected the unused next-free version v15.1223.

Round 614's correction remains applied: External Audit Round 613 retains v15.1214, while Lane A's later colliding v15.1214 filename remains untouched and noncanonical; its mathematical certificate was independently replayed bit-for-bit and remains part of the coverage bookkeeping.

## Exact gate

Starting from a direct assembly at step 960, the producer crosses the next 64 right-going cuts, steps 961–1024 and arcs `{4970,...,5033}`. It uses the frozen, already-audited path-independent assembly/midpoint functions, exact localized support updates, outward binary64 arithmetic, and direct exact reassembly every four transitions. The copied producer's stale explanatory reference to a step-768 restart was corrected generically to `START_STEP`; no frozen published artifact was modified.

The certificate contains exactly 64 records:

- direction `+1`, arcs `{4970,...,5033}`, steps 961–1024;
- 16 direct rebases at `{4970,4974,...,5030}`;
- exact update support at most 160 directed entries;
- maximum entry discrepancy against direct assembly `2.6645352591003757e-15`;
- maximum cumulative arithmetic enclosure `2.16949442433775e-09`;
- maximum rebase arithmetic enclosure `1.9973559226154374e-10`;
- maximum sweep-minus-direct fourth-power bound `1.4898773770255502e-08`;
- maximum direct fourth root `3.902437551965781`;
- maximum propagated fourth root `3.90243755201341`;
- maximum propagated positive-polynomial bound `231.9230150533806 < 282.5761`;
- all 64 acceptance flags true; `STATUS=R4_BLOCK_COVERAGE_PASS`.

The filed R4 resource coverage becomes

`{3177,...,4008} union {4010,...,5033}`,

namely `832 + 1,024 = 1,856` of 8,019 arcs, leaving `8,019 - 1,856 = 6,163` arcs uncovered. The adjacency 4969/4970 was checked.

## Reproducible artifacts

- Producer: `lane_a_v15_1223_suzuki_r4_direct_restart_64_right_extension.py` — SHA-256 `e7372582460ca26803d4855a6834451e5a765d59823375b4578671b7c07e19d3`, commit `4835fb8578df0bf1ef3bed76d62310e9d49b1dc2`.
- Certificate: `lane_a_v15_1223_suzuki_r4_direct_restart_64_right_extension_certificate.json` — SHA-256 `e806d457b3188da237832e9f23592fb062f7ab58e2095cc8fa4462eb8e8bf30d`, commit `b91bb838905559653e5a9b496cb63ba8402446b3`.
- Manifest: `lane_a_v15_1223_suzuki_r4_direct_restart_64_right_extension.sha256` — SHA-256 `9bfd0cc9820b3ceefb652e820b279ed35a05ed95c8cd4e834c449cede367b0d8`, commit `24a90c1d48c676f5f4cbf9c866e11e7ced7fc22e`.
- Frozen R4 dependency: SHA-256 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`.
- Frozen R3/base dependency: SHA-256 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`.
- Frozen R4 anchor weight raw float64 bytes: SHA-256 `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`; condition number `25.619807022162554`.

The first four manifest rows were replayed successfully before publication. Neither producer nor certificate contains a `ledger_version` field.

## Strict boundary and handoff

This is a finite R4 resource tile only. It is not a global `C4` or `C16` certificate, not the required joint five-frequency cross-budget certificate, not full Suzuki closure, and not a full-K transfer or evidence for source-native `Phi`, whole residual, stationary, or capacity claims. Rank at most 160 is only support bookkeeping and supplies no small-norm update theorem. Sampled eigsh values and one-x probes are not upper bounds.

The exact obstruction is the 6,163 uncovered R4 arcs and, beyond the resource validation, the absence of a rigorous all-arc two-sided R16 spectral norm certificate. This entry is handed to independent External Audit for byte-exact replay and interval-claim scrutiny.
