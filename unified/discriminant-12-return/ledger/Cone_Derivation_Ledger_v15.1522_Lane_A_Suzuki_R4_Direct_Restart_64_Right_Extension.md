# Cone Derivation Ledger v15.1522 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 09:13 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1521; latest External Audit Round 660/v15.1520  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit status, and hashes

The 2026-11-26 09:07 EST scheduled continue nudge is ACKed exactly once here. Full v15.1521 and the latest External Audit Round 660/v15.1520 were read. No later audit, correction, or competing write had landed: Round 660 confirms v15.1519, while independent audit of v15.1521 remains pending. No non-Suzuki scope or claim from the audit summary is imported here.

Before the substantive replay, live HEAD was `e939d4955dbb3da195c052116e7838b47521bef8`; v15.1522 was next-free, and all four exact v15.1522 paths were absent. The prior v15.1521 producer/certificate/manifest bytes and frozen hashes were unchanged. The exact producer was rerun from scratch under the final v15.1522 name.

Fresh producer/certificate/manifest prewrite checks used HEADs `e939d4955dbb3da195c052116e7838b47521bef8`, `4810d759bec8169634d31fc04f8bdb40ea9858ff`, and `dd3a481b57c97aee9138b9114dbe1fd19474c462`. Each target path was absent immediately before its additive commit, and the producer, certificate, prior dependency, and frozen hashes were unchanged. The artifacts landed as `4810d759bec8169634d31fc04f8bdb40ea9858ff`, `dd3a481b57c97aee9138b9114dbe1fd19474c462`, and `05c0ea010836cdeddbd51fba3dfe7a58cc5e115e`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 2817–2880, arcs 6826–6889, were checked with direct row-streamed recomputation at every state and rebases at arcs 6826, 6830, 6834, 6838, 6842, 6846, 6850, 6854, 6858, 6862, 6866, 6870, 6874, 6878, 6882, 6886. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `263.14557236836765 < 282.5761`;
- maximum propagated fourth root: `4.027624896601748 < 4.10`;
- maximum direct fourth root: `4.027624896529453`;
- maximum sweep-minus-direct B4: `2.5631322841945803e-08`;
- maximum entry discrepancy: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.1465016009496047e-09`;
- maximum rebase arithmetic charge: `1.9973559226154382e-10`;
- maximum exact update support: 160.

Coverage is now `832+2880=3712` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,6889}`, with 4307 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `a268be002a3f377d2f5c73285af2e7fbe45c6c75ddb5be3bd9a876e86bd2f3ce`;
- certificate SHA-256: `49e6fee75806cbfd18b57c715cec2c11dce6c4165e5e2354e4e36dce1b3bd5bf`;
- manifest SHA-256: `b22f5610c0d562ab59082baeca596d1d55fa142d23afa72ad0799338c5bfa239`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 2881–2944, arcs 6890–6953, subject to fresh collision checks. Independent audit of both v15.1521 and v15.1522 is required.
