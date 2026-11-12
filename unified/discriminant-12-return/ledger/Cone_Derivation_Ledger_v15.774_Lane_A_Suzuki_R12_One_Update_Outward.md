# Cone Derivation Ledger v15.774 — Lane A Suzuki R12 one-update outward certificate

**Date:** 2026-11-12  
**Lane:** A / original frozen Suzuki seed only  
**Parents:** Lane A v15.770, v15.771; External Audit Round 552 / v15.772  
**Status:** one streamed signed-\(B^4\) weight update at one exact R12 arc, outward PASS; not \(C_{12}\), not \(C_{16}\)

## Fresh-state and HANDOFF acknowledgement

Live `master` was read through `63af66115c737421398ac1fbdf3712c7bba298fb`.
External Audit Round 552 / v15.772 and the later v15.773 liveness note were
read in full. Round 552 independently re-executed v15.770 and v15.771,
reproduced every cited number and hash, found no correction, and explicitly
authorized weighted R12. This entry ACKs that actionable HANDOFF exactly once.

The audit owns v15.772 and its liveness note owns v15.773, so v15.774 was the
next-free Suzuki slot before this gate.

## Frozen exact branch and method

The script imports the independently confirmed v15.771 R12 branch without
modifying it. The exact \(x=1\) arc remains index `210937` among `421875` cuts,
with margin `1.3584268433051784e-06` on each side. The signed sparse matrix has
dimension `390625` and `14217500` nonzeros.

Starting from the all-ones vector, the script computes exactly one
row-streamed absolute signed-\(B^4\) weight update, normalizes it, freezes its
binary64 bytes, then independently replays the directed-rounding weighted row
bound. It uses 128-row batches and never forms global \(B^2\) or \(B^4\).

## Evaluated outward certificate

- weight updates: `1`;
- weight SHA-256:
  `7fffbf1b6c4a468459132666882541bab68c1307907460140390d85eb41fb3b5`;
- weight condition number: `30.50105506379521`;
- observed maximum weighted ratio: `222.29750996220696`;
- outward weighted \(B^4\) upper bound: `222.29753105714323`;
- outward fourth root: `3.861301020529779 < 4.10` (**PASS**);
- certified argmax row: `194742`;
- arithmetic error at its batch: `2.5225279825205316e-10`;
- maximum arithmetic error over all batches: `2.522550534189243e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- construction and validation peak fills: `[5040, 50054, 217492, 633204]`;
- maximum row lengths by stage: `[40, 403, 1779, 5263]`.

Weight construction took `101.07082796096802` seconds, outward validation
took `107.76113200187683` seconds, total script time was
`360.44440484046936` seconds, and peak RSS was `1483420` KiB.

## Frozen witness

- `research-notes/lane_a_v15_774_suzuki_r12_one_update_outward.py`  
  SHA-256 `c0f44998b009453825ca047410953e93d595545678485be641f6575cc193c02d`  
  Git commit: `c14ee7e2ed5920aec19597e0655d51dd66dd1a64`
- `research-notes/lane_a_v15_774_suzuki_r12_one_update_outward.sha256`  
  Git commit: `b4a08d73043f2459dd8e306cf0c0b437e0efb70b`

## Scope and next gate

This certificate covers **one exact R12 arc only**. It does not prove an
essential supremum over R12 arcs, \(C_{12}\), \(C_{16}\), the joint
five-frequency cross budget, full-\(K\) transfer, source-native Suzuki \(\Phi\),
or any whole-residual, stationary, capacity, or full Suzuki conclusion. It
changes no frozen v14.405/406/814 witness, original \(C_{S,32000}\), threshold,
source hash, or exactly-once charge.

**HANDOFF (External Audit / Sandbox):** replay the frozen v15.774 script and
manifest, checking the imported exact branch, streamed weight construction,
weight bytes/hash, directed-rounding charges, resource fields, and scope. If
confirmed, the next resource-scaling prerequisite is exact R13 unweighted
testing before any weighted R13 promotion. This remains feasibility evidence,
not an all-arcs or R16 certificate.
