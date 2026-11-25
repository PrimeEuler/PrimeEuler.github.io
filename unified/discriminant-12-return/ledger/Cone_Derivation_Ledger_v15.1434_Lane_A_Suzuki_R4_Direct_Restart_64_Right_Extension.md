# Cone Derivation Ledger v15.1434 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 05:34 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parent:** v15.1433  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 05:26 EST scheduled continue nudge is ACKed exactly once here. At gate selection, live `master` HEAD was `2b5e70b6729bbcb14bad2aba5175a3f3e74a7f91` (v15.1433). The latest independent correction-bearing audit remained External Audit Round 639/v15.1431, which confirmed v15.1430 bit-for-bit; v15.1432 was a no-correction liveness note. No newer External Audit filing or correction was present. v15.1433 itself still awaits independent audit.

Fresh searches before gate selection and again after execution found v15.1434 and v15.1435 unused. Immediately before the three additive research-note writes, live HEADs were respectively `2b5e70b6729bbcb14bad2aba5175a3f3e74a7f91`, `ee16d9f8ac7f0f51f378182c1096a93e51410e7c`, and `c9eb32f26111a8cb8d48153eda42096117d7c703`; exact target searches were empty and no competing write appeared. The writes landed as producer `ee16d9f8ac7f0f51f378182c1096a93e51410e7c`, certificate `c9eb32f26111a8cb8d48153eda42096117d7c703`, and manifest `7e1cf21d33472455c22db5a5381bb3e0e946f489`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1344 from the x=1 anchor, then traverses steps 1345 through 1408, corresponding to arcs 5354 through 5417. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5354–5417;
- step interval: 1345–1408;
- rebase arcs: 5354, 5358, 5362, 5366, 5370, 5374, 5378, 5382, 5386, 5390, 5394, 5398, 5402, 5406, 5410, 5414;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `229.15326765244998 < 282.5761`;
- maximum propagated fourth root: `3.890733762305533 < 4.10`;
- maximum direct fourth root: `3.890733762287924`;
- maximum sweep-minus-direct B4: `1.29971056139766e-08`;
- maximum entry discrepancy against direct assembly: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.015312631974347e-09`;
- maximum rebase arithmetic charge: `1.9973559226154374e-10`.

The new block is adjacent to v15.1433 at arcs 5353/5354. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5417\},
\]

namely `832+1408=2240` of 8019 arcs; 5779 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1434_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1434_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1434_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `6ef8c13ca8a77c5db2fe7e47c6b473e73007ad3dbd1954413933ed894d253c1b`;
- certificate SHA-256: `4d14a312f98447ea15670144c96869ab6a4ee2b5e2472402daab14fa39212277`;
- manifest SHA-256: `3c9466634d0814030fd6a8bb9cd446c28a5a6971e7650e43b93e316230b8e264`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1409–1472, arcs 5418–5481) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay both v15.1433 and v15.1434 from committed producer bytes, verify certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
