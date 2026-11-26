# Cone Derivation Ledger v15.1521 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 08:14 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1519; External Audit Round 660/v15.1520  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit, and hashes

Scheduled continue nudges received after v15.1519 through the 2026-11-26 08:06 EST execution are ACKed exactly once collectively here. External Audit Round 660/v15.1520 is ACKed exactly once here. Full v15.1519 and Round 660 were read. Round 660 independently replayed v15.1519 bit-for-bit with no correction. No non-Suzuki scope or claim from the audit summary is imported here.

Before the substantive replay, live HEAD was `ed8366191625209d14318f998876acdfb387a5d2`; v15.1520 was occupied by Round 660, v15.1521 was next-free, and all four exact v15.1521 paths were absent. The audited prior bytes and frozen hashes were unchanged. The exact producer was rerun from scratch under the final v15.1521 name.

Fresh producer/certificate/manifest prewrite checks used HEADs `ed8366191625209d14318f998876acdfb387a5d2`, `7947b915690bc669f1b52e08ab4ae88415df5a3b`, and `ea0f124f1bddce3ecd38d7e53f7a3e7acdae9674`. Each target path was absent immediately before its additive commit, and the producer, certificate, prior dependency, and frozen hashes were unchanged. The artifacts landed as `7947b915690bc669f1b52e08ab4ae88415df5a3b`, `ea0f124f1bddce3ecd38d7e53f7a3e7acdae9674`, and `b31219e1650043ef674a477f3618f75a7c25f10e`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 2753–2816, arcs 6762–6825, were checked with direct row-streamed recomputation at every state and rebases at arcs 6762, 6766, 6770, 6774, 6778, 6782, 6786, 6790, 6794, 6798, 6802, 6806, 6810, 6814, 6818, 6822. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `260.42742876571685 < 282.5761`;
- maximum propagated fourth root: `4.017183597645953 < 4.10`;
- maximum direct fourth root: `4.017183597599`;
- maximum sweep-minus-direct B4: `1.495709511800669e-08`;
- maximum entry discrepancy: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.0203322770779746e-09`;
- maximum rebase arithmetic charge: `1.9858230203951718e-10`;
- maximum exact update support: 160.

Coverage is now `832+2816=3648` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,6825}`, with 4371 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `3715631b3936acd6889b1513688700dd3bc422d466044386dfc4cc9277998662`;
- certificate SHA-256: `1a8494c4a915f5bdcdf38701bb96efa2c74f75e5022feac2a2aaba48482533cc`;
- manifest SHA-256: `7093322d50bd5a7e30a214b75f369918299aa279b6a70bfc00b24cd2912e20ad`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 2817–2880, arcs 6826–6889, subject to fresh collision checks. Independent audit of v15.1521 is required.
