# Cone Derivation Ledger v15.1516 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 04:58 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1514; External Audit Round 658/v15.1515  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-26 04:51 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 658/v15.1515 is ACKed exactly once here. Before gate selection, live master was `99c6d3246048feab43ae8011c6459eb6a07b279e`. The full latest Suzuki entry v15.1514 and full Round 658 entry were checked. Round 658 independently replayed v15.1514, confirmed its producer, certificate, manifest, extrema, adjacency, and coverage arithmetic bit-for-bit, and makes no Suzuki correction.

Audit owns v15.1515, so version and competing-write checks found v15.1516 next-free. Immediately before exact execution, live master remained `99c6d3246048feab43ae8011c6459eb6a07b279e`; the exact target paths were absent and the audited prior block plus all frozen hashes were unchanged. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `99c6d3246048feab43ae8011c6459eb6a07b279e`, `ffde4f6b96a330477ce4608637790bac48f14149`, and `07f26e9febae3a0c8555c47390fac8c58947ded7`; every target path was absent and every local hash set was unchanged. Those artifacts landed as commits `ffde4f6b96a330477ce4608637790bac48f14149`, `07f26e9febae3a0c8555c47390fac8c58947ded7`, and `5ed65c1dde796310528019784da7768c1f0b08c1`.

Frozen dependency hashes were rechecked: v15.842 producer `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 producer `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; raw R4 anchor-weight bytes `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The producer rebuilds the exact R4 state at step 2624, then traverses steps 2625–2688, arcs 6634–6697. Every fourth transition receives a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass `(4.10)^4=282.5761`.

- state count: 64;
- rebase arcs: 6634, 6638, 6642, 6646, 6650, 6654, 6658, 6662, 6666, 6670, 6674, 6678, 6682, 6686, 6690, 6694;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `265.88271640241885 < 282.5761`;
- maximum propagated fourth root: `4.038057760173857 < 4.10`;
- maximum direct fourth root: `4.038057760157515`;
- maximum sweep-minus-direct B4: `1.4967099559726194e-08`;
- maximum entry discrepancy: `3.1086244689504383e-15`;
- maximum cumulative arithmetic charge: `2.1290972668398798e-09`;
- maximum rebase arithmetic charge: `1.997355922615438e-10`.

The block is adjacent to v15.1514 at arcs 6633/6634. Finite-resource coverage is now `832+2688=3520` of 8019 arcs:

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6697\},
\]

with 4499 arcs uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer SHA-256: `e18f609d6886b4bf490a72ac393fd189bc82c2bbf09dcf422997186421e469c1`;
- certificate SHA-256: `cb5242b96a6eacb6b2555a0b50771bff668365c31ed877d2e35b32e2e4362e53`;
- manifest SHA-256: `91d1ae8151bb5ba4faea09b69b6a13f1b46547e718206ac20ac3e0e40c814dab`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

Next independently feasible work is another collision-checked 64-arc R4 extension (steps 2689–2752, arcs 6698–6761) or a stronger rigorously outward all-arc method. Independent audit should replay v15.1516 from committed bytes and verify the certificate, manifest, extrema, adjacency, and coverage arithmetic before promotion.
