# Cone Derivation Ledger v15.1509 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 01:50 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1504; External Audit Round 655/v15.1506; External Audit liveness v15.1507–1508  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, collision, and ownership check

The scheduled continue nudges received after v15.1504 through the 2026-11-26 01:42 EST execution are ACKed exactly once collectively here. External Audit Round 655/v15.1506 and its v15.1507–1508 liveness continuations are ACKed exactly once here. Before the renumbered substantive gate, live master was `932c1bae0348052b91e68f1bb120d031774149f1`. The full latest Suzuki entry v15.1504 and full latest External Audit entries were checked. Round 655 independently reran v15.1504 and confirmed its producer, certificate, manifest, extrema, adjacency, and coverage arithmetic bit-for-bit, with no Suzuki correction. The two subsequent liveness notes issue no correction.

The first local replay was provisionally named v15.1505. Live history then showed that v15.1505–1508 were occupied by a competing unrelated write and External Audit entries. The provisional name was therefore discarded without publication. A fresh exact replay was performed under next-free v15.1509 after confirming both exact v15.1509 artifact and ledger paths absent. This ledger does not adopt or extend the unrelated subject matter occupying v15.1505.

Immediately before the renumbered exact execution, live master remained `932c1bae0348052b91e68f1bb120d031774149f1`. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `932c1bae0348052b91e68f1bb120d031774149f1`, `2373be666cebc4d8386fc533c1e38d5af48ba286`, and `6a2b5270c7031fc5dbb1fa696a0476fd260c3275`; every exact target path was absent and every local frozen hash set was unchanged. Those artifacts landed as commits `2373be666cebc4d8386fc533c1e38d5af48ba286`, `6a2b5270c7031fc5dbb1fa696a0476fd260c3275`, and `777f2110a509d70b9c7172ea4ee2d8d0a8d90ae9`.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2368 from the x=1 anchor, then traverses steps 2369 through 2432, corresponding to arcs 6378 through 6441. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6378–6441;
- step interval: 2369–2432;
- rebase arcs: 6378, 6382, 6386, 6390, 6394, 6398, 6402, 6406, 6410, 6414, 6418, 6422, 6426, 6430, 6434, 6438;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `230.31983223482695 < 282.5761`;
- maximum propagated fourth root: `3.895676036507786 < 4.10`;
- maximum direct fourth root: `3.895676036438678`;
- maximum sweep-minus-direct B4: `3.53539064690267e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `1.96635384264075e-09`;
- maximum rebase arithmetic charge: `1.9973559226154374e-10`.

The new block is adjacent to v15.1504 at arcs 6377/6378. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6441\},
\]

namely `832+2432=3264` of 8019 arcs; 4755 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1509_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1509_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1509_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `bd79d519794220d138f3c58fea05b783abe3ba05bde20d0f8c35b90db29a3b1f`;
- certificate SHA-256: `538beed07abad26d647dca533c42f4903a83f2c1f468bd65b849fa54d182fb00`;
- manifest SHA-256: `0dd40534f12be077ed6f392d3c984a533828a9dc47b04a72a43b37a1c3ce74de`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2433–2496, arcs 6442–6505) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1509 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
