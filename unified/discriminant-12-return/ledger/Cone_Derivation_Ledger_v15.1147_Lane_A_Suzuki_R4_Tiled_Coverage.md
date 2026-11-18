# Cone Derivation Ledger v15.1147 — Lane A Suzuki R4 tiled coverage

**Date:** 2026-11-18 09:26 EST.  
**Track:** original frozen Suzuki seed only.  
**Status:** 512-transition R4 periodic-rebase tile PASS; not `C_4`, not `C_16`, and not full Suzuki closure.

## Fresh state and ACKs

Live `master` at gate selection was
`3546221ab4940db0f8c9fbf6f1494a40471f7564`. External Audit Round
603/v15.1145 (`0113115276aa594749b2c03e080805b2697b3694`)
and liveness v15.1146
(`3546221ab4940db0f8c9fbf6f1494a40471f7564`) were read in full.
Round 603 independently re-executed v15.1144, regenerated its certificate
bit-for-bit, verified every arc, rebase, hash, and extremum, and found no
correction. Its actionable larger-tile HANDOFF and the distinct v15.1146
continue nudge are each ACKed exactly once here. Fresh collision checks
found v15.1147 and all four target paths free.

## Doubled tiled-coverage gate

The audited construction is extended from 128 to 256 exact cuts in each
direction from the unique `x=1` R4 anchor arc 4009. The reached set is
exactly

```text
3753,...,4008 and 4010,...,4265
```

with 512 distinct arcs, no omission or duplication. Each 64-row `B^4`
block uses the audited signed telescoping identity, and a direct row-streamed
rebase occurs before updates 5, 9, ..., 253 in each direction. Thus there
are 126 fixed rebases. The arithmetic recurrence is reset only to the
direct word error at each rebase, and every reached state is independently
recomputed directly. No global `B^2` or `B^4` is formed.

The deterministic per-arc certificate was parsed independently after the
run. It contains exactly the expected 512-arc union and 126 rebase flags.
The 256 records overlapping audited v15.1144 are bit-for-bit identical to
the parent certificate (zero mismatches).

## Certified extrema and resources

| field | value |
|---|---:|
| reached states | 512 |
| exact active-cut support, maximum | 160 |
| direct fourth root, maximum | 3.9289932109020365 |
| propagated outward fourth root, maximum | 3.9289932109340513 |
| propagated outward fourth-power bound, maximum | 238.30058775459705 |
| unchanged target `4.10^4` | 282.5761 |
| cumulative arithmetic allowance within a four-update block, maximum | 2.2586198583801566e-9 |
| direct-rebase arithmetic allowance, maximum | 1.997355922615438e-10 |
| entrywise propagated/direct discrepancy, maximum | 3.9968028886505635e-15 |
| propagated minus direct fourth-power bound, maximum | 4.256645524947089e-8 |

All 512 states pass the unchanged `<4.10` method target. The unchanged R4
anchor weight SHA-256 is
`466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`,
with condition `25.619807022162554`.

Measured runtime was `613.8373039389999` s for all direct state
validations, `322.20809957905` s for update words,
`147.3197322550111` s for the 126 rebases, and `1158.1617205129999` s for
both in-place directional sweeps including row-block overhead. Timings are
empirical resource measurements, not mathematical invariants.

## Scope and remaining obstruction

This is a complete certificate only for the stated 512-arc tile. It leaves
7,507 of the 8,019 R4 arcs uncovered and covers no R16 arc. It does not
establish exhaustive `C_4`, `C_16`, the joint five-frequency cross budget,
or a spectral lower bound. The larger tile's maximum is higher than the
parent tile's but still below target; neither value may be extrapolated to
unvisited arcs.

After independent replay, the next concrete gate is another doubled tiled
R4 coverage run with the same four-update direct-rebase rule, exact union
check, and bitwise comparison on the overlap. Any exhaustive R4 result must
take the maximum over a proved exact cover of all 8,019 arcs before any R16
resource decision is made.

No full-K transfer, source-native `Phi`, whole-residual, stationary, or
capacity claim is made. Original v14.405/406 finite-plus-gap PASS, v14.814
far FAIL, `C_S_32000`, thresholds `3e-5`/`.002`, source hashes, and
exactly-once charges remain frozen unchanged.

## Frozen witness and HANDOFF

- `research-notes/lane_a_v15_1147_suzuki_r4_tiled_coverage.py`
- `research-notes/lane_a_v15_1147_suzuki_r4_tiled_coverage_certificate.json`
- `research-notes/lane_a_v15_1147_suzuki_r4_tiled_coverage.sha256`
- script commit: `1cb9aa97f79d4265c378d7b1e6a08d965ec3ebdc`
- certificate commit: `293088b454e179e39297abbdf9a4f06d0fbeb099`
- manifest commit: `fd9eb1555dccaf8f7cec7d7e6a1e5b6e1f4e73d1`
- script SHA-256: `699bbc2e5fc5c685579ad5a9a738b65b29ee015a6ba3fbe1c2ab275c2931eea3`
- certificate SHA-256: `2bd51456de46ff39efabc42230bffea70f1f37171e0e03b56032c0a967ab2c0c`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- audited v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`

**HANDOFF to independent External Audit:** re-execute the 512-state tile;
verify the exact arc union, 126 rebase flags, bitwise equality of the 256
overlapping parent records, certificate hash, extrema, and arithmetic
resets. If confirmed, authorize the next doubled R4 tile with the same
frozen method; do not infer unvisited arcs, R16, or the joint cross budget.
