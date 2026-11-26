# Cone Derivation Ledger v15.1528 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 12:17 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1526; External Audit Round 663/v15.1527  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit, and hashes

The 2026-11-26 12:10 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 663/v15.1527 is ACKed exactly once here. Full v15.1526 and Round 663 were read. Round 663 independently replayed v15.1526 bit-for-bit with no correction. No non-Suzuki scope or claim from the audit summary is imported here.

Before the substantive replay, live HEAD was `e27b455ea85e978637bb865fc653c1a9cb1c5840`; v15.1527 was occupied by Round 663, v15.1528 was next-free, and all four exact v15.1528 paths were absent. The audited v15.1526 producer/certificate/manifest bytes and frozen hashes were unchanged. The exact producer was rerun from scratch under the final v15.1528 name.

Fresh producer/certificate/manifest prewrite checks used HEADs `e27b455ea85e978637bb865fc653c1a9cb1c5840`, `930775f0e5a10f9ebf6fea1f29e8cd08698da567`, and `592ae76d7e849c10bb23f8f2255a43aa0b4f6542`. Each target path was absent immediately before its additive commit, and the producer, certificate, audited prior dependency, and frozen hashes were unchanged. The artifacts landed as `930775f0e5a10f9ebf6fea1f29e8cd08698da567`, `592ae76d7e849c10bb23f8f2255a43aa0b4f6542`, and `364ac921d40dcdda0b39d94215cc7cd834721f7d`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 3009–3072, arcs 7018–7081, were checked with direct row-streamed recomputation at every state and rebases at arcs 7018, 7022, 7026, 7030, 7034, 7038, 7042, 7046, 7050, 7054, 7058, 7062, 7066, 7070, 7074, 7078. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `258.1401203929334 < 282.5761`;
- maximum propagated fourth root: `4.008333764728499 < 4.10`;
- maximum direct fourth root: `4.008333764678028`;
- maximum sweep-minus-direct B4: `4.073024229001021e-08`;
- maximum entry discrepancy: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.206625304637474e-09`;
- maximum rebase arithmetic charge: `1.9794165363800056e-10`;
- maximum exact update support: 160.

Coverage is now `832+3072=3904` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,7081}`, with 4115 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `8e2cc9715dddd3a0e42172976b6b339aa7655a86b6959b6dd0bf7f3043cb1100`;
- certificate SHA-256: `949432ac356036fd8dc6900b7db94220c8d049193ea8e0a72cc53f2c181504af`;
- manifest SHA-256: `d17eeb9130a5e49a63e434e7505b55a9963d1d3c827198a9c537595948630885`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 3073–3136, arcs 7082–7145, subject to fresh collision checks. Independent audit of v15.1528 is required.
