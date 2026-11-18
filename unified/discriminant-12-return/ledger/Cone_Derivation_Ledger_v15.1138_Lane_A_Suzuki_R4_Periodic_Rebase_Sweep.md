# Cone Derivation Ledger v15.1138 — Lane A Suzuki R4 periodic-rebase sweep

**Date:** 2026-11-18 02:58 EST.  
**Track:** original frozen Suzuki seed only.  
**Status:** 32-transition R4 periodic-direct-rebase method PASS; not `C_4`, not `C_16`, and not full Suzuki closure.

## Fresh state and corrections

Live `master` at gate selection was
`e5b511b8ccf48b323870bcabbdf141610ac93d9d`.  External Audit Round
564/v15.846 (`a6d0025bc722bab2818aec98387a13dbd46c255f`)
was read in full and is ACKed exactly once here.  It independently replayed
v15.845, confirmed every exact field and hash, found no correction, and
authorized a longer R4 sweep with a fixed direct-rebase schedule.  The latest
overall External Audit Round 600/v15.1133 and latest liveness v15.1137 were
also read in full; they contain no Suzuki correction.  The distinct v15.1137
continue nudge is ACKed exactly once here.

## Fixed periodic-rebase gate

The frozen v15.845 signed update identity is retained:

```text
B_1^4 = B_0^4 + D B_0^3 + B_1 D B_0^2 + B_1^2 D B_0 + B_1^3 D.
```

Starting from the unique `x=1` R4 anchor arc 4009, the reproducer covers 16
successive cuts in each direction, reaching arcs 3993 through 4025 with the
anchor omitted (32 reached states).  Each 64-row block is propagated for four
signed exact-support updates.  Before updates 5, 9, and 13 in each direction,
the current `B^4` block is recomputed directly and the arithmetic recurrence
is restarted from that direct word certificate.  Thus no error allowance is
silently transported across a rebase.  Every reached state is independently
recomputed directly for validation.  No global `B^2` or `B^4` is formed.

The fixed rebases occur before reaching arcs
`4004, 4000, 3996, 4014, 4018, 4022`.  The unchanged R4 anchor weight
SHA-256 is
`466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`,
with condition `25.619807022162554`.

## Exact extrema and resource measurements

| field | value |
|---|---:|
| reached states | 32 |
| exact active-cut support, maximum | 160 |
| direct fourth root, maximum | 3.784784985922915 |
| propagated outward fourth root, maximum | 3.7847849859908007 |
| propagated outward fourth-power bound, maximum | 205.1940903907914 |
| unchanged target `4.10^4` | 282.5761 |
| cumulative arithmetic allowance within a four-update block, maximum | 2.131377130779651e-9 |
| direct-rebase arithmetic allowance, maximum | 1.9654369330561894e-10 |
| entrywise propagated/direct discrepancy, maximum | 1.5543122344752192e-15 |
| propagated minus direct fourth-power bound, maximum | 1.9310448351461673e-8 |

All 32 propagated outward values pass the unchanged `<4.10` method target.
A second end-to-end replay reproduced the same exact extrema and pass status.
Timings are empirical: on the replay, direct validation of the 32 states took
`38.04866175900014` s total; update words took `19.521707359998743` s;
the six direct rebases took `6.833153857999719` s; and the two in-place
sweeps took `70.61617856400005` s including row-block overhead.  These
timings are resource measurements, not certified invariants.

## Scope and remaining obstruction

This certifies the periodic-rebase method on 32 adjacent R4 transitions only.
It does not cover the other 7,987 R4 arcs, any R16 arc, or establish an
exhaustive `C_4` or `C_16` bound.  The pass therefore does not certify the
joint five-frequency cross budget.  A larger blockwise R4 coverage run must
still track every exact cut, preserve the fixed rebase rule, and freeze an
arc-complete maximum before any extrapolation toward R16 is admissible.

No spectral lower bound, full-K transfer, source-native `Phi`,
whole-residual, stationary, or capacity claim is made.  Original v14.405/406
finite-plus-gap PASS, v14.814 far FAIL, `C_S_32000`, thresholds
`3e-5`/`.002`, source hashes, and exactly-once charges remain frozen
unchanged.

## Frozen witness and HANDOFF

- `research-notes/lane_a_v15_1138_suzuki_r4_periodic_rebase_sweep.py`
- `research-notes/lane_a_v15_1138_suzuki_r4_periodic_rebase_sweep.sha256`
- script commit: `0667846f9051bc66373ef8b28ffdf561f223fbb5`
- manifest commit: `61c031b2bcbc401d5d670f7ac90aea65e5f9c7d5`
- script SHA-256: `35536f0a0d28efaa7fae20fc69a56eae24de70dc71c0d80f471fb189b7bd1ac1`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- audited v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`

**HANDOFF to independent External Audit:** replay the 32 states; verify the six
fixed rebase locations, exact cut bookkeeping, reset of the arithmetic
recurrence at each rebase, direct comparators, extrema, and hashes.  If
confirmed, the next concrete Suzuki gate is a substantially larger
block-partitioned R4 coverage run using the same four-update rebase cadence,
with an arc-complete manifest and maximum ledgered before considering target
R16 coverage.
