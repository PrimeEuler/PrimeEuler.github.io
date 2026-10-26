# Cone Derivation Ledger v14.905 - Sandbox addendum resolving Audit R356's two disclosures on v14.901

**Date:** 2026-10-26. **Lane:** Sandbox (little Euler).
**Parents:** v14.901 (far-coefficient return), v14.903 (External
Audit Round 356). **Status:** both of R356's disclosed items are
addressed below - the first resolved completely (a reporting
ambiguity in the sandbox's own summary line, no numerical
discrepancy), the second narrowed and restated precisely.
**Collision check:** immediately before writing, live master
HEAD is this entry's own payload commits (tip
`34fc9244188c57b110ddd756affd90971d3805ef`); v14.905 next free.
No v14.901 witness file is modified; Lane A's v14.902 hash
freeze is untouched.

## 1. The nU channel-check "intercept discrepancy" - resolved

R356 reported: its independent two-parameter OLS fit of the
even-sector nU block means against Lambda = ln ln(n/4) gives
slope 1.77246 and intercept -4.367, while TASK2.md's one-line
summary ("slope 1.77320, gamma_U = 0.014, rms 0.0008") could
not be reconciled with that intercept.

Resolution: the TASK2.md line quotes a THREE-parameter free
fit (fit_blocks.py; model nU = K - beta*Lambda + gamma/ln n -
the script's sign convention prints beta negative). Its exact
values, even sector: K = -4.37028, slope 1.77320,
gamma = +0.01402, rms 0.00078. The quoted "gamma_U = 0.014" is
the coefficient of the 1/ln n term, NOT an intercept, and the
summary line omitted K entirely. The auditor's two-parameter
intercept -4.367 matches K = -4.37028 to 0.003 (the residual
difference is exactly the gamma/ln n term their fit does not
carry), and their slope matches to 0.04%. There is no
numerical discrepancy; the ambiguity was in the sandbox's
one-line reporting, corrected here. Odd sector, same fit:
K = -4.27336, slope 1.74573, gamma = -0.37081, rms 0.00066
(analytic pi*W_0/2: 1.77933 even / 1.77769 odd).

## 2. The private-evaluator limitation - narrowed, restated

R356 disclosed that it could not regenerate the raw block
means / moments from first inputs because the producer scripts
import workspace modules and read workspace data. With this
entry the generation code and the pinned source are deposited
in `payloads/r356_followup_v14_905/`:

- sandbox_region23_evaluator.py -
  sha256 2492b1b8dade5ee290153c9c59db80b6d58f3cf4fa3911994bfd22c89eb03727
- whole-source-affine.json (the hash-pinned seed source;
  byte-identical to the far producer's copy) -
  sha256 6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6
- suzuki_direct_middle_changed_compact_action.py (compact-side
  module used by the Task 3 evaluator) -
  sha256 7784532512ea8a9e6c5bdb3728bb52ca7af281b6da97f076b17057f39885eeb2

Residual limitation, stated plainly: the far BANK data itself
(channel pickles and composed buffers in the workspace far585
tree, ~11 GB) is not in the repository, so a byte-level
regeneration of the block means from raw bank inputs remains
workspace-bound. What the repo now supports is: full
inspection of the exact generation code and pinned source,
plus R356's already-completed verification of every derived
quantity from the deposited JSON intermediates. Depositing
the bank tree is a size decision left to the project owner.

**Flags:** `nU_discrepancy=RESOLVED_reporting_ambiguity`;
`evaluator_code=DEPOSITED`; `bank_data_in_repo=false`;
`v14.901_witnesses=UNMODIFIED`; `far_tail_touched=false`.
