# Cone Derivation Ledger v15.1438 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 07:24 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1436; External Audit Round 641/v15.1437  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 07:17 EST scheduled continue nudge and External Audit Round 641/v15.1437 are each ACKed exactly once here. At gate selection, live `master` HEAD was `2e1ac4076a504f803c53404b7a2a6fc9684a30bd`. Round 641 independently re-executed the exact committed v15.1436 producer, reproduced its certificate bit-for-bit, verified every quoted numerical field and the 2304/8019 coverage total, and confirmed adjacency to v15.1434 with the identical frozen anchor weight. It issued no correction.

Round 641 occupies v15.1437. Fresh searches before gate selection and again after execution found v15.1438 and v15.1439 unused. Immediately before the three additive research-note writes, live HEADs were respectively `2e1ac4076a504f803c53404b7a2a6fc9684a30bd`, `3b3400c437d38754160d00c258ef501f2301d210`, and `944b86983294c4f2230edb32758e49ca6b86b2a5`; exact target searches were empty and no competing write appeared. The writes landed as producer `3b3400c437d38754160d00c258ef501f2301d210`, certificate `944b86983294c4f2230edb32758e49ca6b86b2a5`, and manifest `f98b522114336ca18f240ed1e6ed5abfaebe555c`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1472 from the x=1 anchor, then traverses steps 1473 through 1536, corresponding to arcs 5482 through 5545. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5482–5545;
- step interval: 1473–1536;
- rebase arcs: 5482, 5486, 5490, 5494, 5498, 5502, 5506, 5510, 5514, 5518, 5522, 5526, 5530, 5534, 5538, 5542;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `226.46737167292702 < 282.5761`;
- maximum propagated fourth root: `3.8792825239586812 < 4.10`;
- maximum direct fourth root: `3.8792825238823845`;
- maximum sweep-minus-direct B4: `2.639711738083861e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.3987155308802454e-09`;
- maximum rebase arithmetic charge: `1.9973559226154377e-10`.

The new block is adjacent to v15.1436 at arcs 5481/5482. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5545\},
\]

namely `832+1536=2368` of 8019 arcs; 5651 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1438_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1438_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1438_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `bf3f09a158adc21d727e6884e108273695f3e5a22671838a14cba2c514615551`;
- certificate SHA-256: `e59eccedee89cff9e39e8907c988ef00750c14f7aba292ec12547bcb87d49fb0`;
- manifest SHA-256: `fd04b49ecb0f08ad6faeaa55cc71c5d1fe2f986a89a1bcde5f08fbc91e1a3e66`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1537–1600, arcs 5546–5609) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1438 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
