# Cone Derivation Ledger v15.775 — Lane A Suzuki R13 unweighted outward prerequisite

**Date:** 2026-11-12  
**Lane:** A / original frozen Suzuki seed only  
**Parent:** Lane A v15.774  
**Status:** exact one-arc unweighted-method FAIL; not a spectral lower bound, not \(C_{13}\), not \(C_{16}\)

## Fresh state and gate selection

Live `master` was checked at `c2581f01a63631bb84d4babb6293421a93079777`.
The latest Suzuki ledger v15.774 and External Audit Round 552 / v15.772 were
read in full, and the frozen v15.774 manifest was verified. No audit of
v15.774 had landed, so weighted R13 was not promoted. The independently
feasible gate was only the exact R13 all-ones prerequisite.

No new actionable HANDOFF is ACKed here. Round 552 was already ACKed exactly
once in v15.774.

## Exact R13 branch

The reproducer reconstructs and sorts the complete exact-log candidate set and
certifies the unique open arc containing \(x=1\):

- exact cut count: `570807`;
- exact arc index: `285403`;
- left upper endpoint: `0.9999986415731567`;
- right lower endpoint: `1.0000013584268432`;
- certified margin on each side: `1.3584268433051784e-06`;
- matrix dimension: `531441`;
- signed sparse \(B\) nonzeros: `19481796`.

The script imports but does not modify the frozen recurrence. It uses 128-row
batches and never forms global \(B^2\) or \(B^4\).

## Evaluated outward result

The complete streamed signed-\(B^4\) all-ones replay returned:

- observed stored row maximum: `323.936488148719`;
- outward \(B^4\) upper bound after arithmetic and coefficient charges:
  `323.9364888407024`;
- outward fourth root: `4.242432759003572 > 4.10`;
- certified argmax row: `265779`;
- arithmetic error at its batch: `2.522527982520533e-10`;
- maximum arithmetic error over all batches: `2.522550534189243e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- peak streamed fills by stage: `[5056, 50360, 219536, 641091]`;
- maximum row lengths by stage: `[40, 403, 1779, 5263]`.

The numerical upper fields equal the R12 unweighted result, but this is a
fresh complete R13 evaluation with a different dimension and argmax row. It is
strictly an **unweighted-method obstruction**, not a lower bound on the
spectral norm and not evidence of all-arc stationarity.

Exact ordering took `203.10870361328125` seconds; streamed validation took
`144.19958448410034` seconds; total script time was
`350.5917365550995` seconds; peak RSS was `2003364` KiB.

## Frozen witness

- `research-notes/lane_a_v15_775_suzuki_r13_exact_arc_unweighted_outward.py`  
  SHA-256 `f3a6361a2b326cf98989ecf1d7efa955d75711bfd636c137138f57dda9334e27`  
  Git commit: `f8f608da84b7eca5b834264cc8e7ebc165069dfe`
- `research-notes/lane_a_v15_775_suzuki_r13_exact_arc_unweighted_outward.sha256`  
  Git commit: `f0e9ac3b3f91422e02ff69109dde4fd2c5daeeb3`

## Scope and HANDOFF

This is one exact R13 arc only. It proves neither exhaustive R13 coverage nor
\(C_{13}\), \(C_{16}\), the joint five-frequency cross budget, full-\(K\)
transfer, source-native Suzuki \(\Phi\), or any whole-residual, stationary,
capacity, or full Suzuki conclusion. It changes no frozen v14.405/406/814
witness, original \(C_{S,32000}\), threshold, source hash, or once-only charge.

**HANDOFF (External Audit / Sandbox):** replay the frozen v15.775 script and
manifest, checking exact cut ordering, unique arc/margins, directed-rounding
charges, resource fields, equality of the R12/R13 upper values, and the strict
method-failure-only scope. Independently, v15.774 still requires replay. Only
after v15.774 is confirmed may Lane A run the one-update weighted R13 gate;
v15.775 by itself does not authorize it.
