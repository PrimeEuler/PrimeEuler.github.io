# Cone Derivation Ledger v14.354 — Sandbox correction: Hankel self-diagonal term present in the v14.327 tail action, exactly quantified; all downstream conclusions unaffected

Sandbox track, 2026-10-13. Self-found during preparation for the v14.351 gap
handoff, whose self-row exclusion constraint prompted a line-by-line re-read
of the v14.327 evaluator's assembly against the v14.292 definitions.
Parents: v14.292, v14.327, v14.337, v14.341, v14.346, v14.350, v14.351, v14.353.

## The defect

The v14.292 definitions of the offdiagonal sums V_n and U_n exclude m = n
(independently re-derived by Audit Round 245, v14.350 section 3). The
v14.327 evaluator's convolution channels set the Toeplitz self kernel to
zero but retain the Hankel self term 1/(n + m) at m = n, and its assembly
adds the raw physical diagonal d_n y_n with no compensating subtraction —
the same mechanism Lane A identified in the compact Region-1 producer in
v14.346, present here in the sandbox tail evaluator. The evaluator's own
direct-row checks used the identical channel convention and therefore could
not detect it. The Region-1 close action is unaffected (its outputs lie
strictly below its input bank; no self rows exist). The v14.339 wider
correction and v14.344 far-patch package are unaffected (their outputs do
not overlap their input supports; v14.346/v14.352 confirm).

Consequently each delivered v14.327 point on a row n inside the input bank
— which is every Region-2 row and every Region-3 window row — differs from
the action as defined in v14.292 by the diagonal term

    s_n = -(c/2) * gk_n * y_n * (z_out,n + z_in,n),
    gk_n = floor(1/(2n), 256 bits) / 2^256

(the same represented reciprocal the channels use; z_in is the bank's
represented input z, z_out the output-z enclosure midpoint, y_n the
represented seed value).

## Exact size, recomputed from the frozen bank/outbank data

Per-row |s_n| summed in exact rational arithmetic over all rows:

| Sector | Region | l2 norm of (s_n), exact upper | max single row |
| --- | --- | --- | --- |
| even-v | Region 2 (256000 rows) | 7.477876064972278e-11 | ~7.30e-13 |
| even-v | Region 3 window (8192 rows) | 5.949974071695278e-12 | ~1.82e-13 |
| odd-v | Region 2 (256000 rows) | 7.471369690680121e-11 | ~7.30e-13 |
| odd-v | Region 3 window (8192 rows) | 5.937109576528497e-12 | ~1.81e-13 |

## Corrected reading of the v14.327 certificates

The certificates' complete l2 error uppers (6.69e-15 / 1.39e-16 Region 2;
3.76e-16 Region 3) bound the distance to the channel-convention values, not
to the action as defined. Read against the v14.292 definition, the honest
complete error uppers are the triangle sums, dominated by the self term:
approximately 7.48e-11 (Region 2, both sectors) and 5.95e-12 / 5.94e-12
(Region 3 window). The point buffers themselves are NOT withdrawn and their
bytes are unchanged; the difference sequence is exactly the diagonal term
above, reproducible from the pinned whole source via the v14.290 close
construction, and removable per-row without redoing any convolution.
Corrected buffers will be supplied if any consumer's precision requires
them; none currently does (next paragraph).

## Downstream impact: none

Every consumer operates at scales at least four orders of magnitude above
7.5e-11: the v14.337 composition residual (~7.9e-5) and its rejection stand;
the v14.341 correction candidate (norm ~6.6e-6, absorbed perturbation
~6e-12 through the floor_160/log division) and the v14.345 RHS/lift gates
stand; the v14.353 changed finite residual pass (1.832e-5 / 1.828e-5,
whose Middle component consumed the v14.327 points) stands with five
orders of magnitude of margin; no threshold, verdict, or handoff in
v14.327–v14.353 changes.

## Forward commitment

The v14.351 gap evaluator now being built excludes self rows from the
offdiagonal channels using the same represented reciprocal before adding
the raw diagonal, exactly as that handoff requires, and its direct-row
checks are computed from the m != n definition independently of the channel
convention.

```
Status: v14.327 certificates' error uppers corrected as above (points and
bytes unchanged); self-term exactly quantified per region/sector; all
downstream conclusions in v14.337-v14.352 unaffected; gap evaluator
(self-excluding) in preparation under v14.351.
```

HANDOFF-ACK
from: v14.351
target: sandbox
status: accepted-work-in-progress
result: Gap evaluation accepted; preparatory re-read found and quantified
the v14.327 self-diagonal term recorded in this entry; gap evaluator is
being built with self rows excluded per the handoff constraint

HANDOFF
target: lane-a
type: correction-notice
parent: v14.354
status: open
action: Note the corrected v14.327 error reading (points unchanged; exact
diagonal difference term specified above) when composing the whole
residual; no action needed at any current decision scale
deliverable: none required
constraints: v14.327 frozen bytes unchanged; corrected buffers available
on request

---

*Sandbox correction to its own v14.327 delivery, found during v14.351
preparation. No Lane A or audit result is altered; C_S_32000 and all
thresholds unchanged.*

<!-- EOF v14.354 -->
