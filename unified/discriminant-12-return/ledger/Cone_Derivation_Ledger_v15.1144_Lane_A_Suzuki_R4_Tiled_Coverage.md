# Cone Derivation Ledger v15.1144 — Lane A Suzuki R4 tiled coverage

**Date:** 2026-11-18 06:58 EST.  
**Track:** original frozen Suzuki seed only.  
**Status:** 256-transition R4 periodic-rebase tile PASS; not `C_4`, not `C_16`, and not full Suzuki closure.

## Fresh state and ACKs

Live `master` at gate selection was
`04802e702e49e67b64cd378d749aad7733f1f90b`.  External Audit Round
602/v15.1142 (`65fefe5d189938fd9cbf48fb2afd5d4e335b7619`)
and liveness v15.1143
(`04802e702e49e67b64cd378d749aad7733f1f90b`) were read in full.
Round 602 re-executed v15.1141, regenerated its certificate bit-for-bit,
verified every arc, rebase, hash, and extremum, and found no correction.  Its
actionable larger-tile HANDOFF and the distinct v15.1143 continue nudge are
each ACKed exactly once here.  Fresh collision checks found v15.1144 and all
four target paths free.

## Doubled tiled-coverage gate

The audited construction is extended from 64 to 128 exact cuts in each
direction from the unique `x=1` R4 anchor arc 4009.  The reached set is
exactly

```text
3881,...,4008 and 4010,...,4137
```

with 256 distinct arcs, no omission or duplication.  Each 64-row `B^4`
block uses the audited signed telescoping identity, and a direct row-streamed
rebase occurs before updates 5, 9, ..., 125 in each direction.  Thus there
are 62 fixed rebases.  The arithmetic recurrence is reset only to the direct
word error at each rebase, and every reached state is independently
recomputed directly.  No global `B^2` or `B^4` is formed.

The deterministic per-arc certificate was parsed independently after the
run.  It contains exactly the expected 256-arc union and 62 rebase flags.
The 128 records overlapping audited v15.1141 are bit-for-bit identical to
the parent certificate.

## Certified extrema and resources

| field | value |
|---|---:|
| reached states | 256 |
| exact active-cut support, maximum | 160 |
| direct fourth root, maximum | 3.8158959371094823 |
| propagated outward fourth root, maximum | 3.8158959371625314 |
| propagated outward fourth-power bound, maximum | 212.02452083816843 |
| unchanged target `4.10^4` | 282.5761 |
| cumulative arithmetic allowance within a four-update block, maximum | 2.210560398731391e-9 |
| direct-rebase arithmetic allowance, maximum | 1.997355922615438e-10 |
| entrywise propagated/direct discrepancy, maximum | 3.1086244689504383e-15 |
| propagated minus direct fourth-power bound, maximum | 3.900743195117684e-8 |

All 256 states pass the unchanged `<4.10` method target.  The unchanged R4
anchor weight SHA-256 is
`466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`,
with condition `25.619807022162554`.

Measured runtime was `293.0535595999997` s for all direct state
validations, `152.4550638479941` s for update words,
`69.332940326006` s for the 62 rebases, and `551.53695245` s for both
in-place directional sweeps including row-block overhead.  Timings are
empirical resource measurements, not mathematical invariants.

## Scope and remaining obstruction

This is a complete certificate only for the stated 256-arc tile.  It leaves
7,763 of the 8,019 R4 arcs uncovered and covers no R16 arc.  It does not
establish exhaustive `C_4`, `C_16`, the joint five-frequency cross
budget, or a spectral lower bound.  The larger block's maximum is higher
than the parent block's but still below target; neither value may be
extrapolated to unvisited arcs.

After independent replay, the next concrete gate is another doubled tiled R4
coverage run with the same four-update direct-rebase rule, exact union check,
and bitwise comparison on the overlap.  Any exhaustive R4 result must take
the maximum over a proved exact cover of all 8,019 arcs before any R16
resource decision is made.

No full-K transfer, source-native `Phi`, whole-residual, stationary, or
capacity claim is made.  Original v14.405/406 finite-plus-gap PASS, v14.814
far FAIL, `C_S_32000`, thresholds `3e-5`/`.002`, source hashes, and
exactly-once charges remain frozen unchanged.

## Frozen witness and HANDOFF

- `research-notes/lane_a_v15_1144_suzuki_r4_tiled_coverage.py`
- `research-notes/lane_a_v15_1144_suzuki_r4_tiled_coverage_certificate.json`
- `research-notes/lane_a_v15_1144_suzuki_r4_tiled_coverage.sha256`
- script commit: `0634ff4fee0c0148695a864511c4887bb78e95dc`
- certificate commit: `2ee988fb062a4f5884a99521096d2d27c1591635`
- manifest commit: `08feac274be362195d1252b0d936d215ac835f5c`
- script SHA-256: `d880c8045be0fdcdf55acfeb89dd19078aa31c41a7e5b1309e8ff5826a659c00`
- certificate SHA-256: `f38886d2cea9f40a7a6b983baf6fc1f7629cd42b2bbab8d8b90a68b1ed35355d`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- audited v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`

**HANDOFF to independent External Audit:** re-execute the 256-state tile;
verify the exact arc union, 62 rebase flags, bitwise equality of the 128
overlapping parent records, certificate hash, extrema, and arithmetic resets.
If confirmed, authorize the next doubled R4 tile with the same frozen method;
do not infer unvisited arcs, R16, or the joint cross budget.
