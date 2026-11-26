# Cone Derivation Ledger v15.1500 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 21:03 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1499; External Audit Round 652/v15.1494; External Audit Round 653/v15.1497  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 20:57 EST scheduled continue nudge is ACKed exactly once here. Before gate selection, live master was `2c260ff804e998abbf0477a857d503427cfb3e4e`. The full latest Suzuki entry v15.1499 and full latest External Audit Round 653/v15.1497 were checked. Round 653 concerns Gravity only and issues no Suzuki correction. External Audit Round 652 remains the latest independent Suzuki replay, confirming v15.1490 and v15.1492 bit-for-bit; independent audit of v15.1498 and v15.1499 remains pending.

Version and competing-write checks found v15.1500 next-free, with no competing Suzuki owner or correction. Immediately after exact execution, live master remained `2c260ff804e998abbf0477a857d503427cfb3e4e`; the exact ledger path remained absent. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `2c260ff804e998abbf0477a857d503427cfb3e4e`, `16a6360cd19eda7057a46c54115fe5c7ef8cb93b`, and `e96ea6df71fa5c4cbbcbd4d2b1b2e2be9b93810f`; every exact target path was absent and every local frozen hash set was unchanged. Those artifacts landed as commits `16a6360cd19eda7057a46c54115fe5c7ef8cb93b`, `e96ea6df71fa5c4cbbcbd4d2b1b2e2be9b93810f`, and `bb09caf286c76cde8ad6f16e4c6982dd5067a7b6`. The final ledger prewrite check used HEAD `bb09caf286c76cde8ad6f16e4c6982dd5067a7b6`, again found no competing write or Suzuki correction, confirmed the ledger path absent, and rechecked the unchanged hashes.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2176 from the x=1 anchor, then traverses steps 2177 through 2240, corresponding to arcs 6186 through 6249. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6186–6249;
- step interval: 2177–2240;
- rebase arcs: 6186, 6190, 6194, 6198, 6202, 6206, 6210, 6214, 6218, 6222, 6226, 6230, 6234, 6238, 6242, 6246;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `237.6461230946896 < 282.5761`;
- maximum propagated fourth root: `3.9262927982580846 < 4.10`;
- maximum direct fourth root: `3.926292798192158`;
- maximum sweep-minus-direct B4: `3.8116496625661966e-08`;
- maximum entry discrepancy against direct assembly: `3.552713678800501e-15`;
- maximum cumulative arithmetic charge: `2.047048234735715e-09`;
- maximum rebase arithmetic charge: `1.997355922615438e-10`.

The new block is adjacent to v15.1499 at arcs 6185/6186. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6249\},
\]

namely `832+2240=3072` of 8019 arcs; 4947 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1500_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1500_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1500_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `8dfec441192e845431df4e57cf247dea690b08dcadb5e3792f61c3e5196603ac`;
- certificate SHA-256: `11b9a7a9152993545d51e965311d74bf4198f38b678dfd39954bc9a6c46bacf1`;
- manifest SHA-256: `18bd7c4378b34175ef4c5d555e3e678d75c2aefa02a54f15673da30ba3791d7b`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2241–2304, arcs 6250–6313) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1500 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
