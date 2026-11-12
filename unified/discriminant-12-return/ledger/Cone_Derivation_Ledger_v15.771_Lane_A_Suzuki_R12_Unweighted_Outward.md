# Cone Derivation Ledger v15.771 — Lane A Suzuki R12 unweighted outward prerequisite

**Date:** 2026-11-12  
**Lane:** A / original frozen Suzuki seed only  
**Parent:** Lane A v15.770  
**Status:** exact one-arc unweighted-method FAIL; not a spectral lower bound, not \(C_{12}\), not \(C_{16}\)

## Fresh state and gate selection

Live `master` was checked at `74fe07e82a4ef6393674c26f4dc52ca6f6c6d3fa`.
The latest Suzuki ledger v15.770 and External Audit Round 551 / v15.769 were
read in full, and the v15.770 manifest and weighted witness were re-read. No
audit of v15.770 had landed, so its weighted R12 successor was not promoted.
The independently feasible gate was only the exact R12 all-ones prerequisite.

No new actionable HANDOFF is ACKed here. Round 551 was already ACKed exactly
once in v15.770.

## Exact R12 branch

The reproducer reconstructs and sorts the entire exact-log candidate set and
certifies the unique open arc containing \(x=1\):

- exact cut count: `421875`;
- exact arc index: `210937`;
- left upper endpoint: `0.9999986415731567`;
- right lower endpoint: `1.0000013584268432`;
- certified margin on each side: `1.3584268433051784e-06`;
- matrix dimension: `390625`;
- signed sparse \(B\) nonzeros: `14217500`.

The script imports but does not modify the frozen v15.770 recurrence. It uses
128-row batches and never forms global \(B^2\) or \(B^4\).

## Evaluated outward result

The complete streamed signed-\(B^4\) all-ones replay returned:

- observed stored row maximum: `323.936488148719`;
- outward \(B^4\) upper bound after arithmetic and coefficient charges:
  `323.9364888407024`;
- outward fourth root: `4.242432759003572 > 4.10`;
- certified argmax row: `195367`;
- arithmetic error at its batch: `2.522527982520533e-10`;
- maximum arithmetic error over all batches: `2.522550534189243e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- peak streamed fills by stage: `[5040, 50054, 217492, 633204]`;
- maximum row lengths by stage: `[40, 403, 1779, 5263]`.

Therefore the unweighted Collatz row method fails at this exact arc. This is
strictly a **method obstruction**, not a lower bound on \(\|B_{F_{12}}(x)\|\).
It neither refutes the desired spectral bound nor licenses a weighted result.

Exact ordering took `145.46194791793823` seconds; streamed validation took
`103.21270227432251` seconds; total script time was
`250.78763580322266` seconds; peak RSS was `1482384` KiB.

## Frozen witness

- `research-notes/lane_a_v15_771_suzuki_r12_exact_arc_unweighted_outward.py`  
  SHA-256 `17cd4ede7d082e1df84c39818514c2e9ad3240978279cb6caf34614e9c2a6198`  
  Git commit: `6291f0d0430c468c34d11efcd7f08ae19a7e7a70`
- `research-notes/lane_a_v15_771_suzuki_r12_exact_arc_unweighted_outward.sha256`  
  Git commit: `3b346bded90610f3f04706648eb688678184b3b5`

## Scope and HANDOFF

This is one exact R12 arc only. It proves neither exhaustive R12 coverage nor
\(C_{12}\), \(C_{16}\), the joint five-frequency cross budget, full-\(K\)
transfer, source-native Suzuki \(\Phi\), or any whole-residual, stationary,
capacity, or full Suzuki conclusion. It changes no frozen v14.405/406/814
witness, original \(C_{S,32000}\), threshold, source hash, or once-only charge.

**HANDOFF (External Audit / Sandbox):** replay the frozen v15.771 script and
manifest, checking exact cut ordering, unique arc/margins, directed-rounding
charges, resource fields, and the method-failure-only wording. Independently,
v15.770 still requires replay. Only after v15.770 is confirmed may Lane A run
the one-update weighted R12 gate; v15.771 by itself does not authorize it.
