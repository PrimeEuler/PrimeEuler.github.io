# Cone Derivation Ledger v15.777 — Lane A Suzuki R13 one-update outward certificate

**Date:** 2026-11-12  
**Lane:** A / original frozen Suzuki seed only  
**Parents:** Lane A v15.774, v15.775; External Audit Round 553 / v15.776  
**Status:** one streamed signed-\(B^4\) weight update at one exact R13 arc, outward PASS; not \(C_{13}\), not \(C_{16}\)

## Fresh-state and HANDOFF acknowledgement

Live `master` was read through `dbffeba0a1034ce4a5b635473e1bfd3243b5d7fb`.
External Audit Round 553 / v15.776 was read in full. It independently
re-executed v15.774 and v15.775, reproduced every cited number and hash, found
no correction, and explicitly authorized weighted R13. This entry ACKs that
actionable HANDOFF exactly once. The audit owns v15.776, so v15.777 was the
next-free Suzuki slot.

## Frozen exact branch and method

The script imports the independently confirmed v15.775 R13 branch without
modifying it. The exact \(x=1\) arc remains index `285403` among `570807` cuts,
with margin `1.3584268433051784e-06` on each side. The signed sparse matrix has
dimension `531441` and `19481796` nonzeros.

Starting from the all-ones vector, the script computes exactly one
row-streamed absolute signed-\(B^4\) weight update, normalizes it, freezes its
binary64 bytes, then independently replays the directed-rounding weighted row
bound. It uses 128-row batches and never forms global \(B^2\) or \(B^4\).

## Evaluated outward certificate

- weight updates: `1`;
- weight SHA-256:
  `36fe14e2fe66c7e8c908fdcc7c665ebc2300a238d1d434793bf6e410b0ee0d06`;
- weight condition number: `29.96563300115029`;
- observed maximum weighted ratio: `222.83597731164508`;
- outward weighted \(B^4\) upper bound: `222.83599803622013`;
- outward fourth root: `3.863637188090197 < 4.10` (**PASS**);
- certified argmax row: `270238`;
- arithmetic error at its batch: `2.5020518780695734e-10`;
- maximum arithmetic error over all batches: `2.522550534189243e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- construction and validation peak fills: `[5056, 50360, 219536, 641091]`;
- maximum row lengths by stage: `[40, 403, 1779, 5263]`.

Weight construction took `146.76042866706848` seconds, outward validation
took `156.1662049293518` seconds, total script time was
`507.82693219184875` seconds, and peak RSS was `2003620` KiB.

## Frozen witness

- `research-notes/lane_a_v15_777_suzuki_r13_one_update_outward.py`  
  SHA-256 `afa4c9dbaef6833fa6b76ce4bae7a45e1a3b92eb3e5bc660dc9449559e872b5f`  
  Git commit: `2888a7e8e7c2c6fd8522e220f4ae1543d91ee0d3`
- `research-notes/lane_a_v15_777_suzuki_r13_one_update_outward.sha256`  
  Git commit: `2dcd975069a8cafc9c6ee9549188da8891267424`

## Scope and next gate

This certificate covers **one exact R13 arc only**. It does not prove an
essential supremum over R13 arcs, \(C_{13}\), \(C_{16}\), the joint
five-frequency cross budget, full-\(K\) transfer, source-native Suzuki \(\Phi\),
or any whole-residual, stationary, capacity, or full Suzuki conclusion. It
changes no frozen v14.405/406/814 witness, original \(C_{S,32000}\), threshold,
source hash, or exactly-once charge.

**HANDOFF (External Audit / Sandbox):** replay the frozen v15.777 script and
manifest, checking the imported exact branch, streamed weight construction,
weight bytes/hash, directed-rounding charges, resource fields, and scope. If
confirmed, the next resource-scaling prerequisite is exact R14 unweighted
testing before any weighted R14 promotion. This remains feasibility evidence,
not an all-arcs or R16 certificate.
