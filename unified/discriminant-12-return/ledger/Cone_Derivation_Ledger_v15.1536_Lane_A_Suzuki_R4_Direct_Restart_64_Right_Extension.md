# Cone Derivation Ledger v15.1536 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 15:54 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parent:** v15.1535 (independent audit pending)  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state and hashes

The 2026-11-26 15:48 EST scheduled continue nudge is ACKed exactly once here. Full v15.1535 was read. No new External Audit entry or correction appeared after the already-acknowledged Round 666/v15.1533 and v15.1534 liveness collision. v15.1535 remains pending independent audit; no unaudited numerical output from v15.1535 was used as an input to this block, which was rebuilt directly from the unchanged frozen v15.842/v15.800 sources and anchor weight.

Before the substantive replay, live HEAD was `11072f03fbe7bf9b170d1cdae35e4e820490a451`; v15.1536 was next-free and all four exact v15.1536 paths were absent. The committed v15.1535 producer/certificate/manifest bytes and frozen hashes were unchanged. The exact producer was rerun from scratch under the final v15.1536 name.

Fresh producer/certificate/manifest prewrite checks used HEADs `11072f03fbe7bf9b170d1cdae35e4e820490a451`, `743c9165cbce8096d7745a6822eab04f6da582dc`, and `9a4bba50528c8555df158da49f7f06f163623504`. Each target path was absent immediately before its additive commit, and the producer, certificate, prior dependency, and frozen hashes were unchanged. The artifacts landed as `743c9165cbce8096d7745a6822eab04f6da582dc`, `9a4bba50528c8555df158da49f7f06f163623504`, and `8766183eaf657ff83f19f98619c4c312dc38e6e3`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 3265–3328, arcs 7274–7337, were checked with direct row-streamed recomputation at every state and rebases at arcs 7274, 7278, 7282, 7286, 7290, 7294, 7298, 7302, 7306, 7310, 7314, 7318, 7322, 7326, 7330, 7334. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `261.87807869214674 < 282.5761`;
- maximum propagated fourth root: `4.022766144857933 < 4.10`;
- maximum direct fourth root: `4.022766144823935`;
- maximum sweep-minus-direct B4: `3.710565010806022e-08`;
- maximum entry discrepancy: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.2868848258062514e-09`;
- maximum rebase arithmetic charge: `1.9875619412558748e-10`;
- maximum exact update support: 160.

Coverage is now `832+3328=4160` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,7337}`, with 3859 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `687f21c24ef194b88da565dac937d0ffbf1bbfe5cf1a4f7976e396c5f2c3c1cb`;
- certificate SHA-256: `25030adef63544463c36619a01123f7209664dd2a214e81ccbd699c9309c7596`;
- manifest SHA-256: `4fa4e98343ee322852cff24a6606584965411a3e8d023ed3bce26fc766b0c72f`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 3329–3392, arcs 7338–7401, subject to fresh collision checks. Independent audit of v15.1535 and v15.1536 is required.
