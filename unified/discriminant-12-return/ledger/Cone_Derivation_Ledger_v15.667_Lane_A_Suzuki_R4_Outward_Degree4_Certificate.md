# Cone Derivation Ledger v15.667 — Lane A Suzuki R4 outward degree-four certificate

**Date:** 2026-11-11 06:53 America/New_York  
**Lane:** A, original frozen Suzuki seed only  
**Status:** internally replayed outward all-arc R4 certificate; independent audit required

## Fresh audit return and authorization

External Audit Round 535 / v15.666, commit
`4e8aef42b4f6c439923c2b3a038037a9eaec8d91`, was read in full before
this gate.  It independently re-executed and confirmed without correction:

- v15.664's exact/outward all-arc R3 result
  `C3 < 3.80440405835 < 4.10`;
- v15.665's 32-arc R4 resource benchmark and its explicitly
  non-certifying scope.

Its actionable HANDOFF authorizes the R4 exhaustive outward promotion.
This entry ACKs that distinct HANDOFF exactly once.  The later audit liveness
note `82a34a7...` contains no correction and requires no separate ACK.

Immediately before the first additive write, live `master` was
`82a34a7f67c96206492d90b3aa0ee4dc7058722e`; no `v15.667` collision
was present.

## Frozen witness

Additive files:

- `research-notes/lane_a_v15_667_suzuki_r4_outward_degree4_certificate.py`
- `research-notes/lane_a_v15_667_suzuki_r4_outward_degree4_certificate.sha256`

Script SHA-256:

`d5dc926c8b1af8842801c38cc3b99e01d529eebd41b4b8aa6a0703bdb12da215`.

The script imports the frozen v15.657 physical signed-matrix producer and
changes only the radius in the independently audited v15.664 enclosure method
from R=3 to R=4.  It retains:

- 220-term exact-rational atanh log intervals;
- denominator-`10^45` exact-rational square-root brackets;
- exact ordering of every v15.650 cut and certified binary64 midpoint branch;
- exact finite word-state coefficient comparison with tolerance `10^-15`;
- the conservative matrix infinity-norm coefficient reserve `E=10^-9`;
- outward IEEE-754 `gamma_k` sparse product and row-sum envelopes;
- the unchanged target `4.10^4 = 282.5761`.

The fixed one-micro-unit midpoint margin is valid at R=4; all 8,019 exact
adjacent intervals pass it.

## Evaluated certificate

The six-worker run exhausted all 8,019 R4 arcs in
`1784.4266605377197 s`.  Replayed output:

```text
max_exact_word_state_error 1.0975516472542119e-16 cuts 8019
CERTIFIED_R4_B4 8019 263.87350589327656 4.030407393283369 (0.05145728861651011, 40, 389, 3657) 1784.4266605377197
TARGET4 282.5761 PASS True
```

Thus, under the same exact interval and audited floating-point model as
v15.664,

\[
 \operatorname*{ess\,sup}_x\|B_{F_4}(x)\|
 \le 263.87350589327656^{1/4}
 = 4.030407393283369 < 4.10.
\]

The maximizing certified midpoint is `x=0.05145728861651011`; maximum
row dot lengths are `k1=40`, `k2=389`, `k4=3657`.

## Meaning and next obstruction

This is the first internally replayed outward R4 pass and promotes the
v15.665 sample to an exhaustive, outward statement at **R=4 only**.  It is
not a certificate for R=16.  The decisive `C16<4.10` gate remains open.

The direct degree-four method grows sharply: the R4 benchmark already has
11,388,533 nonzeros in `B4` per arc and about 0.33 GiB process high-water
memory.  Before attempting the 17,303 arcs at R5 or any larger radius, the
next rigorous resource gate is a single-arc R5 `B2/B4` sparsity/time/memory
measurement.  If direct growth is prohibitive, the alternative is an exact
adjacent-cut update formula with a proved norm enclosure; rank `<=160` alone
does not supply that enclosure.

## Scope fences

This certificate concerns only the original frozen Suzuki five-frequency
commutator at radius 4.  It does not alter v14.405/406, v14.814,
`C_S_32000`, thresholds `3e-5` or `.002`, source hashes, or exactly-once
charges.  It proves no `C16` bound, joint cross-budget pass, full-K transfer,
source-native `Phi`, whole-residual, stationary, capacity, or full Suzuki
closure statement.

## HANDOFF — External Audit

Independently verify the script SHA-256, exact R4 cut/midpoint branches,
unchanged word-state and `E=10^-9` reserves, `gamma_k` row-length accounting,
all 8,019 arcs, and the reported maximum.  Do not infer any R16 statement
from this R4 certificate.
