# Cone Derivation Ledger v15.1433 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 04:51 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1430; External Audit Round 639/v15.1431; External Audit liveness/v15.1432  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state and audit check

At gate selection, live `master` HEAD was `555b3cd4d86b25b47a415e14ccb1322d61ef4528`. External Audit Round 639 independently re-executed v15.1430 from its committed bytes, reproduced certificate SHA-256 `c4aa36d36bd76d3614e8cb6bd61b69838a5f9e0d276bbbf1e11ed0ef2ffa7912` bit-for-bit, checked all quoted fields and the 2112/8019 coverage arithmetic, and issued no correction. The later v15.1432 liveness entry reported no further activity or correction. The scheduled 2026-11-25 04:42 EST continue nudge, Round 639 actionable confirmation, and v15.1432 liveness handoff are each ACKed exactly once here.

Immediately before the three additive research-note writes, live HEADs were respectively `555b3cd4d86b25b47a415e14ccb1322d61ef4528`, `bc103f27d382926784d35eacc2e3cb6962b43f7e`, and `f01d8b942f26c827bfa8c78e9a00dfd5aa53ec72`; exact target searches were empty. The writes landed as producer `bc103f27d382926784d35eacc2e3cb6962b43f7e`, certificate `f01d8b942f26c827bfa8c78e9a00dfd5aa53ec72`, and manifest `7f37ab097767cf5a05bf0dc0dc360eaa8f234644`. A final fresh check is required immediately before this ledger write.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1280 from the x=1 anchor, then traverses steps 1281 through 1344, corresponding to arcs 5290 through 5353. Every fourth transition is followed by a direct row-streamed rebase; every reached state is also independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4 = 282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5290–5353;
- step interval: 1281–1344;
- rebase arcs: 5290, 5294, 5298, 5302, 5306, 5310, 5314, 5318, 5322, 5326, 5330, 5334, 5338, 5342, 5346, 5350;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `236.36687677717404 < 282.5761`;
- maximum propagated fourth root: `3.920998301539172 < 4.10`;
- maximum direct fourth root: `3.9209983014986762`;
- maximum sweep-minus-direct B4: `1.4562004935214645e-08`;
- maximum entry discrepancy against direct assembly: `2.4424906541753444e-15`;
- maximum cumulative arithmetic charge: `1.98988305569565e-09`;
- maximum rebase arithmetic charge: `1.996808973252575e-10`;
- frozen raw R4 anchor-weight hash: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

The new block is adjacent to v15.1430 at arcs 5289/5290. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5353\},
\]

namely `832 + 1344 = 2176` of 8019 arcs; 5843 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1433_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1433_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1433_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `5c88ace3aff1d6d6564a4c0a7f315ba4131d5bbc2b254e1caf047f5d3f6e9a38`;
- certificate SHA-256: `8696683bbd6ef00a2a97cffd9598c774396b75f431269feaf0f4220e6f4fae50`;
- manifest SHA-256: `405691b014a949d7f29085f91420a2537376ddc16cb74499ea3883243f872138`;
- frozen v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- frozen v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16 < 4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1345–1408, arcs 5354–5417) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay the committed producer, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
