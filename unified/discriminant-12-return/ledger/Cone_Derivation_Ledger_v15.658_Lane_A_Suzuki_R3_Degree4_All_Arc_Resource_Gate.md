# Cone Derivation Ledger v15.658 — Lane A Suzuki exhaustive R=3 degree-four all-arc resource gate

**Date:** 2026-11-11 (America/New_York). **Track:** original frozen Suzuki five-frequency commutator only. **Parents:** v15.420, v15.499, v15.643–645, v15.649–650, v15.657. **Status:** [N] exhaustive binary64 evaluation over every R=3 candidate arc; [D] exact degree-four norm inequality; [O] outward interval certification and radius-16 execution. External Audit of v15.657 and this entry pending.

## Fresh state and collision control

Live master and the latest full Suzuki/audit chain were rechecked before the gate and before every additive write. No audit return or correction newer than Round 530/v15.652 was present; Round 530's missing `sigma*tau` correction remains applied. Immediately before this ledger write HEAD was `04b79eac342fccc13d771564f182472f23a0987b`, containing only the v15.658 witness and SHA-256 manifest after v15.657; the v15.658 ledger path was absent. No competing Suzuki owner was present. Separate non-Suzuki entries are not used.

## Degree-four certificate form

For Hermitian `B=B_{F_R}(x)`, `B^4` is Hermitian positive semidefinite and

`||B||_2^4=||B^4||_2 <= sqrt(||B^4||_1 ||B^4||_infinity)=||B^4||_infinity.`

Therefore a genuinely outward all-arc inequality `||B^4||_infinity<4.10^4` would be a valid two-sided spectral norm certificate. This retains cancellations through four matrix multiplications before taking entrywise absolute row sums. It is stronger than the v15.657 degree-two form at R=3.

The present calculation is not that certificate: cut locations, coefficients, sparse products, and row sums are binary64. It is an exhaustive resource/margin probe on the v15.650 partition.

## Exhaustive R=3 result

The SHA-frozen producer enumerated all

`(2R+3)(2R+1)^3=9*7^3=3,087`

candidate arcs at `R=3`, assembled the source-faithful physical 40-shift Hermitian matrix at one midpoint of every arc, formed `B^2` and `B^4`, and evaluated `||B^4||_infinity^(1/4)`. Six worker processes with `OPENBLAS_NUM_THREADS=1` completed the full sweep twice, independently through the exploratory harness and final frozen script.

Both runs returned the same maximum:

- all arcs exhausted: **3,087 / 3,087**;
- maximum binary64 degree-four value: **3.8044040552098752**;
- maximizing displayed midpoint: `x≈0.05144000755705935`;
- at that arc: `nnz(B^2)=485,421`, `nnz(B^4)=2,793,323`;
- final frozen replay wall time: approximately **172.89 s** on the current machine;
- numerical margin to 4.10: approximately **0.2955959448**.

This improves the v15.657 all-arc degree-two maximum `4.345872925431914`, which exceeded the gate. It demonstrates that degree four is a viable small-radius positive-polynomial candidate with a sizeable numerical margin. It does **not** prove `C_3<4.10`, because no branch/roundoff interval enclosure has yet been applied, and it says nothing certified about R=16.

## Frozen replay

- Script: `unified/discriminant-12-return/research-notes/lane_a_v15_658_suzuki_r3_degree4_all_arc_probe.py`
- Script commit: `285fa183cdec359cb5cf7fe7db60ad2abbdf9661`
- Git blob: `7a1a5ec180c79d7736beb5e414bd179e49df1903`
- SHA-256: `fc5f9f70731c177ee3681b63cd39fb1cdb03c3e30bf7561174623a7e996dc688`
- Manifest commit: `04b79eac342fccc13d771564f182472f23a0987b`
- Upstream frozen producer: v15.657 blob `cea6a8e2372d9ba61e5dee3e8a5af3ad073ec8a2`, SHA-256 `3e8a7de0b0596ff9bafaa15c62fb08c627b0d5651d36140d40dc366ad992b8b5`.

## Resource obstruction and next rigorous gate

Naively recomputing `B^4` on each radius-16 arc is not resource-effective: R=16 has 1,257,795 arcs and 1,185,921 sites, versus 3,087 arcs and 2,401 sites here, and even R=3 already materializes about 2.8 million B4 nonzeros per maximizing arc. The v15.650 <=160 directed-entry adjacency update must be exploited algebraically, not treated as a small-norm perturbation.

The next concrete gate is:

1. build exact/outward branch and coefficient intervals at R=3;
2. certify the all-arc degree-four maximum by interval sparse products or by a midpoint-plus-rigorous error decomposition;
3. measure interval widening and fill-in;
4. derive exact sparse update identities
   `(B+Delta)^2-B^2=B Delta+Delta B+Delta^2`
   and the corresponding factored update for `B^4=(B^2)^2`, updating only provably affected rows/columns with periodic full-anchor rebuilds;
5. only after the R=3 interval replay passes independently, test scaling toward R=16.

Rank <=160 alone is not a norm bound, and neither this all-arc binary64 probe nor the earlier eigsh samples may be promoted. The decisive acceptance gate remains an independently audited outward all-arc `C_16<4.10`. Only then may audited `E_16<0.142` be charged to obtain the scoped five-frequency cross budget `||X||<4.242<4.249030150943723`.

Protected unchanged: original frozen seed, `C_S_32000`, thresholds `3e-5` and `.002`, v14.405/406 finite-plus-gap PASS, v14.814 finite-far FAIL, source hashes, and exactly-once charges. `FULL_K_TRANSFER=INCONCLUSIVE`; no source-native Phi, whole-residual, stationary, capacity, physical-equivalence, or full-Suzuki claim.

HANDOFF
target: external-audit
parent: v15.658
type: suzuki-r3-degree4-all-arc-resource-gate
status: actionable
action: Replay the SHA-frozen six-worker script from repository root; verify the v15.657 source signs/indexing and Round-530 sigma*tau correction, the exact 3,087-arc count, Hermiticity checks, duplicate reproducibility, and the reported maximum 3.8044040552098752. Audit the exact degree-four norm inequality. Treat all numeric values as binary64 resource evidence only and do not infer C3 or C16.
deliverable: independent confirmation or correction of the exhaustive R3 degree-four resource result and scope, before any interval promotion.
