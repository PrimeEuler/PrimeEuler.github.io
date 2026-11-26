# Cone Derivation Ledger v15.1530 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 13:12 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1528; External Audit Round 664/v15.1529  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit, and hashes

The 2026-11-26 13:05 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 664/v15.1529 is ACKed exactly once here. Full v15.1528 and Round 664 were read. Round 664 independently replayed v15.1528 bit-for-bit with no correction. No non-Suzuki scope or claim from the audit summary is imported here.

Before the substantive replay, live HEAD was `88fac0235ca6cb5a5e4b7a21e9e27e888e06fa33`; v15.1529 was occupied by Round 664, v15.1530 was next-free, and all four exact v15.1530 paths were absent. The audited v15.1528 producer/certificate/manifest bytes and frozen hashes were unchanged. The exact producer was rerun from scratch under the final v15.1530 name.

Fresh producer/certificate/manifest prewrite checks used HEADs `88fac0235ca6cb5a5e4b7a21e9e27e888e06fa33`, `5dd7f567ecf276b04b745ee0a16f5caaf2ea3525`, and `9b1fb9019e89f6501835c83e6a56b87445694cbb`. Each target path was absent immediately before its additive commit, and the producer, certificate, audited prior dependency, and frozen hashes were unchanged. The artifacts landed as `5dd7f567ecf276b04b745ee0a16f5caaf2ea3525`, `9b1fb9019e89f6501835c83e6a56b87445694cbb`, and `95bad525b134a0b8e0e701a578ccde9f12a68c6b`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 3073–3136, arcs 7082–7145, were checked with direct row-streamed recomputation at every state and rebases at arcs 7082, 7086, 7090, 7094, 7098, 7102, 7106, 7110, 7114, 7118, 7122, 7126, 7130, 7134, 7138, 7142. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `254.2757540348494 < 282.5761`;
- maximum propagated fourth root: `3.9932475852685614 < 4.10`;
- maximum direct fourth root: `3.9932475852041858`;
- maximum sweep-minus-direct B4: `3.634974632404919e-08`;
- maximum entry discrepancy: `2.220446049250313e-15`;
- maximum cumulative arithmetic charge: `1.9624689743884317e-09`;
- maximum rebase arithmetic charge: `1.996808973252574e-10`;
- maximum exact update support: 160.

Coverage is now `832+3136=3968` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,7145}`, with 4051 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `457c67426cdfd0ef372595d714e82bd655c8ce6bf6d37f7cbd5dcaaeb69f573e`;
- certificate SHA-256: `f83bef9feb540685c8f884df0e26211d977cc990e083571f6e8af3e1f9e1151f`;
- manifest SHA-256: `04be92f3000aad6cd5e27cc60920d8f43993526e5bb0ddc2d1015a8d87057923`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 3137–3200, arcs 7146–7209, subject to fresh collision checks. Independent audit of v15.1530 is required.
