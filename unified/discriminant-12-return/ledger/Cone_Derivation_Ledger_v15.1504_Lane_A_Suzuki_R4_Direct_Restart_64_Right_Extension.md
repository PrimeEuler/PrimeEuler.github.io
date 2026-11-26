# Cone Derivation Ledger v15.1504 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-25 22:41 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1501; External Audit Round 654/v15.1502; External Audit liveness v15.1503  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-25 22:34 EST scheduled continue nudge is ACKed exactly once here. External Audit Round 654/v15.1502 and its v15.1503 liveness continuation are ACKed exactly once here. Before gate selection, live master was `71bdc657623deb20b4e3490fd348aba5ed690826`. The full latest Suzuki entry v15.1501 and full latest External Audit entries were checked. Round 654 independently reran v15.1498–1501 and confirmed all four producers, certificates, manifests, extrema, adjacency, and coverage arithmetic bit-for-bit, with no correction. The v15.1503 liveness note issues no correction.

Audit owns v15.1502 and v15.1503, so version and competing-write checks found v15.1504 next-free, with no competing Suzuki owner or correction. Immediately after exact execution, live master remained `71bdc657623deb20b4e3490fd348aba5ed690826`; the exact ledger path remained absent. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `71bdc657623deb20b4e3490fd348aba5ed690826`, `a444016cec80778c0d1d08260e084ab266353967`, and `690fe71f7cbec9e1a54148b4fabf1739dae18743`; every exact target path was absent and every local frozen hash set was unchanged. Those artifacts landed as commits `a444016cec80778c0d1d08260e084ab266353967`, `690fe71f7cbec9e1a54148b4fabf1739dae18743`, and `78771e457f93305ef113b11b665eb7cd1ad896a0`. The final ledger prewrite check used HEAD `78771e457f93305ef113b11b665eb7cd1ad896a0`, again found no competing write or Suzuki correction, confirmed the ledger path absent, and rechecked the unchanged hashes.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2304 from the x=1 anchor, then traverses steps 2305 through 2368, corresponding to arcs 6314 through 6377. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6314–6377;
- step interval: 2305–2368;
- rebase arcs: 6314, 6318, 6322, 6326, 6330, 6334, 6338, 6342, 6346, 6350, 6354, 6358, 6362, 6366, 6370, 6374;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `230.40084581464382 < 282.5761`;
- maximum propagated fourth root: `3.8960185613326876 < 4.10`;
- maximum direct fourth root: `3.896018561254271`;
- maximum sweep-minus-direct B4: `3.95450001633435e-08`;
- maximum entry discrepancy against direct assembly: `2.4424906541753444e-15`;
- maximum cumulative arithmetic charge: `2.3030268493831324e-09`;
- maximum rebase arithmetic charge: `1.9875619412558748e-10`.

The new block is adjacent to v15.1501 at arcs 6313/6314. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6377\},
\]

namely `832+2368=3200` of 8019 arcs; 4819 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1504_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1504_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1504_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `994941455da571765bb57581339c7be5cfde62c3878c3ac69cff6506d118540c`;
- certificate SHA-256: `3e097a606a95f5236296bb21393e8259d49e55e1b3d337ebf671a92e413ada74`;
- manifest SHA-256: `c45e6e7a9938cf7f27ea463e081551fa92f349bc79bf48bcb3ec0b4013d97f93`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2369–2432, arcs 6378–6441) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1504 from committed producer bytes, verify the certificate and manifest hashes byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
