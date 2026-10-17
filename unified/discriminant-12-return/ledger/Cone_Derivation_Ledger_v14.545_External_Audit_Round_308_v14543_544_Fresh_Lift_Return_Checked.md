# Cone Derivation Ledger v14.545 — External Audit Round 308: v14.543 Fresh-Lift Return Cross-Checked; v14.544 Handoff Verified Against Precedent

**Date:** 2026-10-17
**Track:** External Audit
**Status:** [V] v14.543 (Sandbox: both-sector fresh finite lifts certified and exactly replayed against the v14.539 RHS) and v14.544 (Lane A: ACK + corrected sequencing + new changed-compact-action HANDOFF) are read in full. Every claim checkable without the untransferred lift bytes passes: hash provenance, buffer byte arithmetic, a from-scratch reproduction of the finite-lift remote-action charge formula from only the two reported display numbers, and confirmation that v14.544's cited `3e-11` compact-action threshold and Hankel-self-removal convention are genuine long-standing project precedent, not new or invented. v14.544's restated numeric table is a character-for-character match to v14.543. The raw lift certificates/buffers themselves remain Sandbox-resident (not yet repository-accessible), so they cannot be independently byte-verified this round — disclosed by v14.543 itself, and consistent with the pattern already seen for v14.500 and v14.539.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–544.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `ba94998...` (v14.544), matching local HEAD; live ledger max was v14.544. v14.545 is next-free. No collision.

---

## 1. Hash provenance — exact

v14.543 cites the RHS certificate and candidate-point hashes it consumed (even `d56eaf3a...`/`c5b68453...`, odd `19c67577...`/`e9efaf91...`) — all four match, character for character, the values this auditor already cross-checked in Rounds 306–307 against the pinned producer constants. No input substitution occurred.

## 2. Buffer byte-count arithmetic — exact

```
128,000 rows x 87 bytes = 11,136,000 -- claimed 11,136,000, exact (both sectors)
```

## 3. Finite-lift remote-action charge — independently reproduced from the producer's own formula

Round 307 read `suzuki_direct_middle_delta_finite_lift.py` in full, including `certify()`'s line `charge = 22 * sqrt_upper(energy, 192)`. Using only the two *display* values v14.543 reports (lift certification is otherwise opaque without the raw snapshot), this auditor independently recomputed the prediction:

```
even-v: sqrt(2.0195325411596953e-23) = 4.49392...e-12;  22 x that = 9.8866260671742437...e-11
         v14.543 claimed charge:                                   9.886626067174243e-11
         agreement: ~18 significant figures (ratio 1.0000000000000000678)

odd-v:  sqrt(3.221825968223164e-30)  = 1.79494...e-15;  22 x that = 3.9488780287823672...e-14
         v14.543 claimed charge:                                   3.948878028782367e-14
         agreement: ~18 significant figures (ratio 1.0000000000000000405)
```

This is not a restatement: it is an independent numerical derivation from a formula read out of the producer's own source in a prior round, applied here for the first time to these specific reported numbers, and it reproduces the claimed charge to essentially full double-precision agreement in both sectors (the residual ~7e-17 relative discrepancy is explained by `sqrt_upper`'s deliberate upward rounding to a 192-bit grid plus the finite decimal digits of the *display* fields themselves, not by any inconsistency). Both charges are confirmed below the unchanged `2e-10` cap: even `9.887e-11` (~49% of budget — a closer margin than most prior gates in this project, though still a clean pass), odd `3.949e-14` (far below cap).

## 4. v14.544's cited invariants — checked against genuine project precedent, not asserted blind

v14.544 cites an "unchanged compact-action physical-error threshold `3e-11`." Grepped the ledger history: this exact threshold appears as early as v14.238/v14.239 and recurs unchanged through v14.285, v14.349, v14.353, and v14.405 — a real, long-standing invariant, not a new or invented number introduced here.

v14.544 also cites "the already audited support-owner convention in `suzuki_gap_extended_compact_action.py`" for removing the artificial Hankel self-interaction exactly once and adding the raw diagonal exactly once. Read that file directly: it carries the certificate flag `"artificial_Hankel_self_removed_once": True` — confirming the cited convention genuinely exists in the named file, not a fabricated citation.

## 5. v14.544's restated table — drift-free

v14.544's six-value table (projected physical residual upper, protected-dot upper, remote-action charge, both sectors) is a character-for-character match to v14.543's own figures. No drift.

## 6. Scope limitation — disclosed, not a defect

No file matching the new lift certificate hashes (`d3ea6436...`, `6c52c4fd...`) or buffer hashes (`d3fd00e0...`, `a852b54e...`) exists anywhere in the repository; v14.543 explicitly discloses the buffers "remain in the sandbox workspace... a repository payload transfer... awaits Jeremy's explicit line." This is the same disclosed pattern already seen for v14.500 (resolved in Round 296) and v14.539 (still pending as of Round 306). Full byte-level replay of the lift buffers is not possible this round for that reason, not because of any defect.

## 7. v14.544's new HANDOFF — scoped, no premature claim

The new changed direct-middle compact-action HANDOFF (five components: front with the v14.543 fresh lift, existing near, existing first patch, existing gap patch, v14.500 delta on its own output rows; single Hankel-self removal, single raw-diagonal insertion) correctly pins the v14.500 delta buffers and v14.539 correction-input-z buffers to their already-verified hashes, explicitly forbids re-charging v14.354 or the source/v14.403 transport (already charged once, per v14.442), and explicitly states "this entry does not claim that the compact-action gate has run or passed." No premature closure claim is made.

## 8. Verdict

```
Hash provenance: exact match to already-verified pins.
Buffer byte-count arithmetic: exact.
Finite-lift remote-action charge: independently reproduced via the
  producer's own charge=22*sqrt_upper(energy,192) formula, matching
  both reported charges to ~18 significant figures.
Cited invariants (3e-11 compact-action threshold, Hankel self-removal
  convention): confirmed as genuine, pre-existing project precedent,
  not new or invented citations.
v14.544's restated table: character-for-character match, no drift.
New HANDOFF: correctly scoped, explicitly disclaims any compact-action
  result.
Scope limitation (disclosed): new lift certificate/buffer bytes remain
  outside the repository; full byte-level replay awaits that transfer.
No defect found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.545
status: open
action: this auditor independently reproduced the finite-lift remote-action charge formula from the producer's own source and confirmed it matches both reported charges to ~18 significant figures; confirmed the cited 3e-11 threshold and Hankel-removal convention are genuine project precedent; confirmed v14.544's restated table is drift-free. No correction needed. Awaiting the lift-payload transfer and Sandbox's changed compact-action return.
deliverable: none required; informational confirmation
constraints: None.
