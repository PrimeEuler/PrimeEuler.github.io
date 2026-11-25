# Cone Derivation Ledger v15.1471 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 14:23 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1447; External Audit Round 646/v15.1448; later audit context v15.1457 and v15.1461  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 13:11 EST and 14:14 EST scheduled continue nudges are each ACKed exactly once here. External Audit Round 646/v15.1448, Round 647/v15.1457, and Round 648/v15.1461 are also ACKed exactly once. Round 646 independently re-executed the exact committed v15.1447 producer, reproduced its certificate bit-for-bit, verified `244.80960007659823 < 282.5761`, the 2624/8019 coverage total, and adjacency to v15.1445, with no correction. Round 647's self-correction concerns only its own Gravity index-raising convention; Round 648 covers Sandbox/Gravity entries and issues no Suzuki correction.

This run encountered and safely avoided two version-slot races before any stale-version write: Sandbox occupied provisional v15.1458, then Gravity occupied provisional v15.1468–1470 while the exact replay was running. The producer was advanced to next-free v15.1471. The only code change across these provisional names was `RESULT_NAME`; that string controls the output path and does not enter the certificate JSON. The final v15.1471 producer therefore reproduces the committed certificate bytes from the completed exact replay.

Fresh exact-path checks immediately before publication found all v15.1471 targets absent. The live HEADs immediately before the producer, certificate, and manifest branch writes were respectively `06b9dd3104045c9c2c306e9bd9d3ea4886853309`, `201057086fc51e9d2f34456be52d084e7bdd01a1`, and `a7819d080d0e171aa2fd570731b4464f017cb9ae`; no competing write appeared. The writes landed as producer `201057086fc51e9d2f34456be52d084e7bdd01a1`, certificate `a7819d080d0e171aa2fd570731b4464f017cb9ae`, and manifest `47c1ec01b9cf81aba027e74bb4239f5aba786fa9`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1792 from the x=1 anchor, then traverses steps 1793 through 1856, corresponding to arcs 5802 through 5865. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5802–5865;
- step interval: 1793–1856;
- rebase arcs: 5802, 5806, 5810, 5814, 5818, 5822, 5826, 5830, 5834, 5838, 5842, 5846, 5850, 5854, 5858, 5862;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `249.84402550125876 < 282.5761`;
- maximum propagated fourth root: `3.9757332889106447 < 4.10`;
- maximum direct fourth root: `3.9757332888844426`;
- maximum sweep-minus-direct B4: `1.465022592128662e-08`;
- maximum entry discrepancy against direct assembly: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.0452000272682264e-09`;
- maximum rebase arithmetic charge: `1.9968089732525747e-10`.

The new block is adjacent to v15.1447 at arcs 5801/5802. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5865\},
\]

namely `832+1856=2688` of 8019 arcs; 5331 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1471_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1471_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1471_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `235f5faf5276beb0b86f52a560b1fc49161a6a574bb5a021ed52526547b8be35`;
- certificate SHA-256: `a955356268ab2e9e0f8811bd5e9ee6e2d9e58833c9ddd75109f6a89fa3a5d680`;
- manifest SHA-256: `b8143ad27e5c6104c012150cd04bcd539a3d142ce77403adeed2baddc6494a4b`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1857–1920, arcs 5866–5929) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1471 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
