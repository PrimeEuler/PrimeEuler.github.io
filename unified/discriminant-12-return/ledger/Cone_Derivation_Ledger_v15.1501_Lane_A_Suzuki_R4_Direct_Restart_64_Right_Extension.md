# Cone Derivation Ledger v15.1501 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 21:31 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1500; External Audit Round 652/v15.1494; External Audit Round 653/v15.1497  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 21:25 EST scheduled continue nudge is ACKed exactly once here. Before gate selection, live master was `f822dc0c4d75aab40a94136ed9c4dfb4cdd22409`. The full latest Suzuki entry v15.1500 and full latest External Audit Round 653/v15.1497 were checked. Round 653 concerns Gravity only and issues no Suzuki correction. External Audit Round 652 remains the latest independent Suzuki replay, confirming v15.1490 and v15.1492 bit-for-bit; independent audit of v15.1498–1500 remains pending.

Version and competing-write checks found v15.1501 next-free, with no competing Suzuki owner or correction. Immediately after exact execution, live master remained `f822dc0c4d75aab40a94136ed9c4dfb4cdd22409`; the exact ledger path remained absent. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `f822dc0c4d75aab40a94136ed9c4dfb4cdd22409`, `b83bedb16e8e232d06c40f88eff5db801cdf5891`, and `277c464b57d8065a89ddc51ff7acd513c79b3680`; every exact target path was absent and every local frozen hash set was unchanged. Those artifacts landed as commits `b83bedb16e8e232d06c40f88eff5db801cdf5891`, `277c464b57d8065a89ddc51ff7acd513c79b3680`, and `f7fbce86e6cb41753eb90743db9b1f1f871d263a`. The final ledger prewrite check used HEAD `f7fbce86e6cb41753eb90743db9b1f1f871d263a`, again found no competing write or Suzuki correction, confirmed the ledger path absent, and rechecked the unchanged hashes.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2240 from the x=1 anchor, then traverses steps 2241 through 2304, corresponding to arcs 6250 through 6313. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6250–6313;
- step interval: 2241–2304;
- rebase arcs: 6250, 6254, 6258, 6262, 6266, 6270, 6274, 6278, 6282, 6286, 6290, 6294, 6298, 6302, 6306, 6310;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `236.04437186731144 < 282.5761`;
- maximum propagated fourth root: `3.9196601394932222 < 4.10`;
- maximum direct fourth root: `3.9196601394281614`;
- maximum sweep-minus-direct B4: `4.407658593663655e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `1.987854859197763e-09`;
- maximum rebase arithmetic charge: `1.9956170017547347e-10`.

The new block is adjacent to v15.1500 at arcs 6249/6250. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6313\},
\]

namely `832+2304=3136` of 8019 arcs; 4883 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1501_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1501_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1501_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `c622c3301aae874cebe2cbb115ba04a87088393c0b0b894a53a8ac76709c4caf`;
- certificate SHA-256: `bf976078852939b7360c3d9776828454d77330db979223b9661e4ff28d65d7c4`;
- manifest SHA-256: `4c93565c20f0e111708f4bbcc53d957ce7c771ad1ee72aa1228316ac3d8f3b78`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2305–2368, arcs 6314–6377) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1501 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
