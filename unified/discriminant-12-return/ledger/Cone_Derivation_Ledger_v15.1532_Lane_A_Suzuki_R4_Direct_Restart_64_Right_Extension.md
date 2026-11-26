# Cone Derivation Ledger v15.1532 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 14:21 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1530; External Audit Round 665/v15.1531  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit, and hashes

The 2026-11-26 14:15 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 665/v15.1531 is ACKed exactly once here. Full v15.1530 and Round 665 were read. Round 665 independently replayed v15.1530 bit-for-bit with no correction. No non-Suzuki scope or claim from the audit summary is imported here.

Before the substantive replay, live HEAD was `5a70ff6ca0870b2789d5fdff74d7555cc7a07182`; v15.1531 was occupied by Round 665, v15.1532 was next-free, and all four exact v15.1532 paths were absent. The audited v15.1530 producer/certificate/manifest bytes and frozen hashes were unchanged. The exact producer was rerun from scratch under the final v15.1532 name.

Fresh producer/certificate/manifest prewrite checks used HEADs `5a70ff6ca0870b2789d5fdff74d7555cc7a07182`, `3a05a58f9646dc9734b6504fa3e7d2bfc97c8a78`, and `ee8a7d98fd2cb1747e413160b6463fe2be521f52`. Each target path was absent immediately before its additive commit, and the producer, certificate, audited prior dependency, and frozen hashes were unchanged. The artifacts landed as `3a05a58f9646dc9734b6504fa3e7d2bfc97c8a78`, `ee8a7d98fd2cb1747e413160b6463fe2be521f52`, and `07455a83315b64718d13987bc818f6ad64b84720`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 3137–3200, arcs 7146–7209, were checked with direct row-streamed recomputation at every state and rebases at arcs 7146, 7150, 7154, 7158, 7162, 7166, 7170, 7174, 7178, 7182, 7186, 7190, 7194, 7198, 7202, 7206. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `252.7792676600059 < 282.5761`;
- maximum propagated fourth root: `3.987359219438579 < 4.10`;
- maximum direct fourth root: `3.9873592194210783`;
- maximum sweep-minus-direct B4: `1.8612070107337786e-08`;
- maximum entry discrepancy: `3.552713678800501e-15`;
- maximum cumulative arithmetic charge: `2.1834565440672584e-09`;
- maximum rebase arithmetic charge: `1.9846004839777586e-10`;
- maximum exact update support: 160.

Coverage is now `832+3200=4032` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,7209}`, with 3987 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `381f802b9f37b4f93bc0208acae1513fde068dce0631b57f3ed7337f987f7b41`;
- certificate SHA-256: `8a5de19d1c0bb4306d0eddd3e1e0f040d0a524678b2037adc61dabd7c0a0ce5c`;
- manifest SHA-256: `b451946e83ecf81d7b7a1fd4912f9e12cf0b211c24cca7f0a3c3d208a4763315`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 3201–3264, arcs 7210–7273, subject to fresh collision checks. Independent audit of v15.1532 is required.
