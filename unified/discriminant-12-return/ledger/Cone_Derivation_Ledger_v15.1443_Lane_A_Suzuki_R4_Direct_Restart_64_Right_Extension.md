# Cone Derivation Ledger v15.1443 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 09:43 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1441; External Audit Round 643/v15.1442  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 09:35 EST scheduled continue nudge and External Audit Round 643/v15.1442 are each ACKed exactly once here. At gate selection, live `master` HEAD was `b11c3e0235f6bd46faba1b8abd5839397579687f`. Round 643 independently re-executed the exact committed v15.1441 producer, reproduced its certificate bit-for-bit, verified every quoted numerical field and the 2432/8019 coverage total, and confirmed adjacency to v15.1438 with the identical frozen anchor weight. It issued no correction.

Round 643 occupies v15.1442. Fresh searches before gate selection and again after execution found v15.1443 and v15.1444 unused. Immediately before the three additive research-note writes, live HEADs were respectively `b11c3e0235f6bd46faba1b8abd5839397579687f`, `d765457a0617c73eff697fc4799d6a8cf91a73dd`, and `742901b57f0c4a312c4e2b46930de6cdb5238769`; exact target searches were empty and no competing write appeared. The writes landed as producer `d765457a0617c73eff697fc4799d6a8cf91a73dd`, certificate `742901b57f0c4a312c4e2b46930de6cdb5238769`, and manifest `ffd106f5aa1a220353c49a9a682751a5edde7dff`. A final fresh check is required immediately before this ledger write.

The frozen dependency hashes were rechecked before execution:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The committed producer rebuilds the exact R4 state at step 1600 from the x=1 anchor, then traverses steps 1601 through 1664, corresponding to arcs 5610 through 5673. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 5610–5673;
- step interval: 1601–1664;
- rebase arcs: 5610, 5614, 5618, 5622, 5626, 5630, 5634, 5638, 5642, 5646, 5650, 5654, 5658, 5662, 5666, 5670;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `235.91597974321135 < 282.5761`;
- maximum propagated fourth root: `3.9191270234411753 < 4.10`;
- maximum direct fourth root: `3.919127023422945`;
- maximum sweep-minus-direct B4: `1.5931817642922397e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.120917755706443e-09`;
- maximum rebase arithmetic charge: `1.9973559226154377e-10`.

The new block is adjacent to v15.1441 at arcs 5609/5610. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,5673\},
\]

namely `832+1664=2496` of 8019 arcs; 5523 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1443_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1443_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1443_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `e342e692faa22b93d260f0f14ce2f575c287997c9979a9efa6e7ca70d7933af9`;
- certificate SHA-256: `ccea76fa70cc652d50f567d77bdc01bd9c4a1ccbadeb8f5092b229ca7f6f3af3`;
- manifest SHA-256: `9f5531d16818b5a780eae2391c0472e51839d7e82d7f9e2543a4379ddcb280c2`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. Round 627's reclassification remains in force: these computations are Suzuki consistency/spectral-realization research, not an RH proof or falsification.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 1665–1728, arcs 5674–5737) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1443 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
