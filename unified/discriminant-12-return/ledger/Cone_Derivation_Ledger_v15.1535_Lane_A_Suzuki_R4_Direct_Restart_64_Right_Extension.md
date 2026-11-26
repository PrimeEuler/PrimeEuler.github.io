# Cone Derivation Ledger v15.1535 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 15:35 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1532; External Audit Round 666/v15.1533; v15.1534 External Audit liveness collision  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. Exact 64-arc R4 right extension only; not an all-arc C4/C16 certificate or full Suzuki/full-K closure.

## Live state, audit, collision, and hashes

The 2026-11-26 15:22 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 666/v15.1533 is ACKed exactly once here. Full v15.1532 and Round 666 were read. Round 666 independently replayed v15.1532 bit-for-bit with no correction. No non-Suzuki scope or claim from the audit summary is imported here.

Before the substantive replay, live HEAD was `893041ee84e6cb72c4526271800609cb5a68d2aa`; v15.1533 was occupied by Round 666, v15.1534 was initially next-free, and all four exact v15.1534 paths were absent. The audited v15.1532 producer/certificate/manifest bytes and frozen hashes were unchanged. The first exact replay under the provisional v15.1534 name passed, but before its first additive write live HEAD moved to `a707d53df2a24a594b9080285644cf09253bbb76`, a heartbeat-only External Audit liveness entry occupying ledger version v15.1534. The collision guard stopped the write. That v15.1534 liveness entry is ACKed exactly once here; it supplied no correction or mathematical evidence and none is imported.

The producer was renumbered to next-free v15.1535 and rerun from scratch under that final name. Immediately before the final-name replay, live HEAD was `a707d53df2a24a594b9080285644cf09253bbb76`, all four exact v15.1535 paths were absent, and the audited prior dependency and frozen hashes were unchanged.

Fresh producer/certificate/manifest prewrite checks used HEADs `a707d53df2a24a594b9080285644cf09253bbb76`, `a397db31ce6e31e59a280ecc9412700dd0c984f4`, and `a808bc444d750f5cbec2ef81d201396751ffa61c`. Each target path was absent immediately before its additive commit, and the producer, certificate, audited prior dependency, and frozen hashes were unchanged. The artifacts landed as `a397db31ce6e31e59a280ecc9412700dd0c984f4`, `a808bc444d750f5cbec2ef81d201396751ffa61c`, and `daee0c550b4f110f930e79dcaa48681f9a786281`.

Frozen hashes remain: v15.842 `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; anchor weight `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate

Steps 3201–3264, arcs 7210–7273, were checked with direct row-streamed recomputation at every state and rebases at arcs 7210, 7214, 7218, 7222, 7226, 7230, 7234, 7238, 7242, 7246, 7250, 7254, 7258, 7262, 7266, 7270. All 64 states pass `(4.10)^4=282.5761`.

- maximum propagated outward B4: `261.0701667975274 < 282.5761`;
- maximum propagated fourth root: `4.019659921353575 < 4.10`;
- maximum direct fourth root: `4.019659921310965`;
- maximum sweep-minus-direct B4: `1.5052108892632532e-08`;
- maximum entry discrepancy: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.0679452483551197e-09`;
- maximum rebase arithmetic charge: `1.9680712527676298e-10`;
- maximum exact update support: 160.

Coverage is now `832+3264=4096` of 8019 arcs,
`{3177,...,4008} ∪ {4010,...,7273}`, with 3923 uncovered. Arc 4009 remains the uncounted x=1 anchor.

## Reproducibility and boundary

- producer SHA-256: `5ccf248ed06d11c852df4ab562d7471bd6bce77cbc3fa48fc7abbe5d74a388af`;
- certificate SHA-256: `bf10824e499c4a59e4419f72a48f2ec5062297af698f10ea2cfcf006f0c7d15d`;
- manifest SHA-256: `6c714b1e5d6df4ec4ca13507ad2c1a20a55bd4d5c313616a59ab8ca7d6a354ef`.

This finite R4 PASS does not establish the 1,257,795-arc `C16<4.10` essential supremum, the five-frequency budget, full Suzuki closure, full-K transfer, source-native Phi, or any whole-residual/stationary/capacity/RH claim. v14.405/406 PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged. Next finite gate is steps 3265–3328, arcs 7274–7337, subject to fresh collision checks. Independent audit of v15.1535 is required.
