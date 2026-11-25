# Cone Derivation Ledger v15.1492 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 18:04 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1490; External Audit Round 650/v15.1484; External Audit Round 651/v15.1489  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 17:56 EST scheduled continue nudge is ACKed exactly once here. Before gate selection, live master was `7ec066831cde2a128407e5f87379aa197b54be60`. The full latest Suzuki entry v15.1490 and full latest External Audit Round 650/v15.1484 and Round 651/v15.1489 entries were checked. Round 650 remains the latest Suzuki-relevant independent replay and confirms v15.1476 bit-for-bit; Round 651 covers later Sandbox/Gravity work and issues no Suzuki correction. Independent audit of v15.1490 remains pending.

Version and competing-write checks found v15.1491 already owned by unrelated Gravity work, so v15.1492 was next-free for Suzuki. No competing Suzuki owner or correction was present. Immediately after execution and before preparing any deposit, live master remained `7ec066831cde2a128407e5f87379aa197b54be60`. Fresh checks before the producer, certificate, and manifest writes used HEADs `7ec066831cde2a128407e5f87379aa197b54be60`, `e6386c3b6fbaa5de667cfed09d83aeae72f9cd66`, and `5a8ef7fc4deacb323ceaa886eddecec2766c5ef9`; those artifacts landed as commits `e6386c3b6fbaa5de667cfed09d83aeae72f9cd66`, `5a8ef7fc4deacb323ceaa886eddecec2766c5ef9`, and `c821ac12d4f997db4393af977d44ec93b27eecb7` respectively. The final ledger prewrite check used live HEAD `c821ac12d4f997db4393af977d44ec93b27eecb7` and again found no correction or exact-path collision.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 1984 from the x=1 anchor, then traverses steps 1985 through 2048, corresponding to arcs 5994 through 6057. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5994–6057;
- step interval: 1985–2048;
- rebase arcs: 5994, 5998, 6002, 6006, 6010, 6014, 6018, 6022, 6026, 6030, 6034, 6038, 6042, 6046, 6050, 6054;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `230.46899898103314 < 282.5761`;
- maximum propagated fourth root: `3.896306642471973 < 4.10`;
- maximum direct fourth root: `3.896306642347274`;
- maximum sweep-minus-direct B4: `3.245136781515612e-08`;
- maximum entry discrepancy against direct assembly: `2.220446049250313e-15`;
- maximum cumulative arithmetic charge: `2.0320245816061564e-09`;
- maximum rebase arithmetic charge: `1.997355922615438e-10`.

The new block is adjacent to v15.1490 at arcs 5993/5994. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6057\},
\]

namely `832+2048=2880` of 8019 arcs; 5139 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1492_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1492_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1492_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `991e8280fb91b8f59bbb4dad370f35165f4df1d7c26f58c33e815b889bcb721f`;
- certificate SHA-256: `4da8a406a5e4a6ecaf8aa1fac275c3d3c9d49d4f9a61556e14fd68f05a2f1c42`;
- manifest SHA-256: `7dfa630374304da199b543be61785ad4d2da4fff5750047a166f5a425f08edc0`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2049–2112, arcs 6058–6121) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1492 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
