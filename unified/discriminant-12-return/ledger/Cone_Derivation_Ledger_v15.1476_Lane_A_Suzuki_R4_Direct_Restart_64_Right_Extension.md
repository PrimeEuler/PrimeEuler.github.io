# Cone Derivation Ledger v15.1476 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 15:35 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1471; External Audit Round 649/v15.1474; External Audit continue v15.1475  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 15:27 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 649/v15.1474 and its v15.1475 continue note are also ACKed exactly once. Round 649 independently rebuilt v15.1471 from a clean invocation, reproduced the certificate bit-for-bit, verified every field and quoted extremum, rechecked all frozen dependency hashes, and confirmed adjacency and the 2688/8019 coverage arithmetic. It issues no Suzuki correction. The later v15.1475 note explicitly directs Lane A to continue.

Before gate selection, live master was `462ec9c62c361697a3e8f65c0b921d803e86c9bf`; full Round 649 and the continue note were read, v15.1476 was next-free, and no competing Suzuki owner was present. Fresh exact-path, HEAD, audit, version, and frozen-hash checks immediately before every additive write found no collision or correction. The producer, certificate, and manifest prewrite HEADs were respectively `462ec9c62c361697a3e8f65c0b921d803e86c9bf`, `bff719b25ab3f739c65a0ca3ddbc9a2c874829f3`, and `d760568782e19bf7a4927c55ddffaad5c260bec2`. They landed as commits `bff719b25ab3f739c65a0ca3ddbc9a2c874829f3`, `d760568782e19bf7a4927c55ddffaad5c260bec2`, and `a138bf40ce75b65226bd2675064f2e8d0c7329b1`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 1856 from the x=1 anchor, then traverses steps 1857 through 1920, corresponding to arcs 5866 through 5929. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5866–5929;
- step interval: 1857–1920;
- rebase arcs: 5866, 5870, 5874, 5878, 5882, 5886, 5890, 5894, 5898, 5902, 5906, 5910, 5914, 5918, 5922, 5926;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `241.2762948518818 < 282.5761`;
- maximum propagated fourth root: `3.9412017209446875 < 4.10`;
- maximum direct fourth root: `3.9412017209267614`;
- maximum sweep-minus-direct B4: `1.4590199270969606e-08`;
- maximum entry discrepancy against direct assembly: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.090822234512203e-09`;
- maximum rebase arithmetic charge: `1.9799719640018838e-10`.

The new block is adjacent to v15.1471 at arcs 5865/5866. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5929\},
\]

namely `832+1920=2752` of 8019 arcs; 5267 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1476_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1476_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1476_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `93832ce5c92daf131ca9bcbd6c2f8c7e87ab715d495694813f33647758e78069`;
- certificate SHA-256: `9dc33b98e285ed34ef0edaa877e0deee9dc75981a8dfd3fae9fe7519a759dc63`;
- manifest SHA-256: `fe2d5a64841733e6243cf8b30c76c716147c1b8d328854b214ca7c1926fb7525`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1921–1984, arcs 5930–5993) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1476 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
