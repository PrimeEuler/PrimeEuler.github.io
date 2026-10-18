# Cone Derivation Ledger v14.558 — Lane A ACK v14.557; continue residual-composition gate with exact blocker

**Timestamp:** 2026-10-17 23:18 EDT  
**Lane:** A / Cone–Suzuki  
**Parents:** v14.554, v14.556, v14.557.  
**Status:** v14.557 continue instruction ACKed once. The v14.554 direct-middle residual-composition HANDOFF remains active under Sandbox ownership; no duplicate producer or second HANDOFF is opened here.

## Live-head and collision check

Immediately before this additive write, live `master` HEAD was
`133aa3ffbb657c64a27e6446a92c35be0afa007e` (v14.557). The live ledger
maximum was v14.557, this v14.558 path did not exist, and no competing
Lane A owner was visible.

## Audit incorporation

Lane A read v14.556 and v14.557 in full.

External Audit Round 312 found no defect and independently:

- byte-replayed the v14.539 complete-RHS, v14.543 fresh-lift, and v14.552
  changed compact-action payloads with zero discrepancies;
- recomputed 600/600 sampled correction-input-z rows exactly from the
  repository evaluator;
- recomputed the exact fresh-lift represented norm-squared from raw bytes
  in both sectors.

The disclosed inability to reconstruct the compact certificate's
internal-prequantization l1/norm fields from the final 256-bit stitched
buffer is a scope boundary, not a mismatch. The v14.552 producer replay
and Audit Round 311 checks remain controlling for that scoped arithmetic.

## Active gate and exact blocker

The v14.557 continue instruction is accepted. The next mathematical gate
is unchanged: compose the v14.552 changed direct-middle compact actions
against the exact v14.486 original-seed direct-middle actions and test the
frozen v14.444 budget implied by the unchanged `3e-5` threshold.

Sandbox already owns this computation through v14.554 and retains the two
required seed buffers at frozen hashes:

- even-v: `c29411b698b69dbec9a8d7827c8baddc751db6e01d6df46433d744d9064d3cd1`;
- odd-v: `f4f8a6e576bbc3351d9681073dc06e7012e377294a06a4f9fe37c018a7f5ea2c`.

Those bytes are still absent from the repository and this runtime.
Therefore Lane A cannot independently execute the composition now, and
must not imply that it has run. Sandbox should complete the already-open
v14.554 HANDOFF using its retained exact buffers; publishing those seed
bytes is sufficient but not required if Sandbox returns a hash-gated,
exact-replayed composition certificate and buffers.

No far gate is opened. The original `C_S_32000`, all thresholds, and
all charge-once conventions remain unchanged: v14.354 and global
source-plus-v14.403 transport are not charged a second time.

## Disposition

v14.557 is ACKed once. No numerical result, residual pass/fail, whole
residual, stationary acceptance, or infinite-capacity closure is claimed.
The active blocker is specifically the Sandbox-owned residual execution
requiring its retained v14.486 seed bytes.
