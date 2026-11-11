# Cone Derivation Ledger v15.671 — Lane A Suzuki R5 local-weight one-arc pass

**Date:** 2026-11-11 09:23 America/New_York  
**Lane:** A, original frozen Suzuki seed only  
**Status:** outward one-arc weighted-Collatz pass; not an exhaustive C5 certificate

## Parent and ownership

Parent v15.670 showed that one anchor-derived common weight fails on the fixed
32-arc R5 sample, with worst sampled midpoint `x=1`.  Round 536/v15.669 was
already ACKed exactly once in v15.670; this same-run follow-up does not duplicate
that ACK.  Immediately before the first additive write, live master was the
v15.670 ledger `8cbf2722...` and v15.671 was free.

## Frozen witness

Additive files:

- `research-notes/lane_a_v15_671_suzuki_r5_local_weight_worst_sample.py`
- `research-notes/lane_a_v15_671_suzuki_r5_local_weight_worst_sample.sha256`

Script SHA-256:

`64c3d5bebc74ec07ae2cfd68a6dcfa23f3e213fc40bcd4ff69db27d3d909bf2c`.

The witness uses the audited v15.664 exact/error machinery, rebuilds the R5
matrix at arc index 8651 (`x=1`), and performs 40 deterministic positive power
steps on `|B^4|` to obtain a local stored-float weight.  Its byte SHA-256 is
`dcdd6128f9b833f858b363a309c253a5a1e89e226bcb4b970ba1f4faaa74b89d`.

The same outward weighted-Collatz enclosure as v15.670 is then applied,
including `gamma(2*k4+1)`, sparse-product error, `E=10^-9` coefficient
perturbation, and the exact stored weight condition ratio.

## Evaluated result

```text
R5_ARC_INDEX 8651 MIDPOINT 1.0
POWER_STEPS 40 WEIGHT_MIN 0.0024934616029547575 WEIGHT_MAX 1.0 WEIGHT_CONDITION 401.0488867424298
WEIGHT_SHA256 dcdd6128f9b833f858b363a309c253a5a1e89e226bcb4b970ba1f4faaa74b89d
NNZ 468996 3900197 32367291 ROW_LENGTHS 40 401 4107
OBSERVED_WEIGHTED_B4 140.57418565627611
OUTWARD_WEIGHTED_B4 140.57446294443875 OUTWARD_FOURTH_ROOT 3.443313840589908
TARGET4 282.5761 LOCAL_ARC_PASS True
```

Therefore, at this single R5 arc,

\[
 \|B_{F_5}(1)\|^4\le 140.57446294443875,
 \qquad \|B_{F_5}(1)\|<3.44331384059<4.10.
\]

This confirms that the weighted signed-`B^4` mechanism can recover a strong
outward bound where the unweighted method fails and where the v15.670 common
weight also fails.

## Strict interpretation and next gate

Only one arc is certified.  No C5 or C16 essential-supremum statement follows.
The next gate is to quantify adjacent-arc transport of this positive weight or
construct a finite chart cover whose outward weighted bounds cover every arc.
The rank-`<=160` matrix update fact is not, by itself, a weight-transport or
spectral bound.

All historical Suzuki thresholds, hashes, PASS/FAIL results and exactly-once
charges remain untouched.  No full-K, source-native `Phi`, whole-residual,
stationary, capacity, or full Suzuki closure claim is made.

## HANDOFF — External Audit

Independently replay the script and hashes, verify the one-arc branch, local
weight construction, outward error transport and strict one-arc scope.
