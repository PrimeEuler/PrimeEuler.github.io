# Cone Derivation Ledger v15.842 — Lane A Suzuki R4 streamed exact-support scaling

**Date:** 2026-11-12 19:26 EST.  
**Track:** original frozen Suzuki seed only.  
**Status:** rigorous two-transition R4 method PASS and resource measurement; not `C_4`, not `C_16`, and not a full-Suzuki closure.

## Fresh state and Round 562 ACK

Live `master` immediately before this gate was
`5f97b8c4492612a2f51d02e5a5bf298e48646a59`.  External Audit Round
562/v15.836 at `a52ae8983676c8de9c2be0744429b1b3d1086d14` was read in full.
Its actionable HANDOFF is ACKed exactly once here.  Round 562 independently
replayed v15.823 from both repository root and `research-notes/`, reproduced
every exact-support and outward field, found no correction, and explicitly
authorized this memory-bounded R4 comparison.  Fresh collision checks found
v15.842 and all three target paths free.

## Gate and arithmetic

The reproducer sets `R=4`, giving 6,561 rows, 199,260 stored matrix entries,
and the exact v15.650 partition of 8,019 arcs.  It locates the unique `x=1`
anchor arc 4009 and tests the adjacent arcs 4008 and 4010.  It never forms a
global `B^2` or `B^4`: anchor weight, direct `B_1^4`, and all five signed words
are evaluated in 64-row batches with the audited binary64 product/addition and
coefficient-error envelopes.

The exact crossed-corner construction gives 102 affected word/aggregate
positions for each transition.  Naive subtraction instead stores 7,803/7,768
entries because independently evaluated mathematically constant coefficients
leave residues up to `5.551115123125783e-16`.  No threshold defines support;
the 102-entry support is combinatorial and the unchanged-entry residues are
diagnostic only.

The streamed anchor weight has SHA-256
`466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`
and condition ratio `25.619807022162554`.

## Rigorous outward results

| neighbor | crossed label | direct fourth root | signed-factorized fourth root | direct seconds | total factorized seconds |
|---:|---|---:|---:|---:|---:|
| 4008 | `(-3,3,0,4)` | 3.6324928325057364 | 3.6324928325371895 | 1.16967 | 1.73446 |
| 4010 | `(3,-3,0,-4)` | 3.6324928325053967 | 3.6324928325360655 | 1.07717 | 1.77835 |

Both direct and factorized outward values pass the unchanged `<4.10` method
target.  The corresponding factorized fourth-power bounds are
`174.10813526889217` and `174.10813526867665`, below `4.10^4=282.5761`.

## Cached-anchor resource result

For an all-arc row-block sweep, the current `B_0^4` block is already present;
the per-transition work is the four mixed update words, not reconstruction of
the anchor word.  Timing those components separately gives:

| transition | anchor-word seconds | four update-word seconds | update/direct ratio | total factor/direct ratio |
|---:|---:|---:|---:|---:|
| 4009→4008 | 1.11648 | 0.52036 | 0.44488 | 1.48286 |
| 4009→4010 | 1.14121 | 0.53671 | 0.49826 | 1.65094 |

Thus the exact-support update itself is already cheaper than direct
recomputation at R4—about 44.5%–49.8% of direct time—although a one-off
factorized evaluation remains slower if it must also rebuild the anchor.  The
localization is visible in peak fill: on the left transition `D B_0^3` uses
stage counts `[40,367,1498,3879]`, while direct `B_1^4` uses
`[2433,22016,74361,155066]`.

This validates the cached-block architecture at one R4 anchor.  It does not
show that 8,019 R4 transitions, much less 1,257,795 R16 transitions, fit the
runtime budget; it provides no sublinear grouping and no global maximum.

## Frozen witness and strict scope

- `research-notes/lane_a_v15_842_suzuki_r4_streamed_exact_support_scaling.py`
- `research-notes/lane_a_v15_842_suzuki_r4_streamed_exact_support_scaling.sha256`
- script SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- audited v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- script commit: `26eb05d073a075bbe2ef47697c4d7f9c485e56e8`
- manifest commit: `2e5c0e79f89766324a378c3a8fb19ecc6d0c9fd1`

No all-arc R4/R16 certificate, spectral lower bound, joint five-frequency
budget, full-K transfer, source-native `Phi`, whole-residual, stationary, or
capacity claim is made.  Original v14.405/406 finite-plus-gap PASS, v14.814 far
FAIL, `C_S_32000`, thresholds `3e-5`/`.002`, source hashes, and exactly-once
charges remain frozen unchanged.

**HANDOFF to independent External Audit:** replay the two R4 transitions,
verify exact support, batch arithmetic, weight hash, and the separation between
cached-anchor and update-only timings.  If confirmed, the next concrete Suzuki
gate is a bounded multi-transition R4 row-block sweep to measure whether the
current block can be updated in place across successive exact cuts without
fill or arithmetic allowance accumulating beyond the certified margin.
