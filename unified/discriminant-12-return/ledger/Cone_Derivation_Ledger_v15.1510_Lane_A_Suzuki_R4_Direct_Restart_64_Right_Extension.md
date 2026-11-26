# Cone Derivation Ledger v15.1510 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-26 02:29 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Parents:** v15.1509; External Audit Round 655/v15.1506; External Audit liveness v15.1507–1508  
**Status:** SUBSTANTIVE FINITE-RESOURCE PASS. This entry extends the exact R4 direct-restart resource certificate by 64 contiguous right-hand arcs. It is not an all-arc C4 or C16 certificate and is not a full Suzuki or full-K closure.

## Live-state, audit, and ownership check

The 2026-11-26 02:21 EST scheduled continue nudge is ACKed exactly once here. Before gate selection, live master was `a3ce7b164b6ad8197ae95d47746ebb1f6e3b311c`. The full latest Suzuki entry v15.1509 and full latest External Audit entries Round 655/v15.1506 and liveness v15.1507–1508 were checked. Round 655 independently confirms v15.1504 bit-for-bit and makes no Suzuki correction; the liveness entries make no correction. No independent audit of v15.1509 had landed at gate selection, so v15.1509 and this entry remain explicitly pending independent replay.

Version and competing-write checks found v15.1510 next-free, with no competing Suzuki owner or correction. Immediately before exact execution, live master remained `a3ce7b164b6ad8197ae95d47746ebb1f6e3b311c`; the exact producer, certificate, and ledger paths were absent and the prior block plus all frozen hashes were unchanged. Fresh checks immediately before the producer, certificate, and manifest writes used HEADs `a3ce7b164b6ad8197ae95d47746ebb1f6e3b311c`, `ed11efa5262871d255773445948797e6e3e326b9`, and `b104bc3101197e944c557b8342dfb4397e19e4e7`; every exact target path was absent and every local hash set was unchanged. Those artifacts landed as commits `ed11efa5262871d255773445948797e6e3e326b9`, `b104bc3101197e944c557b8342dfb4397e19e4e7`, and `11ae49793163e593686171bc42f6131e9e68dfc2`.

The frozen dependency hashes were rechecked:

- v15.842 producer: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`;
- v15.800 producer: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`;
- raw R4 anchor-weight bytes: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Exact gate and result

The deposited producer rebuilds the exact R4 state at step 2432 from the x=1 anchor, then traverses steps 2433 through 2496, corresponding to arcs 6442 through 6505. Every fourth transition is followed by a direct row-streamed rebase; every reached state is independently recomputed row-streamingly. All 64 states pass the unchanged target

\[
(4.10)^4=282.5761.
\]

Certified extrema and bookkeeping:

- state count: 64;
- direction: right only;
- arc interval: 6442–6505;
- step interval: 2433–2496;
- rebase arcs: 6442, 6446, 6450, 6454, 6458, 6462, 6466, 6470, 6474, 6478, 6482, 6486, 6490, 6494, 6498, 6502;
- maximum exact update support: 160 nonzeros;
- maximum propagated outward B4: `278.8339936324534 < 282.5761`;
- maximum propagated fourth root: `4.086358168155933 < 4.10`;
- maximum direct fourth root: `4.086358168131455`;
- maximum sweep-minus-direct B4: `2.92907884613669e-08`;
- maximum entry discrepancy against direct assembly: `2.6645352591003757e-15`;
- maximum cumulative arithmetic charge: `2.123466642656719e-09`;
- maximum rebase arithmetic charge: `1.997355922615438e-10`.

The new block is adjacent to v15.1509 at arcs 6441/6442. The certified finite-resource coverage is now

\[
\{3177,\ldots,4008\}\cup\{4010,\ldots,6505\},
\]

namely `832+2496=3328` of 8019 arcs; 4691 arcs remain uncovered. Arc 4009 is the x=1 anchor and is not counted as a traversed cut arc.

## Reproducibility

- producer: `research-notes/lane_a_v15_1510_suzuki_r4_direct_restart_64_right_extension.py`;
- certificate: `research-notes/lane_a_v15_1510_suzuki_r4_direct_restart_64_right_extension_certificate.json`;
- SHA-256 manifest: `research-notes/lane_a_v15_1510_suzuki_r4_direct_restart_64_right_extension.sha256`;
- producer SHA-256: `638998bd4ba555bcf9cdf6f3c1b3d27da9873b5801db53fb416ec7f4694c4b58`;
- certificate SHA-256: `1d2f78818d5d3b909cd33c9bad0b4af0d92d354f9e21c6ef186142f6ed2f9ce8`;
- manifest SHA-256: `bd69227726e5df54adefc922b8f5f0faf34d0ded2e1161bb8eb4305ea66645dd`.

## Strict boundary and next gate

This is a finite R4 method/resource certificate only. It does not establish the essential supremum over all 1,257,795 R16 arcs, `C16<4.10`, the joint five-frequency budget, full Suzuki closure, a full-K spectral transfer, a source-native Suzuki Phi, or any whole-residual, stationary, capacity, or RH conclusion. The v14.405/406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000` thresholds `3e-5/.002`, source hashes, and once-only charges are unchanged.

The maximum in this block is close to the 4.10 resource target, but it is still an outward finite-block PASS and is not extrapolated beyond the certified arcs. Next independently feasible work is another collision-checked contiguous 64-arc R4 extension (steps 2497–2560, arcs 6506–6569) or a stronger rigorously outward all-arc method if one is derived. Independent audit should replay v15.1509 and v15.1510 from committed producer bytes, verify both certificates and manifests byte-for-byte, and recheck the finite coverage arithmetic before any promotion.
