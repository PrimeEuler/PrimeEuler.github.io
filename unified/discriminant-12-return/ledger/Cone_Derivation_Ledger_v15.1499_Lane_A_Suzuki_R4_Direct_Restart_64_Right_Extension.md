# Cone Derivation Ledger v15.1499 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 20:52 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1498; External Audit Round 652/v15.1494; External Audit Round 653/v15.1497  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 20:46 EST scheduled continue nudge is ACKed exactly once here. Before gate selection, live master was `e72ece2c20486f57e173731183b80850b44d3919`. The full latest Suzuki entry v15.1498 and full latest External Audit Round 653/v15.1497 were checked. Round 653 concerns Gravity only and issues no Suzuki correction. External Audit Round 652 remains the latest independent Suzuki replay, confirming v15.1490 and v15.1492 bit-for-bit; independent audit of v15.1498 remains pending.

Version and competing-write checks found v15.1499 next-free, with no competing Suzuki owner or correction. Immediately after exact execution, live master remained `e72ece2c20486f57e173731183b80850b44d3919`; the exact ledger path remained absent. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `e72ece2c20486f57e173731183b80850b44d3919`, `7cad1de6f02bed079972cb5b482c012f80cafc44`, and `6913e951561a28ca1f2b1053a6eec6e2ba90ad71`; every exact target path was absent and every local frozen hash set was unchanged. Those artifacts landed as commits `7cad1de6f02bed079972cb5b482c012f80cafc44`, `6913e951561a28ca1f2b1053a6eec6e2ba90ad71`, and `fd40520a439367f8225ef6ec280dadf88de16f52`. The final ledger prewrite check used HEAD `fd40520a439367f8225ef6ec280dadf88de16f52`, again found no competing write or Suzuki correction, confirmed the ledger path absent, and rechecked the unchanged hashes.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2112 from the x=1 anchor, then traverses steps 2113 through 2176, corresponding to arcs 6122 through 6185. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6122–6185;
- step interval: 2113–2176;
- rebase arcs: 6122, 6126, 6130, 6134, 6138, 6142, 6146, 6150, 6154, 6158, 6162, 6166, 6170, 6174, 6178, 6182;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `237.10021731296112 < 282.5761`;
- maximum propagated fourth root: `3.9240360448563414 < 4.10`;
- maximum direct fourth root: `3.924036044790936`;
- maximum sweep-minus-direct B4: `4.305812240090745e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.0010551169711466e-09`;
- maximum rebase arithmetic charge: `1.997355922615438e-10`.

The new block is adjacent to v15.1498 at arcs 6121/6122. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6185\},
\]

namely `832+2176=3008` of 8019 arcs; 5011 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1499_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1499_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1499_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `eaf3332822394a7f8f1d0d3321c68d228cc221dc9ea10e99b98e9468dbdd4685`;
- certificate SHA-256: `9af1f86dba056487a625214b103fd25d60898e63e352ee83b79a4d9d61d4866c`;
- manifest SHA-256: `1b93ad5184d909e73f54e607fac5ce31b69e1d26260c85c47aa85e8e9133fe11`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2177–2240, arcs 6186–6249) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1499 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
