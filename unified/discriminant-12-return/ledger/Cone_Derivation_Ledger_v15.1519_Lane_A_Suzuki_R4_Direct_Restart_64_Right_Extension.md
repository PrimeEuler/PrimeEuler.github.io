# Cone Derivation Ledger v15.1519 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 06:35 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1516; External Audit Round 659/v15.1517; External Audit liveness v15.1518  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit, collision, and hashes

Scheduled continue nudges received after v15.1516 through the 2026-11-26 06:22 EST execution are ACKed exactly once collectively here. Round 659/v15.1517 and liveness v15.1518 are ACKed exactly once here. Full v15.1516 and both audit entries were read. Round 659 independently replayed v15.1516 bit-for-bit with no correction; v15.1518 is a no-correction liveness entry.

The first exact local replay was provisionally named v15.1518. Its producer prewrite check detected that liveness v15.1518 had landed at `9e37a835bd097df9904f33195ffa8329aa247d4b`; no provisional artifact was published. The provisional name was discarded, v15.1519 was confirmed next-free, and the exact producer was rerun from scratch under v15.1519. Before that rerun, HEAD was `9e37a835bd097df9904f33195ffa8329aa247d4b`, all exact v15.1519 paths were absent, and the audited prior bytes plus frozen hashes were unchanged.

Fresh producer/certificate/manifest prewrite checks used HEADs `9e37a835bd097df9904f33195ffa8329aa247d4b`, `f5a57034eac4a9d52197e99b15efceb3cbacc54d`, and `709ab645da19cf360e8beea873edd51ff8d58561`. The artifacts landed as `f5a57034eac4a9d52197e99b15efceb3cbacc54d`, `709ab645da19cf360e8beea873edd51ff8d58561`, and `97151cf9f16675c3c3cf41008e3e09a1008e28e0`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 2689–2752, arcs 6698–6761, were checked with direct row-streamed recomputation at every state and rebases at arcs 6698, 6702, 6706, 6710, 6714, 6718, 6722, 6726, 6730, 6734, 6738, 6742, 6746, 6750, 6754, 6758. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `262.261553464276 < 282.5761`;
- maximum propagated fourth root: `4.024237996730211 < 4.10`;
- maximum direct fourth root: `4.024237996704354`;
- maximum sweep-minus-direct B4: `1.6559312143726856e-08`;
- maximum entry discrepancy: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.090332318284404e-09`;
- maximum rebase arithmetic charge: `1.9875619412558745e-10`;
- maximum exact update support: 160.

Coverage is now `832+2752=3584` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,6761}`, with 4435 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `4eca62767158b7de0a275829014ee54a39757ccfcbcf3d800a210058a8dd15e9`;
- certificate SHA-256: `009e0f879b6fb4929cd0f908855a1a0334a982c3a7b5c2834a393ffe81dcf542`;
- manifest SHA-256: `9bdfe502804e52fb44f2f03f6b2cc5e2a4e7aa24d9a94876e92503aab3af881d`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 2753–2816, arcs 6762–6825, subject to fresh collision checks. Independent audit of v15.1519 is required.
