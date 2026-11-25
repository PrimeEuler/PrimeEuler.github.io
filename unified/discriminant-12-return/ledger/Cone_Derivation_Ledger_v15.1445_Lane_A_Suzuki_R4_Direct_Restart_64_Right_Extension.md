# Cone Derivation Ledger v15.1445 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 10:48 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1443; External Audit Round 644/v15.1444  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 10:30 EST scheduled continue nudge and External Audit Round 644/v15.1444 are each ACKed exactly once here. At gate selection, live `master` HEAD was `14236c9409a2699f78377b5ce41cdb8a70eb466c`; during execution Round 644 landed at `fe406408a709430a6fc651cb507e1c16c2d862b1`, so the provisional version was advanced from v15.1444 to v15.1445 before any research-note write. Round 644 independently re-executed the exact committed v15.1443 producer, reproduced its certificate bit-for-bit, verified every quoted numerical field and the 2496/8019 coverage total, and confirmed adjacency to v15.1441 with the identical frozen anchor weight. It issued no correction.

Fresh exact-path checks immediately before publication found all v15.1445 targets absent. The live HEADs immediately before the producer, certificate, and manifest branch writes were respectively `fe406408a709430a6fc651cb507e1c16c2d862b1`, `ff6fddbd2d5bcc48ce942bedecc72fe248328a27`, and `893f540f4e90560ebebd5e281d5be8efbf7e7be4`; no competing write appeared. The writes landed as producer `ff6fddbd2d5bcc48ce942bedecc72fe248328a27`, certificate `893f540f4e90560ebebd5e281d5be8efbf7e7be4`, and manifest `b476c3ca6b125725b63cd6991194a0b43187c7c6`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1664 from the x=1 anchor, then traverses steps 1665 through 1728, corresponding to arcs 5674 through 5737. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5674–5737;
- step interval: 1665–1728;
- rebase arcs: 5674, 5678, 5682, 5686, 5690, 5694, 5698, 5702, 5706, 5710, 5714, 5718, 5722, 5726, 5730, 5734;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `239.1085111741955 < 282.5761`;
- maximum propagated fourth root: `3.9323191551126566 < 4.10`;
- maximum direct fourth root: `3.932319155094835`;
- maximum sweep-minus-direct B4: `1.4449256013904233e-08`;
- maximum entry discrepancy against direct assembly: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.09145402072614e-09`;
- maximum rebase arithmetic charge: `1.9799485646939115e-10`.

The new block is adjacent to v15.1443 at arcs 5673/5674. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5737\},
\]

namely `832+1728=2560` of 8019 arcs; 5459 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1445_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1445_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1445_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `60ce72ed94247301a1dc951097b4d7c67dcc1ad803aa44a49748e509cac0d808`;
- certificate SHA-256: `f9e5b2e7fc605cece0e24b57ce1ae04e7b7babe8ef8064693b852e6b6dd5c574`;
- manifest SHA-256: `a5b3c96d6c5913b1db52682fa7362b71cb4765571b2586bb8f152f8ade31f9d2`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1729–1792, arcs 5738–5801) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1445 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
