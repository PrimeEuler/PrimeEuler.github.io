# Cone Derivation Ledger v15.845 — Lane A Suzuki R4 bounded in-place multi-transition sweep

**Date:** 2026-11-12 20:41 EST.  
**Track:** original frozen Suzuki seed only.  
**Status:** eight-transition R4 in-place method PASS with cumulative arithmetic charging; not `C_4`, not `C_16`, and not full Suzuki closure.

## Fresh state and ACKs

Live `master` immediately before this gate was
`742cc632cf2651eca5eec784c147a3c32ea454b1`.  External Audit Round
563/v15.843 (`d3039de159845b5115239228da654cc1560f75e3`) and the subsequent
v15.844 liveness entry (`742cc632cf2651eca5eec784c147a3c32ea454b1`)
were read in full.  The Round 563 actionable HANDOFF and the distinct v15.844
continue nudge are each ACKed exactly once here.  Round 563 independently
reproduced all exact v15.842 Suzuki fields, found no correction, and authorized
a bounded multi-transition R4 row-block sweep.  Fresh collision checks found
v15.845 and all three target paths free.

## In-place gate

Starting from the unique `x=1` R4 anchor arc 4009, the reproducer propagates
each 64-row `B^4` block across four exact cuts in each direction.  At every
transition it uses

```text
B_1^4 = B_0^4 + D B_0^3 + B_1 D B_0^2 + B_1^2 D B_0 + B_1^3 D,
```

retains the signed current block in memory, and charges prior arithmetic error,
all four new word errors, and five-term addition error.  The coefficient
perturbation envelope is refreshed for the reached matrix rather than summed
as if it were independent at every prior state.  Every reached state is also
recomputed directly, row-streamingly, as a validation comparator.  No global
`B^2` or `B^4` is formed.

The unchanged R4 anchor weight SHA-256 is
`466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`.

## Results

| direction/step | reached arc | exact `nnz(D)` | direct fourth root | propagated fourth root | cumulative arithmetic allowance | max entry discrepancy vs direct |
|---|---:|---:|---:|---:|---:|---:|
| left 1 | 4008 | 102 | 3.6324928325057364 | 3.6324928325371895 | 5.470506602157746e-10 | 8.881784197001252e-16 |
| left 2 | 4007 | 130 | 3.6324928325054490 | 3.6324928325825696 | 9.751580681364225e-10 | 1.1102230246251565e-15 |
| left 3 | 4006 | 126 | 3.6324928325054490 | 3.6324928326061700 | 1.3826362240525516e-9 | 1.3322676295501878e-15 |
| left 4 | 4005 | 102 | 3.7847849859229130 | 3.7847849859907990 | 1.7326661848904726e-9 | 1.3322676295501878e-15 |
| right 1 | 4010 | 102 | 3.6324928325053967 | 3.6324928325360655 | 5.470506602157747e-10 | 1.3322676295501878e-15 |
| right 2 | 4011 | 130 | 3.6324928325053967 | 3.6324928325620323 | 9.752317326406182e-10 | 1.3322676295501878e-15 |
| right 3 | 4012 | 126 | 3.6324928325053967 | 3.6324928325855130 | 1.3827098885567475e-9 | 1.3322676295501878e-15 |
| right 4 | 4013 | 102 | 3.7847849859229150 | 3.7847849859908007 | 1.7326609787672698e-9 | 1.3322676295501878e-15 |

All eight propagated outward values pass the unchanged `<4.10` method target.
The largest certified fourth-power upper value is `205.1940903907914`, still
below `4.10^4=282.5761`.  Exact support remains at most 130 entries here,
within the v15.650 uniform bound 160.

Arithmetic allowance grows across successive in-place updates, as it must, but
remains small over this bounded window.  The excess of propagated over directly
recomputed fourth-power bounds is at most `1.9310448351461673e-8`; this is an
outward-enclosure cost, not disagreement in the mathematical matrices.  The
binary64 blocks themselves agree to at most `1.3322676295501878e-15` entrywise.

Measured update-word time per transition was approximately 0.598–0.631 s.
These timings are empirical and system-dependent; they are not certified
invariants.  The exact supports, bounds, hashes, and error envelopes are the
reproducible mathematical fields.

## Scope and obstruction remaining

This validates in-place propagation across eight selected adjacent R4 arcs.
It does not certify any of the other 8,011 R4 arcs or any R16 arc.  In
particular, the observed four-step arithmetic growth cannot simply be linearly
extrapolated through 8,019 or 1,257,795 cuts: mixed-word norms and maximizing
rows may change.  A longer bounded sweep with periodic certified rebasing is
still required before committing resources to an all-arc R4 pass.

No spectral lower bound, `C_4`, `C_16`, joint five-frequency budget, full-K
transfer, source-native `Phi`, whole-residual, stationary, or capacity claim is
made.  Original v14.405/406 finite-plus-gap PASS, v14.814 far FAIL,
`C_S_32000`, thresholds `3e-5`/`.002`, source hashes, and exactly-once charges
remain frozen unchanged.

## Frozen witness and HANDOFF

- `research-notes/lane_a_v15_845_suzuki_r4_multitransition_inplace_sweep.py`
- `research-notes/lane_a_v15_845_suzuki_r4_multitransition_inplace_sweep.sha256`
- script commit: `0dfef34b6118c20e6a42d27dd61b4085abcff010`
- manifest commit: `b833d3bed47bf9f72a486b79f20fc3bf900386ab`
- script SHA-256: `cf33ea4bccca709a1535463090ace6c21d4cf2d303dd7c57e8c1072d870c9da7`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- audited v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`

**HANDOFF to independent External Audit:** replay all eight states, verify exact
cut bookkeeping, cumulative-error recurrence, direct comparators, and hashes.
If confirmed, the next concrete Suzuki gate is a longer R4 sweep with a fixed
periodic direct-rebase schedule, measuring the maximum enclosure cost and
runtime per certified arc block before considering exhaustive R4 coverage.
