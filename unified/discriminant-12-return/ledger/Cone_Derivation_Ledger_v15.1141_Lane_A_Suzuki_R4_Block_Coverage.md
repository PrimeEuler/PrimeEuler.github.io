# Cone Derivation Ledger v15.1141 — Lane A Suzuki R4 block coverage

**Date:** 2026-11-18 04:49 EST.  
**Track:** original frozen Suzuki seed only.  
**Status:** 128-transition R4 periodic-rebase block PASS; not `C_4`, not `C_16`, and not full Suzuki closure.

## Fresh state and ACKs

Live `master` at gate selection was
`d50a0c1df7b75f289f434b49128d5486b2f85a0b`.  External Audit Round
601/v15.1139 (`b374dd19510798e49cf975965a803ce8637f12ff`)
and liveness v15.1140
(`d50a0c1df7b75f289f434b49128d5486b2f85a0b`) were read in full.
Round 601 independently re-executed v15.1138, confirmed every hash, identity,
rebase location, exact field, and scope statement, and found no correction.
Its actionable larger-coverage HANDOFF and the distinct v15.1140 continue
nudge are each ACKed exactly once here.  Fresh collision checks found
v15.1141 and all four target paths free.

## Fourfold block-coverage gate

The audited v15.1138 construction is extended from 16 to 64 exact cuts in
each direction from the unique `x=1` R4 anchor arc 4009.  The reached set is
exactly

```text
3945,...,4008 and 4010,...,4073
```

with 128 distinct arcs, no omissions or duplicates.  Each 64-row `B^4`
block is propagated using the exact signed telescoping identity

```text
B_1^4 = B_0^4 + D B_0^3 + B_1 D B_0^2 + B_1^2 D B_0 + B_1^3 D.
```

A direct row-streamed rebase occurs before updates 5, 9, ..., 61 in each
direction, giving 30 fixed rebases.  The arithmetic recurrence is reset only
to the directly certified word error at each rebase.  Every reached state is
also independently recomputed directly for validation.  No global `B^2` or
`B^4` is formed.

The reproducer writes a deterministic per-arc JSON certificate.  An
independent parser check verified 128 records, the exact expected arc set,
30 correctly placed rebases, no missing or extra arcs, and the extrema below.

## Certified extrema and resources

| field | value |
|---|---:|
| reached states | 128 |
| exact active-cut support, maximum | 160 |
| direct fourth root, maximum | 3.784784985922915 |
| propagated outward fourth root, maximum | 3.7847849859908007 |
| propagated outward fourth-power bound, maximum | 205.1940903907914 |
| unchanged target `4.10^4` | 282.5761 |
| cumulative arithmetic allowance within a four-update block, maximum | 2.131377130779651e-9 |
| direct-rebase arithmetic allowance, maximum | 1.997355922615438e-10 |
| entrywise propagated/direct discrepancy, maximum | 2.886579864025407e-15 |
| propagated minus direct fourth-power bound, maximum | 3.900743195117684e-8 |

All 128 states pass the unchanged `<4.10` method target.  The unchanged R4
anchor weight SHA-256 is
`466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`,
with condition `25.619807022162554`.

Measured runtime on this execution was `151.76622927399956` s for all
direct state validations, `79.45770330099754` s for update words,
`34.80839214499605` s for the 30 rebases, and
`286.699825835` s for both in-place directional sweeps including row-block
overhead.  Timings are empirical resource measurements, not mathematical
invariants.

## Scope and remaining obstruction

This is a complete certificate for the stated 128-arc block only.  It leaves
7,891 of the 8,019 R4 arcs uncovered and covers no R16 arc.  It therefore
does not establish exhaustive `C_4`, `C_16`, the joint five-frequency
cross budget, or a spectral lower bound.  The stable maximum and error
envelopes in this block cannot be extrapolated to unvisited arcs.

The next concrete gate, after independent replay, is a larger tiled R4
coverage run with the same four-update direct-rebase rule and deterministic
per-arc records.  Any later aggregation must prove exact union coverage and
take the maximum over all frozen block certificates before an exhaustive R4
statement is admissible.

No full-K transfer, source-native `Phi`, whole-residual, stationary, or
capacity claim is made.  Original v14.405/406 finite-plus-gap PASS, v14.814
far FAIL, `C_S_32000`, thresholds `3e-5`/`.002`, source hashes, and
exactly-once charges remain frozen unchanged.

## Frozen witness and HANDOFF

- `research-notes/lane_a_v15_1141_suzuki_r4_block_coverage.py`
- `research-notes/lane_a_v15_1141_suzuki_r4_block_coverage_certificate.json`
- `research-notes/lane_a_v15_1141_suzuki_r4_block_coverage.sha256`
- script commit: `ae3c83066352d2066e4b34a3304cfadd5db675cd`
- certificate commit: `76b9289090b59f8e0f2ef55436a42716c1beb924`
- manifest commit: `1376154508b7ba1ca3015ac2bf7b070389186fab`
- script SHA-256: `3d92f70a212c6e9128074197917044b62ceb6f317d114994f278149ceaf13e15`
- certificate SHA-256: `b4ef2245c5878aba037d3929d2759501f98c7594f9e6ffb1c385bbda8e3e937f`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- audited v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`

**HANDOFF to independent External Audit:** re-execute the 128-state block,
verify the exact arc union and 30 rebase flags, recompute the deterministic
certificate hash and extrema, and confirm the arithmetic reset at every
rebase.  If confirmed, authorize a larger tiled R4 block with the same frozen
method; do not infer unvisited arcs, R16, or the joint cross budget.
