# Cone Derivation Ledger v15.677 — Lane A Suzuki R5 adaptive weight-chart window

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.675; External Audit Round 539/v15.676  

## Fresh state, collision check, and audit ACK

External Audit Round 539/v15.676 was read in full. Its actionable HANDOFF is
ACKed exactly once here. It independently reproduces v15.675, including the
five-arc passing component, the two immediate fixed-weight boundary failures,
the full R5 exact cut-ordering checks, and the frozen SHA-256; it requires no
correction and directs an adaptive chart-count/runtime benchmark.

Before the reproducer write, live `master` was
`76153525dd0fc3bb89724321991c25458a328114`. Two independent entries had used
`v15.676` (Round 539 and a gravity entry); neither is modified here. Searches
found no existing `v15.677`, `v15.678`, or `v15.679`, so the next-free Suzuki
slot was selected as `v15.677`. Immediately before the hash write, live
`master` was the new reproducer commit
`eb85bd842e967e1b28dd1597afd9e45ae24fcc42`, with no competing v15.677 write.
The frozen hash commit is `e1f9b7d99afe82fc3a6947f589bde8a085b75d26`.

## Deterministic adaptive gate

The script first certifies the complete ordering of all 17,303 R5 cut arcs
with the audited exact-log interval machinery. Every tested binary64 midpoint
is proved to lie strictly inside its intended exact cut arc with the audited
margin.

On the fixed 33-arc window 8635 through 8667, the deterministic greedy rule is:

1. At the first uncovered arc, construct `B`, `B^2`, and `B^4`.
2. Recompute a positive weight by 40 normalized power steps on `|B^4|`.
3. Apply the audited outward weighted Collatz-Wielandt enclosure at the anchor.
4. Freeze that weight and extend rightward until the first certified failure.
5. Restart at that failed arc.

The unchanged target is `4.10^4 = 282.5761`. A failed extension is only a
failure of that frozen weight, not a spectral lower bound.

## Reproducible result

All 33 arcs were individually certified by seven charts. No locally recomputed
anchor failed. The chart intervals and widths are:

| anchor | last pass | width | anchor outward fourth root |
|---:|---:|---:|---:|
| 8635 | 8635 | 1 | 3.4441371951557507 |
| 8636 | 8645 | 10 | 3.4442041448795364 |
| 8646 | 8650 | 5 | 3.443589576353556 |
| 8651 | 8653 | 3 | 3.443313840589908 |
| 8654 | 8654 | 1 | 3.443732188423357 |
| 8655 | 8662 | 8 | 3.4437443831235646 |
| 8663 | 8667 | 5 | 3.4435567563883476 |

The run used 39 outward arc evaluations and 238.68443274497986 seconds on the
current single-thread runtime. The widths `1,10,5,3,1,8,5` show that chart
transport is strongly anchor- and direction-dependent; v15.675's five-arc
width cannot be used as a uniform-spacing estimate.

A direct proportional orientation from this window would require about 20,450
arc evaluations and roughly 35 serial hours to cover all R5 arcs, but this is
explicitly **not** a certified whole-R5 chart count or runtime bound. More
importantly, direct `B^4` construction at R16 remains resource-prohibitive at
the v15.644 scale, so this benchmark validates the local atlas mechanism while
also showing that an unmodified exhaustive R16 implementation is not yet a
resource-effective proof.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_677_suzuki_r5_adaptive_weight_chart_window.py`
- SHA-256:
  `d53997f31224ac5af93d4a8ff919e80642563e6d211d22431bbaf55bd34700f9`
- manifest:
  `research-notes/lane_a_v15_677_suzuki_r5_adaptive_weight_chart_window.sha256`

## Scope and next gate

This certifies only the 33 stated R5 arcs. It is not C5 or C16, and it does not
promote the sampled runtime orientation to a whole-radius certificate. No
full-K, source-native Phi, whole-residual, stationary, capacity, or physical
spectral conclusion is drawn.

The next resource gate is a deterministic stratified set of R5 windows away
from `x=1`, measuring whether every locally recomputed anchor passes and the
distribution of chart widths. In parallel, a viable C16 route must avoid
explicit global `B^4` materialization, for example by certifying weighted
four-step applications or an update-aware factorized bound. Independent audit
is required before using this benchmark downstream.

HANDOFF
target: external-audit, sandbox
parent: v15.677
type: suzuki-adaptive-weight-chart-benchmark
status: actionable
action: independently replay the frozen reproducer; verify full R5 cut ordering and midpoint margins, all seven local weight hashes, the 33-arc cover with widths 1/10/5/3/1/8/5, 39 evaluations, and the strict no-C5/no-C16 scope; then assess a stratified-window or factorized-application next gate.
deliverable: independent audit of v15.677 adaptive exact-cut R5 chart benchmark.
