# Cone Derivation Ledger v13.534 — M16001 Q/N and remote transcript scaffold

**Status:** `[Audit]` implementation scaffold; **no theorem promotion**.

## Synchronization warning

This entry is drafted on branch `audit/m16001-qn-formation`. Its number is provisional until the live `master` ledger is rechecked immediately before merge. If another numbered ledger entry has landed, this file must be renumbered rather than colliding.

## Purpose

Continue the fail-closed rebuild required by v13.505/v13.510 after v13.533 closed the frozen-payload conversion subgate. The remaining arithmetic chain includes normalized Q/N formation, explicit remote Gram accumulation, and far-tail moment/envelope evaluation.

## New Q/N checker

Added:

`research-notes/suzuki_M16001_QN_formation_transcript.py`

and producer contract:

`research-notes/M16001_QN_formation_transcript_spec.md`.

The checker contains no accepted Q/N radius literal. Given emitted midpoint entries, absolute-product sums, and operation counts, it derives entrywise

`rad_ij = gamma_{k_ij} S_ij`,

then supplies the conservative block bound

`||B_QN||_2 <= ||B_QN_mid||_F + ||Rad_QN||_F`.

It fails closed if the required transcript is absent or malformed, or if the platform provides fewer than 64 long-double significand bits.

This does **not** yet close the Q/N gate: the actual M16001 producer still has to be instrumented, and every rounded normalization/scaling stage in the inspected formation path must be charged.

## Remote accumulation contract

Added:

`research-notes/M16001_remote_gram_transcript_spec.md`.

The explicit remote range is odd `n` from 16003 through 1999999 inclusive, exactly 991999 rows. The contract requires per-chunk absolute-product sums and operation counts plus a second accounting layer for the actual chunk-aggregation tree. It explicitly forbids replacing this with a hard-coded remote radius.

## Audit consequence

No theorem-level endpoint is asserted here. Certified status remains

`ind_{<=0}(A_even(1)) <= 4`,

`ind_{<=0}(A_{a=1}) <= 6`.

The next implementation obligation is to locate and instrument the exact code path that produces the normalized Q/N block used by the M16001 seven-plane replay. Only after that emitted transcript is CI-executed and its complete rounded formation path is audited may the Q/N arithmetic gate be marked closed.
