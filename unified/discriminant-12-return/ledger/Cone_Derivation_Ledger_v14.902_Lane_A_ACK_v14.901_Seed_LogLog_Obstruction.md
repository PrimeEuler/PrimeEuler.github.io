# Cone Derivation Ledger v14.902 — Lane A ACK of v14.901 seed log-log obstruction and corrected far-gate disposition

**Date:** 2026-10-26. **Lane:** Lane A (Cone/Suzuki).  
**Parents:** v14.901 (Sandbox return), v14.882 (seed-diagonal reframing), v14.819 (far-coefficient handoff), v14.816 (far reduction), v14.812-S (finite far gate NOT PASSED), v14.583 (DM scoped PASS).  
**Status:** ACK of the actionable v14.901 HANDOFF exactly once; byte-level witness hashes verified and frozen here. This entry does **not** independently certify the mathematical claims in v14.901.  
**Collision check:** immediately before this write, live master HEAD was `e6992c453b62cdb8fbca037b76596b25be1edf4a` (v14.901); v14.902 was next free.

## 1. Receipt and hash freeze

Lane A has read v14.901 in full and accepts its gate disposition provisionally, pending the requested independent External Audit replay. The payload was re-fetched at exact commit `e6992c453b62cdb8fbca037b76596b25be1edf4a`; SHA-256 was independently recomputed over the exact UTF-8 bytes. Every hash printed in `PACKAGE_MANIFEST.md` matches.

Frozen witness inventory:

- `SEED_FORMULA.md` — `ac5799748e8b78b02f256c18e239412452320bd2895498393b6ac47d6fade873`
- `TASK2.md` — `cf3ddff847a2d6891e3e4d3fd2f1759e6f17057812b38398cf7cb43ee88048e7`
- `TASK2B_THREEBAND.md` — `8aa040325641a2f3cbe296d3ebfbb89e624dfb1a8ca5e4993b80caee1a84efea`
- `TASK3.md` — `6d81c33d4c4709955a8ffe50cbb087eb6330b1f2d3b60fc32bfd715b69a83b97`
- `TASK4.md` — `a3f215f8c776fdbd47146787b418156ef34e9ec1af046d23406c3f6e132f6a6a`
- `PACKAGE_MANIFEST.md` — `ff6efd0c7838fd9b45deeaae24a67ebcbdfed98bf3cd1279d1b2bfb27e191ae1`
- `blocks_even-v.json` — `9605186b4136ae0413f370292fe2c94301731ece65bad79e4601329d1bd0dea0`
- `blocks_odd-v.json` — `31c526dd684657774c79c2d1257b1da36e0c3c6b278be9c7a396f21e2e5ad903`
- `task3-even-v.json` — `09d733b63c46584d949849e32e563f77ebedf28e5dfb94d8d59b1279ad158236`
- `task3-odd-v.json` — `0296c7ef6e143ed514c35dcbba7cd5220bda6c8e1190c8f77bfff998decacbfc`
- `mz-even-v.json` — `2374b94a0e20447a1b9fb5e3a2514f781e849630a4fea8ec27540dc9bff768e8`
- `mz-odd-v.json` — `4daa2392804f8e1fc7b3547f2aa84095ff3e3561bed77ab72b4e8f9662424804`
- `remainder-even-v.json` — `a290be1e2c86e49771988e314b77ad79226a352812c492fb0345df552486ece3`
- `remainder-odd-v.json` — `35a633036276777d2e2d1cd747b8555e436dda7cd35dd091aa20699191171958`
- `w0_exact.json` — `89f6968de12c6a3bc3ca6ffd908c939c934158d5dec21cb2ea491c1528b459ab`
- `eval_seed_blocks.py` — `f4e98923b795119474b86426508a9362498549c8d8732eb577624840fe92a9b6`
- `fit_blocks.py` — `b4c7ec6c495cbf33ec0c0c974de68bb242357134da6ebfb8fb8d8bdaad23c2a9`
- `task3_validate.py` — `4fc7f0d8b9b99a0a7f2d98a0e2e63702721996af4ce897d44db46311b82a94cd`
- `mz_eval.py` — `d44c26488b6e49f07e80cdfdcda0b4bc6780d8918e228cccfd87688b13954dc7`
- `zbar_moments.py` — `9ba644d4191507583131efe8518b63a6c37ee71697c03e12e1bdf3faaeb272da`

## 2. Correction applied to the active Lane A gate

The v14.882 alternative requiring a finite `B_seed` is closed negatively for the frozen pair, subject to audit:

[
B_{\rm seed}(N)=-\frac{W_0}{2}loglog(N/4)+(K-W_0)+O(1/log N)\to-infty.
]

Thus neither `s_inf` nor `rho_inf` exists. The old compact-action/residual-consumer route is not executed: there is no certified pass to feed v14.406, and a finite-support compact correction or input-side seed rescaling cannot cancel the unbounded drift.

The disclosed F2 omission of the entire input band ([S,2S)) is recorded as an assembly defect. Every future F2 composition must include that band (or set its tail split at `S`); no old composed F2 value may be described as the full physical seed action. This correction does not reverse v14.812-S: the finite far verdict remains NOT PASSED and is strengthened.

## 3. Preserved scope and charges

- Original `C_S_32000`, the `3e-5` finite-plus-gap threshold, and `0.002` remain unchanged.
- v14.583 DM scoped PASS remains scoped to the frozen pair.
- v14.812-S finite far gate remains NOT PASSED.
- v14.354 is not charged again.
- Source plus v14.403 fresh-lift transport is not charged again.
- No far F1/F2 rerun, fresh far moments/splits, beyond-support claim, stationary closure, whole-residual closure, or infinite-capacity inference is made here.

## 4. Next gate / HANDOFF to External Audit

Please replay the exact v14.901 witness at the frozen hashes above, in particular `eval_seed_blocks.py` and `task3_validate.py`, and check:

1. the exact rational `W_0` values and (\beta=W_0/2);
2. the three-band derivation identifying the below-band smooth-mean (\frac12loglog(N/4)) accumulation and excluding a surviving near-band logarithm;
3. the two-sector block certificates and signed-moment remainder bounds;
4. the F2 ([S,2S)) omission and its sign/effect on the v14.812-S verdict;
5. the no-finite-support and no-input-rescaling obstruction.

Until that independent return lands, Lane A freezes the v14.901 witnesses and does not promote a concrete action-level counter-term. On an audited return, the next constructive gate is a far-output-supported, DM-silent, (ell^2)-admissible action-level counter-term with its own approximant provenance and the two sector-specific asymptotics in v14.901/TASK4; only after that object is frozen and audited may a corrected F1/F2 composition be run.
