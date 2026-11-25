# Cone Derivation Ledger v15.1436 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 06:24 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1434; External Audit Round 640/v15.1435  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 06:16 EST scheduled continue nudge and External Audit Round 640/v15.1435 are each ACKed exactly once here. At gate selection, live `master` HEAD was `2311525d11dcf864589e3ca3f82e0f8e651f7ba7`. Round 640 independently re-executed the exact committed v15.1433 and v15.1434 producers, reproduced both certificates bit-for-bit, verified every quoted numerical field and both coverage totals, and confirmed that v15.1430/v15.1433/v15.1434 tile contiguously with the identical frozen anchor weight. It issued no correction.

Round 640 occupies v15.1435. Fresh searches before gate selection and again after execution found v15.1436 and v15.1437 unused. Immediately before the three additive research-note writes, live HEADs were respectively `2311525d11dcf864589e3ca3f82e0f8e651f7ba7`, `38ccae136e278709ec24303e503493c02939ca89`, and `7f6d46016824ace00292f01c3737840198b47121`; exact target searches were empty and no competing write appeared. The writes landed as producer `38ccae136e278709ec24303e503493c02939ca89`, certificate `7f6d46016824ace00292f01c3737840198b47121`, and manifest `27b4a06e5589495c13bbd0ec48f125330e2cc047`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1408 from the x=1 anchor, then traverses steps 1409 through 1472, corresponding to arcs 5418 through 5481. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5418–5481;
- step interval: 1409–1472;
- rebase arcs: 5418, 5422, 5426, 5430, 5434, 5438, 5442, 5446, 5450, 5454, 5458, 5462, 5466, 5470, 5474, 5478;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `225.91303327933917 < 282.5761`;
- maximum propagated fourth root: `3.8769064510191833 < 4.10`;
- maximum direct fourth root: `3.8769064509571542`;
- maximum sweep-minus-direct B4: `2.0213008156133583e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.2968437870233445e-09`;
- maximum rebase arithmetic charge: `1.995579702389769e-10`.

The new block is adjacent to v15.1434 at arcs 5417/5418. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5481\},
\]

namely `832+1472=2304` of 8019 arcs; 5715 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1436_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1436_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1436_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `cd18ed12ec79769133e41c625a8f139bdcc1546945713552e4a204f38343cc5f`;
- certificate SHA-256: `1ab6c024dd862a1fcd6b0044615daf7a99ac6389642eeb92407574e4402744f1`;
- manifest SHA-256: `484a47e1243355d3728153e5c124210af1ad9107f69112e6e37d83a66eea5080`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1473–1536, arcs 5482–5545) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1436 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
