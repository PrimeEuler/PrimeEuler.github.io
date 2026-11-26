# Cone Derivation Ledger v15.1514 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 04:01 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1512; External Audit Round 657/v15.1513  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-26 03:54 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 657/v15.1513 is ACKed exactly once here. Before gate selection, live master was `840359667e949b612fdfadcf35e4487d5c24dc55`. The full latest Suzuki entry v15.1512 and full Round 657 entry were checked. Round 657 independently replayed v15.1512, confirmed its producer, certificate, manifest, extrema, adjacency, and coverage arithmetic bit-for-bit, and explicitly verified that its narrowing margin remains roughly eight orders of magnitude larger than its propagated-versus-direct discrepancy. It makes no Suzuki correction.

Audit owns v15.1513, so version and competing-write checks found v15.1514 next-free, with no competing Suzuki owner or correction. Immediately before exact execution, live master remained `840359667e949b612fdfadcf35e4487d5c24dc55`; the exact producer, certificate, and ledger paths were absent and the audited prior block plus all frozen hashes were unchanged. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `840359667e949b612fdfadcf35e4487d5c24dc55`, `67a7c0117aaf4babbf2ae9cae9e7d146bf2b1b8e`, and `dc8251c38c0908070f7dc9a052d381d7c8c8c7bd`; every exact target path was absent and every local hash set was unchanged. Those artifacts landed as commits `67a7c0117aaf4babbf2ae9cae9e7d146bf2b1b8e`, `dc8251c38c0908070f7dc9a052d381d7c8c8c7bd`, and `636558ac49fda4e273b1c3bf209b6c1e9e75d7b5`.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2560 from the x=1 anchor, then traverses steps 2561 through 2624, corresponding to arcs 6570 through 6633. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6570–6633;
- step interval: 2561–2624;
- rebase arcs: 6570, 6574, 6578, 6582, 6586, 6590, 6594, 6598, 6602, 6606, 6610, 6614, 6618, 6622, 6626, 6630;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `266.2878327059386 < 282.5761`;
- maximum propagated fourth root: `4.0395950443412065 < 4.10`;
- maximum direct fourth root: `4.039595044302954`;
- maximum sweep-minus-direct B4: `1.5258649455063278e-08`;
- maximum entry discrepancy against direct assembly: `2.220446049250313e-15`;
- maximum cumulative arithmetic charge: `2.2887684996175668e-09`;
- maximum rebase arithmetic charge: `1.9968089732525747e-10`.

The new block is adjacent to v15.1512 at arcs 6569/6570. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6633\},
\]

namely `832+2624=3456` of 8019 arcs; 4563 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1514_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1514_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1514_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `c2366831b4e8682204f28b3b98e47c27160fda5e0c6e8b20289996ba53b23879`;
- certificate SHA-256: `adf002b5fcd6a184833bfc173d23a8a9ec5a4ee19c0fe474e328aa63ca6a0914`;
- manifest SHA-256: `ed21af345e5c2f8a58a4dd8a2bd935581b840d023563a958e8741a7c8dea598f`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

The previous two blocks' narrowing trend does not persist here: the certified maximum falls to `4.0395950443412065`. This observation is confined to the present finite block and is not extrapolated. Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2625–2688, arcs 6634–6697) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1514 from committed producer bytes, verify its certificate and manifest byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
