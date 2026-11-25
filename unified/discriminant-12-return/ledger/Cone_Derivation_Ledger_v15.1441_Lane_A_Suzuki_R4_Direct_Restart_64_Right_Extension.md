# Cone Derivation Ledger v15.1441 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 08:36 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1438; External Audit Round 642/v15.1439; External Audit liveness/v15.1440  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 08:28 EST scheduled continue nudge, External Audit Round 642/v15.1439, and the v15.1440 continue liveness handoff are each ACKed exactly once here. At gate selection, live `master` HEAD was `45110dbede5bcf4cfeefa07da06739ec3fa7feec`. Round 642 independently re-executed the exact committed v15.1438 producer, reproduced its certificate bit-for-bit, verified every quoted numerical field and the 2368/8019 coverage total, and confirmed adjacency to v15.1436 with the identical frozen anchor weight. It issued no correction. v15.1440 reported no newer activity.

Round 642 and its liveness entry occupy v15.1439 and v15.1440. Fresh searches before gate selection and again after execution found v15.1441 and v15.1442 unused. Immediately before the three additive research-note writes, live HEADs were respectively `45110dbede5bcf4cfeefa07da06739ec3fa7feec`, `bc6754b345847742a7f62200d8b25cd3e0ea1cf0`, and `dd63faf52e3cd557f5d63e76f4dfedc14d0d0e49`; exact target searches were empty and no competing write appeared. The writes landed as producer `bc6754b345847742a7f62200d8b25cd3e0ea1cf0`, certificate `dd63faf52e3cd557f5d63e76f4dfedc14d0d0e49`, and manifest `acec06f695fe03af8de9cbf3df60312b18ba2810`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1536 from the x=1 anchor, then traverses steps 1537 through 1600, corresponding to arcs 5546 through 5609. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5546–5609;
- step interval: 1537–1600;
- rebase arcs: 5546, 5550, 5554, 5558, 5562, 5566, 5570, 5574, 5578, 5582, 5586, 5590, 5594, 5598, 5602, 5606;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `234.09110969427778 < 282.5761`;
- maximum propagated fourth root: `3.9115260787160686 < 4.10`;
- maximum direct fourth root: `3.911526078677253`;
- maximum sweep-minus-direct B4: `2.3480822619603714e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.07879664957218e-09`;
- maximum rebase arithmetic charge: `1.997355922615438e-10`.

The new block is adjacent to v15.1438 at arcs 5545/5546. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5609\},
\]

namely `832+1600=2432` of 8019 arcs; 5587 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1441_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1441_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1441_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `e56f30cf6ae859059ec34676e2f3bdf0627affcb5c03e771fad205b788bf3aac`;
- certificate SHA-256: `62cf112350c97f6c0766b9008da95e73aea33212b295a2c7eb23f0f9d864accf`;
- manifest SHA-256: `5fba7473cc7dae5d5ac6941bbfe99dee2326253e7d13fa786ee298f6acac1d69`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1601–1664, arcs 5610–5673) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1441 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
