# Cone Derivation Ledger v15.1524 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 10:05 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1522; External Audit Round 661/v15.1523  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit, and hashes

The 2026-11-26 09:59 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 661/v15.1523 is ACKed exactly once here. Full v15.1522 and Round 661 were read. Round 661 independently replayed v15.1521 and v15.1522 bit-for-bit with no correction. Its file-layout observation is non-decisive and does not alter either verdict. No non-Suzuki scope or claim from the audit summary is imported here.

Before the substantive replay, live HEAD was `0f507fbe24b7b4de8f9e2f0fd7a09ec27fe9f66e`; v15.1523 was occupied by Round 661, v15.1524 was next-free, and all four exact v15.1524 paths were absent. The audited v15.1522 producer/certificate/manifest bytes and frozen hashes were unchanged. The exact producer was rerun from scratch under the final v15.1524 name.

Fresh producer/certificate/manifest prewrite checks used HEADs `0f507fbe24b7b4de8f9e2f0fd7a09ec27fe9f66e`, `2daf4175a07a8026f92acbbc8a09819ae7f84908`, and `2ba94f4775a164c7c364b75f06da512e743ce282`. Each target path was absent immediately before its additive commit, and the producer, certificate, audited prior dependency, and frozen hashes were unchanged. The artifacts landed as `2daf4175a07a8026f92acbbc8a09819ae7f84908`, `2ba94f4775a164c7c364b75f06da512e743ce282`, and `de00a44ecd22ebc6fec3214e77fe180eebb01b73`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 2881–2944, arcs 6890–6953, were checked with direct row-streamed recomputation at every state and rebases at arcs 6890, 6894, 6898, 6902, 6906, 6910, 6914, 6918, 6922, 6926, 6930, 6934, 6938, 6942, 6946, 6950. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `260.5995643990118 < 282.5761`;
- maximum propagated fourth root: `4.017847246165207 < 4.10`;
- maximum direct fourth root: `4.01784724608675`;
- maximum sweep-minus-direct B4: `2.7660917112370953e-08`;
- maximum entry discrepancy: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.4375799837472486e-09`;
- maximum rebase arithmetic charge: `1.9943895512187042e-10`;
- maximum exact update support: 160.

Coverage is now `832+2944=3776` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,6953}`, with 4243 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `0dabd3b00104752ed4fa078f3f13aea5e0d9a0635f09c9049bae99668d00f41a`;
- certificate SHA-256: `06e8138e9003a9cb33f701b7260adf4a2b314501139184ccc2b8fad6e07ef574`;
- manifest SHA-256: `07071cca4daab2f3313f403f466418b278d577cd1897cf822e6d40aadac29279`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 2945–3008, arcs 6954–7017, subject to fresh collision checks. Independent audit of v15.1524 is required.
