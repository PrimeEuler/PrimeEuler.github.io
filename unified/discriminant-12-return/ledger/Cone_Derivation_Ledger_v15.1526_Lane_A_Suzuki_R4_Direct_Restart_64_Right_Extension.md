# Cone Derivation Ledger v15.1526 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 11:06 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1524; External Audit Round 662/v15.1525  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit, and hashes

The 2026-11-26 10:59 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 662/v15.1525 is ACKed exactly once here. Full v15.1524 and Round 662 were read. Round 662 independently replayed v15.1524 bit-for-bit with no correction. No non-Suzuki scope or claim from the audit summary is imported here.

Before the substantive replay, live HEAD was `566a4cc4c959cca285d405f1af81d09c971eeae3`; v15.1525 was occupied by Round 662, v15.1526 was next-free, and all four exact v15.1526 paths were absent. The audited v15.1524 producer/certificate/manifest bytes and frozen hashes were unchanged. The exact producer was rerun from scratch under the final v15.1526 name.

Fresh producer/certificate/manifest prewrite checks used HEADs `566a4cc4c959cca285d405f1af81d09c971eeae3`, `cee0765947ef91532ed13116b56bf247cc92bc37`, and `99d5740a63de9ab4dda994e6d99406439541bbec`. Each target path was absent immediately before its additive commit, and the producer, certificate, audited prior dependency, and frozen hashes were unchanged. The artifacts landed as `cee0765947ef91532ed13116b56bf247cc92bc37`, `99d5740a63de9ab4dda994e6d99406439541bbec`, and `d1bca4b6f3bf66838b3faa233ba96f06b4b73eb7`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 2945–3008, arcs 6954–7017, were checked with direct row-streamed recomputation at every state and rebases at arcs 6954, 6958, 6962, 6966, 6970, 6974, 6978, 6982, 6986, 6990, 6994, 6998, 7002, 7006, 7010, 7014. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `254.45512457796264 < 282.5761`;
- maximum propagated fourth root: `3.9939516256444763 < 4.10`;
- maximum direct fourth root: `3.993951625627021`;
- maximum sweep-minus-direct B4: `3.80042592951213e-08`;
- maximum entry discrepancy: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `1.9360322211425068e-09`;
- maximum rebase arithmetic charge: `1.9875246450545043e-10`;
- maximum exact update support: 160.

Coverage is now `832+3008=3840` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,7017}`, with 4179 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `bd4257d9940fcb7bb359858e7f02302bd3fbc35131ede9c23e300b8d8e186bef`;
- certificate SHA-256: `198677cd31a99743b951363d5b063f805be1e0ce4a0447bff52f921dc50fa91f`;
- manifest SHA-256: `d2276a4862dcff7df8705a9a386d409544c86d311fd70b88aaee64956e978398`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 3009–3072, arcs 7018–7081, subject to fresh collision checks. Independent audit of v15.1526 is required.
