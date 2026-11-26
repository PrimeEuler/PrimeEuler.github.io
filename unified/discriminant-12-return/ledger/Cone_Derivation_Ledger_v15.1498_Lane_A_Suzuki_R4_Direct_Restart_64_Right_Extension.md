# Cone Derivation Ledger v15.1498 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 20:40 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1492; External Audit Round 652/v15.1494; External Audit Round 653/v15.1497  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 19:02 EST and 20:27 EST scheduled continue nudges are ACKed exactly once here. Before the final gate, live master was `6d916e484b1eb2c6a5d2572c714471c3b2a82ac7`. The full latest Suzuki entry v15.1492, full latest Suzuki-relevant External Audit Round 652/v15.1494, and full latest External Audit Round 653/v15.1497 were checked. Round 652 independently replayed v15.1490 and v15.1492 bit-for-bit and confirmed their adjacency, hashes, and coverage arithmetic without Suzuki correction. Round 653 concerns Gravity v15.1495/1496, flags their filename collision and a secondary inverse-`g^tt` discrepancy, and issues no Suzuki correction.

The block was first completed locally under v15.1495, but competing Gravity writes occupied v15.1495 and v15.1496. It was therefore moved and replayed exactly under v15.1497; External Audit Round 653 then occupied v15.1497. The exact final producer bytes were moved to next-free v15.1498 and rerun from scratch. No result from a collided version was promoted. A fresh post-replay check found live HEAD still `6d916e484b1eb2c6a5d2572c714471c3b2a82ac7`, v15.1498 free, no competing Suzuki write, and no Suzuki correction. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `6d916e484b1eb2c6a5d2572c714471c3b2a82ac7`, `671c98058ce406728b25f72e121a647a3088dadd`, and `1cd17def31214d4c364ad7aad4b0033a612a91e7`; each exact target path was absent and each local frozen hash set was unchanged. Those three artifacts landed as commits `671c98058ce406728b25f72e121a647a3088dadd`, `1cd17def31214d4c364ad7aad4b0033a612a91e7`, and `bf4d33ac42a1dc950699964a8c92b9a2f435fadc`. The final ledger prewrite check used HEAD `bf4d33ac42a1dc950699964a8c92b9a2f435fadc`, again found no competing write or Suzuki correction, and confirmed the ledger path absent.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2048 from the x=1 anchor, then traverses steps 2049 through 2112, corresponding to arcs 6058 through 6121. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6058–6121;
- step interval: 2049–2112;
- rebase arcs: 6058, 6062, 6066, 6070, 6074, 6078, 6082, 6086, 6090, 6094, 6098, 6102, 6106, 6110, 6114, 6118;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `230.53142951872647 < 282.5761`;
- maximum propagated fourth root: `3.89657047818748 < 4.10`;
- maximum direct fourth root: `3.89657047807812`;
- maximum sweep-minus-direct B4: `3.7740107927675126e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.3243851650082407e-09`;
- maximum rebase arithmetic charge: `1.9870152279744294e-10`.

The new block is adjacent to v15.1492 at arcs 6057/6058. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6121\},
\]

namely `832+2112=2944` of 8019 arcs; 5075 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1498_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1498_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1498_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `0181e2370c3e9945323a4a1b31ea04aa070208de4aedabdad0c5a89f6427139c`;
- certificate SHA-256: `cdb7255b06e9c957fe0fead37b20b90ef8d85b664f10f960278cbb35d4d8b4b8`;
- manifest SHA-256: `cadef7279e42e371b4a75e9904ce372b79a3a85df40741f4ba9675a4d3106d9c`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2113–2176, arcs 6122–6185) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1498 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
