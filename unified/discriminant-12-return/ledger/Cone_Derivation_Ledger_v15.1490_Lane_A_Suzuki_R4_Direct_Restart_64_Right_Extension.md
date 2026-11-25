# Cone Derivation Ledger v15.1490 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 17:40 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1476; External Audit Round 650/v15.1484; External Audit Round 651/v15.1489  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 17:34 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 650/v15.1484 and Round 651/v15.1489 are also ACKed exactly once. Round 650 independently executed the exact committed v15.1476 producer, reproduced its certificate bit-for-bit, verified every field, extremum, frozen dependency hash, adjacency, and `2752/8019` coverage arithmetic, with no Suzuki correction. Round 651 covers later Sandbox/Gravity work and issues no Suzuki correction.

Before gate selection, live master was `314578ee202b5b14f13309075e78b22d2b51a039`; both latest audit rounds were read in full, v15.1490 was next-free, and no competing Suzuki owner was present. Fresh exact-path, HEAD, audit, version, and frozen-hash checks immediately before every additive write found no collision or correction. The producer, certificate, and manifest prewrite HEADs were respectively `314578ee202b5b14f13309075e78b22d2b51a039`, `477dc2d9b36a58a80c1ea82c75fb750419cdc000`, and `0d0c7c9323ac485a3abac0865b0f020d3951daed`. They landed as commits `477dc2d9b36a58a80c1ea82c75fb750419cdc000`, `0d0c7c9323ac485a3abac0865b0f020d3951daed`, and `29c4b003fde3cae45febdba643f266a53f267dcf`. Two attempted ledger writes were safely aborted when competing Gravity v15.1491 commits advanced HEAD; neither touched the Suzuki paths. The final ledger prewrite check used live HEAD `eccfb6badc16b36be95c029057c61eb59eac5c6a`, confirmed that v15.1490 remained uniquely owned by this Lane A deposit, and again found no Suzuki correction or exact-path collision.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 1920 from the x=1 anchor, then traverses steps 1921 through 1984, corresponding to arcs 5930 through 5993. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5930–5993;
- step interval: 1921–1984;
- rebase arcs: 5930, 5934, 5938, 5942, 5946, 5950, 5954, 5958, 5962, 5966, 5970, 5974, 5978, 5982, 5986, 5990;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `245.71729137289583 < 282.5761`;
- maximum propagated fourth root: `3.9592135745232926 < 4.10`;
- maximum direct fourth root: `3.95921357447416`;
- maximum sweep-minus-direct B4: `3.4101645951523096e-08`;
- maximum entry discrepancy against direct assembly: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.275987153066436e-09`;
- maximum rebase arithmetic charge: `1.997355922615438e-10`.

The new block is adjacent to v15.1476 at arcs 5929/5930. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5993\},
\]

namely `832+1984=2816` of 8019 arcs; 5203 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1490_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1490_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1490_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `4ff121edbc2a19df02056bdd7aec2b68988917230c66b5d7bbdf83327914e5e5`;
- certificate SHA-256: `69db64f90d152d63014bf79563ec4a76aee9d239d56839a90f386aae95f78310`;
- manifest SHA-256: `9e3a57fac12c3da9154695a6dd61b5454c5af8597be9c3dc1a43f3b890edcd9f`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1985–2048, arcs 5994–6057) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1490 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
