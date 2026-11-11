# Cone Derivation Ledger v15.668 — Lane A Suzuki R5 degree-four method obstruction

**Date:** 2026-11-11 08:13 America/New_York  
**Lane:** A, original frozen Suzuki seed only  
**Status:** exact/outward one-arc obstruction to the direct absolute-row `B^4` certificate

## Fresh state and authorization

The interrupted v15.667 publication was reconciled first.  Live master lacked
only its ledger, so the already evaluated R4 all-arc certificate ledger was
added at commit `8246f8f6cb0a382a3432dfa902dfd6b74776bdcc`.  No competing
v15.667 entry or later audit correction existed.

Immediately before this gate, live master was that v15.667 ledger commit and
`v15.668` was free.  Latest full independent audit remained Round 535/v15.666,
which confirmed v15.664-v15.665 without correction.  v15.667 remains pending
independent audit.  This entry ACKs the current distinct PRIMARY MISSION
continuation once; it does not claim an audit of v15.667.

## Frozen witness

Additive files:

- `research-notes/lane_a_v15_668_suzuki_r5_degree4_method_obstruction.py`
- `research-notes/lane_a_v15_668_suzuki_r5_degree4_method_obstruction.sha256`

Script SHA-256:

`6d4f32a9863a8ff3562c0ffb7299b0261c488ff598bb5e6d2893be1a84a3305a`.

The witness imports the independently audited v15.664 exact-rational interval
and IEEE error machinery.  It rebuilds and proves the full R5 ordering of all
17,303 v15.650 cuts, then selects the R5 arc containing the v15.667 R4
maximizer.  The certified midpoint is
`x=0.051440007557059575` (arc index 445).

At this midpoint it forms the physical signed matrices `B`, `B2=B@B`, and
`B4=B2@B2`.  To prove a lower enclosure for the absolute-row functional, it
uses the maximizing computed row and:

1. divides the binary64 row sum by `1+gamma(k4)` to get a lower bound for the
   exact row sum of the stored `B4` matrix;
2. subtracts the audited sparse-product error `r4`;
3. subtracts the audited coefficient perturbation `(m+E)^4-m^4`, with the
   unchanged `E=10^-9`.

## Evaluated obstruction

Replayed output:

```text
R5_CUTS 17303 ARC_INDEX 445 MIDPOINT 0.051440007557059575
MAX_EXACT_WORD_STATE_ERROR 1.0975516472542119e-16
NNZ 468996 3900197 32367291 ROW_LENGTHS 40 401 4107
OBSERVED_B4_ROW 295.26546248989615 OBSERVED_ROOT 4.145273237245092
ARITHMETIC_R4_ERROR 5.506236646669709e-11 COEFFICIENT_PERTURBATION 6.913525593247088e-07
CERTIFIED_B4_ROW_INTERVAL 295.2654617983539 295.2654631814384
TARGET4 282.5761 METHOD_OBSTRUCTION True
SECONDS 3.5550029277801514
NO_SPECTRAL_NORM_LOWER_BOUND
NO_C5_OR_C16_CONCLUSION
```

Therefore the exact absolute-row fourth-power functional at this single R5
arc satisfies

\[
 \|B_{F_5}(x)^4\|_\infty
 > 295.2654617983539
 > 4.10^4=282.5761.
\]

Consequently the direct positive-polynomial estimate

\[
 \|B_{F_5}(x)\|\le \|B_{F_5}(x)^4\|_\infty^{1/4}
\]

cannot certify the `4.10` target at R5, even before considering the other
17,302 arcs.  An exhaustive R5 run of this same functional is therefore not a
useful next gate.

## Strict interpretation

This is a **method obstruction**, not a spectral lower bound.  An induced
absolute-row norm can exceed the Hilbert-space spectral norm substantially.
Nothing here proves `C5 >= 4.10`, and nothing here supports or refutes
`C16 < 4.10`.

The direct R5 object also has 32,367,291 `B4` nonzeros on this arc and reached
about 0.84 GiB process high-water memory once the absolute row sum was formed.
That resource growth reinforces—but is not needed for—the exact method
obstruction.

The next viable Suzuki gate must retain more signed/operator cancellation:
for example a rigorously certified signed block enclosure, a higher-degree
polynomial evaluated without materializing dense powers, or an exact
adjacent-cut update with a proved spectral (not merely rank) control.  The
v15.650 rank-`<=160` fact alone remains insufficient.

## Scope fences

This entry concerns only the original frozen Suzuki five-frequency
commutator and only the direct R5 `B^4` absolute-row method.  It does not alter
v14.405/406, v14.814, `C_S_32000`, thresholds `3e-5` or `.002`, source hashes,
or exactly-once charges.  It proves no C16 bound, joint cross-budget result,
full-K transfer, source-native `Phi`, whole-residual, stationary, capacity, or
full Suzuki closure statement.

## HANDOFF — External Audit

Independently verify the frozen SHA-256, full R5 cut ordering, selected arc,
lower-row rounding direction, subtraction of sparse arithmetic and coefficient
errors, and the method-only interpretation.  Audit v15.667 separately before
promoting its R4 certificate.
