# Cone Derivation Ledger v15.1512 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 03:13 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1510; External Audit Round 656/v15.1511  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-26 03:06 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 656/v15.1511 is ACKed exactly once here. Before gate selection, live master was `953d943d64605312113eda76677514bb9a8b2ca0`. The full latest Suzuki entry v15.1510 and full Round 656 entry were checked. Round 656 independently replayed v15.1509 and v15.1510, confirmed both producers, certificates, manifests, extrema, adjacency, and coverage arithmetic bit-for-bit, and specifically verified that the v15.1510 margin dominates its propagation discrepancy by roughly nine orders of magnitude. It makes no Suzuki correction.

Audit owns v15.1511, so version and competing-write checks found v15.1512 next-free, with no competing Suzuki owner or correction. Immediately before exact execution, live master remained `953d943d64605312113eda76677514bb9a8b2ca0`; the exact producer, certificate, and ledger paths were absent and the audited prior block plus all frozen hashes were unchanged. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `953d943d64605312113eda76677514bb9a8b2ca0`, `eec5bc33b9b4fab66b65f74f9a49db8e37d8c35e`, and `af919af7aa4a12edae5d54fc85cf78c74e4ac115`; every exact target path was absent and every local hash set was unchanged. Those artifacts landed as commits `eec5bc33b9b4fab66b65f74f9a49db8e37d8c35e`, `af919af7aa4a12edae5d54fc85cf78c74e4ac115`, and `e78656726b0c5e405309ab2b78f8e6037d16284b`.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2496 from the x=1 anchor, then traverses steps 2497 through 2560, corresponding to arcs 6506 through 6569. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6506–6569;
- step interval: 2497–2560;
- rebase arcs: 6506, 6510, 6514, 6518, 6522, 6526, 6530, 6534, 6538, 6542, 6546, 6550, 6554, 6558, 6562, 6566;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `279.43034882840794 < 282.5761`;
- maximum propagated fourth root: `4.0885413389072776 < 4.10`;
- maximum direct fourth root: `4.088541338869433`;
- maximum sweep-minus-direct B4: `1.667132210059208e-08`;
- maximum entry discrepancy against direct assembly: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.4200085912652488e-09`;
- maximum rebase arithmetic charge: `1.9875619412558745e-10`.

The new block is adjacent to v15.1510 at arcs 6505/6506. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6569\},
\]

namely `832+2560=3392` of 8019 arcs; 4627 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1512_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1512_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1512_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `58de7df5b52664c5b0f6b5169373efd21b80703908c2bb13c840a1ef691189ee`;
- certificate SHA-256: `3efbed380c0d38784832ed7cbf261454114f35e6e16f5371919ed5fa7be7108a`;
- manifest SHA-256: `3419c7c8d42b28e021fbdaa953a7fd66f7c9d5118d714d8cc7277c8a3c0cfca2`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

This block remains close to the 4.10 resource target, but it is still an outward finite-block PASS and is not extrapolated beyond the certified arcs. Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2561–2624, arcs 6570–6633) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1512 from committed producer bytes, verify its certificate and manifest byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
