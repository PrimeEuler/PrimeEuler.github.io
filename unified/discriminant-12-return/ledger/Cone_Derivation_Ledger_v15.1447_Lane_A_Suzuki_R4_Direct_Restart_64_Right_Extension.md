# Cone Derivation Ledger v15.1447 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 11:48 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1445; External Audit Round 645/v15.1446  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 11:40 EST scheduled continue nudge and External Audit Round 645/v15.1446 are each ACKed exactly once here. At gate selection, live `master` HEAD was `3e99a9d03043bc57dd1317c454e05d34ef17f872`. Round 645 independently re-executed the exact committed v15.1445 producer, reproduced its certificate bit-for-bit, verified every quoted numerical field and the 2560/8019 coverage total, confirmed adjacency to v15.1443 with the identical frozen anchor weight, and confirmed the prior collision avoidance. It issued no correction.

Fresh searches found v15.1447 and v15.1448 unused. Exact-path checks immediately before publication found all v15.1447 targets absent. The live HEADs immediately before the producer, certificate, and manifest branch writes were respectively `3e99a9d03043bc57dd1317c454e05d34ef17f872`, `1635921266920cebac6ae9ea44d2b3976854d2c2`, and `2495724838106d27056f6049c49a3d8ff3300459`; no competing write appeared. The writes landed as producer `1635921266920cebac6ae9ea44d2b3976854d2c2`, certificate `2495724838106d27056f6049c49a3d8ff3300459`, and manifest `9dda02e6f0c760bdde3e7e610be35a4b80207998`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1728 from the x=1 anchor, then traverses steps 1729 through 1792, corresponding to arcs 5738 through 5801. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5738–5801;
- step interval: 1729–1792;
- rebase arcs: 5738, 5742, 5746, 5750, 5754, 5758, 5762, 5766, 5770, 5774, 5778, 5782, 5786, 5790, 5794, 5798;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `244.80960007659823 < 282.5761`;
- maximum propagated fourth root: `3.955552117963059 < 4.10`;
- maximum direct fourth root: `3.9555521179331503`;
- maximum sweep-minus-direct B4: `1.4882715504427324e-08`;
- maximum entry discrepancy against direct assembly: `2.220446049250313e-15`;
- maximum cumulative arithmetic charge: `2.2510863108474823e-09`;
- maximum rebase arithmetic charge: `1.9973559226154377e-10`.

The new block is adjacent to v15.1445 at arcs 5737/5738. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5801\},
\]

namely `832+1792=2624` of 8019 arcs; 5395 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1447_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1447_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1447_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `ebe1ac3bb5860fe816abb174587549761de9894a7e77d54150a126cd5c47a981`;
- certificate SHA-256: `4fa6cf19b86c1b9a0a00c8fa8997be38efd4e35c62565b754a980271c9b2ffff`;
- manifest SHA-256: `bc58edf361775624417625fa3189aa813a68c9e0de7dfa3e8c99c8fe4cd6749a`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1793–1856, arcs 5802–5865) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1447 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
